import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common import Manifest
from validate_ceph_corpus import extract_markdown_targets, validate_corpus


class CephValidatorTests(unittest.TestCase):
    def test_markdown_targets_allow_parentheses(self):
        body = "See [the page](../guide/install-(quickly).md#start) and ![plot](plot(a).svg)."
        self.assertEqual(
            extract_markdown_targets(body),
            ["../guide/install-(quickly).md#start", "plot(a).svg"],
        )

    def test_istio_site_absolute_links_require_explicit_marker_and_are_counted(self):
        with TemporaryDirectory() as temporary:
            corpus = Path(temporary) / "corpus"
            page = corpus / "guide.md"
            corpus.mkdir()
            page.write_text(
                "---\n"
                "collection: istio\n"
                'version: "1.24"\n'
                "title: Guide\n"
                "source_url: https://example.invalid/source\n"
                "fetched_at: now\n"
                "---\n"
                "[Blog](https://istio.io/v1.24/blog/post)"
                " <!-- unresolved-site-link: route=/blog/post -->\n"
                "> ```bash\n"
                "> curl -L https://istio.io/downloadIstio | sh -\n"
                "> ```\n"
            )
            manifest = Manifest(
                name="istio-1.24",
                collection="istio",
                version="1.24",
                shortcode_profile="istio",
                site_overrides={"url": "https://istio.io", "baseurl": "/v1.24"},
            )

            report = validate_corpus(corpus, manifest, raw_required=False)
            self.assertEqual(report["unresolved_link_markers"], {"site": 1})
            self.assertEqual(report["failures"], [])

            page.write_text(
                page.read_text()
                + "[Unmarked](https://istio.io/v1.24/blog/other)\n"
            )
            report = validate_corpus(corpus, manifest, raw_required=False)
            self.assertTrue(
                any("route: /blog/other" in failure for failure in report["failures"])
            )
            page.write_text(
                page.read_text().replace(
                    "[Unmarked](https://istio.io/v1.24/blog/other)\n", ""
                )
            )

            page.write_text(
                page.read_text().replace(
                    " <!-- unresolved-site-link: route=/blog/post -->", ""
                )
            )
            report = validate_corpus(corpus, manifest, raw_required=False)
            self.assertTrue(
                any("unclassified site link" in failure for failure in report["failures"])
            )

            page.write_text(
                page.read_text()
                + "See https://istio.io/v1.24/about/faq for more information.\n"
            )
            report = validate_corpus(corpus, manifest, raw_required=False)
            self.assertTrue(
                any("unclassified site link" in failure for failure in report["failures"])
            )

    def test_declared_chart_version_is_required(self):
        with TemporaryDirectory() as temporary:
            corpus = Path(temporary) / "corpus"
            corpus.mkdir()
            page = corpus / "README.md"
            page.write_text(
                "---\n"
                "collection: example\n"
                'version: "1.0.0"\n'
                "title: Example\n"
                "source_url: https://example.invalid/source\n"
                "fetched_at: now\n"
                'chart_version: "2.7.0"\n'
                "---\n"
                "Body.\n"
            )
            manifest = Manifest(
                name="example",
                collection="example",
                version="1.0.0",
                chart_version="2.7.0",
            )

            self.assertEqual(
                validate_corpus(corpus, manifest, raw_required=False)["failures"],
                [],
            )
            page.write_text(page.read_text().replace('chart_version: "2.7.0"\n', ""))
            failures = validate_corpus(corpus, manifest, raw_required=False)["failures"]
            self.assertTrue(any("missing frontmatter chart_version" in item for item in failures))

if __name__ == "__main__":
    unittest.main()
