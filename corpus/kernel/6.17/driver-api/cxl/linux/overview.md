---
collection: kernel
version: "6.17"
title: "Overview"
source_url: https://www.kernel.org/doc/html/v6.17/driver-api/cxl/linux/overview.html
fetched_at: 2026-09-16T16:36:39+00:00
---
# Overview

This section presents the configuration process of a CXL Type-3 memory device,
and how it is ultimately exposed to users as either a `DAX` device or
normal memory pages via the kernel’s page allocator.

Portions marked with a bullet are points at which certain kernel objects
are generated.

1. Early Boot

> 1. BIOS, Build, and Boot Parameters
>
> > 1. EFI_MEMORY_SP
> > 2. CONFIG_EFI_SOFT_RESERVE
> > 3. CONFIG_MHP_DEFAULT_ONLINE_TYPE
> > 4. nosoftreserve
>
> 2. Memory Map Creation
>
> > 1. EFI Memory Map / E820 Consulted for Soft-Reserved
> >
> > > - CXL Memory is set aside to be handled by the CXL driver
> > > - Soft-Reserved IO Resource created for CFMWS entry
>
> 3. NUMA Node Creation
>
> > - Nodes created from ACPI CEDT CFMWS and SRAT Proximity domains (PXM)
>
> 4. Memory Tier Creation
>
> > - A default memory_tier is created with all nodes.
>
> 5. Contiguous Memory Allocation
>
> > - Any requested CMA is allocated from Online nodes
>
> 6. Init Finishes, Drivers start probing

2. ACPI and PCI Drivers

> 1. Detects PCI device is CXL, marking it for probe by CXL driver

3. CXL Driver Operation

> 1. Base device creation
>
> > - root, port, and memdev devices created
> > - CEDT CFMWS IO Resource creation
>
> 2. Decoder creation
>
> > - root, switch, and endpoint decoders created
>
> 3. Logical device creation
>
> > - memory_region and endpoint devices created
>
> 4. Devices are associated with each other
>
> > - If auto-decoder (BIOS-programmed decoders), driver validates
> >   configurations, builds associations, and locks configs at probe time.
> > - If user-configured, validation and associations are built at
> >   decoder-commit time.
>
> 5. Regions surfaced as DAX region
>
> > - dax_region created
> > - DAX device created via DAX driver

4. DAX Driver Operation

> 1. DAX driver surfaces DAX region as one of two dax device modes
>
> > - kmem - dax device is converted to hotplug memory blocks
> >
> >   - DAX kmem IO Resource creation
> > - hmem - dax device is left as daxdev to be accessed as a file.
> >
> >   - If hmem, journey ends here.
>
> 2. DAX kmem surfaces memory region to Memory Hotplug to add to page
>    allocator as “driver managed memory”

5. Memory Hotplug

> 1. mhp component surfaces a dax device memory region as multiple memory
>    blocks to the page allocator
>
> > - blocks appear in `/sys/bus/memory/devices` and linked to a NUMA node
>
> 2. blocks are onlined into the requested zone (NORMAL or MOVABLE)
>
> > - Memory is marked “Driver Managed” to avoid kexec from using it as region
> >   for kernel updates
