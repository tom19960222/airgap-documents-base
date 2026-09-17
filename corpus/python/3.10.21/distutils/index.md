---
collection: python
version: "3.10.21"
title: "Distributing Python Modules (Legacy version)"
source_url: https://docs.python.org/3.10/distutils/index.html
fetched_at: 2026-09-17T15:15:40+00:00
---
# Distributing Python Modules (Legacy version)

Authors
:   Greg Ward, Anthony Baxter

Email
:   [distutils-sig@python.org](mailto:distutils-sig%40python.org)

> **See also:**
>
> [Distributing Python Modules](https://docs.python.org/3.10/distributing/index.html#distributing-index)
> :   The up to date module distribution documentations

> **Note:**
>
> The entire `distutils` package has been deprecated and will be
> removed in Python 3.12. This documentation is retained as a
> reference only, and will be removed with the package. See the
> [What’s New](https://docs.python.org/3.10/whatsnew/3.10.html#distutils-deprecated) entry for more information.

> **Note:**
>
> This document is being retained solely until the `setuptools` documentation
> at <https://setuptools.readthedocs.io/en/latest/setuptools.html>
> independently covers all of the relevant information currently included here.

> **Note:**
>
> This guide only covers the basic tools for building and distributing
> extensions that are provided as part of this version of Python. Third party
> tools offer easier to use and more secure alternatives. Refer to the [quick
> recommendations section](https://packaging.python.org/guides/tool-recommendations/)
> in the Python Packaging User Guide for more information.

This document describes the Python Distribution Utilities (“Distutils”) from
the module developer’s point of view, describing the underlying capabilities
that `setuptools` builds on to allow Python developers to make Python modules
and extensions readily available to a wider audience.

- [1. An Introduction to Distutils](introduction.md)
  - [1.1. Concepts & Terminology](introduction.md#concepts-terminology)
  - [1.2. A Simple Example](introduction.md#a-simple-example)
  - [1.3. General Python terminology](introduction.md#general-python-terminology)
  - [1.4. Distutils-specific terminology](introduction.md#distutils-specific-terminology)
- [2. Writing the Setup Script](setupscript.md)
  - [2.1. Listing whole packages](setupscript.md#listing-whole-packages)
  - [2.2. Listing individual modules](setupscript.md#listing-individual-modules)
  - [2.3. Describing extension modules](setupscript.md#describing-extension-modules)
  - [2.4. Relationships between Distributions and Packages](setupscript.md#relationships-between-distributions-and-packages)
  - [2.5. Installing Scripts](setupscript.md#installing-scripts)
  - [2.6. Installing Package Data](setupscript.md#installing-package-data)
  - [2.7. Installing Additional Files](setupscript.md#installing-additional-files)
  - [2.8. Additional meta-data](setupscript.md#additional-meta-data)
  - [2.9. Debugging the setup script](setupscript.md#debugging-the-setup-script)
- [3. Writing the Setup Configuration File](configfile.md)
- [4. Creating a Source Distribution](sourcedist.md)
  - [4.1. Specifying the files to distribute](sourcedist.md#specifying-the-files-to-distribute)
  - [4.2. Manifest-related options](sourcedist.md#manifest-related-options)
- [5. Creating Built Distributions](builtdist.md)
  - [5.1. Creating RPM packages](builtdist.md#creating-rpm-packages)
  - [5.2. Cross-compiling on Windows](builtdist.md#cross-compiling-on-windows)
- [6. Distutils Examples](examples.md)
  - [6.1. Pure Python distribution (by module)](examples.md#pure-python-distribution-by-module)
  - [6.2. Pure Python distribution (by package)](examples.md#pure-python-distribution-by-package)
  - [6.3. Single extension module](examples.md#single-extension-module)
  - [6.4. Checking a package](examples.md#checking-a-package)
  - [6.5. Reading the metadata](examples.md#reading-the-metadata)
- [7. Extending Distutils](extending.md)
  - [7.1. Integrating new commands](extending.md#integrating-new-commands)
  - [7.2. Adding new distribution types](extending.md#adding-new-distribution-types)
- [8. Command Reference](commandref.md)
  - [8.1. Installing modules: the **install** command family](commandref.md#installing-modules-the-install-command-family)
  - [8.2. Creating a source distribution: the **sdist** command](commandref.md#creating-a-source-distribution-the-sdist-command)
- [9. API Reference](apiref.md)
  - [9.1. `distutils.core` — Core Distutils functionality](apiref.md#module-distutils.core)
  - [9.2. `distutils.ccompiler` — CCompiler base class](apiref.md#module-distutils.ccompiler)
  - [9.3. `distutils.unixccompiler` — Unix C Compiler](apiref.md#module-distutils.unixccompiler)
  - [9.4. `distutils.msvccompiler` — Microsoft Compiler](apiref.md#module-distutils.msvccompiler)
  - [9.5. `distutils.bcppcompiler` — Borland Compiler](apiref.md#module-distutils.bcppcompiler)
  - [9.6. `distutils.cygwincompiler` — Cygwin Compiler](apiref.md#module-distutils.cygwinccompiler)
  - [9.7. `distutils.archive_util` — Archiving utilities](apiref.md#module-distutils.archive_util)
  - [9.8. `distutils.dep_util` — Dependency checking](apiref.md#module-distutils.dep_util)
  - [9.9. `distutils.dir_util` — Directory tree operations](apiref.md#module-distutils.dir_util)
  - [9.10. `distutils.file_util` — Single file operations](apiref.md#module-distutils.file_util)
  - [9.11. `distutils.util` — Miscellaneous other utility functions](apiref.md#module-distutils.util)
  - [9.12. `distutils.dist` — The Distribution class](apiref.md#module-distutils.dist)
  - [9.13. `distutils.extension` — The Extension class](apiref.md#module-distutils.extension)
  - [9.14. `distutils.debug` — Distutils debug mode](apiref.md#module-distutils.debug)
  - [9.15. `distutils.errors` — Distutils exceptions](apiref.md#module-distutils.errors)
  - [9.16. `distutils.fancy_getopt` — Wrapper around the standard getopt module](apiref.md#module-distutils.fancy_getopt)
  - [9.17. `distutils.filelist` — The FileList class](apiref.md#module-distutils.filelist)
  - [9.18. `distutils.log` — Simple **PEP 282**-style logging](apiref.md#module-distutils.log)
  - [9.19. `distutils.spawn` — Spawn a sub-process](apiref.md#module-distutils.spawn)
  - [9.20. `distutils.sysconfig` — System configuration information](apiref.md#module-distutils.sysconfig)
  - [9.21. `distutils.text_file` — The TextFile class](apiref.md#module-distutils.text_file)
  - [9.22. `distutils.version` — Version number classes](apiref.md#module-distutils.version)
  - [9.23. `distutils.cmd` — Abstract base class for Distutils commands](apiref.md#module-distutils.cmd)
  - [9.24. Creating a new Distutils command](apiref.md#creating-a-new-distutils-command)
  - [9.25. `distutils.command` — Individual Distutils commands](apiref.md#module-distutils.command)
  - [9.26. `distutils.command.bdist` — Build a binary installer](apiref.md#module-distutils.command.bdist)
  - [9.27. `distutils.command.bdist_packager` — Abstract base class for packagers](apiref.md#module-distutils.command.bdist_packager)
  - [9.28. `distutils.command.bdist_dumb` — Build a “dumb” installer](apiref.md#module-distutils.command.bdist_dumb)
  - [9.29. `distutils.command.bdist_msi` — Build a Microsoft Installer binary package](apiref.md#module-distutils.command.bdist_msi)
  - [9.30. `distutils.command.bdist_rpm` — Build a binary distribution as a Redhat RPM and SRPM](apiref.md#module-distutils.command.bdist_rpm)
  - [9.31. `distutils.command.sdist` — Build a source distribution](apiref.md#module-distutils.command.sdist)
  - [9.32. `distutils.command.build` — Build all files of a package](apiref.md#module-distutils.command.build)
  - [9.33. `distutils.command.build_clib` — Build any C libraries in a package](apiref.md#module-distutils.command.build_clib)
  - [9.34. `distutils.command.build_ext` — Build any extensions in a package](apiref.md#module-distutils.command.build_ext)
  - [9.35. `distutils.command.build_py` — Build the .py/.pyc files of a package](apiref.md#module-distutils.command.build_py)
  - [9.36. `distutils.command.build_scripts` — Build the scripts of a package](apiref.md#module-distutils.command.build_scripts)
  - [9.37. `distutils.command.clean` — Clean a package build area](apiref.md#module-distutils.command.clean)
  - [9.38. `distutils.command.config` — Perform package configuration](apiref.md#module-distutils.command.config)
  - [9.39. `distutils.command.install` — Install a package](apiref.md#module-distutils.command.install)
  - [9.40. `distutils.command.install_data` — Install data files from a package](apiref.md#module-distutils.command.install_data)
  - [9.41. `distutils.command.install_headers` — Install C/C++ header files from a package](apiref.md#module-distutils.command.install_headers)
  - [9.42. `distutils.command.install_lib` — Install library files from a package](apiref.md#module-distutils.command.install_lib)
  - [9.43. `distutils.command.install_scripts` — Install script files from a package](apiref.md#module-distutils.command.install_scripts)
  - [9.44. `distutils.command.register` — Register a module with the Python Package Index](apiref.md#module-distutils.command.register)
  - [9.45. `distutils.command.check` — Check the meta-data of a package](apiref.md#module-distutils.command.check)
