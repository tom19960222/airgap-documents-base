---
collection: libvirt
version: "12.7.0"
title: "C# API bindings"
source_url: https://libvirt.org/csharp.html
fetched_at: 2026-08-21T04:10:12+00:00
---
# C# API bindings

# Description

The C# libvirt bindings are a class library. They use a Microsoft Visual Studio
project architecture, and have been tested with Windows .NET, and Mono, on both
Linux and Windows.

Compiling them produces **LibvirtBindings.dll**, which can be added as a .NET
reference to any .NET project needing access to libvirt.

# Requirements

These bindings depend upon the libvirt libraries being installed.

In the .NET case, this is **libvirt-0.dll**, produced from compiling libvirt for
windows.

# GIT source repository

The C# bindings source code is maintained in a git repository available on
[gitlab.com](https://gitlab.com/libvirt/libvirt-csharp):

```
git clone https://gitlab.com/libvirt/libvirt-csharp.git
```

# Authors

The C# bindings are the work of Arnaud Champion <[arnaud.champion AT
devatom.fr](mailto:arnaud.champion%20AT%20devatom.fr)>, based upon the
previous work of Jaromír Červenka.
