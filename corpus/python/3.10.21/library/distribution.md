---
collection: python
version: "3.10.21"
title: "Software Packaging and Distribution"
source_url: https://docs.python.org/3.10/library/distribution.html
fetched_at: 2026-09-17T15:14:53+00:00
---
# Software Packaging and Distribution

These libraries help you with publishing and installing Python software.
While these modules are designed to work in conjunction with the
[Python Package Index](https://pypi.org), they can also be used
with a local index server, or without any index server at all.

- [`distutils` — Building and installing Python modules](distutils.md)
- [`ensurepip` — Bootstrapping the `pip` installer](ensurepip.md)
  - [Command line interface](ensurepip.md#command-line-interface)
  - [Module API](ensurepip.md#module-api)
- [`venv` — Creation of virtual environments](venv.md)
  - [Creating virtual environments](venv.md#creating-virtual-environments)
  - [How venvs work](venv.md#how-venvs-work)
  - [API](venv.md#api)
  - [An example of extending `EnvBuilder`](venv.md#an-example-of-extending-envbuilder)
- [`zipapp` — Manage executable Python zip archives](zipapp.md)
  - [Basic Example](zipapp.md#basic-example)
  - [Command-Line Interface](zipapp.md#command-line-interface)
  - [Python API](zipapp.md#python-api)
  - [Examples](zipapp.md#examples)
  - [Specifying the Interpreter](zipapp.md#specifying-the-interpreter)
  - [Creating Standalone Applications with zipapp](zipapp.md#creating-standalone-applications-with-zipapp)
    - [Making a Windows executable](zipapp.md#making-a-windows-executable)
    - [Caveats](zipapp.md#caveats)
  - [The Python Zip Application Archive Format](zipapp.md#the-python-zip-application-archive-format)
