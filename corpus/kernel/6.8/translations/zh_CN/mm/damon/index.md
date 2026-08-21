---
collection: kernel
version: "6.8"
title: "DAMON:数据访问监视器"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/mm/damon/index.html
fetched_at: 2026-08-21T03:59:16+00:00
---
Chinese (Simplified)

- [English](../../../../mm/damon/index.md)

# DAMON:数据访问监视器

DAMON是Linux内核的一个数据访问监控框架子系统。DAMON的核心机制使其成为
（该核心机制详见([设计](design.md))）

> - *准确度* （监测输出对DRAM级别的内存管理足够有用；但可能不适合CPU Cache级别），
> - *轻量级* （监控开销低到可以在线应用），以及
> - *可扩展* （无论目标工作负载的大小，开销的上限值都在恒定范围内）。

因此，利用这个框架，内核的内存管理机制可以做出高级决策。会导致高数据访问监控开销的实
验性内存管理优化工作可以再次进行。同时，在用户空间，有一些特殊工作负载的用户可以编写
个性化的应用程序，以便更好地了解和优化他们的工作负载和系统。

- [常见问题](faq.md)
  - [为什么是一个新的子系统，而不是扩展perf或其他用户空间工具？](faq.md#perf)
  - [“闲置页面跟踪” 或 “perf mem” 可以替代DAMON吗？](faq.md#perf-mem-damon)
  - [DAMON是否只支持虚拟内存？](faq.md#damon)
  - [我可以简单地监测页面的粒度吗？](faq.md#id2)
- [设计](design.md)
  - [可配置的层](design.md#id2)
  - [特定地址空间基元的参考实现](design.md#id3)
  - [独立于地址空间的核心机制](design.md#id4)
- [API参考](api.md)
  - [结构体](api.md#id1)
  - [函数](api.md#id2)
