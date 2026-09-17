---
collection: python
version: "3.10.21"
title: "builtins — Built-in objects"
source_url: https://docs.python.org/3.10/library/builtins.html
fetched_at: 2026-09-17T15:14:57+00:00
---
# `builtins` — Built-in objects

---

This module provides direct access to all ‘built-in’ identifiers of Python; for
example, `builtins.open` is the full name for the built-in function
[`open()`](functions.md#open "open"). See [Built-in Functions](functions.md#built-in-funcs) and [Built-in Constants](constants.md#built-in-consts) for
documentation.

This module is not normally accessed explicitly by most applications, but can be
useful in modules that provide objects with the same name as a built-in value,
but in which the built-in of that name is also needed. For example, in a module
that wants to implement an [`open()`](functions.md#open "open") function that wraps the built-in
[`open()`](functions.md#open "open"), this module can be used directly:

```python3
import builtins

def open(path):
    f = builtins.open(path, 'r')
    return UpperCaser(f)

class UpperCaser:
    '''Wrapper around a file that converts output to upper-case.'''

    def __init__(self, f):
        self._f = f

    def read(self, count=-1):
        return self._f.read(count).upper()

    # ...
```

As an implementation detail, most modules have the name `__builtins__` made
available as part of their globals. The value of `__builtins__` is normally
either this module or the value of this module’s [`__dict__`](stdtypes.md#object.__dict__ "object.__dict__") attribute.
Since this is an implementation detail, it may not be used by alternate
implementations of Python.
