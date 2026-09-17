import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common import Manifest
from normalize import to_markdown

SIGNATURE_PAGE = """
<html><body><div class="body" role="main">
<h1><a class="reference internal" href="#module-os" title="os: Miscellaneous operating
system interfaces."><code class="xref py py-mod"><span class="pre">os</span></code></a>
&#8212; Miscellaneous operating system interfaces</h1>
<h2>See also <a class="reference internal" href="shutil.html#module-shutil"><code
class="xref py py-mod"><span class="pre">shutil</span></code></a></h2>
<dl class="py function">
<dt id="os.getcwd">
<code class="sig-prename descclassname">os.</code><code class="sig-name descname">getcwd</code><span
class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink"
href="#os.getcwd" title="Permalink to this definition">&#182;</a></dt>
<dd><p>Return a string representing the current working directory.</p></dd>
</dl>
<dl class="py exception">
<dt id="os.error">
<em class="property">exception </em><code class="sig-prename descclassname">os.</code><code
class="sig-name descname">error</code></dt>
<dd><p>An alias for the built-in OSError exception.</p></dd>
</dl>
</div></body></html>
"""


def manifest(collection: str) -> Manifest:
    return Manifest(
        name=f"{collection}-test",
        collection=collection,
        version="1.0",
        base_url="https://docs.python.org/3.10/library/",
        content_selector="div.body[role=main]",
    )


# Sphinx 4 之後的簽章片段是 span，不是 code；3.12 文件屬於這一種。
MODERN_SIGNATURE_PAGE = """
<html><body><div class="body" role="main">
<h1>os — Miscellaneous operating system interfaces</h1>
<dl class="py function">
<dt class="sig sig-object py" id="os.getcwd">
<span class="sig-prename descclassname"><span class="pre">os.</span></span><span
class="sig-name descname"><span class="pre">getcwd</span></span><span
class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink"
href="#os.getcwd" title="Link to this definition">&#182;</a></dt>
<dd><p>Return a string representing the current working directory.</p></dd>
</dl>
</div></body></html>
"""


class SphinxSignatureTests(unittest.TestCase):
    def test_python_signature_becomes_one_inline_code_span(self):
        _, markdown = to_markdown(
            SIGNATURE_PAGE, "https://docs.python.org/3.10/library/os.html", manifest("python")
        )
        self.assertIn("`os.getcwd()`", markdown)
        self.assertIn("`exception os.error`", markdown)
        self.assertNotIn("`os.``getcwd`", markdown)

    def test_other_collections_keep_their_existing_conversion(self):
        _, markdown = to_markdown(
            SIGNATURE_PAGE, "https://docs.python.org/3.10/library/os.html", manifest("kernel")
        )
        self.assertNotIn("`os.getcwd()`", markdown)
        self.assertIn("`os.``getcwd`", markdown)

    def test_self_link_in_heading_is_unwrapped_but_cross_page_link_stays(self):
        _, markdown = to_markdown(
            SIGNATURE_PAGE, "https://docs.python.org/3.10/library/os.html", manifest("python")
        )
        self.assertIn("# `os` — Miscellaneous operating system interfaces", markdown)
        self.assertIn("## See also [`shutil`](shutil.md#module-shutil)", markdown)

    def test_span_based_signature_is_merged_like_the_code_based_one(self):
        _, markdown = to_markdown(
            MODERN_SIGNATURE_PAGE,
            "https://docs.python.org/3.12/library/os.html",
            manifest("python"),
        )
        self.assertIn("`os.getcwd()`", markdown)

    def test_page_title_and_body_survive_the_merge(self):
        title, markdown = to_markdown(
            SIGNATURE_PAGE, "https://docs.python.org/3.10/library/os.html", manifest("python")
        )
        self.assertEqual(title, "os — Miscellaneous operating system interfaces")
        self.assertIn("Return a string representing the current working directory.", markdown)


if __name__ == "__main__":
    unittest.main()
