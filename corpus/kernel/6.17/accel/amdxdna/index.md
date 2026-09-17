---
collection: kernel
version: "6.17"
title: "accel/amdxdna NPU driver"
source_url: https://www.kernel.org/doc/html/v6.17/accel/amdxdna/index.html
fetched_at: 2026-09-16T16:45:45+00:00
---
# accel/amdxdna NPU driver

The accel/amdxdna driver supports the AMD NPU (Neural Processing Unit).

- [AMD NPU](amdnpu.md)
  - [Overview](amdnpu.md#overview)
  - [Hardware Description](amdnpu.md#hardware-description)
    - [AMD XDNA Array](amdnpu.md#amd-xdna-array)
    - [Shared L2 Memory](amdnpu.md#shared-l2-memory)
    - [Microcontroller](amdnpu.md#microcontroller)
    - [Mailboxes](amdnpu.md#mailboxes)
    - [PCIe EP](amdnpu.md#pcie-ep)
    - [Process Isolation Hardware](amdnpu.md#process-isolation-hardware)
  - [Mixed Spatial and Temporal Scheduling](amdnpu.md#mixed-spatial-and-temporal-scheduling)
    - [Resource Solver](amdnpu.md#resource-solver)
  - [Application Binaries](amdnpu.md#application-binaries)
  - [Special Host Buffers](amdnpu.md#special-host-buffers)
    - [Per-context Instruction Buffer](amdnpu.md#per-context-instruction-buffer)
    - [Global Privileged Buffer](amdnpu.md#global-privileged-buffer)
  - [High-level Use Flow](amdnpu.md#high-level-use-flow)
  - [Boot Flow](amdnpu.md#boot-flow)
  - [Userspace components](amdnpu.md#userspace-components)
    - [Compiler](amdnpu.md#compiler)
    - [Usermode Driver (UMD)](amdnpu.md#usermode-driver-umd)
  - [DMA Operation](amdnpu.md#dma-operation)
  - [Error Handling](amdnpu.md#error-handling)
  - [Telemetry](amdnpu.md#telemetry)
  - [References](amdnpu.md#references)
