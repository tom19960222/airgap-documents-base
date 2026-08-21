---
collection: libvirt
version: "12.7.0"
title: "virt-pki-validate"
source_url: https://libvirt.org/manpages/virt-pki-validate.html
fetched_at: 2026-08-21T04:10:31+00:00
---
# virt-pki-validate

validate libvirt PKI files are configured correctly

Manual section
:   1

Manual group
:   Virtualization Support

Contents

- [SYNOPSIS](virt-pki-validate.md#synopsis)
- [DESCRIPTION](virt-pki-validate.md#description)
- [OPTIONS](virt-pki-validate.md#options)
- [EXIT STATUS](virt-pki-validate.md#exit-status)
- [AUTHOR](virt-pki-validate.md#author)
- [BUGS](virt-pki-validate.md#bugs)
- [COPYRIGHT](virt-pki-validate.md#copyright)
- [LICENSE](virt-pki-validate.md#license)
- [SEE ALSO](virt-pki-validate.md#see-also)

# [SYNOPSIS](virt-pki-validate.md#id1)

virt-pki-validate [*OPTION*] [trust|server|client]

# [DESCRIPTION](virt-pki-validate.md#id2)

This tool validates that the necessary PKI files are configured for
a secure libvirt server or client using the TLS encryption protocol.
It will report any missing certificate or key files on the host. It
should be run as root to ensure it can read all the necessary files

With no arguments it will check the trusted CA config, the server
config and the client config. The optional positional argument can
be used to restrict the checks to just one of these three sets.

# [OPTIONS](virt-pki-validate.md#id3)

-h, --help

Display command line help usage then exit.

-V, --version

Display version information then exit.

# [EXIT STATUS](virt-pki-validate.md#id4)

Upon successful validation, an exit status of 0 will be set. Upon
failure a non-zero status will be set.

# [AUTHOR](virt-pki-validate.md#id5)

Daniel Veillard, Daniel P. Berrangé

# [BUGS](virt-pki-validate.md#id6)

Please report all bugs you discover. This should be done via either:

1. the mailing list

   <https://libvirt.org/contact.html>
2. the bug tracker

   [https://libvirt.org/bugs.html](../bugs.md)

Alternatively, you may report bugs to your software distributor / vendor.

# [COPYRIGHT](virt-pki-validate.md#id7)

Copyright (C) 2006-2024 by Red Hat, Inc.

# [LICENSE](virt-pki-validate.md#id8)

virt-pki-validate is distributed under the terms of the GNU GPL v2+.
This is free software; see the source for copying conditions. There
is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE

# [SEE ALSO](virt-pki-validate.md#id9)

virsh(1), [online PKI setup instructions](../remote.md),
[https://libvirt.org/](../index.md)
