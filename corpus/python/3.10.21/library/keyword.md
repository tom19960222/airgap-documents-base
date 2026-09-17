---
collection: python
version: "3.10.21"
title: "keyword — Testing for Python keywords"
source_url: https://docs.python.org/3.10/library/keyword.html
fetched_at: 2026-09-17T15:15:08+00:00
---
# `keyword` — Testing for Python keywords

**Source code:** [Lib/keyword.py](https://github.com/python/cpython/tree/3.10/Lib/keyword.py)

---

This module allows a Python program to determine if a string is a
[keyword](https://docs.python.org/3.10/reference/lexical_analysis.html#keywords) or [soft keyword](https://docs.python.org/3.10/reference/lexical_analysis.html#soft-keywords).

`keyword.iskeyword(s)`
:   Return `True` if *s* is a Python [keyword](https://docs.python.org/3.10/reference/lexical_analysis.html#keywords).

`keyword.kwlist`
:   Sequence containing all the [keywords](https://docs.python.org/3.10/reference/lexical_analysis.html#keywords) defined for the
    interpreter. If any keywords are defined to only be active when particular
    [`__future__`](__future__.md#module-__future__ "__future__: Future statement definitions") statements are in effect, these will be included as well.

`keyword.issoftkeyword(s)`
:   Return `True` if *s* is a Python [soft keyword](https://docs.python.org/3.10/reference/lexical_analysis.html#soft-keywords).

    New in version 3.9.

`keyword.softkwlist`
:   Sequence containing all the [soft keywords](https://docs.python.org/3.10/reference/lexical_analysis.html#soft-keywords) defined for the
    interpreter. If any soft keywords are defined to only be active when particular
    [`__future__`](__future__.md#module-__future__ "__future__: Future statement definitions") statements are in effect, these will be included as well.

    New in version 3.9.
