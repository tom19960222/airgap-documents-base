---
collection: python
version: "3.10.21"
title: "distutils — Building and installing Python modules"
source_url: https://docs.python.org/3.10/library/distutils.html
fetched_at: 2026-09-17T15:14:54+00:00
---
# `distutils` — Building and installing Python modules

---

[`distutils`](distutils.md#module-distutils "distutils: Support for building and installing Python modules into an existing Python installation.") is deprecated with removal planned for Python 3.12.
See the [What’s New](https://docs.python.org/3.10/whatsnew/3.10.html#distutils-deprecated) entry for more information.

---

The [`distutils`](distutils.md#module-distutils "distutils: Support for building and installing Python modules into an existing Python installation.") package provides support for building and installing
additional modules into a Python installation. The new modules may be either
100%-pure Python, or may be extension modules written in C, or may be
collections of Python packages which include modules coded in both Python and C.

Most Python users will *not* want to use this module directly, but instead
use the cross-version tools maintained by the Python Packaging Authority. In
particular,
[setuptools](https://setuptools.readthedocs.io/en/latest/) is an
enhanced alternative to [`distutils`](distutils.md#module-distutils "distutils: Support for building and installing Python modules into an existing Python installation.") that provides:

- support for declaring project dependencies
- additional mechanisms for configuring which files to include in source
  releases (including plugins for integration with version control systems)
- the ability to declare project “entry points”, which can be used as the
  basis for application plugin systems
- the ability to automatically generate Windows command line executables at
  installation time rather than needing to prebuild them
- consistent behaviour across all supported Python versions

The recommended [pip](https://pip.pypa.io/) installer runs all
`setup.py` scripts with `setuptools`, even if the script itself only
imports `distutils`. Refer to the
[Python Packaging User Guide](https://packaging.python.org) for more
information.

For the benefits of packaging tool authors and users seeking a deeper
understanding of the details of the current packaging and distribution
system, the legacy [`distutils`](distutils.md#module-distutils "distutils: Support for building and installing Python modules into an existing Python installation.") based user documentation and API
reference remain available:

- [Installing Python Modules (Legacy version)](https://docs.python.org/3.10/install/index.html#install-index)
- [Distributing Python Modules (Legacy version)](../distutils/index.md#distutils-index)
