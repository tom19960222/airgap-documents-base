---
collection: python
version: "3.10.21"
title: "__future__ — Future statement definitions"
source_url: https://docs.python.org/3.10/library/__future__.html
fetched_at: 2026-09-17T15:15:00+00:00
---
# `__future__` — Future statement definitions

**Source code:** [Lib/__future__.py](https://github.com/python/cpython/tree/3.10/Lib/__future__.py)

---

[`__future__`](__future__.md#module-__future__ "__future__: Future statement definitions") is a real module, and serves three purposes:

- To avoid confusing existing tools that analyze import statements and expect to
  find the modules they’re importing.
- To ensure that [future statements](https://docs.python.org/3.10/reference/simple_stmts.html#future) run under releases prior to
  2.1 at least yield runtime exceptions (the import of [`__future__`](__future__.md#module-__future__ "__future__: Future statement definitions") will
  fail, because there was no module of that name prior to 2.1).
- To document when incompatible changes were introduced, and when they will be
  — or were — made mandatory. This is a form of executable documentation, and
  can be inspected programmatically via importing [`__future__`](__future__.md#module-__future__ "__future__: Future statement definitions") and examining
  its contents.

Each statement in `__future__.py` is of the form:

```python3
FeatureName = _Feature(OptionalRelease, MandatoryRelease,
                       CompilerFlag)
```

where, normally, *OptionalRelease* is less than *MandatoryRelease*, and both are
5-tuples of the same form as [`sys.version_info`](sys.md#sys.version_info "sys.version_info"):

```python3
(PY_MAJOR_VERSION, # the 2 in 2.1.0a3; an int
 PY_MINOR_VERSION, # the 1; an int
 PY_MICRO_VERSION, # the 0; an int
 PY_RELEASE_LEVEL, # "alpha", "beta", "candidate" or "final"; string
 PY_RELEASE_SERIAL # the 3; an int
)
```

*OptionalRelease* records the first release in which the feature was accepted.

In the case of a *MandatoryRelease* that has not yet occurred,
*MandatoryRelease* predicts the release in which the feature will become part of
the language.

Else *MandatoryRelease* records when the feature became part of the language; in
releases at or after that, modules no longer need a future statement to use the
feature in question, but may continue to use such imports.

*MandatoryRelease* may also be `None`, meaning that a planned feature got
dropped.

Instances of class `_Feature` have two corresponding methods,
`getOptionalRelease()` and `getMandatoryRelease()`.

*CompilerFlag* is the (bitfield) flag that should be passed in the fourth
argument to the built-in function [`compile()`](functions.md#compile "compile") to enable the feature in
dynamically compiled code. This flag is stored in the `compiler_flag`
attribute on `_Feature` instances.

No feature description will ever be deleted from [`__future__`](__future__.md#module-__future__ "__future__: Future statement definitions"). Since its
introduction in Python 2.1 the following features have found their way into the
language using this mechanism:

| feature | optional in | mandatory in | effect |
| --- | --- | --- | --- |
| nested_scopes | 2.1.0b1 | 2.2 | [**PEP 227**](https://www.python.org/dev/peps/pep-0227): *Statically Nested Scopes* |
| generators | 2.2.0a1 | 2.3 | [**PEP 255**](https://www.python.org/dev/peps/pep-0255): *Simple Generators* |
| division | 2.2.0a2 | 3.0 | [**PEP 238**](https://www.python.org/dev/peps/pep-0238): *Changing the Division Operator* |
| absolute_import | 2.5.0a1 | 3.0 | [**PEP 328**](https://www.python.org/dev/peps/pep-0328): *Imports: Multi-Line and Absolute/Relative* |
| with_statement | 2.5.0a1 | 2.6 | [**PEP 343**](https://www.python.org/dev/peps/pep-0343): *The “with” Statement* |
| print_function | 2.6.0a2 | 3.0 | [**PEP 3105**](https://www.python.org/dev/peps/pep-3105): *Make print a function* |
| unicode_literals | 2.6.0a2 | 3.0 | [**PEP 3112**](https://www.python.org/dev/peps/pep-3112): *Bytes literals in Python 3000* |
| generator_stop | 3.5.0b1 | 3.7 | [**PEP 479**](https://www.python.org/dev/peps/pep-0479): *StopIteration handling inside generators* |
| annotations | 3.7.0b1 | TBD [1](__future__.md#id2) | [**PEP 563**](https://www.python.org/dev/peps/pep-0563): *Postponed evaluation of annotations* |

[1](__future__.md#id1)
:   `from __future__ import annotations` was previously scheduled to
    become mandatory in Python 3.10, but the Python Steering Council
    twice decided to delay the change
    ([announcement for Python 3.10](https://mail.python.org/archives/list/python-dev@python.org/message/CLVXXPQ2T2LQ5MP2Y53VVQFCXYWQJHKZ/);
    [announcement for Python 3.11](https://mail.python.org/archives/list/python-dev@python.org/message/VIZEBX5EYMSYIJNDBF6DMUMZOCWHARSO/)).
    No final decision has been made yet. See also [**PEP 563**](https://www.python.org/dev/peps/pep-0563) and [**PEP 649**](https://www.python.org/dev/peps/pep-0649).

> **See also:**
>
> [Future statements](https://docs.python.org/3.10/reference/simple_stmts.html#future)
> :   How the compiler treats future imports.
