---
collection: python
version: "3.12.14"
title: "uu — Encode and decode uuencode files"
source_url: https://docs.python.org/3.12/library/uu.html
fetched_at: 2026-09-17T15:35:47+00:00
---
# `uu` — Encode and decode uuencode files

**Source code:** [Lib/uu.py](https://github.com/python/cpython/tree/3.12/Lib/uu.py)

Deprecated since version 3.11, will be removed in version 3.13: The [`uu`](uu.md#module-uu "uu: Encode and decode files in uuencode format. (deprecated)") module is deprecated
(see [**PEP 594**](https://peps.python.org/pep-0594/#uu-and-the-uu-encoding) for details).
[`base64`](base64.md#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85") is a modern alternative.

---

This module encodes and decodes files in uuencode format, allowing arbitrary
binary data to be transferred over ASCII-only connections. Wherever a file
argument is expected, the methods accept a file-like object. For backwards
compatibility, a string containing a pathname is also accepted, and the
corresponding file will be opened for reading and writing; the pathname `'-'`
is understood to mean the standard input or output. However, this interface is
deprecated; it’s better for the caller to open the file itself, and be sure
that, when required, the mode is `'rb'` or `'wb'` on Windows.

This code was contributed by Lance Ellinghouse, and modified by Jack Jansen.

The [`uu`](uu.md#module-uu "uu: Encode and decode files in uuencode format. (deprecated)") module defines the following functions:

uu.encode(*in_file*, *out_file*, *name=None*, *mode=None*, *\**, *backtick=False*)
:   Uuencode file *in_file* into file *out_file*. The uuencoded file will have
    the header specifying *name* and *mode* as the defaults for the results of
    decoding the file. The default defaults are taken from *in_file*, or `'-'`
    and `0o666` respectively. If *backtick* is true, zeros are represented by
    `` '`' `` instead of spaces.

    Changed in version 3.7: Added the *backtick* parameter.

uu.decode(*in_file*, *out_file=None*, *mode=None*, *quiet=False*)
:   This call decodes uuencoded file *in_file* placing the result on file
    *out_file*. If *out_file* is a pathname, *mode* is used to set the permission
    bits if the file must be created. Defaults for *out_file* and *mode* are taken
    from the uuencode header. However, if the file specified in the header already
    exists, a [`uu.Error`](uu.md#uu.Error "uu.Error") is raised.

    [`decode()`](uu.md#uu.decode "uu.decode") may print a warning to standard error if the input was produced
    by an incorrect uuencoder and Python could recover from that error. Setting
    *quiet* to a true value silences this warning.

*exception* uu.Error
:   Subclass of [`Exception`](exceptions.md#Exception "Exception"), this can be raised by [`uu.decode()`](uu.md#uu.decode "uu.decode") under
    various situations, such as described above, but also including a badly
    formatted header, or truncated input file.

> **See also:**
>
> Module [`binascii`](binascii.md#module-binascii "binascii: Tools for converting between binary and various ASCII-encoded binary representations.")
> :   Support module containing ASCII-to-binary and binary-to-ASCII conversions.
