---
collection: libvirt
version: "12.7.0"
title: "virt-pki-query-dn"
source_url: https://libvirt.org/manpages/virt-pki-query-dn.html
fetched_at: 2026-08-21T04:10:36+00:00
---
# virt-pki-query-dn

extract Distinguished Name from a PEM certificate

Manual section
:   1

Manual group
:   Virtualization Support

Contents

- [SYNOPSIS](virt-pki-query-dn.md#synopsis)
- [DESCRIPTION](virt-pki-query-dn.md#description)
- [OPTIONS](virt-pki-query-dn.md#options)
- [EXIT STATUS](virt-pki-query-dn.md#exit-status)
- [AUTHOR](virt-pki-query-dn.md#author)
- [BUGS](virt-pki-query-dn.md#bugs)
- [COPYRIGHT](virt-pki-query-dn.md#copyright)
- [LICENSE](virt-pki-query-dn.md#license)
- [SEE ALSO](virt-pki-query-dn.md#see-also)

# [SYNOPSIS](virt-pki-query-dn.md#id1)

virt-pki-query-dn [*OPTION*]... *FILE*

# [DESCRIPTION](virt-pki-query-dn.md#id2)

Extract Distinguished Name from a PEM certificate.

The output is meant to be used in the tls_allowed_dn_list
configuration option in the libvirtd.conf file.

# [OPTIONS](virt-pki-query-dn.md#id3)

-h, --help

Display command line help usage then exit.

-V, --version

Display version information then exit.

# [EXIT STATUS](virt-pki-query-dn.md#id4)

The exit status will be zero on success, non-zero on failure.

# [AUTHOR](virt-pki-query-dn.md#id5)

Martin Kletzander

# [BUGS](virt-pki-query-dn.md#id6)

Please report all bugs you discover. This should be done via either:

1. the mailing list

   <https://libvirt.org/contact.html>
2. the bug tracker

   [https://libvirt.org/bugs.html](../bugs.md)

Alternatively, you may report bugs to your software distributor / vendor.

# [COPYRIGHT](virt-pki-query-dn.md#id7)

Copyright (C) 2021 Red Hat, Inc.

# [LICENSE](virt-pki-query-dn.md#id8)

virt-pki-query-dn is distributed under the terms of the GNU GPL v2+.
This is free software; see the source for copying conditions. There
is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE.

# [SEE ALSO](virt-pki-query-dn.md#id9)

virsh(1), virt-pki-validate(1),
[online PKI setup instructions](../remote.md),
[https://libvirt.org/](../index.md)
