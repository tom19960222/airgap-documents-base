---
collection: kernel
version: "6.8"
title: "LoongArch體系結構"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_TW/arch/loongarch/index.html
fetched_at: 2026-08-21T03:38:04+00:00
---
Chinese (Traditional)

- [English](../../../../arch/loongarch/index.md)
- [Chinese (Simplified)](../../../zh_CN/arch/loongarch/index.md)

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
:   [LoongArch Architecture](../../../../arch/loongarch/index.md)

Translator
:   Huacai Chen <[chenhuacai@loongson.cn](mailto:chenhuacai%40loongson.cn)>

# LoongArch體系結構

- [1. LoongArch介紹](introduction.md)
  - [1.1. 寄存器](introduction.md#id1)
  - [1.2. 基礎指令集](introduction.md#id6)
  - [1.3. 虛擬內存](introduction.md#id9)
  - [1.4. Loongson與LoongArch的關係](introduction.md#loongsonloongarch)
  - [1.5. 參考文獻](introduction.md#loongarch-references-zh-tw)
- [2. 啓動 Linux/LoongArch](booting.md)
  - [2.1. BootLoader傳遞給內核的信息](booting.md#bootloader)
  - [2.2. Linux/LoongArch內核鏡像文件頭](booting.md#id1)
- [3. LoongArch的IRQ芯片模型（層級關係）](irq-chip-model.md)
  - [3.1. 傳統IRQ模型](irq-chip-model.md#irq)
  - [3.2. 擴展IRQ模型](irq-chip-model.md#id1)
  - [3.3. ACPI相關的定義](irq-chip-model.md#acpi)
  - [3.4. 參考文獻](irq-chip-model.md#id2)
- [4. Feature status on loongarch architecture](features.md)
