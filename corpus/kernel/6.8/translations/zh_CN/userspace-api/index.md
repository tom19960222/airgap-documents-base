---
collection: kernel
version: "6.8"
title: "Linux 内核用户空间API指南"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/userspace-api/index.html
fetched_at: 2026-08-21T03:35:32+00:00
---
Chinese (Simplified)

- [English](../../../userspace-api/index.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [The Linux kernel user-space API guide](../../../userspace-api/index.md)

翻译
:   李睿 Rui Li <[me@lirui.org](mailto:me%40lirui.org)>

# Linux 内核用户空间API指南

尽管许多用户空间API的文档被记录在别处（特别是在 [man-pages](https://www.kernel.org/doc/man-pages/) 项目中），
在代码树中仍然可以找到有关用户空间的部分信息。这个手册意在成为这些信息
聚集的地方。

目录

- [无新权限标志](no_new_privs.md)
- [Seccomp BPF (基于过滤器的安全计算)](seccomp_filter.md)
  - [介绍](seccomp_filter.md#id1)
  - [这不是什么](seccomp_filter.md#id2)
  - [用法](seccomp_filter.md#id3)
  - [返回值](seccomp_filter.md#id4)
  - [隐患](seccomp_filter.md#id5)
  - [例子](seccomp_filter.md#id6)
  - [用户空间通知](seccomp_filter.md#id7)
  - [Sysctls](seccomp_filter.md#sysctls)
  - [添加架构支持](seccomp_filter.md#id8)
  - [注意事项](seccomp_filter.md#id9)
- [OpenCAPI （开放相干加速器处理器接口）](accelerators/ocxl.md)
  - [高层视角](accelerators/ocxl.md#id1)
  - [设备发现](accelerators/ocxl.md#id2)
  - [MMIO](accelerators/ocxl.md#mmio)
  - [AFU中断](accelerators/ocxl.md#afu)
  - [字符设备](accelerators/ocxl.md#id3)
  - [Sysfs类](accelerators/ocxl.md#sysfs)
  - [用户API](accelerators/ocxl.md#api)
- [eBPF 用户空间API](ebpf/index.md)
  - [eBPF Syscall](ebpf/syscall.md)
- [平台配置文件选择（如 /sys/firmware/acpi/platform_profile）](sysfs-platform_profile.md)
- [futex2](futex2.md)
  - [用户API](futex2.md#api)

TODOList:

- landlock
- unshare
- spec_ctrl
- ioctl/index
- iommu
- media/index
- netlink/index
- vduse
