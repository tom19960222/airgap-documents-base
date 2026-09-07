import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from validate_ceph_corpus import extract_markdown_targets


class CephValidatorTests(unittest.TestCase):
    def test_markdown_targets_allow_parentheses(self):
        body = "See [the page](../guide/install-(quickly).md#start) and ![plot](plot(a).svg)."
        self.assertEqual(
            extract_markdown_targets(body),
            ["../guide/install-(quickly).md#start", "plot(a).svg"],
        )

if __name__ == "__main__":
    unittest.main()
