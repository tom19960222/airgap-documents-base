---
collection: libvirt
version: "12.7.0"
title: "virt-host-validate"
source_url: https://libvirt.org/manpages/virt-host-validate.html
fetched_at: 2026-08-21T04:10:31+00:00
---
# virt-host-validate

validate host virtualization setup

Manual section
:   1

Manual group
:   Virtualization Support

Contents

- [SYNOPSIS](virt-host-validate.md#synopsis)
- [DESCRIPTION](virt-host-validate.md#description)
- [OPTIONS](virt-host-validate.md#options)
- [EXIT STATUS](virt-host-validate.md#exit-status)
- [AUTHOR](virt-host-validate.md#author)
- [BUGS](virt-host-validate.md#bugs)
- [COPYRIGHT](virt-host-validate.md#copyright)
- [LICENSE](virt-host-validate.md#license)
- [SEE ALSO](virt-host-validate.md#see-also)

# [SYNOPSIS](virt-host-validate.md#id1)

virt-host-validate [*OPTIONS*...] [*HV-TYPE*]

# [DESCRIPTION](virt-host-validate.md#id2)

This tool validates that the host is configured in a suitable
way to run libvirt hypervisor drivers. If invoked without any
arguments it will check support for all hypervisor drivers it
is aware of. Optionally it can be given a particular hypervisor
type (qemu, lxc or bhyve) to restrict the checks
to those relevant for that virtualization technology

# [OPTIONS](virt-host-validate.md#id3)

-v, --version

Display the command version

-h, --help

Display the command line help

-q, --quiet

Don't display details of individual checks being performed.
Only display output if a check does not pass.

# [EXIT STATUS](virt-host-validate.md#id4)

Upon successful validation, an exit status of 0 will be set. Upon
failure a non-zero status will be set.

# [AUTHOR](virt-host-validate.md#id5)

Daniel P. Berrangé

# [BUGS](virt-host-validate.md#id6)

Please report all bugs you discover. This should be done via either:

1. the mailing list

   <https://libvirt.org/contact.html>
2. the bug tracker

   [https://libvirt.org/bugs.html](../bugs.md)

Alternatively, you may report bugs to your software distributor / vendor.

# [COPYRIGHT](virt-host-validate.md#id7)

Copyright (C) 2012 by Red Hat, Inc.

# [LICENSE](virt-host-validate.md#id8)

virt-host-validate is distributed under the terms of the GNU GPL v2+.
This is free software; see the source for copying conditions. There
is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE

# [SEE ALSO](virt-host-validate.md#id9)

virsh(1), virt-pki-validate(1), virt-xml-validate(1),
[https://libvirt.org/](../index.md)
