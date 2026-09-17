---
collection: python
version: "3.12.14"
title: "marshal — Internal Python object serialization"
source_url: https://docs.python.org/3.12/library/marshal.html
fetched_at: 2026-09-17T15:32:54+00:00
---
# `marshal` — Internal Python object serialization

---

This module contains functions that can read and write Python values in a binary
format. The format is specific to Python, but independent of machine
architecture issues (e.g., you can write a Python value to a file on a PC,
transport the file to a Mac, and read it back there). Details of the format are
undocumented on purpose; it may change between Python versions (although it
rarely does). [[1]](marshal.md#id2)

This is not a general “persistence” module. For general persistence and
transfer of Python objects through RPC calls, see the modules [`pickle`](pickle.md#module-pickle "pickle: Convert Python objects to streams of bytes and back.") and
[`shelve`](shelve.md#module-shelve "shelve: Python object persistence."). The [`marshal`](marshal.md#module-marshal "marshal: Convert Python objects to streams of bytes and back (with different constraints).") module exists mainly to support reading and
writing the “pseudo-compiled” code for Python modules of `.pyc` files.
Therefore, the Python maintainers reserve the right to modify the marshal format
in backward incompatible ways should the need arise. If you’re serializing and
de-serializing Python objects, use the [`pickle`](pickle.md#module-pickle "pickle: Convert Python objects to streams of bytes and back.") module instead – the
performance is comparable, version independence is guaranteed, and pickle
supports a substantially wider range of objects than marshal.

> **Warning:**
>
> The [`marshal`](marshal.md#module-marshal "marshal: Convert Python objects to streams of bytes and back (with different constraints).") module is not intended to be secure against erroneous or
> maliciously constructed data. Never unmarshal data received from an
> untrusted or unauthenticated source.

Not all Python object types are supported; in general, only objects whose value
is independent from a particular invocation of Python can be written and read by
this module. The following types are supported: booleans, integers, floating-point
numbers, complex numbers, strings, bytes, bytearrays, tuples, lists, sets,
frozensets, dictionaries, and code objects, where it should be understood that
tuples, lists, sets, frozensets and dictionaries are only supported as long as
the values contained therein are themselves supported. The
singletons [`None`](constants.md#None "None"), [`Ellipsis`](constants.md#Ellipsis "Ellipsis") and [`StopIteration`](exceptions.md#StopIteration "StopIteration") can also be
marshalled and unmarshalled.
For format *version* lower than 3, recursive lists, sets and dictionaries cannot
be written (see below).

There are functions that read/write files as well as functions operating on
bytes-like objects.

The module defines these functions:

`marshal.dump(value, file[, version])`
:   Write the value on the open file. The value must be a supported type. The
    file must be a writeable [binary file](https://docs.python.org/3.12/glossary.html#term-binary-file).

    If the value has (or contains an object that has) an unsupported type, a
    [`ValueError`](exceptions.md#ValueError "ValueError") exception is raised — but garbage data will also be written
    to the file. The object will not be properly read back by [`load()`](marshal.md#marshal.load "marshal.load").

    The *version* argument indicates the data format that `dump` should use
    (see below).

    Raises an [auditing event](sys.md#auditing) `marshal.dumps` with arguments `value`, `version`.

`marshal.load(file)`
:   Read one value from the open file and return it. If no valid value is read
    (e.g. because the data has a different Python version’s incompatible marshal
    format), raise [`EOFError`](exceptions.md#EOFError "EOFError"), [`ValueError`](exceptions.md#ValueError "ValueError") or [`TypeError`](exceptions.md#TypeError "TypeError"). The
    file must be a readable [binary file](https://docs.python.org/3.12/glossary.html#term-binary-file).

    Raises an [auditing event](sys.md#auditing) `marshal.load` with no arguments.

    > **Note:**
    >
    > If an object containing an unsupported type was marshalled with [`dump()`](marshal.md#marshal.dump "marshal.dump"),
    > [`load()`](marshal.md#marshal.load "marshal.load") will substitute `None` for the unmarshallable type.

    Changed in version 3.10: This call used to raise a `code.__new__` audit event for each code object. Now
    it raises a single `marshal.load` event for the entire load operation.

`marshal.dumps(value[, version])`
:   Return the bytes object that would be written to a file by `dump(value, file)`. The
    value must be a supported type. Raise a [`ValueError`](exceptions.md#ValueError "ValueError") exception if value
    has (or contains an object that has) an unsupported type.

    The *version* argument indicates the data format that `dumps` should use
    (see below).

    Raises an [auditing event](sys.md#auditing) `marshal.dumps` with arguments `value`, `version`.

`marshal.loads(bytes)`
:   Convert the [bytes-like object](https://docs.python.org/3.12/glossary.html#term-bytes-like-object) to a value. If no valid value is found, raise
    [`EOFError`](exceptions.md#EOFError "EOFError"), [`ValueError`](exceptions.md#ValueError "ValueError") or [`TypeError`](exceptions.md#TypeError "TypeError"). Extra bytes in the
    input are ignored.

    Raises an [auditing event](sys.md#auditing) `marshal.loads` with argument `bytes`.

    Changed in version 3.10: This call used to raise a `code.__new__` audit event for each code object. Now
    it raises a single `marshal.loads` event for the entire load operation.

In addition, the following constants are defined:

`marshal.version`
:   Indicates the format that the module uses. Version 0 is the historical
    format, version 1 shares interned strings and version 2 uses a binary format
    for floating-point numbers.
    Version 3 adds support for object instancing and recursion.
    The current version is 4.

Footnotes

[[1](marshal.md#id1)]

The name of this module stems from a bit of terminology used by the designers of
Modula-3 (amongst others), who use the term “marshalling” for shipping of data
around in a self-contained form. Strictly speaking, “to marshal” means to
convert some data from internal to external form (in an RPC buffer for instance)
and “unmarshalling” for the reverse process.
