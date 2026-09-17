---
collection: kernel
version: "6.17"
title: "Kexec Handover Concepts"
source_url: https://www.kernel.org/doc/html/v6.17/core-api/kho/concepts.html
fetched_at: 2026-09-16T16:28:58+00:00
---
# Kexec Handover Concepts

Kexec HandOver (KHO) is a mechanism that allows Linux to preserve memory
regions, which could contain serialized system states, across kexec.

It introduces multiple concepts:

## KHO FDT

Every KHO kexec carries a KHO specific flattened device tree (FDT) blob
that describes preserved memory regions. These regions contain either
serialized subsystem states, or in-memory data that shall not be touched
across kexec. After KHO, subsystems can retrieve and restore preserved
memory regions from KHO FDT.

KHO only uses the FDT container format and libfdt library, but does not
adhere to the same property semantics that normal device trees do: Properties
are passed in native endianness and standardized properties like `regs` and
`ranges` do not exist, hence there are no `#...-cells` properties.

KHO is still under development. The FDT schema is unstable and would change
in the future.

## Scratch Regions

To boot into kexec, we need to have a physically contiguous memory range that
contains no handed over memory. Kexec then places the target kernel and initrd
into that region. The new kernel exclusively uses this region for memory
allocations before during boot up to the initialization of the page allocator.

We guarantee that we always have such regions through the scratch regions: On
first boot KHO allocates several physically contiguous memory regions. Since
after kexec these regions will be used by early memory allocations, there is a
scratch region per NUMA node plus a scratch region to satisfy allocations
requests that do not require particular NUMA node assignment.
By default, size of the scratch region is calculated based on amount of memory
allocated during boot. The `kho_scratch` kernel command line option may be
used to explicitly define size of the scratch regions.
The scratch regions are declared as CMA when page allocator is initialized so
that their memory can be used during system lifetime. CMA gives us the
guarantee that no handover pages land in that region, because handover pages
must be at a static physical memory location and CMA enforces that only
movable pages can be located inside.

After KHO kexec, we ignore the `kho_scratch` kernel command line option and
instead reuse the exact same region that was originally allocated. This allows
us to recursively execute any amount of KHO kexecs. Because we used this region
for boot memory allocations and as target memory for kexec blobs, some parts
of that memory region may be reserved. These reservations are irrelevant for
the next KHO, because kexec can overwrite even the original kernel.

## KHO finalization phase

To enable user space based kexec file loader, the kernel needs to be able to
provide the FDT that describes the current kernel’s state before
performing the actual kexec. The process of generating that FDT is
called serialization. When the FDT is generated, some properties
of the system may become immutable because they are already written down
in the FDT. That state is called the KHO finalization phase.

## Public API

struct [folio](../mm-api.md#c.folio "folio") \*kho_restore_folio(phys_addr_t phys)
:   recreates the folio from the preserved memory.

**Parameters**

`phys_addr_t phys`
:   physical address of the folio.

**Return**

pointer to the [`struct folio`](../mm-api.md#c.folio "folio") on success, NULL on failure.

int kho_add_subtree(struct kho_serialization \*ser, const char \*name, void \*fdt)
:   record the physical address of a sub FDT in KHO root tree.

**Parameters**

`struct kho_serialization *ser`
:   serialization control object passed by KHO notifiers.

`const char *name`
:   name of the sub tree.

`void *fdt`
:   the sub tree blob.

**Description**

Creates a new child node named **name** in KHO root FDT and records
the physical address of **fdt**. The pages of **fdt** must also be preserved
by KHO for the new kernel to retrieve it after kexec.

A debugfs blob entry is also created at
`/sys/kernel/debug/kho/out/sub_fdts/**name**`.

**Return**

0 on success, error code on failure

int kho_preserve_folio(struct [folio](concepts.md#c.kho_preserve_folio "folio") \*folio)
:   preserve a folio across kexec.

**Parameters**

`struct folio *folio`
:   folio to preserve.

**Description**

Instructs KHO to preserve the whole folio across kexec. The order
will be preserved as well.

**Return**

0 on success, error code on failure

int kho_preserve_phys(phys_addr_t phys, size_t size)
:   preserve a physically contiguous range across kexec.

**Parameters**

`phys_addr_t phys`
:   physical address of the range.

`size_t size`
:   size of the range.

**Description**

Instructs KHO to preserve the memory range from **phys** to **phys** + **size**
across kexec.

**Return**

0 on success, error code on failure

int kho_retrieve_subtree(const char \*name, phys_addr_t \*phys)
:   retrieve a preserved sub FDT by its name.

**Parameters**

`const char *name`
:   the name of the sub FDT passed to [`kho_add_subtree()`](concepts.md#c.kho_add_subtree "kho_add_subtree").

`phys_addr_t *phys`
:   if found, the physical address of the sub FDT is stored in **phys**.

**Description**

Retrieve a preserved sub FDT named **name** and store its physical
address in **phys**.

**Return**

0 on success, error code on failure
