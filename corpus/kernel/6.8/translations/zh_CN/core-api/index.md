---
collection: kernel
version: "6.8"
title: "核心API文档"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/core-api/index.html
fetched_at: 2026-08-21T03:30:24+00:00
---
Chinese (Simplified)

- [English](../../../core-api/index.md)
- [Italian](../../it_IT/core-api/index.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [Core API Documentation](../../../core-api/index.md)

翻译
:   司延腾 Yanteng Si <[siyanteng@loongson.cn](mailto:siyanteng%40loongson.cn)>

# 核心API文档

这是核心内核API手册的首页。 非常感谢为本手册转换(和编写!)的文档!

## 核心实用程序

本节包含通用的和“核心中的核心”文档。 第一部分是 docbook 时期遗留下
来的大量 kerneldoc 信息；有朝一日，若有人有动力的话，应当把它们拆分
出来。

- [Linux内核API](kernel-api.md)
- [使用printk记录消息](printk-basics.md)
- [如何获得正确的printk格式占位符](printk-formats.md)
- [并发管理的工作队列 (cmwq)](workqueue.md)
- [通用通知机制](watch_queue.md)
- [符号命名空间（Symbol Namespaces）](symbol-namespaces.md)

## 数据结构和低级实用程序

在整个内核中使用的函数库。

- [关于kobjects、ksets和ktypes的一切你没想过需要了解的东西](kobject.md)
- [为内核对象添加引用计数器（krefs）](kref.md)
- [通用关联数组的实现](assoc_array.md)
- [XArray](xarray.md)
- [Linux中的红黑树（rbtree）](rbtree.md)
- [ID分配](idr.md)
- [环形缓冲区](circular-buffers.md)
- [通用基数树/稀疏数组](generic-radix-tree.md)
- [通用的位域打包和解包函数](packing.md)
- [this_cpu操作](this_cpu_ops.md)

---

Todolist:

> timekeeping
> errseq

## 并发原语

Linux如何让一切同时发生。 详情请参阅
[Locking](../../../locking/index.md)

- [IRQs](irq/index.md)
- [与atomic_t相比，refcount_t的API是这样的](refcount-vs-atomic.md)
- [本地原子操作的语义和行为](local_ops.md)
- [padata并行执行机制](padata.md)

Todolist:

> ../RCU/index

## 低级硬件管理

缓存管理，CPU热插拔管理等。

- [Linux下的缓存和TLB刷新](cachetlb.md)
- [内核中的CPU热拔插](cpu_hotplug.md)
- [Linux通用IRQ处理](genericirq.md)
- [内存热插拔](memory-hotplug.md)
- [内存保护密钥](protection-keys.md)

Todolist:

> memory-hotplug
> cpu_hotplug
> genericirq

## 内存管理

如何在内核中分配和使用内存。请注意，在
[Memory Management Documentation](../../../mm/index.md) 中有更多的内存管理文档。

- [内存分配指南](memory-allocation.md)
- [非对齐内存访问](unaligned-memory-access.md)
- [内存管理APIs](mm-api.md)
- [genalloc/genpool子系统](genalloc.md)
- [启动时的内存管理](boot-time-mm.md)
- [从FS/IO上下文中使用的GFP掩码](gfp_mask-from-fs-io.md)

Todolist:

> dma-api
> dma-api-howto
> dma-attributes
> dma-isa-lpc
> pin_user_pages

## 内核调试的接口

Todolist:

> debug-objects
> tracepoint
> debugging-via-ohci1394

## 其它文档

不适合放在其它地方或尚未归类的文件；

Todolist:

> librs
