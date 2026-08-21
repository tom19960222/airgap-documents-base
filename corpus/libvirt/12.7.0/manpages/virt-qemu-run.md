---
collection: libvirt
version: "12.7.0"
title: "virt-qemu-run"
source_url: https://libvirt.org/manpages/virt-qemu-run.html
fetched_at: 2026-08-21T04:10:35+00:00
---
# virt-qemu-run

Run a standalone QEMU guest

Manual section
:   1

Manual group
:   Virtualization Support

Contents

- [SYNOPSIS](virt-qemu-run.md#synopsis)
- [DESCRIPTION](virt-qemu-run.md#description)
- [OPTIONS](virt-qemu-run.md#options)
- [EXIT STATUS](virt-qemu-run.md#exit-status)
- [AUTHOR](virt-qemu-run.md#author)
- [BUGS](virt-qemu-run.md#bugs)
- [COPYRIGHT](virt-qemu-run.md#copyright)
- [LICENSE](virt-qemu-run.md#license)
- [SEE ALSO](virt-qemu-run.md#see-also)

# [SYNOPSIS](virt-qemu-run.md#id1)

virt-qemu-run [*OPTION*]... *GUEST-XML-FILE*

# [DESCRIPTION](virt-qemu-run.md#id2)

This tool provides a way to run a standalone QEMU guest such that it
is completely independent of libvirtd. It makes use of the embedded
QEMU driver support to run the VM placing files under an isolated
directory tree. When the guest is run with this tool it is invisible
to libvirtd and thus also invisible to other libvirt tools such as
virsh.

The virt-qemu-run program will run the QEMU virtual machine, and
then block until the guest OS shuts down, at which point it will
exit.

If the virt-qemu-run program is interrupted (eg Ctrl-C) it will
immediately terminate the virtual machine without giving the guest OS
any opportunity to gracefully shutdown.

**NOTE: this tool is currently considered experimental.** Its
usage and behaviour is still subject to change in future libvirt
releases. For further information on its usage consult the
[QEMU driver documentation](../drvqemu.md#embedded-driver).

# [OPTIONS](virt-qemu-run.md#id3)

*GUEST-XML-FILE*

The full path to the XML file describing the guest virtual machine
to be booted.

-r *DIR*, --root=*DIR*

Specify the root directory to use for storing state associated with
the virtual machine. The caller is responsible for deleting this
directory when it is no longer required.

If this parameter is omitted, then a random temporary directory
will be created, and its contents be automatically deleted at
VM shutdown.

-s *SECRET-XML-FILE*,*SECRET-VALUE-FILE*,
--secret=*SECRET-XML-FILE*,*SECRET-VALUE-FILE*

Specify a secret to be loaded into the secret driver.
*SECRET-XML-FILE* is a path to the XML description of the secret,
whose UUID should match a secret referenced in the guest domain XML.
*SECRET-VALUE-FILE* is a path containing the raw value of the secret.

-v, --verbose

Display verbose information about startup.

-h, --help

Display the command line help.

# [EXIT STATUS](virt-qemu-run.md#id4)

Upon successful shutdown, an exit status of 0 will be set. Upon
failure a non-zero status will be set.

# [AUTHOR](virt-qemu-run.md#id5)

Daniel P. Berrangé

# [BUGS](virt-qemu-run.md#id6)

Please report all bugs you discover. This should be done via either:

1. the mailing list

   <https://libvirt.org/contact.html>
2. the bug tracker

   [https://libvirt.org/bugs.html](../bugs.md)

Alternatively, you may report bugs to your software distributor / vendor.

# [COPYRIGHT](virt-qemu-run.md#id7)

Copyright (C) 2019 by Red Hat, Inc.

# [LICENSE](virt-qemu-run.md#id8)

virt-run-qemu is distributed under the terms of the GNU LGPL v2+.
This is free software; see the source for copying conditions. There
is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE

# [SEE ALSO](virt-qemu-run.md#id9)

virsh(1), [https://libvirt.org/](../index.md)
