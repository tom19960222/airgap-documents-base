---
collection: kernel
version: "6.17"
title: "DAMON: Data Access MONitoring and Access-aware System Operations"
source_url: https://www.kernel.org/doc/html/v6.17/admin-guide/mm/damon/index.html
fetched_at: 2026-09-16T16:48:11+00:00
---
English

- [Chinese (Simplified)](../../../translations/zh_CN/admin-guide/mm/damon/index.md)
- [Chinese (Traditional)](../../../translations/zh_TW/admin-guide/mm/damon/index.md)

# DAMON: Data Access MONitoring and Access-aware System Operations

[DAMON](../../../mm/damon/index.md) is a Linux kernel subsystem for efficient data
access monitoring and access-aware system operations.

- [Getting Started](start.md)
  - [Prerequisites](start.md#prerequisites)
  - [Snapshot Data Access Patterns](start.md#snapshot-data-access-patterns)
  - [Recording Data Access Patterns](start.md#recording-data-access-patterns)
  - [Visualizing Recorded Patterns](start.md#visualizing-recorded-patterns)
  - [Data Access Pattern Aware Memory Management](start.md#data-access-pattern-aware-memory-management)
- [Detailed Usages](usage.md)
  - [sysfs Interface](usage.md#sysfs-interface)
  - [Tracepoints for Monitoring Results](usage.md#tracepoints-for-monitoring-results)
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
- [Data Access Monitoring Results Stat](stat.md)
  - [Monitoring Accuracy and Overhead](stat.md#monitoring-accuracy-and-overhead)
  - [Interface: Module Parameters](stat.md#interface-module-parameters)
