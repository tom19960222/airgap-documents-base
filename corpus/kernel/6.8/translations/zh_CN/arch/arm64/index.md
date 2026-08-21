---
collection: kernel
version: "6.8"
title: "ARM64 架构"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/arch/arm64/index.html
fetched_at: 2026-08-21T03:37:30+00:00
---
Chinese (Simplified)

- [English](../../../../arch/arm64/index.md)
- [Chinese (Traditional)](../../../zh_TW/arch/arm64/index.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [Documentation/arch/arm64/index.rst](../../../../arch/arm64/index.md#arm64-index)

Translator
:   Bailu Lin <[bailu.lin@vivo.com](mailto:bailu.lin%40vivo.com)>

# ARM64 架构

- [AArch64 Linux 中扩展的活动监控单元](amu.md)
  - [架构总述](amu.md#id1)
  - [基本支持](amu.md#id2)
  - [用户空间访问](amu.md#id3)
  - [虚拟化](amu.md#id4)
- [ARM64中的 HugeTLBpage](hugetlbpage.md)
  - [1) pud/pmd 级别的块映射](hugetlbpage.md#pud-pmd)
  - [2) 使用连续位](hugetlbpage.md#id1)
- [Perf 事件属性](perf.md)
  - [exclude_user](perf.md#exclude-user)
  - [exclude_kernel](perf.md#exclude-kernel)
  - [exclude_hv](perf.md#exclude-hv)
  - [exclude_host / exclude_guest](perf.md#exclude-host-exclude-guest)
  - [准确性](perf.md#id1)
- [ARM64 ELF hwcaps](elf_hwcaps.md)
  - [1. 简介](elf_hwcaps.md#id1)
  - [2. Hwcaps 的说明](elf_hwcaps.md#hwcaps)
  - [3. AT_HWCAP 中揭示的 hwcaps](elf_hwcaps.md#at-hwcap-hwcaps)
  - [4. 未使用的 AT_HWCAP 位](elf_hwcaps.md#at-hwcap)
