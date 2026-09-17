---
collection: python
version: "3.10.21"
title: "Custom Python Interpreters"
source_url: https://docs.python.org/3.10/library/custominterp.html
fetched_at: 2026-09-17T15:15:02+00:00
---
# Custom Python Interpreters

The modules described in this chapter allow writing interfaces similar to
Python’s interactive interpreter. If you want a Python interpreter that
supports some special feature in addition to the Python language, you should
look at the [`code`](code.md#module-code "code: Facilities to implement read-eval-print loops.") module. (The [`codeop`](codeop.md#module-codeop "codeop: Compile (possibly incomplete) Python code.") module is lower-level, used
to support compiling a possibly incomplete chunk of Python code.)

The full list of modules described in this chapter is:

- [`code` — Interpreter base classes](code.md)
  - [Interactive Interpreter Objects](code.md#interactive-interpreter-objects)
  - [Interactive Console Objects](code.md#interactive-console-objects)
- [`codeop` — Compile Python code](codeop.md)
