---
collection: kernel
version: "6.17"
title: "Memory Management Documentation"
source_url: https://www.kernel.org/doc/html/v6.17/mm/index.html
fetched_at: 2026-09-16T16:19:33+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/mm/index.md)

# Memory Management Documentation

This is a guide to understanding the memory management subsystem
of Linux. If you are looking for advice on simply allocating memory,
see the [Memory Allocation Guide](../core-api/memory-allocation.md#memory-allocation). For controlling and tuning guides,
see the [admin guide](../admin-guide/mm/index.md).

- [Physical Memory](physical_memory.md)
- [Page Tables](page_tables.md)
- [Process Addresses](process_addrs.md)
- [Boot Memory](bootmem.md)
- [Page Allocation](page_allocation.md)
- [Virtually Contiguous Memory Allocation](vmalloc.md)
- [Slab Allocation](slab.md)
- [High Memory Handling](highmem.md)
- [Page Reclaim](page_reclaim.md)
- [Swap](swap.md)
- [Page Cache](page_cache.md)
- [Shared Memory Filesystem](shmfs.md)
- [Out Of Memory Handling](oom.md)

## Unsorted Documentation

This is a collection of unsorted documents about the Linux memory management
(MM) subsystem internals with different level of details ranging from notes and
mailing list responses for elaborating descriptions of data structures and
algorithms. It should all be integrated nicely into the above structured
documentation, or deleted if it has served its purpose.

- [Active MM](active_mm.md)
- [MEMORY ALLOCATION PROFILING](allocation-profiling.md)
- [Architecture Page Table Helpers](arch_pgtable_helpers.md)
- [Memory Balancing](balance.md)
- [DAMON: Data Access MONitoring and Access-aware System Operations](damon/index.md)
- [Free Page Reporting](free_page_reporting.md)
- [Heterogeneous Memory Management (HMM)](hmm.md)
- [hwpoison](hwpoison.md)
- [Hugetlbfs Reservation](hugetlbfs_reserv.md)
- [Kernel Samepage Merging](ksm.md)
- [Physical Memory Model](memory-model.md)
- [When do you need to notify inside page table lock ?](mmu_notifier.md)
- [Multi-Gen LRU](multigen_lru.md)
- [What is NUMA?](numa.md)
- [Overcommit Accounting](overcommit-accounting.md)
- [Page migration](page_migration.md)
- [Page fragments](page_frags.md)
- [page owner: Tracking about who allocated each page](page_owner.md)
- [Page Table Check](page_table_check.md)
- [remap_file_pages() system call](remap_file_pages.md)
- [Split page table lock](split_page_table_lock.md)
- [Transparent Hugepage Support](transhuge.md)
- [Unevictable LRU Infrastructure](unevictable-lru.md)
- [Virtually Mapped Kernel Stack Support](vmalloced-kernel-stacks.md)
- [A vmemmap diet for HugeTLB and Device DAX](vmemmap_dedup.md)
- [zsmalloc](zsmalloc.md)
