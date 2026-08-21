---
collection: kernel
version: "6.8"
title: "架构支持"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/rust/arch-support.html
fetched_at: 2026-08-21T03:54:33+00:00
---
Chinese (Simplified)

- [English](../../../rust/arch-support.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [Arch Support](../../../rust/arch-support.md)

翻译
:   司延腾 Yanteng Si <[siyanteng@loongson.cn](mailto:siyanteng%40loongson.cn)>

# 架构支持

目前，Rust编译器（`rustc`）使用LLVM进行代码生成，这限制了可以支持的目标架构。此外，对
使用LLVM/Clang构建内核的支持也有所不同（请参见 [Building Linux with Clang/LLVM](../../../kbuild/llvm.md) ）。这
种支持对于使用 `libclang` 的 `bindgen` 来说是必需的。

下面是目前可以工作的架构的一般总结。支持程度与 `MAINTAINERS` 文件中的``S`` 值相对应:

| 架构 | 支持水平 | 限制因素 |
| --- | --- | --- |
| `x86` | Maintained | 只有 `x86_64` |
