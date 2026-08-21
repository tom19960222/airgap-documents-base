---
collection: kernel
version: "6.8"
title: "Linux内存管理文档"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/mm/index.html
fetched_at: 2026-08-21T03:46:00+00:00
---
Chinese (Simplified)

- [English](../../../mm/index.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [Memory Management Documentation](../../../mm/index.md)

翻译
:   司延腾 Yanteng Si <[siyanteng@loongson.cn](mailto:siyanteng%40loongson.cn)>

校译

# Linux内存管理文档

这是一份关于了解Linux的内存管理子系统的指南。如果你正在寻找关于简单分配内存的
建议，请参阅内存分配指南
([内存分配指南](../core-api/memory-allocation.md))。
关于控制和调整的指南，请看管理指南
([内存管理](../admin-guide/mm/index.md))。

- [高内存处理](highmem.md)

该处剩余文档待原始文档有内容后翻译。

## 遗留文档

这是一个关于Linux内存管理（MM）子系统内部的旧文档的集合，其中有不同层次的细节，
包括注释和邮件列表的回复，用于阐述数据结构和算法的描述。它应该被很好地整合到上述
结构化的文档中，如果它已经完成了它的使命，可以删除。

- [Active MM](active_mm.md)
- [内存平衡](balance.md)
- [DAMON:数据访问监视器](damon/index.md)
- [空闲页报告](free_page_reporting.md)
- [内核同页合并](ksm.md)
- [异构内存管理 (HMM)](hmm.md)
- [hwpoison](hwpoison.md)
- [Hugetlbfs 预留](hugetlbfs_reserv.md)
- [物理内存模型](memory-model.md)
- [什么时候需要页表锁内通知？](mmu_notifier.md)
- [何为非统一内存访问(NUMA)？](numa.md)
- [超量使用审计](overcommit-accounting.md)
- [页面片段](page_frags.md)
- [页面迁移](page_migration.md)
- [page owner: 跟踪谁分配的每个页面](page_owner.md)
- [页表检查](page_table_check.md)
- [remap_file_pages()系统调用](remap_file_pages.md)
- [分页表锁（split page table lock）](split_page_table_lock.md)
- [支持虚拟映射的内核栈](vmalloced-kernel-stacks.md)
- [z3fold](z3fold.md)
- [zsmalloc](zsmalloc.md)

TODOLIST:
\* arch_pgtable_helpers
\* free_page_reporting
\* hugetlbfs_reserv
\* slub
\* transhuge
\* unevictable-lru
