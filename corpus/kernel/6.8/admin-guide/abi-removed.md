---
collection: kernel
version: "6.8"
title: "ABI removed symbols"
source_url: https://www.kernel.org/doc/html/v6.8/admin-guide/abi-removed.html
fetched_at: 2026-08-21T03:54:41+00:00
---
# ABI removed symbols

## Symbols under /sys/bus

|  |
| --- |
| **/sys/bus/nd/devices/regionX/nfit/ecc_unit_size** |

Defined on file [sysfs-bus-nfit](abi-removed.md#abi-file-removed-sysfs-bus-nfit)

(RO) Size of a write request to a DIMM that will not incur a
read-modify-write cycle at the memory controller.

When the nfit driver initializes it runs an ARS (Address Range
Scrub) operation across every pmem range. Part of that process
involves determining the ARS capabilities of a given address
range. One of the capabilities that is reported is the 'Clear
Uncorrectable Error Range Length Unit Size' (see: ACPI 6.2
section 9.20.7.4 Function Index 1 - Query ARS Capabilities).
This property indicates the boundary at which the NVDIMM may
need to perform read-modify-write cycles to maintain ECC (Error
Correcting Code) blocks.

## Symbols under /sys/class

|  |
| --- |
| **/sys/class/rfkill/rfkill[0-9]+/claim** |

