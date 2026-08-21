---
collection: kernel
version: "6.8"
title: "Linux Kernel中的文件系統"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_TW/filesystems/index.html
fetched_at: 2026-08-21T03:50:07+00:00
---
Chinese (Traditional)

- [English](../../../filesystems/index.md)
- [Chinese (Simplified)](../../zh_CN/filesystems/index.md)

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
:   [Documentation/filesystems/index.rst](../../../filesystems/index.md#filesystems-index)

Translator
:   Wang Wenhu <[wenhu.wang@vivo.com](mailto:wenhu.wang%40vivo.com)>
    Hu Haowen <[2023002089@link.tyut.edu.cn](mailto:2023002089%40link.tyut.edu.cn)>

# Linux Kernel中的文件系統

這份正在開發的手冊或許在未來某個輝煌的日子裏以易懂的形式將Linux虛擬文件系統（VFS）層以及基於其上的各種文件系統如何工作呈現給大家。當前可以看到下面的內容。

## 文件系統

文件系統實現文檔。

- [virtiofs: virtio-fs 主機<->客機共享文件系統](virtiofs.md)
  - [介紹](virtiofs.md#id1)
  - [用法](virtiofs.md#id2)
  - [內幕](virtiofs.md#id3)
- [Debugfs](debugfs.md)
- [Tmpfs](tmpfs.md)
