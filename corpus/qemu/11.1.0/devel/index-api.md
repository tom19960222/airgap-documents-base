---
collection: qemu
version: "11.1.0"
title: "Internal QEMU APIs"
source_url: https://www.qemu.org/docs/master/devel/index-api.html
fetched_at: 2026-08-21T03:23:06+00:00
---
# Internal QEMU APIs

Details about how QEMU’s various internal APIs. Most of these are
generated from in-code annotations to function prototypes.

- [Bitwise operations](bitops.md)
- [Load and Store APIs](loads-stores.md)
  - [`ld*_p and st*_p`](loads-stores.md#ld-p-and-st-p)
  - [`cpu_{ld,st}*_mmu`](loads-stores.md#cpu-ld-st-mmu)
  - [`cpu_{ld,st}*_mmuidx_ra`](loads-stores.md#cpu-ld-st-mmuidx-ra)
  - [`cpu_{ld,st}*_data_ra`](loads-stores.md#cpu-ld-st-data-ra)
  - [`cpu_{ld,st}*_data`](loads-stores.md#cpu-ld-st-data)
  - [`cpu_ld*_code_mmu`](loads-stores.md#cpu-ld-code-mmu)
  - [`translator_ld*`](loads-stores.md#translator-ld)
  - [`helper_{ld,st}*_mmu`](loads-stores.md#helper-ld-st-mmu)
  - [`address_space_*`](loads-stores.md#address-space)
  - [`address_space_write_rom`](loads-stores.md#address-space-write-rom)
  - [`{ld,st}*_phys`](loads-stores.md#ld-st-phys)
  - [`physical_memory_*`](loads-stores.md#physical-memory)
  - [`cpu_memory_rw_debug`](loads-stores.md#cpu-memory-rw-debug)
  - [`dma_memory_*`](loads-stores.md#dma-memory)
  - [`pci_dma_*` and `{ld,st}*_pci_dma`](loads-stores.md#pci-dma-and-ld-st-pci-dma)
- [Locked Counters (aka `QemuLockCnt`)](lockcnt.md)
  - [`QemuLockCnt` concepts](lockcnt.md#qemulockcnt-concepts)
  - [`QemuLockCnt` API](lockcnt.md#qemulockcnt-api)
  - [`QemuLockCnt` usage](lockcnt.md#qemulockcnt-usage)
- [The memory API](memory.md)
  - [Types of regions](memory.md#types-of-regions)
  - [Migration](memory.md#migration)
  - [Region names](memory.md#region-names)
  - [Region lifecycle](memory.md#region-lifecycle)
  - [Overlapping regions and priority](memory.md#overlapping-regions-and-priority)
  - [Visibility](memory.md#visibility)
  - [Example memory map](memory.md#example-memory-map)
  - [MMIO Operations](memory.md#mmio-operations)
  - [API Reference](memory.md#api-reference)
- [QEMU modules](modules.md)
- [PCI subsystem](pci.md)
  - [API Reference](pci.md#api-reference)
- [QEMU Object Model (QOM) API Reference](qom-api.md)
- [QEMU Device (qdev) API Reference](qdev-api.md)
  - [Realization](qdev-api.md#realization)
  - [Hiding a device](qdev-api.md#hiding-a-device)
- [QEMU UI subsystem](ui.md)
  - [QEMU Clipboard](ui.md#qemu-clipboard)
- [zoned-storage](zoned-storage.md)
  - [1. Block layer APIs for zoned storage](zoned-storage.md#block-layer-apis-for-zoned-storage)
  - [2. Emulating zoned storage controllers](zoned-storage.md#emulating-zoned-storage-controllers)
