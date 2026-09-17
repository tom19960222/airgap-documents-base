---
collection: kernel
version: "6.17"
title: "Memory Management"
source_url: https://www.kernel.org/doc/html/v6.17/gpu/xe/xe_mm.html
fetched_at: 2026-09-16T16:30:49+00:00
---
# Memory Management

## BO management

TTM manages (placement, eviction, etc...) all BOs in XE.

## BO creation

Create a chunk of memory which can be used by the GPU. Placement rules
(sysmem or vram region) passed in upon creation. TTM handles placement of BO
and can trigger eviction of other BOs to make space for the new BO.

### Kernel BOs

A kernel BO is created as part of driver load (e.g. uC firmware images, GuC
ADS, etc...) or a BO created as part of a user operation which requires
a kernel BO (e.g. engine state, memory for page tables, etc...). These BOs
are typically mapped in the GGTT (any kernel BOs aside memory for page tables
are in the GGTT), are pinned (can’t move or be evicted at runtime), have a
vmap (XE can access the memory via xe_map layer) and have contiguous physical
memory.

More details of why kernel BOs are pinned and contiguous below.

### User BOs

A user BO is created via the DRM_IOCTL_XE_GEM_CREATE IOCTL. Once it is
created the BO can be mmap’d (via DRM_IOCTL_XE_GEM_MMAP_OFFSET) for user
access and it can be bound for GPU access (via DRM_IOCTL_XE_VM_BIND). All
user BOs are evictable and user BOs are never pinned by XE. The allocation of
the backing store can be deferred from creation time until first use which is
either mmap, bind, or pagefault.

#### Private BOs

A private BO is a user BO created with a valid VM argument passed into the
create IOCTL. If a BO is private it cannot be exported via prime FD and
mappings can only be created for the BO within the VM it is tied to. Lastly,
the BO dma-resv slots / lock point to the VM’s dma-resv slots / lock (all
private BOs to a VM share common dma-resv slots / lock).

#### External BOs

An external BO is a user BO created with a NULL VM argument passed into the
create IOCTL. An external BO can be shared with different UMDs / devices via
prime FD and the BO can be mapped into multiple VMs. An external BO has its
own unique dma-resv slots / lock. An external BO will be in an array of all
VMs which has a mapping of the BO. This allows VMs to lookup and lock all
external BOs mapped in the VM as needed.

#### BO placement

When a user BO is created, a mask of valid placements is passed indicating
which memory regions are considered valid.

The memory region information is available via query uAPI (TODO: add link).

## BO validation

BO validation (ttm_bo_validate) refers to ensuring a BO has a valid
placement. If a BO was swapped to temporary storage, a validation call will
trigger a move back to a valid (location where GPU can access BO) placement.
Validation of a BO may evict other BOs to make room for the BO being
validated.

## BO eviction / moving

All eviction (or in other words, moving a BO from one memory location to
another) is routed through TTM with a callback into XE.

### Runtime eviction

Runtime evictions refers to during normal operations where TTM decides it
needs to move a BO. Typically this is because TTM needs to make room for
another BO and the evicted BO is first BO on LRU list that is not locked.

An example of this is a new BO which can only be placed in VRAM but there is
not space in VRAM. There could be multiple BOs which have sysmem and VRAM
placement rules which currently reside in VRAM, TTM trigger a will move of
one (or multiple) of these BO(s) until there is room in VRAM to place the new
BO. The evicted BO(s) are valid but still need new bindings before the BO
used again (exec or compute mode rebind worker).

Another example would be, TTM can’t find a BO to evict which has another
valid placement. In this case TTM will evict one (or multiple) unlocked BO(s)
to a temporary unreachable (invalid) placement. The evicted BO(s) are invalid
and before next use need to be moved to a valid placement and rebound.

In both cases, moves of these BOs are scheduled behind the fences in the BO’s
dma-resv slots.

WW locking tries to ensures if 2 VMs use 51% of the memory forward progress
is made on both VMs.

Runtime eviction uses per a GT migration engine (TODO: link to migration
engine doc) to do a GPU memcpy from one location to another.

### Rebinds after runtime eviction

