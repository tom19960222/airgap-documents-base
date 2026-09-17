---
collection: kernel
version: "6.17"
title: "30. x86_64 Support"
source_url: https://www.kernel.org/doc/html/v6.17/arch/x86/x86_64/index.html
fetched_at: 2026-09-16T16:25:34+00:00
---
# 30. x86_64 Support

- [30.1. General note on [U]EFI x86_64 support](uefi.md)
  - [30.1.1. Mechanics](uefi.md#mechanics)
- [30.2. Memory Management](mm.md)
  - [30.2.1. Complete virtual memory map with 4-level page tables](mm.md#complete-virtual-memory-map-with-4-level-page-tables)
  - [30.2.2. Complete virtual memory map with 5-level page tables](mm.md#complete-virtual-memory-map-with-5-level-page-tables)
- [30.3. 5-level paging](5level-paging.md)
  - [30.3.1. Overview](5level-paging.md#overview)
  - [30.3.2. User-space and large virtual address space](5level-paging.md#user-space-and-large-virtual-address-space)
- [30.4. Fake NUMA For CPUSets](fake-numa-for-cpusets.md)
- [30.5. Firmware support for CPU hotplug under Linux/x86-64](cpu-hotplug-spec.md)
- [30.6. Configurable sysfs parameters for the x86-64 machine check code](machinecheck.md)
- [30.7. Using FS and GS segments in user space applications](fsgs.md)
  - [30.7.1. Common FS and GS usage](fsgs.md#common-fs-and-gs-usage)
  - [30.7.2. Reading and writing the FS/GS base address](fsgs.md#reading-and-writing-the-fs-gs-base-address)
  - [30.7.3. Accessing FS/GS base with arch_prctl()](fsgs.md#accessing-fs-gs-base-with-arch-prctl)
  - [30.7.4. Accessing FS/GS base with the FSGSBASE instructions](fsgs.md#accessing-fs-gs-base-with-the-fsgsbase-instructions)
  - [30.7.5. Compiler support for FS/GS based addressing](fsgs.md#compiler-support-for-fs-gs-based-addressing)
  - [30.7.6. FS/GS based addressing with inline assembly](fsgs.md#fs-gs-based-addressing-with-inline-assembly)
- [30.8. Flexible Return and Event Delivery (FRED)](fred.md)
  - [30.8.1. Overview](fred.md#overview)
  - [30.8.2. Software based event dispatching](fred.md#software-based-event-dispatching)
  - [30.8.3. Full supervisor/user context](fred.md#full-supervisor-user-context)
  - [30.8.4. LKGS](fred.md#lkgs)
  - [30.8.5. Stack levels](fred.md#stack-levels)
