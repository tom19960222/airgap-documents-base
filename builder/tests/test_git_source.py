import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common import Manifest
from git_source import _discover_source_files, _rewrite_source_links


class GitSourceTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