When BOs are moved, every mapping (VMA) of the BO needs to rebound before
the BO is used again. Every VMA is added to an evicted list of its VM when
the BO is moved. This is safe because of the VM locking structure (TODO: link
to VM locking doc). On the next use of a VM (exec or compute mode rebind
worker) the evicted VMA list is checked and rebinds are triggered. In the
case of faulting VM, the rebind is done in the page fault handler.

### Suspend / resume eviction of VRAM

During device suspend / resume VRAM may lose power which means the contents
of VRAM’s memory is blown away. Thus BOs present in VRAM at the time of
suspend must be moved to sysmem in order for their contents to be saved.

A simple TTM call (ttm_resource_manager_evict_all) can move all non-pinned
(user) BOs to sysmem. External BOs that are pinned need to be manually
evicted with a simple loop + xe_bo_evict call. It gets a little trickier
with kernel BOs.

Some kernel BOs are used by the GT migration engine to do moves, thus we
can’t move all of the BOs via the GT migration engine. For simplity, use a
TTM memcpy (CPU) to move any kernel (pinned) BO on either suspend or resume.

Some kernel BOs need to be restored to the exact same physical location. TTM
makes this rather easy but the caveat is the memory must be contiguous. Again
for simplity, we enforce that all kernel (pinned) BOs are contiguous and
restored to the same physical location.

Pinned external BOs in VRAM are restored on resume via the GPU.

### Rebinds after suspend / resume

Most kernel BOs have GGTT mappings which must be restored during the resume
process. All user BOs are rebound after validation on their next use.

## Future work

Trim the list of BOs which is saved / restored via TTM memcpy on suspend /
resume. All we really need to save / restore via TTM memcpy is the memory
required for the GuC to load and the memory for the GT migrate engine to
operate.

Do not require kernel BOs to be contiguous in physical memory / restored to
the same physical address on resume. In all likelihood the only memory that
needs to be restored to the same physical address is memory used for page
tables. All of that memory is allocated 1 page at time so the contiguous
requirement isn’t needed. Some work on the vmap code would need to be done if
kernel BOs are not contiguous too.

Make some kernel BO evictable rather than pinned. An example of this would be
engine state, in all likelihood if the dma-slots of these BOs where properly
used rather than pinning we could safely evict + rebind these BOs as needed.

Some kernel BOs do not need to be restored on resume (e.g. GuC ADS as that is
repopulated on resume), add flag to mark such objects as no save / restore.

## GGTT

Xe GGTT implements the support for a Global Virtual Address space that is used
for resources that are accessible to privileged (i.e. kernel-mode) processes,
and not tied to a specific user-level process. For example, the Graphics
micro-Controller (GuC) and Display Engine (if present) utilize this Global
address space.

The Global GTT (GGTT) translates from the Global virtual address to a physical
address that can be accessed by HW. The GGTT is a flat, single-level table.

Xe implements a simplified version of the GGTT specifically managing only a
certain range of it that goes from the Write Once Protected Content Memory (WOPCM)
Layout to a predefined GUC_GGTT_TOP. This approach avoids complications related to
the GuC (Graphics Microcontroller) hardware limitations. The GuC address space
is limited on both ends of the GGTT, because the GuC shim HW redirects
accesses to those addresses to other HW areas instead of going through the
GGTT. On the bottom end, the GuC can’t access offsets below the WOPCM size,
while on the top side the limit is fixed at GUC_GGTT_TOP. To keep things
simple, instead of checking each object to see if they are accessed by GuC or
not, we just exclude those areas from the allocator. Additionally, to simplify
the driver load, we use the maximum WOPCM size in this logic instead of the
programmed one, so we don’t need to wait until the actual size to be
programmed is determined (which requires FW fetch) before initializing the
GGTT. These simplifications might waste space in the GGTT (about 20-25 MBs
depending on the platform) but we can live with this. Another benefit of this
is the GuC bootrom can’t access anything below the WOPCM max size so anything
the bootrom needs to access (e.g. a RSA key) needs to be placed in the GGTT
above the WOPCM max size. Starting the GGTT allocations above the WOPCM max
give us the correct placement for free.

