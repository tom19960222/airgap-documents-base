---
collection: kernel
version: "6.8"
title: "内核开发工具"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/dev-tools/index.html
fetched_at: 2026-08-21T03:33:38+00:00
---
Chinese (Simplified)

- [English](../../../dev-tools/index.md)
- [Chinese (Traditional)](../../zh_TW/dev-tools/index.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [Development tools for the kernel](../../../dev-tools/index.md)

Translator
:   赵军奎 Bernard Zhao <[bernard@vivo.com](mailto:bernard%40vivo.com)>

# 内核开发工具

本文档是有关内核开发工具文档的合集。
目前这些文档已经整理在一起，不需要再花费额外的精力。
欢迎任何补丁。

有关测试专用工具的简要概述，参见
[内核测试指南](testing-overview.md)

目录

- [内核测试指南](testing-overview.md)
  - [编写和运行测试](testing-overview.md#id2)
  - [代码覆盖率工具](testing-overview.md#id3)
  - [动态分析工具](testing-overview.md#id4)
  - [静态分析工具](testing-overview.md#id5)
- [Sparse](sparse.md)
  - [使用 sparse 工具做类型检查](sparse.md#id1)
  - [获取 sparse 工具](sparse.md#id3)
  - [使用 sparse 工具](sparse.md#id4)
- [在Linux内核里使用gcov做代码覆盖率检查](gcov.md)
  - [准备](gcov.md#id1)
  - [定制化](gcov.md#id2)
  - [相关文件](gcov.md#id3)
  - [针对模块的统计](gcov.md#id4)
  - [编译机和测试机分离](gcov.md#id5)
  - [关于编译器的注意事项](gcov.md#id6)
  - [问题定位](gcov.md#id8)
  - [附录A：collect_on_build.sh](gcov.md#a-collect-on-build-sh)
  - [附录B：collect_on_test.sh](gcov.md#b-collect-on-test-sh)
- [内核地址消毒剂(KASAN)](kasan.md)
  - [概述](kasan.md#id1)
  - [支持](kasan.md#id2)
  - [用法](kasan.md#id6)
  - [实施细则](kasan.md#id9)
  - [影子内存](kasan.md#id13)
  - [对于开发者](kasan.md#id15)
- [通过gdb调试内核和模块](gdb-kernel-debugging.md)
  - [环境配置要求](gdb-kernel-debugging.md#id1)
  - [设置](gdb-kernel-debugging.md#id2)
  - [使用Linux提供的gdb脚本的示例](gdb-kernel-debugging.md#linuxgdb)
  - [命令和辅助调试功能列表](gdb-kernel-debugging.md#id3)

Todolist:

> - coccinelle
> - kcov
> - ubsan
> - kmemleak
> - kcsan
> - kfence
> - kgdb
> - kselftest
> - kunit/index
