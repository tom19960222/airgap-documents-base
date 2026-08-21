---
collection: kernel
version: "6.8"
title: "Memory Management"
source_url: https://www.kernel.org/doc/html/v6.8/admin-guide/mm/index.html
fetched_at: 2026-08-21T03:34:55+00:00
---
English

- [Chinese (Simplified)](../../translations/zh_CN/admin-guide/mm/index.md)
- [Chinese (Traditional)](../../translations/zh_TW/admin-guide/mm/index.md)

# Memory Management

Linux memory management subsystem is responsible, as the name implies,
for managing the memory in the system. This includes implementation of
virtual memory and demand paging, memory allocation both for kernel
internal structures and user space programs, mapping of files into
processes address space and many other cool things.

Linux memory management is a complex system with many configurable
settings. Most of these settings are available via `/proc`
filesystem and can be quired and adjusted using `sysctl`. These APIs
are described in [Documentation for /proc/sys/vm/](../sysctl/vm.md) and in [man 5 proc](http://man7.org/linux/man-pages/man5/proc.5.html).

Linux memory management has its own jargon and if you are not yet
familiar with it, consider reading [Concepts overview](concepts.md).

Here we document in detail how to interact with various mechanisms in
the Linux memory management.

- [Concepts overview](concepts.md)
- [CMA Debugfs Interface](cma_debugfs.md)
- [DAMON: Data Access MONitor](damon/index.md)
- [HugeTLB Pages](hugetlbpage.md)
- [Idle Page Tracking](idle_page_tracking.md)
- [Kernel Samepage Merging](ksm.md)
- [Memory Hot(Un)Plug](memory-hotplug.md)
- [Multi-Gen LRU](multigen_lru.md)
- [No-MMU memory mapping support](nommu-mmap.md)
- [NUMA Memory Policy](numa_memory_policy.md)
- [NUMA Memory Performance](numaperf.md)
- [Examining Process Page Tables](pagemap.md)
- [Shrinker Debugfs Interface](shrinker_debugfs.md)
- [Soft-Dirty PTEs](soft-dirty.md)
- [Automatically bind swap device to numa node](swap_numa.md)
- [Transparent Hugepage Support](transhuge.md)
- [Userfaultfd](userfaultfd.md)
- [zswap](zswap.md)
