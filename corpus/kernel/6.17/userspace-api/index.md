---
collection: kernel
version: "6.17"
title: "The Linux kernel user-space API guide"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/index.html
fetched_at: 2026-09-16T16:17:49+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/userspace-api/index.md)

# The Linux kernel user-space API guide

While much of the kernel’s user-space API is documented elsewhere
(particularly in the [man-pages](https://www.kernel.org/doc/man-pages/) project), some user-space information can
also be found in the kernel tree itself. This manual is intended to be the
place where this information is gathered.

## System calls

- [unshare system call](unshare.md)
- [futex2](futex2.md)
- [eBPF Userspace API](ebpf/index.md)
- [IOCTLs](ioctl/index.md)
- [Introduction of mseal](mseal.md)

## Security-related interfaces

- [No New Privileges Flag](no_new_privs.md)
- [Seccomp BPF (SECure COMPuting with filters)](seccomp_filter.md)
- [Landlock: unprivileged access control](landlock.md)
- [Linux Security Modules](lsm.md)
- [Introduction of non-executable mfd](mfd_noexec.md)
- [Speculation Control](spec_ctrl.md)
- [TEE (Trusted Execution Environment) Userspace API](tee.md)
- [Executability check](check_exec.md)

## Devices and I/O

- [OpenCAPI (Open Coherent Accelerator Processor Interface)](accelerators/ocxl.md)
- [Allocating dma-buf using heaps](dma-buf-heaps.md)
- [Exchanging pixel buffers](dma-buf-alloc-exchange.md)
- [Firmware Control (FWCTL) Userspace API](fwctl/index.md)
- [GPIO](gpio/index.md)
- [IOMMUFD](iommufd.md)
- [Linux Media Infrastructure userspace API](media/index.md)
- [Dell Systems Management Base Driver](dcdbas.md)
- [VDUSE - “vDPA Device in Userspace”](vduse.md)
- [ISA Plug & Play support](isapnp.md)

## Everything else

- [Linux-specific ELF idiosyncrasies](ELF.md)
- [Netlink Handbook](netlink/index.md)
- [Platform Profile Selection (e.g. /sys/firmware/acpi/platform_profile)](sysfs-platform_profile.md)
- [VDUSE - “vDPA Device in Userspace”](vduse.md)
- [futex2](futex2.md)
- [Perf ring buffer](perf_ring_buffer.md)
- [NT synchronization primitive driver](ntsync.md)
