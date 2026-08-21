---
collection: kernel
version: "6.8"
title: "清除 WARN_ONCE"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_TW/admin-guide/clearing-warn-once.html
fetched_at: 2026-08-21T03:55:11+00:00
---
Chinese (Traditional)

- [English](../../../admin-guide/clearing-warn-once.md)
- [Chinese (Simplified)](../../zh_CN/admin-guide/clearing-warn-once.md)

> **Warning:**
>
> 此文件的目的是爲讓中文讀者更容易閱讀和理解，而不是作爲一個分支。因此，
> 如果您對此文件有任何意見或改動，請先嘗試更新原始英文文件。如果要更改或
> 修正某處翻譯文件，請將意見或補丁發送給維護者（聯繫方式見下）。

> **Note:**
>
> 如果您發現本文檔與原始文件有任何不同或者有翻譯問題，請聯繫該文件的譯者，
> 或者發送電子郵件給胡皓文以獲取幫助：<[2023002089@link.tyut.edu.cn](mailto:2023002089%40link.tyut.edu.cn)>。

Translator
:   胡皓文 Hu Haowen <[2023002089@link.tyut.edu.cn](mailto:2023002089%40link.tyut.edu.cn)>

# 清除 WARN_ONCE

WARN_ONCE / WARN_ON_ONCE / printk_once 僅僅打印一次消息.

echo 1 > /sys/kernel/debug/clear_warn_once

可以清除這種狀態並且再次允許打印一次告警信息，這對於運行測試集後重現問題
很有用。
