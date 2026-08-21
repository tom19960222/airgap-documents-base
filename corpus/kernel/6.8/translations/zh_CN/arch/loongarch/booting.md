---
collection: kernel
version: "6.8"
title: "2. 启动 Linux/LoongArch"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/arch/loongarch/booting.html
fetched_at: 2026-08-21T03:58:36+00:00
---
Chinese (Simplified)

- [English](../../../../arch/loongarch/booting.md)
- [Chinese (Traditional)](../../../zh_TW/arch/loongarch/booting.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [Booting Linux/LoongArch](../../../../arch/loongarch/booting.md)

翻译
:   司延腾 Yanteng Si <[siyanteng@loongson.cn](mailto:siyanteng%40loongson.cn)>

# 2. 启动 Linux/LoongArch

作者
:   司延腾 <[siyanteng@loongson.cn](mailto:siyanteng%40loongson.cn)>

日期
:   2022年11月18日

## 2.1. BootLoader传递给内核的信息

LoongArch支持ACPI和FDT启动，需要传递给内核的信息包括memmap、initrd、cmdline、可
选的ACPI/FDT表等。

内核在 kernel_entry 入口处被传递以下参数:

> - a0 = efi_boot: efi_boot 是一个标志，表示这个启动环境是否完全符合UEFI
>   的要求。
> - a1 = cmdline: cmdline 是一个指向内核命令行的指针。
> - a2 = systemtable: systemtable 指向EFI的系统表，在这个阶段涉及的所有
>   指针都是物理地址。

## 2.2. Linux/LoongArch内核镜像文件头

内核镜像是EFI镜像。作为PE文件，它们有一个64字节的头部结构体，如下所示:

```
u32     MZ_MAGIC                /* "MZ", MS-DOS 头 */
u32     res0 = 0                /* 保留 */
u64     kernel_entry            /* 内核入口点 */
u64     _end - _text            /* 内核镜像有效大小 */
u64     load_offset             /* 加载内核镜像相对内存起始地址的偏移量 */
u64     res1 = 0                /* 保留 */
u64     res2 = 0                /* 保留 */
u64     res3 = 0                /* 保留 */
u32     LINUX_PE_MAGIC          /* 魔术数 */
u32     pe_header - _head       /* 到PE头的偏移量 */
```
