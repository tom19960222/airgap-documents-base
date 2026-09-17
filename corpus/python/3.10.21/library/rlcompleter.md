---
collection: python
version: "3.10.21"
title: "rlcompleter — Completion function for GNU readline"
source_url: https://docs.python.org/3.10/library/rlcompleter.html
fetched_at: 2026-09-17T15:13:30+00:00
---
# `rlcompleter` — Completion function for GNU readline

**Source code:** [Lib/rlcompleter.py](https://github.com/python/cpython/tree/3.10/Lib/rlcompleter.py)

---

The [`rlcompleter`](rlcompleter.md#module-rlcompleter "rlcompleter: Python identifier completion, suitable for the GNU readline library.") module defines a completion function suitable for the
[`readline`](readline.md#module-readline "readline: GNU readline support for Python. (Unix)") module by completing valid Python identifiers and keywords.

When this module is imported on a Unix platform with the [`readline`](readline.md#module-readline "readline: GNU readline support for Python. (Unix)") module
available, an instance of the `Completer` class is automatically created
and its `complete()` method is set as the [`readline`](readline.md#module-readline "readline: GNU readline support for Python. (Unix)") completer.

Example:

```python3
>>> import rlcompleter
>>> import readline
>>> readline.parse_and_bind("tab: complete")
>>> readline. <TAB PRESSED>
readline.__doc__          readline.get_line_buffer(  readline.read_init_file(
readline.__file__         readline.insert_text(      readline.set_completer(
readline.__name__         readline.parse_and_bind(
>>> readline.
```

The [`rlcompleter`](rlcompleter.md#module-rlcompleter "rlcompleter: Python identifier completion, suitable for the GNU readline library.") module is designed for use with Python’s
[interactive mode](https://docs.python.org/3.10/tutorial/interpreter.html#tut-interactive). Unless Python is run with the
[`-S`](https://docs.python.org/3.10/using/cmdline.html#cmdoption-S) option, the module is automatically imported and configured
(see [Readline configuration](site.md#rlcompleter-config)).

On platforms without [`readline`](readline.md#module-readline "readline: GNU readline support for Python. (Unix)"), the `Completer` class defined by
this module can still be used for custom purposes.

## Completer Objects

Completer objects have the following method:

`Completer.complete(text, state)`
:   Return the *state*th completion for *text*.

    If called for *text* that doesn’t include a period character (`'.'`), it will
    complete from names currently defined in [`__main__`](__main__.md#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``."), [`builtins`](builtins.md#module-builtins "builtins: The module that provides the built-in namespace.") and
    keywords (as defined by the [`keyword`](keyword.md#module-keyword "keyword: Test whether a string is a keyword in Python.") module).

    If called for a dotted name, it will try to evaluate anything without obvious
    side-effects (functions will not be evaluated, but it can generate calls to
    `__getattr__()`) up to the last part, and find matches for the rest via the
    [`dir()`](functions.md#dir "dir") function. Any exception raised during the evaluation of the
    expression is caught, silenced and [`None`](constants.md#None "None") is returned.
