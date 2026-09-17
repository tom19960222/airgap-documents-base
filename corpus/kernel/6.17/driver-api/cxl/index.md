---
collection: kernel
version: "6.17"
title: "Compute Express Link"
source_url: https://www.kernel.org/doc/html/v6.17/driver-api/cxl/index.html
fetched_at: 2026-09-16T16:19:48+00:00
---
# Compute Express Link

CXL device configuration has a complex handoff between platform (Hardware,
BIOS, EFI), OS (early boot, core kernel, driver), and user policy decisions
that have impacts on each other. The docs here break up configurations steps.

Overview

- [Compute Express Link Driver Theory of Operation](theory-of-operation.md)
  - [The CXL Bus](theory-of-operation.md#the-cxl-bus)
  - [Driver Infrastructure](theory-of-operation.md#driver-infrastructure)
  - [External Interfaces](theory-of-operation.md#external-interfaces)
- [Compute Express Link Subsystem Maturity Map](maturity-map.md)
  - [Feature and Capabilities](maturity-map.md#feature-and-capabilities)
  - [Details](maturity-map.md#details)
- [Compute Express Link: Linux Conventions](conventions.md)
  - [<(template) Title>](conventions.md#template-title)

Device Reference

- [Devices and Protocols](devices/device-types.md)
  - [Protocols](devices/device-types.md#protocols)
  - [Device Types](devices/device-types.md#device-types)
  - [Example Devices](devices/device-types.md#example-devices)

Platform Configuration

- [BIOS/EFI Configuration](platform/bios-and-efi.md)
  - [UEFI Settings](platform/bios-and-efi.md#uefi-settings)
  - [Physical Memory Map](platform/bios-and-efi.md#physical-memory-map)
  - [Decoder Programming](platform/bios-and-efi.md#decoder-programming)
- [ACPI Tables](platform/acpi.md)
  - [CEDT - CXL Early Discovery Table](platform/acpi/cedt.md)
  - [SRAT - Static Resource Affinity Table](platform/acpi/srat.md)
  - [HMAT - Heterogeneous Memory Attribute Table](platform/acpi/hmat.md)
  - [SLIT - System Locality Information Table](platform/acpi/slit.md)
  - [DSDT - Differentiated system Description Table](platform/acpi/dsdt.md)
  - [ACPI Debugging](platform/acpi.md#acpi-debugging)
- [Coherent Device Attribute Table (CDAT)](platform/cdat.md)
- [Device Scoped Memory Affinity Structure (DSMAS)](platform/cdat.md#device-scoped-memory-affinity-structure-dsmas)
- [Device Scoped Latency and Bandwidth Information Structure (DSLBIS)](platform/cdat.md#device-scoped-latency-and-bandwidth-information-structure-dslbis)
- [Switch Scoped Latency and Bandwidth Information Structure (SSLBIS)](platform/cdat.md#switch-scoped-latency-and-bandwidth-information-structure-sslbis)
- [Example Platform Configurations](platform/example-configs.md)
  - [One Device per Host Bridge](platform/example-configurations/one-dev-per-hb.md)
  - [Multiple Devices per Host Bridge](platform/example-configurations/multi-dev-per-hb.md)
  - [Cross-Host-Bridge Interleave](platform/example-configurations/hb-interleave.md)
  - [Flexible Presentation](platform/example-configurations/flexible.md)

Linux Kernel Configuration

- [Overview](linux/overview.md)
- [Linux Init (Early Boot)](linux/early-boot.md)
  - [BIOS, Build and Boot Options](linux/early-boot.md#bios-build-and-boot-options)
  - [Memory Map Creation](linux/early-boot.md#memory-map-creation)
  - [NUMA Node Reservation](linux/early-boot.md#numa-node-reservation)
  - [Memory Tiers Creation](linux/early-boot.md#memory-tiers-creation)
  - [Contiguous Memory Allocation](linux/early-boot.md#contiguous-memory-allocation)
- [CXL Driver Operation](linux/cxl-driver.md)
  - [Drivers](linux/cxl-driver.md#drivers)
  - [Driver Devices](linux/cxl-driver.md#driver-devices)
  - [Decoder Programming](linux/cxl-driver.md#decoder-programming)
  - [Example Configurations](linux/cxl-driver.md#example-configurations)
- [DAX Driver Operation](linux/dax-driver.md)
  - [DAX Device](linux/dax-driver.md#dax-device)
  - [kmem conversion](linux/dax-driver.md#kmem-conversion)
- [Memory Hotplug](linux/memory-hotplug.md)
  - [Default Online Behavior](linux/memory-hotplug.md#default-online-behavior)
  - [Hotplug Memory Block Size](linux/memory-hotplug.md#hotplug-memory-block-size)
  - [Memory Map](linux/memory-hotplug.md#memory-map)
  - [Driver Managed Memory](linux/memory-hotplug.md#driver-managed-memory)
- [CXL Access Coordinates Computation](linux/access-coordinates.md)
  - [Latency and Bandwidth Calculation](linux/access-coordinates.md#latency-and-bandwidth-calculation)
  - [Shared Upstream Link Calculation](linux/access-coordinates.md#shared-upstream-link-calculation)
  - [QTG ID](linux/access-coordinates.md#qtg-id)

Memory Allocation

- [DAX Devices](allocation/dax.md)
- [The Page Allocator](allocation/page-allocator.md)
  - [NUMA nodes and mempolicy](allocation/page-allocator.md#numa-nodes-and-mempolicy)
  - [Memory Zones](allocation/page-allocator.md#memory-zones)
  - [Zone and Node Quirks](allocation/page-allocator.md#zone-and-node-quirks)
  - [CGroups and CPUSets](allocation/page-allocator.md#cgroups-and-cpusets)
- [Reclaim](allocation/reclaim.md)
  - [Demotion](allocation/reclaim.md#demotion)
  - [ZSwap and Node Preference](allocation/reclaim.md#zswap-and-node-preference)
  - [Demotion with ZSwap](allocation/reclaim.md#demotion-with-zswap)
- [Huge Pages](allocation/hugepages.md)
  - [Contiguous Memory Allocator](allocation/hugepages.md#contiguous-memory-allocator)
  - [HugeTLB](allocation/hugepages.md#hugetlb)
