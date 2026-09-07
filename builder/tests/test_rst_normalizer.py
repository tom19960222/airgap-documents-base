import time
import unittest
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common import Manifest
from git_source import (
    _collect_rst_targets,
    _has_source_content,
    _rewrite_rst_links,
    _rewrite_source_links,
    rst_to_markdown,
)


class RstNormalizerTests(unittest.TestCase):
    def test_section_levels_follow_rst_style_order_and_overline_shape(self):
        _, ordered = rst_to_markdown(
            "Top level\n"
            "---------\n\n"
            "Nested\n"
            "~~~~~~~\n\n"
            "Deep nested\n"
            "^^^^^^^^^^^\n"
        )
        self.assertEqual(
            [line for line in ordered.splitlines() if line.startswith("#")],
            ["# Top level", "## Nested", "### Deep nested"],
        )

        _, mixed_shapes = rst_to_markdown(
            "==============\n"
            "Root\n"
            "==============\n\n"
            "Child\n"
            "=====\n\n"
            "Grandchild\n"
            "----------\n"
        )
        self.assertEqual(
            [line for line in mixed_shapes.splitlines() if line.startswith("#")],
            ["# Root", "## Child", "### Grandchild"],
        )

    def test_nested_admonition_directives_render_as_quoted_code_blocks(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary) / "repo"
            source = repo / "doc" / "page.rst"
            source.parent.mkdir(parents=True)
            source.write_text(
                ".. warning:: Outer warning\n\n"
                "   Introductory text.\n\n"
                "   .. note:: Nested note\n\n"
                "      .. code-block:: console\n\n"
                "         # cat [config](config.rst)\n"
                "         # keep :ref:`target <target>`\n\n"
                "      .. prompt:: bash #\n\n"
                "         ceph -s\n"
                "\n"
                "      .. code-block:: text\n\n"
                "         +---+---+\n"
                "         | A | B |\n"
                "         +===+===+\n"
                "         | x | y |\n"
                "         +---+---+\n"
            )
            manifest = Manifest(
                name="test",
                collection="ceph",
                version="20.2.4",
                source_type="git",
                repo_url="https://github.com/ceph/ceph",
                git_ref="a" * 40,
                source_url_template="{repo_url}/blob/{git_ref}/{path}",
            )
            source_outputs = {"doc/page.rst": "page.md"}

            _, normalized = rst_to_markdown(
                source.read_text(),
                repo_dir=repo,
                source_path=source,
                preserve_rst_links=True,
            )
            rewritten = _rewrite_rst_links(
                normalized,
                source,
                Path("page.md"),
                repo,
                source_outputs,
                manifest,
            )
            rewritten = _rewrite_source_links(
                rewritten,
                source,
                Path("page.md"),
                repo,
                source_outputs,
                manifest,
            )

            self.assertIn("> > **Note:** Nested note", rewritten)
            self.assertIn("> > ```console", rewritten)
            self.assertIn("> > # cat [config](config.rst)", rewritten)
            self.assertIn("> > # keep :ref:`target <target>`", rewritten)
            self.assertIn("> > ```bash", rewritten)
            self.assertIn("> > ceph -s", rewritten)
            self.assertIn("> > ```text", rewritten)
            self.assertIn("> > +---+---+", rewritten)
            self.assertIn("> > | A | B |", rewritten)
            self.assertIn("> > +===+===+", rewritten)
            self.assertNotIn("> > .. code-block::", rewritten)
            self.assertNotIn("unresolved-rst-link", rewritten)
            self.assertNotIn("unresolved-source-link", rewritten)

    def test_included_sections_keep_parent_rst_style_levels(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary) / "repo"
            source = repo / "doc" / "page.rst"
            fragment = repo / "doc" / "fragment.inc.rst"
            source.parent.mkdir(parents=True)
            source.write_text(
                "Parent\n"
                "======\n\n"
                "Section\n"
                "-------\n\n"
                "Subsection\n"
                "^^^^^^^^^^\n\n"
                ".. include:: fragment.inc.rst\n"
            )
            fragment.write_text(
                "Feature Toggles\n"
                "^^^^^^^^^^^^^^^\n\n"
                "Included details.\n"
            )

            _, body = rst_to_markdown(
                source.read_text(),
                repo_dir=repo,
                source_path=source,
            )
            self.assertEqual(
                [line for line in body.splitlines() if line.startswith("#")],
                ["# Parent", "## Section", "### Subsection", "### Feature Toggles"],
            )

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

    def test_multiline_admonition_ref_keeps_blockquote_out_of_link_label(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary) / "repo"
            source = repo / "doc" / "index.rst"
            target = repo / "doc" / "dev" / "developer_guide" / "basic-workflow.rst"
            target.parent.mkdir(parents=True)
            source.parent.mkdir(parents=True, exist_ok=True)
            source.write_text(
                "Welcome\n=======\n\n"
                ".. warning::\n\n"
                "   :ref:`If this is your first time using Ceph, read the \"Basic Workflow\"\n"
                "   page in the Ceph Developer Guide to learn how to contribute to the\n"
                "   Ceph project. <basic workflow dev guide>`.\n"
            )
            target.write_text("Basic Workflow\n===============\n")
            manifest = Manifest(
                name="test",
                collection="ceph",
                version="20.2.4",
                source_type="git",
                repo_url="https://github.com/ceph/ceph",
                git_ref="a" * 40,
                source_url_template="{repo_url}/blob/{git_ref}/{path}",
            )
            source_outputs = {
                "doc/index.rst": "index.md",
                "doc/dev/developer_guide/basic-workflow.rst": "dev/developer_guide/basic-workflow.md",
            }
            rst_targets = {
                "basic workflow dev guide": (target, "", "basic workflow dev guide"),
            }

            _, normalized = rst_to_markdown(
                source.read_text(),
                repo_dir=repo,
                source_path=source,
                preserve_rst_links=True,
            )
            rendered = _rewrite_rst_links(
                normalized,
                source,
                Path("index.md"),
                repo,
                source_outputs,
                manifest,
                rst_targets,
            )

            self.assertIn(
                '> [If this is your first time using Ceph, read the "Basic Workflow" '
                'page in the Ceph Developer Guide to learn how to contribute to the '
                'Ceph project.](dev/developer_guide/basic-workflow.md#basic-workflow-dev-guide).',
                rendered,
            )
            self.assertNotIn('Basic Workflow" > page', rendered)

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

    def test_mixed_space_tab_indentation_becomes_deterministic_spaces(self):
        _, body = rst_to_markdown("Output::\n\n   \tvalue\n")
        self.assertNotIn("\t", body)
        self.assertIn("```\nvalue\n```", body)

    def test_grid_tables_become_gfm_tables(self):
        _, body = rst_to_markdown(
            "+----------+----------+\n"
            "| Name     | Status   |\n"
            "+==========+==========+\n"
            "| ceph-osd | healthy  |\n"
            "+----------+----------+\n"
        )

        self.assertIn("| Name | Status |\n| --- | --- |\n| ceph-osd | healthy |", body)
        self.assertNotIn("+----------+----------+", body)

    def test_grid_tables_with_spanning_headers_keep_all_columns(self):
        _, body = rst_to_markdown(
            "+-----------+-----------------------------------------------+\n"
            "|  Ceph     |                 Podman                        |\n"
            "+-----------+-------+-------+-------+-------+-------+-------+\n"
            "|           | 1.9   |  2.0  |  2.1  |  2.2  |  3.0  | > 3.0 |\n"
            "+===========+=======+=======+=======+=======+=======+=======+\n"
            "| <= 15.2.5 | True  | False | False | False | False | False |\n"
            "+-----------+-------+-------+-------+-------+-------+-------+\n"
        )

        self.assertIn("| Ceph | Podman |  |  |  |  |  |", body)
        self.assertIn("|  | 1.9 | 2.0 | 2.1 | 2.2 | 3.0 | > 3.0 |", body)
        self.assertNotIn("1.9 \\| 2.0", body)

    def test_grid_tables_with_partial_spanning_borders_keep_rows(self):
        _, body = rst_to_markdown(
            "+---+-----+---+\n"
            "| A | B   | C |\n"
            "+---+-----+---+\n"
            "| x | y   | z |\n"
            "| x +-----+---+\n"
            "|   | w   | q |\n"
            "+---+-----+---+\n"
        )

        self.assertIn("| A | B | C |\n| --- | --- | --- |", body)
        self.assertIn("x <br> x", body)
        self.assertIn("w", body)
        self.assertNotIn("+-----+", body)

    def test_grid_tables_with_one_column_overrun_keep_trailing_cell(self):
        _, body = rst_to_markdown(
            "+---+-----+---+\n"
            "| A | B   | C |\n"
            "+---+-----+---+\n"
            "| x | y   | z |\n"
            "| x | y   | z  |\n"
            "+---+-----+---+\n"
        )

        self.assertIn("| x <br> x | y <br> y | z <br> z |", body)
        self.assertNotIn("+---+-----+---+", body)

    def test_simple_tables_become_gfm_tables(self):
        _, body = rst_to_markdown(
            "==============  =========\n"
            " Name            Status\n"
            "==============  =========\n"
            " ceph-osd        healthy\n"
            " ceph-mgr        ready\n"
            "==============  =========\n"
        )

        self.assertIn("| Name | Status |\n| --- | --- |", body)
        self.assertIn("| ceph-osd | healthy |", body)
        self.assertNotIn("==============  =========", body)

    def test_grid_tables_inside_code_directives_remain_code(self):
        _, body = rst_to_markdown(
            ".. code-block:: text\n\n"
            "   +------+--------+\n"
            "   | NAME | STATUS |\n"
            "   +------+--------+\n"
        )

        self.assertIn("```text\n+------+--------+\n| NAME | STATUS |\n+------+--------+\n```", body)
        self.assertNotIn("| NAME | STATUS |\n| --- | --- |", body)

    def test_table_directive_becomes_gfm_table(self):
        _, body = rst_to_markdown(
            ".. table:: Status meanings\n\n"
            "   ================ ===========================================\n"
            "   Status           Meaning\n"
            "   ================ ===========================================\n"
            "   New              Initial status\n"
            "   Resolved         Fix has been merged\n"
            "   ================ ===========================================\n"
        )

        self.assertIn("**Status meanings**", body)
        self.assertIn("| Status | Meaning |\n| --- | --- |", body)
        self.assertNotIn(".. table::", body)

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

    def test_images_and_includes_become_searchable_markdown(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary) / "repo"
            source = repo / "doc" / "page.rst"
            fragment = repo / "doc" / "fragment.inc.rst"
            source.parent.mkdir(parents=True)
            source.write_text(
                "Page\n====\n\n"
                ".. image:: diagram.svg\n   :alt: A diagram\n\n"
                ".. include:: fragment.inc.rst\n"
            )
            fragment.write_text("Included heading\n-----------------\n\nIncluded text.\n")
            (source.parent / "diagram.svg").write_text("<svg />")

            _, body = rst_to_markdown(
                source.read_text(),
                repo_dir=repo,
                source_path=source,
            )

            self.assertIn("![A diagram](diagram.svg)", body)
            self.assertIn("Included file `doc/fragment.inc.rst`:", body)
            self.assertIn("## Included heading", body)
            self.assertNotIn(".. image::", body)
            self.assertNotIn(".. include::", body)

    def test_rst_roles_named_refs_and_unresolved_refs_are_classified(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary) / "repo"
            source = repo / "doc" / "page.rst"
            target = repo / "doc" / "target.rst"
            source.parent.mkdir(parents=True)
            source.write_text("")
            target.write_text("")
            manifest = Manifest(
                name="test",
                collection="ceph",
                version="20.2.4",
                source_type="git",
                repo_url="https://github.com/ceph/ceph",
                git_ref="a" * 40,
                source_url_template="{repo_url}/blob/{git_ref}/{path}",
            )
            source_outputs = {"doc/page.rst": "page.md", "doc/target.rst": "target.md"}
            rst_targets = {
                "target": (target, "", "Target"),
                "external": (source, "https://example.com/", "External"),
            }

            body = _rewrite_rst_links(
                ".. _page-anchor:\n"
                "Read :ref:`Target <target>` and :doc:`Target doc <target.rst>`.\n"
                "Also use Target_ and `External`_.\n"
                "Missing :ref:`missing <missing>`.\n"
                "Anonymous link `External docs`__.\n"
                "__ https://example.com/anonymous\n"
                "Teaching text: ``:ref:`Target <target>``` and ``.. _page-anchor:``.\n"
                "```text\n:ref:`must stay code <target>`\n```\n",
                source,
                Path("page.md"),
                repo,
                source_outputs,
                manifest,
                rst_targets,
            )

            self.assertIn("[Target](target.md#target)", body)
            self.assertIn("[Target doc](target.md)", body)
            self.assertIn("[External](https://example.com/)", body)
            self.assertIn("[External docs](https://example.com/anonymous)", body)
            self.assertIn(
                "Missing missing <!-- unresolved-rst-link: kind=ref target=missing -->.",
                body,
            )
            self.assertIn(":ref:`must stay code <target>`", body)
            self.assertIn(":ref:`Target <target>`", body)
            self.assertIn(".. _page-anchor:", body)
            self.assertNotIn("-->_", body)

            blockquote = _rewrite_rst_links(
                "> :ref:`the\n> same procedures <target>`\n"
                "Spaced :download: `missing`.\n",
                source,
                Path("page.md"),
                repo,
                source_outputs,
                manifest,
                rst_targets,
            )
            self.assertIn("> [the same procedures](target.md#target)", blockquote)
            self.assertIn(
                "Spaced missing <!-- unresolved-rst-link: kind=download target=missing -->.",
                blockquote,
            )

            multiline = _rewrite_rst_links(
                "Read `The RADOS Object Store\n<https://ceph.io/rados>`_.\n",
                source,
                Path("page.md"),
                repo,
                source_outputs,
                manifest,
                rst_targets,
            )
            self.assertIn("[The RADOS Object Store](https://ceph.io/rados)", multiline)

            source.write_text("Accessing Shares\n================\n")
            section_targets = _collect_rst_targets([(source, "doc/page.rst")])
            same_page = _rewrite_rst_links(
                "See `Accessing Shares`_ for details.\n",
                source,
                Path("page.md"),
                repo,
                {"doc/page.rst": "page.md"},
                manifest,
                section_targets,
            )
            self.assertIn("[Accessing Shares](page.md#accessing-shares)", same_page)

            source.write_text(
                "Recovery/Backfill Options\n"
                "-------------------------\n\n"
                "See `Recovery/Backfill Options`_ for details.\n\n"
                "mClock ``Profile`` (HDD)!\n"
                "~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n"
                "See ``mClock Profile (HDD)!``_.\n\n"
                "Understanding mon_status\n"
                "^^^^^^^^^^^^^^^^^^^^^^^^\n\n"
                "See `Understanding mon_status`_.\n\n"
                "``cluster_fsid``\n"
                "\"\"\"\"\"\"\"\"\"\"\"\"\"\n\n"
                "See ``cluster_fsid``_.\n"
            )
            punctuation_targets = _collect_rst_targets([(source, "doc/page.rst")])
            _, punctuation_body = rst_to_markdown(
                source.read_text(),
                repo_dir=repo,
                source_path=source,
                preserve_rst_links=True,
            )
            punctuation_link = _rewrite_rst_links(
                punctuation_body,
                source,
                Path("page.md"),
                repo,
                {"doc/page.rst": "page.md"},
                manifest,
                punctuation_targets,
            )
            self.assertIn(
                "# Recovery/Backfill Options",
                punctuation_link,
            )
            self.assertIn(
                "[Recovery/Backfill Options](page.md#recoverybackfill-options)",
                punctuation_link,
            )
            self.assertIn(
                "## mClock ``Profile`` (HDD)!",
                punctuation_link,
            )
            self.assertIn(
                "[mClock Profile (HDD)!](page.md#mclock-profile-hdd)",
                punctuation_link,
            )
            self.assertIn(
                "[Understanding mon_status](page.md#understanding-mon_status)",
                punctuation_link,
            )
            self.assertIn(
                "[cluster_fsid](page.md#cluster_fsid)",
                punctuation_link,
            )

            anonymous_order = _rewrite_rst_links(
                "Read `First wrapped\nlink`__ and then `Second single`__.\n"
                "__ https://example.com/first\n"
                "__ https://example.com/second\n",
                source,
                Path("page.md"),
                repo,
                source_outputs,
                manifest,
                rst_targets,
            )
            self.assertIn(
                "[First wrapped link](https://example.com/first) and then "
                "[Second single](https://example.com/second).",
                anonymous_order,
            )

    def test_local_document_target_wins_same_label_collision(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary) / "repo"
            source = repo / "doc" / "index.rst"
            colliding = repo / "doc" / "radosgw" / "config-ref.rst"
            architecture = repo / "doc" / "architecture.rst"
            colliding.parent.mkdir(parents=True)
            source.parent.mkdir(parents=True, exist_ok=True)
            source.write_text(
                "See our `Architecture`_ section.\n\n"
                ".. _Architecture: architecture\n"
            )
            colliding.write_text(
                ".. _Architecture: ../../architecture#data-striping\n"
            )
            architecture.write_text("Architecture\n============\n")
            manifest = Manifest(
                name="test",
                collection="ceph",
                version="20.2.4",
                source_type="git",
                repo_url="https://github.com/ceph/ceph",
                git_ref="a" * 40,
                source_url_template="{repo_url}/blob/{git_ref}/{path}",
            )
            source_outputs = {
                "doc/index.rst": "index.md",
                "doc/radosgw/config-ref.rst": "radosgw/config-ref.md",
                "doc/architecture.rst": "architecture.md",
            }
            targets = _collect_rst_targets(
                [
                    (source, "doc/index.rst"),
                    (colliding, "doc/radosgw/config-ref.rst"),
                    (architecture, "doc/architecture.rst"),
                ]
            )

            rendered = _rewrite_rst_links(
                source.read_text(),
                source,
                Path("index.md"),
                repo,
                source_outputs,
                manifest,
                targets,
            )

            self.assertIn("[Architecture](architecture.md)", rendered)
            self.assertNotIn("architecture.md#data-striping", rendered)

    def test_named_reference_rewrite_scales_with_large_rst_target_set(self):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary) / "repo"
            source = repo / "doc" / "page.rst"
            source.parent.mkdir(parents=True)
            source.write_text("")
            manifest = Manifest(
                name="test",
                collection="ceph",
                version="20.2.4",
                source_type="git",
                repo_url="https://github.com/ceph/ceph",
                git_ref="a" * 40,
                source_url_template="{repo_url}/blob/{git_ref}/{path}",
            )
            target = repo / "doc" / "target.rst"
            target.write_text("")
            source_outputs = {"doc/page.rst": "page.md", "doc/target.rst": "target.md"}
            rst_targets = {
                f"label-{index}": (target, "", f"label-{index}")
                for index in range(1_348)
            }
            body = "ordinary prose without references\n" * 10_000
            started = time.perf_counter()
            rewritten = _rewrite_rst_links(
                body,
                source,
                Path("page.md"),
                repo,
                source_outputs,
                manifest,
                rst_targets,
            )
            elapsed = time.perf_counter() - started

            self.assertEqual(rewritten, body)
            self.assertLess(elapsed, 3.0, f"RST link rewrite regressed to slow target scans: {elapsed:.3f}s")

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
            external = _rewrite_source_links(
                "[Kerberos](https://en.wikipedia.org/wiki/Kerberos_(protocol))",
                source,
                Path("page.md"),
                repo,
                {"doc/page.rst": "page.md", "doc/target.rst": "target.md"},
                manifest,
            )
            self.assertEqual(
                external,
                "[Kerberos](https://en.wikipedia.org/wiki/Kerberos_(protocol))",
            )
            pinned = _rewrite_source_links(
                "![Diagram](https://github.com/ceph/ceph/blob/master/doc/diagram.svg)",
                source,
                Path("page.md"),
                repo,
                {"doc/page.rst": "page.md", "doc/target.rst": "target.md"},
                manifest,
            )
            self.assertIn("/blob/" + "a" * 40 + "/doc/diagram.svg", pinned)
            missing = _rewrite_source_links(
                "[Missing](missing-page)",
                source,
                Path("page.md"),
                repo,
                {"doc/page.rst": "page.md", "doc/target.rst": "target.md"},
                manifest,
            )
            self.assertEqual(
                missing,
                "[Missing](missing-page) <!-- unresolved-source-link: target=missing-page -->",
            )

    def test_explicit_link_does_not_consume_prose_comparison(self):
        _, body = rst_to_markdown(
            "libfuse < 3.0.0 (`pr#34769 <https://tracker.ceph.com/issues/34769>`_, maintainer)\n"
        )

        self.assertIn(
            "libfuse < 3.0.0 ([pr#34769](https://tracker.ceph.com/issues/34769), maintainer)",
            body,
        )

    def test_empty_source_is_not_a_document(self):
        self.assertFalse(_has_source_content(""))
        self.assertFalse(_has_source_content(" \n\t\n"))
        self.assertTrue(_has_source_content("# Real document\n"))


if __name__ == "__main__":
    unittest.main()
