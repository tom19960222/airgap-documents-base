import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common import Manifest
from normalize import to_markdown

MANIFEST = Manifest(
    name="python-3.12",
    collection="python",
    version="3.12.14",
    base_url="https://docs.python.org/3.12/library/",
    content_selector="div[role=main]",
)
PAGE_URL = "https://docs.python.org/3.12/library/asyncio-task.html"


def convert(body: str) -> str:
    html = f'<html><body><div class="body" role="main">{body}</div></body></html>'
    return to_markdown(html, PAGE_URL, MANIFEST)[1]


class TocBackrefTests(unittest.TestCase):
    def test_contents_backref_heading_keeps_text_without_self_link(self):
        markdown = convert(
            '<h2><a class="toc-backref" href="#id2" role="doc-backlink">Coroutines</a>'
            '<a class="headerlink" href="#coroutines">¶</a></h2>'
        )
        self.assertIn("## Coroutines", markdown)
        self.assertNotIn("](asyncio-task.md#id2)", markdown)

    def test_cross_reference_link_in_heading_is_preserved(self):
        markdown = convert(
            '<h2><a class="reference internal" href="ast.html#module-ast">'
            "<code>ast</code></a></h2>"
        )
        self.assertIn("## [`ast`](ast.md#module-ast)", markdown)

    def test_module_target_self_link_in_heading_is_unwrapped(self):
        markdown = convert(
            '<h1><a class="reference internal" href="#module-asyncio">'
            "<code>asyncio</code></a> — Asynchronous I/O</h1>"
        )
        self.assertIn("# `asyncio` — Asynchronous I/O", markdown)

    def test_same_page_anchor_in_body_text_is_kept(self):
        markdown = convert('<p>See <a href="#id9">Eager Task Factory</a>.</p>')
        self.assertIn("[Eager Task Factory](asyncio-task.md#id9)", markdown)


if __name__ == "__main__":
    unittest.main()
