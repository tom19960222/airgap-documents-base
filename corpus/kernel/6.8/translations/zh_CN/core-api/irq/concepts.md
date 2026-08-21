---
collection: kernel
version: "6.8"
title: "什么是IRQ？"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/core-api/irq/concepts.html
fetched_at: 2026-08-21T03:59:13+00:00
---
Chinese (Simplified)

- [English](../../../../core-api/irq/concepts.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [What is an IRQ?](../../../../core-api/irq/concepts.md)

翻译
:   司延腾 Yanteng Si <[siyanteng@loongson.cn](mailto:siyanteng%40loongson.cn)>

# 什么是IRQ？

IRQ (Interrupt ReQuest) 指来自设备的中断请求。
目前，它们可以通过一个引脚或通过一个数据包进入。
多个设备可以连接到同一个引脚，从而共享一个IRQ。

IRQ编号是用来描述硬件中断源的内核标识符。通常它是一个到全局irq_desc数组的索引，
但是除了在linux/interrupt.h中实现的之外，其它细节是体系结构特征相关的。

IRQ编号是对机器上可能的中断源的枚举。通常枚举的是系统中所有中断控制器的输入引脚
编号。在ISA（工业标准体系结构）的情况下所枚举的是两个i8259中断控制器的16个输入引脚。

体系结构可以给IRQ号赋予额外的含义，在涉及到硬件手动配置的情况下，我们鼓励这样做。
ISA IRQ是赋予这种额外含义的一个典型例子。
