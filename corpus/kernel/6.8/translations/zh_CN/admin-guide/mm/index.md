---
collection: kernel
version: "6.8"
title: "内存管理"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/admin-guide/mm/index.html
fetched_at: 2026-08-21T03:56:15+00:00
---
Chinese (Simplified)

- [English](../../../../admin-guide/mm/index.md)
- [Chinese (Traditional)](../../../zh_TW/admin-guide/mm/index.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [Memory Management](../../../../admin-guide/mm/index.md)

翻译
:   徐鑫 xu xin <[xu.xin16@zte.com.cn](mailto:xu.xin16%40zte.com.cn)>

# 内存管理

Linux内存管理子系统，顾名思义，是负责系统中的内存管理。它包括了虚拟内存与请求
分页的实现，内核内部结构和用户空间程序的内存分配、将文件映射到进程地址空间以
及许多其他很酷的事情。

Linux内存管理是一个具有许多可配置设置的复杂系统, 且这些设置中的大多数都可以通
过 `/proc` 文件系统获得，并且可以使用 `sysctl` 进行查询和调整。这些API接
口被描述在Documentation/admin-guide/sysctl/vm.rst文件和 [man 5 proc](http://man7.org/linux/man-pages/man5/proc.5.html) 中。

Linux内存管理有它自己的术语，如果你还不熟悉它，请考虑阅读下面参考：
[Concepts overview](../../../../admin-guide/mm/concepts.md).

在此目录下，我们详细描述了如何与Linux内存管理中的各种机制交互。

- [监测数据访问](damon/index.md)
- [内核同页合并](ksm.md)

Todolist:
\* concepts
\* cma_debugfs
\* hugetlbpage
\* idle_page_tracking
\* memory-hotplug
\* nommu-mmap
\* numa_memory_policy
\* numaperf
\* pagemap
\* soft-dirty
\* swap_numa
\* transhuge
\* userfaultfd
\* zswap
