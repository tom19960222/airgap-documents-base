---
collection: kernel
version: "6.8"
title: "Linux虚拟化支持"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/virt/index.html
fetched_at: 2026-08-21T03:52:43+00:00
---
Chinese (Simplified)

- [English](../../../virt/index.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [Virtualization Support](../../../virt/index.md)

翻译
:   司延腾 Yanteng Si <[siyanteng@loongson.cn](mailto:siyanteng%40loongson.cn)>

校译
:   时奎亮 Alex Shi <[alexs@kernel.org](mailto:alexs%40kernel.org)>

# Linux虚拟化支持

- [半虚拟化操作](paravirt_ops.md)
- [客户机停机轮询机制（Guest halt polling）](guest-halt-polling.md)
  - [模块参数](guest-halt-polling.md#id1)
  - [进一步说明](guest-halt-polling.md#id2)
- [Nitro Enclaves](ne_overview.md)
  - [概述](ne_overview.md#id1)
- [ACRN超级管理器](acrn/index.md)
  - [ACRN超级管理器介绍](acrn/introduction.md)
  - [I/O请求处理](acrn/io-request.md)
  - [ACRN CPUID位域](acrn/cpuid.md)

TODOLIST:

> kvm/index
> uml/user_mode_linux_howto_v2
