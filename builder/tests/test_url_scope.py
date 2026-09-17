import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common import Manifest, in_scope, url_to_relpath

BASE = "https://docs.python.org/3.10/"


def manifest(**kwargs) -> Manifest:
    return Manifest(name="python-3.10", collection="python", version="3.10.21", base_url=BASE, **kwargs)


class AllowPrefixTests(unittest.TestCase):
    def test_empty_allowlist_keeps_everything_below_base_url(self):
        m = manifest()
        self.assertTrue(in_scope(BASE + "library/os.html", m))
        self.assertTrue(in_scope(BASE + "tutorial/index.html", m))

    def test_allowlist_is_fail_closed(self):
        m = manifest(allow_prefixes=["library/", "distutils/"])
        self.assertTrue(in_scope(BASE + "library/os.html", m))
        self.assertTrue(in_scope(BASE + "distutils/apiref.html", m))
        self.assertFalse(in_scope(BASE + "tutorial/index.html", m))
        self.assertFalse(in_scope(BASE + "c-api/list.html", m))
        self.assertFalse(in_scope(BASE + "genindex.html", m))

    def test_base_page_stays_in_scope_as_the_crawl_seed(self):
        m = manifest(allow_prefixes=["library/"])
        self.assertTrue(in_scope(BASE, m))
        self.assertTrue(in_scope(BASE + "index.html", m))
        self.assertEqual(url_to_relpath(BASE, m).as_posix(), "index.md")
        self.assertEqual(url_to_relpath(BASE + "index.html", m).as_posix(), "index.md")

    def test_deny_prefixes_still_apply_inside_the_allowlist(self):
        m = manifest(allow_prefixes=["library/"], deny_prefixes=["library/xml."])
        self.assertTrue(in_scope(BASE + "library/os.html", m))
        self.assertFalse(in_scope(BASE + "library/xml.dom.html", m))

    def test_other_hosts_and_versions_are_out_of_scope(self):
        m = manifest(allow_prefixes=["library/"])
        self.assertFalse(in_scope("https://docs.python.org/3.12/library/os.html", m))
        self.assertFalse(in_scope("https://example.com/library/os.html", m))


if __name__ == "__main__":
    unittest.main()
