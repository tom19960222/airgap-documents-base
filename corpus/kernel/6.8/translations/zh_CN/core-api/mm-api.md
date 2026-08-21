---
collection: kernel
version: "6.8"
title: "内存管理APIs"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/core-api/mm-api.html
fetched_at: 2026-08-21T03:45:57+00:00
---
Chinese (Simplified)

- [English](../../../core-api/mm-api.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [Memory Management APIs](../../../core-api/mm-api.md)

翻译
:   司延腾 Yanteng Si <[siyanteng@loongson.cn](mailto:siyanteng%40loongson.cn)>
    周彬彬 Binbin Zhou <[zhoubinbin@loongson.cn](mailto:zhoubinbin%40loongson.cn)>

校译
:   时奎亮<[alexs@kernel.org](mailto:alexs%40kernel.org)>

# 内存管理APIs

API（Application Programming Interface，应用程序接口）

## 用户空间内存访问

该API在以下内核代码中:

arch/x86/include/asm/uaccess.h

arch/x86/lib/usercopy_32.c

mm/gup.c

## 内存分配控制

该API在以下内核代码中:

include/linux/gfp_types.h

## Slab缓存

此缓存非cpu片上缓存，请读者自行查阅资料。

该API在以下内核代码中:

include/linux/slab.h

mm/slab.c

mm/slab_common.c

mm/util.c

## 虚拟连续（内存页）映射

该API在以下内核代码中:

mm/vmalloc.c

## 文件映射和页面缓存

该API在以下内核代码中:

### 文件映射

mm/filemap.c

### 预读

mm/readahead.c

### 回写

mm/page-writeback.c

### 截断

mm/truncate.c

include/linux/pagemap.h

## 内存池

该API在以下内核代码中:

mm/mempool.c

## DMA池

DMA(Direct Memory Access，直接存储器访问)

该API在以下内核代码中:

mm/dmapool.c

## 更多的内存管理函数

该API在以下内核代码中:

mm/memory.c

mm/page_alloc.c

mm/mempolicy.c

include/linux/mm_types.h

include/linux/mm_inline.h

include/linux/page-flags.h

include/linux/mm.h

include/linux/page_ref.h

include/linux/mmzone.h

mm/util.c
