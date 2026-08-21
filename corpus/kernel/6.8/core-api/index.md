---
collection: kernel
version: "6.8"
title: "Core API Documentation"
source_url: https://www.kernel.org/doc/html/v6.8/core-api/index.html
fetched_at: 2026-08-21T03:28:38+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/core-api/index.md)
- [Italian](../translations/it_IT/core-api/index.md)

# Core API Documentation

This is the beginning of a manual for core kernel APIs. The conversion
(and writing!) of documents for this manual is much appreciated!

## Core utilities

This section has general and "core core" documentation. The first is a
massive grab-bag of kerneldoc info left over from the docbook days; it
should really be broken up someday when somebody finds the energy to do
it.

- [The Linux Kernel API](kernel-api.md)
- [Workqueue](workqueue.md)
- [General notification mechanism](watch_queue.md)
- [Message logging with printk](printk-basics.md)
- [How to get printk format specifiers right](printk-formats.md)
- [Printk Index](printk-index.md)
- [Symbol Namespaces](symbol-namespaces.md)
- [Assembler Annotations](asm-annotations.md)

## Data structures and low-level utilities

Library functionality that is used throughout the kernel.

- [Everything you never wanted to know about kobjects, ksets, and ktypes](kobject.md)
- [Adding reference counters (krefs) to kernel objects](kref.md)
- [Generic Associative Array Implementation](assoc_array.md)
- [XArray](xarray.md)
- [Maple Tree](maple_tree.md)
- [ID Allocation](idr.md)
- [Circular Buffers](circular-buffers.md)
- [Red-black Trees (rbtree) in Linux](rbtree.md)
- [Generic radix trees/sparse arrays](generic-radix-tree.md)
- [Generic bitfield packing and unpacking functions](packing.md)
- [this_cpu operations](this_cpu_ops.md)
- [ktime accessors](timekeeping.md)
- [The errseq_t datatype](errseq.md)
- [Atomic types](wrappers/atomic_t.md)
- [Atomic bitops](wrappers/atomic_bitops.md)

## Low level entry and exit

- [Entry/exit handling for exceptions, interrupts, syscalls and KVM](entry.md)

## Concurrency primitives

How Linux keeps everything from happening at the same time. See
[Locking](../locking/index.md) for more related documentation.

- [refcount_t API compared to atomic_t](refcount-vs-atomic.md)
- [IRQs](irq/index.md)
- [Semantics and Behavior of Local Atomic Operations](local_ops.md)
- [The padata parallel execution mechanism](padata.md)
- [RCU concepts](../RCU/index.md)
- [Linux kernel memory barriers](wrappers/memory-barriers.md)

## Low-level hardware management

Cache management, managing CPU hotplug, etc.

- [Cache and TLB Flushing Under Linux](cachetlb.md)
- [CPU hotplug in the Kernel](cpu_hotplug.md)
- [Memory hotplug](memory-hotplug.md)
- [Linux generic IRQ handling](genericirq.md)
- [Memory Protection Keys](protection-keys.md)

## Memory management

How to allocate and use memory in the kernel. Note that there is a lot
more memory-management documentation in [Memory Management Documentation](../mm/index.md).

- [Memory Allocation Guide](memory-allocation.md)
- [Unaligned Memory Accesses](unaligned-memory-access.md)
- [Dynamic DMA mapping using the generic device](dma-api.md)
- [Dynamic DMA mapping Guide](dma-api-howto.md)
- [DMA attributes](dma-attributes.md)
- [DMA with ISA and LPC devices](dma-isa-lpc.md)
- [Memory Management APIs](mm-api.md)
- [The genalloc/genpool subsystem](genalloc.md)
- [pin_user_pages() and related calls](pin_user_pages.md)
- [Boot time memory management](boot-time-mm.md)
- [GFP masks used from FS/IO context](gfp_mask-from-fs-io.md)

## Interfaces for kernel debugging

- [The object-lifetime debugging infrastructure](debug-objects.md)
- [The Linux Kernel Tracepoint API](tracepoint.md)
- [Using physical DMA provided by OHCI-1394 FireWire controllers for debugging](debugging-via-ohci1394.md)

## Everything else

Documents that don't fit elsewhere or which have yet to be categorized.

- [Reed-Solomon Library Programming Interface](librs.md)
- [Netlink notes for kernel developers](netlink.md)
