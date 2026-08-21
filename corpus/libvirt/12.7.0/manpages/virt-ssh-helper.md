---
collection: libvirt
version: "12.7.0"
title: "virt-ssh-helper"
source_url: https://libvirt.org/manpages/virt-ssh-helper.html
fetched_at: 2026-08-21T04:10:37+00:00
---
# virt-ssh-helper

libvirt socket proxy

Manual section
:   8

Manual group
:   Virtualization Support

Contents

- [SYNOPSIS](virt-ssh-helper.md#synopsis)
- [DESCRIPTION](virt-ssh-helper.md#description)
- [OPTIONS](virt-ssh-helper.md#options)
- [EXIT STATUS](virt-ssh-helper.md#exit-status)
- [AUTHOR](virt-ssh-helper.md#author)
- [BUGS](virt-ssh-helper.md#bugs)
- [COPYRIGHT](virt-ssh-helper.md#copyright)
- [LICENSE](virt-ssh-helper.md#license)
- [SEE ALSO](virt-ssh-helper.md#see-also)

# [SYNOPSIS](virt-ssh-helper.md#id1)

virt-ssh-helper [*OPTION*]... *URI*

# [DESCRIPTION](virt-ssh-helper.md#id2)

virt-ssh-helper is an internal tool used to handle connections
coming from remote clients, and it's not intended to be called
directly by the user.

# [OPTIONS](virt-ssh-helper.md#id3)

*URI*

Local libvirt URI to connect the remote client to.

-r, --readonly

Make the connection read-only.

-h, --help

Display command line help usage then exit.

-V, --version

Display version information then exit.

# [EXIT STATUS](virt-ssh-helper.md#id4)

The exit status will be zero on success, non-zero on failure.

# [AUTHOR](virt-ssh-helper.md#id5)

Daniel P. Berrangé

# [BUGS](virt-ssh-helper.md#id6)

Please report all bugs you discover. This should be done via either:

1. the mailing list

   <https://libvirt.org/contact.html>
2. the bug tracker

   [https://libvirt.org/bugs.html](../bugs.md)

Alternatively, you may report bugs to your software distributor / vendor.

# [COPYRIGHT](virt-ssh-helper.md#id7)

Copyright (C) 2020 Red Hat, Inc.

# [LICENSE](virt-ssh-helper.md#id8)

virt-ssh-helper is distributed under the terms of the GNU LGPL v2+.
This is free software; see the source for copying conditions. There
is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE.

# [SEE ALSO](virt-ssh-helper.md#id9)

virsh(1), [https://libvirt.org/](../index.md)
