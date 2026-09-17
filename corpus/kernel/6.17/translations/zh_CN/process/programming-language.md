---
collection: kernel
version: "6.17"
title: "程序设计语言"
source_url: https://www.kernel.org/doc/html/v6.17/translations/zh_CN/process/programming-language.html
fetched_at: 2026-09-16T16:31:45+00:00
---
Chinese (Simplified)

- [English](../../../process/programming-language.md)
- [Chinese (Traditional)](../../zh_TW/process/programming-language.md)
- [Italian](../../it_IT/process/programming-language.md)
- [Spanish](../../sp_SP/process/programming-language.md)

> **Note:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请发建议或者补丁给
> 该文件的译者，或者请求中文文档维护者和审阅者的帮助。

Original:
:   [Documentation/process/programming-language.rst](../../../process/programming-language.md#programming-language)

Translator:
:   Alex Shi <[alex.shi@linux.alibaba.com](mailto:alex.shi%40linux.alibaba.com)>

# 程序设计语言

内核是用 C 编程语言编写的 [[zh_cn_c-language]](programming-language.md#zh-cn-c-language)。更准确地说，内核通常使用 `gcc` [[zh_cn_gcc]](programming-language.md#zh-cn-gcc) 编译，
并且使用 `-std=gnu11` [[zh_cn_gcc-c-dialect-options]](programming-language.md#zh-cn-gcc-c-dialect-options)：这是 ISO C11 的 GNU 方言。
`clang` [[zh_cn_clang]](programming-language.md#zh-cn-clang) 也得到了支持，详见文档：
[使用 Clang/LLVM 构建 Linux](../../../kbuild/llvm.md#kbuild-llvm)。

这种方言包含对 C 语言的许多扩展 [[zh_cn_gnu-extensions]](programming-language.md#zh-cn-gnu-extensions)，当然，它们许多都在内核中使用。

## 属性

在整个内核中使用的一个常见扩展是属性（attributes） [[zh_cn_gcc-attribute-syntax]](programming-language.md#zh-cn-gcc-attribute-syntax)。
属性允许将实现定义的语义引入语言实体（如变量、函数或类型），而无需对语言进行
重大的语法更改（例如添加新关键字） [[zh_cn_n2049]](programming-language.md#zh-cn-n2049)。

在某些情况下，属性是可选的（即不支持这些属性的编译器仍然应该生成正确的代码，
即使其速度较慢或执行的编译时检查/诊断次数不够）

内核定义了伪关键字（例如， `pure` ），而不是直接使用GNU属性语法（例如,
`__attribute__((__pure__))` ），以检测可以使用哪些关键字和/或缩短代码, 具体
请参阅 `include/linux/compiler_attributes.h`

## Rust

内核对 Rust 编程语言 [[zh_cn_rust-language]](programming-language.md#zh-cn-rust-language) 的支持是实验性的，并且可以通过配置选项
`CONFIG_RUST` 来启用。Rust 代码使用 `rustc` [[zh_cn_rustc]](programming-language.md#zh-cn-rustc) 编译器在
`--edition=2021` [[zh_cn_rust-editions]](programming-language.md#zh-cn-rust-editions) 选项下进行编译。版本（Editions）是一种
在语言中引入非后向兼容的小型变更的方式。

除此之外，内核中还使用了一些不稳定的特性 [[zh_cn_rust-unstable-features]](programming-language.md#zh-cn-rust-unstable-features)。这些不稳定
的特性将来可能会发生变化，因此，一个重要的目标是达到仅使用稳定特性的程度。

具体请参阅 [Rust](../../../rust/index.md)

[[zh_cn_c-language](programming-language.md#id2)]

<http://www.open-std.org/jtc1/sc22/wg14/www/standards>

[[zh_cn_gcc](programming-language.md#id3)]

<https://gcc.gnu.org>

[[zh_cn_clang](programming-language.md#id5)]

<https://clang.llvm.org>

[[zh_cn_gcc-c-dialect-options](programming-language.md#id4)]

<https://gcc.gnu.org/onlinedocs/gcc/C-Dialect-Options.html>

[[zh_cn_gnu-extensions](programming-language.md#id6)]

<https://gcc.gnu.org/onlinedocs/gcc/C-Extensions.html>

[[zh_cn_gcc-attribute-syntax](programming-language.md#id8)]

<https://gcc.gnu.org/onlinedocs/gcc/Attribute-Syntax.html>

[[zh_cn_n2049](programming-language.md#id9)]

<http://www.open-std.org/jtc1/sc22/wg14/www/docs/n2049.pdf>

[[zh_cn_rust-language](programming-language.md#id10)]

<https://www.rust-lang.org>

[[zh_cn_rustc](programming-language.md#id11)]

<https://doc.rust-lang.org/rustc/>

[[zh_cn_rust-editions](programming-language.md#id12)]

<https://doc.rust-lang.org/edition-guide/editions/>

[[zh_cn_rust-unstable-features](programming-language.md#id13)]

<https://github.com/Rust-for-Linux/linux/issues/2>
