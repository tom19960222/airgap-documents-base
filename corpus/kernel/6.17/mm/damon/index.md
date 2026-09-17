---
collection: kernel
version: "6.17"
title: "DAMON: Data Access MONitoring and Access-aware System Operations"
source_url: https://www.kernel.org/doc/html/v6.17/mm/damon/index.html
fetched_at: 2026-09-16T16:36:11+00:00
---
English

- [Chinese (Simplified)](../../translations/zh_CN/mm/damon/index.md)

# DAMON: Data Access MONitoring and Access-aware System Operations

DAMON is a Linux kernel subsystem that provides a framework for data access
monitoring and the monitoring results based system operations. The core
monitoring [mechanisms](design.md#damon-design-monitoring) of DAMON make it

> - *accurate* (the monitoring output is useful enough for DRAM level memory
>   management; It might not appropriate for CPU Cache levels, though),
> - *light-weight* (the monitoring overhead is low enough to be applied online),
>   and
> - *scalable* (the upper-bound of the overhead is in constant range regardless
>   of the size of target workloads).

Using this framework, therefore, the kernel can operate system in an
access-aware fashion. Because the features are also exposed to the [user
space](../../admin-guide/mm/damon/index.md), users who have special information about
their workloads can write personalized applications for better understanding
and optimizations of their workloads and systems.

For easier development of such systems, DAMON provides a feature called
[DAMOS](design.md#damon-design-damos) (DAMon-based Operation Schemes) in addition
to the monitoring. Using the feature, DAMON users in both kernel and [user
spaces](../../admin-guide/mm/damon/index.md) can do access-aware system operations
with no code but simple configurations.

- [Frequently Asked Questions](faq.md)
  - [Does DAMON support virtual memory only?](faq.md#does-damon-support-virtual-memory-only)
  - [Can I simply monitor page granularity?](faq.md#can-i-simply-monitor-page-granularity)
- [Design](design.md)
  - [Execution Model and Data Structures](design.md#execution-model-and-data-structures)
  - [Overall Architecture](design.md#overall-architecture)
  - [Operations Set Layer](design.md#operations-set-layer)
  - [Core Logics](design.md#core-logics)
  - [Modules](design.md#modules)
- [API Reference](api.md)
  - [Structures](api.md#structures)
  - [Functions](api.md#functions)
- [DAMON Maintainer Entry Profile](maintainer-profile.md)
  - [SCM Trees](maintainer-profile.md#scm-trees)
  - [Submit checklist addendum](maintainer-profile.md#submit-checklist-addendum)
  - [Key cycle dates](maintainer-profile.md#key-cycle-dates)
  - [Review cadence](maintainer-profile.md#review-cadence)
  - [Mailing tool](maintainer-profile.md#mailing-tool)
  - [Community meetup](maintainer-profile.md#community-meetup)

To utilize and control DAMON from the user-space, please refer to the
administration [guide](../../admin-guide/mm/damon/index.md).

If you prefer academic papers for reading and citations, please use the papers
from [HPDC’22](https://dl.acm.org/doi/abs/10.1145/3502181.3531466) and
[Middleware19 Industry](https://dl.acm.org/doi/abs/10.1145/3366626.3368125) .
Note that those cover DAMON implementations in Linux v5.16 and v5.15,
respectively.
