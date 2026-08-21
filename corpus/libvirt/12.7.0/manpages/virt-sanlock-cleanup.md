---
collection: libvirt
version: "12.7.0"
title: "virt-sanlock-cleanup"
source_url: https://libvirt.org/manpages/virt-sanlock-cleanup.html
fetched_at: 2026-08-21T04:10:33+00:00
---
# virt-sanlock-cleanup

remove stale sanlock resource lease files

Manual section
:   8

Manual group
:   Virtualization Support

Contents

- [SYNOPSIS](virt-sanlock-cleanup.md#synopsis)
- [DESCRIPTION](virt-sanlock-cleanup.md#description)
- [EXIT STATUS](virt-sanlock-cleanup.md#exit-status)
- [AUTHOR](virt-sanlock-cleanup.md#author)
- [BUGS](virt-sanlock-cleanup.md#bugs)
- [COPYRIGHT](virt-sanlock-cleanup.md#copyright)
- [LICENSE](virt-sanlock-cleanup.md#license)
- [SEE ALSO](virt-sanlock-cleanup.md#see-also)

# [SYNOPSIS](virt-sanlock-cleanup.md#id1)

virt-sanlock-cleanup

# [DESCRIPTION](virt-sanlock-cleanup.md#id2)

This tool removes any resource lease files created by the sanlock
lock manager plugin. The resource lease files only need to exist
on disks when a guest using the resource is active. This script
reclaims the disk space used by resources which are not currently
active.

# [EXIT STATUS](virt-sanlock-cleanup.md#id3)

Upon successful processing of leases cleanup, an exit status
of 0 will be set. Upon fatal error a non-zero status will
be set.

# [AUTHOR](virt-sanlock-cleanup.md#id4)

Daniel P. Berrangé

# [BUGS](virt-sanlock-cleanup.md#id5)

Please report all bugs you discover. This should be done via either:

1. the mailing list

   <https://libvirt.org/contact.html>
2. the bug tracker

   [https://libvirt.org/bugs.html](../bugs.md)

Alternatively, you may report bugs to your software distributor / vendor.

# [COPYRIGHT](virt-sanlock-cleanup.md#id6)

Copyright (C) 2011, 2013 Red Hat, Inc.

# [LICENSE](virt-sanlock-cleanup.md#id7)

virt-sanlock-cleanup is distributed under the terms of the GNU GPL v2+.
This is free software; see the source for copying conditions. There
is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE

# [SEE ALSO](virt-sanlock-cleanup.md#id8)

virsh(1), [online instructions](../kbase/locking.md),
[https://libvirt.org/](../index.md)
