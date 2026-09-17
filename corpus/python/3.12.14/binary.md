---
collection: python
version: "3.12.14"
title: "Binary Data Services"
source_url: https://docs.python.org/3.12/library/binary.html
fetched_at: 2026-09-17T15:32:17+00:00
---
# Binary Data Services

The modules described in this chapter provide some basic services operations
for manipulation of binary data. Other operations on binary data, specifically
in relation to file formats and network protocols, are described in the
relevant sections.

Some libraries described under [Text Processing Services](text.md#textservices) also work with either
ASCII-compatible binary formats (for example, [`re`](re.md#module-re "re: Regular expression operations.")) or all binary data
(for example, [`difflib`](difflib.md#module-difflib "difflib: Helpers for computing differences between objects.")).

In addition, see the documentation for Python’s built-in binary data types in
[Binary Sequence Types — bytes, bytearray, memoryview](stdtypes.md#binaryseq).

- [`struct` — Interpret bytes as packed binary data](struct.md)
  - [Functions and Exceptions](struct.md#functions-and-exceptions)
  - [Format Strings](struct.md#format-strings)
    - [Byte Order, Size, and Alignment](struct.md#byte-order-size-and-alignment)
    - [Format Characters](struct.md#format-characters)
    - [Examples](struct.md#examples)
  - [Applications](struct.md#applications)
    - [Native Formats](struct.md#native-formats)
    - [Standard Formats](struct.md#standard-formats)
  - [Classes](struct.md#classes)
- [`codecs` — Codec registry and base classes](codecs.md)
  - [Codec Base Classes](codecs.md#codec-base-classes)
    - [Error Handlers](codecs.md#error-handlers)
    - [Stateless Encoding and Decoding](codecs.md#stateless-encoding-and-decoding)
    - [Incremental Encoding and Decoding](codecs.md#incremental-encoding-and-decoding)
      - [IncrementalEncoder Objects](codecs.md#incrementalencoder-objects)
      - [IncrementalDecoder Objects](codecs.md#incrementaldecoder-objects)
    - [Stream Encoding and Decoding](codecs.md#stream-encoding-and-decoding)
      - [StreamWriter Objects](codecs.md#streamwriter-objects)
      - [StreamReader Objects](codecs.md#streamreader-objects)
      - [StreamReaderWriter Objects](codecs.md#streamreaderwriter-objects)
      - [StreamRecoder Objects](codecs.md#streamrecoder-objects)
  - [Encodings and Unicode](codecs.md#encodings-and-unicode)
  - [Standard Encodings](codecs.md#standard-encodings)
  - [Python Specific Encodings](codecs.md#python-specific-encodings)
    - [Text Encodings](codecs.md#text-encodings)
    - [Binary Transforms](codecs.md#binary-transforms)
    - [Text Transforms](codecs.md#text-transforms)
  - [`encodings.idna` — Internationalized Domain Names in Applications](codecs.md#module-encodings.idna)
  - [`encodings.mbcs` — Windows ANSI codepage](codecs.md#module-encodings.mbcs)
  - [`encodings.utf_8_sig` — UTF-8 codec with BOM signature](codecs.md#module-encodings.utf_8_sig)
