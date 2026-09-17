---
collection: python
version: "3.10.21"
title: "fnmatch — Unix filename pattern matching"
source_url: https://docs.python.org/3.10/library/fnmatch.html
fetched_at: 2026-09-17T15:13:47+00:00
---
# `fnmatch` — Unix filename pattern matching

**Source code:** [Lib/fnmatch.py](https://github.com/python/cpython/tree/3.10/Lib/fnmatch.py)

---

This module provides support for Unix shell-style wildcards, which are *not* the
same as regular expressions (which are documented in the [`re`](re.md#module-re "re: Regular expression operations.") module). The
special characters used in shell-style wildcards are:

| Pattern | Meaning |
| --- | --- |
| `*` | matches everything |
| `?` | matches any single character |
| `[seq]` | matches any character in *seq* |
| `[!seq]` | matches any character not in *seq* |

For a literal match, wrap the meta-characters in brackets.
For example, `'[?]'` matches the character `'?'`.

Note that the filename separator (`'/'` on Unix) is *not* special to this
module. See module [`glob`](glob.md#module-glob "glob: Unix shell style pathname pattern expansion.") for pathname expansion ([`glob`](glob.md#module-glob "glob: Unix shell style pathname pattern expansion.") uses
[`filter()`](fnmatch.md#fnmatch.filter "fnmatch.filter") to match pathname segments). Similarly, filenames starting with
a period are not special for this module, and are matched by the `*` and `?`
patterns.

`fnmatch.fnmatch(filename, pattern)`
:   Test whether the *filename* string matches the *pattern* string, returning
    [`True`](constants.md#True "True") or [`False`](constants.md#False "False"). Both parameters are case-normalized
    using [`os.path.normcase()`](os.path.md#os.path.normcase "os.path.normcase"). [`fnmatchcase()`](fnmatch.md#fnmatch.fnmatchcase "fnmatch.fnmatchcase") can be used to perform a
    case-sensitive comparison, regardless of whether that’s standard for the
    operating system.

    This example will print all file names in the current directory with the
    extension `.txt`:

    ```python3
    import fnmatch
    import os

    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.txt'):
            print(file)
    ```

`fnmatch.fnmatchcase(filename, pattern)`
:   Test whether *filename* matches *pattern*, returning [`True`](constants.md#True "True") or
    [`False`](constants.md#False "False"); the comparison is case-sensitive and does not apply
    [`os.path.normcase()`](os.path.md#os.path.normcase "os.path.normcase").

`fnmatch.filter(names, pattern)`
:   Construct a list from those elements of the iterable *names* that match *pattern*. It is the same as
    `[n for n in names if fnmatch(n, pattern)]`, but implemented more efficiently.

`fnmatch.translate(pattern)`
:   Return the shell-style *pattern* converted to a regular expression for
    using with [`re.match()`](re.md#re.match "re.match").

    Example:

    ```
    >>> import fnmatch, re
    >>>
    >>> regex = fnmatch.translate('*.txt')
    >>> regex
    '(?s:.*\\.txt)\\Z'
    >>> reobj = re.compile(regex)
    >>> reobj.match('foobar.txt')
    <re.Match object; span=(0, 10), match='foobar.txt'>
    ```

> **See also:**
>
> Module [`glob`](glob.md#module-glob "glob: Unix shell style pathname pattern expansion.")
> :   Unix shell-style path expansion.
