import unittest
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common import Manifest
from git_source import _has_source_content, _rewrite_source_links, rst_to_markdown


class RstNormalizerTests(unittest.TestCase):
    def test_titles_and_code_directives_become_markdown(self):
        title, body = rst_to_markdown(
            """================
Example document
================

Section
-------

Subsection
``````````

.. code-block:: bash

   ceph -s
""",
            default_title="fallback",
        )

        self.assertEqual(title, "Example document")
        self.assertIn("# Example document", body)
        self.assertIn("## Section", body)
        self.assertIn("### Subsection", body)
        self.assertIn("```bash\nceph -s\n```", body)

    def test_admonitions_links_and_roles_keep_readable_content(self):
        _, body = rst_to_markdown(
            """.. note::

   Read the `Ceph guide <https://docs.ceph.com/>`_ and check
   :ref:`the configuration option <configuring-ceph>`.

.. unknown-ceph-directive:: value

   directive payload must remain searchable
"""
        )

        self.assertIn("> **Note:**", body)
        self.assertIn("[Ceph guide](https://docs.ceph.com/)", body)
        self.assertIn("the configuration option", body)
        self.assertIn(".. unknown-ceph-directive:: value", body)
        self.assertIn("directive payload must remain searchable", body)

    def test_literal_blocks_preserve_commands_and_content(self):
        _, body = rst_to_markdown(
            """Run the command::

   ceph orch upgrade status
   ceph health
"""
        )

        self.assertIn("Run the command:", body)
        self.assertIn("```\nceph orch upgrade status\nceph health\n```", body)

    def test_trailing_whitespace_is_not_carried_into_markdown(self):
        _, body = rst_to_markdown("A line with spaces   \n")
        self.assertNotIn("spaces   ", body)

    def test_literalinclude_embeds_only_files_inside_repo(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary) / "repo"
            source = repo / "doc" / "page.rst"
            source.parent.mkdir(parents=True)
            (source.parent / "snippet.conf").write_text("[global]\nosd_pool_default_size = 3\n")
            outside = Path(temporary) / "secret.conf"
            outside.write_text("should not be included\n")

            _, included = rst_to_markdown(
                """.. literalinclude:: snippet.conf
   :language: ini
""",
                repo_dir=repo,
                source_path=source,
            )
            self.assertIn("Included file `doc/snippet.conf`:", included)
            self.assertIn("```ini\n[global]\nosd_pool_default_size = 3\n```", included)

            _, escaped = rst_to_markdown(
                ".. literalinclude:: ../../secret.conf\n",
                repo_dir=repo,
                source_path=source,
            )
            self.assertIn(".. literalinclude:: ../../secret.conf", escaped)
            self.assertNotIn("should not be included", escaped)

    def test_source_links_resolve_to_corpus_pages_or_pinned_assets(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary) / "repo"
            source = repo / "doc" / "page.rst"
            target = repo / "doc" / "target.rst"
            asset = repo / "doc" / "diagram.png"
            source.parent.mkdir(parents=True)
            source.write_text("")
            target.write_text("")
            asset.write_bytes(b"png")
            manifest = Manifest(
                name="test",
                collection="ceph",
                version="20.2.4",
                source_type="git",
                repo_url="https://github.com/ceph/ceph",
                git_ref="a" * 40,
                source_url_template="{repo_url}/blob/{git_ref}/{path}",
            )

            body = _rewrite_source_links(
                "[Target](target) ![Diagram](diagram.png)",
                source,
                Path("page.md"),
                repo,
                {"doc/page.rst": "page.md", "doc/target.rst": "target.md"},
                manifest,
            )
            self.assertIn("[Target](target.md)", body)
            self.assertIn(
                "https://github.com/ceph/ceph/blob/" + "a" * 40 + "/doc/diagram.png",
                body,
            )

    def test_empty_source_is_not_a_document(self):
        self.assertFalse(_has_source_content(""))
        self.assertFalse(_has_source_content(" \n\t\n"))
        self.assertTrue(_has_source_content("# Real document\n"))


if __name__ == "__main__":
    unittest.main()
