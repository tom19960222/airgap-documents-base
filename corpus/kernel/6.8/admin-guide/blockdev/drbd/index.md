---
collection: kernel
version: "6.8"
title: "Distributed Replicated Block Device - DRBD"
source_url: https://www.kernel.org/doc/html/v6.8/admin-guide/blockdev/drbd/index.html
fetched_at: 2026-08-21T03:54:59+00:00
---
# Distributed Replicated Block Device - DRBD

## Description

> DRBD is a shared-nothing, synchronously replicated block device. It
> is designed to serve as a building block for high availability
> clusters and in this context, is a "drop-in" replacement for shared
> storage. Simplistically, you could see it as a network RAID 1.
>
> Please visit <https://www.drbd.org> to find out more.

- [kernel data structure for DRBD-9](data-structure-v9.md)
- [Data flows that Relate some functions, and write packets](figures.md)
- [Sub graphs of DRBD's state transitions](figures.md#sub-graphs-of-drbd-s-state-transitions)
