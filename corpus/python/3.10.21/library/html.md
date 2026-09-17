---
collection: python
version: "3.10.21"
title: "html — HyperText Markup Language support"
source_url: https://docs.python.org/3.10/library/html.html
fetched_at: 2026-09-17T15:14:20+00:00
---
# `html` — HyperText Markup Language support

**Source code:** [Lib/html/__init__.py](https://github.com/python/cpython/tree/3.10/Lib/html/__init__.py)

---

This module defines utilities to manipulate HTML.

`html.escape(s, quote=True)`
:   Convert the characters `&`, `<` and `>` in string *s* to HTML-safe
    sequences. Use this if you need to display text that might contain such
    characters in HTML. If the optional flag *quote* is true, the characters
    (`"`) and (`'`) are also translated; this helps for inclusion in an HTML
    attribute value delimited by quotes, as in `<a href="...">`.

    New in version 3.2.

`html.unescape(s)`
:   Convert all named and numeric character references (e.g. `&gt;`,
    `&#62;`, `&#x3e;`) in the string *s* to the corresponding Unicode
    characters. This function uses the rules defined by the HTML 5 standard
    for both valid and invalid character references, and the [`list of
    HTML 5 named character references`](html.entities.md#html.entities.html5 "html.entities.html5").

    New in version 3.4.

---

Submodules in the `html` package are:

- [`html.parser`](html.parser.md#module-html.parser "html.parser: A simple parser that can handle HTML and XHTML.") – HTML/XHTML parser with lenient parsing mode
- [`html.entities`](html.entities.md#module-html.entities "html.entities: Definitions of HTML general entities.") – HTML entity definitions
