import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from validate_ceph_corpus import extract_markdown_targets, scan_secret_findings


class CephValidatorTests(unittest.TestCase):
    def test_markdown_targets_allow_parentheses(self):
        body = "See [the page](../guide/install-(quickly).md#start) and ![plot](plot(a).svg)."
        self.assertEqual(
            extract_markdown_targets(body),
            ["../guide/install-(quickly).md#start", "plot(a).svg"],
        )

    def test_secret_inventory_returns_only_classifications(self):
        body = (
            "-----BEGIN CERTIFICATE-----\n"
            "MIIB\n"
            "-----END CERTIFICATE-----\n"
            "key: AQ" + "A" * 16 + "\n"
            "X-Auth-Token: " + "t" * 24 + "\n"
        )
        findings = scan_secret_findings(body)
        self.assertEqual(
            [kind for kind, _ in findings],
            ["certificate", "cephx", "x-auth-token"],
        )
        self.assertEqual([line for _, line in findings], [1, 4, 5])
        self.assertTrue(all(len(finding) == 2 for finding in findings))

if __name__ == "__main__":
    unittest.main()
