---
collection: kernel
version: "6.8"
title: "LoongArch体系结构"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/arch/loongarch/index.html
fetched_at: 2026-08-21T03:37:32+00:00
---
Chinese (Simplified)

- [English](../../../../arch/loongarch/index.md)
- [Chinese (Traditional)](../../../zh_TW/arch/loongarch/index.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [LoongArch Architecture](../../../../arch/loongarch/index.md)

Translator
:   Huacai Chen <[chenhuacai@loongson.cn](mailto:chenhuacai%40loongson.cn)>

# LoongArch体系结构

- [1. LoongArch介绍](introduction.md)
  - [1.1. 寄存器](introduction.md#id1)
  - [1.2. 基础指令集](introduction.md#id6)
  - [1.3. 虚拟内存](introduction.md#id9)
  - [1.4. Loongson与LoongArch的关系](introduction.md#loongsonloongarch)
  - [1.5. 参考文献](introduction.md#loongarch-references-zh-cn)
- [2. 启动 Linux/LoongArch](booting.md)
  - [2.1. BootLoader传递给内核的信息](booting.md#bootloader)
  - [2.2. Linux/LoongArch内核镜像文件头](booting.md#id1)
- [3. LoongArch的IRQ芯片模型（层级关系）](irq-chip-model.md)
  - [3.1. 传统IRQ模型](irq-chip-model.md#irq)
  - [3.2. 扩展IRQ模型](irq-chip-model.md#id1)
  - [3.3. ACPI相关的定义](irq-chip-model.md#acpi)
  - [3.4. 参考文献](irq-chip-model.md#id2)
- [4. Feature status on loongarch architecture](features.md)
