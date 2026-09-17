---
collection: kernel
version: "6.17"
title: "VFS iomap Documentation"
source_url: https://www.kernel.org/doc/html/v6.17/filesystems/iomap/index.html
fetched_at: 2026-09-16T16:41:56+00:00
---
# VFS iomap Documentation

- [1. Library Design](design.md)
  - [1.1. Introduction](design.md#introduction)
  - [1.2. Who Should Read This?](design.md#who-should-read-this)
  - [1.3. How Is This Better?](design.md#how-is-this-better)
  - [1.4. File Range Iterator](design.md#file-range-iterator)
  - [1.5. Preparing for File Operations](design.md#preparing-for-file-operations)
  - [1.6. Locking Hierarchy](design.md#locking-hierarchy)
  - [1.7. Bugs and Limitations](design.md#bugs-and-limitations)
- [2. Supported File Operations](operations.md)
  - [2.1. Buffered I/O](operations.md#buffered-i-o)
  - [2.2. Direct I/O](operations.md#direct-i-o)
  - [2.3. DAX I/O](operations.md#dax-i-o)
  - [2.4. Seeking Files](operations.md#seeking-files)
  - [2.5. Swap File Activation](operations.md#swap-file-activation)
  - [2.6. File Space Mapping Reporting](operations.md#file-space-mapping-reporting)
- [3. Porting Your Filesystem](porting.md)
  - [3.1. Why Convert?](porting.md#why-convert)
  - [3.2. How Do I Convert a Filesystem?](porting.md#how-do-i-convert-a-filesystem)
