---
collection: kernel
version: "6.8"
title: "Devicetree动态解析器说明"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/devicetree/dynamic-resolution-notes.html
fetched_at: 2026-08-21T03:58:26+00:00
---
Chinese (Simplified)

- [English](../../../devicetree/dynamic-resolution-notes.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [Devicetree Dynamic Resolver Notes](../../../devicetree/dynamic-resolution-notes.md)

翻译
:   司延腾 Yanteng Si <[siyanteng@loongson.cn](mailto:siyanteng%40loongson.cn)>

校译

# Devicetree动态解析器说明

本文描述了内核内DeviceTree解析器的实现，它位于drivers/of/resolver.c中。

## 解析器如何工作？

解析器被赋予一个任意的树作为输入，该树用适当的dtc选项编译，并有一个/plugin/标签。这就产
生了适当的__fixups__和__local_fixups__节点。

解析器依次通过以下步骤工作:

1. 从实时树中获取最大的设备树phandle值 + 1.
2. 调整树的所有本地 phandles，以解决这个量。
3. 使用 __local__fixups__ 节点信息以相同的量调整所有本地引用。
4. 对于__fixups__节点中的每个属性，找到它在实时树中引用的节点。这是用来标记该节点的标签。
5. 检索fixup的目标的phandle。
6. 对于属性中的每个fixup，找到节点:属性:偏移的位置，并用phandle值替换它。
