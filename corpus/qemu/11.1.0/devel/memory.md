---
collection: qemu
version: "11.1.0"
title: "The memory API"
source_url: https://www.qemu.org/docs/master/devel/memory.html
fetched_at: 2026-08-21T03:25:53+00:00
---
# The memory API

The memory API models the memory and I/O buses and controllers of a QEMU
machine. It attempts to allow modelling of:

- ordinary RAM
- memory-mapped I/O (MMIO)
- memory controllers that can dynamically reroute physical memory regions
  to different destinations

The memory model provides support for

- tracking RAM changes by the guest
- setting up coalesced memory for kvm
- setting up ioeventfd regions for kvm

Memory is modelled as an acyclic graph of MemoryRegion objects. Sinks
(leaves) are RAM and MMIO regions, while other nodes represent
buses, memory controllers, and memory regions that have been rerouted.

In addition to MemoryRegion objects, the memory API provides AddressSpace
objects for every root and possibly for intermediate MemoryRegions too.
These represent memory as seen from the CPU or a device’s viewpoint.

## Types of regions

There are multiple types of memory regions (all represented by a single C type
MemoryRegion):

- RAM: a RAM region is simply a range of host memory that can be made available
  to the guest.
  You typically initialize these with memory_region_init_ram(). Some special
  purposes require the variants memory_region_init_resizeable_ram(),
  memory_region_init_ram_from_file(), or memory_region_init_ram_ptr().
- MMIO: a range of guest memory that is implemented by host callbacks;
  each read or write causes a callback to be called on the host.
  You initialize these with memory_region_init_io(), passing it a
  MemoryRegionOps structure describing the callbacks.
- ROM: a ROM memory region works like RAM for reads (directly accessing
  a region of host memory), and forbids writes. You initialize these with
  memory_region_init_rom().
- ROM device: a ROM device memory region works like RAM for reads
  (directly accessing a region of host memory), but like MMIO for
  writes (invoking a callback). You initialize these with
  memory_region_init_rom_device().
- IOMMU region: an IOMMU region translates addresses of accesses made to it
  and forwards them to some other target memory region. As the name suggests,
  these are only needed for modelling an IOMMU, not for simple devices.
  You initialize these with memory_region_init_iommu().
- container: a container simply includes other memory regions, each at
  a different offset. Containers are useful for grouping several regions
  into one unit. For example, a PCI BAR may be composed of a RAM region
  and an MMIO region.

  A container’s subregions are usually non-overlapping. In some cases it is
  useful to have overlapping regions; for example a memory controller that
  can overlay a subregion of RAM with MMIO or ROM, or a PCI controller
  that does not prevent card from claiming overlapping BARs.

  You initialize a pure container with memory_region_init().
