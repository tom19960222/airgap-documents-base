---
collection: kernel
version: "6.8"
title: "29. x86_64 Support"
source_url: https://www.kernel.org/doc/html/v6.8/arch/x86/x86_64/index.html
fetched_at: 2026-08-21T03:37:20+00:00
---
# 29. x86_64 Support

- [29.1. AMD64 Specific Boot Options](boot-options.md)
  - [29.1.1. Machine check](boot-options.md#machine-check)
  - [29.1.2. APICs](boot-options.md#apics)
  - [29.1.3. Timing](boot-options.md#timing)
  - [29.1.4. Idle loop](boot-options.md#idle-loop)
  - [29.1.5. Rebooting](boot-options.md#rebooting)
  - [29.1.6. NUMA](boot-options.md#numa)
  - [29.1.7. ACPI](boot-options.md#acpi)
  - [29.1.8. PCI](boot-options.md#pci)
  - [29.1.9. IOMMU (input/output memory management unit)](boot-options.md#iommu-input-output-memory-management-unit)
  - [29.1.10. Miscellaneous](boot-options.md#miscellaneous)
  - [29.1.11. AMD SEV (Secure Encrypted Virtualization)](boot-options.md#amd-sev-secure-encrypted-virtualization)
- [29.2. General note on [U]EFI x86_64 support](uefi.md)
  - [29.2.1. Mechanics](uefi.md#mechanics)
- [29.3. Memory Management](mm.md)
  - [29.3.1. Complete virtual memory map with 4-level page tables](mm.md#complete-virtual-memory-map-with-4-level-page-tables)
  - [29.3.2. Complete virtual memory map with 5-level page tables](mm.md#complete-virtual-memory-map-with-5-level-page-tables)
- [29.4. 5-level paging](5level-paging.md)
  - [29.4.1. Overview](5level-paging.md#overview)
  - [29.4.2. Enabling 5-level paging](5level-paging.md#enabling-5-level-paging)
  - [29.4.3. User-space and large virtual address space](5level-paging.md#user-space-and-large-virtual-address-space)
- [29.5. Fake NUMA For CPUSets](fake-numa-for-cpusets.md)
- [29.6. Firmware support for CPU hotplug under Linux/x86-64](cpu-hotplug-spec.md)
- [29.7. Configurable sysfs parameters for the x86-64 machine check code](machinecheck.md)
- [29.8. Using FS and GS segments in user space applications](fsgs.md)
  - [29.8.1. Common FS and GS usage](fsgs.md#common-fs-and-gs-usage)
  - [29.8.2. Reading and writing the FS/GS base address](fsgs.md#reading-and-writing-the-fs-gs-base-address)
  - [29.8.3. Accessing FS/GS base with arch_prctl()](fsgs.md#accessing-fs-gs-base-with-arch-prctl)
  - [29.8.4. Accessing FS/GS base with the FSGSBASE instructions](fsgs.md#accessing-fs-gs-base-with-the-fsgsbase-instructions)
  - [29.8.5. Compiler support for FS/GS based addressing](fsgs.md#compiler-support-for-fs-gs-based-addressing)
  - [29.8.6. FS/GS based addressing with inline assembly](fsgs.md#fs-gs-based-addressing-with-inline-assembly)
