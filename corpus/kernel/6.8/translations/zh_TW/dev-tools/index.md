---
collection: kernel
version: "6.8"
title: "內核開發工具"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_TW/dev-tools/index.html
fetched_at: 2026-08-21T03:33:39+00:00
---
Chinese (Traditional)

- [English](../../../dev-tools/index.md)
- [Chinese (Simplified)](../../zh_CN/dev-tools/index.md)

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
:   [Development tools for the kernel](../../../dev-tools/index.md)

Translator
:   趙軍奎 Bernard Zhao <[bernard@vivo.com](mailto:bernard%40vivo.com)>

# 內核開發工具

本文檔是有關內核開發工具文檔的合集。
目前這些文檔已經整理在一起，不需要再花費額外的精力。
歡迎任何補丁。

有關測試專用工具的簡要概述，參見
[內核測試指南](testing-overview.md)

目錄

- [內核測試指南](testing-overview.md)
  - [編寫和運行測試](testing-overview.md#id2)
  - [代碼覆蓋率工具](testing-overview.md#id3)
  - [動態分析工具](testing-overview.md#id4)
  - [靜態分析工具](testing-overview.md#id5)
- [Traditional Chinese maintainer: Hu Haowen <2023002089@link.tyut.edu.cn>](sparse.md)
- [以下爲正文](sparse.md#id1)
  - [使用 sparse 工具做類型檢查](sparse.md#sparse)
  - [獲取 sparse 工具](sparse.md#id2)
  - [使用 sparse 工具](sparse.md#id3)
- [在Linux內核裏使用gcov做代碼覆蓋率檢查](gcov.md)
  - [準備](gcov.md#id1)
  - [定製化](gcov.md#id2)
  - [相關文件](gcov.md#id3)
  - [針對模塊的統計](gcov.md#id4)
  - [編譯機和測試機分離](gcov.md#id5)
  - [關於編譯器的注意事項](gcov.md#id6)
  - [問題定位](gcov.md#id8)
  - [附錄A：collect_on_build.sh](gcov.md#a-collect-on-build-sh)
  - [附錄B：collect_on_test.sh](gcov.md#b-collect-on-test-sh)
- [內核地址消毒劑(KASAN)](kasan.md)
  - [概述](kasan.md#id1)
  - [支持](kasan.md#id2)
  - [用法](kasan.md#id6)
  - [實施細則](kasan.md#id9)
  - [影子內存](kasan.md#id13)
  - [對於開發者](kasan.md#id15)
- [通過gdb調試內核和模塊](gdb-kernel-debugging.md)
  - [環境配置要求](gdb-kernel-debugging.md#id1)
  - [設置](gdb-kernel-debugging.md#id2)
  - [使用Linux提供的gdb腳本的示例](gdb-kernel-debugging.md#linuxgdb)
  - [命令和輔助調試功能列表](gdb-kernel-debugging.md#id3)

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
