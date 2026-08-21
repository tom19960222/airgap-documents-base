---
collection: kernel
version: "6.8"
title: "DAMON: Data Access MONitor"
source_url: https://www.kernel.org/doc/html/v6.8/admin-guide/mm/damon/index.html
fetched_at: 2026-08-21T03:56:09+00:00
---
English

- [Chinese (Simplified)](../../../translations/zh_CN/admin-guide/mm/damon/index.md)
- [Chinese (Traditional)](../../../translations/zh_TW/admin-guide/mm/damon/index.md)

# DAMON: Data Access MONitor

[DAMON](../../../mm/damon/index.md) allows light-weight data access monitoring.
Using DAMON, users can analyze the memory access patterns of their systems and
optimize those.

- [Getting Started](start.md)
  - [Prerequisites](start.md#prerequisites)
  - [Recording Data Access Patterns](start.md#recording-data-access-patterns)
  - [Visualizing Recorded Patterns](start.md#visualizing-recorded-patterns)
  - [Data Access Pattern Aware Memory Management](start.md#data-access-pattern-aware-memory-management)
- [Detailed Usages](usage.md)
  - [sysfs Interface](usage.md#sysfs-interface)
  - [Tracepoints for Monitoring Results](usage.md#tracepoints-for-monitoring-results)
  - [debugfs Interface (DEPRECATED!)](usage.md#debugfs-interface-deprecated)
- [DAMON-based Reclamation](reclaim.md)
  - [Where Proactive Reclamation is Required?](reclaim.md#where-proactive-reclamation-is-required)
  - [How It Works?](reclaim.md#how-it-works)
  - [Interface: Module Parameters](reclaim.md#interface-module-parameters)
  - [Example](reclaim.md#example)
- [DAMON-based LRU-lists Sorting](lru_sort.md)
  - [Where Proactive LRU-lists Sorting is Required?](lru_sort.md#where-proactive-lru-lists-sorting-is-required)
  - [How It Works?](lru_sort.md#how-it-works)
  - [Interface: Module Parameters](lru_sort.md#interface-module-parameters)
  - [Example](lru_sort.md#example)
