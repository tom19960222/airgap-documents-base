---
collection: kernel
version: "6.17"
title: "Map Layer"
source_url: https://www.kernel.org/doc/html/v6.17/gpu/xe/xe_map.html
fetched_at: 2026-09-16T16:39:34+00:00
---
# Map Layer

All access to any memory shared with a device (both sysmem and vram) in the
XE driver should go through this layer (xe_map). This layer is built on top
of [Generalizing Access to System and I/O Memory](../../driver-api/device-io.md#generalizing-access-to-system-and-i-o-memory)
and with extra hooks into the XE driver that allows adding asserts to memory
accesses (e.g. for blocking runtime_pm D3Cold on Discrete Graphics).
