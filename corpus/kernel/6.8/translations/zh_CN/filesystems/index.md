---
collection: kernel
version: "6.8"
title: "Linux Kernel中的文件系统"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/filesystems/index.html
fetched_at: 2026-08-21T03:50:07+00:00
---
Chinese (Simplified)

- [English](../../../filesystems/index.md)
- [Chinese (Traditional)](../../zh_TW/filesystems/index.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [Documentation/filesystems/index.rst](../../../filesystems/index.md#filesystems-index)

Translator
:   Wang Wenhu <[wenhu.wang@vivo.com](mailto:wenhu.wang%40vivo.com)>

# Linux Kernel中的文件系统

这份正在开发的手册或许在未来某个辉煌的日子里以易懂的形式将Linux虚拟文件系统（VFS）层以及基于其上的各种文件系统如何工作呈现给大家。当前可以看到下面的内容。

## 文件系统

文件系统实现文档。

- [virtiofs: virtio-fs 主机<->客机共享文件系统](virtiofs.md)
  - [介绍](virtiofs.md#id1)
  - [用法](virtiofs.md#id2)
  - [内幕](virtiofs.md#id3)
- [Debugfs](debugfs.md)
- [Tmpfs](tmpfs.md)