### GGTT Internal API

struct xe_ggtt
:   Main GGTT struct

**Definition**:

```
struct xe_ggtt {
    struct xe_tile *tile;
    u64 size;
#define XE_GGTT_FLAGS_64K BIT(0);
    unsigned int flags;
    struct xe_bo *scratch;
    struct mutex lock;
    u64 __iomem *gsm;
    const struct xe_ggtt_pt_ops *pt_ops;
    struct drm_mm mm;
    unsigned int access_count;
    struct workqueue_struct *wq;
};
```

**Members**

`tile`
:   Back pointer to tile where this GGTT belongs

`size`
:   Total size of this GGTT

`flags`
:   Flags for this GGTT
    Acceptable flags:
    - `XE_GGTT_FLAGS_64K` - if PTE size is 64K. Otherwise, regular is 4K.

`scratch`
:   Internal object allocation used as a scratch page

`lock`
:   Mutex lock to protect GGTT data

`gsm`
:   The iomem pointer to the actual location of the translation
    table located in the GSM for easy PTE manipulation

`pt_ops`
:   Page Table operations per platform

`mm`
:   The memory manager used to manage individual GGTT allocations

`access_count`
:   counts GGTT writes

`wq`
:   Dedicated unordered work queue to process node removals

**Description**

In general, each tile can contains its own Global Graphics Translation Table
(GGTT) instance.

struct xe_ggtt_node
:   A node in GGTT.

**Definition**:

```
struct xe_ggtt_node {
    struct xe_ggtt *ggtt;
    struct drm_mm_node base;
    struct work_struct delayed_removal_work;
    bool invalidate_on_remove;
};
```

**Members**

`ggtt`
:   Back pointer to xe_ggtt where this region will be inserted at

`base`
:   A drm_mm_node

`delayed_removal_work`
:   The work struct for the delayed removal

`invalidate_on_remove`
:   If it needs invalidation upon removal

**Description**