Defined on file [sysfs-class-rfkill](abi-removed.md#abi-file-removed-sysfs-class-rfkill)

This file was deprecated because there no longer was a way to
claim just control over a single rfkill instance.
This file was scheduled to be removed in 2012, and was removed
in 2016.
Values: 0: Kernel handles events

## Symbols under /sys/devices

|  |
| --- |
| **/sys/devices/system/machinecheck/machinecheckX/tolerant** |

Defined on file [sysfs-mce](abi-removed.md#abi-file-removed-sysfs-mce)

Unused and obsolete after the advent of recoverable machine
checks (see last sentence below) and those are present since
2010 (Nehalem).

Original description:

The entries appear for each CPU, but they are truly shared
between all CPUs.

Tolerance level. When a machine check exception occurs for a
non corrected machine check the kernel can take different
actions.

Since machine check exceptions can happen any time it is
sometimes risky for the kernel to kill a process because it
defies normal kernel locking rules. The tolerance level
configures how hard the kernel tries to recover even at some
risk of deadlock. Higher tolerant values trade potentially
better uptime with the risk of a crash or even corruption
(for tolerant >= 3).

|  |  |
| --- | --- |
| 0 | always panic on uncorrected errors, log corrected errors |
| 1 | panic or SIGBUS on uncorrected errors, log corrected errors |
| 2 | SIGBUS or log uncorrected errors, log corrected errors |
| 3 | never panic or SIGBUS, log all errors (for testing only) |

Default: 1

Note this only makes a difference if the CPU allows recovery
from a machine check exception. Current x86 CPUs generally
do not.

## Symbols under /sys/fs

|  |
| --- |
| **/sys/fs/selinux/checkreqprot** |

Defined on file [sysfs-selinux-checkreqprot](abi-removed.md#abi-file-removed-sysfs-selinux-checkreqprot)

REMOVAL UPDATE: The SELinux checkreqprot functionality was removed in
March 2023, the original deprecation notice is shown below.

The selinuxfs "checkreqprot" node allows SELinux to be configured
to check the protection requested by userspace for mmap/mprotect
calls instead of the actual protection applied by the kernel.
This was a compatibility mechanism for legacy userspace and
for the READ_IMPLIES_EXEC personality flag. However, if set to
1, it weakens security by allowing mappings to be made executable
without authorization by policy. The default value of checkreqprot
at boot was changed starting in Linux v4.4 to 0 (i.e. check the
actual protection), and Android and Linux distributions have been
explicitly writing a "0" to [/sys/fs/selinux/checkreqprot](abi-removed.md#abi-sys-fs-selinux-checkreqprot) during
initialization for some time. Support for setting checkreqprot to 1
will be removed no sooner than June 2021, at which point the kernel
will always cease using checkreqprot internally and will always
check the actual protections being applied upon mmap/mprotect calls.
The checkreqprot selinuxfs node will remain for backward compatibility
but will discard writes of the "0" value and will reject writes of the
"1" value when this mechanism is removed.

|  |
| --- |
| **/sys/fs/selinux/disable** |

Defined on file [sysfs-selinux-disable](abi-removed.md#abi-file-removed-sysfs-selinux-disable)

REMOVAL UPDATE: The SELinux runtime disable functionality was removed
in March 2023, the original deprecation notice is shown below.

The selinuxfs "disable" node allows SELinux to be disabled at runtime
prior to a policy being loaded into the kernel. If disabled via this
mechanism, SELinux will remain disabled until the system is rebooted.

The preferred method of disabling SELinux is via the "selinux=0" boot
parameter, but the selinuxfs "disable" node was created to make it
easier for systems with primitive bootloaders that did not allow for
easy modification of the kernel command line. Unfortunately, allowing
for SELinux to be disabled at runtime makes it difficult to secure the
kernel's LSM hooks using the "__ro_after_init" feature.

Thankfully, the need for the SELinux runtime disable appears to be
gone, the default Kconfig configuration disables this selinuxfs node,
and only one of the major distributions, Fedora, supports disabling
SELinux at runtime. Fedora is in the process of removing the
selinuxfs "disable" node and once that is complete we will start the
slow process of removing this code from the kernel.

More information on [/sys/fs/selinux/disable](abi-removed.md#abi-sys-fs-selinux-disable) can be found under the
CONFIG_SECURITY_SELINUX_DISABLE Kconfig option.

## Symbols under /sys/kernel

|  |
| --- |
| **/sys/kernel/fadump_release_opalcore** |

Defined on file [sysfs-kernel-fadump_release_opalcore](abi-removed.md#abi-file-removed-sysfs-kernel-fadump-release-opalcore)

write only
The sysfs file is available when the system is booted to
collect the dump on OPAL based machine. It used to release
the memory used to collect the opalcore.

|  |
| --- |
| **/sys/kernel/uids/<uid>/cpu_shares** |

Defined on file [sysfs-kernel-uids](abi-removed.md#abi-file-removed-sysfs-kernel-uids)

The [/sys/kernel/uids/<uid>/cpu_shares](abi-removed.md#abi-sys-kernel-uids-uid-cpu-shares) tunable is used
to set the cpu bandwidth a user is allowed. This is a
proportional value. What that means is that if there
are two users logged in, each with an equal number of
shares, then they will get equal CPU bandwidth. Another
example would be, if User A has shares = 1024 and user
B has shares = 2048, User B will get twice the CPU
bandwidth user A will. For more details refer
[CFS Scheduler](../scheduler/sched-design-CFS.md)

## Symbols under /sys/o2cb

|  |
| --- |
| **/sys/o2cb symlink** |

Defined on file [o2cb](abi-removed.md#abi-file-removed-o2cb)

This is a symlink: /sys/o2cb to /sys/fs/o2cb. The symlink is
removed when new versions of ocfs2-tools which know to look
in /sys/fs/o2cb are sufficiently prevalent. Don't code new
software to look here, it should try /sys/fs/o2cb instead.

Users:
ocfs2-tools. It's sufficient to mail proposed changes to
[ocfs2-devel@lists.linux.dev](mailto:ocfs2-devel%40lists.linux.dev).

## devfs

|  |
| --- |
| **devfs** |

Defined on file [devfs](abi-removed.md#abi-file-removed-devfs)

devfs has been unmaintained for a number of years, has unfixable
races, contains a naming policy within the kernel that is
against the LSB, and can be replaced by using udev.

The files fs/devfs/*, include/linux/devfs_fs*.h were removed,
along with the assorted devfs function calls throughout the
kernel tree.

## Symbols under dv1394

|  |
| --- |
| **dv1394 (a.k.a. "OHCI-DV I/O support" for FireWire)** |

Defined on file [dv1394](abi-removed.md#abi-file-removed-dv1394)

/dev/dv1394/\* were character device files, one for each FireWire
controller and for NTSC and PAL respectively, from which DV data
could be received by read() or transmitted by write(). A few
ioctl()s allowed limited control.
This special-purpose interface has been superseded by libraw1394 +
libiec61883 which are functionally equivalent, support HDV, and
transparently work on top of the newer firewire kernel drivers.

Users:

ffmpeg/libavformat (if configured for DV1394)

## ip_queue

|  |
| --- |
| **ip_queue** |

Defined on file [ip_queue](abi-removed.md#abi-file-removed-ip-queue)

ip_queue has been replaced by nfnetlink_queue which provides
more advanced queueing mechanism to user-space. The ip_queue
module was already announced to become obsolete years ago.

## Symbols under raw1394

|  |
| --- |
| **raw1394 (a.k.a. "Raw IEEE1394 I/O support" for FireWire)** |

Defined on file [raw1394](abi-removed.md#abi-file-removed-raw1394)

/dev/raw1394 was a character device file that allowed low-level
access to FireWire buses. Its major drawbacks were its inability
to implement sensible device security policies, and its low level
of abstraction that required userspace clients to duplicate much
of the kernel's ieee1394 core functionality.

Replaced by /dev/fw\*, i.e. the <linux/firewire-cdev.h> ABI of
firewire-core.

Users:

libraw1394 (works with firewire-cdev too, transparent to library ABI
users)

## tcp_dma_copybreak sysctl

|  |
| --- |
| **tcp_dma_copybreak sysctl** |

Defined on file [net_dma](abi-removed.md#abi-file-removed-net-dma)

Formerly the lower limit, in bytes, of the size of socket reads
that will be offloaded to a DMA copy engine. Removed due to
coherency issues of the cpu potentially touching the buffers
while dma is in flight.

## video1394 (a.k.a. "OHCI-1394 Video support" for FireWire)

|  |
| --- |
| **video1394 (a.k.a. "OHCI-1394 Video support" for FireWire)** |

Defined on file [video1394](abi-removed.md#abi-file-removed-video1394)

/dev/video1394/\* were character device files, one for each FireWire
controller, which were used for isochronous I/O. It was added as an
alternative to raw1394's isochronous I/O functionality which had
performance issues in its first generation. Any video1394 user had
to use raw1394 + libraw1394 too because video1394 did not provide
asynchronous I/O for device discovery and configuration.

Replaced by /dev/fw\*, i.e. the <linux/firewire-cdev.h> ABI of
firewire-core.

Users:

libdc1394 (works with firewire-cdev too, transparent to library ABI
users)

## File removed/devfs

Has the following ABI:

- [devfs](abi-removed.md#abi-devfs)

## File removed/dv1394

Has the following ABI:

- [dv1394 (a.k.a. "OHCI-DV I/O support" for FireWire)](abi-removed.md#abi-dv1394-a-k-a-ohci-dv-i-o-support-for-firewire)

## File removed/ip_queue

Has the following ABI:

- [ip_queue](abi-removed.md#abi-ip-queue)

## File removed/net_dma

Has the following ABI:

- [tcp_dma_copybreak sysctl](abi-removed.md#abi-tcp-dma-copybreak-sysctl)

## File removed/o2cb

Has the following ABI:

- [/sys/o2cb symlink](abi-removed.md#abi-sys-o2cb-symlink)

## File removed/raw1394

Has the following ABI:

- [raw1394 (a.k.a. "Raw IEEE1394 I/O support" for FireWire)](abi-removed.md#abi-raw1394-a-k-a-raw-ieee1394-i-o-support-for-firewire)

## File removed/sysfs-bus-nfit

Has the following ABI:

- [/sys/bus/nd/devices/regionX/nfit/ecc_unit_size](abi-removed.md#abi-sys-bus-nd-devices-regionx-nfit-ecc-unit-size)

## File removed/sysfs-class-rfkill

rfkill - radio frequency (RF) connector kill switch support

For details to this subsystem look at [rfkill - RF kill switch support](../driver-api/rfkill.md).

Has the following ABI:

- [/sys/class/rfkill/rfkill[0-9]+/claim](abi-removed.md#abi-sys-class-rfkill-rfkill-0-9-claim)

## File removed/sysfs-kernel-fadump_release_opalcore

This ABI is moved to /sys/firmware/opal/mpipl/release_core.

Has the following ABI:

- [/sys/kernel/fadump_release_opalcore](abi-removed.md#abi-sys-kernel-fadump-release-opalcore)

## File removed/sysfs-kernel-uids

Has the following ABI:

- [/sys/kernel/uids/<uid>/cpu_shares](abi-removed.md#abi-sys-kernel-uids-uid-cpu-shares)

## File removed/sysfs-mce

Has the following ABI:

- [/sys/devices/system/machinecheck/machinecheckX/tolerant](abi-removed.md#abi-sys-devices-system-machinecheck-machinecheckx-tolerant)

## File removed/sysfs-selinux-checkreqprot

Has the following ABI:

- [/sys/fs/selinux/checkreqprot](abi-removed.md#abi-sys-fs-selinux-checkreqprot)

## File removed/sysfs-selinux-disable

Has the following ABI:

- [/sys/fs/selinux/disable](abi-removed.md#abi-sys-fs-selinux-disable)

## File removed/video1394

Has the following ABI:

- [video1394 (a.k.a. "OHCI-1394 Video support" for FireWire)](abi-removed.md#abi-video1394-a-k-a-ohci-1394-video-support-for-firewire)