- alias: a subsection of another region. Aliases allow a region to be
  split apart into discontiguous regions. Examples of uses are memory
  banks used when the guest address space is smaller than the amount
  of RAM addressed, or a memory controller that splits main memory to
  expose a “PCI hole”. You can also create aliases to avoid trying to
  add the original region to multiple parents via
  [`memory_region_add_subregion`](memory.md#c.memory_region_add_subregion "memory_region_add_subregion").

  Aliases may point to any type of region, including other aliases,
  but an alias may not point back to itself, directly or indirectly.
  You initialize these with memory_region_init_alias().
- reservation region: a reservation region is primarily for debugging.
  It claims I/O space that is not supposed to be handled by QEMU itself.
  The typical use is to track parts of the address space which will be
  handled by the host kernel when KVM is enabled. You initialize these
  by passing a NULL callback parameter to memory_region_init_io().

It is valid to add subregions to a region which is not a pure container
(that is, to an MMIO, RAM or ROM region). This means that the region
will act like a container, except that any addresses within the container’s
region which are not claimed by any subregion are handled by the
container itself (ie by its MMIO callbacks or RAM backing). However
it is generally possible to achieve the same effect with a pure container
one of whose subregions is a low priority “background” region covering
the whole address range; this is often clearer and is preferred.
Subregions cannot be added to an alias region.

## Migration

Where the memory region is backed by host memory (RAM, ROM and
ROM device memory region types), this host memory needs to be
copied to the destination on migration. These APIs which allocate
the host memory for you will also register the memory so it is
migrated:

- memory_region_init_ram()
- memory_region_init_rom()
- memory_region_init_rom_device()

For most devices and boards this is the correct thing. If you
have a special case where you need to manage the migration of
the backing memory yourself, you can call the function
memory_region_init_ram_flags_nomigrate()
which only initializes the MemoryRegion and leaves handling
migration to the caller.

The functions:

- memory_region_init_resizeable_ram()
- memory_region_init_ram_from_file()
- memory_region_init_ram_from_fd()
- memory_region_init_ram_ptr()
- memory_region_init_ram_device_ptr()

are for special cases only, and so they do not automatically
register the backing memory for migration; the caller must
manage migration if necessary.

## Region names

Regions are assigned names by the constructor. For most regions these are
only used for debugging purposes, but RAM regions also use the name to identify
live migration sections. This means that RAM region names need to have ABI
stability.

## Region lifecycle

A region is created by one of the memory_region_init\*() functions and
attached to an object, which acts as its owner or parent. QEMU ensures
that the owner object remains alive as long as the region is visible to
the guest, or as long as the region is in use by a virtual CPU or another
device. For example, the owner object will not die between an
address_space_map operation and the corresponding address_space_unmap.

After creation, a region can be added to an address space or a
container with memory_region_add_subregion(), and removed using
memory_region_del_subregion().

Various region attributes (read-only, dirty logging, coalesced mmio,
ioeventfd) can be changed during the region lifecycle. They take effect
as soon as the region is made visible. This can be immediately, later,
or never.

Destruction of a memory region happens automatically when the owner object
dies. When there are multiple memory regions under the same owner object,
the memory API will guarantee all memory regions will be properly detached
and finalized one by one. The order in which memory regions will be
finalized is not guaranteed.

If however the memory region is part of a dynamically allocated data
structure, you should free the memory region in the instance_finalize
callback. For an example see VFIOMSIXInfo and VFIOQuirk in
hw/vfio/pci.c.

You must not destroy a memory region as long as it may be in use by a
device or CPU. In order to do this, as a general rule do not create or
destroy memory regions dynamically during a device’s lifetime, and never
call object_unparent().

If you break this rule, the following situation can happen:

- the memory region’s owner had a reference taken via memory_region_ref
  (for example by address_space_map)
- the region is unparented, and has no owner anymore
- when address_space_unmap is called, the reference to the memory region’s
  owner is leaked.

There is an exception to the above rule: it is okay to call
object_unparent at any time for an alias or a container region. It is
therefore also okay to create or destroy alias and container regions
dynamically during a device’s lifetime.

This exceptional usage is valid because aliases and containers only help
QEMU building the guest’s memory map; they are never accessed directly.
memory_region_ref and memory_region_unref are never called on aliases
or containers, and the above situation then cannot happen. Exploiting
this exception is rarely necessary, and therefore it is discouraged,
but nevertheless it is used in a few places.

For regions that “have no owner” (NULL is passed at creation time), the
machine object is actually used as the owner.

## Overlapping regions and priority

Usually, regions may not overlap each other; a memory address decodes into
exactly one target. In some cases it is useful to allow regions to overlap,
and sometimes to control which of an overlapping regions is visible to the
guest. This is done with memory_region_add_subregion_overlap(), which
allows the region to overlap any other region in the same container, and
specifies a priority that allows the core to decide which of two regions at
the same address are visible (highest wins).
Priority values are signed, and the default value is zero. This means that
you can use memory_region_add_subregion_overlap() both to specify a region
that must sit ‘above’ any others (with a positive priority) and also a
background region that sits ‘below’ others (with a negative priority).

If the higher priority region in an overlap is a container or alias, then
the lower priority region will appear in any “holes” that the higher priority
region has left by not mapping subregions to that area of its address range.
(This applies recursively – if the subregions are themselves containers or
aliases that leave holes then the lower priority region will appear in these
holes too.)

For example, suppose we have a container A of size 0x8000 with two subregions
B and C. B is a container mapped at 0x2000, size 0x4000, priority 2; C is
an MMIO region mapped at 0x0, size 0x6000, priority 1. B currently has two
of its own subregions: D of size 0x1000 at offset 0 and E of size 0x1000 at
offset 0x2000. As a diagram:

```
      0      1000   2000   3000   4000   5000   6000   7000   8000
      |------|------|------|------|------|------|------|------|
A:    [                                                      ]
C:    [CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC]
B:                  [                          ]
D:                  [DDDDD]
E:                                [EEEEE]
```

The regions that will be seen within this address range then are:

```
[CCCCCCCCCCCC][DDDDD][CCCCC][EEEEE][CCCCC]
```

Since B has higher priority than C, its subregions appear in the flat map
even where they overlap with C. In ranges where B has not mapped anything
C’s region appears.

If B had provided its own MMIO operations (ie it was not a pure container)
then these would be used for any addresses in its range not handled by
D or E, and the result would be:

```
[CCCCCCCCCCCC][DDDDD][BBBBB][EEEEE][BBBBB]
```

Priority values are local to a container, because the priorities of two
regions are only compared when they are both children of the same container.
This means that the device in charge of the container (typically modelling
a bus or a memory controller) can use them to manage the interaction of
its child regions without any side effects on other parts of the system.
In the example above, the priorities of D and E are unimportant because
they do not overlap each other. It is the relative priority of B and C
that causes D and E to appear on top of C: D and E’s priorities are never
compared against the priority of C.

## Visibility

The memory core uses the following rules to select a memory region when the
guest accesses an address:

- all direct subregions of the root region are matched against the address, in
  descending priority order

  - if the address lies outside the region offset/size, the subregion is
    discarded
  - if the subregion is a leaf (RAM or MMIO), the search terminates, returning
    this leaf region
  - if the subregion is a container, the same algorithm is used within the
    subregion (after the address is adjusted by the subregion offset)
  - if the subregion is an alias, the search is continued at the alias target
    (after the address is adjusted by the subregion offset and alias offset)
  - if a recursive search within a container or alias subregion does not
    find a match (because of a “hole” in the container’s coverage of its
    address range), then if this is a container with its own MMIO or RAM
    backing the search terminates, returning the container itself. Otherwise
    we continue with the next subregion in priority order
- if none of the subregions match the address then the search terminates
  with no match found

## Example memory map

```
system_memory: container@0-2^48-1
 |
 +---- lomem: alias@0-0xdfffffff ---> #ram (0-0xdfffffff)
 |
 +---- himem: alias@0x100000000-0x11fffffff ---> #ram (0xe0000000-0xffffffff)
 |
 +---- vga-window: alias@0xa0000-0xbffff ---> #pci (0xa0000-0xbffff)
 |      (prio 1)
 |
 +---- pci-hole: alias@0xe0000000-0xffffffff ---> #pci (0xe0000000-0xffffffff)

pci (0-2^32-1)
 |
 +--- vga-area: container@0xa0000-0xbffff
 |      |
 |      +--- alias@0x00000-0x7fff  ---> #vram (0x010000-0x017fff)
 |      |
 |      +--- alias@0x08000-0xffff  ---> #vram (0x020000-0x027fff)
 |
 +---- vram: ram@0xe1000000-0xe1ffffff
 |
 +---- vga-mmio: mmio@0xe2000000-0xe200ffff

ram: ram@0x00000000-0xffffffff
```

This is a (simplified) PC memory map. The 4GB RAM block is mapped into the
system address space via two aliases: “lomem” is a 1:1 mapping of the first
3.5GB; “himem” maps the last 0.5GB at address 4GB. This leaves 0.5GB for the
so-called PCI hole, that allows a 32-bit PCI bus to exist in a system with
4GB of memory.

The memory controller diverts addresses in the range 640K-768K to the PCI
address space. This is modelled using the “vga-window” alias, mapped at a
higher priority so it obscures the RAM at the same addresses. The vga window
can be removed by programming the memory controller; this is modelled by
removing the alias and exposing the RAM underneath.

The pci address space is not a direct child of the system address space, since
we only want parts of it to be visible (we accomplish this using aliases).
It has two subregions: vga-area models the legacy vga window and is occupied
by two 32K memory banks pointing at two sections of the framebuffer.
In addition the vram is mapped as a BAR at address e1000000, and an additional
BAR containing MMIO registers is mapped after it.

Note that if the guest maps a BAR outside the PCI hole, it would not be
visible as the pci-hole alias clips it to a 0.5GB range.

## MMIO Operations

MMIO regions are provided with ->read() and ->write() callbacks,
which are sufficient for most devices. Some devices change behaviour
based on the attributes used for the memory transaction, or need
to be able to respond that the access should provoke a bus error
rather than completing successfully; those devices can use the
->read_with_attrs() and ->write_with_attrs() callbacks instead.

In addition various constraints can be supplied to control how these
callbacks are called:

- .valid.min_access_size, .valid.max_access_size define the access sizes
  (in bytes) which the device accepts; accesses outside this range will
  have device and bus specific behaviour (ignored, or machine check)
- .valid.unaligned specifies that the *device being modelled* supports
  unaligned accesses; if false, unaligned accesses will invoke the
  appropriate bus or CPU specific behaviour.
- .impl.min_access_size, .impl.max_access_size define the access sizes
  (in bytes) supported by the *implementation*; other access sizes will be
  emulated using the ones available. For example a 4-byte write will be
  emulated using four 1-byte writes, if .impl.max_access_size = 1.
- .impl.unaligned specifies that the *implementation* supports unaligned
  accesses; if false, unaligned accesses will be emulated by two aligned
  accesses.

## API Reference

struct MemoryRegionSection
:   describes a fragment of a `MemoryRegion`

**Definition**:

```
struct MemoryRegionSection {
    Int128 size;
    MemoryRegion *mr;
    FlatView *fv;
    hwaddr offset_within_region;
    hwaddr offset_within_address_space;
    bool readonly;
    bool nonvolatile;
    bool unmergeable;
};
```

**Members**

`size`
:   the size of the section; will not exceed **mr**’s boundaries

`mr`
:   the region, or `NULL` if empty

`fv`
:   the flat view of the address space the region is mapped in

`offset_within_region`
:   the beginning of the section, relative to **mr**’s start

`offset_within_address_space`
:   the address of the first byte of the section
    relative to the region’s address space

`readonly`
:   writes to this section are ignored

`nonvolatile`
:   this section is non-volatile

`unmergeable`
:   this section should not get merged with adjacent sections

MemoryRegion \*memory_translate_iotlb(IOMMUTLBEntry \*iotlb, hwaddr \*xlat_p, Error \*\*errp)
:   Extract addresses from a TLB entry. Called with rcu_read_lock held.

**Parameters**

`IOMMUTLBEntry *iotlb`
:   pointer to an `IOMMUTLBEntry`

`hwaddr *xlat_p`
:   return the offset of the entry from the start of the returned
    MemoryRegion.

`Error **errp`
:   pointer to Error\*, to store an error if it happens.

**Return**

On success, return the MemoryRegion containing the **iotlb** translated
addr. The MemoryRegion must not be accessed after rcu_read_unlock.
On failure, return NULL, setting **errp** with error.

struct MemoryListener
:   callbacks structure for updates to the physical memory map

**Definition**:

```
struct MemoryListener {
    void (*begin)(MemoryListener *listener);
    void (*commit)(MemoryListener *listener);
    void (*region_add)(MemoryListener *listener, MemoryRegionSection *section);
    void (*region_del)(MemoryListener *listener, MemoryRegionSection *section);
    void (*region_nop)(MemoryListener *listener, MemoryRegionSection *section);
    void (*log_start)(MemoryListener *listener, MemoryRegionSection *section, int old_val, int new_val);
    void (*log_stop)(MemoryListener *listener, MemoryRegionSection *section, int old_val, int new_val);
    void (*log_sync)(MemoryListener *listener, MemoryRegionSection *section);
    void (*log_sync_global)(MemoryListener *listener, bool last_stage);
    void (*log_clear)(MemoryListener *listener, MemoryRegionSection *section);
    bool (*log_global_start)(MemoryListener *listener, Error **errp);
    void (*log_global_stop)(MemoryListener *listener);
    void (*log_global_after_sync)(MemoryListener *listener);
    void (*eventfd_add)(MemoryListener *listener, MemoryRegionSection *section, bool match_data, uint64_t data, EventNotifier *e);
    void (*eventfd_del)(MemoryListener *listener, MemoryRegionSection *section, bool match_data, uint64_t data, EventNotifier *e);
    void (*coalesced_io_add)(MemoryListener *listener, MemoryRegionSection *section, hwaddr addr, hwaddr len);
    void (*coalesced_io_del)(MemoryListener *listener, MemoryRegionSection *section, hwaddr addr, hwaddr len);
    unsigned priority;
    const char *name;
};
```

**Members**

`begin`
:   Called at the beginning of an address space update transaction.
    Followed by calls to [`MemoryListener.region_add()`](memory.md#c.MemoryListener "MemoryListener"),
    [`MemoryListener.region_del()`](memory.md#c.MemoryListener "MemoryListener"), [`MemoryListener.region_nop()`](memory.md#c.MemoryListener "MemoryListener"),
    [`MemoryListener.log_start()`](memory.md#c.MemoryListener "MemoryListener") and [`MemoryListener.log_stop()`](memory.md#c.MemoryListener "MemoryListener") in
    increasing address order.

    **listener**: The [`MemoryListener`](memory.md#c.MemoryListener "MemoryListener").

`commit`
:   Called at the end of an address space update transaction,
    after the last call to [`MemoryListener.region_add()`](memory.md#c.MemoryListener "MemoryListener"),
    [`MemoryListener.region_del()`](memory.md#c.MemoryListener "MemoryListener") or [`MemoryListener.region_nop()`](memory.md#c.MemoryListener "MemoryListener"),
    [`MemoryListener.log_start()`](memory.md#c.MemoryListener "MemoryListener") and [`MemoryListener.log_stop()`](memory.md#c.MemoryListener "MemoryListener").

    **listener**: The [`MemoryListener`](memory.md#c.MemoryListener "MemoryListener").

`region_add`
:   Called during an address space update transaction,
    for a section of the address space that is new in this address space
    space since the last transaction.

    **listener**: The [`MemoryListener`](memory.md#c.MemoryListener "MemoryListener").
    **section**: The new [`MemoryRegionSection`](memory.md#c.MemoryRegionSection "MemoryRegionSection").

`region_del`
:   Called during an address space update transaction,
    for a section of the address space that has disappeared in the address
    space since the last transaction.

    **listener**: The [`MemoryListener`](memory.md#c.MemoryListener "MemoryListener").
    **section**: The old [`MemoryRegionSection`](memory.md#c.MemoryRegionSection "MemoryRegionSection").

`region_nop`
:   Called during an address space update transaction,
    for a section of the address space that is in the same place in the address
    space as in the last transaction.

    **listener**: The [`MemoryListener`](memory.md#c.MemoryListener "MemoryListener").
    **section**: The [`MemoryRegionSection`](memory.md#c.MemoryRegionSection "MemoryRegionSection").

`log_start`
:   Called during an address space update transaction, after
    one of [`MemoryListener.region_add()`](memory.md#c.MemoryListener "MemoryListener"), [`MemoryListener.region_del()`](memory.md#c.MemoryListener "MemoryListener") or
    [`MemoryListener.region_nop()`](memory.md#c.MemoryListener "MemoryListener"), if dirty memory logging clients have
    become active since the last transaction.

    **listener**: The [`MemoryListener`](memory.md#c.MemoryListener "MemoryListener").
    **section**: The [`MemoryRegionSection`](memory.md#c.MemoryRegionSection "MemoryRegionSection").
    **old**: A bitmap of dirty memory logging clients that were active in
    the previous transaction.
    **new**: A bitmap of dirty memory logging clients that are active in
    the current transaction.

`log_stop`
:   Called during an address space update transaction, after
    one of [`MemoryListener.region_add()`](memory.md#c.MemoryListener "MemoryListener"), [`MemoryListener.region_del()`](memory.md#c.MemoryListener "MemoryListener") or
    [`MemoryListener.region_nop()`](memory.md#c.MemoryListener "MemoryListener") and possibly after
    [`MemoryListener.log_start()`](memory.md#c.MemoryListener "MemoryListener"), if dirty memory logging clients have
    become inactive since the last transaction.

    **listener**: The [`MemoryListener`](memory.md#c.MemoryListener "MemoryListener").
    **section**: The [`MemoryRegionSection`](memory.md#c.MemoryRegionSection "MemoryRegionSection").
    **old**: A bitmap of dirty memory logging clients that were active in
    the previous transaction.
    **new**: A bitmap of dirty memory logging clients that are active in
    the current transaction.

`log_sync`
:   Called by memory_region_snapshot_and_clear_dirty() and
    memory_global_dirty_log_sync(), before accessing QEMU’s “official”
    copy of the dirty memory bitmap for a [`MemoryRegionSection`](memory.md#c.MemoryRegionSection "MemoryRegionSection").

    **listener**: The [`MemoryListener`](memory.md#c.MemoryListener "MemoryListener").
    **section**: The [`MemoryRegionSection`](memory.md#c.MemoryRegionSection "MemoryRegionSection").

`log_sync_global`
:   This is the global version of **log_sync** when the listener does
    not have a way to synchronize the log with finer granularity.
    When the listener registers with **log_sync_global** defined, then
    its **log_sync** must be NULL. Vice versa.

    **listener**: The [`MemoryListener`](memory.md#c.MemoryListener "MemoryListener").
    **last_stage**: The last stage to synchronize the log during migration.
    The caller should guarantee that the synchronization with true for
    **last_stage** is triggered for once after all VCPUs have been stopped.

`log_clear`
:   Called before reading the dirty memory bitmap for a
    [`MemoryRegionSection`](memory.md#c.MemoryRegionSection "MemoryRegionSection").

    **listener**: The [`MemoryListener`](memory.md#c.MemoryListener "MemoryListener").
    **section**: The [`MemoryRegionSection`](memory.md#c.MemoryRegionSection "MemoryRegionSection").

`log_global_start`
:   Called by memory_global_dirty_log_start(), which
    enables the `DIRTY_LOG_MIGRATION` client on all memory regions in
    the address space. [`MemoryListener.log_global_start()`](memory.md#c.MemoryListener "MemoryListener") is also
    called when a [`MemoryListener`](memory.md#c.MemoryListener "MemoryListener") is added, if global dirty logging is
    active at that time.

    **listener**: The [`MemoryListener`](memory.md#c.MemoryListener "MemoryListener").
    **errp**: pointer to Error\*, to store an error if it happens.

    Return: true on success, else false setting **errp** with error.

`log_global_stop`
:   Called by memory_global_dirty_log_stop(), which
    disables the `DIRTY_LOG_MIGRATION` client on all memory regions in
    the address space.

    **listener**: The [`MemoryListener`](memory.md#c.MemoryListener "MemoryListener").

`log_global_after_sync`
:   Called after reading the dirty memory bitmap
    for any [`MemoryRegionSection`](memory.md#c.MemoryRegionSection "MemoryRegionSection").

    **listener**: The [`MemoryListener`](memory.md#c.MemoryListener "MemoryListener").

`eventfd_add`
:   Called during an address space update transaction,
    for a section of the address space that has had a new ioeventfd
    registration since the last transaction.

    **listener**: The [`MemoryListener`](memory.md#c.MemoryListener "MemoryListener").
    **section**: The new [`MemoryRegionSection`](memory.md#c.MemoryRegionSection "MemoryRegionSection").
    **match_data**: The **match_data** parameter for the new ioeventfd.
    **data**: The **data** parameter for the new ioeventfd.
    **e**: The `EventNotifier` parameter for the new ioeventfd.

`eventfd_del`
:   Called during an address space update transaction,
    for a section of the address space that has dropped an ioeventfd
    registration since the last transaction.

    **listener**: The [`MemoryListener`](memory.md#c.MemoryListener "MemoryListener").
    **section**: The new [`MemoryRegionSection`](memory.md#c.MemoryRegionSection "MemoryRegionSection").
    **match_data**: The **match_data** parameter for the dropped ioeventfd.
    **data**: The **data** parameter for the dropped ioeventfd.
    **e**: The `EventNotifier` parameter for the dropped ioeventfd.

`coalesced_io_add`
:   Called during an address space update transaction,
    for a section of the address space that has had a new coalesced
    MMIO range registration since the last transaction.

    **listener**: The [`MemoryListener`](memory.md#c.MemoryListener "MemoryListener").
    **section**: The new [`MemoryRegionSection`](memory.md#c.MemoryRegionSection "MemoryRegionSection").
    **addr**: The starting address for the coalesced MMIO range.
    **len**: The length of the coalesced MMIO range.

`coalesced_io_del`
:   Called during an address space update transaction,
    for a section of the address space that has dropped a coalesced
    MMIO range since the last transaction.

    **listener**: The [`MemoryListener`](memory.md#c.MemoryListener "MemoryListener").
    **section**: The new [`MemoryRegionSection`](memory.md#c.MemoryRegionSection "MemoryRegionSection").
    **addr**: The starting address for the coalesced MMIO range.
    **len**: The length of the coalesced MMIO range.

`priority`
:   Govern the order in which memory listeners are invoked. Lower priorities
    are invoked earlier for “add” or “start” callbacks, and later for “delete”
    or “stop” callbacks.

`name`
:   Name of the listener. It can be used in contexts where we’d like to
    identify one memory listener with the rest.

**Description**

Allows a component to adjust to changes in the guest-visible memory map.
Use with memory_listener_register() and memory_listener_unregister().

struct AddressSpace
:   describes a mapping of addresses to `MemoryRegion` objects

**Definition**:

```
struct AddressSpace {
};
```

**Members**

flatview_cb
:   **Typedef**: callback for flatview_for_each_range()

**Syntax**

> `bool flatview_cb (Int128 start, Int128 len, const MemoryRegion *mr, hwaddr offset_in_region, void *opaque)`

**Parameters**

`Int128 start`
:   start address of the range within the FlatView

`Int128 len`
:   length of the range in bytes

`const MemoryRegion *mr`
:   MemoryRegion covering this range

`hwaddr offset_in_region`
:   offset of the first byte of the range within **mr**

`void *opaque`
:   data pointer passed to flatview_for_each_range()

**Return**

true to stop the iteration, false to keep going.

void flatview_for_each_range(FlatView \*fv, [flatview_cb](memory.md#c.flatview_cb "flatview_cb") cb, void \*opaque)
:   Iterate through a FlatView

**Parameters**

`FlatView *fv`
:   the FlatView to iterate through

`flatview_cb cb`
:   function to call for each range

`void *opaque`
:   opaque data pointer to pass to **cb**

**Description**

A FlatView is made up of a list of non-overlapping ranges, each of
which is a slice of a MemoryRegion. This function iterates through
each range in **fv**, calling **cb**. The callback function can terminate
iteration early by returning ‘true’.

[MemoryRegionSection](memory.md#c.MemoryRegionSection "MemoryRegionSection") \*memory_region_section_new_copy([MemoryRegionSection](memory.md#c.MemoryRegionSection "MemoryRegionSection") \*s)
:   Copy a memory region section

**Parameters**

`MemoryRegionSection *s`
:   the [`MemoryRegionSection`](memory.md#c.MemoryRegionSection "MemoryRegionSection") to copy

**Description**

Allocate memory for a new copy, copy the memory region section, and
properly take a reference on all relevant members.

void memory_region_section_free_copy([MemoryRegionSection](memory.md#c.MemoryRegionSection "MemoryRegionSection") \*s)
:   Free a copied memory region section

**Parameters**

`MemoryRegionSection *s`
:   the [`MemoryRegionSection`](memory.md#c.MemoryRegionSection "MemoryRegionSection") to copy

**Description**

Free a copy of a memory section created via memory_region_section_new_copy().
properly dropping references on all relevant members.

bool memory_region_section_intersect_range([MemoryRegionSection](memory.md#c.MemoryRegionSection "MemoryRegionSection") \*s, uint64_t offset, uint64_t size)
:   Adjust the memory section to cover the intersection with the given range.

**Parameters**

`MemoryRegionSection *s`
:   the [`MemoryRegionSection`](memory.md#c.MemoryRegionSection "MemoryRegionSection") to be adjusted

`uint64_t offset`
:   the offset of the given range in the memory region

`uint64_t size`
:   the size of the given range

**Description**

Returns false if the intersection is empty, otherwise returns true.

void memory_region_init(MemoryRegion \*mr, [Object](qom-api.md#c.Object "Object") \*owner, const char \*name, uint64_t size)
:   Initialize a memory region

**Parameters**

`MemoryRegion *mr`
:   the `MemoryRegion` to be initialized

`Object *owner`
:   the object that tracks the region’s reference count

`const char *name`
:   used for debugging; not visible to the user or ABI

`uint64_t size`
:   size of the region; any subregions beyond this size will be clipped

**Description**

The region typically acts as a container for other memory regions. Use
memory_region_add_subregion() to add subregions.

void memory_region_ref(MemoryRegion \*mr)
:   Add 1 to a memory region’s reference count

**Parameters**

`MemoryRegion *mr`
:   the `MemoryRegion`

**Description**

Whenever memory regions are accessed outside the BQL, they need to be
preserved against hot-unplug. MemoryRegions actually do not have their
own reference count; they piggyback on a QOM object, their “owner”.
This function adds a reference to the owner.

All MemoryRegions must have an owner if they can disappear, even if the
device they belong to operates exclusively under the BQL. This is because
the region could be returned at any time by memory_region_find, and this
is usually under guest control.

void memory_region_unref(MemoryRegion \*mr)
:   Remove 1 to a memory region’s reference count

**Parameters**

`MemoryRegion *mr`
:   the `MemoryRegion`

**Description**

Whenever memory regions are accessed outside the BQL, they need to be
preserved against hot-unplug. MemoryRegions actually do not have their
own reference count; they piggyback on a QOM object, their “owner”.
This function removes a reference to the owner and possibly destroys it.

void memory_region_init_io(MemoryRegion \*mr, [Object](qom-api.md#c.Object "Object") \*owner, const MemoryRegionOps \*ops, void \*opaque, const char \*name, uint64_t size)
:   Initialize an I/O memory region.

**Parameters**

`MemoryRegion *mr`
:   the `MemoryRegion` to be initialized.

`Object *owner`
:   the object that tracks the region’s reference count

`const MemoryRegionOps *ops`
:   a structure containing read and write callbacks to be used when
    I/O is performed on the region.

`void *opaque`
:   passed to the read and write callbacks of the **ops** structure.

`const char *name`
:   used for debugging; not visible to the user or ABI

`uint64_t size`
:   size of the region.

**Description**

Accesses into the region will cause the callbacks in **ops** to be called.
if **size** is nonzero, subregions will be clipped to **size**.

bool memory_region_init_ram_flags_nomigrate(MemoryRegion \*mr, [Object](qom-api.md#c.Object "Object") \*owner, const char \*name, uint64_t size, uint32_t ram_flags, Error \*\*errp)
:   Initialize RAM memory region. Accesses into the region will modify memory directly.

**Parameters**

`MemoryRegion *mr`
:   the `MemoryRegion` to be initialized.

`Object *owner`
:   the object that tracks the region’s reference count

`const char *name`
:   Region name, becomes part of RAMBlock name used in migration stream
    must be unique within any device

`uint64_t size`
:   size of the region.

`uint32_t ram_flags`
:   RamBlock flags. Supported flags: RAM_SHARED, RAM_NORESERVE,
    RAM_GUEST_MEMFD.

`Error **errp`
:   pointer to Error\*, to store an error if it happens.

**Description**

Note that this function does not do anything to cause the data in the
RAM memory region to be migrated; that is the responsibility of the caller.

**Return**

true on success, else false setting **errp** with error.

bool memory_region_init_resizeable_ram(MemoryRegion \*mr, [Object](qom-api.md#c.Object "Object") \*owner, const char \*name, uint64_t size, uint64_t max_size, void (\*resized)(const char\*, uint64_t length, void \*host), Error \*\*errp)
:   Initialize memory region with resizable RAM. Accesses into the region will modify memory directly. Only an initial portion of this RAM is actually used. Changing the size while migrating can result in the migration being canceled.

**Parameters**

`MemoryRegion *mr`
:   the `MemoryRegion` to be initialized.

`Object *owner`
:   the object that tracks the region’s reference count

`const char *name`
:   Region name, becomes part of RAMBlock name used in migration stream
    must be unique within any device

`uint64_t size`
:   used size of the region.

`uint64_t max_size`
:   max size of the region.

`void (*resized)(const char*, uint64_t length, void *host)`
:   callback to notify owner about used size change.

`Error **errp`
:   pointer to Error\*, to store an error if it happens.

**Description**

Note that this function does not do anything to cause the data in the
RAM memory region to be migrated; that is the responsibility of the caller.

**Return**

true on success, else false setting **errp** with error.

bool memory_region_init_ram_from_file(MemoryRegion \*mr, [Object](qom-api.md#c.Object "Object") \*owner, const char \*name, uint64_t size, uint64_t align, uint32_t ram_flags, const char \*path, ram_addr_t offset, Error \*\*errp)
:   Initialize RAM memory region with a mmap-ed backend.

**Parameters**

`MemoryRegion *mr`
:   the `MemoryRegion` to be initialized.

`Object *owner`
:   the object that tracks the region’s reference count

`const char *name`
:   Region name, becomes part of RAMBlock name used in migration stream
    must be unique within any device

`uint64_t size`
:   size of the region.

`uint64_t align`
:   alignment of the region base address; if 0, the default alignment
    (getpagesize()) will be used.

`uint32_t ram_flags`
:   RamBlock flags. Supported flags: RAM_SHARED, RAM_PMEM,
    RAM_NORESERVE, RAM_PROTECTED, RAM_NAMED_FILE, RAM_READONLY,
    RAM_READONLY_FD, RAM_GUEST_MEMFD

`const char *path`
:   the path in which to allocate the RAM.

`ram_addr_t offset`
:   offset within the file referenced by path

`Error **errp`
:   pointer to Error\*, to store an error if it happens.

**Description**

Note that this function does not do anything to cause the data in the
RAM memory region to be migrated; that is the responsibility of the caller.

**Return**

true on success, else false setting **errp** with error.

bool memory_region_init_ram_from_fd(MemoryRegion \*mr, [Object](qom-api.md#c.Object "Object") \*owner, const char \*name, uint64_t size, uint32_t ram_flags, int fd, ram_addr_t offset, Error \*\*errp)
:   Initialize RAM memory region with a mmap-ed backend.

**Parameters**

`MemoryRegion *mr`
:   the `MemoryRegion` to be initialized.

`Object *owner`
:   the object that tracks the region’s reference count

`const char *name`
:   the name of the region.

`uint64_t size`
:   size of the region.

`uint32_t ram_flags`
:   RamBlock flags. Supported flags: RAM_SHARED, RAM_PMEM,
    RAM_NORESERVE, RAM_PROTECTED, RAM_NAMED_FILE, RAM_READONLY,
    RAM_READONLY_FD, RAM_GUEST_MEMFD

`int fd`
:   the fd to mmap.

`ram_addr_t offset`
:   offset within the file referenced by fd

`Error **errp`
:   pointer to Error\*, to store an error if it happens.

**Description**

Note that this function does not do anything to cause the data in the
RAM memory region to be migrated; that is the responsibility of the caller.

**Return**

true on success, else false setting **errp** with error.

void memory_region_init_ram_ptr(MemoryRegion \*mr, [Object](qom-api.md#c.Object "Object") \*owner, const char \*name, uint64_t size, void \*ptr)
:   Initialize RAM memory region from a user-provided pointer. Accesses into the region will modify memory directly.

**Parameters**

`MemoryRegion *mr`
:   the `MemoryRegion` to be initialized.

`Object *owner`
:   the object that tracks the region’s reference count

`const char *name`
:   Region name, becomes part of RAMBlock name used in migration stream
    must be unique within any device

`uint64_t size`
:   size of the region.

`void *ptr`
:   memory to be mapped; must contain at least **size** bytes.

**Description**

Note that this function does not do anything to cause the data in the
RAM memory region to be migrated; that is the responsibility of the caller.

void memory_region_init_ram_device_ptr(MemoryRegion \*mr, [Object](qom-api.md#c.Object "Object") \*owner, const char \*name, uint64_t size, void \*ptr)
:   Initialize RAM device memory region from a user-provided pointer.

**Parameters**

`MemoryRegion *mr`
:   the `MemoryRegion` to be initialized.

`Object *owner`
:   the object that tracks the region’s reference count

`const char *name`
:   the name of the region.

`uint64_t size`
:   size of the region.

`void *ptr`
:   memory to be mapped; must contain at least **size** bytes.

**Description**

A RAM device represents a mapping to a physical device, such as to a PCI
MMIO BAR of an vfio-pci assigned device. The memory region may be mapped
into the VM address space and access to the region will modify memory
directly. However, the memory region should not be included in a memory
dump (device may not be enabled/mapped at the time of the dump), and
operations incompatible with manipulating MMIO should be avoided. Replaces
skip_dump flag.

Note that this function does not do anything to cause the data in the
RAM memory region to be migrated; that is the responsibility of the caller.
(For RAM device memory regions, migrating the contents rarely makes sense.)

void memory_region_init_alias(MemoryRegion \*mr, [Object](qom-api.md#c.Object "Object") \*owner, const char \*name, MemoryRegion \*orig, hwaddr offset, uint64_t size)
:   Initialize a memory region that aliases all or a part of another memory region.

**Parameters**

`MemoryRegion *mr`
:   the `MemoryRegion` to be initialized.

`Object *owner`
:   the object that tracks the region’s reference count

`const char *name`
:   used for debugging; not visible to the user or ABI

`MemoryRegion *orig`
:   the region to be referenced; **mr** will be equivalent to
    **orig** between **offset** and **offset** + **size** - 1.

`hwaddr offset`
:   start of the section in **orig** to be referenced.

`uint64_t size`
:   size of the region.

void memory_region_init_iommu(void \*_iommu_mr, size_t instance_size, const char \*mrtypename, [Object](qom-api.md#c.Object "Object") \*owner, const char \*name, uint64_t size)
:   Initialize a memory region of a custom type that translates addresses

**Parameters**

`void *_iommu_mr`
:   the `IOMMUMemoryRegion` to be initialized

`size_t instance_size`
:   the IOMMUMemoryRegion subclass instance size

`const char *mrtypename`
:   the type name of the `IOMMUMemoryRegion`

`Object *owner`
:   the object that tracks the region’s reference count

`const char *name`
:   used for debugging; not visible to the user or ABI

`uint64_t size`
:   size of the region.

**Description**

An IOMMU region translates addresses and forwards accesses to a target
memory region.

The IOMMU implementation must define a subclass of TYPE_IOMMU_MEMORY_REGION.
**_iommu_mr** should be a pointer to enough memory for an instance of
that subclass, **instance_size** is the size of that subclass, and
**mrtypename** is its name. This function will initialize **_iommu_mr** as an
instance of the subclass, and its methods will then be called to handle
accesses to the memory region. See the documentation of
`IOMMUMemoryRegionClass` for further details.

bool memory_region_init_ram(MemoryRegion \*mr, [Object](qom-api.md#c.Object "Object") \*owner, const char \*name, uint64_t size, Error \*\*errp)
:   Initialize RAM memory region. Accesses into the region will modify memory directly.

**Parameters**

`MemoryRegion *mr`
:   the `MemoryRegion` to be initialized

`Object *owner`
:   the object that tracks the region’s reference count (must be
    TYPE_DEVICE or a subclass of TYPE_DEVICE, or NULL)

`const char *name`
:   name of the memory region

`uint64_t size`
:   size of the region in bytes

`Error **errp`
:   pointer to Error\*, to store an error if it happens.

**Description**

This function allocates RAM for a board model or device, and
arranges for it to be migrated (by calling vmstate_register_ram()
if **owner** is a DeviceState, or vmstate_register_ram_global() if
**owner** is NULL).

TODO: Currently we restrict **owner** to being either NULL (for
global RAM regions with no owner) or devices, so that we can
give the RAM block a unique name for migration purposes.
We should lift this restriction and allow arbitrary Objects.
If you pass a non-NULL non-device **owner** then we will assert.

**Return**

true on success, else false setting **errp** with error.

bool memory_region_init_rom(MemoryRegion \*mr, [Object](qom-api.md#c.Object "Object") \*owner, const char \*name, uint64_t size, Error \*\*errp)
:   Initialize a ROM memory region.

**Parameters**

`MemoryRegion *mr`
:   the `MemoryRegion` to be initialized.

`Object *owner`
:   the object that tracks the region’s reference count

`const char *name`
:   Region name, becomes part of RAMBlock name used in migration stream
    must be unique within any device

`uint64_t size`
:   size of the region.

`Error **errp`
:   pointer to Error\*, to store an error if it happens.

**Description**

This has the same effect as calling memory_region_init_ram()
and then marking the resulting region read-only with
memory_region_set_readonly(). This includes arranging for the
contents to be migrated.

TODO: Currently we restrict **owner** to being either NULL (for
global RAM regions with no owner) or devices, so that we can
give the RAM block a unique name for migration purposes.
We should lift this restriction and allow arbitrary Objects.
If you pass a non-NULL non-device **owner** then we will assert.

**Return**

true on success, else false setting **errp** with error.

bool memory_region_init_rom_device(MemoryRegion \*mr, [Object](qom-api.md#c.Object "Object") \*owner, const MemoryRegionOps \*ops, void \*opaque, const char \*name, uint64_t size, Error \*\*errp)
:   Initialize a ROM memory region. Writes are handled via callbacks.

**Parameters**

`MemoryRegion *mr`
:   the `MemoryRegion` to be initialized.

`Object *owner`
:   the object that tracks the region’s reference count

`const MemoryRegionOps *ops`
:   callbacks for write access handling (must not be NULL).

`void *opaque`
:   passed to the read and write callbacks of the **ops** structure.

`const char *name`
:   Region name, becomes part of RAMBlock name used in migration stream
    must be unique within any device

`uint64_t size`
:   size of the region.

`Error **errp`
:   pointer to Error\*, to store an error if it happens.

**Description**

This function initializes a memory region backed by RAM for reads
and callbacks for writes, and arranges for the RAM backing to
be migrated (by calling vmstate_register_ram()
if **owner** is a DeviceState, or vmstate_register_ram_global() if
**owner** is NULL).

TODO: Currently we restrict **owner** to being either NULL (for
global RAM regions with no owner) or devices, so that we can
give the RAM block a unique name for migration purposes.
We should lift this restriction and allow arbitrary Objects.
If you pass a non-NULL non-device **owner** then we will assert.

**Return**

true on success, else false setting **errp** with error.

[Object](qom-api.md#c.Object "Object") \*memory_region_owner(const MemoryRegion \*mr)
:   get a memory region’s owner.

**Parameters**

`const MemoryRegion *mr`
:   the memory region being queried.

uint64_t memory_region_size(const MemoryRegion \*mr)
:   get a memory region’s size.

**Parameters**

`const MemoryRegion *mr`
:   the memory region being queried.

bool memory_region_is_ram(const MemoryRegion \*mr)
:   check whether a memory region is random access

**Parameters**

`const MemoryRegion *mr`
:   the memory region being queried

**Description**

Returns `true` if a memory region is random access.

bool memory_region_is_ram_device(const MemoryRegion \*mr)
:   check whether a memory region is a ram device

**Parameters**

`const MemoryRegion *mr`
:   the memory region being queried

**Description**

Returns `true` if a memory region is a device backed ram region

bool memory_region_is_romd(const MemoryRegion \*mr)
:   check whether a memory region is in ROMD mode

**Parameters**

`const MemoryRegion *mr`
:   the memory region being queried

**Description**

Returns `true` if a memory region is a ROM device and currently set to allow
direct reads.

bool memory_region_is_protected(const MemoryRegion \*mr)
:   check whether a memory region is protected

**Parameters**

`const MemoryRegion *mr`
:   the memory region being queried

**Description**

Returns `true` if a memory region is protected RAM and cannot be accessed
via standard mechanisms, e.g. DMA.

bool memory_region_skip_iommu_map(const MemoryRegion \*mr)
:   check whether a memory region is excluded from IOMMU mapping

**Parameters**

`const MemoryRegion *mr`
:   the memory region being queried

**Description**

Returns `true` if **mr** is a RAM device region marked to skip IOMMU mapping.

void memory_region_set_skip_iommu_map(MemoryRegion \*mr, bool skip)
:   mark a RAM device region to skip IOMMU mapping

**Parameters**

`MemoryRegion *mr`
:   the memory region being modified

`bool skip`
:   `true` to skip IOMMU mapping, `false` to allow it

bool memory_region_has_guest_memfd(const MemoryRegion \*mr)
:   check whether a memory region has guest_memfd associated

**Parameters**

`const MemoryRegion *mr`
:   the memory region being queried

**Description**

Returns `true` if a memory region’s ram_block has valid guest_memfd assigned.

IOMMUMemoryRegion \*memory_region_get_iommu(const MemoryRegion \*mr)
:   check whether a memory region is an iommu

**Parameters**

`const MemoryRegion *mr`
:   the memory region being queried

**Description**

Returns pointer to IOMMUMemoryRegion if a memory region is an iommu,
otherwise NULL.

IOMMUMemoryRegionClass \*memory_region_get_iommu_class_nocheck(IOMMUMemoryRegion \*iommu_mr)
:   returns iommu memory region class if an iommu or NULL if not

**Parameters**

`IOMMUMemoryRegion *iommu_mr`
:   the memory region being queried

**Description**

Returns pointer to IOMMUMemoryRegionClass if a memory region is an iommu,
otherwise NULL. This is fast path avoiding QOM checking, use with caution.

uint64_t memory_region_iommu_get_min_page_size(IOMMUMemoryRegion \*iommu_mr)
:   get minimum supported page size for an iommu

**Parameters**

`IOMMUMemoryRegion *iommu_mr`
:   the memory region being queried

**Description**

Returns minimum supported page size for an iommu.

void memory_region_notify_iommu(IOMMUMemoryRegion \*iommu_mr, int iommu_idx, const IOMMUTLBEvent event)
:   notify a change in an IOMMU translation entry.

**Parameters**

`IOMMUMemoryRegion *iommu_mr`
:   the memory region that was changed

`int iommu_idx`
:   the IOMMU index for the translation table which has changed

`const IOMMUTLBEvent event`
:   TLB event with the new entry in the IOMMU translation table.
    The entry replaces all old entries for the same virtual I/O address
    range.

**Note**

for any IOMMU implementation, an in-place mapping change
should be notified with an UNMAP followed by a MAP.

void memory_region_notify_iommu_one(IOMMUNotifier \*notifier, const IOMMUTLBEvent \*event)
:   notify a change in an IOMMU translation entry to a single notifier

**Parameters**

`IOMMUNotifier *notifier`
:   the notifier to be notified

`const IOMMUTLBEvent *event`
:   TLB event with the new entry in the IOMMU translation table.
    The entry replaces all old entries for the same virtual I/O address
    range.

**Description**

This works just like memory_region_notify_iommu(), but it only
notifies a specific notifier, not all of them.

void memory_region_unmap_iommu_notifier_range(IOMMUNotifier \*notifier)
:   notify a unmap for an IOMMU translation that covers the range of a notifier

**Parameters**

`IOMMUNotifier *notifier`
:   the notifier to be notified

int memory_region_register_iommu_notifier(MemoryRegion \*mr, IOMMUNotifier \*n, Error \*\*errp)
:   register a notifier for changes to IOMMU translation entries.

**Parameters**

`MemoryRegion *mr`
:   the memory region to observe

`IOMMUNotifier *n`
:   the IOMMUNotifier to be added; the notify callback receives a
    pointer to an `IOMMUTLBEntry` as the opaque value; the pointer
    ceases to be valid on exit from the notifier.

`Error **errp`
:   pointer to Error\*, to store an error if it happens.

**Description**

Returns 0 on success, or a negative errno otherwise. In particular,
-EINVAL indicates that at least one of the attributes of the notifier
is not supported (flag/range) by the IOMMU memory region. In case of error
the error object must be created.

void memory_region_iommu_replay(IOMMUMemoryRegion \*iommu_mr, IOMMUNotifier \*n)
:   replay existing IOMMU translations to a notifier with the minimum page granularity returned by mr->iommu_ops->get_page_size().

**Parameters**

`IOMMUMemoryRegion *iommu_mr`
:   the memory region to observe

`IOMMUNotifier *n`
:   the notifier to which to replay iommu mappings

**Note**

this is not related to record-and-replay functionality.

void memory_region_unregister_iommu_notifier(MemoryRegion \*mr, IOMMUNotifier \*n)
:   unregister a notifier for changes to IOMMU translation entries.

**Parameters**

`MemoryRegion *mr`
:   the memory region which was observed and for which notify_stopped()
    needs to be called

`IOMMUNotifier *n`
:   the notifier to be removed.

int memory_region_iommu_get_attr(IOMMUMemoryRegion \*iommu_mr, enum IOMMUMemoryRegionAttr attr, void \*data)
:   return an IOMMU attr if get_attr() is defined on the IOMMU.

**Parameters**

`IOMMUMemoryRegion *iommu_mr`
:   the memory region

`enum IOMMUMemoryRegionAttr attr`
:   the requested attribute

`void *data`
:   a pointer to the requested attribute data

**Description**

Returns 0 on success, or a negative errno otherwise. In particular,
-EINVAL indicates that the IOMMU does not support the requested
attribute.

int memory_region_iommu_attrs_to_index(IOMMUMemoryRegion \*iommu_mr, MemTxAttrs attrs)
:   return the IOMMU index to use for translations with the given memory transaction attributes.

**Parameters**

`IOMMUMemoryRegion *iommu_mr`
:   the memory region

`MemTxAttrs attrs`
:   the memory transaction attributes

int memory_region_iommu_num_indexes(IOMMUMemoryRegion \*iommu_mr)
:   return the total number of IOMMU indexes that this IOMMU supports.

**Parameters**

`IOMMUMemoryRegion *iommu_mr`
:   the memory region

const char \*memory_region_name(const MemoryRegion \*mr)
:   get a memory region’s name

**Parameters**

`const MemoryRegion *mr`
:   the memory region being queried

**Description**

Returns the string that was used to initialize the memory region.

bool memory_region_is_logging(const MemoryRegion \*mr, uint8_t client)
:   return whether a memory region is logging writes

**Parameters**

`const MemoryRegion *mr`
:   the memory region being queried

`uint8_t client`
:   the client being queried

**Description**

Returns `true` if the memory region is logging writes for the given client

uint8_t memory_region_get_dirty_log_mask(const MemoryRegion \*mr)
:   return the clients for which a memory region is logging writes.

**Parameters**

`const MemoryRegion *mr`
:   the memory region being queried

**Description**

Returns a bitmap of clients, in which the DIRTY_MEMORY_\* constants
are the bit indices.

bool memory_region_is_rom(const MemoryRegion \*mr)
:   check whether a memory region is ROM

**Parameters**

`const MemoryRegion *mr`
:   the memory region being queried

**Description**

Returns `true` if a memory region is read-only memory.

bool memory_region_is_nonvolatile(const MemoryRegion \*mr)
:   check whether a memory region is non-volatile

**Parameters**

`const MemoryRegion *mr`
:   the memory region being queried

**Description**

Returns `true` is a memory region is non-volatile memory.

int memory_region_get_fd(const MemoryRegion \*mr)
:   Get a file descriptor backing a RAM memory region.

**Parameters**

`const MemoryRegion *mr`
:   the RAM or alias memory region being queried.

**Description**

Returns a file descriptor backing a file-based RAM memory region,
or -1 if the region is not a file-based RAM memory region.

MemoryRegion \*memory_region_from_host(void \*ptr, ram_addr_t \*offset)
:   Convert a pointer into a RAM memory region and an offset within it.

**Parameters**

`void *ptr`
:   the host pointer to be converted

`ram_addr_t *offset`
:   the offset within memory region

**Description**

Given a host pointer inside a RAM memory region (created with
memory_region_init_ram() or memory_region_init_ram_ptr()), return
the MemoryRegion and the offset within it.

Use with care; by the time this function returns, the returned pointer is
not protected by RCU anymore. If the caller is not within an RCU critical
section and does not hold the BQL, it must have other means of
protecting the pointer, such as a reference to the region that includes
the incoming ram_addr_t.

void \*memory_region_get_ram_ptr(const MemoryRegion \*mr)
:   Get a pointer into a RAM memory region.

**Parameters**

`const MemoryRegion *mr`
:   the memory region being queried.

**Description**

Returns a host pointer to a RAM memory region (created with
memory_region_init_ram() or memory_region_init_ram_ptr()).

Use with care; by the time this function returns, the returned pointer is
not protected by RCU anymore. If the caller is not within an RCU critical
section and does not hold the BQL, it must have other means of
protecting the pointer, such as a reference to the region that includes
the incoming ram_addr_t.

void memory_region_msync(MemoryRegion \*mr, hwaddr addr, hwaddr size)
:   Synchronize selected address range of a memory mapped region

**Parameters**

`MemoryRegion *mr`
:   the memory region to be msync

`hwaddr addr`
:   the initial address of the range to be sync

`hwaddr size`
:   the size of the range to be sync

void memory_region_writeback(MemoryRegion \*mr, hwaddr addr, hwaddr size)
:   Trigger cache writeback for selected address range

**Parameters**

`MemoryRegion *mr`
:   the memory region to be updated

`hwaddr addr`
:   the initial address of the range to be written back

`hwaddr size`
:   the size of the range to be written back

void memory_region_set_log(MemoryRegion \*mr, bool log, unsigned client)
:   Turn dirty logging on or off for a region.

**Parameters**

`MemoryRegion *mr`
:   the memory region being updated.

`bool log`
:   whether dirty logging is to be enabled or disabled.

`unsigned client`
:   the user of the logging information; `DIRTY_MEMORY_VGA` only.

**Description**

Turns dirty logging on or off for a specified client (display, migration).
Only meaningful for RAM regions.

void memory_region_set_dirty(MemoryRegion \*mr, hwaddr addr, hwaddr size)
:   Mark a range of bytes as dirty in a memory region.

**Parameters**

`MemoryRegion *mr`
:   the memory region being dirtied.

`hwaddr addr`
:   the address (relative to the start of the region) being dirtied.

`hwaddr size`
:   size of the range being dirtied.

**Description**

Marks a range of bytes as dirty, after it has been dirtied outside
guest code.

void memory_region_clear_dirty_bitmap(MemoryRegion \*mr, hwaddr start, hwaddr len)
:   clear dirty bitmap for memory range

**Parameters**

`MemoryRegion *mr`
:   the memory region to clear the dirty log upon

`hwaddr start`
:   start address offset within the memory region

`hwaddr len`
:   length of the memory region to clear dirty bitmap

**Description**

This function is called when the caller wants to clear the remote
dirty bitmap of a memory range within the memory region. This can
be used by e.g. KVM to manually clear dirty log when
KVM_CAP_MANUAL_DIRTY_LOG_PROTECT is declared support by the host
kernel.

DirtyBitmapSnapshot \*memory_region_snapshot_and_clear_dirty(MemoryRegion \*mr, hwaddr addr, hwaddr size, unsigned client)
:   Get a snapshot of the dirty bitmap and clear it.

**Parameters**

`MemoryRegion *mr`
:   the memory region being queried.

`hwaddr addr`
:   the address (relative to the start of the region) being queried.

`hwaddr size`
:   the size of the range being queried.

`unsigned client`
:   the user of the logging information; typically `DIRTY_MEMORY_VGA`.

**Description**

Creates a snapshot of the dirty bitmap, clears the dirty bitmap and
returns the snapshot. The snapshot can then be used to query dirty
status, using memory_region_snapshot_get_dirty. Snapshotting allows
querying the same page multiple times, which is especially useful for
display updates where the scanlines often are not page aligned.

The dirty bitmap region which gets copied into the snapshot (and
cleared afterwards) can be larger than requested. The boundaries
are rounded up/down so complete bitmap longs (covering 64 pages on
64bit hosts) can be copied over into the bitmap snapshot. Which
isn’t a problem for display updates as the extra pages are outside
the visible area, and in case the visible area changes a full
display redraw is due anyway. Should other use cases for this
function emerge we might have to revisit this implementation
detail.

Use g_free to release DirtyBitmapSnapshot.

bool memory_region_snapshot_get_dirty(MemoryRegion \*mr, DirtyBitmapSnapshot \*snap, hwaddr addr, hwaddr size)
:   Check whether a range of bytes is dirty in the specified dirty bitmap snapshot.

**Parameters**

`MemoryRegion *mr`
:   the memory region being queried.

`DirtyBitmapSnapshot *snap`
:   the dirty bitmap snapshot

`hwaddr addr`
:   the address (relative to the start of the region) being queried.

`hwaddr size`
:   the size of the range being queried.

void memory_region_reset_dirty(MemoryRegion \*mr, hwaddr addr, hwaddr size, unsigned client)
:   Mark a range of pages as clean, for a specified client.

**Parameters**

`MemoryRegion *mr`
:   the region being updated.

`hwaddr addr`
:   the start of the subrange being cleaned.

`hwaddr size`
:   the size of the subrange being cleaned.

`unsigned client`
:   the user of the logging information; `DIRTY_MEMORY_MIGRATION` or
    `DIRTY_MEMORY_VGA`.

**Description**

Marks a range of pages as no longer dirty.

void memory_region_flush_rom_device(MemoryRegion \*mr, hwaddr addr, hwaddr size)
:   Mark a range of pages dirty and invalidate TBs (for self-modifying code).

**Parameters**

`MemoryRegion *mr`
:   the region being flushed.

`hwaddr addr`
:   the start, relative to the start of the region, of the range being
    flushed.

`hwaddr size`
:   the size, in bytes, of the range being flushed.

**Description**

The MemoryRegionOps->write() callback of a ROM device must use this function
to mark byte ranges that have been modified internally, such as by directly
accessing the memory returned by memory_region_get_ram_ptr().

This function marks the range dirty and invalidates TBs so that TCG can
detect self-modifying code.

void memory_region_set_readonly(MemoryRegion \*mr, bool readonly)
:   Turn a memory region read-only (or read-write)

**Parameters**

`MemoryRegion *mr`
:   the region being updated.

`bool readonly`
:   whether the region is to be ROM or RAM.

**Description**

Allows a memory region to be marked as read-only (turning it into a ROM).
only useful on RAM regions.

void memory_region_set_nonvolatile(MemoryRegion \*mr, bool nonvolatile)
:   Turn a memory region non-volatile

**Parameters**

`MemoryRegion *mr`
:   the region being updated.

`bool nonvolatile`
:   whether the region is to be non-volatile.

**Description**

Allows a memory region to be marked as non-volatile.
only useful on RAM regions.

void memory_region_rom_device_set_romd(MemoryRegion \*mr, bool romd_mode)
:   enable/disable ROMD mode

**Parameters**

`MemoryRegion *mr`
:   the memory region to be updated

`bool romd_mode`
:   `true` to put the region into ROMD mode

**Description**

Allows a ROM device (initialized with memory_region_init_rom_device() to
set to ROMD mode (default) or MMIO mode. When it is in ROMD mode, the
device is mapped to guest memory and satisfies read access directly.
When in MMIO mode, reads are forwarded to the `MemoryRegion.read` function.
Writes are always handled by the `MemoryRegion.write` function.

void memory_region_set_coalescing(MemoryRegion \*mr)
:   Enable memory coalescing for the region.

**Parameters**

`MemoryRegion *mr`
:   the memory region to be write coalesced

**Description**

Enabled writes to a region to be queued for later processing. MMIO ->write
callbacks may be delayed until a non-coalesced MMIO is issued.
Only useful for IO regions. Roughly similar to write-combining hardware.

void memory_region_add_coalescing(MemoryRegion \*mr, hwaddr offset, uint64_t size)
:   Enable memory coalescing for a sub-range of a region.

**Parameters**

`MemoryRegion *mr`
:   the memory region to be updated.

`hwaddr offset`
:   the start of the range within the region to be coalesced.

`uint64_t size`
:   the size of the subrange to be coalesced.

**Description**

Like memory_region_set_coalescing(), but works on a sub-range of a region.
Multiple calls can be issued coalesced disjoint ranges.

void memory_region_clear_coalescing(MemoryRegion \*mr)
:   Disable MMIO coalescing for the region.

**Parameters**

`MemoryRegion *mr`
:   the memory region to be updated.

**Description**

Disables any coalescing caused by memory_region_set_coalescing() or
memory_region_add_coalescing(). Roughly equivalent to uncacheble memory
hardware.

void memory_region_set_flush_coalesced(MemoryRegion \*mr)
:   Enforce memory coalescing flush before accesses.

**Parameters**

`MemoryRegion *mr`
:   the memory region to be updated.

**Description**

Ensure that pending coalesced MMIO request are flushed before the memory
region is accessed. This property is automatically enabled for all regions
passed to memory_region_set_coalescing() and memory_region_add_coalescing().

void memory_region_clear_flush_coalesced(MemoryRegion \*mr)
:   Disable memory coalescing flush before accesses.

**Parameters**

`MemoryRegion *mr`
:   the memory region to be updated.

**Description**

Clear the automatic coalesced MMIO flushing enabled via
memory_region_set_flush_coalesced. Note that this service has no effect on
memory regions that have MMIO coalescing enabled for themselves. For them,
automatic flushing will stop once coalescing is disabled.

void memory_region_enable_lockless_io(MemoryRegion \*mr)
:   Enable lockless (BQL free) acceess.

**Parameters**

`MemoryRegion *mr`
:   the memory region to be updated.

**Description**

Enable BQL-free access for devices that are well prepared to handle
locking during I/O themselves: either by doing fine grained locking or
by providing lock-free I/O schemes.

void memory_region_add_eventfd(MemoryRegion \*mr, hwaddr addr, unsigned size, bool match_data, uint64_t data, EventNotifier \*e)
:   Request an eventfd to be triggered when a word is written to a location.

**Parameters**

`MemoryRegion *mr`
:   the memory region being updated.

`hwaddr addr`
:   the address within **mr** that is to be monitored

`unsigned size`
:   the size of the access to trigger the eventfd

`bool match_data`
:   whether to match against **data**, instead of just **addr**

`uint64_t data`
:   the data to match against the guest write

`EventNotifier *e`
:   event notifier to be triggered when **addr**, **size**, and **data** all match.

**Description**

Marks a word in an IO region (initialized with memory_region_init_io())
as a trigger for an eventfd event. The I/O callback will not be called.
The caller must be prepared to handle failure (that is, take the required
action if the callback _is_ called).

void memory_region_del_eventfd(MemoryRegion \*mr, hwaddr addr, unsigned size, bool match_data, uint64_t data, EventNotifier \*e)
:   Cancel an eventfd.

**Parameters**

`MemoryRegion *mr`
:   the memory region being updated.

`hwaddr addr`
:   the address within **mr** that is to be monitored

`unsigned size`
:   the size of the access to trigger the eventfd

`bool match_data`
:   whether to match against **data**, instead of just **addr**

`uint64_t data`
:   the data to match against the guest write

`EventNotifier *e`
:   event notifier to be triggered when **addr**, **size**, and **data** all match.

**Description**

Cancels an eventfd trigger requested by a previous
memory_region_add_eventfd() call.

void memory_region_add_subregion(MemoryRegion \*mr, hwaddr offset, MemoryRegion \*subregion)
:   Add a subregion to a container.

**Parameters**

`MemoryRegion *mr`
:   the region to contain the new subregion; must be a container
    initialized with memory_region_init().

`hwaddr offset`
:   the offset relative to **mr** where **subregion** is added.

`MemoryRegion *subregion`
:   the subregion to be added.

**Description**

Adds a subregion at **offset**. The subregion may not overlap with other
subregions (except for those explicitly marked as overlapping). A region
may only be added once as a subregion (unless removed with
memory_region_del_subregion()); use memory_region_init_alias() if you
want a region to be a subregion in multiple locations.

void memory_region_add_subregion_overlap(MemoryRegion \*mr, hwaddr offset, MemoryRegion \*subregion, int priority)
:   Add a subregion to a container with overlap.

**Parameters**

`MemoryRegion *mr`
:   the region to contain the new subregion; must be a container
    initialized with memory_region_init().

`hwaddr offset`
:   the offset relative to **mr** where **subregion** is added.

`MemoryRegion *subregion`
:   the subregion to be added.

`int priority`
:   used for resolving overlaps; highest priority wins.

**Description**

Adds a subregion at **offset**. The subregion may overlap with other
subregions. Conflicts are resolved by having a higher **priority** hide a
lower **priority**. Subregions without priority are taken as **priority** 0.
A region may only be added once as a subregion (unless removed with
memory_region_del_subregion()); use memory_region_init_alias() if you
want a region to be a subregion in multiple locations.

ram_addr_t memory_region_get_ram_addr(const MemoryRegion \*mr)
:   Get the ram address associated with a memory region

**Parameters**

`const MemoryRegion *mr`
:   the region to be queried

void memory_region_del_subregion(MemoryRegion \*mr, MemoryRegion \*subregion)
:   Remove a subregion.

**Parameters**

`MemoryRegion *mr`
:   the container to be updated.

`MemoryRegion *subregion`
:   the region being removed; must be a current subregion of **mr**.

**Description**

Removes a subregion from its container.

bool memory_region_present(MemoryRegion \*container, hwaddr addr)
:   checks if an address relative to a **container** translates into `MemoryRegion` within **container**

**Parameters**

`MemoryRegion *container`
:   a `MemoryRegion` within which **addr** is a relative address

`hwaddr addr`
:   the area within **container** to be searched

**Description**

Answer whether a `MemoryRegion` within **container** covers the address
**addr**.

bool memory_region_is_mapped(const MemoryRegion \*mr)
:   returns true if `MemoryRegion` is mapped into another memory region, which does not necessarily imply that it is mapped into an address space.

**Parameters**

`const MemoryRegion *mr`
:   a `MemoryRegion` which should be checked if it’s mapped

RamDiscardManager \*memory_region_get_ram_discard_manager(MemoryRegion \*mr)
:   get the `RamDiscardManager` for a `MemoryRegion`

**Parameters**

`MemoryRegion *mr`
:   the `MemoryRegion`

**Description**

The `RamDiscardManager` cannot change while a memory region is mapped.

bool memory_region_has_ram_discard_manager(MemoryRegion \*mr)
:   check whether a `MemoryRegion` has a `RamDiscardManager` assigned

**Parameters**

`MemoryRegion *mr`
:   the `MemoryRegion`

int memory_region_add_ram_discard_source(MemoryRegion \*mr, RamDiscardSource \*source)
:   add a `RamDiscardSource` for a `MemoryRegion`

**Parameters**

`MemoryRegion *mr`
:   the `MemoryRegion`

`RamDiscardSource *source`
:   `RamDiscardSource` to add

int memory_region_del_ram_discard_source(MemoryRegion \*mr, RamDiscardSource \*source)
:   remove a `RamDiscardSource` for a `MemoryRegion`

**Parameters**

`MemoryRegion *mr`
:   the `MemoryRegion`

`RamDiscardSource *source`
:   `RamDiscardSource` to remove

**Return**

0 on success, or a negative error code on failure.

[MemoryRegionSection](memory.md#c.MemoryRegionSection "MemoryRegionSection") memory_region_find(MemoryRegion \*mr, hwaddr addr, uint64_t size)
:   translate an address/size relative to a MemoryRegion into a [`MemoryRegionSection`](memory.md#c.MemoryRegionSection "MemoryRegionSection").

**Parameters**

`MemoryRegion *mr`
:   a MemoryRegion within which **addr** is a relative address

`hwaddr addr`
:   start of the area within **as** to be searched

`uint64_t size`
:   size of the area to be searched

**Description**

Locates the first `MemoryRegion` within **mr** that overlaps the range
given by **addr** and **size**.

Returns a [`MemoryRegionSection`](memory.md#c.MemoryRegionSection "MemoryRegionSection") that describes a contiguous overlap.
It will have the following characteristics:
- **size** = 0 iff no overlap was found
- **mr** is non-`NULL` iff an overlap was found

Remember that in the return value the **offset_within_region** is
relative to the returned region (in the .\*\*mr\*\* field), not to the
**mr** argument.

Similarly, the .\*\*offset_within_address_space\*\* is relative to the
address space that contains both regions, the passed and the
returned one. However, in the special case where the **mr** argument
has no container (and thus is the root of the address space), the
following will hold:
- **offset_within_address_space** >= **addr**
- **offset_within_address_space** + .\*\*size\*\* <= **addr** + **size**

void memory_global_dirty_log_sync(bool last_stage)
:   synchronize the dirty log for all memory

**Parameters**

`bool last_stage`
:   whether this is the last stage of live migration

**Description**

Synchronizes the dirty page log for all address spaces.

void memory_global_after_dirty_log_sync(void)
:   synchronize the dirty log for all memory

**Parameters**

`void`
:   no arguments

**Description**

Synchronizes the vCPUs with a thread that is reading the dirty bitmap.
This function must be called after the dirty log bitmap is cleared, and
before dirty guest memory pages are read. If you are using
`DirtyBitmapSnapshot`, memory_region_snapshot_and_clear_dirty() takes
care of doing this.

void memory_region_transaction_begin(void)
:   Start a transaction.

**Parameters**

`void`
:   no arguments

**Description**

During a transaction, changes will be accumulated and made visible
only when the transaction ends (is committed).

void memory_region_transaction_commit(void)
:   Commit a transaction and make changes visible to the guest.

**Parameters**

`void`
:   no arguments

void memory_listener_register([MemoryListener](memory.md#c.MemoryListener "MemoryListener") \*listener, [AddressSpace](memory.md#c.AddressSpace "AddressSpace") \*filter)
:   register callbacks to be called when memory sections are mapped or unmapped into an address space

**Parameters**

`MemoryListener *listener`
:   an object containing the callbacks to be called

`AddressSpace *filter`
:   if non-`NULL`, only regions in this address space will be observed

void memory_listener_unregister([MemoryListener](memory.md#c.MemoryListener "MemoryListener") \*listener)
:   undo the effect of memory_listener_register()

**Parameters**

`MemoryListener *listener`
:   an object containing the callbacks to be removed

bool memory_global_dirty_log_start(unsigned int flags, Error \*\*errp)
:   begin dirty logging for all regions

**Parameters**

`unsigned int flags`
:   purpose of starting dirty log, migration or dirty rate

`Error **errp`
:   pointer to Error\*, to store an error if it happens.

**Return**

true on success, else false setting **errp** with error.

void memory_global_dirty_log_stop(unsigned int flags)
:   end dirty logging for all regions

**Parameters**

`unsigned int flags`
:   purpose of stopping dirty log, migration or dirty rate

MemTxResult memory_region_dispatch_read(MemoryRegion \*mr, hwaddr addr, uint64_t \*pval, MemOp op, MemTxAttrs attrs)
:   perform a read directly to the specified MemoryRegion.

**Parameters**

`MemoryRegion *mr`
:   `MemoryRegion` to access

`hwaddr addr`
:   address within that region

`uint64_t *pval`
:   pointer to uint64_t which the data is written to

`MemOp op`
:   size, sign, and endianness of the memory operation

`MemTxAttrs attrs`
:   memory transaction attributes to use for the access

MemTxResult memory_region_dispatch_write(MemoryRegion \*mr, hwaddr addr, uint64_t data, MemOp op, MemTxAttrs attrs)
:   perform a write directly to the specified MemoryRegion.

**Parameters**

`MemoryRegion *mr`
:   `MemoryRegion` to access

`hwaddr addr`
:   address within that region

`uint64_t data`
:   data to write

`MemOp op`
:   size, sign, and endianness of the memory operation

`MemTxAttrs attrs`
:   memory transaction attributes to use for the access

void address_space_init([AddressSpace](memory.md#c.AddressSpace "AddressSpace") \*as, MemoryRegion \*root, const char \*name)
:   initializes an address space

**Parameters**

`AddressSpace *as`
:   an uninitialized [`AddressSpace`](memory.md#c.AddressSpace "AddressSpace")

`MemoryRegion *root`
:   a `MemoryRegion` that routes addresses for the address space

`const char *name`
:   an address space name. The name is only used for debugging
    output.

void address_space_destroy([AddressSpace](memory.md#c.AddressSpace "AddressSpace") \*as)
:   destroy an address space

**Parameters**

`AddressSpace *as`
:   address space to be destroyed

**Description**

Releases all resources associated with an address space. After an
address space is destroyed, the reference the AddressSpace had to
its root memory region is dropped, which may result in the
destruction of that memory region as well.

Note that destruction of the AddressSpace is done via RCU;
it is therefore not valid to free the memory the AddressSpace
struct is in until after that RCU callback has completed.
If you want to g_free() the AddressSpace after destruction you
can do that with address_space_destroy_free().

void address_space_destroy_free([AddressSpace](memory.md#c.AddressSpace "AddressSpace") \*as)
:   destroy an address space and free it

**Parameters**

`AddressSpace *as`
:   address space to be destroyed

**Description**

This does the same thing as address_space_destroy(), and then also
frees (via g_free()) the AddressSpace itself once the destruction
is complete.

void address_space_remove_listeners(const [AddressSpace](memory.md#c.AddressSpace "AddressSpace") \*as)
:   unregister all listeners of an address space

**Parameters**

`const AddressSpace *as`
:   an initialized [`AddressSpace`](memory.md#c.AddressSpace "AddressSpace")

**Description**

Removes all callbacks previously registered with memory_listener_register()
for **as**.

MemTxResult address_space_rw(const [AddressSpace](memory.md#c.AddressSpace "AddressSpace") \*as, hwaddr addr, MemTxAttrs attrs, void \*buf, hwaddr len, bool is_write)
:   read from or write to an address space.

**Parameters**

`const AddressSpace *as`
:   [`AddressSpace`](memory.md#c.AddressSpace "AddressSpace") to be accessed

`hwaddr addr`
:   address within that address space

`MemTxAttrs attrs`
:   memory transaction attributes

`void *buf`
:   buffer with the data transferred

`hwaddr len`
:   the number of bytes to read or write

`bool is_write`
:   indicates the transfer direction

**Description**

Return a MemTxResult indicating whether the operation succeeded
or failed (eg unassigned memory, device rejected the transaction,
IOMMU fault).

MemTxResult address_space_write(const [AddressSpace](memory.md#c.AddressSpace "AddressSpace") \*as, hwaddr addr, MemTxAttrs attrs, const void \*buf, hwaddr len)
:   write to address space.

**Parameters**

`const AddressSpace *as`
:   [`AddressSpace`](memory.md#c.AddressSpace "AddressSpace") to be accessed

`hwaddr addr`
:   address within that address space

`MemTxAttrs attrs`
:   memory transaction attributes

`const void *buf`
:   buffer with the data transferred

`hwaddr len`
:   the number of bytes to write

**Description**

Return a MemTxResult indicating whether the operation succeeded
or failed (eg unassigned memory, device rejected the transaction,
IOMMU fault).

MemTxResult address_space_write_rom([AddressSpace](memory.md#c.AddressSpace "AddressSpace") \*as, hwaddr addr, MemTxAttrs attrs, const void \*buf, hwaddr len)
:   write to address space, including ROM.

**Parameters**

`AddressSpace *as`
:   [`AddressSpace`](memory.md#c.AddressSpace "AddressSpace") to be accessed

`hwaddr addr`
:   address within that address space

`MemTxAttrs attrs`
:   memory transaction attributes

`const void *buf`
:   buffer with the data transferred

`hwaddr len`
:   the number of bytes to write

**Description**

This function writes to the specified address space, but will
write data to both ROM and RAM. This is used for non-guest
writes like writes from the gdb debug stub or initial loading
of ROM contents.

Note that portions of the write which attempt to write data to
a device will be silently ignored – only real RAM and ROM will
be written to.

Return a MemTxResult indicating whether the operation succeeded
or failed (eg unassigned memory, device rejected the transaction,
IOMMU fault).

bool address_space_is_io([AddressSpace](memory.md#c.AddressSpace "AddressSpace") \*as, hwaddr addr)
:   check whether an guest physical addresses whithin an address space is I/O memory.

**Parameters**

`AddressSpace *as`
:   [`AddressSpace`](memory.md#c.AddressSpace "AddressSpace") to be accessed

`hwaddr addr`
:   address within that address space

void qemu_ram_move(void \*dst, const void \*src, size_t n)
:   move data from or to ramblock

**Parameters**

`void *dst`
:   destination where the data is moved to

`const void *src`
:   source where the data is moved from

`size_t n`
:   length of data to be moved

**Description**

Move **n** bytes from **src** to **dst**, the memory areas may overlap. This
provides the same semantics as memmove(), plus an additional stronger
guarantee: if **n** is 1, 2 or 4 or 8 bytes, and **src** and **dst** are both
naturally aligned for that access size, then both the load and the store
will be done as a single atomic access (with the semantics of
qatomic_read() and qatomic_set()).

This is the underlying function that we use to implement accesses by
a guest vCPU or a device DMA operation to a ram block. The atomic
guarantee is needed for two major cases: (A) When the ram block is
backed by a PCI BAR passed through from a host device (and so it might
be hardware registers that must be accessed exactly once at the right
width); (B) When an emulated device updates a data structure shared in
guest memory with guest software (e.g. a network device’s set of tx and
rx descriptor blocks), if a write to memory is accidentally performed
multiple times then it can break the guest code when it busy polls the
guest memory.

We don’t attempt to perform the exact access when it would be unaligned
because this can’t be done on all host architectures. Although this is
strictly speaking not doing what would happen on real hardware, we don’t
think there are going to be situations where that matters in practice.

MemTxResult address_space_read(const [AddressSpace](memory.md#c.AddressSpace "AddressSpace") \*as, hwaddr addr, MemTxAttrs attrs, void \*buf, hwaddr len)
:   read from an address space.

**Parameters**

`const AddressSpace *as`
:   [`AddressSpace`](memory.md#c.AddressSpace "AddressSpace") to be accessed

`hwaddr addr`
:   address within that address space

`MemTxAttrs attrs`
:   memory transaction attributes

`void *buf`
:   buffer with the data transferred

`hwaddr len`
:   length of the data transferred

**Description**

Return a MemTxResult indicating whether the operation succeeded
or failed (eg unassigned memory, device rejected the transaction,
IOMMU fault). Called within RCU critical section.

MemTxResult address_space_set(const [AddressSpace](memory.md#c.AddressSpace "AddressSpace") \*as, hwaddr addr, uint8_t c, hwaddr len, MemTxAttrs attrs)
:   Fill address space with a constant byte.

**Parameters**

`const AddressSpace *as`
:   [`AddressSpace`](memory.md#c.AddressSpace "AddressSpace") to be accessed

`hwaddr addr`
:   address within that address space

`uint8_t c`
:   constant byte to fill the memory

`hwaddr len`
:   the number of bytes to fill with the constant byte

`MemTxAttrs attrs`
:   memory transaction attributes

**Description**

Return a MemTxResult indicating whether the operation succeeded
or failed (eg unassigned memory, device rejected the transaction,
IOMMU fault).
