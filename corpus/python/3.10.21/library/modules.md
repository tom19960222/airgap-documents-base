---
collection: python
version: "3.10.21"
title: "Importing Modules"
source_url: https://docs.python.org/3.10/library/modules.html
fetched_at: 2026-09-17T15:15:03+00:00
---
# Importing Modules

The modules described in this chapter provide new ways to import other Python
modules and hooks for customizing the import process.

The full list of modules described in this chapter is:

- [`zipimport` — Import modules from Zip archives](zipimport.md)
  - [zipimporter Objects](zipimport.md#zipimporter-objects)
  - [Examples](zipimport.md#examples)
- [`pkgutil` — Package extension utility](pkgutil.md)
- [`modulefinder` — Find modules used by a script](modulefinder.md)
  - [Example usage of `ModuleFinder`](modulefinder.md#example-usage-of-modulefinder)
- [`runpy` — Locating and executing Python modules](runpy.md)
- [`importlib` — The implementation of `import`](importlib.md)
  - [Introduction](importlib.md#introduction)
  - [Functions](importlib.md#functions)
  - [`importlib.abc` – Abstract base classes related to import](importlib.md#module-importlib.abc)
  - [`importlib.resources` – Resources](importlib.md#module-importlib.resources)
  - [`importlib.machinery` – Importers and path hooks](importlib.md#module-importlib.machinery)
  - [`importlib.util` – Utility code for importers](importlib.md#module-importlib.util)
  - [Examples](importlib.md#examples)
    - [Importing programmatically](importlib.md#importing-programmatically)
    - [Checking if a module can be imported](importlib.md#checking-if-a-module-can-be-imported)
    - [Importing a source file directly](importlib.md#importing-a-source-file-directly)
    - [Implementing lazy imports](importlib.md#implementing-lazy-imports)
    - [Setting up an importer](importlib.md#setting-up-an-importer)
    - [Approximating `importlib.import_module()`](importlib.md#approximating-importlib-import-module)
- [Using `importlib.metadata`](importlib.metadata.md)
  - [Overview](importlib.metadata.md#overview)
  - [Functional API](importlib.metadata.md#functional-api)
    - [Entry points](importlib.metadata.md#entry-points)
    - [Distribution metadata](importlib.metadata.md#distribution-metadata)
    - [Distribution versions](importlib.metadata.md#distribution-versions)
    - [Distribution files](importlib.metadata.md#distribution-files)
    - [Distribution requirements](importlib.metadata.md#distribution-requirements)
    - [Package distributions](importlib.metadata.md#package-distributions)
  - [Distributions](importlib.metadata.md#distributions)
  - [Extending the search algorithm](importlib.metadata.md#extending-the-search-algorithm)
