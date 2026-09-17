---
collection: kernel
version: "6.17"
title: "The Linux kernel user’s and administrator’s guide"
source_url: https://www.kernel.org/doc/html/v6.17/admin-guide/index.html
fetched_at: 2026-09-16T16:17:46+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/admin-guide/index.md)
- [Chinese (Traditional)](../translations/zh_TW/admin-guide/index.md)

# The Linux kernel user’s and administrator’s guide

The following is a collection of user-oriented documents that have been
added to the kernel over time. There is, as yet, little overall order or
organization here — this material was not written to be a single, coherent
document! With luck things will improve quickly over time.

## General guides to kernel administration

This initial section contains overall information, including the README
file describing the kernel as a whole, documentation on kernel parameters,
etc.

- [Linux kernel release 6.x <http://kernel.org/>](README.md)
- [Linux allocated devices (4.x+ version)](devices.md)
- [Feature status on all architectures](features.md)

A big part of the kernel’s administrative interface is the /proc and sysfs
virtual filesystems; these documents describe how to interact with tem

- [Rules on how to access information in sysfs](sysfs-rules.md)
- [Documentation for /proc/sys](sysctl/index.md)
- [How CPU topology info is exported via sysfs](cputopology.md)
- [Linux ABI description](abi.md)

Security-related documentation:

- [Hardware vulnerabilities](hw-vuln/index.md)
- [Linux Security Module Usage](LSM/index.md)
- [Perf events and tool security](perf-security.md)

## Booting the kernel

- [Boot Configuration](bootconfig.md)
- [The kernel’s command-line parameters](kernel-parameters.md)
- [The EFI Boot Stub](efi-stub.md)
- [Using the initial RAM disk (initrd)](initrd.md)

## Tracking down and identifying problems

Here is a set of documents aimed at users who are trying to track down
problems and bugs in particular.

- [Reporting issues](reporting-issues.md)
- [Reporting regressions](reporting-regressions.md)
- [How to quickly build a trimmed Linux kernel](quickly-build-trimmed-linux.md)
- [How to verify bugs and bisect regressions](verify-bugs-and-bisect-regressions.md)
- [Bug hunting](bug-hunting.md)
- [Bisecting a regression](bug-bisect.md)
- [Tainted kernels](tainted-kernels.md)
- [Ramoops oops/panic logger](ramoops.md)
- [Dynamic debug](dynamic-debug-howto.md)
- [Explaining the “No working init found.” boot hang message](init.md)
- [Documentation for Kdump - The kexec-based Crash Dumping Solution](kdump/index.md)
- [Performance monitor support](perf/index.md)
- [pstore block oops/panic logger](pstore-blk.md)
- [Clearing WARN_ONCE](clearing-warn-once.md)
- [Reducing OS jitter due to per-cpu kthreads](kernel-per-CPU-kthreads.md)
- [Softlockup detector and hardlockup detector (aka nmi_watchdog)](lockup-watchdogs.md)
- [Reliability, Availability and Serviceability (RAS)](RAS/main.md)
- [Error decoding](RAS/error-decoding.md)
- [Address translation](RAS/address-translation.md)
- [Linux Magic System Request Key Hacks](sysrq.md)

## Core-kernel subsystems

These documents describe core-kernel administration interfaces that are
likely to be of interest on almost any system.

- [Control Group v2](cgroup-v2.md)
- [Control Groups version 1](cgroup-v1/index.md)
- [CPU load](cpu-load.md)
- [Memory Management](mm/index.md)
- [Kernel module signing facility](module-signing.md)
- [Namespaces](namespaces/index.md)
- [Numa policy hit/miss statistics](numastat.md)
- [Power Management](pm/index.md)
- [Syscall User Dispatch](syscall-user-dispatch.md)

Support for non-native binary formats. Note that some of these
documents are ... old ...

- [Kernel Support for miscellaneous Binary Formats (binfmt_misc)](binfmt-misc.md)
- [Java(tm) Binary Kernel Support for Linux v1.03](java.md)
- [Mono(tm) Binary Kernel Support for Linux](mono.md)

## Block-layer and filesystem administration

- [A block layer cache (bcache)](bcache.md)
- [The Android binderfs Filesystem](binderfs.md)
- [Block Devices](blockdev/index.md)
- [CIFS](cifs/index.md)
- [Device Mapper](device-mapper/index.md)
- [ext4 General Information](ext4.md)
- [File system Monitoring with fanotify](filesystem-monitoring.md)
- [NFS](nfs/index.md)
- [I/O statistics fields](iostats.md)
- [IBM’s Journaled File System (JFS) for Linux](jfs.md)
- [RAID arrays](md.md)
- [Using UFS](ufs.md)
- [The SGI XFS Filesystem](xfs.md)

## Device-specific guides

How to configure your hardware within your Linux system.

- [ACPI Support](acpi/index.md)
- [ATA over Ethernet (AoE)](aoe/index.md)
- [Auxiliary Display Support](auxdisplay/index.md)
- [Linux Braille Console](braille-console.md)
- [btmrvl driver](btmrvl.md)
- [Dell Remote BIOS Update driver (dell_rbu)](dell_rbu.md)
- [EDID](edid.md)
- [GPIO](gpio/index.md)
- [Hardware random number generators](hw_random.md)
- [Laptop Drivers](laptops/index.md)
- [Parallel port LCD/Keypad Panel support](lcd-panel-cgram.md)
- [Media subsystem admin and user guide](media/index.md)
- [Linux NVMe multipath](nvme-multipath.md)
- [Parport](parport.md)
- [Linux Plug and Play Documentation](pnp.md)
- [RapidIO Subsystem Guide](rapidio.md)
- [Real Time Clock (RTC) Drivers for Linux](rtc.md)
- [Linux Serial Console](serial-console.md)
- [Video Mode Selection Support 2.13](svga.md)
- [Thermal Subsystem](thermal/index.md)
- [USB4 and Thunderbolt](thunderbolt.md)
- [Software cursor for VGA](vga-softcursor.md)
- [Video Output Switcher Control](video-output.md)

## Workload analysis

This is the beginning of a section with information of interest to
application developers and system integrators doing analysis of the
Linux kernel for safety critical applications. Documents supporting
analysis of kernel interactions with applications, and key kernel
subsystems expectations will be found here.

- [Discovering Linux kernel subsystems used by a workload](workload-tracing.md)

## Everything else

A few hard-to-categorize and generally obsolete documents.

- [LDM - Logical Disk Manager (Dynamic Disks)](ldm.md)
- [Unicode support](unicode.md)
