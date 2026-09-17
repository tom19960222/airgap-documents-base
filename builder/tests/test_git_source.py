import io
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import common
from common import Manifest
from git_source import (
    JekyllRenderError,
    _discover_source_files,
    _rewrite_source_links,
    _rewrite_jekyll_links,
    _build_jekyll_registry,
    _peer_jekyll_registry,
    clean_hugo_shortcodes,
    extract_frontmatter_description,
    parse_jekyll_frontmatter,
    normalize,
    render_jekyll_template,
    validate_no_residual_template_syntax,
)
from normalize import to_markdown as html_to_markdown


class GitSourceTests(unittest.TestCase):
    def test_html_normalizer_preserves_markdown_hard_breaks(self):
        manifest = Manifest(
            name="html-test",
            collection="html-test",
            version="1.0",
            base_url="https://docs.example/",
            content_selector="div[role=main]",
        )
        result = html_to_markdown(
            '<html><title>Example</title><div role="main">'
            '<p>first<br>second</p>'
            '<pre># comment   \nvalue  </pre>'
            '</div></html>',
            "https://docs.example/index.html",
            manifest,
        )

        self.assertIsNotNone(result)
        _, body = result
        self.assertIn("first  \nsecond", body)
        self.assertIn("# comment   \nvalue  ", body)
        self.assertNotRegex(body, r"\n{3,}")

    def test_manifest_shortcode_profile_defaults_to_empty_for_compatibility(self):
        manifest = Manifest(name="test", collection="test", version="1.0.0")

        self.assertEqual(manifest.shortcode_profile, "")
        self.assertEqual(manifest.chart_version, "")

    def test_vault_secrets_operator_manifest_includes_chart_readme(self):
        manifest_path = (
            Path(__file__).resolve().parents[1]
            / "manifests"
            / "vault-secrets-operator-1.26.0.toml"
        )
        manifest = common.load_manifest(manifest_path)

        self.assertEqual(manifest.git_ref, "0522e930be76ea763c6611a130d44b7ef59182b0")
        self.assertEqual(manifest.chart_version, "2.7.0")
        self.assertEqual(manifest.docs_paths, ["README.md", "charts/README.md"])
        self.assertIn("charts/README.md", manifest.sparse_paths)
        corpus_dir = common.REPO_ROOT / "corpus" / "vault-secrets-operator" / "1.26.0"
        self.assertEqual(
            sorted(path.relative_to(corpus_dir).as_posix() for path in corpus_dir.rglob("*.md")),
            ["README.md", "charts/README.md"],
        )
        for page in corpus_dir.rglob("*.md"):
            self.assertIn('chart_version: "2.7.0"', page.read_text())

    def test_istio_shortcode_profile_renders_common_shortcodes_without_template_syntax(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary)
            (repo / "content/en/docs/images").mkdir(parents=True)
            (repo / "content/en/docs/images/diagram.svg").write_text("<svg />")
            content = """Before

{{< text syntax=yaml snip_id=example >}}
apiVersion: v1
kind: Demo
{{< /text >}}

{{< tabset category-name="platform" >}}
{{< tab name="One" category-value="one" >}}
One content
{{< /tab >}}
{{< tab title="Two" category-value="two" >}}
Two content
{{< /tab >}}
{{< /tabset >}}

{{< warning >}}
Read this warning.
{{< /warning >}}
{{< tip >}}A useful tip.{{< /tip >}}
{{< idea >}}A good idea.{{< /idea >}}
{{< quote >}}A useful quote.{{< /quote >}}
{{< image link="images/diagram.svg" caption="A diagram" width="100%" >}}
This is {{< gloss "term" >}}important text{{< /gloss >}}.
{{< text html >}}
{{</* image link="./example.svg" caption="Example" */>}}
{{< /text >}}
{{< future_feature version="1.25" >}}Future content{{< /future_feature >}}
{{/* hidden implementation note */}}
After
"""

            rendered = clean_hugo_shortcodes(content, repo, profile="istio")

            self.assertNotRegex(rendered, r"\{\{[<%]")
            self.assertNotIn("hidden implementation note", rendered)
            self.assertIn("```yaml\napiVersion: v1\nkind: Demo\n```", rendered)
            self.assertIn("**Tab: One**", rendered)
            self.assertIn("One content", rendered)
            self.assertIn("**Tab: Two**", rendered)
            self.assertIn("Two content", rendered)
            self.assertIn("> **Warning:**", rendered)
            self.assertIn("> **Tip:**", rendered)
            self.assertIn("> **Idea:**", rendered)
            self.assertIn("> **Quote:**", rendered)
            self.assertIn("![A diagram](images/diagram.svg)", rendered)
            self.assertIn("This is important text.", rendered)
            self.assertIn('[image link="./example.svg" caption="Example"]', rendered)
            self.assertIn('[future_feature version="1.25"]', rendered)

    def test_istio_github_shortcodes_use_immutable_application_commit_and_preserve_literals(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary)
            content = """[Tree]({{< github_tree >}}/samples/bookinfo?view=1#top)
[Blob]({{< github_blob >}}/pilot/pkg?tab=readme#part)
{{< github_file >}}/samples/bookinfo.yaml
{{< istio_release_url >}}
`{{< github_file >}}/literal.yaml`
```text
{{< github_tree >}}/literal
```
{{</* github_file */>}}
"""

            rendered = clean_hugo_shortcodes(content, repo, profile="istio")
            commit = "8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99"
            self.assertIn(
                f"[Tree](https://github.com/istio/istio/tree/{commit}/samples/bookinfo?view=1#top)",
                rendered,
            )
            self.assertIn(
                f"[Blob](https://github.com/istio/istio/blob/{commit}/pilot/pkg?tab=readme#part)",
                rendered,
            )
            self.assertIn(
                f"https://raw.githubusercontent.com/istio/istio/{commit}/samples/bookinfo.yaml",
                rendered,
            )
            self.assertIn(
                "https://github.com/istio/istio/releases/tag/1.24.0",
                rendered,
            )
            self.assertIn("`{{< github_file >}}/literal.yaml`", rendered)
            self.assertIn(
                "```text\n{{< github_tree >}}/literal\n```",
                rendered,
            )
            self.assertIn("[github_file]", rendered)
            self.assertNotIn("https://github.com/istio/istio/tree/main", rendered)

    def test_istio_site_routes_map_docs_and_mark_out_of_scope_links(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary) / "repo"
            source = repo / "content/en/docs/guide/source.md"
            source.parent.mkdir(parents=True)
            source.write_text("")
            manifest = Manifest(
                name="istio-1.24",
                collection="istio",
                version="1.24",
                shortcode_profile="istio",
                site_overrides={
                    "url": "https://istio.io",
                    "baseurl": "/v1.24",
                    "docs_prefix": "/docs",
                },
            )
            body = """[Docs](/docs/guide/?q=1#frag)
[Latest](https://istio.io/latest/docs/guide/#latest)
[Blog](/blog/2024/post?q=2#news)
`[Literal](/docs/guide/)`
```markdown
[Fenced](/docs/guide/)
```
"""

            rewritten = _rewrite_source_links(
                body,
                source,
                Path("guide/source.md"),
                repo,
                {
                    "content/en/docs/guide/index.md": "guide/index.md",
                    "content/en/docs/guide/source.md": "guide/source.md",
                },
                manifest,
            )

            self.assertIn("[Docs](index.md?q=1#frag)", rewritten)
            self.assertIn("[Latest](index.md#latest)", rewritten)
            self.assertIn(
                "[Blog](https://istio.io/v1.24/blog/2024/post?q=2#news)"
                " <!-- unresolved-site-link: route=/blog/2024/post -->",
                rewritten,
            )
            self.assertIn("`[Literal](/docs/guide/)`", rewritten)
            self.assertIn("```markdown\n[Fenced](/docs/guide/)\n```", rewritten)

    def test_istio_description_is_preserved_and_falls_back_to_empty_body(self):
        self.assertEqual(
            extract_frontmatter_description(
                "---\ntitle: Section\ndescription: A useful section.\n---\n"
            ),
            "A useful section.",
        )
        with TemporaryDirectory() as temporary:
            temp_path = Path(temporary)
            repo = temp_path / "raw" / "istio" / "1.24" / "repo"
            source = repo / "content/en/docs/guide/_index.md"
            source.parent.mkdir(parents=True)
            source.write_text(
                "---\n"
                "title: Guide\n"
                "description: A useful section.\n"
                "---\n"
            )
            manifest = Manifest(
                name="istio-1.24",
                collection="istio",
                version="1.24",
                source_type="git",
                repo_url="https://github.com/istio/istio.io",
                git_ref="3" * 40,
                docs_paths=["content/en/docs"],
                shortcode_profile="istio",
                preserve_description=True,
                source_url_template="{repo_url}/blob/{git_ref}/{path}",
            )

            with patch.object(common, "REPO_ROOT", temp_path), redirect_stdout(io.StringIO()):
                normalize(manifest)

            output = (temp_path / "corpus/istio/1.24/guide/_index.md").read_text()
            self.assertIn('description: "A useful section."', output)
            self.assertTrue(output.endswith("A useful section.\n"))

    def test_istio_boilerplate_and_include_reject_paths_outside_repository(self):
        with TemporaryDirectory() as temporary:
            temp_path = Path(temporary)
            repo = temp_path / "repo"
            repo.mkdir()
            boilerplates = repo / "content/en/boilerplates"
            boilerplates.mkdir(parents=True)
            (boilerplates / "base.md").write_text(
                "Boilerplate body\n\n{{< tip >}}Nested tip{{< /tip >}}\n"
            )
            (repo / "content/en/includes").mkdir(parents=True)
            (repo / "content/en/includes/local.md").write_text("Local include body\n")
            (temp_path / "outside.md").write_text("SECRET OUTSIDE\n")

            rendered = clean_hugo_shortcodes(
                """{{< boilerplate base >}}
{{< boilerplate ../outside >}}
{{< include "local.md" >}}
{{< include "../../outside.md" >}}
""",
                repo,
                profile="istio",
            )

            self.assertIn("Boilerplate body", rendered)
            self.assertIn("> **Tip:**", rendered)
            self.assertIn("Local include body", rendered)
            self.assertNotIn("SECRET OUTSIDE", rendered)
            self.assertNotRegex(rendered, r"\{\{[<%]")

    def test_generic_git_normalize_emits_manifest_app_version(self):
        with TemporaryDirectory() as temporary:
            temp_path = Path(temporary)
            repo = temp_path / "raw" / "cert-manager" / "1.14" / "repo"
            source = repo / "docs" / "index.md"
            source.parent.mkdir(parents=True)
            source.write_text("# Cert-manager\n\nDocument line.\n")
            manifest = Manifest(
                name="cert-manager-1.14",
                collection="cert-manager",
                version="1.14",
                app_version="1.14.7",
                chart_version="2.7.0",
                source_type="git",
                repo_url="https://github.com/example/cert-manager-website",
                git_ref="a" * 40,
                docs_paths=["docs"],
                source_url_template="{repo_url}/blob/{git_ref}/{path}",
            )

            with patch.object(common, "REPO_ROOT", temp_path), redirect_stdout(io.StringIO()):
                normalize(manifest)

            output = (temp_path / "corpus/cert-manager/1.14/index.md").read_text()
            self.assertIn('app_version: "1.14.7"', output)
            self.assertIn('chart_version: "2.7.0"', output)

    def test_generic_git_normalize_redacts_only_secret_shaped_slack_webhooks(self):
        with TemporaryDirectory() as temporary:
            temp_path = Path(temporary)
            repo = temp_path / "raw" / "example" / "1.0" / "repo"
            source = repo / "docs" / "index.md"
            source.parent.mkdir(parents=True)
            secret_url = (
                "https://hooks.slack.com/services/T00000000/B00000000/"
                "XXXXXXXXXXXXXXXXXXXXXXXX"
            )
            safe_url = "https://hooks.slack.com/services/WORKSPACE_ID/CHANNEL_ID/REDACTED_TOKEN"
            benign_url = "https://hooks.slack.com/services/xxx/yyy/zzz"
            source.write_text(
                f"# Example\n\nPlain: {secret_url}\n\n"
                f"[Slack]({secret_url})\n\n"
                f"Benign: {benign_url}\n"
            )
            manifest = Manifest(
                name="example-1.0",
                collection="example",
                version="1.0",
                source_type="git",
                repo_url="https://github.com/example/docs",
                git_ref="a" * 40,
                docs_paths=["docs"],
                source_url_template="{repo_url}/blob/{git_ref}/{path}",
            )

            with patch.object(common, "REPO_ROOT", temp_path), redirect_stdout(io.StringIO()):
                normalize(manifest)

            output = (temp_path / "corpus/example/1.0/index.md").read_text()
            self.assertEqual(output.count(safe_url), 2)
            self.assertIn(f"[Slack]({safe_url})", output)
            self.assertIn(benign_url, output)
            self.assertNotIn(secret_url, output)

    def test_kubernetes_default_shortcode_profile_preserves_existing_result(self):
        content = """Before
{{< note title="N" >}}
Body
{{< /note >}}
{{< tabs >}}
{{< tab name="One" >}}
A
{{< /tab >}}
{{< /tabs >}}
{{< latest-version >}}
After
"""

        self.assertEqual(
            clean_hugo_shortcodes(content, Path(".")),
            "Before\n\n\n> **Note (N):**\n>\n> Body\n\n\n\n\n\n**Tab: One**\n\n\nA\n\n\nv1.31\nAfter\n",
        )

    def test_unknown_shortcode_profile_fails_fast(self):
        with self.assertRaises(ValueError):
            clean_hugo_shortcodes("{{< future >}}", Path("."), profile="typo")

    def test_prometheus_operator_profile_resolves_refs_alert_and_preserves_literals(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary) / "repo"
            docs = repo / "Documentation"
            source = docs / "user-guides" / "source.md"
            source.parent.mkdir(parents=True)
            (source.parent / "same.md").write_text("# Same\n")
            (docs / "parent.md").write_text("# Parent\n")

            content = """[Same]({{< ref \"same\" >}})
[Parent]({{< relref \"parent\" >}})
[Anchor]({{< ref \"#ca-bundle\" >}})
{{< alert icon=\"👉\" text=\"Use the pinned release.\"/>}}
`{{< ref \"same\" >}}`
```markdown
{{< ref \"same\" >}}
{{< alert icon=\"👉\" text=\"literal\"/>}}
```
{{</* ref \"same\" */>}}
{{< future-widget value=\"kept\" >}}Future body{{< /future-widget >}}
"""

            rendered = clean_hugo_shortcodes(
                content,
                repo,
                profile="prometheus-operator",
                source_path=source,
            )

            self.assertIn("[Same](same.md)", rendered)
            self.assertIn("[Parent](../parent.md)", rendered)
            self.assertIn("[Anchor](#ca-bundle)", rendered)
            self.assertIn("> **Note:** 👉 Use the pinned release.", rendered)
            self.assertIn("`{{< ref \"same\" >}}`", rendered)
            self.assertIn(
                "```markdown\n{{< ref \"same\" >}}\n"
                "{{< alert icon=\"👉\" text=\"literal\"/>}}\n```",
                rendered,
            )
            self.assertIn("{{</* ref \"same\" */>}}", rendered)
            self.assertIn("[future-widget value=\"kept\"]", rendered)
            self.assertIn("Future body", rendered)
            normal = rendered.replace('`{{< ref "same" >}}`', "")
            normal = normal.replace(
                "```markdown\n{{< ref \"same\" >}}\n"
                "{{< alert icon=\"👉\" text=\"literal\"/>}}\n```",
                "",
            )
            normal = normal.replace('{{</* ref "same" */>}}', "")
            self.assertNotRegex(normal, r"\{\{[<%]")

    def test_prometheus_operator_nested_literals_restore_and_nul_fails_fast(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary) / "repo"
            source = repo / "Documentation" / "source.md"
            source.parent.mkdir(parents=True)
            (source.parent / "same.md").write_text("# Same\n")

            nested = '`{{</* ref "same" */>}}`'
            rendered = clean_hugo_shortcodes(
                nested,
                repo,
                profile="prometheus-operator",
                source_path=source,
            )
            self.assertEqual(rendered, nested)
            self.assertNotIn("\x00", rendered)

            with self.assertRaisesRegex(ValueError, "NUL"):
                clean_hugo_shortcodes(
                    "unsafe\x00content",
                    repo,
                    profile="prometheus-operator",
                    source_path=source,
                )

    def test_prometheus_operator_profile_resolves_refs_during_normalize(self):
        with TemporaryDirectory() as temporary:
            temp_path = Path(temporary)
            repo = temp_path / "raw" / "prometheus-operator" / "0.73.2" / "repo"
            docs = repo / "Documentation"
            source = docs / "user-guides" / "source.md"
            source.parent.mkdir(parents=True)
            (source.parent / "same.md").write_text("# Same\n")
            (docs / "parent.md").write_text("# Parent\n")
            source.write_text(
                "[Same]({{< ref \"same\" >}}) and "
                "[Parent]({{< ref \"parent\" >}})\n"
                "{{< alert icon=\"👉\" text=\"Pinned.\"/>}}\n"
            )
            commit = "f" * 40
            manifest = Manifest(
                name="prometheus-operator-0.73.2",
                collection="prometheus-operator",
                version="0.73.2",
                source_type="git",
                repo_url="https://github.com/prometheus-operator/prometheus-operator",
                git_ref=commit,
                docs_paths=["Documentation"],
                shortcode_profile="prometheus-operator",
                source_url_template="{repo_url}/blob/{git_ref}/{path}",
            )

            with patch.object(common, "REPO_ROOT", temp_path), redirect_stdout(io.StringIO()):
                normalize(manifest)

            rendered = (temp_path / "corpus" / "prometheus-operator" / "0.73.2" / "user-guides" / "source.md").read_text()
            self.assertIn("[Same](same.md)", rendered)
            self.assertIn("[Parent](../parent.md)", rendered)
            self.assertIn("> **Note:** 👉 Pinned.", rendered)
            self.assertNotIn("unresolved-source-link", rendered)
            self.assertNotRegex(rendered, r"\{\{[<%]")

    def test_same_repository_raw_and_bare_urls_are_pinned_without_touching_literals(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary) / "repo"
            source = repo / "docs" / "page.md"
            source.parent.mkdir(parents=True)
            source.write_text("")
            commit = "1" * 40
            manifest = Manifest(
                name="test",
                collection="test",
                version="1.0.0",
                source_type="git",
                repo_url="https://github.com/example/test",
                git_ref=commit,
            )
            body = """[Blob](https://github.com/example/test/blob/main/docs/a.md?raw=1#part)
[Tree](https://github.com/example/test/tree/master/docs?view=1#top)
[Raw](https://github.com/example/test/raw/main/docs/a.yaml?download=1#yaml)
[Raw host](https://raw.githubusercontent.com/example/test/master/docs/a.yaml?download=1#yaml)
[Root tree]: https://github.com/example/test/tree/main
[![Badge](https://img.shields.io/example)](https://github.com/example/test/blob/master/LICENSE)
[Nested query](https://viewer.example/?url=https://raw.githubusercontent.com/example/test/main/docs/schema.yaml)
[Install `tool`]: https://external.example/install
[^1]: keep the `Certificate` name intact
<https://github.com/example/test/blob/main/docs/auto.md?x=1#auto>
See https://github.com/example/test/tree/master/docs?view=2#bare.
[Ref]: <https://github.com/example/test/blob/main/docs/ref.md?x=1#ref> "Reference title"
https://github.com/other/test/blob/main/docs/cross.md
https://raw.githubusercontent.com/other/test/main/docs/cross.yaml
`https://github.com/example/test/blob/main/docs/inline.md`
```text
https://github.com/example/test/blob/main/docs/fenced.md
```
"""

            rewritten = _rewrite_source_links(
                body,
                source,
                Path("docs/page.md"),
                repo,
                {"docs/page.md": "docs/page.md"},
                manifest,
            )

            self.assertIn(f"/blob/{commit}/docs/a.md?raw=1#part", rewritten)
            self.assertIn(f"/tree/{commit}/docs?view=1#top", rewritten)
            self.assertIn(f"/raw/{commit}/docs/a.yaml?download=1#yaml", rewritten)
            self.assertIn(
                f"https://raw.githubusercontent.com/example/test/{commit}/docs/a.yaml?download=1#yaml",
                rewritten,
            )
            self.assertIn(f"[Root tree]: https://github.com/example/test/tree/{commit}", rewritten)
            self.assertIn(f"https://github.com/example/test/blob/{commit}/LICENSE", rewritten)
            self.assertIn(
                f"https://viewer.example/?url=https://raw.githubusercontent.com/example/test/{commit}/docs/schema.yaml",
                rewritten,
            )
            self.assertIn("[Install `tool`]: https://external.example/install", rewritten)
            self.assertIn("[^1]: keep the `Certificate` name intact", rewritten)
            self.assertNotIn("\x00SOURCE_LINK_LITERAL_", rewritten)
            self.assertIn(f"<https://github.com/example/test/blob/{commit}/docs/auto.md?x=1#auto>", rewritten)
            self.assertIn(f"https://github.com/example/test/tree/{commit}/docs?view=2#bare.", rewritten)
            self.assertIn(f"/blob/{commit}/docs/ref.md?x=1#ref> \"Reference title\"", rewritten)
            self.assertIn("https://github.com/other/test/blob/main/docs/cross.md", rewritten)
            self.assertIn("https://raw.githubusercontent.com/other/test/main/docs/cross.yaml", rewritten)
            self.assertIn("`https://github.com/example/test/blob/main/docs/inline.md`", rewritten)
            self.assertIn(
                "```text\nhttps://github.com/example/test/blob/main/docs/fenced.md\n```",
                rewritten,
            )

    def test_mutable_ref_allowlist_pins_dotted_refs_without_touching_tags(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary) / "repo"
            source = repo / "docs" / "page.md"
            source.parent.mkdir(parents=True)
            source.write_text("")
            commit = "2" * 40
            manifest = Manifest(
                name="test",
                collection="test",
                version="1.0.0",
                source_type="git",
                repo_url="https://github.com/example/test",
                git_ref=commit,
                mutable_refs=["release-1.2", "docs/v1.2"],
            )
            body = (
                "[Blob](https://github.com/example/test/blob/release-1.2/docs/a.md)\n"
                "[Tree](https://github.com/example/test/tree/docs/v1.2/docs)\n"
                "[Raw](https://github.com/example/test/raw/release-1.2/docs/a.yaml)\n"
                "https://raw.githubusercontent.com/example/test/docs/v1.2/docs/a.yaml\n"
                "See https://github.com/example/test/blob/release-1.2/docs/b.md.\n"
                "https://github.com/example/test/blob/v1.2.3/docs/tag.md\n"
            )

            rewritten = _rewrite_source_links(
                body,
                source,
                Path("docs/page.md"),
                repo,
                {"docs/page.md": "docs/page.md"},
                manifest,
            )

            self.assertIn(f"/blob/{commit}/docs/a.md", rewritten)
            self.assertIn(f"/tree/{commit}/docs", rewritten)
            self.assertIn(f"/raw/{commit}/docs/a.yaml", rewritten)
            self.assertIn(
                f"https://raw.githubusercontent.com/example/test/{commit}/docs/a.yaml",
                rewritten,
            )
            self.assertIn(f"/blob/{commit}/docs/b.md.", rewritten)
            self.assertIn(
                "https://github.com/example/test/blob/v1.2.3/docs/tag.md",
                rewritten,
            )

    def test_unmatched_closing_shortcode_does_not_consume_following_content(self):
        rendered = clean_hugo_shortcodes(
            "Before\n{{< /future-container >}}\nKeep this paragraph.\n",
            Path("."),
            profile="istio",
        )

        self.assertIn("Before", rendered)
        self.assertIn("Keep this paragraph.", rendered)
        self.assertNotIn("{{<", rendered)

    def test_discovery_disambiguates_colliding_paths_and_normalize_keeps_both_sources(self):
        with TemporaryDirectory() as temporary:
            temp_path = Path(temporary)
            repo = temp_path / "raw" / "test" / "1.0.0" / "repo"
            docs = repo / "docs"
            docs.mkdir(parents=True)
            (repo / "README.md").write_text("# Root README\n\nroot-only\n")
            (docs / "README.md").write_text("# Docs README\n\ndocs-only\n")
            manifest = Manifest(
                name="test",
                collection="test",
                version="1.0.0",
                source_type="git",
                repo_url="https://github.com/example/test",
                git_ref="a" * 40,
                docs_paths=["docs", "README.md"],
                source_url_template="{repo_url}/blob/{git_ref}/{path}",
            )

            discovered = _discover_source_files(manifest, repo)

            discovered_outputs = {
                file_path.relative_to(repo).as_posix(): output_path
                for file_path, output_path in discovered
            }
            self.assertEqual(
                discovered_outputs,
                {
                    "README.md": "README.md",
                    "docs/README.md": "docs/README.md",
                },
            )

            with patch.object(common, "REPO_ROOT", temp_path), redirect_stdout(io.StringIO()):
                normalize(manifest)

            corpus = temp_path / "corpus" / "test" / "1.0.0"
            root_output = corpus / "README.md"
            docs_output = corpus / "docs" / "README.md"
            self.assertTrue(root_output.is_file())
            self.assertTrue(docs_output.is_file())
            self.assertIn("root-only", root_output.read_text())
            self.assertIn("docs-only", docs_output.read_text())
            self.assertIn(
                "source_url: https://github.com/example/test/blob/" + "a" * 40 + "/README.md",
                root_output.read_text(),
            )
            self.assertIn(
                "source_url: https://github.com/example/test/blob/" + "a" * 40 + "/docs/README.md",
                docs_output.read_text(),
            )

    def test_discovery_deduplicates_sources_from_overlapping_docs_paths(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary) / "repo"
            source = repo / "docs" / "guide.md"
            source.parent.mkdir(parents=True)
            source.write_text("# Guide\n")
            manifest = Manifest(
                name="test",
                collection="test",
                version="1.0.0",
                docs_paths=["docs", "docs"],
            )

            discovered = _discover_source_files(manifest, repo)

            self.assertEqual(len(discovered), 1)
            self.assertEqual(discovered[0][0], source)
            self.assertEqual(discovered[0][1], "guide.md")

    def test_discovery_does_not_collapse_root_markdown_and_rst_sources(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary) / "repo"
            repo.mkdir(parents=True)
            (repo / "README.md").write_text("# Markdown README\n")
            (repo / "README.rst").write_text("RST README\n")
            manifest = Manifest(
                name="test",
                collection="test",
                version="1.0.0",
                docs_paths=["README.md", "README.rst"],
            )

            discovered = _discover_source_files(manifest, repo)
            output_paths = [Path(relative_path).with_suffix(".md").as_posix() for _, relative_path in discovered]

            self.assertEqual(len(discovered), 2)
            self.assertEqual(len(set(output_paths)), 2)
            self.assertEqual(output_paths[0], "README.md")
            self.assertEqual(output_paths[1], "README.rst.md")

    def test_discovery_keeps_symlink_alias_and_target_as_separate_sources(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary) / "repo"
            docs = repo / "docs"
            alias_dir = docs / "Getting-Started"
            alias_dir.mkdir(parents=True)
            target = docs / "README.md"
            alias = alias_dir / "intro.md"
            target.write_text("# Intro\n")
            alias.symlink_to("../README.md")
            manifest = Manifest(
                name="test",
                collection="test",
                version="1.0.0",
                docs_paths=["docs"],
            )

            discovered = _discover_source_files(manifest, repo)
            discovered_sources = {
                file_path.relative_to(repo).as_posix() for file_path, _ in discovered
            }

            self.assertEqual(discovered_sources, {"docs/README.md", "docs/Getting-Started/intro.md"})

    def test_discovery_applies_manifest_excludes_and_materializes_symlinks(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary) / "repo"
            docs = repo / "Documentation"
            (docs / "Getting-Started").mkdir(parents=True)
            (docs / "Helm-Charts").mkdir()
            (docs / "README.md").write_text("# Intro\n")
            (docs / "guide.md").write_text("# Guide\n")
            (docs / "Helm-Charts" / "operator-chart.gotmpl.md").write_text(
                "{{ template \"chart.header\" . }}\n"
            )
            (docs / "Getting-Started" / "intro.md").symlink_to("../README.md")
            manifest = Manifest(
                name="test",
                collection="rook",
                version="1.20.7",
                docs_paths=["Documentation"],
                exclude_globs=["README.md", "*.gotmpl.md"],
            )

            discovered = _discover_source_files(manifest, repo)

            self.assertEqual(
                [relative for _, relative in discovered],
                ["Getting-Started/intro.md", "guide.md"],
            )
            self.assertEqual(discovered[0][0].read_text(), "# Intro\n")

    def test_same_repository_master_blob_and_tree_links_are_commit_pinned(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary) / "repo"
            source = repo / "Documentation" / "page.md"
            source.parent.mkdir(parents=True)
            source.write_text("")
            commit = "a" * 40
            manifest = Manifest(
                name="test",
                collection="rook",
                version="1.20.7",
                source_type="git",
                repo_url="https://github.com/rook/rook",
                git_ref=commit,
            )

            rewritten = _rewrite_source_links(
                "[File](https://github.com/rook/rook/blob/master/deploy/examples/cluster.yaml) "
                "[Directory](https://github.com/rook/rook/tree/master/deploy/examples) "
                "[External](https://github.com/other/repo/blob/master/README.md)",
                source,
                Path("page.md"),
                repo,
                {"Documentation/page.md": "page.md"},
                manifest,
            )

            self.assertIn(f"/blob/{commit}/deploy/examples/cluster.yaml", rewritten)
            self.assertIn(f"/tree/{commit}/deploy/examples", rewritten)
            self.assertIn("https://github.com/other/repo/blob/master/README.md", rewritten)

            versioned_asset = _rewrite_source_links(
                "![Diagram](https://github.com/rook/rook/blob/release-1.20/design/diagram.svg)",
                source,
                Path("page.md"),
                repo,
                {"Documentation/page.md": "page.md"},
                manifest,
            )
            self.assertIn(f"/blob/{commit}/design/diagram.svg", versioned_asset)

    def test_percent_encoded_asset_path_resolves_to_pinned_source(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary) / "repo"
            source = repo / "Documentation" / "page.md"
            asset = repo / "Documentation" / "Rook Architecture.png"
            source.parent.mkdir(parents=True)
            source.write_text("")
            asset.write_bytes(b"png")
            commit = "b" * 40
            manifest = Manifest(
                name="test",
                collection="rook",
                version="1.20.7",
                source_type="git",
                repo_url="https://github.com/rook/rook",
                git_ref=commit,
                source_url_template="{repo_url}/blob/{git_ref}/{path}",
            )

            rewritten = _rewrite_source_links(
                "![Diagram](Rook%20Architecture.png)",
                source,
                Path("page.md"),
                repo,
                {"Documentation/page.md": "page.md"},
                manifest,
            )

            self.assertEqual(
                rewritten,
                "![Diagram](https://github.com/rook/rook/blob/"
                f"{commit}/Documentation/Rook%20Architecture.png)",
            )

    def test_normalize_exits_nonzero_when_docs_paths_do_not_exist(self):
        with TemporaryDirectory() as temporary:
            temp_path = Path(temporary)
            repo = temp_path / "raw" / "test" / "1.0.0" / "repo"
            repo.mkdir(parents=True)
            manifest = Manifest(
                name="test",
                collection="test",
                version="1.0.0",
                source_type="git",
                repo_url="https://github.com/example/test",
                git_ref="HEAD",
                docs_paths=["nonexistent_docs"],
            )
            stderr_buf = io.StringIO()
            with patch.object(common, "REPO_ROOT", temp_path), redirect_stderr(stderr_buf), redirect_stdout(io.StringIO()):
                with self.assertRaises(SystemExit) as cm:
                    normalize(manifest)
                self.assertEqual(cm.exception.code, 1)
            self.assertIn("no processable documentation files found", stderr_buf.getvalue())

    def test_normalize_exits_nonzero_when_no_documents_written(self):
        with TemporaryDirectory() as temporary:
            temp_path = Path(temporary)
            repo = temp_path / "raw" / "test" / "1.0.0" / "repo"
            repo.mkdir(parents=True)
            docs = repo / "docs"
            docs.mkdir(parents=True)
            (docs / "empty.md").write_text("   \n\n  ")
            manifest = Manifest(
                name="test",
                collection="test",
                version="1.0.0",
                source_type="git",
                repo_url="https://github.com/example/test",
                git_ref="HEAD",
                docs_paths=["docs"],
            )
            stderr_buf = io.StringIO()
            with patch.object(common, "REPO_ROOT", temp_path), redirect_stderr(stderr_buf), redirect_stdout(io.StringIO()):
                with self.assertRaises(SystemExit) as cm:
                    normalize(manifest)
                self.assertEqual(cm.exception.code, 1)
            self.assertIn("0 pages written to corpus", stderr_buf.getvalue())

    def test_gitbook_shortcode_profile_renders_nested_tags_and_preserves_hugo(self):
        rendered = clean_hugo_shortcodes(
"""Before
{%- hint style="info" -%}
See [the guide](docs/guide.md).
{%- endhint -%}
{% tabs %}
{% tab title="Outer" %}
Outer content
{% tabs %}
{% tab title="Inner" %}Inner content{% endtab %}
{% endtabs %}
{% endtab %}
{% endtabs %}
{% embed url="https://example.com/video" %}
Workshop
{% endembed %}
{% embed url="https://example.com/self" %}
After the self-closing embed.
{{< note >}}Hugo must stay literal{{< /note >}}
{{% future %}}Hugo percent must stay literal{{% /future %}}
""",
            Path("."),
            profile="gitbook",
        )

        self.assertIn("> **Note:**", rendered)
        self.assertIn("See [the guide](docs/guide.md).", rendered)
        self.assertIn("**Tab: Outer**", rendered)
        self.assertIn("**Tab: Inner**", rendered)
        self.assertIn("[Workshop](https://example.com/video)", rendered)
        self.assertIn("[https://example.com/self](https://example.com/self)", rendered)
        self.assertIn("After the self-closing embed.", rendered)
        self.assertIn("{{< note >}}Hugo must stay literal{{< /note >}}", rendered)
        self.assertIn("{{% future %}}Hugo percent must stay literal{{% /future %}}", rendered)
        self.assertNotRegex(rendered, r"(?<!\{)\{%[- ]")

    def test_gitbook_fenced_tags_stay_literal_and_end_hint_typo_is_supported(self):
        content = """Before
```markdown
{% hint style="warning" %}
literal fenced hint
{% endhint %}
```
>   ~~~yaml
>   {% tabs %}
>   {% tab title="literal" %}
>   ~~~
{% hint style="warning" %}
Warning body
{% end hint %}
After
"""

        rendered = clean_hugo_shortcodes(content, Path("."), profile="gitbook")

        self.assertIn(
            "```markdown\n{% hint style=\"warning\" %}\nliteral fenced hint\n{% endhint %}\n```",
            rendered,
        )
        self.assertIn(">   ~~~yaml\n>   {% tabs %}\n>   {% tab title=\"literal\" %}\n>   ~~~", rendered)
        self.assertIn("> **Warning:**", rendered)
        self.assertIn("Warning body", rendered)
        self.assertNotIn("{% end hint %}", rendered)

    def test_gitbook_include_is_confined_to_gitbook_directory_and_blocks_recursion(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary) / "repo"
            includes = repo / ".gitbook" / "includes"
            includes.mkdir(parents=True)
            (includes / "ok.md").write_text("Included body\n")
            (includes / "loop.md").write_text('{% include file="loop.md" %}\n')
            (Path(temporary) / "outside.md").write_text("SECRET OUTSIDE\n")

            rendered = clean_hugo_shortcodes(
                """{% include file="ok.md" %}
{% include file="../../outside.md" %}
{% include file="loop.md" %}
Keep this paragraph.
""",
                repo,
                profile="gitbook",
            )

            self.assertIn("Included body", rendered)
            self.assertIn("[include", rendered)
            self.assertIn("recursion blocked", rendered)
            self.assertIn("Keep this paragraph.", rendered)
            self.assertNotIn("SECRET OUTSIDE", rendered)
            self.assertNotRegex(rendered, r"\{%[- ]")

    def test_gitbook_lookahead_tags_render_as_searchable_markdown(self):
        rendered = clean_hugo_shortcodes(
            """{% content-ref url="guide.md" %}Guide{% endcontent-ref %}
{% code title="Config" language="yaml" %}
kind: Demo
{% endcode %}
{% file src="download.txt" %}
{% stepper %}
{% step title="Install" %}Run the command.{% endstep %}
{% endstepper %}
{% columns %}{% column %}Column body{% endcolumn %}{% endcolumns %}
""",
            Path("."),
            profile="gitbook",
        )

        self.assertIn("[Guide](guide.md)", rendered)
        self.assertIn("**Code: Config**", rendered)
        self.assertIn("```yaml\nkind: Demo\n```", rendered)
        self.assertIn("[download.txt](download.txt)", rendered)
        self.assertIn("**Step: Install**", rendered)
        self.assertIn("Run the command.", rendered)
        self.assertIn("Column body", rendered)
        self.assertNotRegex(rendered, r"\{%[- ]")

    def test_reference_definitions_pin_same_repository_main_and_preserve_other_targets(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary) / "repo"
            source = repo / "docs" / "page.md"
            source.parent.mkdir(parents=True)
            source.write_text("")
            commit = "c" * 40
            manifest = Manifest(
                name="test",
                collection="test",
                version="1.0.0",
                source_type="git",
                repo_url="https://github.com/example/test",
                git_ref=commit,
            )
            body = """[main]:https://github.com/example/test/blob/main/docs/main.md#part "Main title"
[angle]: <https://github.com/example/test/tree/main/docs> 'Angle title'
[master]: https://github.com/example/test/blob/master/docs/master.md
[cross]: https://github.com/other/repo/blob/main/docs/other.md
[relative]: ../guide.md
[malformed]: <https://github.com/example/test/blob/main/docs/bad.md "unterminated
```
[fenced]:https://github.com/example/test/blob/main/docs/fenced.md
```
"""

            rewritten = _rewrite_source_links(
                body,
                source,
                Path("docs/page.md"),
                repo,
                {"docs/page.md": "docs/page.md"},
                manifest,
            )

            self.assertIn(f"/blob/{commit}/docs/main.md#part \"Main title\"", rewritten)
            self.assertIn(f"/tree/{commit}/docs> 'Angle title'", rewritten)
            self.assertIn(f"/blob/{commit}/docs/master.md", rewritten)
            self.assertIn("https://github.com/other/repo/blob/main/docs/other.md", rewritten)
            self.assertIn("[relative]: ../guide.md", rewritten)
            self.assertIn(
                '[malformed]: <https://github.com/example/test/blob/main/docs/bad.md "unterminated',
                rewritten,
            )
            self.assertIn(
                "[fenced]:https://github.com/example/test/blob/main/docs/fenced.md",
                rewritten,
            )

    def test_same_repository_main_inline_tree_and_blob_links_pin_but_cross_repo_stays(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary) / "repo"
            source = repo / "docs" / "page.md"
            source.parent.mkdir(parents=True)
            source.write_text("")
            commit = "d" * 40
            manifest = Manifest(
                name="test",
                collection="test",
                version="1.0.0",
                source_type="git",
                repo_url="https://github.com/example/test",
                git_ref=commit,
            )

            rewritten = _rewrite_source_links(
                "[File](https://github.com/example/test/blob/main/docs/a.md) "
                "[Directory](https://github.com/example/test/tree/main/docs) "
                "[External](https://github.com/other/repo/blob/main/docs/b.md)",
                source,
                Path("docs/page.md"),
                repo,
                {"docs/page.md": "docs/page.md"},
                manifest,
            )

            self.assertIn(f"/blob/{commit}/docs/a.md", rewritten)
            self.assertIn(f"/tree/{commit}/docs", rewritten)
            self.assertIn("https://github.com/other/repo/blob/main/docs/b.md", rewritten)

    def test_normalize_gitbook_hint_rewrites_inner_source_link_after_profile(self):
        with TemporaryDirectory() as temporary:
            temp_path = Path(temporary)
            repo = temp_path / "raw" / "test" / "1.0.0" / "repo"
            docs = repo / "docs"
            docs.mkdir(parents=True)
            (docs / "a.md").write_text(
                "{% hint style=\"info\" %}\n[B](b.md)\n{% endhint %}\n"
            )
            (docs / "b.md").write_text("# B\n")
            commit = "e" * 40
            manifest = Manifest(
                name="test",
                collection="test",
                version="1.0.0",
                source_type="git",
                repo_url="https://github.com/example/test",
                git_ref=commit,
                docs_paths=["docs"],
                shortcode_profile="gitbook",
                source_url_template="{repo_url}/blob/{git_ref}/{path}",
            )

            with patch.object(common, "REPO_ROOT", temp_path), redirect_stdout(io.StringIO()):
                normalize(manifest)

            rendered = (temp_path / "corpus" / "test" / "1.0.0" / "a.md").read_text()
            self.assertIn("> **Note:**", rendered)
            self.assertIn("[B](b.md)", rendered)
            self.assertNotIn("unresolved-source-link", rendered)

    def test_jekyll_normalize_expands_direct_includes_and_indented_list_fence(self):
        with TemporaryDirectory() as temporary:
            temp_path = Path(temporary)
            repo = temp_path / "raw" / "opensearch" / "2.19" / "repo"
            (repo / "docs").mkdir(parents=True)
            (repo / "_includes").mkdir()
            for name in ("cards.html", "list.html", "copy.html", "copy-curl.html", "youtube-player.html"):
                (repo / "_includes" / name).write_text("<!-- template -->\n")
            (repo / "_config.yml").write_text(
                "url: https://docs.opensearch.org\nbaseurl: /latest\n"
                "opensearch_version: '2.19.6'\n"
                "opensearch_dashboards_version: '2.19.6'\n"
                "opensearch_major_minor_version: '2.19'\n"
            )
            (repo / "docs" / "index.md").write_text(
                """---
title: Home
getting_started:
  - heading: Start here
    description: A short description
    link: /guide/
steps:
  - heading: First step
    description: Run the command.
    link: /guide/
---
{% include cards.html cards=page.getting_started %}
{% include list.html list_items=page.steps %}
```bash
{% include copy.html %}
```
1. Send a request.
    ```bash
    curl https://localhost:9200
    ```
    {% include copy.html %}
{% include copy-curl.html %}
{% include youtube-player.html id='abc123' %}
"""
            )
            manifest = Manifest(
                name="opensearch-2.19",
                collection="opensearch",
                version="2.19",
                source_type="git",
                repo_url="https://github.com/opensearch-project/documentation-website",
                git_ref="a" * 40,
                docs_paths=["docs"],
                shortcode_profile="jekyll",
                app_version="2.19.3",
            )
            with patch.object(common, "REPO_ROOT", temp_path), redirect_stdout(io.StringIO()):
                normalize(manifest)
            output = next((temp_path / "corpus" / "opensearch" / "2.19").rglob("*.md"))
            rendered = output.read_text()
            self.assertIn("[Start here](/guide/)", rendered)
            self.assertIn("1. [First step](/guide/)", rendered)
            self.assertIn("<iframe src=\"https://www.youtube.com/embed/abc123\"", rendered)
            self.assertNotIn("{% include copy.html %}", rendered.split("```bash", 1)[0])
            self.assertIn("{% include copy.html %}", rendered)
            self.assertNotIn("{% include copy-curl.html %}", rendered)
            self.assertEqual(validate_no_residual_template_syntax(rendered), [])

    def test_jekyll_normalize_redacts_rendered_secret_shaped_slack_webhook(self):
        with TemporaryDirectory() as temporary:
            temp_path = Path(temporary)
            repo = temp_path / "raw" / "opensearch" / "2.19" / "repo"
            (repo / "docs").mkdir(parents=True)
            (repo / "_includes").mkdir()
            for name in ("cards.html", "list.html", "copy.html", "copy-curl.html", "youtube-player.html"):
                (repo / "_includes" / name).write_text("")
            (repo / "_config.yml").write_text(
                "url: https://docs.opensearch.org\nbaseurl: /latest\n"
            )
            secret_url = (
                "https://hooks.slack.com/services/T00000000/B00000000/"
                "XXXXXXXXXXXXXXXXXXXXXXXX"
            )
            safe_url = "https://hooks.slack.com/services/WORKSPACE_ID/CHANNEL_ID/REDACTED_TOKEN"
            benign_url = "https://hooks.slack.com/services/xxx/yyy/zzz"
            (repo / "docs" / "index.md").write_text(
                "---\n"
                "title: Home\n"
                f"webhook: {secret_url}\n"
                f"example_webhook: {benign_url}\n"
                "---\n"
                "[Slack]({{ page.webhook }})\n\n"
                "[Example]({{ page.example_webhook }})\n"
            )
            manifest = Manifest(
                name="opensearch-2.19",
                collection="opensearch",
                version="2.19",
                source_type="git",
                repo_url="https://github.com/opensearch-project/documentation-website",
                git_ref="a" * 40,
                docs_paths=["docs"],
                shortcode_profile="jekyll",
                app_version="2.19.3",
            )

            with patch.object(common, "REPO_ROOT", temp_path), redirect_stdout(io.StringIO()):
                normalize(manifest)

            output = next(
                (temp_path / "corpus/opensearch/2.19").rglob("*.md")
            ).read_text()
            self.assertIn(f"[Slack]({safe_url})", output)
            self.assertIn(f"[Example]({benign_url})", output)
            self.assertNotIn(secret_url, output)

    def test_jekyll_renderer_renders_site_variables_and_fails_unknown_variables(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary)
            (repo / "_includes").mkdir()
            for name in ("cards.html", "list.html", "copy.html", "copy-curl.html", "youtube-player.html"):
                (repo / "_includes" / name).write_text("")
            manifest = Manifest(
                name="opensearch-2.19",
                collection="opensearch",
                version="2.19",
                shortcode_profile="jekyll",
                app_version="2.19.3",
                site_overrides={
                    "opensearch_version": "2.19.3",
                    "opensearch_dashboards_version": "2.19.1",
                },
            )
            rendered = render_jekyll_template(
                "{{ site.opensearch_version }} {{ site.baseurl}}\n"
                "```text\n{{site.opensearch_version | split: \".\" | first}} {{undefined}}\n```\n"
                "{% raw %}{{ctx.index}}{% endraw %}",
                repo,
                manifest=manifest,
            )
            self.assertIn("2.19.3 /latest", rendered)
            self.assertIn("```text\n2 {{undefined}}\n```", rendered)
            self.assertIn("{{ctx.index}}", rendered)
            with self.assertRaises(JekyllRenderError):
                render_jekyll_template("{{ site.not_defined }}", repo, manifest=manifest)

    def test_jekyll_include_traversal_and_recursive_template_are_safe(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary)
            (repo / "_includes").mkdir()
            for name in ("cards.html", "list.html", "copy.html", "copy-curl.html", "youtube-player.html"):
                (repo / "_includes" / name).write_text("{% include cards.html %}\n" if name == "cards.html" else "")
            with self.assertRaises(JekyllRenderError):
                render_jekyll_template("{% include ../copy.html %}", repo)
            rendered = render_jekyll_template(
                "{% include cards.html cards=page.cards %}",
                repo,
                page_data={"cards": [{"heading": "One"}]},
            )
            self.assertIn("include recursion blocked: cards.html", rendered)

    def test_jekyll_registry_uses_permalink_index_collapse_and_no_suffix_collision_masking(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary)
            (repo / "_docs").mkdir()
            (repo / "_docs" / "index.md").write_text(
                "---\ntitle: Root\npermalink: /docs/\n---\nRoot\n"
            )
            (repo / "_docs" / "a.md").write_text(
                "---\ntitle: A\npermalink: /dup/\ncanonical_url: https://docs.opensearch.org/latest/dup/\n---\nA\n"
            )
            (repo / "_docs" / "b.md").write_text(
                "---\ntitle: B\npermalink: /dup/\ncanonical_url: https://docs.opensearch.org/latest/dup/\n---\nB\n"
            )
            manifest = Manifest(
                name="test",
                collection="opensearch",
                version="2.19",
                docs_paths=["_docs"],
            )
            registry = _build_jekyll_registry(manifest, repo)
            by_source = registry.by_source
            self.assertEqual(by_source["_docs/index.md"].output_rel_path, "docs/index.md")
            self.assertEqual(len(registry.by_route["/dup/"]), 2)
            self.assertTrue(all(page.output_rel_path.startswith("__source__/") for page in registry.by_route["/dup/"]))
            self.assertFalse(any(".source" in page.output_rel_path for page in registry.pages))

    def test_jekyll_registry_resolves_permalink_redirect_case_and_cross_corpus(self):
        with TemporaryDirectory() as temporary:
            temp_path = Path(temporary)
            repo = temp_path / "raw" / "opensearch" / "2.19" / "repo"
            peer_repo = temp_path / "raw" / "opensearch-dashboards" / "2.19" / "repo"
            (repo / "_docs").mkdir(parents=True)
            (peer_repo / "_dashboards").mkdir(parents=True)
            (repo / "_config.yml").write_text(
                "url: https://docs.opensearch.org\nbaseurl: /latest\n"
            )
            (peer_repo / "_config.yml").write_text(
                "url: https://docs.opensearch.org\nbaseurl: /latest\n"
            )
            (repo / "_docs" / "current.md").write_text(
                "---\n"
                "title: Current\n"
                "canonical_url: https://docs.opensearch.org/latest/core/target/\n"
                "permalink: /legacy/TARGET/\n"
                "redirect_from:\n"
                "  - /OLD/\n"
                "---\nCurrent\n"
            )
            (repo / "_docs" / "other.md").write_text(
                "---\ntitle: Other\nredirect_from: /old/\n---\nOther\n"
            )
            (peer_repo / "_dashboards" / "quickstart.md").write_text(
                "---\n"
                "title: Quickstart\n"
                "permalink: /dashboards/quickstart-old/\n"
                "canonical_url: https://docs.opensearch.org/latest/dashboards/quickstart/\n"
                "---\nDashboard\n"
            )
            manifest = Manifest(
                name="opensearch-2.19",
                collection="opensearch",
                version="2.19",
                docs_paths=["_docs"],
                repo_url="https://github.com/opensearch-project/documentation-website",
                git_ref="a" * 40,
            )
            peer_manifest = Manifest(
                name="opensearch-dashboards-2.19",
                collection="opensearch-dashboards",
                version="2.19",
                docs_paths=["_dashboards"],
                repo_url="https://github.com/opensearch-project/documentation-website",
                git_ref="a" * 40,
            )
            registry = _build_jekyll_registry(manifest, repo)
            peer_registry = _build_jekyll_registry(peer_manifest, peer_repo)
            page = registry.by_source["_docs/current.md"]
            self.assertEqual(page.route, "/legacy/target/")
            self.assertEqual(page.canonical_route, "/core/target/")
            self.assertEqual(len(registry.by_alias["/core/target/"]), 1)
            self.assertNotIn("/legacy/target/", registry.by_alias)
            self.assertEqual(len(registry.by_alias["/old/"]), 2)
            rewritten, stats = _rewrite_jekyll_links(
                "[permalink](/latest/legacy/TARGET/) "
                "[redirect](/latest/OLD/) "
                "[cross](https://docs.opensearch.org/latest/dashboards/quickstart-old/)",
                page,
                registry,
                peer_registry,
                repo,
            )
            self.assertIn("[permalink](index.md)", rewritten)
            self.assertIn(
                "[redirect](/latest/OLD/) "
                "<!-- unresolved-jekyll-link: ambiguous-redirect=/old/ -->",
                rewritten,
            )
            self.assertIn(
                "[cross](https://docs.opensearch.org/latest/dashboards/quickstart-old/) "
                "<!-- unresolved-cross-corpus-link: collection=opensearch-dashboards route=/dashboards/quickstart-old/ -->",
                rewritten,
            )
            self.assertEqual(stats["cross_corpus"], 1)
            self.assertEqual(stats["unresolved"], 1)

    def test_jekyll_ial_and_literal_fence_preservation(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary)
            body = """{: .note}
Text {::nomarkdown}<img src=\"x.png\" class=\"inline\"/>{:/}
{:toc}
Use `{% raw %}{{{field-name}}}{% endraw %}` here.
Use {% raw %}`{{{` and `}}}`{% endraw %} for delimiters.
```markdown
{: .note}
{% include copy.html %}
{{mustache}}
```
"""
            rendered = render_jekyll_template(body, repo)
            self.assertIn("{: .note}", rendered)
            self.assertIn('<img src="x.png" class="inline"/>', rendered)
            self.assertIn("<!-- local-toc -->", rendered)
            self.assertIn("Use `{{{field-name}}}` here.", rendered)
            self.assertIn("Use `{{{` and `}}}` for delimiters.", rendered)
            self.assertNotIn("\x00JEKYLL_LITERAL_", rendered)
            self.assertIn("{% include copy.html %}", rendered)
            self.assertIn("{{mustache}}", rendered)
            self.assertEqual(validate_no_residual_template_syntax(rendered), [])

    def test_jekyll_fence_scanner_keeps_inline_and_heading_boundaries(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary)
            body = (
                "```opensearch_security.readonly_mode.roles: [new_role]```\\n"
                "```json\\n"
                "{\\\"ok\\\": true}\\n"
                "\\n"
                "## Next steps\\n"
                "The configured base URL is {{ site.baseurl }}.\\n"
            )
            body = body.replace("\\\\n", "\\n").replace('\\\\"', '"')
            rendered = render_jekyll_template(body, repo)
            self.assertIn(
                "```opensearch_security.readonly_mode.roles: [new_role]```",
                rendered,
            )
            self.assertIn("## Next steps\\nThe configured base URL is /latest.", rendered)
            self.assertEqual(validate_no_residual_template_syntax(rendered), [])

    def test_jekyll_fence_raw_strips_wrapper_preserves_inner_and_fails_closed(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary)
            manifest = Manifest(
                name="opensearch-2.19",
                collection="opensearch",
                version="2.19",
                site_overrides={"opensearch_version": "2.19.3"},
            )
            body = (
                "```liquid\n"
                "{% raw %}{{ site.opensearch_version }} {{mustache}}{% endraw %}\n"
                "{{ site.opensearch_version }}\n"
                "```\n"
            )
            rendered = render_jekyll_template(body, repo, manifest=manifest)
            self.assertIn("{{ site.opensearch_version }} {{mustache}}", rendered)
            self.assertIn("\n2.19.3\n", rendered)
            self.assertNotIn("{% raw %}", rendered)
            self.assertNotIn("{% endraw %}", rendered)
            self.assertEqual(validate_no_residual_template_syntax(rendered), [])

            with self.assertRaises(JekyllRenderError):
                render_jekyll_template("```liquid\n{% raw %}literal\n```\n", repo, manifest=manifest)
            self.assertIn(
                "fence-raw",
                validate_no_residual_template_syntax("```liquid\n{% raw %}literal{% endraw %}\n```\n"),
            )

    def test_jekyll_site_overrides_are_allowlisted_and_app_version_is_metadata(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary)
            manifest = Manifest(
                name="opensearch-2.19",
                collection="opensearch",
                version="2.19",
                app_version="2.19.3",
                site_overrides={"opensearch_version": "2.19.3"},
            )
            self.assertIn(
                "2.19.3",
                render_jekyll_template("{{ site.opensearch_version }}", repo, manifest=manifest),
            )
            self.assertEqual(
                render_jekyll_template(
                    "{{page.title}}",
                    repo,
                    manifest=manifest,
                    page_data={"title": "Rendered title"},
                ),
                "Rendered title",
            )
            self.assertEqual(
                render_jekyll_template(
                    "`{{page.title}}` and {{ctx.index}}",
                    repo,
                    manifest=manifest,
                    page_data={"title": "Rendered title"},
                ),
                "`{{page.title}}` and {{ctx.index}}",
            )
            self.assertIn(
                "output:page.title",
                validate_no_residual_template_syntax("{{page.title}}"),
            )
            with self.assertRaises(JekyllRenderError):
                render_jekyll_template("{{ site.unknown }}", repo, manifest=manifest)
            with self.assertRaises(JekyllRenderError):
                render_jekyll_template(
                    "{{ site.opensearch_version }}",
                    repo,
                    manifest=Manifest(
                        name="opensearch-2.19",
                        collection="opensearch",
                        version="2.19",
                        site_overrides={"unknown": "value"},
                    ),
                )

    def test_jekyll_peer_registry_matches_manifest_version_and_scans_manifest_content(self):
        with TemporaryDirectory() as temporary:
            temp_path = Path(temporary)
            peer_repo = temp_path / "raw" / "opensearch-dashboards" / "2.19.1" / "repo"
            (peer_repo / "_dashboards").mkdir(parents=True)
            (peer_repo / "_dashboards" / "index.md").write_text(
                "---\ntitle: Dashboard\n---\nDashboard\n"
            )
            manifests = temp_path / "builder" / "manifests"
            manifests.mkdir(parents=True)
            (manifests / "dashboard-docs.toml").write_text(
                'name = "dashboard-docs"\n'
                'collection = "opensearch-dashboards"\n'
                'version = "2.19.1"\n'
                'source_type = "git"\n'
                'docs_paths = ["_dashboards"]\n'
            )
            manifest = Manifest(
                name="opensearch-2.19.1",
                collection="opensearch",
                version="2.19.1",
            )
            with patch.object(common, "REPO_ROOT", temp_path):
                registry = _peer_jekyll_registry(manifest)
            self.assertIsNotNone(registry)
            self.assertEqual(registry.manifest.version, "2.19.1")
            self.assertIn("_dashboards/index.md", registry.by_source)

    def test_jekyll_normalize_removes_stale_markdown_and_empty_directories(self):
        with TemporaryDirectory() as temporary:
            temp_path = Path(temporary)
            repo = temp_path / "raw" / "opensearch" / "2.19" / "repo"
            (repo / "_docs").mkdir(parents=True)
            (repo / "_docs" / "index.md").write_text("---\ntitle: Home\n---\nHome\n")
            corpus = temp_path / "corpus" / "opensearch" / "2.19"
            (corpus / "stale" / "nested").mkdir(parents=True)
            (corpus / "stale" / "nested" / "old.md").write_text("old\n")
            (corpus / "empty" / "nested").mkdir(parents=True)
            manifest = Manifest(
                name="opensearch-2.19",
                collection="opensearch",
                version="2.19",
                docs_paths=["_docs"],
                shortcode_profile="jekyll",
                app_version="2.19.3",
                site_overrides={"opensearch_version": "2.19.3"},
            )
            with patch.object(common, "REPO_ROOT", temp_path), redirect_stdout(io.StringIO()):
                normalize(manifest)
            self.assertTrue((corpus / "docs" / "index.md").is_file())
            self.assertIn('app_version: "2.19.3"', (corpus / "docs" / "index.md").read_text())
            self.assertFalse((corpus / "stale").exists())
            self.assertFalse((corpus / "empty").exists())

    def test_jekyll_html_assets_are_pinned_and_unresolved_attrs_are_marked(self):
        with TemporaryDirectory() as temporary:
            temp_path = Path(temporary)
            repo = temp_path / "raw" / "opensearch" / "2.19" / "repo"
            (repo / "_docs").mkdir(parents=True)
            (repo / "images").mkdir()
            (repo / "images" / "icon.png").write_bytes(b"png")
            (repo / "_config.yml").write_text(
                "url: https://docs.opensearch.org\nbaseurl: /latest\n"
            )
            (repo / "_docs" / "current.md").write_text(
                "---\ntitle: Current\n---\nCurrent\n"
            )
            manifest = Manifest(
                name="opensearch-2.19",
                collection="opensearch",
                version="2.19",
                docs_paths=["_docs"],
                repo_url="https://github.com/opensearch-project/documentation-website",
                git_ref="a" * 40,
            )
            registry = _build_jekyll_registry(manifest, repo)
            page = registry.by_source["_docs/current.md"]
            rewritten, stats = _rewrite_jekyll_links(
                '<img src="https://docs.opensearch.org/latest/images/icon.png"> '
                '<a href="/latest/not-a-page/">missing</a> '
                '[source](https://github.com/opensearch-project/documentation-website/blob/main/_docs/current.md)',
                page,
                registry,
                None,
                repo,
            )
            self.assertIn(
                f'https://github.com/opensearch-project/documentation-website/blob/{manifest.git_ref}/images/icon.png',
                rewritten,
            )
            self.assertIn('data-airgap-link-status="unresolved:route=/not-a-page/"', rewritten)
            self.assertIn(
                f"https://github.com/opensearch-project/documentation-website/blob/{manifest.git_ref}/_docs/current.md",
                rewritten,
            )
            self.assertEqual(stats["assets"], 1)
            self.assertEqual(stats["unresolved"], 1)


if __name__ == "__main__":
    unittest.main()
