---
collection: libvirt
version: "12.7.0"
title: "Bindings for other languages and integration API modules"
source_url: https://libvirt.org/bindings.html
fetched_at: 2026-08-21T04:10:11+00:00
---
# Bindings for other languages and integration API modules

Libvirt supports C and C++ directly, and has bindings available for
other languages:

- **C#**: Arnaud Champion develops [C# bindings](csharp.md).
- **Go**: Daniel Berrange develops [Go
  bindings](https://pkg.go.dev/libvirt.org/go/libvirt).
- **Java**: Daniel Veillard develops [Java bindings](https://java.libvirt.org/).
- **OCaml**: Richard Jones develops [OCaml
  bindings](https://ocaml.libvirt.org/).
- **Perl**: Daniel Berrange develops [Perl
  bindings](https://search.cpan.org/dist/Sys-Virt/).
- **PHP**: Radek Hladik started developing [PHP
  bindings](https://php.libvirt.org/) in 2010.

  In February 2011 the binding development has been moved to the
  libvirt.org website as libvirt-php project.

  The project is now maintained by Michal Novotny and it's heavily
  based on Radek's version. For more information, including information
  on posting patches to libvirt-php, please refer to the [PHP
  bindings](https://php.libvirt.org/) site.
- **Python**: Libvirt's python bindings are split to a separate
  [package](https://gitlab.com/libvirt/libvirt-python) since version
  1.2.0, older versions came with direct support for the Python
  language.

  If your libvirt is installed as packages, rather than compiled by you
  from source code, ensure you have the appropriate package installed.

  This is named **libvirt-python** on RHEL/Fedora,
  [python-libvirt](https://packages.ubuntu.com/search?keywords=python-libvirt)
  on Ubuntu, and may be named differently on others.

  For usage information, see the [Python API bindings](python.md)
  page.
- **Ruby**: Chris Lalancette develops [Ruby
  bindings](https://ruby.libvirt.org/).

Integration API modules:

- **D-Bus**: Pavel Hrdina develops [D-Bus API](dbus.md).

For information on using libvirt on **Windows** [please see the Windows
support page](windows.md).

Support, requests or help for libvirt bindings are welcome on the
[devel mailing list](https://lists.libvirt.org/admin/lists/devel.lists.libvirt.org/),
as usual try to provide enough background information and make sure you
use recent version, see the [help page](bugs.md).
