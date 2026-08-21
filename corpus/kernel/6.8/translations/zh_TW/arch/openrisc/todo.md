---
collection: kernel
version: "6.8"
title: "待辦事項"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_TW/arch/openrisc/todo.html
fetched_at: 2026-08-21T03:58:42+00:00
---
Chinese (Traditional)

- [English](../../../../arch/openrisc/todo.md)
- [Chinese (Simplified)](../../../zh_CN/arch/openrisc/todo.md)

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
:   [TODO](../../../../arch/openrisc/todo.md)

翻譯
:   司延騰 Yanteng Si <[siyanteng@loongson.cn](mailto:siyanteng%40loongson.cn)>

# 待辦事項

OpenRISC Linux的移植已經完全投入使用，並且從 2.6.35 開始就一直在上游同步。
然而，還有一些剩餘的項目需要在未來幾個月內完成。 下面是一個即將進行調查的已知
不盡完美的項目列表，即我們的待辦事項列表。

- 實現其餘的DMA API……dma_map_sg等。
- 完成重命名清理工作……代碼中提到了or32，這是架構的一個老名字。 我們
  已經確定的名字是or1k，這個改變正在以緩慢積累的方式進行。 目前，or32相當
  於or1k。
