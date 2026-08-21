---
collection: kernel
version: "6.8"
title: "The Linux kernel user's and administrator's guide"
source_url: https://www.kernel.org/doc/html/v6.8/admin-guide/index.html
fetched_at: 2026-08-21T03:28:46+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/admin-guide/index.md)
- [Chinese (Traditional)](../translations/zh_TW/admin-guide/index.md)

# The Linux kernel user's and administrator's guide

The following is a collection of user-oriented documents that have been
added to the kernel over time. There is, as yet, little overall order or
organization here — this material was not written to be a single, coherent
document! With luck things will improve quickly over time.

This initial section contains overall information, including the README
file describing the kernel as a whole, documentation on kernel parameters,
etc.

- [Linux kernel release 6.x <http://kernel.org/>](README.md)
- [The kernel's command-line parameters](kernel-parameters.md)
- [Linux allocated devices (4.x+ version)](devices.md)
- [Documentation for /proc/sys](sysctl/index.md)
- [Linux ABI description](abi.md)
- [Feature status on all architectures](features.md)

This section describes CPU vulnerabilities and their mitigations.

- [Hardware vulnerabilities](hw-vuln/index.md)

Here is a set of documents aimed at users who are trying to track down
problems and bugs in particular.

- [Reporting issues](reporting-issues.md)
- [Reporting regressions](reporting-regressions.md)
- [How to quickly build a trimmed Linux kernel](quickly-build-trimmed-linux.md)
- [Bug hunting](bug-hunting.md)
- [Bisecting a bug](bug-bisect.md)
- [Tainted kernels](tainted-kernels.md)
- [Ramoops oops/panic logger](ramoops.md)
- [Dynamic debug](dynamic-debug-howto.md)
- [Explaining the "No working init found." boot hang message](init.md)
- [Documentation for Kdump - The kexec-based Crash Dumping Solution](kdump/index.md)
- [Performance monitor support](perf/index.md)
- [pstore block oops/panic logger](pstore-blk.md)

This is the beginning of a section with information of interest to
application developers. Documents covering various aspects of the kernel
ABI will be found here.

- [Rules on how to access information in sysfs](sysfs-rules.md)

This is the beginning of a section with information of interest to
application developers and system integrators doing analysis of the
Linux kernel for safety critical applications. Documents supporting
analysis of kernel interactions with applications, and key kernel
subsystems expectations will be found here.

- [Discovering Linux kernel subsystems used by a workload](workload-tracing.md)

The rest of this manual consists of various unordered guides on how to
configure specific aspects of kernel behavior to your liking.

- [ACPI Support](acpi/index.md)
- [ATA over Ethernet (AoE)](aoe/index.md)
- [Auxiliary Display Support](auxdisplay/index.md)
- [A block layer cache (bcache)](bcache.md)
- [The Android binderfs Filesystem](binderfs.md)
- [Kernel Support for miscellaneous Binary Formats (binfmt_misc)](binfmt-misc.md)
- [Block Devices](blockdev/index.md)
- [Boot Configuration](bootconfig.md)
- [Linux Braille Console](braille-console.md)
- [btmrvl driver](btmrvl.md)
- [Control Groups version 1](cgroup-v1/index.md)
- [Control Group v2](cgroup-v2.md)
- [CIFS](cifs/index.md)
- [Clearing WARN_ONCE](clearing-warn-once.md)
- [CPU load](cpu-load.md)
- [How CPU topology info is exported via sysfs](cputopology.md)
- [Dell Remote BIOS Update driver (dell_rbu)](dell_rbu.md)
- [Device Mapper](device-mapper/index.md)
- [EDID](edid.md)
- [The EFI Boot Stub](efi-stub.md)
- [ext4 General Information](ext4.md)
- [File system Monitoring with fanotify](filesystem-monitoring.md)
- [NFS](nfs/index.md)
- [gpio](gpio/index.md)
- [Notes on the change from 16-bit UIDs to 32-bit UIDs](highuid.md)
- [Hardware random number generators](hw_random.md)
- [Using the initial RAM disk (initrd)](initrd.md)
- [I/O statistics fields](iostats.md)
- [Java(tm) Binary Kernel Support for Linux v1.03](java.md)
- [IBM's Journaled File System (JFS) for Linux](jfs.md)
- [Reducing OS jitter due to per-cpu kthreads](kernel-per-CPU-kthreads.md)
- [Laptop Drivers](laptops/index.md)
- [Parallel port LCD/Keypad Panel support](lcd-panel-cgram.md)
- [LDM - Logical Disk Manager (Dynamic Disks)](ldm.md)
- [Softlockup detector and hardlockup detector (aka nmi_watchdog)](lockup-watchdogs.md)
- [Linux Security Module Usage](LSM/index.md)
- [RAID arrays](md.md)
- [Media subsystem admin and user guide](media/index.md)
- [Memory Management](mm/index.md)
- [Kernel module signing facility](module-signing.md)
- [Mono(tm) Binary Kernel Support for Linux](mono.md)
- [Namespaces](namespaces/index.md)
- [Numa policy hit/miss statistics](numastat.md)
- [Parport](parport.md)
- [Perf events and tool security](perf-security.md)
- [Power Management](pm/index.md)
- [Set udev rules for PMF Smart PC Builder](pmf.md)
- [Linux Plug and Play Documentation](pnp.md)
- [RapidIO Subsystem Guide](rapidio.md)
- [Reliability, Availability and Serviceability](ras.md)
- [Real Time Clock (RTC) Drivers for Linux](rtc.md)
- [Linux Serial Console](serial-console.md)
- [Video Mode Selection Support 2.13](svga.md)
- [Syscall User Dispatch](syscall-user-dispatch.md)
- [Linux Magic System Request Key Hacks](sysrq.md)
- [Thermal Subsystem](thermal/index.md)
- [USB4 and Thunderbolt](thunderbolt.md)
- [Using UFS](ufs.md)
- [Unicode support](unicode.md)
- [Software cursor for VGA](vga-softcursor.md)
- [Video Output Switcher Control](video-output.md)
- [The SGI XFS Filesystem](xfs.md)
