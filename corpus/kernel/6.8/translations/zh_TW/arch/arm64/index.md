---
collection: kernel
version: "6.8"
title: "ARM64 架構"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_TW/arch/arm64/index.html
fetched_at: 2026-08-21T03:38:03+00:00
---
Chinese (Traditional)

- [English](../../../../arch/arm64/index.md)
- [Chinese (Simplified)](../../../zh_CN/arch/arm64/index.md)

> **Warning:**
>
> 此文件的目的是爲讓中文讀者更容易閱讀和理解，而不是作爲一個分支。因此，
> 如果您對此文件有任何意見或改動，請先嘗試更新原始英文文件。如果要更改或
> 修正某處翻譯文件，請將意見或補丁發送給維護者（聯繫方式見下）。

> **Note:**
>
> 如果您發現本文檔與原始文件有任何不同或者有翻譯問題，請聯繫該文件的譯者，
> 或者發送電子郵件給胡皓文以獲取幫助：<[2023002089@link.tyut.edu.cn](mailto:2023002089%40link.tyut.edu.cn)>。

Original
:   [Documentation/arch/arm64/index.rst](../../../../arch/arm64/index.md#arm64-index)

Translator
:   Bailu Lin <[bailu.lin@vivo.com](mailto:bailu.lin%40vivo.com)>
    Hu Haowen <[2023002089@link.tyut.edu.cn](mailto:2023002089%40link.tyut.edu.cn)>

# ARM64 架構

- [AArch64 Linux 中擴展的活動監控單元](amu.md)
  - [架構總述](amu.md#id1)
  - [基本支持](amu.md#id2)
  - [用戶空間訪問](amu.md#id3)
  - [虛擬化](amu.md#id4)
- [ARM64中的 HugeTLBpage](hugetlbpage.md)
  - [1) pud/pmd 級別的塊映射](hugetlbpage.md#pud-pmd)
  - [2) 使用連續位](hugetlbpage.md#id1)
- [Perf 事件屬性](perf.md)
  - [exclude_user](perf.md#exclude-user)
  - [exclude_kernel](perf.md#exclude-kernel)
  - [exclude_hv](perf.md#exclude-hv)
  - [exclude_host / exclude_guest](perf.md#exclude-host-exclude-guest)
  - [準確性](perf.md#id1)
- [ARM64 ELF hwcaps](elf_hwcaps.md)
  - [1. 簡介](elf_hwcaps.md#id1)
  - [2. Hwcaps 的說明](elf_hwcaps.md#hwcaps)
  - [3. AT_HWCAP 中揭示的 hwcaps](elf_hwcaps.md#at-hwcap-hwcaps)
  - [4. 未使用的 AT_HWCAP 位](elf_hwcaps.md#at-hwcap)