This `struct needs` to be initialized (only-once) with [`xe_ggtt_node_init()`](xe_mm.md#c.xe_ggtt_node_init "xe_ggtt_node_init") before any node
insertion, reservation, or ‘ballooning’.
It will, then, be finalized by either [`xe_ggtt_node_remove()`](xe_mm.md#c.xe_ggtt_node_remove "xe_ggtt_node_remove") or `xe_ggtt_node_deballoon()`.

struct xe_ggtt_pt_ops
:   GGTT Page table operations Which can vary from platform to platform.

**Definition**:

```
struct xe_ggtt_pt_ops {
    u64 (*pte_encode_flags)(struct xe_bo *bo, u16 pat_index);
    void (*ggtt_set_pte)(struct xe_ggtt *ggtt, u64 addr, u64 pte);
};
```

**Members**

`pte_encode_flags`
:   Encode PTE flags for a given BO

`ggtt_set_pte`
:   Directly write into GGTT’s PTE

struct [xe_ggtt](xe_mm.md#c.xe_ggtt "xe_ggtt") \*xe_ggtt_alloc(struct xe_tile \*tile)
:   Allocate a GGTT for a given `xe_tile`

**Parameters**

`struct xe_tile *tile`
:   `xe_tile`

**Description**

Allocates a [`xe_ggtt`](xe_mm.md#c.xe_ggtt "xe_ggtt") for a given tile.

**Return**

[`xe_ggtt`](xe_mm.md#c.xe_ggtt "xe_ggtt") on success, or NULL when out of memory.

int xe_ggtt_init_early(struct [xe_ggtt](xe_mm.md#c.xe_ggtt "xe_ggtt") \*ggtt)
:   Early GGTT initialization

**Parameters**

`struct xe_ggtt *ggtt`
:   the [`xe_ggtt`](xe_mm.md#c.xe_ggtt "xe_ggtt") to be initialized

**Description**

It allows to create new mappings usable by the GuC.
Mappings are not usable by the HW engines, as it doesn’t have scratch nor
initial clear done to it yet. That will happen in the regular, non-early
GGTT initialization.

**Return**

0 on success or a negative error code on failure.

void xe_ggtt_node_remove(struct [xe_ggtt_node](xe_mm.md#c.xe_ggtt_node "xe_ggtt_node") \*node, bool invalidate)
:   Remove a [`xe_ggtt_node`](xe_mm.md#c.xe_ggtt_node "xe_ggtt_node") from the GGTT

**Parameters**

`struct xe_ggtt_node *node`
:   the [`xe_ggtt_node`](xe_mm.md#c.xe_ggtt_node "xe_ggtt_node") to be removed

`bool invalidate`
:   if node needs invalidation upon removal

int xe_ggtt_init(struct [xe_ggtt](xe_mm.md#c.xe_ggtt "xe_ggtt") \*ggtt)
:   Regular non-early GGTT initialization

**Parameters**

`struct xe_ggtt *ggtt`
:   the [`xe_ggtt`](xe_mm.md#c.xe_ggtt "xe_ggtt") to be initialized

**Return**

0 on success or a negative error code on failure.

int xe_ggtt_node_insert_balloon_locked(struct [xe_ggtt_node](xe_mm.md#c.xe_ggtt_node "xe_ggtt_node") \*node, u64 start, u64 end)
:   prevent allocation of specified GGTT addresses

**Parameters**

`struct xe_ggtt_node *node`
:   the [`xe_ggtt_node`](xe_mm.md#c.xe_ggtt_node "xe_ggtt_node") to hold reserved GGTT node

`u64 start`
:   the starting GGTT address of the reserved region

`u64 end`
:   then end GGTT address of the reserved region

**Description**

To be used in cases where ggtt->lock is already taken.
Use [`xe_ggtt_node_remove_balloon_locked()`](xe_mm.md#c.xe_ggtt_node_remove_balloon_locked "xe_ggtt_node_remove_balloon_locked") to release a reserved GGTT node.

**Return**

0 on success or a negative error code on failure.

void xe_ggtt_node_remove_balloon_locked(struct [xe_ggtt_node](xe_mm.md#c.xe_ggtt_node "xe_ggtt_node") \*node)
:   release a reserved GGTT region

**Parameters**

`struct xe_ggtt_node *node`
:   the [`xe_ggtt_node`](xe_mm.md#c.xe_ggtt_node "xe_ggtt_node") with reserved GGTT region

**Description**

To be used in cases where ggtt->lock is already taken.
See [`xe_ggtt_node_insert_balloon_locked()`](xe_mm.md#c.xe_ggtt_node_insert_balloon_locked "xe_ggtt_node_insert_balloon_locked") for details.

void xe_ggtt_shift_nodes_locked(struct [xe_ggtt](xe_mm.md#c.xe_ggtt "xe_ggtt") \*ggtt, s64 shift)
:   Shift GGTT nodes to adjust for a change in usable address range.

**Parameters**

`struct xe_ggtt *ggtt`
:   the [`xe_ggtt`](xe_mm.md#c.xe_ggtt "xe_ggtt") `struct instance`

`s64 shift`
:   change to the location of area provisioned for current VF

**Description**

This function moves all nodes from the GGTT VM, to a temp list. These nodes are expected
to represent allocations in range formerly assigned to current VF, before the range changed.
When the GGTT VM is completely clear of any nodes, they are re-added with shifted offsets.

The function has no ability of failing - because it shifts existing nodes, without
any additional processing. If the nodes were successfully existing at the old address,
they will do the same at the new one. A fail inside this function would indicate that
the list of nodes was either already damaged, or that the shift brings the address range
outside of valid bounds. Both cases justify an assert rather than error code.

int xe_ggtt_node_insert_locked(struct [xe_ggtt_node](xe_mm.md#c.xe_ggtt_node "xe_ggtt_node") \*node, u32 size, u32 align, u32 mm_flags)
:   Locked version to insert a [`xe_ggtt_node`](xe_mm.md#c.xe_ggtt_node "xe_ggtt_node") into the GGTT

**Parameters**

`struct xe_ggtt_node *node`
:   the [`xe_ggtt_node`](xe_mm.md#c.xe_ggtt_node "xe_ggtt_node") to be inserted

`u32 size`
:   size of the node

`u32 align`
:   alignment constrain of the node

`u32 mm_flags`
:   flags to control the node behavior

**Description**

It cannot be called without first having called [`xe_ggtt_init()`](xe_mm.md#c.xe_ggtt_init "xe_ggtt_init") once.
To be used in cases where ggtt->lock is already taken.

**Return**

0 on success or a negative error code on failure.

int xe_ggtt_node_insert(struct [xe_ggtt_node](xe_mm.md#c.xe_ggtt_node "xe_ggtt_node") \*node, u32 size, u32 align)
:   Insert a [`xe_ggtt_node`](xe_mm.md#c.xe_ggtt_node "xe_ggtt_node") into the GGTT

**Parameters**

`struct xe_ggtt_node *node`
:   the [`xe_ggtt_node`](xe_mm.md#c.xe_ggtt_node "xe_ggtt_node") to be inserted

`u32 size`
:   size of the node

`u32 align`
:   alignment constrain of the node

**Description**

It cannot be called without first having called [`xe_ggtt_init()`](xe_mm.md#c.xe_ggtt_init "xe_ggtt_init") once.

**Return**

0 on success or a negative error code on failure.

struct [xe_ggtt_node](xe_mm.md#c.xe_ggtt_node "xe_ggtt_node") \*xe_ggtt_node_init(struct [xe_ggtt](xe_mm.md#c.xe_ggtt "xe_ggtt") \*ggtt)
:   Initialize `xe_ggtt_node` struct

**Parameters**

`struct xe_ggtt *ggtt`
:   the [`xe_ggtt`](xe_mm.md#c.xe_ggtt "xe_ggtt") where the new node will later be inserted/reserved.

**Description**

This function will allocate the struct `xe_ggtt_node` and return its pointer.
This `struct will` then be freed after the node removal upon [`xe_ggtt_node_remove()`](xe_mm.md#c.xe_ggtt_node_remove "xe_ggtt_node_remove")
or [`xe_ggtt_node_remove_balloon_locked()`](xe_mm.md#c.xe_ggtt_node_remove_balloon_locked "xe_ggtt_node_remove_balloon_locked").
Having `xe_ggtt_node` `struct allocated` doesn’t mean that the node is already allocated
in GGTT. Only the [`xe_ggtt_node_insert()`](xe_mm.md#c.xe_ggtt_node_insert "xe_ggtt_node_insert"), [`xe_ggtt_node_insert_locked()`](xe_mm.md#c.xe_ggtt_node_insert_locked "xe_ggtt_node_insert_locked"),
[`xe_ggtt_node_insert_balloon_locked()`](xe_mm.md#c.xe_ggtt_node_insert_balloon_locked "xe_ggtt_node_insert_balloon_locked") will ensure the node is inserted or reserved in GGTT.

**Return**

A pointer to `xe_ggtt_node` `struct on` success. An ERR_PTR otherwise.

void xe_ggtt_node_fini(struct [xe_ggtt_node](xe_mm.md#c.xe_ggtt_node "xe_ggtt_node") \*node)
:   Forcebly finalize `xe_ggtt_node` struct

**Parameters**

`struct xe_ggtt_node *node`
:   the [`xe_ggtt_node`](xe_mm.md#c.xe_ggtt_node "xe_ggtt_node") to be freed

**Description**

If anything went wrong with either [`xe_ggtt_node_insert()`](xe_mm.md#c.xe_ggtt_node_insert "xe_ggtt_node_insert"), [`xe_ggtt_node_insert_locked()`](xe_mm.md#c.xe_ggtt_node_insert_locked "xe_ggtt_node_insert_locked"),
or [`xe_ggtt_node_insert_balloon_locked()`](xe_mm.md#c.xe_ggtt_node_insert_balloon_locked "xe_ggtt_node_insert_balloon_locked"); and this **node** is not going to be reused, then,
this function needs to be called to free the `xe_ggtt_node` struct

bool xe_ggtt_node_allocated(const struct [xe_ggtt_node](xe_mm.md#c.xe_ggtt_node "xe_ggtt_node") \*node)
:   Check if node is allocated in GGTT

**Parameters**

`const struct xe_ggtt_node *node`
:   the [`xe_ggtt_node`](xe_mm.md#c.xe_ggtt_node "xe_ggtt_node") to be inspected

**Return**

True if allocated, False otherwise.

void xe_ggtt_map_bo(struct [xe_ggtt](xe_mm.md#c.xe_ggtt "xe_ggtt") \*ggtt, struct [xe_ggtt_node](xe_mm.md#c.xe_ggtt_node "xe_ggtt_node") \*node, struct xe_bo \*bo, u16 pat_index)
:   Map the BO into GGTT

**Parameters**

`struct xe_ggtt *ggtt`
:   the [`xe_ggtt`](xe_mm.md#c.xe_ggtt "xe_ggtt") where node will be mapped

`struct xe_ggtt_node *node`
:   the [`xe_ggtt_node`](xe_mm.md#c.xe_ggtt_node "xe_ggtt_node") where this BO is mapped

`struct xe_bo *bo`
:   the `xe_bo` to be mapped

`u16 pat_index`
:   Which pat_index to use.

void xe_ggtt_map_bo_unlocked(struct [xe_ggtt](xe_mm.md#c.xe_ggtt "xe_ggtt") \*ggtt, struct xe_bo \*bo)
:   Restore a mapping of a BO into GGTT

**Parameters**

`struct xe_ggtt *ggtt`
:   the [`xe_ggtt`](xe_mm.md#c.xe_ggtt "xe_ggtt") where node will be mapped

`struct xe_bo *bo`
:   the `xe_bo` to be mapped

**Description**

This is used to restore a GGTT mapping after suspend.

int xe_ggtt_insert_bo_at(struct [xe_ggtt](xe_mm.md#c.xe_ggtt "xe_ggtt") \*ggtt, struct xe_bo \*bo, u64 start, u64 end)
:   Insert BO at a specific GGTT space

**Parameters**

`struct xe_ggtt *ggtt`
:   the [`xe_ggtt`](xe_mm.md#c.xe_ggtt "xe_ggtt") where bo will be inserted

`struct xe_bo *bo`
:   the `xe_bo` to be inserted

`u64 start`
:   address where it will be inserted

`u64 end`
:   end of the range where it will be inserted

**Return**

0 on success or a negative error code on failure.

int xe_ggtt_insert_bo(struct [xe_ggtt](xe_mm.md#c.xe_ggtt "xe_ggtt") \*ggtt, struct xe_bo \*bo)
:   Insert BO into GGTT

**Parameters**

`struct xe_ggtt *ggtt`
:   the [`xe_ggtt`](xe_mm.md#c.xe_ggtt "xe_ggtt") where bo will be inserted

`struct xe_bo *bo`
:   the `xe_bo` to be inserted

**Return**

0 on success or a negative error code on failure.

void xe_ggtt_remove_bo(struct [xe_ggtt](xe_mm.md#c.xe_ggtt "xe_ggtt") \*ggtt, struct xe_bo \*bo)
:   Remove a BO from the GGTT

**Parameters**

`struct xe_ggtt *ggtt`
:   the [`xe_ggtt`](xe_mm.md#c.xe_ggtt "xe_ggtt") where node will be removed

`struct xe_bo *bo`
:   the `xe_bo` to be removed

u64 xe_ggtt_largest_hole(struct [xe_ggtt](xe_mm.md#c.xe_ggtt "xe_ggtt") \*ggtt, u64 alignment, u64 \*spare)
:   Largest GGTT hole

**Parameters**

`struct xe_ggtt *ggtt`
:   the [`xe_ggtt`](xe_mm.md#c.xe_ggtt "xe_ggtt") that will be inspected

`u64 alignment`
:   minimum alignment

`u64 *spare`
:   If not NULL: in: desired memory size to be spared / out: Adjusted possible spare

**Return**

size of the largest continuous GGTT region

void xe_ggtt_assign(const struct [xe_ggtt_node](xe_mm.md#c.xe_ggtt_node "xe_ggtt_node") \*node, u16 vfid)
:   assign a GGTT region to the VF

**Parameters**

`const struct xe_ggtt_node *node`
:   the [`xe_ggtt_node`](xe_mm.md#c.xe_ggtt_node "xe_ggtt_node") to update

`u16 vfid`
:   the VF identifier

**Description**

This function is used by the PF driver to assign a GGTT region to the VF.
In addition to PTE’s VFID bits 11:2 also PRESENT bit 0 is set as on some
platforms VFs can’t modify that either.

int xe_ggtt_dump(struct [xe_ggtt](xe_mm.md#c.xe_ggtt "xe_ggtt") \*ggtt, struct [drm_printer](../drm-internals.md#c.drm_printer "drm_printer") \*p)
:   Dump GGTT for debug

**Parameters**

`struct xe_ggtt *ggtt`
:   the [`xe_ggtt`](xe_mm.md#c.xe_ggtt "xe_ggtt") to be dumped

`struct drm_printer *p`
:   the `drm_mm_printer` helper handle to be used to dump the information

**Return**

0 on success or a negative error code on failure.

u64 xe_ggtt_print_holes(struct [xe_ggtt](xe_mm.md#c.xe_ggtt "xe_ggtt") \*ggtt, u64 alignment, struct [drm_printer](../drm-internals.md#c.drm_printer "drm_printer") \*p)
:   Print holes

**Parameters**

`struct xe_ggtt *ggtt`
:   the [`xe_ggtt`](xe_mm.md#c.xe_ggtt "xe_ggtt") to be inspected

`u64 alignment`
:   min alignment

`struct drm_printer *p`
:   the [`drm_printer`](../drm-internals.md#c.drm_printer "drm_printer")

**Description**

Print GGTT ranges that are available and return total size available.

**Return**

Total available size.

u64 xe_ggtt_encode_pte_flags(struct [xe_ggtt](xe_mm.md#c.xe_ggtt "xe_ggtt") \*ggtt, struct xe_bo \*bo, u16 pat_index)
:   Get PTE encoding flags for BO

**Parameters**

`struct xe_ggtt *ggtt`
:   [`xe_ggtt`](xe_mm.md#c.xe_ggtt "xe_ggtt")

`struct xe_bo *bo`
:   `xe_bo`

`u16 pat_index`
:   The pat_index for the PTE.

**Description**

This function returns the pte_flags for a given BO, without address.
It’s used for DPT to fill a GGTT mapped BO with a linear lookup table.

u64 xe_ggtt_read_pte(struct [xe_ggtt](xe_mm.md#c.xe_ggtt "xe_ggtt") \*ggtt, u64 offset)
:   Read a PTE from the GGTT

**Parameters**

`struct xe_ggtt *ggtt`
:   [`xe_ggtt`](xe_mm.md#c.xe_ggtt "xe_ggtt")

`u64 offset`
:   the offset for which the mapping should be read.

**Description**

Used by testcases, and by display reading out an inherited bios FB.

## Pagetable building

Below we use the term “page-table” for both page-directories, containing
pointers to lower level page-directories or page-tables, and level 0
page-tables that contain only page-table-entries pointing to memory pages.

When inserting an address range in an already existing page-table tree
there will typically be a set of page-tables that are shared with other
address ranges, and a set that are private to this address range.
The set of shared page-tables can be at most two per level,
and those can’t be updated immediately because the entries of those
page-tables may still be in use by the gpu for other mappings. Therefore
when inserting entries into those, we instead stage those insertions by
adding insertion data into `struct xe_vm_pgtable_update` structures. This
data, (subtrees for the cpu and page-table-entries for the gpu) is then
added in a separate commit step. CPU-data is committed while still under the
vm lock, the object lock and for userptr, the notifier lock in read mode.
The GPU async data is committed either by the GPU or CPU after fulfilling
relevant dependencies.
For non-shared page-tables (and, in fact, for shared ones that aren’t
existing at the time of staging), we add the data in-place without the
special update structures. This private part of the page-table tree will
remain disconnected from the vm page-table tree until data is committed to
the shared page tables of the vm tree in the commit phase.
