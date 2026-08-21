---
collection: kernel
version: "6.8"
title: "监测数据访问"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/admin-guide/mm/damon/index.html
fetched_at: 2026-08-21T04:01:47+00:00
---
Chinese (Simplified)

- [English](../../../../../admin-guide/mm/damon/index.md)
- [Chinese (Traditional)](../../../../zh_TW/admin-guide/mm/damon/index.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [DAMON: Data Access MONitor](../../../../../admin-guide/mm/damon/index.md)

翻译
:   司延腾 Yanteng Si <[siyanteng@loongson.cn](mailto:siyanteng%40loongson.cn)>

校译

# 监测数据访问

[DAMON](../../../../../mm/damon/index.md) 允许轻量级的数据访问监测。使用DAMON，
用户可以分析他们系统的内存访问模式，并优化它们。

- [入门指南](start.md)
  - [前提条件](start.md#id2)
  - [记录数据访问模式](start.md#id5)
  - [将记录的模式可视化](start.md#id6)
  - [数据访问模式感知的内存管理](start.md#id7)
- [详细用法](usage.md)
  - [sysfs接口](usage.md#sysfs)
  - [debugfs接口](usage.md#debugfs)
  - [监测结果的监测点](usage.md#id18)
- [基于DAMON的回收](reclaim.md)
  - [哪些地方需要主动回收？](reclaim.md#id1)
  - [它是如何工作的？](reclaim.md#id5)
  - [接口: 模块参数](reclaim.md#id6)
  - [例子](reclaim.md#id7)
- [基于DAMON的LRU排序](lru_sort.md)
  - [哪里需要主动的LRU排序](lru_sort.md#lru)
  - [这是如何工作的](lru_sort.md#id1)
  - [接口：模块参数](lru_sort.md#id2)
  - [Example](lru_sort.md#example)
