---
collection: python
version: "3.12.14"
title: "html.entities — Definitions of HTML general entities"
source_url: https://docs.python.org/3.12/library/html.entities.html
fetched_at: 2026-09-17T15:33:51+00:00
---
# `html.entities` — Definitions of HTML general entities

**Source code:** [Lib/html/entities.py](https://github.com/python/cpython/tree/3.12/Lib/html/entities.py)

---

This module defines four dictionaries, [`html5`](html.entities.md#html.entities.html5 "html.entities.html5"),
[`name2codepoint`](html.entities.md#html.entities.name2codepoint "html.entities.name2codepoint"), [`codepoint2name`](html.entities.md#html.entities.codepoint2name "html.entities.codepoint2name"), and [`entitydefs`](html.entities.md#html.entities.entitydefs "html.entities.entitydefs").

html.entities.html5
:   A dictionary that maps HTML5 named character references [[1]](html.entities.md#id2) to the
    equivalent Unicode character(s), e.g. `html5['gt;'] == '>'`.
    Note that the trailing semicolon is included in the name (e.g. `'gt;'`),
    however some of the names are accepted by the standard even without the
    semicolon: in this case the name is present with and without the `';'`.
    See also [`html.unescape()`](html.md#html.unescape "html.unescape").

    Added in version 3.3.

html.entities.entitydefs
:   A dictionary mapping XHTML 1.0 entity definitions to their replacement text in
    ISO Latin-1.

html.entities.name2codepoint
:   A dictionary that maps HTML4 entity names to the Unicode code points.

html.entities.codepoint2name
:   A dictionary that maps Unicode code points to HTML4 entity names.

Footnotes

[[1](html.entities.md#id1)]

See <https://html.spec.whatwg.org/multipage/named-characters.html#named-character-references>
