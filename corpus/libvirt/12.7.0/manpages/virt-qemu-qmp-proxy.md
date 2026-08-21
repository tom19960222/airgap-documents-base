---
collection: libvirt
version: "12.7.0"
title: "virt-qemu-qmp-proxy"
source_url: https://libvirt.org/manpages/virt-qemu-qmp-proxy.html
fetched_at: 2026-08-21T04:10:37+00:00
---
# virt-qemu-qmp-proxy

Expose a QMP proxy server for a libvirt QEMU guest

Manual section
:   1

Manual group
:   Virtualization Support

Contents

- [SYNOPSIS](virt-qemu-qmp-proxy.md#synopsis)
- [DESCRIPTION](virt-qemu-qmp-proxy.md#description)
- [OPTIONS](virt-qemu-qmp-proxy.md#options)
- [EXIT STATUS](virt-qemu-qmp-proxy.md#exit-status)
- [AUTHOR](virt-qemu-qmp-proxy.md#author)
- [BUGS](virt-qemu-qmp-proxy.md#bugs)
- [COPYRIGHT](virt-qemu-qmp-proxy.md#copyright)
- [LICENSE](virt-qemu-qmp-proxy.md#license)
- [SEE ALSO](virt-qemu-qmp-proxy.md#see-also)

# [SYNOPSIS](virt-qemu-qmp-proxy.md#id1)

virt-qemu-qmp-proxy [*OPTION*]... *DOMAIN* *QMP-SOCKET-PATH*

# [DESCRIPTION](virt-qemu-qmp-proxy.md#id2)

This tool provides a way to expose a QMP proxy server that communicates
with a QEMU guest managed by libvirt. This enables standard QMP client
tools to interact with libvirt managed guests.

**NOTE: use of this tool will result in the running QEMU guest being
marked as tainted.** It is strongly recommended that this tool *only be
used to send commands which query information* about the running guest.
If this tool is used to make changes to the state of the guest, this
may have negative interactions with the QEMU driver, resulting in an
inability to manage the guest operation thereafter, and in the worst
case **potentially lead to data loss or corruption**.

The virt-qemu-qmp-proxy program will listen on a UNIX socket for incoming
client connections, and run the QMP protocol over the connection. Any
commands received will be sent to the running libvirt guest, and replies
sent back.

The virt-qemu-qmp-proxy program may be interrupted (eg Ctrl-C) when it
is no longer required. The libvirt QEMU guest will continue running.

# [OPTIONS](virt-qemu-qmp-proxy.md#id3)

*DOMAIN*

The ID or UUID or Name of the libvirt QEMU guest.

*QMP-SOCKET-PATH*

The filesystem path at which to run the QMP server, listening for
incoming connections.

-c *CONNECTION-URI*
--connect=*CONNECTION-URI*

The URI for the connection to the libvirt QEMU driver. If omitted,
a URI will be auto-detected.

-v, --verbose

Run in verbose mode, printing all QMP commands and replies that
are handled.

-h, --help

Display the command line help.

# [EXIT STATUS](virt-qemu-qmp-proxy.md#id4)

Upon successful shutdown, an exit status of 0 will be set. Upon
failure a non-zero status will be set.

# [AUTHOR](virt-qemu-qmp-proxy.md#id5)

Daniel P. Berrangé

# [BUGS](virt-qemu-qmp-proxy.md#id6)

Please report all bugs you discover. This should be done via either:

1. the mailing list

   <https://libvirt.org/contact.html>
2. the bug tracker

   [https://libvirt.org/bugs.html](../bugs.md)

Alternatively, you may report bugs to your software distributor / vendor.

# [COPYRIGHT](virt-qemu-qmp-proxy.md#id7)

Copyright (C) 2022 by Red Hat, Inc.

# [LICENSE](virt-qemu-qmp-proxy.md#id8)

virt-qemu-qmp-proxy is distributed under the terms of the GNU LGPL v2+.
This is free software; see the source for copying conditions. There
is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE

# [SEE ALSO](virt-qemu-qmp-proxy.md#id9)

virsh(1), [https://libvirt.org/](../index.md),
[QMP reference](https://www.qemu.org/docs/master/interop/qemu-qmp-ref.html)
