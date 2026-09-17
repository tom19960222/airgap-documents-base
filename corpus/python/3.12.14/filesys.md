---
collection: python
version: "3.12.14"
title: "File and Directory Access"
source_url: https://docs.python.org/3.12/library/filesys.html
fetched_at: 2026-09-17T15:32:43+00:00
---
# File and Directory Access

The modules described in this chapter deal with disk files and directories. For
example, there are modules for reading the properties of files, manipulating
paths in a portable way, and creating temporary files. The full list of modules
in this chapter is:

- [`pathlib` — Object-oriented filesystem paths](pathlib.md)
  - [Basic use](pathlib.md#basic-use)
  - [Pure paths](pathlib.md#pure-paths)
    - [General properties](pathlib.md#general-properties)
    - [Operators](pathlib.md#operators)
    - [Accessing individual parts](pathlib.md#accessing-individual-parts)
    - [Methods and properties](pathlib.md#methods-and-properties)
  - [Concrete paths](pathlib.md#concrete-paths)
    - [Expanding and resolving paths](pathlib.md#expanding-and-resolving-paths)
    - [Querying file type and status](pathlib.md#querying-file-type-and-status)
    - [Reading and writing files](pathlib.md#reading-and-writing-files)
    - [Reading directories](pathlib.md#reading-directories)
    - [Creating files and directories](pathlib.md#creating-files-and-directories)
    - [Renaming and deleting](pathlib.md#renaming-and-deleting)
    - [Permissions and ownership](pathlib.md#permissions-and-ownership)
  - [Correspondence to tools in the `os` module](pathlib.md#correspondence-to-tools-in-the-os-module)
- [`os.path` — Common pathname manipulations](os.path.md)
- [`fileinput` — Iterate over lines from multiple input streams](fileinput.md)
- [`stat` — Interpreting `stat()` results](stat.md)
- [`filecmp` — File and Directory Comparisons](filecmp.md)
  - [The `dircmp` class](filecmp.md#the-dircmp-class)
- [`tempfile` — Generate temporary files and directories](tempfile.md)
  - [Examples](tempfile.md#examples)
  - [Deprecated functions and variables](tempfile.md#deprecated-functions-and-variables)
- [`glob` — Unix style pathname pattern expansion](glob.md)
- [`fnmatch` — Unix filename pattern matching](fnmatch.md)
- [`linecache` — Random access to text lines](linecache.md)
- [`shutil` — High-level file operations](shutil.md)
  - [Directory and files operations](shutil.md#directory-and-files-operations)
    - [Platform-dependent efficient copy operations](shutil.md#platform-dependent-efficient-copy-operations)
    - [copytree example](shutil.md#copytree-example)
    - [rmtree example](shutil.md#rmtree-example)
  - [Archiving operations](shutil.md#archiving-operations)
    - [Archiving example](shutil.md#archiving-example)
    - [Archiving example with *base_dir*](shutil.md#archiving-example-with-base-dir)
  - [Querying the size of the output terminal](shutil.md#querying-the-size-of-the-output-terminal)

> **See also:**
>
> Module [`os`](os.md#module-os "os: Miscellaneous operating system interfaces.")
> :   Operating system interfaces, including functions to work with files at a
>     lower level than Python [file objects](https://docs.python.org/3.12/glossary.html#term-file-object).
>
> Module [`io`](io.md#module-io "io: Core tools for working with streams.")
> :   Python’s built-in I/O library, including both abstract classes and
>     some concrete classes such as file I/O.
>
> Built-in function [`open()`](functions.md#open "open")
> :   The standard way to open files for reading and writing with Python.
