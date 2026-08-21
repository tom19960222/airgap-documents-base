---
collection: kernel
version: "6.8"
title: "程序设计语言"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/process/programming-language.html
fetched_at: 2026-08-21T03:42:04+00:00
---
Chinese (Simplified)

- [English](../../../process/programming-language.md)
- [Chinese (Traditional)](../../zh_TW/process/programming-language.md)
- [Italian](../../it_IT/process/programming-language.md)
- [Spanish](../../sp_SP/process/programming-language.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [Documentation/process/programming-language.rst](../../../process/programming-language.md#programming-language)

Translator
:   Alex Shi <[alex.shi@linux.alibaba.com](mailto:alex.shi%40linux.alibaba.com)>

# 程序设计语言

内核是用C语言 [c-language](programming-language.md#cn-c-language) 编写的。更准确地说，内核通常是用 [gcc](programming-language.md#cn-gcc)
在 `-std=gnu11` [gcc-c-dialect-options](programming-language.md#cn-gcc-c-dialect-options) 下编译的：ISO C11的 GNU 方言

这种方言包含对语言 [gnu-extensions](programming-language.md#cn-gnu-extensions) 的许多扩展，当然，它们许多都在内核中使用。

对于一些体系结构，有一些使用 [clang](programming-language.md#cn-clang) 和 [icc](programming-language.md#cn-icc) 编译内核
的支持，尽管在编写此文档时还没有完成，仍需要第三方补丁。

## 属性

在整个内核中使用的一个常见扩展是属性（attributes） [gcc-attribute-syntax](programming-language.md#cn-gcc-attribute-syntax)
属性允许将实现定义的语义引入语言实体（如变量、函数或类型），而无需对语言进行
重大的语法更改（例如添加新关键字） [n2049](programming-language.md#cn-n2049)

在某些情况下，属性是可选的（即不支持这些属性的编译器仍然应该生成正确的代码，
即使其速度较慢或执行的编译时检查/诊断次数不够）

内核定义了伪关键字（例如， `pure` ），而不是直接使用GNU属性语法（例如,
`__attribute__((__pure__))` ），以检测可以使用哪些关键字和/或缩短代码, 具体
请参阅 `include/linux/compiler_attributes.h`

c-language
:   <http://www.open-std.org/jtc1/sc22/wg14/www/standards>

gcc
:   <https://gcc.gnu.org>

clang
:   <https://clang.llvm.org>

icc
:   <https://software.intel.com/en-us/c-compilers>

c-dialect-options
:   <https://gcc.gnu.org/onlinedocs/gcc/C-Dialect-Options.html>

gnu-extensions
:   <https://gcc.gnu.org/onlinedocs/gcc/C-Extensions.html>

gcc-attribute-syntax
:   <https://gcc.gnu.org/onlinedocs/gcc/Attribute-Syntax.html>

n2049
:   <http://www.open-std.org/jtc1/sc22/wg14/www/docs/n2049.pdf>
