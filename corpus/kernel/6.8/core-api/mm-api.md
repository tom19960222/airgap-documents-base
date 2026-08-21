---
collection: kernel
version: "6.8"
title: "Memory Management APIs"
source_url: https://www.kernel.org/doc/html/v6.8/core-api/mm-api.html
fetched_at: 2026-08-21T03:30:17+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/core-api/mm-api.md)

# Memory Management APIs

## User Space Memory Access

get_user

`get_user (x, ptr)`

> Get a simple variable from user space.

**Parameters**

`x`
:   Variable to store result.

`ptr`
:   Source address, in user space.

**Context**

User context only. This function may sleep if pagefaults are
enabled.

**Description**

This macro copies a single simple variable from user space to kernel
space. It supports simple types like char and int, but not larger
data types like structures or arrays.

**ptr** must have pointer-to-simple-variable type, and the result of
dereferencing **ptr** must be assignable to **x** without a cast.

**Return**

zero on success, or -EFAULT on error.
On error, the variable **x** is set to zero.

__get_user

`__get_user (x, ptr)`

> Get a simple variable from user space, with less checking.

**Parameters**

`x`
:   Variable to store result.

`ptr`
:   Source address, in user space.

**Context**

User context only. This function may sleep if pagefaults are
enabled.

**Description**

This macro copies a single simple variable from user space to kernel
space. It supports simple types like char and int, but not larger
data types like structures or arrays.

**ptr** must have pointer-to-simple-variable type, and the result of
dereferencing **ptr** must be assignable to **x** without a cast.

Caller must check the pointer with access_ok() before calling this
function.

**Return**

zero on success, or -EFAULT on error.
On error, the variable **x** is set to zero.

put_user

`put_user (x, ptr)`

> Write a simple value into user space.

**Parameters**

`x`
:   Value to copy to user space.

`ptr`
:   Destination address, in user space.

**Context**

User context only. This function may sleep if pagefaults are
enabled.

**Description**

This macro copies a single simple value from kernel space to user
space. It supports simple types like char and int, but not larger
data types like structures or arrays.

**ptr** must have pointer-to-simple-variable type, and **x** must be assignable
to the result of dereferencing **ptr**.

**Return**

zero on success, or -EFAULT on error.

__put_user

`__put_user (x, ptr)`

> Write a simple value into user space, with less checking.

**Parameters**

`x`
:   Value to copy to user space.

`ptr`
:   Destination address, in user space.

**Context**

User context only. This function may sleep if pagefaults are
enabled.

**Description**

This macro copies a single simple value from kernel space to user
space. It supports simple types like char and int, but not larger
data types like structures or arrays.

**ptr** must have pointer-to-simple-variable type, and **x** must be assignable
to the result of dereferencing **ptr**.

Caller must check the pointer with access_ok() before calling this
function.

**Return**

zero on success, or -EFAULT on error.

unsigned long clear_user(void __user \*to, unsigned long n)
:   Zero a block of memory in user space.

**Parameters**

`void __user *to`
:   Destination address, in user space.

`unsigned long n`
:   Number of bytes to zero.

**Description**

Zero a block of memory in user space.

**Return**

number of bytes that could not be cleared.
On success, this will be zero.

unsigned long __clear_user(void __user \*to, unsigned long n)
:   Zero a block of memory in user space, with less checking.

**Parameters**

`void __user *to`
:   Destination address, in user space.

`unsigned long n`
:   Number of bytes to zero.

**Description**

Zero a block of memory in user space. Caller must check
the specified block with access_ok() before calling this function.

**Return**

number of bytes that could not be cleared.
On success, this will be zero.

int get_user_pages_fast(unsigned long start, int nr_pages, unsigned int gup_flags, struct page \*\*pages)
:   pin user pages in memory

**Parameters**

`unsigned long start`
:   starting user address

`int nr_pages`
:   number of pages from start to pin

`unsigned int gup_flags`
:   flags modifying pin behaviour

`struct page **pages`
:   array that receives pointers to the pages pinned.
    Should be at least nr_pages long.

**Description**

Attempt to pin user pages in memory without taking mm->mmap_lock.
If not successful, it will fall back to taking the lock and
calling get_user_pages().

Returns number of pages pinned. This may be fewer than the number requested.
If nr_pages is 0 or negative, returns 0. If no pages were pinned, returns
-errno.

## Memory Allocation Controls

### Page mobility and placement hints

These flags provide hints about how mobile the page is. Pages with similar
mobility are placed within the same pageblocks to minimise problems due
to external fragmentation.

`__GFP_MOVABLE` (also a zone modifier) indicates that the page can be
moved by page migration during memory compaction or can be reclaimed.

`__GFP_RECLAIMABLE` is used for slab allocations that specify
SLAB_RECLAIM_ACCOUNT and whose pages can be freed via shrinkers.

`__GFP_WRITE` indicates the caller intends to dirty the page. Where possible,
these pages will be spread between local zones to avoid all the dirty
pages being in one zone (fair zone allocation policy).

`__GFP_HARDWALL` enforces the cpuset memory allocation policy.

`__GFP_THISNODE` forces the allocation to be satisfied from the requested
node with no fallbacks or placement policy enforcements.

`__GFP_ACCOUNT` causes the allocation to be accounted to kmemcg.

### Watermark modifiers -- controls access to emergency reserves

`__GFP_HIGH` indicates that the caller is high-priority and that granting
the request is necessary before the system can make forward progress.
For example creating an IO context to clean pages and requests
from atomic context.

`__GFP_MEMALLOC` allows access to all memory. This should only be used when
the caller guarantees the allocation will allow more memory to be freed
very shortly e.g. process exiting or swapping. Users either should
be the MM or co-ordinating closely with the VM (e.g. swap over NFS).
Users of this flag have to be extremely careful to not deplete the reserve
completely and implement a throttling mechanism which controls the
consumption of the reserve based on the amount of freed memory.
Usage of a pre-allocated pool (e.g. mempool) should be always considered
before using this flag.

`__GFP_NOMEMALLOC` is used to explicitly forbid access to emergency reserves.
This takes precedence over the `__GFP_MEMALLOC` flag if both are set.

### Reclaim modifiers

Please note that all the following flags are only applicable to sleepable
allocations (e.g. `GFP_NOWAIT` and `GFP_ATOMIC` will ignore them).

`__GFP_IO` can start physical IO.

`__GFP_FS` can call down to the low-level FS. Clearing the flag avoids the
allocator recursing into the filesystem which might already be holding
locks.

`__GFP_DIRECT_RECLAIM` indicates that the caller may enter direct reclaim.
This flag can be cleared to avoid unnecessary delays when a fallback
option is available.

`__GFP_KSWAPD_RECLAIM` indicates that the caller wants to wake kswapd when
the low watermark is reached and have it reclaim pages until the high
watermark is reached. A caller may wish to clear this flag when fallback
options are available and the reclaim is likely to disrupt the system. The
canonical example is THP allocation where a fallback is cheap but
reclaim/compaction may cause indirect stalls.

`__GFP_RECLAIM` is shorthand to allow/forbid both direct and kswapd reclaim.

The default allocator behavior depends on the request size. We have a concept
of so-called costly allocations (with order > `PAGE_ALLOC_COSTLY_ORDER`).
!costly allocations are too essential to fail so they are implicitly
non-failing by default (with some exceptions like OOM victims might fail so
the caller still has to check for failures) while costly requests try to be
not disruptive and back off even without invoking the OOM killer.
The following three modifiers might be used to override some of these
implicit rules.

`__GFP_NORETRY`: The VM implementation will try only very lightweight
memory direct reclaim to get some memory under memory pressure (thus
it can sleep). It will avoid disruptive actions like OOM killer. The
caller must handle the failure which is quite likely to happen under
heavy memory pressure. The flag is suitable when failure can easily be
handled at small cost, such as reduced throughput.

`__GFP_RETRY_MAYFAIL`: The VM implementation will retry memory reclaim
procedures that have previously failed if there is some indication
that progress has been made elsewhere. It can wait for other
tasks to attempt high-level approaches to freeing memory such as
compaction (which removes fragmentation) and page-out.
There is still a definite limit to the number of retries, but it is
a larger limit than with `__GFP_NORETRY`.
Allocations with this flag may fail, but only when there is
genuinely little unused memory. While these allocations do not
directly trigger the OOM killer, their failure indicates that
the system is likely to need to use the OOM killer soon. The
caller must handle failure, but can reasonably do so by failing
a higher-level request, or completing it only in a much less
efficient manner.
If the allocation does fail, and the caller is in a position to
free some non-essential memory, doing so could benefit the system
as a whole.

`__GFP_NOFAIL`: The VM implementation _must_ retry infinitely: the caller
cannot handle allocation failures. The allocation could block
indefinitely but will never return with failure. Testing for
failure is pointless.
New users should be evaluated carefully (and the flag should be
used only when there is no reasonable failure policy) but it is
definitely preferable to use the flag rather than opencode endless
loop around allocator.
Using this flag for costly allocations is _highly_ discouraged.

### Useful GFP flag combinations

Useful GFP flag combinations that are commonly used. It is recommended
that subsystems start with one of these combinations and then set/clear
`__GFP_FOO` flags as necessary.

`GFP_ATOMIC` users can not sleep and need the allocation to succeed. A lower
watermark is applied to allow access to "atomic reserves".
The current implementation doesn't support NMI and few other strict
non-preemptive contexts (e.g. raw_spin_lock). The same applies to `GFP_NOWAIT`.

`GFP_KERNEL` is typical for kernel-internal allocations. The caller requires
`ZONE_NORMAL` or a lower zone for direct access but can direct reclaim.

`GFP_KERNEL_ACCOUNT` is the same as GFP_KERNEL, except the allocation is
accounted to kmemcg.

`GFP_NOWAIT` is for kernel allocations that should not stall for direct
reclaim, start physical IO or use any filesystem callback. It is very
likely to fail to allocate memory, even for very small allocations.

`GFP_NOIO` will use direct reclaim to discard clean pages or slab pages
that do not require the starting of any physical IO.
Please try to avoid using this flag directly and instead use
memalloc_noio_{save,restore} to mark the whole scope which cannot
perform any IO with a short explanation why. All allocation requests
will inherit GFP_NOIO implicitly.

`GFP_NOFS` will use direct reclaim but will not use any filesystem interfaces.
Please try to avoid using this flag directly and instead use
memalloc_nofs_{save,restore} to mark the whole scope which cannot/shouldn't
recurse into the FS layer with a short explanation why. All allocation
requests will inherit GFP_NOFS implicitly.

`GFP_USER` is for userspace allocations that also need to be directly
accessibly by the kernel or hardware. It is typically used by hardware
for buffers that are mapped to userspace (e.g. graphics) that hardware
still must DMA to. cpuset limits are enforced for these allocations.

`GFP_DMA` exists for historical reasons and should be avoided where possible.
The flags indicates that the caller requires that the lowest zone be
used (`ZONE_DMA` or 16M on x86-64). Ideally, this would be removed but
it would require careful auditing as some users really require it and
others use the flag to avoid lowmem reserves in `ZONE_DMA` and treat the
lowest zone as a type of emergency reserve.

`GFP_DMA32` is similar to `GFP_DMA` except that the caller requires a 32-bit
address. Note that kmalloc(..., GFP_DMA32) does not return DMA32 memory
because the DMA32 kmalloc cache array is not implemented.
(Reason: there is no such user in kernel).

`GFP_HIGHUSER` is for userspace allocations that may be mapped to userspace,
do not need to be directly accessible by the kernel but that cannot
move once in use. An example may be a hardware allocation that maps
data directly into userspace but has no addressing limitations.

`GFP_HIGHUSER_MOVABLE` is for userspace allocations that the kernel does not
need direct access to but can use [`kmap()`](../mm/highmem.md#c.kmap "kmap") when access is required. They
are expected to be movable via page reclaim or page migration. Typically,
pages on the LRU would also be allocated with `GFP_HIGHUSER_MOVABLE`.

`GFP_TRANSHUGE` and `GFP_TRANSHUGE_LIGHT` are used for THP allocations. They
are compound allocations that will generally fail quickly if memory is not
available and will not wake kswapd/kcompactd on failure. The _LIGHT
version does not attempt reclaim/compaction at all and is by default used
in page fault path, while the non-light is used by khugepaged.

## The Slab Cache

size_t ksize(const void \*objp)
:   Report actual allocation size of associated object

**Parameters**

`const void *objp`
:   Pointer returned from a prior [`kmalloc()`](mm-api.md#c.kmalloc "kmalloc")-family allocation.

**Description**

This should not be used for writing beyond the originally requested
allocation size. Either use [`krealloc()`](mm-api.md#c.krealloc "krealloc") or round up the allocation size
with [`kmalloc_size_roundup()`](mm-api.md#c.kmalloc_size_roundup "kmalloc_size_roundup") prior to allocation. If this is used to
access beyond the originally requested allocation size, UBSAN_BOUNDS
and/or FORTIFY_SOURCE may trip, since they only know about the
originally allocated size via the __alloc_size attribute.

void \*kmem_cache_alloc(struct kmem_cache \*cachep, gfp_t flags)
:   Allocate an object

**Parameters**

`struct kmem_cache *cachep`
:   The cache to allocate from.

`gfp_t flags`
:   See [`kmalloc()`](mm-api.md#c.kmalloc "kmalloc").

**Description**

Allocate an object from this cache.
See kmem_cache_zalloc() for a shortcut of adding __GFP_ZERO to flags.

**Return**

pointer to the new object or `NULL` in case of error

void \*kmalloc(size_t size, gfp_t flags)
:   allocate kernel memory

**Parameters**

`size_t size`
:   how many bytes of memory are required.

`gfp_t flags`
:   describe the allocation context

**Description**

kmalloc is the normal method of allocating memory
for objects smaller than page size in the kernel.

The allocated object address is aligned to at least ARCH_KMALLOC_MINALIGN
bytes. For **size** of power of two bytes, the alignment is also guaranteed
to be at least to the size.

The **flags** argument may be one of the GFP flags defined at
include/linux/gfp_types.h and described at
[Documentation/core-api/mm-api.rst](mm-api.md#mm-api-gfp-flags)

The recommended usage of the **flags** is described at
[Documentation/core-api/memory-allocation.rst](memory-allocation.md#memory-allocation)

Below is a brief outline of the most useful GFP flags

`GFP_KERNEL`
:   Allocate normal kernel ram. May sleep.

`GFP_NOWAIT`
:   Allocation will not sleep.

`GFP_ATOMIC`
:   Allocation will not sleep. May use emergency pools.

Also it is possible to set different flags by OR'ing
in one or more of the following additional **flags**:

`__GFP_ZERO`
:   Zero the allocated memory before returning. Also see [`kzalloc()`](mm-api.md#c.kzalloc "kzalloc").

`__GFP_HIGH`
:   This allocation has high priority and may use emergency pools.

`__GFP_NOFAIL`
:   Indicate that this allocation is in no way allowed to fail
    (think twice before using).

`__GFP_NORETRY`
:   If memory is not immediately available,
    then give up at once.

`__GFP_NOWARN`
:   If allocation fails, don't issue any warnings.

`__GFP_RETRY_MAYFAIL`
:   Try really hard to succeed the allocation but fail
    eventually.

void \*kmalloc_array(size_t n, size_t size, gfp_t flags)
:   allocate memory for an array.

**Parameters**

`size_t n`
:   number of elements.

`size_t size`
:   element size.

`gfp_t flags`
:   the type of memory to allocate (see kmalloc).

void \*krealloc_array(void \*p, size_t new_n, size_t new_size, gfp_t flags)
:   reallocate memory for an array.

**Parameters**

`void *p`
:   pointer to the memory chunk to reallocate

`size_t new_n`
:   new number of elements to alloc

`size_t new_size`
:   new size of a single member of the array

`gfp_t flags`
:   the type of memory to allocate (see kmalloc)

void \*kcalloc(size_t n, size_t size, gfp_t flags)
:   allocate memory for an array. The memory is set to zero.

**Parameters**

`size_t n`
:   number of elements.

`size_t size`
:   element size.

`gfp_t flags`
:   the type of memory to allocate (see kmalloc).

void \*kzalloc(size_t size, gfp_t flags)
:   allocate memory. The memory is set to zero.

**Parameters**

`size_t size`
:   how many bytes of memory are required.

`gfp_t flags`
:   the type of memory to allocate (see kmalloc).

void \*kzalloc_node(size_t size, gfp_t flags, int node)
:   allocate zeroed memory from a particular memory node.

**Parameters**

`size_t size`
:   how many bytes of memory are required.

`gfp_t flags`
:   the type of memory to allocate (see kmalloc).

`int node`
:   memory node from which to allocate

size_t kmalloc_size_roundup(size_t size)
:   Report allocation bucket size for the given size

**Parameters**

`size_t size`
:   Number of bytes to round up from.

**Description**

This returns the number of bytes that would be available in a [`kmalloc()`](mm-api.md#c.kmalloc "kmalloc")
allocation of **size** bytes. For example, a 126 byte request would be
rounded up to the next sized kmalloc bucket, 128 bytes. (This is strictly
for the general-purpose [`kmalloc()`](mm-api.md#c.kmalloc "kmalloc")-based allocations, and is not for the
pre-sized [`kmem_cache_alloc()`](mm-api.md#c.kmem_cache_alloc "kmem_cache_alloc")-based allocations.)

Use this to [`kmalloc()`](mm-api.md#c.kmalloc "kmalloc") the full bucket size ahead of time instead of using
[`ksize()`](mm-api.md#c.ksize "ksize") to query the size after an allocation.

void \*kmem_cache_alloc_node(struct kmem_cache \*s, gfp_t gfpflags, int node)
:   Allocate an object on the specified node

**Parameters**

`struct kmem_cache *s`
:   The cache to allocate from.

`gfp_t gfpflags`
:   See [`kmalloc()`](mm-api.md#c.kmalloc "kmalloc").

`int node`
:   node number of the target node.

**Description**

Identical to kmem_cache_alloc but it will allocate memory on the given
node, which can improve the performance for cpu bound structures.

Fallback to other node is possible if __GFP_THISNODE is not set.

**Return**

pointer to the new object or `NULL` in case of error

void kmem_cache_free(struct kmem_cache \*s, void \*x)
:   Deallocate an object

**Parameters**

`struct kmem_cache *s`
:   The cache the allocation was from.

`void *x`
:   The previously allocated object.

**Description**

Free an object which was previously allocated from this
cache.

void kfree(const void \*object)
:   free previously allocated memory

**Parameters**

`const void *object`
:   pointer returned by [`kmalloc()`](mm-api.md#c.kmalloc "kmalloc") or [`kmem_cache_alloc()`](mm-api.md#c.kmem_cache_alloc "kmem_cache_alloc")

**Description**

If **object** is NULL, no operation is performed.

struct kmem_cache \*kmem_cache_create_usercopy(const char \*name, unsigned int size, unsigned int align, slab_flags_t flags, unsigned int useroffset, unsigned int usersize, void (\*ctor)(void\*))
:   Create a cache with a region suitable for copying to userspace

**Parameters**

`const char *name`
:   A string which is used in /proc/slabinfo to identify this cache.

`unsigned int size`
:   The size of objects to be created in this cache.

`unsigned int align`
:   The required alignment for the objects.

`slab_flags_t flags`
:   SLAB flags

`unsigned int useroffset`
:   Usercopy region offset

`unsigned int usersize`
:   Usercopy region size

`void (*ctor)(void *)`
:   A constructor for the objects.

**Description**

Cannot be called within a interrupt, but can be interrupted.
The **ctor** is run when new pages are allocated by the cache.

The flags are

`SLAB_POISON` - Poison the slab with a known test pattern (a5a5a5a5)
to catch references to uninitialised memory.

`SLAB_RED_ZONE` - Insert Red zones around the allocated memory to check
for buffer overruns.

`SLAB_HWCACHE_ALIGN` - Align the objects in this cache to a hardware
cacheline. This can be beneficial if you're counting cycles as closely
as davem.

**Return**

a pointer to the cache on success, NULL on failure.

struct kmem_cache \*kmem_cache_create(const char \*name, unsigned int size, unsigned int align, slab_flags_t flags, void (\*ctor)(void\*))
:   Create a cache.

**Parameters**

`const char *name`
:   A string which is used in /proc/slabinfo to identify this cache.

`unsigned int size`
:   The size of objects to be created in this cache.

`unsigned int align`
:   The required alignment for the objects.

`slab_flags_t flags`
:   SLAB flags

`void (*ctor)(void *)`
:   A constructor for the objects.

**Description**

Cannot be called within a interrupt, but can be interrupted.
The **ctor** is run when new pages are allocated by the cache.

The flags are

`SLAB_POISON` - Poison the slab with a known test pattern (a5a5a5a5)
to catch references to uninitialised memory.

`SLAB_RED_ZONE` - Insert Red zones around the allocated memory to check
for buffer overruns.

`SLAB_HWCACHE_ALIGN` - Align the objects in this cache to a hardware
cacheline. This can be beneficial if you're counting cycles as closely
as davem.

**Return**

a pointer to the cache on success, NULL on failure.

int kmem_cache_shrink(struct kmem_cache \*cachep)
:   Shrink a cache.

**Parameters**

`struct kmem_cache *cachep`
:   The cache to shrink.

**Description**

Releases as many slabs as possible for a cache.
To help debugging, a zero exit status indicates all slabs were released.

**Return**

`0` if all slabs were released, non-zero otherwise

bool kmem_dump_obj(void \*object)
:   Print available slab provenance information

**Parameters**

`void *object`
:   slab object for which to find provenance information.

**Description**

This function uses [`pr_cont()`](printk-basics.md#c.pr_cont "pr_cont"), so that the caller is expected to have
printed out whatever preamble is appropriate. The provenance information
depends on the type of object and on how much debugging is enabled.
For a slab-cache object, the fact that it is a slab object is printed,
and, if available, the slab name, return address, and stack trace from
the allocation and last free path of that object.

**Return**

`true` if the pointer is to a not-yet-freed object from
[`kmalloc()`](mm-api.md#c.kmalloc "kmalloc") or [`kmem_cache_alloc()`](mm-api.md#c.kmem_cache_alloc "kmem_cache_alloc"), either `true` or `false` if the pointer
is to an already-freed object, and `false` otherwise.

void \*krealloc(const void \*p, size_t new_size, gfp_t flags)
:   reallocate memory. The contents will remain unchanged.

**Parameters**

`const void *p`
:   object to reallocate memory for.

`size_t new_size`
:   how many bytes of memory are required.

`gfp_t flags`
:   the type of memory to allocate.

**Description**

The contents of the object pointed to are preserved up to the
lesser of the new and old sizes (__GFP_ZERO flag is effectively ignored).
If **p** is `NULL`, [`krealloc()`](mm-api.md#c.krealloc "krealloc") behaves exactly like [`kmalloc()`](mm-api.md#c.kmalloc "kmalloc"). If **new_size**
is 0 and **p** is not a `NULL` pointer, the object pointed to is freed.

**Return**

pointer to the allocated memory or `NULL` in case of error

void kfree_sensitive(const void \*p)
:   Clear sensitive information in memory before freeing

**Parameters**

`const void *p`
:   object to free memory of

**Description**

The memory of the object **p** points to is zeroed before freed.
If **p** is `NULL`, [`kfree_sensitive()`](mm-api.md#c.kfree_sensitive "kfree_sensitive") does nothing.

**Note**

this function zeroes the whole allocated buffer which can be a good
deal bigger than the requested buffer size passed to [`kmalloc()`](mm-api.md#c.kmalloc "kmalloc"). So be
careful when using this function in performance sensitive code.

void kfree_const(const void \*x)
:   conditionally free memory

**Parameters**

`const void *x`
:   pointer to the memory

**Description**

Function calls kfree only if **x** is not in .rodata section.

void \*kvmalloc_node(size_t size, gfp_t flags, int node)
:   attempt to allocate physically contiguous memory, but upon failure, fall back to non-contiguous (vmalloc) allocation.

**Parameters**

`size_t size`
:   size of the request.

`gfp_t flags`
:   gfp mask for the allocation - must be compatible (superset) with GFP_KERNEL.

`int node`
:   numa node to allocate from

**Description**

Uses kmalloc to get the memory but if the allocation fails then falls back
to the vmalloc allocator. Use kvfree for freeing the memory.

GFP_NOWAIT and GFP_ATOMIC are not supported, neither is the __GFP_NORETRY modifier.
__GFP_RETRY_MAYFAIL is supported, and it should be used only if kmalloc is
preferable to the vmalloc fallback, due to visible performance drawbacks.

**Return**

pointer to the allocated memory of `NULL` in case of failure

void kvfree(const void \*addr)
:   Free memory.

**Parameters**

`const void *addr`
:   Pointer to allocated memory.

**Description**

kvfree frees memory allocated by any of [`vmalloc()`](mm-api.md#c.vmalloc "vmalloc"), [`kmalloc()`](mm-api.md#c.kmalloc "kmalloc") or kvmalloc().
It is slightly more efficient to use [`kfree()`](mm-api.md#c.kfree "kfree") or [`vfree()`](mm-api.md#c.vfree "vfree") if you are certain
that you know which one to use.

**Context**

Either preemptible task context or not-NMI interrupt.

## Virtually Contiguous Mappings

void vm_unmap_aliases(void)
:   unmap outstanding lazy aliases in the vmap layer

**Parameters**

`void`
:   no arguments

**Description**

The vmap/vmalloc layer lazily flushes kernel virtual mappings primarily
to amortize TLB flushing overheads. What this means is that any page you
have now, may, in a former life, have been mapped into kernel virtual
address by the vmap layer and so there might be some CPUs with TLB entries
still referencing that page (additional to the regular 1:1 kernel mapping).

vm_unmap_aliases flushes all such lazy mappings. After it returns, we can
be sure that none of the pages we have control over will have any aliases
from the vmap layer.

void vm_unmap_ram(const void \*mem, unsigned int count)
:   unmap linear kernel address space set up by vm_map_ram

**Parameters**

`const void *mem`
:   the pointer returned by vm_map_ram

`unsigned int count`
:   the count passed to that vm_map_ram call (cannot unmap partial)

void \*vm_map_ram(struct page \*\*pages, unsigned int count, int node)
:   map pages linearly into kernel virtual address (vmalloc space)

**Parameters**

`struct page **pages`
:   an array of pointers to the pages to be mapped

`unsigned int count`
:   number of pages

`int node`
:   prefer to allocate data structures on this node

**Description**

If you use this function for less than VMAP_MAX_ALLOC pages, it could be
faster than vmap so it's good. But if you mix long-life and short-life
objects with [`vm_map_ram()`](mm-api.md#c.vm_map_ram "vm_map_ram"), it could consume lots of address space through
fragmentation (especially on a 32bit machine). You could see failures in
the end. Please use this function for short-lived objects.

**Return**

a pointer to the address that has been mapped, or `NULL` on failure

void vfree(const void \*addr)
:   Release memory allocated by [`vmalloc()`](mm-api.md#c.vmalloc "vmalloc")

**Parameters**

`const void *addr`
:   Memory base address

**Description**

Free the virtually continuous memory area starting at **addr**, as obtained
from one of the [`vmalloc()`](mm-api.md#c.vmalloc "vmalloc") family of APIs. This will usually also free the
physical memory underlying the virtual allocation, but that memory is
reference counted, so it will not be freed until the last user goes away.

If **addr** is NULL, no operation is performed.

**Context**

May sleep if called *not* from interrupt context.
Must not be called in NMI context (strictly speaking, it could be
if we have CONFIG_ARCH_HAVE_NMI_SAFE_CMPXCHG, but making the calling
conventions for [`vfree()`](mm-api.md#c.vfree "vfree") arch-dependent would be a really bad idea).

void vunmap(const void \*addr)
:   release virtual mapping obtained by [`vmap()`](mm-api.md#c.vmap "vmap")

**Parameters**

`const void *addr`
:   memory base address

**Description**

Free the virtually contiguous memory area starting at **addr**,
which was created from the page array passed to [`vmap()`](mm-api.md#c.vmap "vmap").

Must not be called in interrupt context.

void \*vmap(struct page \*\*pages, unsigned int count, unsigned long flags, pgprot_t prot)
:   map an array of pages into virtually contiguous space

**Parameters**

`struct page **pages`
:   array of page pointers

`unsigned int count`
:   number of pages to map

`unsigned long flags`
:   vm_area->flags

`pgprot_t prot`
:   page protection for the mapping

**Description**

Maps **count** pages from **pages** into contiguous kernel virtual space.
If **flags** contains `VM_MAP_PUT_PAGES` the ownership of the pages array itself
(which must be kmalloc or vmalloc memory) and one reference per pages in it
are transferred from the caller to [`vmap()`](mm-api.md#c.vmap "vmap"), and will be freed / dropped when
[`vfree()`](mm-api.md#c.vfree "vfree") is called on the return value.

**Return**

the address of the area or `NULL` on failure

void \*vmap_pfn(unsigned long \*pfns, unsigned int count, pgprot_t prot)
:   map an array of PFNs into virtually contiguous space

**Parameters**

`unsigned long *pfns`
:   array of PFNs

`unsigned int count`
:   number of pages to map

`pgprot_t prot`
:   page protection for the mapping

**Description**

Maps **count** PFNs from **pfns** into contiguous kernel virtual space and returns
the start address of the mapping.

void \*__vmalloc_node(unsigned long size, unsigned long align, gfp_t gfp_mask, int node, const void \*caller)
:   allocate virtually contiguous memory

**Parameters**

`unsigned long size`
:   allocation size

`unsigned long align`
:   desired alignment

`gfp_t gfp_mask`
:   flags for the page level allocator

`int node`
:   node to use for allocation or NUMA_NO_NODE

`const void *caller`
:   caller's return address

**Description**

Allocate enough pages to cover **size** from the page level allocator with
**gfp_mask** flags. Map them into contiguous kernel virtual space.

Reclaim modifiers in **gfp_mask** - __GFP_NORETRY, __GFP_RETRY_MAYFAIL
and __GFP_NOFAIL are not supported

Any use of gfp flags outside of GFP_KERNEL should be consulted
with mm people.

**Return**

pointer to the allocated memory or `NULL` on error

void \*vmalloc(unsigned long size)
:   allocate virtually contiguous memory

**Parameters**

`unsigned long size`
:   allocation size

**Description**

Allocate enough pages to cover **size** from the page level
allocator and map them into contiguous kernel virtual space.

For tight control over page level allocator and protection flags
use __vmalloc() instead.

**Return**

pointer to the allocated memory or `NULL` on error

void \*vmalloc_huge(unsigned long size, gfp_t gfp_mask)
:   allocate virtually contiguous memory, allow huge pages

**Parameters**

`unsigned long size`
:   allocation size

`gfp_t gfp_mask`
:   flags for the page level allocator

**Description**

Allocate enough pages to cover **size** from the page level
allocator and map them into contiguous kernel virtual space.
If **size** is greater than or equal to PMD_SIZE, allow using
huge pages for the memory

**Return**

pointer to the allocated memory or `NULL` on error

void \*vzalloc(unsigned long size)
:   allocate virtually contiguous memory with zero fill

**Parameters**

`unsigned long size`
:   allocation size

**Description**

Allocate enough pages to cover **size** from the page level
allocator and map them into contiguous kernel virtual space.
The memory allocated is set to zero.

For tight control over page level allocator and protection flags
use __vmalloc() instead.

**Return**

pointer to the allocated memory or `NULL` on error

void \*vmalloc_user(unsigned long size)
:   allocate zeroed virtually contiguous memory for userspace

**Parameters**

`unsigned long size`
:   allocation size

**Description**

The resulting memory area is zeroed so it can be mapped to userspace
without leaking data.

**Return**

pointer to the allocated memory or `NULL` on error

void \*vmalloc_node(unsigned long size, int node)
:   allocate memory on a specific node

**Parameters**

`unsigned long size`
:   allocation size

`int node`
:   numa node

**Description**

Allocate enough pages to cover **size** from the page level
allocator and map them into contiguous kernel virtual space.

For tight control over page level allocator and protection flags
use __vmalloc() instead.

**Return**

pointer to the allocated memory or `NULL` on error

void \*vzalloc_node(unsigned long size, int node)
:   allocate memory on a specific node with zero fill

**Parameters**

`unsigned long size`
:   allocation size

`int node`
:   numa node

**Description**

Allocate enough pages to cover **size** from the page level
allocator and map them into contiguous kernel virtual space.
The memory allocated is set to zero.

**Return**

pointer to the allocated memory or `NULL` on error

void \*vmalloc_32(unsigned long size)
:   allocate virtually contiguous memory (32bit addressable)

**Parameters**

`unsigned long size`
:   allocation size

**Description**

Allocate enough 32bit PA addressable pages to cover **size** from the
page level allocator and map them into contiguous kernel virtual space.

**Return**

pointer to the allocated memory or `NULL` on error

void \*vmalloc_32_user(unsigned long size)
:   allocate zeroed virtually contiguous 32bit memory

**Parameters**

`unsigned long size`
:   allocation size

**Description**

The resulting memory area is 32bit addressable and zeroed so it can be
mapped to userspace without leaking data.

**Return**

pointer to the allocated memory or `NULL` on error

int remap_vmalloc_range(struct vm_area_struct \*vma, void \*addr, unsigned long pgoff)
:   map vmalloc pages to userspace

**Parameters**

`struct vm_area_struct *vma`
:   vma to cover (map full range of vma)

`void *addr`
:   vmalloc memory

`unsigned long pgoff`
:   number of pages into addr before first page to map

**Return**

0 for success, -Exxx on failure

**Description**

This function checks that addr is a valid vmalloc'ed area, and
that it is big enough to cover the vma. Will return failure if
that criteria isn't met.

Similar to [`remap_pfn_range()`](mm-api.md#c.remap_pfn_range "remap_pfn_range") (see mm/memory.c)

## File Mapping and Page Cache

### Filemap

int filemap_fdatawrite_wbc(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, struct writeback_control \*wbc)
:   start writeback on mapping dirty pages in range

**Parameters**

`struct address_space *mapping`
:   address space structure to write

`struct writeback_control *wbc`
:   the writeback_control controlling the writeout

**Description**

Call writepages on the mapping using the provided wbc to control the
writeout.

**Return**

`0` on success, negative error code otherwise.

int filemap_flush(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping)
:   mostly a non-blocking flush

**Parameters**

`struct address_space *mapping`
:   target address_space

**Description**

This is a mostly non-blocking flush. Not suitable for data-integrity
purposes - I/O may not be started against all dirty pages.

**Return**

`0` on success, negative error code otherwise.

bool filemap_range_has_page(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, loff_t start_byte, loff_t end_byte)
:   check if a page exists in range.

**Parameters**

`struct address_space *mapping`
:   address space within which to check

`loff_t start_byte`
:   offset in bytes where the range starts

`loff_t end_byte`
:   offset in bytes where the range ends (inclusive)

**Description**

Find at least one page in the range supplied, usually used to check if
direct writing in this range will trigger a writeback.

**Return**

`true` if at least one page exists in the specified range,
`false` otherwise.

int filemap_fdatawait_range(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, loff_t start_byte, loff_t end_byte)
:   wait for writeback to complete

**Parameters**

`struct address_space *mapping`
:   address space structure to wait for

`loff_t start_byte`
:   offset in bytes where the range starts

`loff_t end_byte`
:   offset in bytes where the range ends (inclusive)

**Description**

Walk the list of under-writeback pages of the given address space
in the given range and wait for all of them. Check error status of
the address space and return it.

Since the error status of the address space is cleared by this function,
callers are responsible for checking the return value and handling and/or
reporting the error.

**Return**

error status of the address space.

int filemap_fdatawait_range_keep_errors(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, loff_t start_byte, loff_t end_byte)
:   wait for writeback to complete

**Parameters**

`struct address_space *mapping`
:   address space structure to wait for

`loff_t start_byte`
:   offset in bytes where the range starts

`loff_t end_byte`
:   offset in bytes where the range ends (inclusive)

**Description**

Walk the list of under-writeback pages of the given address space in the
given range and wait for all of them. Unlike [`filemap_fdatawait_range()`](mm-api.md#c.filemap_fdatawait_range "filemap_fdatawait_range"),
this function does not clear error status of the address space.

Use this function if callers don't handle errors themselves. Expected
call sites are system-wide / filesystem-wide data flushers: e.g. sync(2),
fsfreeze(8)

int file_fdatawait_range(struct [file](mm-api.md#c.file_fdatawait_range "file") \*file, loff_t start_byte, loff_t end_byte)
:   wait for writeback to complete

**Parameters**

`struct file *file`
:   file pointing to address space structure to wait for

`loff_t start_byte`
:   offset in bytes where the range starts

`loff_t end_byte`
:   offset in bytes where the range ends (inclusive)

**Description**

Walk the list of under-writeback pages of the address space that file
refers to, in the given range and wait for all of them. Check error
status of the address space vs. the file->f_wb_err cursor and return it.

Since the error status of the file is advanced by this function,
callers are responsible for checking the return value and handling and/or
reporting the error.

**Return**

error status of the address space vs. the file->f_wb_err cursor.

int filemap_fdatawait_keep_errors(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping)
:   wait for writeback without clearing errors

**Parameters**

`struct address_space *mapping`
:   address space structure to wait for

**Description**

Walk the list of under-writeback pages of the given address space
and wait for all of them. Unlike filemap_fdatawait(), this function
does not clear error status of the address space.

Use this function if callers don't handle errors themselves. Expected
call sites are system-wide / filesystem-wide data flushers: e.g. sync(2),
fsfreeze(8)

**Return**

error status of the address space.

int filemap_write_and_wait_range(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, loff_t lstart, loff_t lend)
:   write out & wait on a file range

**Parameters**

`struct address_space *mapping`
:   the address_space for the pages

`loff_t lstart`
:   offset in bytes where the range starts

`loff_t lend`
:   offset in bytes where the range ends (inclusive)

**Description**

Write out and wait upon file offsets lstart->lend, inclusive.

Note that **lend** is inclusive (describes the last byte to be written) so
that this function can be used to write to the very end-of-file (end = -1).

**Return**

error status of the address space.

int file_check_and_advance_wb_err(struct [file](mm-api.md#c.file_check_and_advance_wb_err "file") \*file)
:   report wb error (if any) that was previously and advance wb_err to current one

**Parameters**

`struct file *file`
:   struct file on which the error is being reported

**Description**

When userland calls fsync (or something like nfsd does the equivalent), we
want to report any writeback errors that occurred since the last fsync (or
since the file was opened if there haven't been any).

Grab the wb_err from the mapping. If it matches what we have in the file,
then just quickly return 0. The file is all caught up.

If it doesn't match, then take the mapping value, set the "seen" flag in
it and try to swap it into place. If it works, or another task beat us
to it with the new value, then update the f_wb_err and return the error
portion. The error at this point must be reported via proper channels
(a'la fsync, or NFS COMMIT operation, etc.).

While we handle mapping->wb_err with atomic operations, the f_wb_err
value is protected by the f_lock since we must ensure that it reflects
the latest value swapped in for this file descriptor.

**Return**

`0` on success, negative error code otherwise.

int file_write_and_wait_range(struct [file](mm-api.md#c.file_write_and_wait_range "file") \*file, loff_t lstart, loff_t lend)
:   write out & wait on a file range

**Parameters**

`struct file *file`
:   file pointing to address_space with pages

`loff_t lstart`
:   offset in bytes where the range starts

`loff_t lend`
:   offset in bytes where the range ends (inclusive)

**Description**

Write out and wait upon file offsets lstart->lend, inclusive.

Note that **lend** is inclusive (describes the last byte to be written) so
that this function can be used to write to the very end-of-file (end = -1).

After writing out and waiting on the data, we check and advance the
f_wb_err cursor to the latest value, and return any errors detected there.

**Return**

`0` on success, negative error code otherwise.

void replace_page_cache_folio(struct [folio](mm-api.md#c.folio "folio") \*old, struct [folio](mm-api.md#c.folio "folio") \*new)
:   replace a pagecache folio with a new one

**Parameters**

`struct folio *old`
:   folio to be replaced

`struct folio *new`
:   folio to replace with

**Description**

This function replaces a folio in the pagecache with a new one. On
success it acquires the pagecache reference for the new folio and
drops it for the old folio. Both the old and new folios must be
locked. This function does not add the new folio to the LRU, the
caller must do that.

The remove + add is atomic. This function cannot fail.

void folio_add_wait_queue(struct [folio](mm-api.md#c.folio_add_wait_queue "folio") \*folio, wait_queue_entry_t \*waiter)
:   Add an arbitrary waiter to a folio's wait queue

**Parameters**

`struct folio *folio`
:   Folio defining the wait queue of interest

`wait_queue_entry_t *waiter`
:   Waiter to add to the queue

**Description**

Add an arbitrary **waiter** to the wait queue for the nominated **folio**.

void folio_unlock(struct [folio](mm-api.md#c.folio_unlock "folio") \*folio)
:   Unlock a locked folio.

**Parameters**

`struct folio *folio`
:   The folio.

**Description**

Unlocks the folio and wakes up any thread sleeping on the page lock.

**Context**

May be called from interrupt or process context. May not be
called from NMI context.

void folio_end_read(struct [folio](mm-api.md#c.folio_end_read "folio") \*folio, bool success)
:   End read on a folio.

**Parameters**

`struct folio *folio`
:   The folio.

`bool success`
:   True if all reads completed successfully.

**Description**

When all reads against a folio have completed, filesystems should
call this function to let the pagecache know that no more reads
are outstanding. This will unlock the folio and wake up any thread
sleeping on the lock. The folio will also be marked uptodate if all
reads succeeded.

**Context**

May be called from interrupt or process context. May not be
called from NMI context.

void folio_end_private_2(struct [folio](mm-api.md#c.folio_end_private_2 "folio") \*folio)
:   Clear PG_private_2 and wake any waiters.

**Parameters**

`struct folio *folio`
:   The folio.

**Description**

Clear the PG_private_2 bit on a folio and wake up any sleepers waiting for
it. The folio reference held for PG_private_2 being set is released.

This is, for example, used when a netfs folio is being written to a local
disk cache, thereby allowing writes to the cache for the same folio to be
serialised.

void folio_wait_private_2(struct [folio](mm-api.md#c.folio_wait_private_2 "folio") \*folio)
:   Wait for PG_private_2 to be cleared on a folio.

**Parameters**

`struct folio *folio`
:   The folio to wait on.

**Description**

Wait for PG_private_2 (aka PG_fscache) to be cleared on a folio.

int folio_wait_private_2_killable(struct [folio](mm-api.md#c.folio_wait_private_2_killable "folio") \*folio)
:   Wait for PG_private_2 to be cleared on a folio.

**Parameters**

`struct folio *folio`
:   The folio to wait on.

**Description**

Wait for PG_private_2 (aka PG_fscache) to be cleared on a folio or until a
fatal signal is received by the calling task.

**Return**

- 0 if successful.
- -EINTR if a fatal signal was encountered.

void folio_end_writeback(struct [folio](mm-api.md#c.folio_end_writeback "folio") \*folio)
:   End writeback against a folio.

**Parameters**

`struct folio *folio`
:   The folio.

**Description**

The folio must actually be under writeback.

**Context**

May be called from process or interrupt context.

void __folio_lock(struct [folio](mm-api.md#c.__folio_lock "folio") \*folio)
:   Get a lock on the folio, assuming we need to sleep to get it.

**Parameters**

`struct folio *folio`
:   The folio to lock

pgoff_t page_cache_next_miss(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, pgoff_t index, unsigned long max_scan)
:   Find the next gap in the page cache.

**Parameters**

`struct address_space *mapping`
:   Mapping.

`pgoff_t index`
:   Index.

`unsigned long max_scan`
:   Maximum range to search.

**Description**

Search the range [index, min(index + max_scan - 1, ULONG_MAX)] for the
gap with the lowest index.

This function may be called under the rcu_read_lock. However, this will
not atomically search a snapshot of the cache at a single point in time.
For example, if a gap is created at index 5, then subsequently a gap is
created at index 10, page_cache_next_miss covering both indices may
return 10 if called under the rcu_read_lock.

**Return**

The index of the gap if found, otherwise an index outside the
range specified (in which case 'return - index >= max_scan' will be true).
In the rare case of index wrap-around, 0 will be returned.

pgoff_t page_cache_prev_miss(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, pgoff_t index, unsigned long max_scan)
:   Find the previous gap in the page cache.

**Parameters**

`struct address_space *mapping`
:   Mapping.

`pgoff_t index`
:   Index.

`unsigned long max_scan`
:   Maximum range to search.

**Description**

Search the range [max(index - max_scan + 1, 0), index] for the
gap with the highest index.

This function may be called under the rcu_read_lock. However, this will
not atomically search a snapshot of the cache at a single point in time.
For example, if a gap is created at index 10, then subsequently a gap is
created at index 5, [`page_cache_prev_miss()`](mm-api.md#c.page_cache_prev_miss "page_cache_prev_miss") covering both indices may
return 5 if called under the rcu_read_lock.

**Return**

The index of the gap if found, otherwise an index outside the
range specified (in which case 'index - return >= max_scan' will be true).
In the rare case of wrap-around, ULONG_MAX will be returned.

struct [folio](mm-api.md#c.folio "folio") \*__filemap_get_folio(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, pgoff_t index, [fgf_t](mm-api.md#c.fgf_t "fgf_t") fgp_flags, gfp_t gfp)
:   Find and get a reference to a folio.

**Parameters**

`struct address_space *mapping`
:   The address_space to search.

`pgoff_t index`
:   The page index.

`fgf_t fgp_flags`
:   `FGP` flags modify how the folio is returned.

`gfp_t gfp`
:   Memory allocation flags to use if `FGP_CREAT` is specified.

**Description**

Looks up the page cache entry at **mapping** & **index**.

If `FGP_LOCK` or `FGP_CREAT` are specified then the function may sleep even
if the `GFP` flags specified for `FGP_CREAT` are atomic.

If this function returns a folio, it is returned with an increased refcount.

**Return**

The found folio or an [`ERR_PTR()`](kernel-api.md#c.ERR_PTR "ERR_PTR") otherwise.

unsigned filemap_get_folios(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, pgoff_t \*start, pgoff_t end, struct folio_batch \*fbatch)
:   Get a batch of folios

**Parameters**

`struct address_space *mapping`
:   The address_space to search

`pgoff_t *start`
:   The starting page index

`pgoff_t end`
:   The final page index (inclusive)

`struct folio_batch *fbatch`
:   The batch to fill.

**Description**

Search for and return a batch of folios in the mapping starting at
index **start** and up to index **end** (inclusive). The folios are returned
in **fbatch** with an elevated reference count.

**Return**

The number of folios which were found.
We also update **start** to index the next folio for the traversal.

unsigned filemap_get_folios_contig(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, pgoff_t \*start, pgoff_t end, struct folio_batch \*fbatch)
:   Get a batch of contiguous folios

**Parameters**

`struct address_space *mapping`
:   The address_space to search

`pgoff_t *start`
:   The starting page index

`pgoff_t end`
:   The final page index (inclusive)

`struct folio_batch *fbatch`
:   The batch to fill

**Description**

[`filemap_get_folios_contig()`](mm-api.md#c.filemap_get_folios_contig "filemap_get_folios_contig") works exactly like [`filemap_get_folios()`](mm-api.md#c.filemap_get_folios "filemap_get_folios"),
except the returned folios are guaranteed to be contiguous. This may
not return all contiguous folios if the batch gets filled up.

**Return**

The number of folios found.
Also update **start** to be positioned for traversal of the next folio.

unsigned filemap_get_folios_tag(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, pgoff_t \*start, pgoff_t end, xa_mark_t tag, struct folio_batch \*fbatch)
:   Get a batch of folios matching **tag**

**Parameters**

`struct address_space *mapping`
:   The address_space to search

`pgoff_t *start`
:   The starting page index

`pgoff_t end`
:   The final page index (inclusive)

`xa_mark_t tag`
:   The tag index

`struct folio_batch *fbatch`
:   The batch to fill

**Description**

The first folio may start before **start**; if it does, it will contain
**start**. The final folio may extend beyond **end**; if it does, it will
contain **end**. The folios have ascending indices. There may be gaps
between the folios if there are indices which have no folio in the
page cache. If folios are added to or removed from the page cache
while this is running, they may or may not be found by this call.
Only returns folios that are tagged with **tag**.

**Return**

The number of folios found.
Also update **start** to index the next folio for traversal.

ssize_t filemap_read(struct kiocb \*iocb, struct iov_iter \*iter, ssize_t already_read)
:   Read data from the page cache.

**Parameters**

`struct kiocb *iocb`
:   The iocb to read.

`struct iov_iter *iter`
:   Destination for the data.

`ssize_t already_read`
:   Number of bytes already read by the caller.

**Description**

Copies data from the page cache. If the data is not currently present,
uses the readahead and read_folio address_space operations to fetch it.

**Return**

Total number of bytes copied, including those already read by
the caller. If an error happens before any bytes are copied, returns
a negative error number.

ssize_t generic_file_read_iter(struct kiocb \*iocb, struct iov_iter \*iter)
:   generic filesystem read routine

**Parameters**

`struct kiocb *iocb`
:   kernel I/O control block

`struct iov_iter *iter`
:   destination for the data read

**Description**

This is the "read_iter()" routine for all filesystems
that can use the page cache directly.

The IOCB_NOWAIT flag in iocb->ki_flags indicates that -EAGAIN shall
be returned when no data can be read without waiting for I/O requests
to complete; it doesn't prevent readahead.

The IOCB_NOIO flag in iocb->ki_flags indicates that no new I/O
requests shall be made for the read or for readahead. When no data
can be read, -EAGAIN shall be returned. When readahead would be
triggered, a partial, possibly empty read shall be returned.

**Return**

- number of bytes copied, even for partial reads
- negative error code (or 0 if IOCB_NOIO) if nothing was read

ssize_t filemap_splice_read(struct file \*in, loff_t \*ppos, struct [pipe_inode_info](../filesystems/splice.md#c.pipe_inode_info "pipe_inode_info") \*pipe, size_t len, unsigned int flags)
:   Splice data from a file's pagecache into a pipe

**Parameters**

`struct file *in`
:   The file to read from

`loff_t *ppos`
:   Pointer to the file position to read from

`struct pipe_inode_info *pipe`
:   The pipe to splice into

`size_t len`
:   The amount to splice

`unsigned int flags`
:   The SPLICE_F_\* flags

**Description**

This function gets folios from a file's pagecache and splices them into the
pipe. Readahead will be called as necessary to fill more folios. This may
be used for blockdevs also.

**Return**

On success, the number of bytes read will be returned and **\*ppos**
will be updated if appropriate; 0 will be returned if there is no more data
to be read; -EAGAIN will be returned if the pipe had no space, and some
other negative error code will be returned on error. A short read may occur
if the pipe has insufficient space, we reach the end of the data or we hit a
hole.

[vm_fault_t](mm-api.md#c.vm_fault_t "vm_fault_t") filemap_fault(struct vm_fault \*vmf)
:   read in file data for page fault handling

**Parameters**

`struct vm_fault *vmf`
:   struct vm_fault containing details of the fault

**Description**

[`filemap_fault()`](mm-api.md#c.filemap_fault "filemap_fault") is invoked via the vma operations vector for a
mapped memory region to read in file data during a page fault.

The goto's are kind of ugly, but this streamlines the normal case of having
it in the page cache, and handles the special cases reasonably without
having a lot of duplicated code.

vma->vm_mm->mmap_lock must be held on entry.

If our return value has VM_FAULT_RETRY set, it's because the mmap_lock
may be dropped before doing I/O or by lock_folio_maybe_drop_mmap().

If our return value does not have VM_FAULT_RETRY set, the mmap_lock
has not been released.

We never return with VM_FAULT_RETRY and a bit from VM_FAULT_ERROR set.

**Return**

bitwise-OR of `VM_FAULT_` codes.

struct [folio](mm-api.md#c.folio "folio") \*read_cache_folio(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, pgoff_t index, filler_t filler, struct [file](mm-api.md#c.read_cache_folio "file") \*file)
:   Read into page cache, fill it if needed.

**Parameters**

`struct address_space *mapping`
:   The address_space to read from.

`pgoff_t index`
:   The index to read.

`filler_t filler`
:   Function to perform the read, or NULL to use aops->read_folio().

`struct file *file`
:   Passed to filler function, may be NULL if not required.

**Description**

Read one page into the page cache. If it succeeds, the folio returned
will contain **index**, but it may not be the first page of the folio.

If the filler function returns an error, it will be returned to the
caller.

**Context**

May sleep. Expects mapping->invalidate_lock to be held.

**Return**

An uptodate folio on success, [`ERR_PTR()`](kernel-api.md#c.ERR_PTR "ERR_PTR") on failure.

struct [folio](mm-api.md#c.folio "folio") \*mapping_read_folio_gfp(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, pgoff_t index, gfp_t gfp)
:   Read into page cache, using specified allocation flags.

**Parameters**

`struct address_space *mapping`
:   The address_space for the folio.

`pgoff_t index`
:   The index that the allocated folio will contain.

`gfp_t gfp`
:   The page allocator flags to use if allocating.

**Description**

This is the same as "read_cache_folio(mapping, index, NULL, NULL)", but with
any new memory allocations done using the specified allocation flags.

The most likely error from this function is EIO, but ENOMEM is
possible and so is EINTR. If ->read_folio returns another error,
that will be returned to the caller.

The function expects mapping->invalidate_lock to be already held.

**Return**

Uptodate folio on success, [`ERR_PTR()`](kernel-api.md#c.ERR_PTR "ERR_PTR") on failure.

struct page \*read_cache_page_gfp(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, pgoff_t index, gfp_t gfp)
:   read into page cache, using specified page allocation flags.

**Parameters**

`struct address_space *mapping`
:   the page's address_space

`pgoff_t index`
:   the page index

`gfp_t gfp`
:   the page allocator flags to use if allocating

**Description**

This is the same as "read_mapping_page(mapping, index, NULL)", but with
any new page allocations done using the specified allocation flags.

If the page does not get brought uptodate, return -EIO.

The function expects mapping->invalidate_lock to be already held.

**Return**

up to date page on success, [`ERR_PTR()`](kernel-api.md#c.ERR_PTR "ERR_PTR") on failure.

ssize_t __generic_file_write_iter(struct kiocb \*iocb, struct iov_iter \*from)
:   write data to a file

**Parameters**

`struct kiocb *iocb`
:   IO state structure (file, offset, etc.)

`struct iov_iter *from`
:   iov_iter with data to write

**Description**

This function does all the work needed for actually writing data to a
file. It does all basic checks, removes SUID from the file, updates
modification times and calls proper subroutines depending on whether we
do direct IO or a standard buffered write.

It expects i_rwsem to be grabbed unless we work on a block device or similar
object which does not need locking at all.

This function does *not* take care of syncing data in case of O_SYNC write.
A caller has to handle it. This is mainly due to the fact that we want to
avoid syncing under i_rwsem.

**Return**

- number of bytes written, even for truncated writes
- negative error code if no data has been written at all

ssize_t generic_file_write_iter(struct kiocb \*iocb, struct iov_iter \*from)
:   write data to a file

**Parameters**

`struct kiocb *iocb`
:   IO state structure

`struct iov_iter *from`
:   iov_iter with data to write

**Description**

This is a wrapper around [`__generic_file_write_iter()`](mm-api.md#c.__generic_file_write_iter "__generic_file_write_iter") to be used by most
filesystems. It takes care of syncing the file in case of O_SYNC file
and acquires i_rwsem as needed.

**Return**

- negative error code if no data has been written at all of
  [`vfs_fsync_range()`](../filesystems/api-summary.md#c.vfs_fsync_range "vfs_fsync_range") failed for a synchronous write
- number of bytes written, even for truncated writes

bool filemap_release_folio(struct [folio](mm-api.md#c.filemap_release_folio "folio") \*folio, gfp_t gfp)
:   Release fs-specific metadata on a folio.

**Parameters**

`struct folio *folio`
:   The folio which the kernel is trying to free.

`gfp_t gfp`
:   Memory allocation flags (and I/O mode).

**Description**

The address_space is trying to release any data attached to a folio
(presumably at folio->private).

This will also be called if the private_2 flag is set on a page,
indicating that the folio has other metadata associated with it.

The **gfp** argument specifies whether I/O may be performed to release
this page (__GFP_IO), and whether the call may block
(__GFP_RECLAIM & __GFP_FS).

**Return**

`true` if the release was successful, otherwise `false`.

### Readahead

Readahead is used to read content into the page cache before it is
explicitly requested by the application. Readahead only ever
attempts to read folios that are not yet in the page cache. If a
folio is present but not up-to-date, readahead will not try to read
it. In that case a simple ->read_folio() will be requested.

Readahead is triggered when an application read request (whether a
system call or a page fault) finds that the requested folio is not in
the page cache, or that it is in the page cache and has the
readahead flag set. This flag indicates that the folio was read
as part of a previous readahead request and now that it has been
accessed, it is time for the next readahead.

Each readahead request is partly synchronous read, and partly async
readahead. This is reflected in the [`struct file_ra_state`](../filesystems/api-summary.md#c.file_ra_state "file_ra_state") which
contains ->size being the total number of pages, and ->async_size
which is the number of pages in the async section. The readahead
flag will be set on the first folio in this async section to trigger
a subsequent readahead. Once a series of sequential reads has been
established, there should be no need for a synchronous component and
all readahead request will be fully asynchronous.

When either of the triggers causes a readahead, three numbers need
to be determined: the start of the region to read, the size of the
region, and the size of the async tail.

The start of the region is simply the first page address at or after
the accessed address, which is not currently populated in the page
cache. This is found with a simple search in the page cache.

The size of the async tail is determined by subtracting the size that
was explicitly requested from the determined request size, unless
this would be less than zero - then zero is used. NOTE THIS
CALCULATION IS WRONG WHEN THE START OF THE REGION IS NOT THE ACCESSED
PAGE. ALSO THIS CALCULATION IS NOT USED CONSISTENTLY.

The size of the region is normally determined from the size of the
previous readahead which loaded the preceding pages. This may be
discovered from the [`struct file_ra_state`](../filesystems/api-summary.md#c.file_ra_state "file_ra_state") for simple sequential reads,
or from examining the state of the page cache when multiple
sequential reads are interleaved. Specifically: where the readahead
was triggered by the readahead flag, the size of the previous
readahead is assumed to be the number of pages from the triggering
page to the start of the new readahead. In these cases, the size of
the previous readahead is scaled, often doubled, for the new
readahead, though see get_next_ra_size() for details.

If the size of the previous read cannot be determined, the number of
preceding pages in the page cache is used to estimate the size of
a previous read. This estimate could easily be misled by random
reads being coincidentally adjacent, so it is ignored unless it is
larger than the current request, and it is not scaled up, unless it
is at the start of file.

In general readahead is accelerated at the start of the file, as
reads from there are often sequential. There are other minor
adjustments to the readahead size in various special cases and these
are best discovered by reading the code.

The above calculation, based on the previous readahead size,
determines the size of the readahead, to which any requested read
size may be added.

Readahead requests are sent to the filesystem using the ->readahead()
address space operation, for which [`mpage_readahead()`](../filesystems/api-summary.md#c.mpage_readahead "mpage_readahead") is a canonical
implementation. ->readahead() should normally initiate reads on all
folios, but may fail to read any or all folios without causing an I/O
error. The page cache reading code will issue a ->read_folio() request
for any folio which ->readahead() did not read, and only an error
from this will be final.

->readahead() will generally call [`readahead_folio()`](mm-api.md#c.readahead_folio "readahead_folio") repeatedly to get
each folio from those prepared for readahead. It may fail to read a
folio by:

- not calling [`readahead_folio()`](mm-api.md#c.readahead_folio "readahead_folio") sufficiently many times, effectively
  ignoring some folios, as might be appropriate if the path to
  storage is congested.
- failing to actually submit a read request for a given folio,
  possibly due to insufficient resources, or
- getting an error during subsequent processing of a request.

In the last two cases, the folio should be unlocked by the filesystem
to indicate that the read attempt has failed. In the first case the
folio will be unlocked by the VFS.

Those folios not in the final `async_size` of the request should be
considered to be important and ->readahead() should not fail them due
to congestion or temporary resource unavailability, but should wait
for necessary resources (e.g. memory or indexing information) to
become available. Folios in the final `async_size` may be
considered less urgent and failure to read them is more acceptable.
In this case it is best to use filemap_remove_folio() to remove the
folios from the page cache as is automatically done for folios that
were not fetched with [`readahead_folio()`](mm-api.md#c.readahead_folio "readahead_folio"). This will allow a
subsequent synchronous readahead request to try them again. If they
are left in the page cache, then they will be read individually using
->read_folio() which may be less efficient.

void page_cache_ra_unbounded(struct [readahead_control](mm-api.md#c.readahead_control "readahead_control") \*ractl, unsigned long nr_to_read, unsigned long lookahead_size)
:   Start unchecked readahead.

**Parameters**

`struct readahead_control *ractl`
:   Readahead control.

`unsigned long nr_to_read`
:   The number of pages to read.

`unsigned long lookahead_size`
:   Where to start the next readahead.

**Description**

This function is for filesystems to call when they want to start
readahead beyond a file's stated i_size. This is almost certainly
not the function you want to call. Use [`page_cache_async_readahead()`](mm-api.md#c.page_cache_async_readahead "page_cache_async_readahead")
or [`page_cache_sync_readahead()`](mm-api.md#c.page_cache_sync_readahead "page_cache_sync_readahead") instead.

**Context**

File is referenced by caller. Mutexes may be held by caller.
May sleep, but will not reenter filesystem to reclaim memory.

void readahead_expand(struct [readahead_control](mm-api.md#c.readahead_control "readahead_control") \*ractl, loff_t new_start, size_t new_len)
:   Expand a readahead request

**Parameters**

`struct readahead_control *ractl`
:   The request to be expanded

`loff_t new_start`
:   The revised start

`size_t new_len`
:   The revised size of the request

**Description**

Attempt to expand a readahead request outwards from the current size to the
specified size by inserting locked pages before and after the current window
to increase the size to the new window. This may involve the insertion of
THPs, in which case the window may get expanded even beyond what was
requested.

The algorithm will stop if it encounters a conflicting page already in the
pagecache and leave a smaller expansion than requested.

The caller must check for this by examining the revised **ractl** object for a
different expansion than was requested.

### Writeback

int balance_dirty_pages_ratelimited_flags(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, unsigned int flags)
:   Balance dirty memory state.

**Parameters**

`struct address_space *mapping`
:   address_space which was dirtied.

`unsigned int flags`
:   BDP flags.

**Description**

Processes which are dirtying memory should call in here once for each page
which was newly dirtied. The function will periodically check the system's
dirty state and will initiate writeback if needed.

See [`balance_dirty_pages_ratelimited()`](mm-api.md#c.balance_dirty_pages_ratelimited "balance_dirty_pages_ratelimited") for details.

**Return**

If **flags** contains BDP_ASYNC, it may return -EAGAIN to
indicate that memory is out of balance and the caller must wait
for I/O to complete. Otherwise, it will return 0 to indicate
that either memory was already in balance, or it was able to sleep
until the amount of dirty memory returned to balance.

void balance_dirty_pages_ratelimited(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping)
:   balance dirty memory state.

**Parameters**

`struct address_space *mapping`
:   address_space which was dirtied.

**Description**

Processes which are dirtying memory should call in here once for each page
which was newly dirtied. The function will periodically check the system's
dirty state and will initiate writeback if needed.

Once we're over the dirty memory limit we decrease the ratelimiting
by a lot, to prevent individual processes from overshooting the limit
by (ratelimit_pages) each.

void tag_pages_for_writeback(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, pgoff_t start, pgoff_t end)
:   tag pages to be written by write_cache_pages

**Parameters**

`struct address_space *mapping`
:   address space structure to write

`pgoff_t start`
:   starting page index

`pgoff_t end`
:   ending page index (inclusive)

**Description**

This function scans the page range from **start** to **end** (inclusive) and tags
all pages that have DIRTY tag set with a special TOWRITE tag. The idea is
that write_cache_pages (or whoever calls this function) will then use
TOWRITE tag to identify pages eligible for writeback. This mechanism is
used to avoid livelocking of writeback by a process steadily creating new
dirty pages in the file (thus it is important for this function to be quick
so that it can tag pages faster than a dirtying process can create them).

int write_cache_pages(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, struct writeback_control \*wbc, writepage_t writepage, void \*data)
:   walk the list of dirty pages of the given address space and write all of them.

**Parameters**

`struct address_space *mapping`
:   address space structure to write

`struct writeback_control *wbc`
:   subtract the number of written pages from **\*wbc->nr_to_write**

`writepage_t writepage`
:   function called for each page

`void *data`
:   data passed to writepage function

**Description**

If a page is already under I/O, [`write_cache_pages()`](mm-api.md#c.write_cache_pages "write_cache_pages") skips it, even
if it's dirty. This is desirable behaviour for memory-cleaning writeback,
but it is INCORRECT for data-integrity system calls such as fsync(). fsync()
and msync() need to guarantee that all the data which was dirty at the time
the call was made get new I/O started against them. If wbc->sync_mode is
WB_SYNC_ALL then we were called for data integrity and we must wait for
existing IO to complete.

To avoid livelocks (when other process dirties new pages), we first tag
pages which should be written back with TOWRITE tag and only then start
writing them. For data-integrity sync we have to be careful so that we do
not miss some pages (e.g., because some other process has cleared TOWRITE
tag we set). The rule we follow is that TOWRITE tag can be cleared only
by the process clearing the DIRTY tag (and submitting the page for IO).

To avoid deadlocks between range_cyclic writeback and callers that hold
pages in PageWriteback to aggregate IO until [`write_cache_pages()`](mm-api.md#c.write_cache_pages "write_cache_pages") returns,
we do not loop back to the start of the file. Doing so causes a page
lock/page writeback access order inversion - we should only ever lock
multiple pages in ascending page->index order, and looping back to the start
of the file violates that rule and causes deadlocks.

**Return**

`0` on success, negative error code otherwise

bool filemap_dirty_folio(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, struct [folio](mm-api.md#c.filemap_dirty_folio "folio") \*folio)
:   Mark a folio dirty for filesystems which do not use buffer_heads.

**Parameters**

`struct address_space *mapping`
:   Address space this folio belongs to.

`struct folio *folio`
:   Folio to be marked as dirty.

**Description**

Filesystems which do not use buffer heads should call this function
from their dirty_folio address space operation. It ignores the
contents of folio_get_private(), so if the filesystem marks individual
blocks as dirty, the filesystem should handle that itself.

This is also sometimes used by filesystems which use buffer_heads when
a single buffer is being dirtied: we want to set the folio dirty in
that case, but not all the buffers. This is a "bottom-up" dirtying,
whereas block_dirty_folio() is a "top-down" dirtying.

The caller must ensure this doesn't race with truncation. Most will
simply hold the folio lock, but e.g. zap_pte_range() calls with the
folio mapped and the pte lock held, which also locks out truncation.

bool folio_redirty_for_writepage(struct writeback_control \*wbc, struct [folio](mm-api.md#c.folio_redirty_for_writepage "folio") \*folio)
:   Decline to write a dirty folio.

**Parameters**

`struct writeback_control *wbc`
:   The writeback control.

`struct folio *folio`
:   The folio.

**Description**

When a writepage implementation decides that it doesn't want to write
**folio** for some reason, it should call this function, unlock **folio** and
return 0.

**Return**

True if we redirtied the folio. False if someone else dirtied
it first.

bool folio_mark_dirty(struct [folio](mm-api.md#c.folio_mark_dirty "folio") \*folio)
:   Mark a folio as being modified.

**Parameters**

`struct folio *folio`
:   The folio.

**Description**

The folio may not be truncated while this function is running.
Holding the folio lock is sufficient to prevent truncation, but some
callers cannot acquire a sleeping lock. These callers instead hold
the page table lock for a page table which contains at least one page
in this folio. Truncation will block on the page table lock as it
unmaps pages before removing the folio from its mapping.

**Return**

True if the folio was newly dirtied, false if it was already dirty.

void folio_wait_writeback(struct [folio](mm-api.md#c.folio_wait_writeback "folio") \*folio)
:   Wait for a folio to finish writeback.

**Parameters**

`struct folio *folio`
:   The folio to wait for.

**Description**

If the folio is currently being written back to storage, wait for the
I/O to complete.

**Context**

Sleeps. Must be called in process context and with
no spinlocks held. Caller should hold a reference on the folio.
If the folio is not locked, writeback may start again after writeback
has finished.

int folio_wait_writeback_killable(struct [folio](mm-api.md#c.folio_wait_writeback_killable "folio") \*folio)
:   Wait for a folio to finish writeback.

**Parameters**

`struct folio *folio`
:   The folio to wait for.

**Description**

If the folio is currently being written back to storage, wait for the
I/O to complete or a fatal signal to arrive.

**Context**

Sleeps. Must be called in process context and with
no spinlocks held. Caller should hold a reference on the folio.
If the folio is not locked, writeback may start again after writeback
has finished.

**Return**

0 on success, -EINTR if we get a fatal signal while waiting.

void folio_wait_stable(struct [folio](mm-api.md#c.folio_wait_stable "folio") \*folio)
:   wait for writeback to finish, if necessary.

**Parameters**

`struct folio *folio`
:   The folio to wait on.

**Description**

This function determines if the given folio is related to a backing
device that requires folio contents to be held stable during writeback.
If so, then it will wait for any pending writeback to complete.

**Context**

Sleeps. Must be called in process context and with
no spinlocks held. Caller should hold a reference on the folio.
If the folio is not locked, writeback may start again after writeback
has finished.

### Truncate

void folio_invalidate(struct [folio](mm-api.md#c.folio_invalidate "folio") \*folio, size_t offset, size_t length)
:   Invalidate part or all of a folio.

**Parameters**

`struct folio *folio`
:   The folio which is affected.

`size_t offset`
:   start of the range to invalidate

`size_t length`
:   length of the range to invalidate

**Description**

[`folio_invalidate()`](mm-api.md#c.folio_invalidate "folio_invalidate") is called when all or part of the folio has become
invalidated by a truncate operation.

[`folio_invalidate()`](mm-api.md#c.folio_invalidate "folio_invalidate") does not have to release all buffers, but it must
ensure that no dirty buffer is left outside **offset** and that no I/O
is underway against any of the blocks which are outside the truncation
point. Because the caller is about to free (and possibly reuse) those
blocks on-disk.

void truncate_inode_pages_range(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, loff_t lstart, loff_t lend)
:   truncate range of pages specified by start & end byte offsets

**Parameters**

`struct address_space *mapping`
:   mapping to truncate

`loff_t lstart`
:   offset from which to truncate

`loff_t lend`
:   offset to which to truncate (inclusive)

**Description**

Truncate the page cache, removing the pages that are between
specified offsets (and zeroing out partial pages
if lstart or lend + 1 is not page aligned).

Truncate takes two passes - the first pass is nonblocking. It will not
block on page locks and it will not block on writeback. The second pass
will wait. This is to prevent as much IO as possible in the affected region.
The first pass will remove most pages, so the search cost of the second pass
is low.

We pass down the cache-hot hint to the page freeing code. Even if the
mapping is large, it is probably the case that the final pages are the most
recently touched, and freeing happens in ascending file offset order.

Note that since ->invalidate_folio() accepts range to invalidate
truncate_inode_pages_range is able to handle cases where lend + 1 is not
page aligned properly.

void truncate_inode_pages(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, loff_t lstart)
:   truncate *all* the pages from an offset

**Parameters**

`struct address_space *mapping`
:   mapping to truncate

`loff_t lstart`
:   offset from which to truncate

**Description**

Called under (and serialised by) inode->i_rwsem and
mapping->invalidate_lock.

**Note**

When this function returns, there can be a page in the process of
deletion (inside __filemap_remove_folio()) in the specified range. Thus
mapping->nrpages can be non-zero when this function returns even after
truncation of the whole mapping.

void truncate_inode_pages_final(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping)
:   truncate *all* pages before inode dies

**Parameters**

`struct address_space *mapping`
:   mapping to truncate

**Description**

Called under (and serialized by) inode->i_rwsem.

Filesystems have to use this in the .evict_inode path to inform the
VM that this is the final truncate and the inode is going away.

unsigned long invalidate_mapping_pages(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, pgoff_t start, pgoff_t end)
:   Invalidate all clean, unlocked cache of one inode

**Parameters**

`struct address_space *mapping`
:   the address_space which holds the cache to invalidate

`pgoff_t start`
:   the offset 'from' which to invalidate

`pgoff_t end`
:   the offset 'to' which to invalidate (inclusive)

**Description**

This function removes pages that are clean, unmapped and unlocked,
as well as shadow entries. It will not block on IO activity.

If you want to remove all the pages of one inode, regardless of
their use and writeback state, use [`truncate_inode_pages()`](mm-api.md#c.truncate_inode_pages "truncate_inode_pages").

**Return**

The number of indices that had their contents invalidated

int invalidate_inode_pages2_range(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, pgoff_t start, pgoff_t end)
:   remove range of pages from an address_space

**Parameters**

`struct address_space *mapping`
:   the address_space

`pgoff_t start`
:   the page offset 'from' which to invalidate

`pgoff_t end`
:   the page offset 'to' which to invalidate (inclusive)

**Description**

Any pages which are found to be mapped into pagetables are unmapped prior to
invalidation.

**Return**

-EBUSY if any pages could not be invalidated.

int invalidate_inode_pages2(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping)
:   remove all pages from an address_space

**Parameters**

`struct address_space *mapping`
:   the address_space

**Description**

Any pages which are found to be mapped into pagetables are unmapped prior to
invalidation.

**Return**

-EBUSY if any pages could not be invalidated.

void truncate_pagecache(struct [inode](mm-api.md#c.truncate_pagecache "inode") \*inode, loff_t newsize)
:   unmap and remove pagecache that has been truncated

**Parameters**

`struct inode *inode`
:   inode

`loff_t newsize`
:   new file size

**Description**

inode's new i_size must already be written before truncate_pagecache
is called.

This function should typically be called before the filesystem
releases resources associated with the freed range (eg. deallocates
blocks). This way, pagecache will always stay logically coherent
with on-disk format, and the filesystem would not have to deal with
situations such as writepage being called for a page that has already
had its underlying blocks deallocated.

void truncate_setsize(struct [inode](mm-api.md#c.truncate_setsize "inode") \*inode, loff_t newsize)
:   update inode and pagecache for a new file size

**Parameters**

`struct inode *inode`
:   inode

`loff_t newsize`
:   new file size

**Description**

truncate_setsize updates i_size and performs pagecache truncation (if
necessary) to **newsize**. It will be typically be called from the filesystem's
setattr function when ATTR_SIZE is passed in.

Must be called with a lock serializing truncates and writes (generally
i_rwsem but e.g. xfs uses a different lock) and before all filesystem
specific block truncation has been performed.

void pagecache_isize_extended(struct [inode](mm-api.md#c.pagecache_isize_extended "inode") \*inode, loff_t from, loff_t to)
:   update pagecache after extension of i_size

**Parameters**

`struct inode *inode`
:   inode for which i_size was extended

`loff_t from`
:   original inode size

`loff_t to`
:   new inode size

**Description**

Handle extension of inode size either caused by extending truncate or by
write starting after current i_size. We mark the page straddling current
i_size RO so that page_mkwrite() is called on the nearest write access to
the page. This way filesystem can be sure that page_mkwrite() is called on
the page before user writes to the page via mmap after the i_size has been
changed.

The function must be called after i_size is updated so that page fault
coming after we unlock the page will already see the new i_size.
The function must be called while we still hold i_rwsem - this not only
makes sure i_size is stable but also that userspace cannot observe new
i_size value before we are prepared to store mmap writes at new inode size.

void truncate_pagecache_range(struct [inode](mm-api.md#c.truncate_pagecache_range "inode") \*inode, loff_t lstart, loff_t lend)
:   unmap and remove pagecache that is hole-punched

**Parameters**

`struct inode *inode`
:   inode

`loff_t lstart`
:   offset of beginning of hole

`loff_t lend`
:   offset of last byte of hole

**Description**

This function should typically be called before the filesystem
releases resources associated with the freed range (eg. deallocates
blocks). This way, pagecache will always stay logically coherent
with on-disk format, and the filesystem would not have to deal with
situations such as writepage being called for a page that has already
had its underlying blocks deallocated.

void filemap_set_wb_err(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, int err)
:   set a writeback error on an address_space

**Parameters**

`struct address_space *mapping`
:   mapping in which to set writeback error

`int err`
:   error to be set in mapping

**Description**

When writeback fails in some way, we must record that error so that
userspace can be informed when fsync and the like are called. We endeavor
to report errors on any file that was open at the time of the error. Some
internal callers also need to know when writeback errors have occurred.

When a writeback error occurs, most filesystems will want to call
filemap_set_wb_err to record the error in the mapping so that it will be
automatically reported whenever fsync is called on the file.

int filemap_check_wb_err(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, errseq_t since)
:   has an error occurred since the mark was sampled?

**Parameters**

`struct address_space *mapping`
:   mapping to check for writeback errors

`errseq_t since`
:   previously-sampled errseq_t

**Description**

Grab the errseq_t value from the mapping, and see if it has changed "since"
the given value was sampled.

If it has then report the latest error set, otherwise return 0.

errseq_t filemap_sample_wb_err(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping)
:   sample the current errseq_t to test for later errors

**Parameters**

`struct address_space *mapping`
:   mapping to be sampled

**Description**

Writeback errors are always reported relative to a particular sample point
in the past. This function provides those sample points.

errseq_t file_sample_sb_err(struct [file](mm-api.md#c.file_sample_sb_err "file") \*file)
:   sample the current errseq_t to test for later errors

**Parameters**

`struct file *file`
:   file pointer to be sampled

**Description**

Grab the most current superblock-level errseq_t value for the given
struct file.

void mapping_set_error(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, int error)
:   record a writeback error in the address_space

**Parameters**

`struct address_space *mapping`
:   the mapping in which an error should be set

`int error`
:   the error to set in the mapping

**Description**

When writeback fails in some way, we must record that error so that
userspace can be informed when fsync and the like are called. We endeavor
to report errors on any file that was open at the time of the error. Some
internal callers also need to know when writeback errors have occurred.

When a writeback error occurs, most filesystems will want to call
mapping_set_error to record the error in the mapping so that it can be
reported when the application calls fsync(2).

void mapping_set_large_folios(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping)
:   Indicate the file supports large folios.

**Parameters**

`struct address_space *mapping`
:   The file.

**Description**

The filesystem should call this function in its inode constructor to
indicate that the VFS can use large folios to cache the contents of
the file.

**Context**

This should not be called while the inode is active as it
is non-atomic.

struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*folio_file_mapping(struct [folio](mm-api.md#c.folio_file_mapping "folio") \*folio)
:   Find the mapping this folio belongs to.

**Parameters**

`struct folio *folio`
:   The folio.

**Description**

For folios which are in the page cache, return the mapping that this
page belongs to. Folios in the swap cache return the mapping of the
swap file or swap device where the data is stored. This is different
from the mapping returned by [`folio_mapping()`](mm-api.md#c.folio_mapping "folio_mapping"). The only reason to
use it is if, like NFS, you return 0 from ->activate_swapfile.

Do not call this for folios which aren't in the page cache or swap cache.

struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*folio_flush_mapping(struct [folio](mm-api.md#c.folio_flush_mapping "folio") \*folio)
:   Find the file mapping this folio belongs to.

**Parameters**

`struct folio *folio`
:   The folio.

**Description**

For folios which are in the page cache, return the mapping that this
page belongs to. Anonymous folios return NULL, even if they're in
the swap cache. Other kinds of folio also return NULL.

This is ONLY used by architecture cache flushing code. If you aren't
writing cache flushing code, you want either [`folio_mapping()`](mm-api.md#c.folio_mapping "folio_mapping") or
[`folio_file_mapping()`](mm-api.md#c.folio_file_mapping "folio_file_mapping").

struct inode \*folio_inode(struct [folio](mm-api.md#c.folio_inode "folio") \*folio)
:   Get the host inode for this folio.

**Parameters**

`struct folio *folio`
:   The folio.

**Description**

For folios which are in the page cache, return the inode that this folio
belongs to.

Do not call this for folios which aren't in the page cache.

void folio_attach_private(struct [folio](mm-api.md#c.folio_attach_private "folio") \*folio, void \*data)
:   Attach private data to a folio.

**Parameters**

`struct folio *folio`
:   Folio to attach data to.

`void *data`
:   Data to attach to folio.

**Description**

Attaching private data to a folio increments the page's reference count.
The data must be detached before the folio will be freed.

void \*folio_change_private(struct [folio](mm-api.md#c.folio_change_private "folio") \*folio, void \*data)
:   Change private data on a folio.

**Parameters**

`struct folio *folio`
:   Folio to change the data on.

`void *data`
:   Data to set on the folio.

**Description**

Change the private data attached to a folio and return the old
data. The page must previously have had data attached and the data
must be detached before the folio will be freed.

**Return**

Data that was previously attached to the folio.

void \*folio_detach_private(struct [folio](mm-api.md#c.folio_detach_private "folio") \*folio)
:   Detach private data from a folio.

**Parameters**

`struct folio *folio`
:   Folio to detach data from.

**Description**

Removes the data that was previously attached to the folio and decrements
the refcount on the page.

**Return**

Data that was attached to the folio.

type fgf_t
:   Flags for getting folios from the page cache.

**Description**

Most users of the page cache will not need to use these flags;
there are convenience functions such as [`filemap_get_folio()`](mm-api.md#c.filemap_get_folio "filemap_get_folio") and
[`filemap_lock_folio()`](mm-api.md#c.filemap_lock_folio "filemap_lock_folio"). For users which need more control over exactly
what is done with the folios, these flags to [`__filemap_get_folio()`](mm-api.md#c.__filemap_get_folio "__filemap_get_folio")
are available.

- `FGP_ACCESSED` - The folio will be marked accessed.
- `FGP_LOCK` - The folio is returned locked.
- `FGP_CREAT` - If no folio is present then a new folio is allocated,
  added to the page cache and the VM's LRU list. The folio is
  returned locked.
- `FGP_FOR_MMAP` - The caller wants to do its own locking dance if the
  folio is already in cache. If the folio was allocated, unlock it
  before returning so the caller can do the same dance.
- `FGP_WRITE` - The folio will be written to by the caller.
- `FGP_NOFS` - __GFP_FS will get cleared in gfp.
- `FGP_NOWAIT` - Don't block on the folio lock.
- `FGP_STABLE` - Wait for the folio to be stable (finished writeback)
- `FGP_WRITEBEGIN` - The flags to use in a filesystem write_begin()
  implementation.

[fgf_t](mm-api.md#c.fgf_t "fgf_t") fgf_set_order(size_t size)
:   Encode a length in the fgf_t flags.

**Parameters**

`size_t size`
:   The suggested size of the folio to create.

**Description**

The caller of [`__filemap_get_folio()`](mm-api.md#c.__filemap_get_folio "__filemap_get_folio") can use this to suggest a preferred
size for the folio that is created. If there is already a folio at
the index, it will be returned, no matter what its size. If a folio
is freshly created, it may be of a different size than requested
due to alignment constraints, memory pressure, or the presence of
other folios at nearby indices.

struct [folio](mm-api.md#c.folio "folio") \*filemap_get_folio(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, pgoff_t index)
:   Find and get a folio.

**Parameters**

`struct address_space *mapping`
:   The address_space to search.

`pgoff_t index`
:   The page index.

**Description**

Looks up the page cache entry at **mapping** & **index**. If a folio is
present, it is returned with an increased refcount.

**Return**

A folio or ERR_PTR(-ENOENT) if there is no folio in the cache for
this index. Will not return a shadow, swap or DAX entry.

struct [folio](mm-api.md#c.folio "folio") \*filemap_lock_folio(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, pgoff_t index)
:   Find and lock a folio.

**Parameters**

`struct address_space *mapping`
:   The address_space to search.

`pgoff_t index`
:   The page index.

**Description**

Looks up the page cache entry at **mapping** & **index**. If a folio is
present, it is returned locked with an increased refcount.

**Context**

May sleep.

**Return**

A folio or ERR_PTR(-ENOENT) if there is no folio in the cache for
this index. Will not return a shadow, swap or DAX entry.

struct [folio](mm-api.md#c.folio "folio") \*filemap_grab_folio(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, pgoff_t index)
:   grab a folio from the page cache

**Parameters**

`struct address_space *mapping`
:   The address space to search

`pgoff_t index`
:   The page index

**Description**

Looks up the page cache entry at **mapping** & **index**. If no folio is found,
a new folio is created. The folio is locked, marked as accessed, and
returned.

**Return**

A found or created folio. ERR_PTR(-ENOMEM) if no folio is found
and failed to create a folio.

struct page \*find_get_page(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, pgoff_t offset)
:   find and get a page reference

**Parameters**

`struct address_space *mapping`
:   the address_space to search

`pgoff_t offset`
:   the page index

**Description**

Looks up the page cache slot at **mapping** & **offset**. If there is a
page cache page, it is returned with an increased refcount.

Otherwise, `NULL` is returned.

struct page \*find_lock_page(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, pgoff_t index)
:   locate, pin and lock a pagecache page

**Parameters**

`struct address_space *mapping`
:   the address_space to search

`pgoff_t index`
:   the page index

**Description**

Looks up the page cache entry at **mapping** & **index**. If there is a
page cache page, it is returned locked and with an increased
refcount.

**Context**

May sleep.

**Return**

A struct page or `NULL` if there is no page in the cache for this
index.

struct page \*find_or_create_page(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, pgoff_t index, gfp_t gfp_mask)
:   locate or add a pagecache page

**Parameters**

`struct address_space *mapping`
:   the page's address_space

`pgoff_t index`
:   the page's index into the mapping

`gfp_t gfp_mask`
:   page allocation mode

**Description**

Looks up the page cache slot at **mapping** & **offset**. If there is a
page cache page, it is returned locked and with an increased
refcount.

If the page is not present, a new page is allocated using **gfp_mask**
and added to the page cache and the VM's LRU list. The page is
returned locked and with an increased refcount.

On memory exhaustion, `NULL` is returned.

[`find_or_create_page()`](mm-api.md#c.find_or_create_page "find_or_create_page") may sleep, even if **gfp_flags** specifies an
atomic allocation!

struct page \*grab_cache_page_nowait(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, pgoff_t index)
:   returns locked page at given index in given cache

**Parameters**

`struct address_space *mapping`
:   target address_space

`pgoff_t index`
:   the page index

**Description**

Same as grab_cache_page(), but do not wait if the page is unavailable.
This is intended for speculative data generators, where the data can
be regenerated if the page couldn't be grabbed. This routine should
be safe to call while holding the lock for another page.

Clear __GFP_FS when allocating the page to avoid recursion into the fs
and deadlock against the caller's locked page.

pgoff_t folio_index(struct [folio](mm-api.md#c.folio_index "folio") \*folio)
:   File index of a folio.

**Parameters**

`struct folio *folio`
:   The folio.

**Description**

For a folio which is either in the page cache or the swap cache,
return its index within the address_space it belongs to. If you know
the page is definitely in the page cache, you can look at the folio's
index directly.

**Return**

The index (offset in units of pages) of a folio in its file.

pgoff_t folio_next_index(struct [folio](mm-api.md#c.folio_next_index "folio") \*folio)
:   Get the index of the next folio.

**Parameters**

`struct folio *folio`
:   The current folio.

**Return**

The index of the folio which follows this folio in the file.

struct page \*folio_file_page(struct [folio](mm-api.md#c.folio_file_page "folio") \*folio, pgoff_t index)
:   The page for a particular index.

**Parameters**

`struct folio *folio`
:   The folio which contains this index.

`pgoff_t index`
:   The index we want to look up.

**Description**

Sometimes after looking up a folio in the page cache, we need to
obtain the specific page for an index (eg a page fault).

**Return**

The page containing the file data for this index.

bool folio_contains(struct [folio](mm-api.md#c.folio_contains "folio") \*folio, pgoff_t index)
:   Does this folio contain this index?

**Parameters**

`struct folio *folio`
:   The folio.

`pgoff_t index`
:   The page index within the file.

**Context**

The caller should have the page locked in order to prevent
(eg) shmem from moving the page between the page cache and swap cache
and changing its index in the middle of the operation.

**Return**

true or false.

loff_t folio_pos(struct [folio](mm-api.md#c.folio_pos "folio") \*folio)
:   Returns the byte position of this folio in its file.

**Parameters**

`struct folio *folio`
:   The folio.

loff_t folio_file_pos(struct [folio](mm-api.md#c.folio_file_pos "folio") \*folio)
:   Returns the byte position of this folio in its file.

**Parameters**

`struct folio *folio`
:   The folio.

**Description**

This differs from [`folio_pos()`](mm-api.md#c.folio_pos "folio_pos") for folios which belong to a swap file.
NFS is the only filesystem today which needs to use [`folio_file_pos()`](mm-api.md#c.folio_file_pos "folio_file_pos").

bool folio_trylock(struct [folio](mm-api.md#c.folio_trylock "folio") \*folio)
:   Attempt to lock a folio.

**Parameters**

`struct folio *folio`
:   The folio to attempt to lock.

**Description**

Sometimes it is undesirable to wait for a folio to be unlocked (eg
when the locks are being taken in the wrong order, or if making
progress through a batch of folios is more important than processing
them in order). Usually [`folio_lock()`](mm-api.md#c.folio_lock "folio_lock") is the correct function to call.

**Context**

Any context.

**Return**

Whether the lock was successfully acquired.

void folio_lock(struct [folio](mm-api.md#c.folio_lock "folio") \*folio)
:   Lock this folio.

**Parameters**

`struct folio *folio`
:   The folio to lock.

**Description**

The folio lock protects against many things, probably more than it
should. It is primarily held while a folio is being brought uptodate,
either from its backing file or from swap. It is also held while a
folio is being truncated from its address_space, so holding the lock
is sufficient to keep folio->mapping stable.

The folio lock is also held while write() is modifying the page to
provide POSIX atomicity guarantees (as long as the write does not
cross a page boundary). Other modifications to the data in the folio
do not hold the folio lock and can race with writes, eg DMA and stores
to mapped pages.

**Context**

May sleep. If you need to acquire the locks of two or
more folios, they must be in order of ascending index, if they are
in the same address_space. If they are in different address_spaces,
acquire the lock of the folio which belongs to the address_space which
has the lowest address in memory first.

void lock_page(struct [page](mm-api.md#c.lock_page "page") \*page)
:   Lock the folio containing this page.

**Parameters**

`struct page *page`
:   The page to lock.

**Description**

See [`folio_lock()`](mm-api.md#c.folio_lock "folio_lock") for a description of what the lock protects.
This is a legacy function and new code should probably use [`folio_lock()`](mm-api.md#c.folio_lock "folio_lock")
instead.

**Context**

May sleep. Pages in the same folio share a lock, so do not
attempt to lock two pages which share a folio.

int folio_lock_killable(struct [folio](mm-api.md#c.folio_lock_killable "folio") \*folio)
:   Lock this folio, interruptible by a fatal signal.

**Parameters**

`struct folio *folio`
:   The folio to lock.

**Description**

Attempts to lock the folio, like [`folio_lock()`](mm-api.md#c.folio_lock "folio_lock"), except that the sleep
to acquire the lock is interruptible by a fatal signal.

**Context**

May sleep; see [`folio_lock()`](mm-api.md#c.folio_lock "folio_lock").

**Return**

0 if the lock was acquired; -EINTR if a fatal signal was received.

bool filemap_range_needs_writeback(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, loff_t start_byte, loff_t end_byte)
:   check if range potentially needs writeback

**Parameters**

`struct address_space *mapping`
:   address space within which to check

`loff_t start_byte`
:   offset in bytes where the range starts

`loff_t end_byte`
:   offset in bytes where the range ends (inclusive)

**Description**

Find at least one page in the range supplied, usually used to check if
direct writing in this range will trigger a writeback. Used by O_DIRECT
read/write with IOCB_NOWAIT, to see if the caller needs to do
[`filemap_write_and_wait_range()`](mm-api.md#c.filemap_write_and_wait_range "filemap_write_and_wait_range") before proceeding.

**Return**

`true` if the caller should do [`filemap_write_and_wait_range()`](mm-api.md#c.filemap_write_and_wait_range "filemap_write_and_wait_range") before
doing O_DIRECT to a page in this range, `false` otherwise.

struct readahead_control
:   Describes a readahead request.

**Definition**:

```
struct readahead_control {
    struct file *file;
    struct address_space *mapping;
    struct file_ra_state *ra;
};
```

**Members**

`file`
:   The file, used primarily by network filesystems for authentication.
    May be NULL if invoked internally by the filesystem.

`mapping`
:   Readahead this filesystem object.

`ra`
:   File readahead state. May be NULL.

**Description**

A readahead request is for consecutive pages. Filesystems which
implement the ->readahead method should call [`readahead_page()`](mm-api.md#c.readahead_page "readahead_page") or
[`readahead_page_batch()`](mm-api.md#c.readahead_page_batch "readahead_page_batch") in a loop and attempt to start I/O against
each page in the request.

Most of the fields in this struct are private and should be accessed
by the functions below.

void page_cache_sync_readahead(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, struct [file_ra_state](../filesystems/api-summary.md#c.file_ra_state "file_ra_state") \*ra, struct [file](mm-api.md#c.page_cache_sync_readahead "file") \*file, pgoff_t index, unsigned long req_count)
:   generic file readahead

**Parameters**

`struct address_space *mapping`
:   address_space which holds the pagecache and I/O vectors

`struct file_ra_state *ra`
:   file_ra_state which holds the readahead state

`struct file *file`
:   Used by the filesystem for authentication.

`pgoff_t index`
:   Index of first page to be read.

`unsigned long req_count`
:   Total number of pages being read by the caller.

**Description**

[`page_cache_sync_readahead()`](mm-api.md#c.page_cache_sync_readahead "page_cache_sync_readahead") should be called when a cache miss happened:
it will submit the read. The readahead logic may decide to piggyback more
pages onto the read request if access patterns suggest it will improve
performance.

void page_cache_async_readahead(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, struct [file_ra_state](../filesystems/api-summary.md#c.file_ra_state "file_ra_state") \*ra, struct [file](mm-api.md#c.page_cache_async_readahead "file") \*file, struct [folio](mm-api.md#c.page_cache_async_readahead "folio") \*folio, pgoff_t index, unsigned long req_count)
:   file readahead for marked pages

**Parameters**

`struct address_space *mapping`
:   address_space which holds the pagecache and I/O vectors

`struct file_ra_state *ra`
:   file_ra_state which holds the readahead state

`struct file *file`
:   Used by the filesystem for authentication.

`struct folio *folio`
:   The folio at **index** which triggered the readahead call.

`pgoff_t index`
:   Index of first page to be read.

`unsigned long req_count`
:   Total number of pages being read by the caller.

**Description**

[`page_cache_async_readahead()`](mm-api.md#c.page_cache_async_readahead "page_cache_async_readahead") should be called when a page is used which
is marked as PageReadahead; this is a marker to suggest that the application
has used up enough of the readahead window that we should start pulling in
more pages.

struct page \*readahead_page(struct [readahead_control](mm-api.md#c.readahead_control "readahead_control") \*ractl)
:   Get the next page to read.

**Parameters**

`struct readahead_control *ractl`
:   The current readahead request.

**Context**

The page is locked and has an elevated refcount. The caller
should decreases the refcount once the page has been submitted for I/O
and unlock the page once all I/O to that page has completed.

**Return**

A pointer to the next page, or `NULL` if we are done.

struct [folio](mm-api.md#c.folio "folio") \*readahead_folio(struct [readahead_control](mm-api.md#c.readahead_control "readahead_control") \*ractl)
:   Get the next folio to read.

**Parameters**

`struct readahead_control *ractl`
:   The current readahead request.

**Context**

The folio is locked. The caller should unlock the folio once
all I/O to that folio has completed.

**Return**

A pointer to the next folio, or `NULL` if we are done.

readahead_page_batch

`readahead_page_batch (rac, array)`

> Get a batch of pages to read.

**Parameters**

`rac`
:   The current readahead request.

`array`
:   An array of pointers to struct page.

**Context**

The pages are locked and have an elevated refcount. The caller
should decreases the refcount once the page has been submitted for I/O
and unlock the page once all I/O to that page has completed.

**Return**

The number of pages placed in the array. 0 indicates the request
is complete.

loff_t readahead_pos(struct [readahead_control](mm-api.md#c.readahead_control "readahead_control") \*rac)
:   The byte offset into the file of this readahead request.

**Parameters**

`struct readahead_control *rac`
:   The readahead request.

size_t readahead_length(struct [readahead_control](mm-api.md#c.readahead_control "readahead_control") \*rac)
:   The number of bytes in this readahead request.

**Parameters**

`struct readahead_control *rac`
:   The readahead request.

pgoff_t readahead_index(struct [readahead_control](mm-api.md#c.readahead_control "readahead_control") \*rac)
:   The index of the first page in this readahead request.

**Parameters**

`struct readahead_control *rac`
:   The readahead request.

unsigned int readahead_count(struct [readahead_control](mm-api.md#c.readahead_control "readahead_control") \*rac)
:   The number of pages in this readahead request.

**Parameters**

`struct readahead_control *rac`
:   The readahead request.

size_t readahead_batch_length(struct [readahead_control](mm-api.md#c.readahead_control "readahead_control") \*rac)
:   The number of bytes in the current batch.

**Parameters**

`struct readahead_control *rac`
:   The readahead request.

ssize_t folio_mkwrite_check_truncate(struct [folio](mm-api.md#c.folio_mkwrite_check_truncate "folio") \*folio, struct [inode](mm-api.md#c.folio_mkwrite_check_truncate "inode") \*inode)
:   check if folio was truncated

**Parameters**

`struct folio *folio`
:   the folio to check

`struct inode *inode`
:   the inode to check the folio against

**Return**

the number of bytes in the folio up to EOF,
or -EFAULT if the folio was truncated.

int page_mkwrite_check_truncate(struct [page](mm-api.md#c.page_mkwrite_check_truncate "page") \*page, struct [inode](mm-api.md#c.page_mkwrite_check_truncate "inode") \*inode)
:   check if page was truncated

**Parameters**

`struct page *page`
:   the page to check

`struct inode *inode`
:   the inode to check the page against

**Description**

Returns the number of bytes in the page up to EOF,
or -EFAULT if the page was truncated.

unsigned int i_blocks_per_folio(struct [inode](mm-api.md#c.i_blocks_per_folio "inode") \*inode, struct [folio](mm-api.md#c.i_blocks_per_folio "folio") \*folio)
:   How many blocks fit in this folio.

**Parameters**

`struct inode *inode`
:   The inode which contains the blocks.

`struct folio *folio`
:   The folio.

**Description**

If the block size is larger than the size of this folio, return zero.

**Context**

The caller should hold a refcount on the folio to prevent it
from being split.

**Return**

The number of filesystem blocks covered by this folio.

## Memory pools

void mempool_exit(mempool_t \*pool)
:   exit a mempool initialized with [`mempool_init()`](mm-api.md#c.mempool_init "mempool_init")

**Parameters**

`mempool_t *pool`
:   pointer to the memory pool which was initialized with
    [`mempool_init()`](mm-api.md#c.mempool_init "mempool_init").

**Description**

Free all reserved elements in **pool** and **pool** itself. This function
only sleeps if the free_fn() function sleeps.

May be called on a zeroed but uninitialized mempool (i.e. allocated with
[`kzalloc()`](mm-api.md#c.kzalloc "kzalloc")).

void mempool_destroy(mempool_t \*pool)
:   deallocate a memory pool

**Parameters**

`mempool_t *pool`
:   pointer to the memory pool which was allocated via
    [`mempool_create()`](mm-api.md#c.mempool_create "mempool_create").

**Description**

Free all reserved elements in **pool** and **pool** itself. This function
only sleeps if the free_fn() function sleeps.

int mempool_init(mempool_t \*pool, int min_nr, mempool_alloc_t \*alloc_fn, mempool_free_t \*free_fn, void \*pool_data)
:   initialize a memory pool

**Parameters**

`mempool_t *pool`
:   pointer to the memory pool that should be initialized

`int min_nr`
:   the minimum number of elements guaranteed to be
    allocated for this pool.

`mempool_alloc_t *alloc_fn`
:   user-defined element-allocation function.

`mempool_free_t *free_fn`
:   user-defined element-freeing function.

`void *pool_data`
:   optional private data available to the user-defined functions.

**Description**

Like [`mempool_create()`](mm-api.md#c.mempool_create "mempool_create"), but initializes the pool in (i.e. embedded in another
structure).

**Return**

`0` on success, negative error code otherwise.

mempool_t \*mempool_create(int min_nr, mempool_alloc_t \*alloc_fn, mempool_free_t \*free_fn, void \*pool_data)
:   create a memory pool

**Parameters**

`int min_nr`
:   the minimum number of elements guaranteed to be
    allocated for this pool.

`mempool_alloc_t *alloc_fn`
:   user-defined element-allocation function.

`mempool_free_t *free_fn`
:   user-defined element-freeing function.

`void *pool_data`
:   optional private data available to the user-defined functions.

**Description**

this function creates and allocates a guaranteed size, preallocated
memory pool. The pool can be used from the [`mempool_alloc()`](mm-api.md#c.mempool_alloc "mempool_alloc") and [`mempool_free()`](mm-api.md#c.mempool_free "mempool_free")
functions. This function might sleep. Both the alloc_fn() and the free_fn()
functions might sleep - as long as the [`mempool_alloc()`](mm-api.md#c.mempool_alloc "mempool_alloc") function is not called
from IRQ contexts.

**Return**

pointer to the created memory pool object or `NULL` on error.

int mempool_resize(mempool_t \*pool, int new_min_nr)
:   resize an existing memory pool

**Parameters**

`mempool_t *pool`
:   pointer to the memory pool which was allocated via
    [`mempool_create()`](mm-api.md#c.mempool_create "mempool_create").

`int new_min_nr`
:   the new minimum number of elements guaranteed to be
    allocated for this pool.

**Description**

This function shrinks/grows the pool. In the case of growing,
it cannot be guaranteed that the pool will be grown to the new
size immediately, but new [`mempool_free()`](mm-api.md#c.mempool_free "mempool_free") calls will refill it.
This function may sleep.

Note, the caller must guarantee that no mempool_destroy is called
while this function is running. [`mempool_alloc()`](mm-api.md#c.mempool_alloc "mempool_alloc") & [`mempool_free()`](mm-api.md#c.mempool_free "mempool_free")
might be called (eg. from IRQ contexts) while this function executes.

**Return**

`0` on success, negative error code otherwise.

void \*mempool_alloc(mempool_t \*pool, gfp_t gfp_mask)
:   allocate an element from a specific memory pool

**Parameters**

`mempool_t *pool`
:   pointer to the memory pool which was allocated via
    [`mempool_create()`](mm-api.md#c.mempool_create "mempool_create").

`gfp_t gfp_mask`
:   the usual allocation bitmask.

**Description**

this function only sleeps if the alloc_fn() function sleeps or
returns NULL. Note that due to preallocation, this function
*never* fails when called from process contexts. (it might
fail if called from an IRQ context.)

**Note**

using __GFP_ZERO is not supported.

**Return**

pointer to the allocated element or `NULL` on error.

void \*mempool_alloc_preallocated(mempool_t \*pool)
:   allocate an element from preallocated elements belonging to a specific memory pool

**Parameters**

`mempool_t *pool`
:   pointer to the memory pool which was allocated via
    [`mempool_create()`](mm-api.md#c.mempool_create "mempool_create").

**Description**

This function is similar to mempool_alloc, but it only attempts allocating
an element from the preallocated elements. It does not sleep and immediately
returns if no preallocated elements are available.

**Return**

pointer to the allocated element or `NULL` if no elements are
available.

void mempool_free(void \*element, mempool_t \*pool)
:   return an element to the pool.

**Parameters**

`void *element`
:   pool element pointer.

`mempool_t *pool`
:   pointer to the memory pool which was allocated via
    [`mempool_create()`](mm-api.md#c.mempool_create "mempool_create").

**Description**

this function only sleeps if the free_fn() function sleeps.

## DMA pools

struct dma_pool \*dma_pool_create(const char \*name, struct [device](../driver-api/infrastructure.md#c.device "device") \*dev, size_t size, size_t align, size_t boundary)
:   Creates a pool of consistent memory blocks, for dma.

**Parameters**

`const char *name`
:   name of pool, for diagnostics

`struct device *dev`
:   device that will be doing the DMA

`size_t size`
:   size of the blocks in this pool.

`size_t align`
:   alignment requirement for blocks; must be a power of two

`size_t boundary`
:   returned blocks won't cross this power of two boundary

**Context**

not in_interrupt()

**Description**

Given one of these pools, [`dma_pool_alloc()`](mm-api.md#c.dma_pool_alloc "dma_pool_alloc")
may be used to allocate memory. Such memory will all have "consistent"
DMA mappings, accessible by the device and its driver without using
cache flushing primitives. The actual size of blocks allocated may be
larger than requested because of alignment.

If **boundary** is nonzero, objects returned from [`dma_pool_alloc()`](mm-api.md#c.dma_pool_alloc "dma_pool_alloc") won't
cross that size boundary. This is useful for devices which have
addressing restrictions on individual DMA transfers, such as not crossing
boundaries of 4KBytes.

**Return**

a dma allocation pool with the requested characteristics, or
`NULL` if one can't be created.

void dma_pool_destroy(struct dma_pool \*pool)
:   destroys a pool of dma memory blocks.

**Parameters**

`struct dma_pool *pool`
:   dma pool that will be destroyed

**Context**

!in_interrupt()

**Description**

Caller guarantees that no more memory from the pool is in use,
and that nothing will try to use the pool after this call.

void \*dma_pool_alloc(struct dma_pool \*pool, gfp_t mem_flags, dma_addr_t \*handle)
:   get a block of consistent memory

**Parameters**

`struct dma_pool *pool`
:   dma pool that will produce the block

`gfp_t mem_flags`
:   GFP_\* bitmask

`dma_addr_t *handle`
:   pointer to dma address of block

**Return**

the kernel virtual address of a currently unused block,
and reports its dma address through the handle.
If such a memory block can't be allocated, `NULL` is returned.

void dma_pool_free(struct dma_pool \*pool, void \*vaddr, dma_addr_t dma)
:   put block back into dma pool

**Parameters**

`struct dma_pool *pool`
:   the dma pool holding the block

`void *vaddr`
:   virtual address of block

`dma_addr_t dma`
:   dma address of block

**Description**

Caller promises neither device nor driver will again touch this block
unless it is first re-allocated.

struct dma_pool \*dmam_pool_create(const char \*name, struct [device](../driver-api/infrastructure.md#c.device "device") \*dev, size_t size, size_t align, size_t allocation)
:   Managed [`dma_pool_create()`](mm-api.md#c.dma_pool_create "dma_pool_create")

**Parameters**

`const char *name`
:   name of pool, for diagnostics

`struct device *dev`
:   device that will be doing the DMA

`size_t size`
:   size of the blocks in this pool.

`size_t align`
:   alignment requirement for blocks; must be a power of two

`size_t allocation`
:   returned blocks won't cross this boundary (or zero)

**Description**

Managed [`dma_pool_create()`](mm-api.md#c.dma_pool_create "dma_pool_create"). DMA pool created with this function is
automatically destroyed on driver detach.

**Return**

a managed dma allocation pool with the requested
characteristics, or `NULL` if one can't be created.

void dmam_pool_destroy(struct dma_pool \*pool)
:   Managed [`dma_pool_destroy()`](mm-api.md#c.dma_pool_destroy "dma_pool_destroy")

**Parameters**

`struct dma_pool *pool`
:   dma pool that will be destroyed

**Description**

Managed [`dma_pool_destroy()`](mm-api.md#c.dma_pool_destroy "dma_pool_destroy").

## More Memory Management Functions

void zap_vma_ptes(struct vm_area_struct \*vma, unsigned long address, unsigned long size)
:   remove ptes mapping the vma

**Parameters**

`struct vm_area_struct *vma`
:   vm_area_struct holding ptes to be zapped

`unsigned long address`
:   starting address of pages to zap

`unsigned long size`
:   number of bytes to zap

**Description**

This function only unmaps ptes assigned to VM_PFNMAP vmas.

The entire address range must be fully contained within the vma.

int vm_insert_pages(struct vm_area_struct \*vma, unsigned long addr, struct page \*\*pages, unsigned long \*num)
:   insert multiple pages into user vma, batching the pmd lock.

**Parameters**

`struct vm_area_struct *vma`
:   user vma to map to

`unsigned long addr`
:   target start user address of these pages

`struct page **pages`
:   source kernel pages

`unsigned long *num`
:   in: number of pages to map. out: number of pages that were *not*
    mapped. (0 means all pages were successfully mapped).

**Description**

Preferred over [`vm_insert_page()`](mm-api.md#c.vm_insert_page "vm_insert_page") when inserting multiple pages.

In case of error, we may have mapped a subset of the provided
pages. It is the caller's responsibility to account for this case.

The same restrictions apply as in [`vm_insert_page()`](mm-api.md#c.vm_insert_page "vm_insert_page").

int vm_insert_page(struct vm_area_struct \*vma, unsigned long addr, struct [page](mm-api.md#c.vm_insert_page "page") \*page)
:   insert single page into user vma

**Parameters**

`struct vm_area_struct *vma`
:   user vma to map to

`unsigned long addr`
:   target user address of this page

`struct page *page`
:   source kernel page

**Description**

This allows drivers to insert individual pages they've allocated
into a user vma.

The page has to be a nice clean _individual_ kernel allocation.
If you allocate a compound page, you need to have marked it as
such (__GFP_COMP), or manually just split the page up yourself
(see split_page()).

NOTE! Traditionally this was done with "[`remap_pfn_range()`](mm-api.md#c.remap_pfn_range "remap_pfn_range")" which
took an arbitrary page protection parameter. This doesn't allow
that. Your vma protection will have to be set up correctly, which
means that if you want a shared writable mapping, you'd better
ask for a shared writable mapping!

The page does not need to be reserved.

Usually this function is called from f_op->mmap() handler
under mm->mmap_lock write-lock, so it can change vma->vm_flags.
Caller must set VM_MIXEDMAP on vma if it wants to call this
function from other places, for example from page-fault handler.

**Return**

`0` on success, negative error code otherwise.

int vm_map_pages(struct vm_area_struct \*vma, struct page \*\*pages, unsigned long num)
:   maps range of kernel pages starts with non zero offset

**Parameters**

`struct vm_area_struct *vma`
:   user vma to map to

`struct page **pages`
:   pointer to array of source kernel pages

`unsigned long num`
:   number of pages in page array

**Description**

Maps an object consisting of **num** pages, catering for the user's
requested vm_pgoff

If we fail to insert any page into the vma, the function will return
immediately leaving any previously inserted pages present. Callers
from the mmap handler may immediately return the error as their caller
will destroy the vma, removing any successfully inserted pages. Other
callers should make their own arrangements for calling unmap_region().

**Context**

Process context. Called by mmap handlers.

**Return**

0 on success and error code otherwise.

int vm_map_pages_zero(struct vm_area_struct \*vma, struct page \*\*pages, unsigned long num)
:   map range of kernel pages starts with zero offset

**Parameters**

`struct vm_area_struct *vma`
:   user vma to map to

`struct page **pages`
:   pointer to array of source kernel pages

`unsigned long num`
:   number of pages in page array

**Description**

Similar to [`vm_map_pages()`](mm-api.md#c.vm_map_pages "vm_map_pages"), except that it explicitly sets the offset
to 0. This function is intended for the drivers that did not consider
vm_pgoff.

**Context**

Process context. Called by mmap handlers.

**Return**

0 on success and error code otherwise.

[vm_fault_t](mm-api.md#c.vm_fault_t "vm_fault_t") vmf_insert_pfn_prot(struct vm_area_struct \*vma, unsigned long addr, unsigned long pfn, pgprot_t pgprot)
:   insert single pfn into user vma with specified pgprot

**Parameters**

`struct vm_area_struct *vma`
:   user vma to map to

`unsigned long addr`
:   target user address of this page

`unsigned long pfn`
:   source kernel pfn

`pgprot_t pgprot`
:   pgprot flags for the inserted page

**Description**

This is exactly like [`vmf_insert_pfn()`](mm-api.md#c.vmf_insert_pfn "vmf_insert_pfn"), except that it allows drivers
to override pgprot on a per-page basis.

This only makes sense for IO mappings, and it makes no sense for
COW mappings. In general, using multiple vmas is preferable;
vmf_insert_pfn_prot should only be used if using multiple VMAs is
impractical.

pgprot typically only differs from **vma->vm_page_prot** when drivers set
caching- and encryption bits different than those of **vma->vm_page_prot**,
because the caching- or encryption mode may not be known at mmap() time.

This is ok as long as **vma->vm_page_prot** is not used by the core vm
to set caching and encryption bits for those vmas (except for COW pages).
This is ensured by core vm only modifying these page table entries using
functions that don't touch caching- or encryption bits, using pte_modify()
if needed. (See for example mprotect()).

Also when new page-table entries are created, this is only done using the
fault() callback, and never using the value of vma->vm_page_prot,
except for page-table entries that point to anonymous pages as the result
of COW.

**Context**

Process context. May allocate using `GFP_KERNEL`.

**Return**

vm_fault_t value.

[vm_fault_t](mm-api.md#c.vm_fault_t "vm_fault_t") vmf_insert_pfn(struct vm_area_struct \*vma, unsigned long addr, unsigned long pfn)
:   insert single pfn into user vma

**Parameters**

`struct vm_area_struct *vma`
:   user vma to map to

`unsigned long addr`
:   target user address of this page

`unsigned long pfn`
:   source kernel pfn

**Description**

Similar to vm_insert_page, this allows drivers to insert individual pages
they've allocated into a user vma. Same comments apply.

This function should only be called from a vm_ops->fault handler, and
in that case the handler should return the result of this function.

vma cannot be a COW mapping.

As this is called only for pages that do not currently exist, we
do not need to flush old virtual caches or the TLB.

**Context**

Process context. May allocate using `GFP_KERNEL`.

**Return**

vm_fault_t value.

int remap_pfn_range(struct vm_area_struct \*vma, unsigned long addr, unsigned long pfn, unsigned long size, pgprot_t prot)
:   remap kernel memory to userspace

**Parameters**

`struct vm_area_struct *vma`
:   user vma to map to

`unsigned long addr`
:   target page aligned user address to start at

`unsigned long pfn`
:   page frame number of kernel physical memory address

`unsigned long size`
:   size of mapping area

`pgprot_t prot`
:   page protection flags for this mapping

**Note**

this is only safe if the mm semaphore is held when called.

**Return**

`0` on success, negative error code otherwise.

int vm_iomap_memory(struct vm_area_struct \*vma, phys_addr_t start, unsigned long len)
:   remap memory to userspace

**Parameters**

`struct vm_area_struct *vma`
:   user vma to map to

`phys_addr_t start`
:   start of the physical memory to be mapped

`unsigned long len`
:   size of area

**Description**

This is a simplified io_remap_pfn_range() for common driver use. The
driver just needs to give us the physical memory range to be mapped,
we'll figure out the rest from the vma information.

NOTE! Some drivers might want to tweak vma->vm_page_prot first to get
whatever write-combining details or similar.

**Return**

`0` on success, negative error code otherwise.

void unmap_mapping_pages(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, pgoff_t start, pgoff_t nr, bool even_cows)
:   Unmap pages from processes.

**Parameters**

`struct address_space *mapping`
:   The address space containing pages to be unmapped.

`pgoff_t start`
:   Index of first page to be unmapped.

`pgoff_t nr`
:   Number of pages to be unmapped. 0 to unmap to end of file.

`bool even_cows`
:   Whether to unmap even private COWed pages.

**Description**

Unmap the pages in this address space from any userspace process which
has them mmaped. Generally, you want to remove COWed pages as well when
a file is being truncated, but not when invalidating pages from the page
cache.

void unmap_mapping_range(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, loff_t const holebegin, loff_t const holelen, int even_cows)
:   unmap the portion of all mmaps in the specified address_space corresponding to the specified byte range in the underlying file.

**Parameters**

`struct address_space *mapping`
:   the address space containing mmaps to be unmapped.

`loff_t const holebegin`
:   byte in first page to unmap, relative to the start of
    the underlying file. This will be rounded down to a PAGE_SIZE
    boundary. Note that this is different from [`truncate_pagecache()`](mm-api.md#c.truncate_pagecache "truncate_pagecache"), which
    must keep the partial page. In contrast, we must get rid of
    partial pages.

`loff_t const holelen`
:   size of prospective hole in bytes. This will be rounded
    up to a PAGE_SIZE boundary. A holelen of zero truncates to the
    end of the file.

`int even_cows`
:   1 when truncating a file, unmap even private COWed pages;
    but 0 when invalidating pagecache, don't throw away private data.

int follow_pte(struct mm_struct \*mm, unsigned long address, pte_t \*\*ptepp, spinlock_t \*\*ptlp)
:   look up PTE at a user virtual address

**Parameters**

`struct mm_struct *mm`
:   the mm_struct of the target address space

`unsigned long address`
:   user virtual address

`pte_t **ptepp`
:   location to store found PTE

`spinlock_t **ptlp`
:   location to store the lock for the PTE

**Description**

On a successful return, the pointer to the PTE is stored in **ptepp**;
the corresponding lock is taken and its location is stored in **ptlp**.
The contents of the PTE are only stable until **ptlp** is released;
any further use, if any, must be protected against invalidation
with MMU notifiers.

Only IO mappings and raw PFN mappings are allowed. The mmap semaphore
should be taken for read.

KVM uses this function. While it is arguably less bad than `follow_pfn`,
it is not a good general-purpose API.

**Return**

zero on success, -ve otherwise.

int follow_pfn(struct vm_area_struct \*vma, unsigned long address, unsigned long \*pfn)
:   look up PFN at a user virtual address

**Parameters**

`struct vm_area_struct *vma`
:   memory mapping

`unsigned long address`
:   user virtual address

`unsigned long *pfn`
:   location to store found PFN

**Description**

Only IO mappings and raw PFN mappings are allowed.

This function does not allow the caller to read the permissions
of the PTE. Do not use it.

**Return**

zero and the pfn at **pfn** on success, -ve otherwise.

int generic_access_phys(struct vm_area_struct \*vma, unsigned long addr, void \*buf, int len, int write)
:   generic implementation for iomem mmap access

**Parameters**

`struct vm_area_struct *vma`
:   the vma to access

`unsigned long addr`
:   userspace address, not relative offset within **vma**

`void *buf`
:   buffer to read/write

`int len`
:   length of transfer

`int write`
:   set to FOLL_WRITE when writing, otherwise reading

**Description**

This is a generic implementation for `vm_operations_struct.access` for an
iomem mapping. This callback is used by access_process_vm() when the **vma** is
not page based.

unsigned long get_pfnblock_flags_mask(const struct [page](mm-api.md#c.get_pfnblock_flags_mask "page") \*page, unsigned long pfn, unsigned long mask)
:   Return the requested group of flags for the pageblock_nr_pages block of pages

**Parameters**

`const struct page *page`
:   The page within the block of interest

`unsigned long pfn`
:   The target page frame number

`unsigned long mask`
:   mask of bits that the caller is interested in

**Return**

pageblock_bits flags

void set_pfnblock_flags_mask(struct [page](mm-api.md#c.set_pfnblock_flags_mask "page") \*page, unsigned long flags, unsigned long pfn, unsigned long mask)
:   Set the requested group of flags for a pageblock_nr_pages block of pages

**Parameters**

`struct page *page`
:   The page within the block of interest

`unsigned long flags`
:   The flags to set

`unsigned long pfn`
:   The target page frame number

`unsigned long mask`
:   mask of bits that the caller is interested in

int split_free_page(struct page \*free_page, unsigned int order, unsigned long split_pfn_offset)
:   - split a free page at split_pfn_offset

**Parameters**

`struct page *free_page`
:   the original free page

`unsigned int order`
:   the order of the page

`unsigned long split_pfn_offset`
:   split offset within the page

**Description**

Return -ENOENT if the free page is changed, otherwise 0

It is used when the free page crosses two pageblocks with different migratetypes
at split_pfn_offset within the page. The split free page will be put into
separate migratetype lists afterwards. Otherwise, the function achieves
nothing.

void __putback_isolated_page(struct [page](mm-api.md#c.__putback_isolated_page "page") \*page, unsigned int order, int mt)
:   Return a now-isolated page back where we got it

**Parameters**

`struct page *page`
:   Page that was isolated

`unsigned int order`
:   Order of the isolated page

`int mt`
:   The page's pageblock's migratetype

**Description**

This function is meant to return a page pulled from the free lists via
__isolate_free_page back to the free lists they were pulled from.

void __free_pages(struct [page](mm-api.md#c.__free_pages "page") \*page, unsigned int order)
:   Free pages allocated with [`alloc_pages()`](mm-api.md#c.alloc_pages "alloc_pages").

**Parameters**

`struct page *page`
:   The page pointer returned from [`alloc_pages()`](mm-api.md#c.alloc_pages "alloc_pages").

`unsigned int order`
:   The order of the allocation.

**Description**

This function can free multi-page allocations that are not compound
pages. It does not check that the **order** passed in matches that of
the allocation, so it is easy to leak memory. Freeing more memory
than was allocated will probably emit a warning.

If the last reference to this page is speculative, it will be released
by put_page() which only frees the first page of a non-compound
allocation. To prevent the remaining pages from being leaked, we free
the subsequent pages here. If you want to use the page's reference
count to decide when to free the allocation, you should allocate a
compound page, and use put_page() instead of [`__free_pages()`](mm-api.md#c.__free_pages "__free_pages").

**Context**

May be called in interrupt context or while holding a normal
spinlock, but not in NMI context or while holding a raw spinlock.

void \*alloc_pages_exact(size_t size, gfp_t gfp_mask)
:   allocate an exact number physically-contiguous pages.

**Parameters**

`size_t size`
:   the number of bytes to allocate

`gfp_t gfp_mask`
:   GFP flags for the allocation, must not contain __GFP_COMP

**Description**

This function is similar to [`alloc_pages()`](mm-api.md#c.alloc_pages "alloc_pages"), except that it allocates the
minimum number of pages to satisfy the request. [`alloc_pages()`](mm-api.md#c.alloc_pages "alloc_pages") can only
allocate memory in power-of-two pages.

This function is also limited by MAX_PAGE_ORDER.

Memory allocated by this function must be released by [`free_pages_exact()`](mm-api.md#c.free_pages_exact "free_pages_exact").

**Return**

pointer to the allocated area or `NULL` in case of error.

void \*alloc_pages_exact_nid(int nid, size_t size, gfp_t gfp_mask)
:   allocate an exact number of physically-contiguous pages on a node.

**Parameters**

`int nid`
:   the preferred node ID where memory should be allocated

`size_t size`
:   the number of bytes to allocate

`gfp_t gfp_mask`
:   GFP flags for the allocation, must not contain __GFP_COMP

**Description**

Like [`alloc_pages_exact()`](mm-api.md#c.alloc_pages_exact "alloc_pages_exact"), but try to allocate on node nid first before falling
back.

**Return**

pointer to the allocated area or `NULL` in case of error.

void free_pages_exact(void \*virt, size_t size)
:   release memory allocated via [`alloc_pages_exact()`](mm-api.md#c.alloc_pages_exact "alloc_pages_exact")

**Parameters**

`void *virt`
:   the value returned by alloc_pages_exact.

`size_t size`
:   size of allocation, same value as passed to [`alloc_pages_exact()`](mm-api.md#c.alloc_pages_exact "alloc_pages_exact").

**Description**

Release the memory allocated by a previous call to alloc_pages_exact.

unsigned long nr_free_zone_pages(int offset)
:   count number of pages beyond high watermark

**Parameters**

`int offset`
:   The zone index of the highest zone

**Description**

[`nr_free_zone_pages()`](mm-api.md#c.nr_free_zone_pages "nr_free_zone_pages") counts the number of pages which are beyond the
high watermark within all zones at or below a given zone index. For each
zone, the number of pages is calculated as:

> nr_free_zone_pages = managed_pages - high_pages

**Return**

number of pages beyond high watermark.

unsigned long nr_free_buffer_pages(void)
:   count number of pages beyond high watermark

**Parameters**

`void`
:   no arguments

**Description**

[`nr_free_buffer_pages()`](mm-api.md#c.nr_free_buffer_pages "nr_free_buffer_pages") counts the number of pages which are beyond the high
watermark within ZONE_DMA and ZONE_NORMAL.

**Return**

number of pages beyond high watermark within ZONE_DMA and
ZONE_NORMAL.

int find_next_best_node(int node, nodemask_t \*used_node_mask)
:   find the next node that should appear in a given node's fallback list

**Parameters**

`int node`
:   node whose fallback list we're appending

`nodemask_t *used_node_mask`
:   nodemask_t of already used nodes

**Description**

We use a number of factors to determine which is the next node that should
appear on a given node's fallback list. The node should not have appeared
already in **node**'s fallback list, and it should be the next closest node
according to the distance array (which contains arbitrary distance values
from each node to each node in the system), and should also prefer nodes
with no CPUs, since presumably they'll have very little allocation pressure
on them otherwise.

**Return**

node id of the found node or `NUMA_NO_NODE` if no node is found.

void setup_per_zone_wmarks(void)
:   called when min_free_kbytes changes or when memory is hot-{added|removed}

**Parameters**

`void`
:   no arguments

**Description**

Ensures that the watermark[min,low,high] values for each zone are set
correctly with respect to min_free_kbytes.

int alloc_contig_range(unsigned long start, unsigned long end, unsigned migratetype, gfp_t gfp_mask)
:   - tries to allocate given range of pages

**Parameters**

`unsigned long start`
:   start PFN to allocate

`unsigned long end`
:   one-past-the-last PFN to allocate

`unsigned migratetype`
:   migratetype of the underlying pageblocks (either
    #MIGRATE_MOVABLE or #MIGRATE_CMA). All pageblocks
    in range must have the same migratetype and it must
    be either of the two.

`gfp_t gfp_mask`
:   GFP mask to use during compaction

**Description**

The PFN range does not have to be pageblock aligned. The PFN range must
belong to a single zone.

The first thing this routine does is attempt to MIGRATE_ISOLATE all
pageblocks in the range. Once isolated, the pageblocks should not
be modified by others.

**Return**

zero on success or negative error code. On success all
pages which PFN is in [start, end) are allocated for the caller and
need to be freed with free_contig_range().

struct page \*alloc_contig_pages(unsigned long nr_pages, gfp_t gfp_mask, int nid, nodemask_t \*nodemask)
:   - tries to find and allocate contiguous range of pages

**Parameters**

`unsigned long nr_pages`
:   Number of contiguous pages to allocate

`gfp_t gfp_mask`
:   GFP mask to limit search and used during compaction

`int nid`
:   Target node

`nodemask_t *nodemask`
:   Mask for other possible nodes

**Description**

This routine is a wrapper around [`alloc_contig_range()`](mm-api.md#c.alloc_contig_range "alloc_contig_range"). It scans over zones
on an applicable zonelist to find a contiguous pfn range which can then be
tried for allocation with [`alloc_contig_range()`](mm-api.md#c.alloc_contig_range "alloc_contig_range"). This routine is intended
for allocation requests which can not be fulfilled with the buddy allocator.

The allocated memory is always aligned to a page boundary. If nr_pages is a
power of two, then allocated range is also guaranteed to be aligned to same
nr_pages (e.g. 1GB request would be aligned to 1GB).

Allocated pages can be freed with free_contig_range() or by manually calling
__free_page() on each allocated page.

**Return**

pointer to contiguous pages on success, or NULL if not successful.

int numa_nearest_node(int node, unsigned int state)
:   Find nearest node by state

**Parameters**

`int node`
:   Node id to start the search

`unsigned int state`
:   State to filter the search

**Description**

Lookup the closest node by distance if **nid** is not in state.

**Return**

this **node** if it is in state, otherwise the closest node by distance

struct page \*alloc_pages_mpol(gfp_t gfp, unsigned int order, struct mempolicy \*pol, pgoff_t ilx, int nid)
:   Allocate pages according to NUMA mempolicy.

**Parameters**

`gfp_t gfp`
:   GFP flags.

`unsigned int order`
:   Order of the page allocation.

`struct mempolicy *pol`
:   Pointer to the NUMA mempolicy.

`pgoff_t ilx`
:   Index for interleave mempolicy (also distinguishes [`alloc_pages()`](mm-api.md#c.alloc_pages "alloc_pages")).

`int nid`
:   Preferred node (usually numa_node_id() but **mpol** may override it).

**Return**

The page on success or NULL if allocation fails.

struct [folio](mm-api.md#c.folio "folio") \*vma_alloc_folio(gfp_t gfp, int order, struct vm_area_struct \*vma, unsigned long addr, bool hugepage)
:   Allocate a folio for a VMA.

**Parameters**

`gfp_t gfp`
:   GFP flags.

`int order`
:   Order of the folio.

`struct vm_area_struct *vma`
:   Pointer to VMA.

`unsigned long addr`
:   Virtual address of the allocation. Must be inside **vma**.

`bool hugepage`
:   Unused (was: For hugepages try only preferred node if possible).

**Description**

Allocate a folio for a specific address in **vma**, using the appropriate
NUMA policy. The caller must hold the mmap_lock of the mm_struct of the
VMA to prevent it from going away. Should be used for all allocations
for folios that will be mapped into user space, excepting hugetlbfs, and
excepting where direct use of [`alloc_pages_mpol()`](mm-api.md#c.alloc_pages_mpol "alloc_pages_mpol") is more appropriate.

**Return**

The folio on success or NULL if allocation fails.

struct page \*alloc_pages(gfp_t gfp, unsigned int order)
:   Allocate pages.

**Parameters**

`gfp_t gfp`
:   GFP flags.

`unsigned int order`
:   Power of two of number of pages to allocate.

**Description**

Allocate 1 << **order** contiguous pages. The physical address of the
first page is naturally aligned (eg an order-3 allocation will be aligned
to a multiple of 8 \* PAGE_SIZE bytes). The NUMA policy of the current
process is honoured when in process context.

**Context**

Can be called from any context, providing the appropriate GFP
flags are used.

**Return**

The page on success or NULL if allocation fails.

int mpol_misplaced(struct [folio](mm-api.md#c.mpol_misplaced "folio") \*folio, struct vm_area_struct \*vma, unsigned long addr)
:   check whether current folio node is valid in policy

**Parameters**

`struct folio *folio`
:   folio to be checked

`struct vm_area_struct *vma`
:   vm area where folio mapped

`unsigned long addr`
:   virtual address in **vma** for shared policy lookup and interleave policy

**Description**

Lookup current policy node id for vma,addr and "compare to" folio's
node id. Policy determination "mimics" alloc_page_vma().
Called from fault path where we know the vma and faulting address.

**Return**

NUMA_NO_NODE if the page is in a node that is valid for this
policy, or a suitable node ID to allocate a replacement folio from.

void mpol_shared_policy_init(struct shared_policy \*sp, struct mempolicy \*mpol)
:   initialize shared policy for inode

**Parameters**

`struct shared_policy *sp`
:   pointer to inode shared policy

`struct mempolicy *mpol`
:   struct mempolicy to install

**Description**

Install non-NULL **mpol** in inode's shared policy rb-tree.
On entry, the current task has a reference on a non-NULL **mpol**.
This must be released on exit.
This is called at get_inode() calls and we can use GFP_KERNEL.

int mpol_parse_str(char \*str, struct mempolicy \*\*mpol)
:   parse string to mempolicy, for tmpfs mpol mount option.

**Parameters**

`char *str`
:   string containing mempolicy to parse

`struct mempolicy **mpol`
:   pointer to struct mempolicy pointer, returned on success.

**Description**

Format of input:
:   <mode>[=<flags>][:<nodelist>]

**Return**

`0` on success, else `1`

void mpol_to_str(char \*buffer, int maxlen, struct mempolicy \*pol)
:   format a mempolicy structure for printing

**Parameters**

`char *buffer`
:   to contain formatted mempolicy string

`int maxlen`
:   length of **buffer**

`struct mempolicy *pol`
:   pointer to mempolicy to be formatted

**Description**

Convert **pol** into a string. If **buffer** is too short, truncate the string.
Recommend a **maxlen** of at least 32 for the longest mode, "interleave", the
longest flag, "relative", and to display at least a few node ids.

struct folio
:   Represents a contiguous set of bytes.

**Definition**:

```
struct folio {
    unsigned long flags;
    union {
        struct list_head lru;
        unsigned int mlock_count;
    };
    struct address_space *mapping;
    pgoff_t index;
    union {
        void *private;
        swp_entry_t swap;
    };
    atomic_t _mapcount;
    atomic_t _refcount;
#ifdef CONFIG_MEMCG;
    unsigned long memcg_data;
#endif;
#if defined(WANT_PAGE_VIRTUAL);
    void *virtual;
#endif;
#ifdef LAST_CPUPID_NOT_IN_PAGE_FLAGS;
    int _last_cpupid;
#endif;
    atomic_t _entire_mapcount;
    atomic_t _nr_pages_mapped;
    atomic_t _pincount;
#ifdef CONFIG_64BIT;
    unsigned int _folio_nr_pages;
#endif;
    void *_hugetlb_subpool;
    void *_hugetlb_cgroup;
    void *_hugetlb_cgroup_rsvd;
    void *_hugetlb_hwpoison;
    struct list_head _deferred_list;
};
```

**Members**

`flags`
:   Identical to the page flags.

`{unnamed_union}`
:   anonymous

`lru`
:   Least Recently Used list; tracks how recently this folio was used.

`mlock_count`
:   Number of times this folio has been pinned by mlock().

`mapping`
:   The file this page belongs to, or refers to the anon_vma for
    anonymous memory.

`index`
:   Offset within the file, in units of pages. For anonymous memory,
    this is the index from the beginning of the mmap.

`{unnamed_union}`
:   anonymous

`private`
:   Filesystem per-folio data (see [`folio_attach_private()`](mm-api.md#c.folio_attach_private "folio_attach_private")).

`swap`
:   Used for swp_entry_t if folio_test_swapcache().

`_mapcount`
:   Do not access this member directly. Use [`folio_mapcount()`](mm-api.md#c.folio_mapcount "folio_mapcount") to
    find out how many times this folio is mapped by userspace.

`_refcount`
:   Do not access this member directly. Use [`folio_ref_count()`](mm-api.md#c.folio_ref_count "folio_ref_count")
    to find how many references there are to this folio.

`memcg_data`
:   Memory Control Group data.

`virtual`
:   Virtual address in the kernel direct map.

`_last_cpupid`
:   IDs of last CPU and last process that accessed the folio.

`_entire_mapcount`
:   Do not use directly, call folio_entire_mapcount().

`_nr_pages_mapped`
:   Do not use directly, call [`folio_mapcount()`](mm-api.md#c.folio_mapcount "folio_mapcount").

`_pincount`
:   Do not use directly, call [`folio_maybe_dma_pinned()`](mm-api.md#c.folio_maybe_dma_pinned "folio_maybe_dma_pinned").

`_folio_nr_pages`
:   Do not use directly, call [`folio_nr_pages()`](mm-api.md#c.folio_nr_pages "folio_nr_pages").

`_hugetlb_subpool`
:   Do not use directly, use accessor in hugetlb.h.

`_hugetlb_cgroup`
:   Do not use directly, use accessor in hugetlb_cgroup.h.

`_hugetlb_cgroup_rsvd`
:   Do not use directly, use accessor in hugetlb_cgroup.h.

`_hugetlb_hwpoison`
:   Do not use directly, call raw_hwp_list_head().

`_deferred_list`
:   Folios to be split under memory pressure.

**Description**

A folio is a physically, virtually and logically contiguous set
of bytes. It is a power-of-two in size, and it is aligned to that
same power-of-two. It is at least as large as `PAGE_SIZE`. If it is
in the page cache, it is at a file offset which is a multiple of that
power-of-two. It may be mapped into userspace at an address which is
at an arbitrary page offset, but its kernel virtual address is aligned
to its size.

struct ptdesc
:   Memory descriptor for page tables.

**Definition**:

```
struct ptdesc {
    unsigned long __page_flags;
    union {
        struct rcu_head pt_rcu_head;
        struct list_head pt_list;
        struct {
            unsigned long _pt_pad_1;
            pgtable_t pmd_huge_pte;
        };
    };
    unsigned long __page_mapping;
    union {
        struct mm_struct *pt_mm;
        atomic_t pt_frag_refcount;
    };
    union {
        unsigned long _pt_pad_2;
#if ALLOC_SPLIT_PTLOCKS;
        spinlock_t *ptl;
#else;
        spinlock_t ptl;
#endif;
    };
    unsigned int __page_type;
    atomic_t __page_refcount;
#ifdef CONFIG_MEMCG;
    unsigned long pt_memcg_data;
#endif;
};
```

**Members**

`__page_flags`
:   Same as page flags. Unused for page tables.

`{unnamed_union}`
:   anonymous

`pt_rcu_head`
:   For freeing page table pages.

`pt_list`
:   List of used page tables. Used for s390 and x86.

`{unnamed_struct}`
:   anonymous

`_pt_pad_1`
:   Padding that aliases with page's compound head.

`pmd_huge_pte`
:   Protected by ptdesc->ptl, used for THPs.

`__page_mapping`
:   Aliases with page->mapping. Unused for page tables.

`{unnamed_union}`
:   anonymous

`pt_mm`
:   Used for x86 pgds.

`pt_frag_refcount`
:   For fragmented page table tracking. Powerpc only.

`{unnamed_union}`
:   anonymous

`_pt_pad_2`
:   Padding to ensure proper alignment.

`ptl`
:   Lock for the page table.

`ptl`
:   Lock for the page table.

`__page_type`
:   Same as page->page_type. Unused for page tables.

`__page_refcount`
:   Same as page refcount.

`pt_memcg_data`
:   Memcg data. Tracked for page tables here.

**Description**

This struct overlays struct page for now. Do not modify without a good
understanding of the issues.

type vm_fault_t
:   Return type for page fault handlers.

**Description**

Page fault handlers return a bitmask of `VM_FAULT` values.

enum vm_fault_reason
:   Page fault handlers return a bitmask of these values to tell the core VM what happened when handling the fault. Used to decide whether a process gets delivered SIGBUS or just gets major/minor fault counters bumped up.

**Constants**

`VM_FAULT_OOM`
:   Out Of Memory

`VM_FAULT_SIGBUS`
:   Bad access

`VM_FAULT_MAJOR`
:   Page read from storage

`VM_FAULT_HWPOISON`
:   Hit poisoned small page

`VM_FAULT_HWPOISON_LARGE`
:   Hit poisoned large page. Index encoded
    in upper bits

`VM_FAULT_SIGSEGV`
:   segmentation fault

`VM_FAULT_NOPAGE`
:   ->fault installed the pte, not return page

`VM_FAULT_LOCKED`
:   ->fault locked the returned page

`VM_FAULT_RETRY`
:   ->fault blocked, must retry

`VM_FAULT_FALLBACK`
:   huge page fault failed, fall back to small

`VM_FAULT_DONE_COW`
:   ->fault has fully handled COW

`VM_FAULT_NEEDDSYNC`
:   ->fault did not modify page tables and needs
    fsync() to complete (for synchronous page faults
    in DAX)

`VM_FAULT_COMPLETED`
:   ->fault completed, meanwhile mmap lock released

`VM_FAULT_HINDEX_MASK`
:   mask HINDEX value

enum fault_flag
:   Fault flag definitions.

**Constants**

`FAULT_FLAG_WRITE`
:   Fault was a write fault.

`FAULT_FLAG_MKWRITE`
:   Fault was mkwrite of existing PTE.

`FAULT_FLAG_ALLOW_RETRY`
:   Allow to retry the fault if blocked.

`FAULT_FLAG_RETRY_NOWAIT`
:   Don't drop mmap_lock and wait when retrying.

`FAULT_FLAG_KILLABLE`
:   The fault task is in SIGKILL killable region.

`FAULT_FLAG_TRIED`
:   The fault has been tried once.

`FAULT_FLAG_USER`
:   The fault originated in userspace.

`FAULT_FLAG_REMOTE`
:   The fault is not for current task/mm.

`FAULT_FLAG_INSTRUCTION`
:   The fault was during an instruction fetch.

`FAULT_FLAG_INTERRUPTIBLE`
:   The fault can be interrupted by non-fatal signals.

`FAULT_FLAG_UNSHARE`
:   The fault is an unsharing request to break COW in a
    COW mapping, making sure that an exclusive anon page is
    mapped after the fault.

`FAULT_FLAG_ORIG_PTE_VALID`
:   whether the fault has vmf->orig_pte cached.
    We should only access orig_pte if this flag set.

`FAULT_FLAG_VMA_LOCK`
:   The fault is handled under VMA lock.

**Description**

About **FAULT_FLAG_ALLOW_RETRY** and **FAULT_FLAG_TRIED**: we can specify
whether we would allow page faults to retry by specifying these two
fault flags correctly. Currently there can be three legal combinations:

1. ALLOW_RETRY and !TRIED: this means the page fault allows retry, and
   :   this is the first try
2. ALLOW_RETRY and TRIED: this means the page fault allows retry, and
   :   we've already tried at least once
3. !ALLOW_RETRY and !TRIED: this means the page fault does not allow retry

The unlisted combination (!ALLOW_RETRY && TRIED) is illegal and should never
be used. Note that page faults can be allowed to retry for multiple times,
in which case we'll have an initial fault with flags (a) then later on
continuous faults with flags (b). We should always try to detect pending
signals before a retry to make sure the continuous page faults can still be
interrupted if necessary.

The combination FAULT_FLAG_WRITE|FAULT_FLAG_UNSHARE is illegal.
FAULT_FLAG_UNSHARE is ignored and treated like an ordinary read fault when
applied to mappings that are not COW mappings.

int folio_is_file_lru(struct [folio](mm-api.md#c.folio_is_file_lru "folio") \*folio)
:   Should the folio be on a file LRU or anon LRU?

**Parameters**

`struct folio *folio`
:   The folio to test.

**Description**

We would like to get this info without a page flag, but the state
needs to survive until the folio is last deleted from the LRU, which
could be as far down as __page_cache_release.

**Return**

An integer (not a boolean!) used to sort a folio onto the
right LRU list and to account folios correctly.
1 if **folio** is a regular filesystem backed page cache folio
or a lazily freed anonymous folio (e.g. via MADV_FREE).
0 if **folio** is a normal anonymous folio, a tmpfs folio or otherwise
ram or swap backed folio.

void __folio_clear_lru_flags(struct [folio](mm-api.md#c.__folio_clear_lru_flags "folio") \*folio)
:   Clear page lru flags before releasing a page.

**Parameters**

`struct folio *folio`
:   The folio that was on lru and now has a zero reference.

enum lru_list folio_lru_list(struct [folio](mm-api.md#c.folio_lru_list "folio") \*folio)
:   Which LRU list should a folio be on?

**Parameters**

`struct folio *folio`
:   The folio to test.

**Return**

The LRU list a folio should be on, as an index
into the array of LRU lists.

page_folio

`page_folio (p)`

> Converts from page to folio.

**Parameters**

`p`
:   The page.

**Description**

Every page is part of a folio. This function cannot be called on a
NULL pointer.

**Context**

No reference, nor lock is required on **page**. If the caller
does not hold a reference, this call may race with a folio split, so
it should re-check the folio still contains this page after gaining
a reference on the folio.

**Return**

The folio which contains this page.

folio_page

`folio_page (folio, n)`

> Return a page from a folio.

**Parameters**

`folio`
:   The folio.

`n`
:   The page number to return.

**Description**

**n** is relative to the start of the folio. This function does not
check that the page number lies within **folio**; the caller is presumed
to have a reference to the page.

bool folio_xor_flags_has_waiters(struct [folio](mm-api.md#c.folio_xor_flags_has_waiters "folio") \*folio, unsigned long mask)
:   Change some folio flags.

**Parameters**

`struct folio *folio`
:   The folio.

`unsigned long mask`
:   Bits set in this word will be changed.

**Description**

This must only be used for flags which are changed with the folio
lock held. For example, it is unsafe to use for PG_dirty as that
can be set without the folio lock held. It can also only be used
on flags which are in the range 0-6 as some of the implementations
only affect those bits.

**Return**

Whether there are tasks waiting on the folio.

bool folio_test_uptodate(struct [folio](mm-api.md#c.folio_test_uptodate "folio") \*folio)
:   Is this folio up to date?

**Parameters**

`struct folio *folio`
:   The folio.

**Description**

The uptodate flag is set on a folio when every byte in the folio is
at least as new as the corresponding bytes on storage. Anonymous
and CoW folios are always uptodate. If the folio is not uptodate,
some of the bytes in it may be; see the is_partially_uptodate()
address_space operation.

bool folio_test_large(struct [folio](mm-api.md#c.folio_test_large "folio") \*folio)
:   Does this folio contain more than one page?

**Parameters**

`struct folio *folio`
:   The folio to test.

**Return**

True if the folio is larger than one page.

bool folio_test_hugetlb(struct [folio](mm-api.md#c.folio_test_hugetlb "folio") \*folio)
:   Determine if the folio belongs to hugetlbfs

**Parameters**

`struct folio *folio`
:   The folio to test.

**Context**

Any context. Caller should have a reference on the folio to
prevent it from being turned into a tail page.

**Return**

True for hugetlbfs folios, false for anon folios or folios
belonging to other filesystems.

int page_has_private(struct [page](mm-api.md#c.page_has_private "page") \*page)
:   Determine if page has private stuff

**Parameters**

`struct page *page`
:   The page to be checked

**Description**

Determine if a page has private stuff, indicating that release routines
should be invoked upon it.

bool fault_flag_allow_retry_first(enum [fault_flag](mm-api.md#c.fault_flag "fault_flag") flags)
:   check ALLOW_RETRY the first time

**Parameters**

`enum fault_flag flags`
:   Fault flags.

**Description**

This is mostly used for places where we want to try to avoid taking
the mmap_lock for too long a time when waiting for another condition
to change, in which case we can try to be polite to release the
mmap_lock in the first round to avoid potential starvation of other
processes that would also want the mmap_lock.

**Return**

true if the page fault allows retry and this is the first
attempt of the fault handling; false otherwise.

unsigned int folio_order(struct [folio](mm-api.md#c.folio_order "folio") \*folio)
:   The allocation order of a folio.

**Parameters**

`struct folio *folio`
:   The folio.

**Description**

A folio is composed of 2^order pages. See get_order() for the definition
of order.

**Return**

The order of the folio.

int page_mapcount(struct [page](mm-api.md#c.page_mapcount "page") \*page)
:   Number of times this precise page is mapped.

**Parameters**

`struct page *page`
:   The page.

**Description**

The number of times this page is mapped. If this page is part of
a large folio, it includes the number of times this page is mapped
as part of that folio.

The result is undefined for pages which cannot be mapped into userspace.
For example SLAB or special types of pages. See function page_has_type().
They use this field in struct page differently.

int folio_mapcount(struct [folio](mm-api.md#c.folio_mapcount "folio") \*folio)
:   Calculate the number of mappings of this folio.

**Parameters**

`struct folio *folio`
:   The folio.

**Description**

A large folio tracks both how many times the entire folio is mapped,
and how many times each individual page in the folio is mapped.
This function calculates the total number of times the folio is
mapped.

**Return**

The number of times this folio is mapped.

bool folio_mapped(struct [folio](mm-api.md#c.folio_mapped "folio") \*folio)
:   Is this folio mapped into userspace?

**Parameters**

`struct folio *folio`
:   The folio.

**Return**

True if any page in this folio is referenced by user page tables.

unsigned int thp_order(struct [page](mm-api.md#c.thp_order "page") \*page)
:   Order of a transparent huge page.

**Parameters**

`struct page *page`
:   Head page of a transparent huge page.

unsigned long thp_size(struct [page](mm-api.md#c.thp_size "page") \*page)
:   Size of a transparent huge page.

**Parameters**

`struct page *page`
:   Head page of a transparent huge page.

**Return**

Number of bytes in this page.

void folio_get(struct [folio](mm-api.md#c.folio_get "folio") \*folio)
:   Increment the reference count on a folio.

**Parameters**

`struct folio *folio`
:   The folio.

**Context**

May be called in any context, as long as you know that
you have a refcount on the folio. If you do not already have one,
[`folio_try_get()`](mm-api.md#c.folio_try_get "folio_try_get") may be the right interface for you to use.

void folio_put(struct [folio](mm-api.md#c.folio_put "folio") \*folio)
:   Decrement the reference count on a folio.

**Parameters**

`struct folio *folio`
:   The folio.

**Description**

If the folio's reference count reaches zero, the memory will be
released back to the page allocator and may be used by another
allocation immediately. Do not access the memory or the [`struct folio`](mm-api.md#c.folio "folio")
after calling [`folio_put()`](mm-api.md#c.folio_put "folio_put") unless you can be sure that it wasn't the
last reference.

**Context**

May be called in process or interrupt context, but not in NMI
context. May be called while holding a spinlock.

void folio_put_refs(struct [folio](mm-api.md#c.folio_put_refs "folio") \*folio, int refs)
:   Reduce the reference count on a folio.

**Parameters**

`struct folio *folio`
:   The folio.

`int refs`
:   The amount to subtract from the folio's reference count.

**Description**

If the folio's reference count reaches zero, the memory will be
released back to the page allocator and may be used by another
allocation immediately. Do not access the memory or the [`struct folio`](mm-api.md#c.folio "folio")
after calling [`folio_put_refs()`](mm-api.md#c.folio_put_refs "folio_put_refs") unless you can be sure that these weren't
the last references.

**Context**

May be called in process or interrupt context, but not in NMI
context. May be called while holding a spinlock.

void folios_put(struct [folio](mm-api.md#c.folio "folio") \*\*folios, unsigned int nr)
:   Decrement the reference count on an array of folios.

**Parameters**

`struct folio **folios`
:   The folios.

`unsigned int nr`
:   How many folios there are.

**Description**

Like [`folio_put()`](mm-api.md#c.folio_put "folio_put"), but for an array of folios. This is more efficient
than writing the loop yourself as it will optimise the locks which
need to be taken if the folios are freed.

**Context**

May be called in process or interrupt context, but not in NMI
context. May be called while holding a spinlock.

unsigned long folio_pfn(struct [folio](mm-api.md#c.folio_pfn "folio") \*folio)
:   Return the Page Frame Number of a folio.

**Parameters**

`struct folio *folio`
:   The folio.

**Description**

A folio may contain multiple pages. The pages have consecutive
Page Frame Numbers.

**Return**

The Page Frame Number of the first page in the folio.

bool folio_maybe_dma_pinned(struct [folio](mm-api.md#c.folio_maybe_dma_pinned "folio") \*folio)
:   Report if a folio may be pinned for DMA.

**Parameters**

`struct folio *folio`
:   The folio.

**Description**

This function checks if a folio has been pinned via a call to
a function in the pin_user_pages() family.

For small folios, the return value is partially fuzzy: false is not fuzzy,
because it means "definitely not pinned for DMA", but true means "probably
pinned for DMA, but possibly a false positive due to having at least
GUP_PIN_COUNTING_BIAS worth of normal folio references".

False positives are OK, because: a) it's unlikely for a folio to
get that many refcounts, and b) all the callers of this routine are
expected to be able to deal gracefully with a false positive.

For large folios, the result will be exactly correct. That's because
we have more tracking data available: the _pincount field is used
instead of the GUP_PIN_COUNTING_BIAS scheme.

For more information, please see [pin_user_pages() and related calls](pin_user_pages.md).

**Return**

True, if it is likely that the page has been "dma-pinned".
False, if the page is definitely not dma-pinned.

bool is_zero_page(const struct [page](mm-api.md#c.is_zero_page "page") \*page)
:   Query if a page is a zero page

**Parameters**

`const struct page *page`
:   The page to query

**Description**

This returns true if **page** is one of the permanent zero pages.

bool is_zero_folio(const struct [folio](mm-api.md#c.is_zero_folio "folio") \*folio)
:   Query if a folio is a zero page

**Parameters**

`const struct folio *folio`
:   The folio to query

**Description**

This returns true if **folio** is one of the permanent zero pages.

long folio_nr_pages(struct [folio](mm-api.md#c.folio_nr_pages "folio") \*folio)
:   The number of pages in the folio.

**Parameters**

`struct folio *folio`
:   The folio.

**Return**

A positive power of two.

int thp_nr_pages(struct [page](mm-api.md#c.thp_nr_pages "page") \*page)
:   The number of regular pages in this huge page.

**Parameters**

`struct page *page`
:   The head page of a huge page.

struct [folio](mm-api.md#c.folio_next "folio") \*folio_next(struct [folio](mm-api.md#c.folio_next "folio") \*folio)
:   Move to the next physical folio.

**Parameters**

`struct folio *folio`
:   The folio we're currently operating on.

**Description**

If you have physically contiguous memory which may span more than
one folio (eg a `struct bio_vec`), use this function to move from one
folio to the next. Do not use it if the memory is only virtually
contiguous as the folios are almost certainly not adjacent to each
other. This is the folio equivalent to writing `page++`.

**Context**

We assume that the folios are refcounted and/or locked at a
higher level and do not adjust the reference counts.

**Return**

The next [`struct folio`](mm-api.md#c.folio "folio").

unsigned int folio_shift(struct [folio](mm-api.md#c.folio_shift "folio") \*folio)
:   The size of the memory described by this folio.

**Parameters**

`struct folio *folio`
:   The folio.

**Description**

A folio represents a number of bytes which is a power-of-two in size.
This function tells you which power-of-two the folio is. See also
[`folio_size()`](mm-api.md#c.folio_size "folio_size") and [`folio_order()`](mm-api.md#c.folio_order "folio_order").

**Context**

The caller should have a reference on the folio to prevent
it from being split. It is not necessary for the folio to be locked.

**Return**

The base-2 logarithm of the size of this folio.

size_t folio_size(struct [folio](mm-api.md#c.folio_size "folio") \*folio)
:   The number of bytes in a folio.

**Parameters**

`struct folio *folio`
:   The folio.

**Context**

The caller should have a reference on the folio to prevent
it from being split. It is not necessary for the folio to be locked.

**Return**

The number of bytes in this folio.

int folio_estimated_sharers(struct [folio](mm-api.md#c.folio_estimated_sharers "folio") \*folio)
:   Estimate the number of sharers of a folio.

**Parameters**

`struct folio *folio`
:   The folio.

**Description**

[`folio_estimated_sharers()`](mm-api.md#c.folio_estimated_sharers "folio_estimated_sharers") aims to serve as a function to efficiently
estimate the number of processes sharing a folio. This is done by
looking at the precise mapcount of the first subpage in the folio, and
assuming the other subpages are the same. This may not be true for large
folios. If you want exact mapcounts for exact calculations, look at
[`page_mapcount()`](mm-api.md#c.page_mapcount "page_mapcount") or folio_total_mapcount().

**Return**

The estimated number of processes sharing a folio.

struct [ptdesc](mm-api.md#c.ptdesc "ptdesc") \*pagetable_alloc(gfp_t gfp, unsigned int order)
:   Allocate pagetables

**Parameters**

`gfp_t gfp`
:   GFP flags

`unsigned int order`
:   desired pagetable order

**Description**

pagetable_alloc allocates memory for page tables as well as a page table
descriptor to describe that memory.

**Return**

The ptdesc describing the allocated page tables.

void pagetable_free(struct [ptdesc](mm-api.md#c.ptdesc "ptdesc") \*pt)
:   Free pagetables

**Parameters**

`struct ptdesc *pt`
:   The page table descriptor

**Description**

pagetable_free frees the memory of all page tables described by a page
table descriptor and the memory for the descriptor itself.

struct vm_area_struct \*vma_lookup(struct mm_struct \*mm, unsigned long addr)
:   Find a VMA at a specific address

**Parameters**

`struct mm_struct *mm`
:   The process address space.

`unsigned long addr`
:   The user address.

**Return**

The vm_area_struct at the given address, `NULL` otherwise.

bool vma_is_special_huge(const struct vm_area_struct \*vma)
:   Are transhuge page-table entries considered special?

**Parameters**

`const struct vm_area_struct *vma`
:   Pointer to the struct vm_area_struct to consider

**Description**

Whether transhuge page-table entries are considered "special" following
the definition in vm_normal_page().

**Return**

true if transhuge page-table entries should be considered special,
false otherwise.

int seal_check_write(int seals, struct vm_area_struct \*vma)
:   Check for F_SEAL_WRITE or F_SEAL_FUTURE_WRITE flags and handle them.

**Parameters**

`int seals`
:   the seals to check

`struct vm_area_struct *vma`
:   the vma to operate on

**Description**

Check whether F_SEAL_WRITE or F_SEAL_FUTURE_WRITE are set; if so, do proper
check/handling on the vma flags. Return 0 if check pass, or <0 for errors.

int folio_ref_count(const struct [folio](mm-api.md#c.folio_ref_count "folio") \*folio)
:   The reference count on this folio.

**Parameters**

`const struct folio *folio`
:   The folio.

**Description**

The refcount is usually incremented by calls to [`folio_get()`](mm-api.md#c.folio_get "folio_get") and
decremented by calls to [`folio_put()`](mm-api.md#c.folio_put "folio_put"). Some typical users of the
folio refcount:

- Each reference from a page table
- The page cache
- Filesystem private data
- The LRU list
- Pipes
- Direct IO which references this page in the process address space

**Return**

The number of references to this folio.

bool folio_try_get(struct [folio](mm-api.md#c.folio_try_get "folio") \*folio)
:   Attempt to increase the refcount on a folio.

**Parameters**

`struct folio *folio`
:   The folio.

**Description**

If you do not already have a reference to a folio, you can attempt to
get one using this function. It may fail if, for example, the folio
has been freed since you found a pointer to it, or it is frozen for
the purposes of splitting or migration.

**Return**

True if the reference count was successfully incremented.

bool folio_try_get_rcu(struct [folio](mm-api.md#c.folio_try_get_rcu "folio") \*folio)
:   Attempt to increase the refcount on a folio.

**Parameters**

`struct folio *folio`
:   The folio.

**Description**

This is a version of [`folio_try_get()`](mm-api.md#c.folio_try_get "folio_try_get") optimised for non-SMP kernels.
If you are still holding the [`rcu_read_lock()`](kernel-api.md#c.rcu_read_lock "rcu_read_lock") after looking up the
page and know that the page cannot have its refcount decreased to
zero in interrupt context, you can use this instead of [`folio_try_get()`](mm-api.md#c.folio_try_get "folio_try_get").

Example users include [`get_user_pages_fast()`](mm-api.md#c.get_user_pages_fast "get_user_pages_fast") (as pages are not unmapped
from interrupt context) and the page cache lookups (as pages are not
truncated from interrupt context). We also know that pages are not
frozen in interrupt context for the purposes of splitting or migration.

You can also use this function if you're holding a lock that prevents
pages being frozen & removed; eg the i_pages lock for the page cache
or the mmap_lock or page table lock for page tables. In this case,
it will always succeed, and you could have used a plain [`folio_get()`](mm-api.md#c.folio_get "folio_get"),
but it's sometimes more convenient to have a common function called
from both locked and RCU-protected contexts.

**Return**

True if the reference count was successfully incremented.

int is_highmem(struct [zone](mm-api.md#c.is_highmem "zone") \*zone)
:   helper function to quickly check if a struct zone is a highmem zone or not. This is an attempt to keep references to ZONE_{DMA/NORMAL/HIGHMEM/etc} in general code to a minimum.

**Parameters**

`struct zone *zone`
:   pointer to struct zone variable

**Return**

1 for a highmem zone, 0 otherwise

for_each_online_pgdat

`for_each_online_pgdat (pgdat)`

> helper macro to iterate over all online nodes

**Parameters**

`pgdat`
:   pointer to a pg_data_t variable

for_each_zone

`for_each_zone (zone)`

> helper macro to iterate over all memory zones

**Parameters**

`zone`
:   pointer to struct zone variable

**Description**

The user only needs to declare the zone variable, for_each_zone
fills it in.

struct zoneref \*next_zones_zonelist(struct zoneref \*z, enum zone_type highest_zoneidx, nodemask_t \*nodes)
:   Returns the next zone at or below highest_zoneidx within the allowed nodemask using a cursor within a zonelist as a starting point

**Parameters**

`struct zoneref *z`
:   The cursor used as a starting point for the search

`enum zone_type highest_zoneidx`
:   The zone index of the highest zone to return

`nodemask_t *nodes`
:   An optional nodemask to filter the zonelist with

**Description**

This function returns the next zone at or below a given zone index that is
within the allowed nodemask using a cursor as the starting point for the
search. The zoneref returned is a cursor that represents the current zone
being examined. It should be advanced by one before calling
next_zones_zonelist again.

**Return**

the next zone at or below highest_zoneidx within the allowed
nodemask using a cursor within a zonelist as a starting point

struct zoneref \*first_zones_zonelist(struct [zonelist](mm-api.md#c.first_zones_zonelist "zonelist") \*zonelist, enum zone_type highest_zoneidx, nodemask_t \*nodes)
:   Returns the first zone at or below highest_zoneidx within the allowed nodemask in a zonelist

**Parameters**

`struct zonelist *zonelist`
:   The zonelist to search for a suitable zone

`enum zone_type highest_zoneidx`
:   The zone index of the highest zone to return

`nodemask_t *nodes`
:   An optional nodemask to filter the zonelist with

**Description**

This function returns the first zone at or below a given zone index that is
within the allowed nodemask. The zoneref returned is a cursor that can be
used to iterate the zonelist with next_zones_zonelist by advancing it by
one before calling.

When no eligible zone is found, zoneref->zone is NULL (zoneref itself is
never NULL). This may happen either genuinely, or due to concurrent nodemask
update due to cpuset modification.

**Return**

Zoneref pointer for the first suitable zone found

for_each_zone_zonelist_nodemask

`for_each_zone_zonelist_nodemask (zone, z, zlist, highidx, nodemask)`

> helper macro to iterate over valid zones in a zonelist at or below a given zone index and within a nodemask

**Parameters**

`zone`
:   The current zone in the iterator

`z`
:   The current pointer within zonelist->_zonerefs being iterated

`zlist`
:   The zonelist being iterated

`highidx`
:   The zone index of the highest zone to return

`nodemask`
:   Nodemask allowed by the allocator

**Description**

This iterator iterates though all zones at or below a given zone index and
within a given nodemask

for_each_zone_zonelist

`for_each_zone_zonelist (zone, z, zlist, highidx)`

> helper macro to iterate over valid zones in a zonelist at or below a given zone index

**Parameters**

`zone`
:   The current zone in the iterator

`z`
:   The current pointer within zonelist->zones being iterated

`zlist`
:   The zonelist being iterated

`highidx`
:   The zone index of the highest zone to return

**Description**

This iterator iterates though all zones at or below a given zone index.

int pfn_valid(unsigned long pfn)
:   check if there is a valid memory map entry for a PFN

**Parameters**

`unsigned long pfn`
:   the page frame number to check

**Description**

Check if there is a valid memory map entry aka struct page for the **pfn**.
Note, that availability of the memory map entry does not imply that
there is actual usable memory at that **pfn**. The struct page may
represent a hole or an unusable page frame.

**Return**

1 for PFNs that have memory map entries and 0 otherwise

struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*folio_mapping(struct [folio](mm-api.md#c.folio_mapping "folio") \*folio)
:   Find the mapping where this folio is stored.

**Parameters**

`struct folio *folio`
:   The folio.

**Description**

For folios which are in the page cache, return the mapping that this
page belongs to. Folios in the swap cache return the swap mapping
this page is stored in (which is different from the mapping for the
swap file or swap device where the data is stored).

You can call this for folios which aren't in the swap cache or page
cache and it will return NULL.

int __anon_vma_prepare(struct vm_area_struct \*vma)
:   attach an anon_vma to a memory region

**Parameters**

`struct vm_area_struct *vma`
:   the memory region in question

**Description**

This makes sure the memory mapping described by 'vma' has
an 'anon_vma' attached to it, so that we can associate the
anonymous pages mapped into it with that anon_vma.

The common case will be that we already have one, which
is handled inline by anon_vma_prepare(). But if
not we either need to find an adjacent mapping that we
can re-use the anon_vma from (very common when the only
reason for splitting a vma has been mprotect()), or we
allocate a new one.

Anon-vma allocations are very subtle, because we may have
optimistically looked up an anon_vma in folio_lock_anon_vma_read()
and that may actually touch the rwsem even in the newly
allocated vma (it depends on RCU to make sure that the
anon_vma isn't actually destroyed).

As a result, we need to do proper anon_vma locking even
for the new allocation. At the same time, we do not want
to do any locking for the common case of already having
an anon_vma.

This must be called with the mmap_lock held for reading.

int folio_referenced(struct [folio](mm-api.md#c.folio_referenced "folio") \*folio, int is_locked, struct mem_cgroup \*memcg, unsigned long \*vm_flags)
:   Test if the folio was referenced.

**Parameters**

`struct folio *folio`
:   The folio to test.

`int is_locked`
:   Caller holds lock on the folio.

`struct mem_cgroup *memcg`
:   target memory cgroup

`unsigned long *vm_flags`
:   A combination of all the vma->vm_flags which referenced the folio.

**Description**

Quick test_and_clear_referenced for all mappings of a folio,

**Return**

The number of mappings which referenced the folio. Return -1 if
the function bailed out due to rmap lock contention.

int pfn_mkclean_range(unsigned long pfn, unsigned long nr_pages, pgoff_t pgoff, struct vm_area_struct \*vma)
:   Cleans the PTEs (including PMDs) mapped with range of [**pfn**, **pfn** + **nr_pages**) at the specific offset (**pgoff**) within the **vma** of shared mappings. And since clean PTEs should also be readonly, write protects them too.

**Parameters**

`unsigned long pfn`
:   start pfn.

`unsigned long nr_pages`
:   number of physically contiguous pages srarting with **pfn**.

`pgoff_t pgoff`
:   page offset that the **pfn** mapped with.

`struct vm_area_struct *vma`
:   vma that **pfn** mapped within.

**Description**

Returns the number of cleaned PTEs (including PMDs).

void folio_move_anon_rmap(struct [folio](mm-api.md#c.folio_move_anon_rmap "folio") \*folio, struct vm_area_struct \*vma)
:   move a folio to our anon_vma

**Parameters**

`struct folio *folio`
:   The folio to move to our anon_vma

`struct vm_area_struct *vma`
:   The vma the folio belongs to

**Description**

When a folio belongs exclusively to one process after a COW event,
that folio can be moved into the anon_vma that belongs to just that
process, so the rmap code will not search the parent or sibling processes.

void __folio_set_anon(struct [folio](mm-api.md#c.__folio_set_anon "folio") \*folio, struct vm_area_struct \*vma, unsigned long address, bool exclusive)
:   set up a new anonymous rmap for a folio

**Parameters**

`struct folio *folio`
:   The folio to set up the new anonymous rmap for.

`struct vm_area_struct *vma`
:   VM area to add the folio to.

`unsigned long address`
:   User virtual address of the mapping

`bool exclusive`
:   Whether the folio is exclusive to the process.

void __page_check_anon_rmap(struct [folio](mm-api.md#c.__page_check_anon_rmap "folio") \*folio, struct [page](mm-api.md#c.__page_check_anon_rmap "page") \*page, struct vm_area_struct \*vma, unsigned long address)
:   sanity check anonymous rmap addition

**Parameters**

`struct folio *folio`
:   The folio containing **page**.

`struct page *page`
:   the page to check the mapping of

`struct vm_area_struct *vma`
:   the vm area in which the mapping is added

`unsigned long address`
:   the user virtual address mapped

void folio_add_anon_rmap_ptes(struct [folio](mm-api.md#c.folio_add_anon_rmap_ptes "folio") \*folio, struct [page](mm-api.md#c.folio_add_anon_rmap_ptes "page") \*page, int nr_pages, struct vm_area_struct \*vma, unsigned long address, rmap_t flags)
:   add PTE mappings to a page range of an anon folio

**Parameters**

`struct folio *folio`
:   The folio to add the mappings to

`struct page *page`
:   The first page to add

`int nr_pages`
:   The number of pages which will be mapped

`struct vm_area_struct *vma`
:   The vm area in which the mappings are added

`unsigned long address`
:   The user virtual address of the first page to map

`rmap_t flags`
:   The rmap flags

**Description**

The page range of folio is defined by [first_page, first_page + nr_pages)

The caller needs to hold the page table lock, and the page must be locked in
the anon_vma case: to serialize mapping,index checking after setting,
and to ensure that an anon folio is not being upgraded racily to a KSM folio
(but KSM folios are never downgraded).

void folio_add_anon_rmap_pmd(struct [folio](mm-api.md#c.folio_add_anon_rmap_pmd "folio") \*folio, struct [page](mm-api.md#c.folio_add_anon_rmap_pmd "page") \*page, struct vm_area_struct \*vma, unsigned long address, rmap_t flags)
:   add a PMD mapping to a page range of an anon folio

**Parameters**

`struct folio *folio`
:   The folio to add the mapping to

`struct page *page`
:   The first page to add

`struct vm_area_struct *vma`
:   The vm area in which the mapping is added

`unsigned long address`
:   The user virtual address of the first page to map

`rmap_t flags`
:   The rmap flags

**Description**

The page range of folio is defined by [first_page, first_page + HPAGE_PMD_NR)

The caller needs to hold the page table lock, and the page must be locked in
the anon_vma case: to serialize mapping,index checking after setting.

void folio_add_new_anon_rmap(struct [folio](mm-api.md#c.folio_add_new_anon_rmap "folio") \*folio, struct vm_area_struct \*vma, unsigned long address)
:   Add mapping to a new anonymous folio.

**Parameters**

`struct folio *folio`
:   The folio to add the mapping to.

`struct vm_area_struct *vma`
:   the vm area in which the mapping is added

`unsigned long address`
:   the user virtual address mapped

**Description**

Like folio_add_anon_rmap_\*() but must only be called on *new* folios.
This means the inc-and-test can be bypassed.
The folio does not have to be locked.

If the folio is pmd-mappable, it is accounted as a THP. As the folio
is new, it's assumed to be mapped exclusively by a single process.

void folio_add_file_rmap_ptes(struct [folio](mm-api.md#c.folio_add_file_rmap_ptes "folio") \*folio, struct [page](mm-api.md#c.folio_add_file_rmap_ptes "page") \*page, int nr_pages, struct vm_area_struct \*vma)
:   add PTE mappings to a page range of a folio

**Parameters**

`struct folio *folio`
:   The folio to add the mappings to

`struct page *page`
:   The first page to add

`int nr_pages`
:   The number of pages that will be mapped using PTEs

`struct vm_area_struct *vma`
:   The vm area in which the mappings are added

**Description**

The page range of the folio is defined by [page, page + nr_pages)

The caller needs to hold the page table lock.

void folio_add_file_rmap_pmd(struct [folio](mm-api.md#c.folio_add_file_rmap_pmd "folio") \*folio, struct [page](mm-api.md#c.folio_add_file_rmap_pmd "page") \*page, struct vm_area_struct \*vma)
:   add a PMD mapping to a page range of a folio

**Parameters**

`struct folio *folio`
:   The folio to add the mapping to

`struct page *page`
:   The first page to add

`struct vm_area_struct *vma`
:   The vm area in which the mapping is added

**Description**

The page range of the folio is defined by [page, page + HPAGE_PMD_NR)

The caller needs to hold the page table lock.

void folio_remove_rmap_ptes(struct [folio](mm-api.md#c.folio_remove_rmap_ptes "folio") \*folio, struct [page](mm-api.md#c.folio_remove_rmap_ptes "page") \*page, int nr_pages, struct vm_area_struct \*vma)
:   remove PTE mappings from a page range of a folio

**Parameters**

`struct folio *folio`
:   The folio to remove the mappings from

`struct page *page`
:   The first page to remove

`int nr_pages`
:   The number of pages that will be removed from the mapping

`struct vm_area_struct *vma`
:   The vm area from which the mappings are removed

**Description**

The page range of the folio is defined by [page, page + nr_pages)

The caller needs to hold the page table lock.

void folio_remove_rmap_pmd(struct [folio](mm-api.md#c.folio_remove_rmap_pmd "folio") \*folio, struct [page](mm-api.md#c.folio_remove_rmap_pmd "page") \*page, struct vm_area_struct \*vma)
:   remove a PMD mapping from a page range of a folio

**Parameters**

`struct folio *folio`
:   The folio to remove the mapping from

`struct page *page`
:   The first page to remove

`struct vm_area_struct *vma`
:   The vm area from which the mapping is removed

**Description**

The page range of the folio is defined by [page, page + HPAGE_PMD_NR)

The caller needs to hold the page table lock.

void try_to_unmap(struct [folio](mm-api.md#c.try_to_unmap "folio") \*folio, enum ttu_flags flags)
:   Try to remove all page table mappings to a folio.

**Parameters**

`struct folio *folio`
:   The folio to unmap.

`enum ttu_flags flags`
:   action and flags

**Description**

Tries to remove all the page table entries which are mapping this
folio. It is the caller's responsibility to check if the folio is
still mapped if needed (use TTU_SYNC to prevent accounting races).

**Context**

Caller must hold the folio lock.

void try_to_migrate(struct [folio](mm-api.md#c.try_to_migrate "folio") \*folio, enum ttu_flags flags)
:   try to replace all page table mappings with swap entries

**Parameters**

`struct folio *folio`
:   the folio to replace page table entries for

`enum ttu_flags flags`
:   action and flags

**Description**

Tries to remove all the page table entries which are mapping this folio and
replace them with special swap entries. Caller must hold the folio lock.

bool folio_make_device_exclusive(struct [folio](mm-api.md#c.folio_make_device_exclusive "folio") \*folio, struct mm_struct \*mm, unsigned long address, void \*owner)
:   Mark the folio exclusively owned by a device.

**Parameters**

`struct folio *folio`
:   The folio to replace page table entries for.

`struct mm_struct *mm`
:   The mm_struct where the folio is expected to be mapped.

`unsigned long address`
:   Address where the folio is expected to be mapped.

`void *owner`
:   passed to MMU_NOTIFY_EXCLUSIVE range notifier callbacks

**Description**

Tries to remove all the page table entries which are mapping this
folio and replace them with special device exclusive swap entries to
grant a device exclusive access to the folio.

**Context**

Caller must hold the folio lock.

**Return**

false if the page is still mapped, or if it could not be unmapped
from the expected address. Otherwise returns true (success).

int make_device_exclusive_range(struct mm_struct \*mm, unsigned long start, unsigned long end, struct page \*\*pages, void \*owner)
:   Mark a range for exclusive use by a device

**Parameters**

`struct mm_struct *mm`
:   mm_struct of associated target process

`unsigned long start`
:   start of the region to mark for exclusive device access

`unsigned long end`
:   end address of region

`struct page **pages`
:   returns the pages which were successfully marked for exclusive access

`void *owner`
:   passed to MMU_NOTIFY_EXCLUSIVE range notifier to allow filtering

**Return**

number of pages found in the range by GUP. A page is marked for
exclusive access only if the page pointer is non-NULL.

**Description**

This function finds ptes mapping page(s) to the given address range, locks
them and replaces mappings with special swap entries preventing userspace CPU
access. On fault these entries are replaced with the original mapping after
calling MMU notifiers.

A driver using this to program access from a device must use a mmu notifier
critical section to hold a device specific lock during programming. Once
programming is complete it should drop the page lock and reference after
which point CPU access to the page will revoke the exclusive access.

int migrate_folio(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, struct [folio](mm-api.md#c.folio "folio") \*dst, struct [folio](mm-api.md#c.folio "folio") \*src, enum migrate_mode mode)
:   Simple folio migration.

**Parameters**

`struct address_space *mapping`
:   The address_space containing the folio.

`struct folio *dst`
:   The folio to migrate the data to.

`struct folio *src`
:   The folio containing the current data.

`enum migrate_mode mode`
:   How to migrate the page.

**Description**

Common logic to directly migrate a single LRU folio suitable for
folios that do not use PagePrivate/PagePrivate2.

Folios are locked upon entry and exit.

int buffer_migrate_folio(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, struct [folio](mm-api.md#c.folio "folio") \*dst, struct [folio](mm-api.md#c.folio "folio") \*src, enum migrate_mode mode)
:   Migration function for folios with buffers.

**Parameters**

`struct address_space *mapping`
:   The address space containing **src**.

`struct folio *dst`
:   The folio to migrate to.

`struct folio *src`
:   The folio to migrate from.

`enum migrate_mode mode`
:   How to migrate the folio.

**Description**

This function can only be used if the underlying filesystem guarantees
that no other references to **src** exist. For example attached buffer
heads are accessed only under the folio lock. If your filesystem cannot
provide this guarantee, [`buffer_migrate_folio_norefs()`](mm-api.md#c.buffer_migrate_folio_norefs "buffer_migrate_folio_norefs") may be more
appropriate.

**Return**

0 on success or a negative errno on failure.

int buffer_migrate_folio_norefs(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, struct [folio](mm-api.md#c.folio "folio") \*dst, struct [folio](mm-api.md#c.folio "folio") \*src, enum migrate_mode mode)
:   Migration function for folios with buffers.

**Parameters**

`struct address_space *mapping`
:   The address space containing **src**.

`struct folio *dst`
:   The folio to migrate to.

`struct folio *src`
:   The folio to migrate from.

`enum migrate_mode mode`
:   How to migrate the folio.

**Description**

Like [`buffer_migrate_folio()`](mm-api.md#c.buffer_migrate_folio "buffer_migrate_folio") except that this variant is more careful
and checks that there are also no buffer head references. This function
is the right one for mappings where buffer heads are directly looked
up and referenced (such as block device mappings).

**Return**

0 on success or a negative errno on failure.

unsigned long unmapped_area(struct vm_unmapped_area_info \*info)
:   Find an area between the low_limit and the high_limit with the correct alignment and offset, all from **info**. Note: current->mm is used for the search.

**Parameters**

`struct vm_unmapped_area_info *info`
:   The unmapped area information including the range [low_limit -
    high_limit), the alignment offset and mask.

**Return**

A memory address or -ENOMEM.

unsigned long unmapped_area_topdown(struct vm_unmapped_area_info \*info)
:   Find an area between the low_limit and the high_limit with the correct alignment and offset at the highest available address, all from **info**. Note: current->mm is used for the search.

**Parameters**

`struct vm_unmapped_area_info *info`
:   The unmapped area information including the range [low_limit -
    high_limit), the alignment offset and mask.

**Return**

A memory address or -ENOMEM.

struct vm_area_struct \*find_vma_intersection(struct mm_struct \*mm, unsigned long start_addr, unsigned long end_addr)
:   Look up the first VMA which intersects the interval

**Parameters**

`struct mm_struct *mm`
:   The process address space.

`unsigned long start_addr`
:   The inclusive start user address.

`unsigned long end_addr`
:   The exclusive end user address.

**Return**

The first VMA within the provided range, `NULL` otherwise. Assumes
start_addr < end_addr.

struct vm_area_struct \*find_vma(struct mm_struct \*mm, unsigned long addr)
:   Find the VMA for a given address, or the next VMA.

**Parameters**

`struct mm_struct *mm`
:   The mm_struct to check

`unsigned long addr`
:   The address

**Return**

The VMA associated with addr, or the next VMA.
May return `NULL` in the case of no VMA at addr or above.

struct vm_area_struct \*find_vma_prev(struct mm_struct \*mm, unsigned long addr, struct vm_area_struct \*\*pprev)
:   Find the VMA for a given address, or the next vma and set `pprev` to the previous VMA, if any.

**Parameters**

`struct mm_struct *mm`
:   The mm_struct to check

`unsigned long addr`
:   The address

`struct vm_area_struct **pprev`
:   The pointer to set to the previous VMA

**Description**

Note that RCU lock is missing here since the external mmap_lock() is used
instead.

**Return**

The VMA associated with **addr**, or the next vma.
May return `NULL` in the case of no vma at addr or above.

void __ref kmemleak_alloc(const void \*ptr, size_t size, int min_count, gfp_t gfp)
:   register a newly allocated object

**Parameters**

`const void *ptr`
:   pointer to beginning of the object

`size_t size`
:   size of the object

`int min_count`
:   minimum number of references to this object. If during memory
    scanning a number of references less than **min_count** is found,
    the object is reported as a memory leak. If **min_count** is 0,
    the object is never reported as a leak. If **min_count** is -1,
    the object is ignored (not scanned and not reported as a leak)

`gfp_t gfp`
:   [`kmalloc()`](mm-api.md#c.kmalloc "kmalloc") flags used for kmemleak internal memory allocations

**Description**

This function is called from the kernel allocators when a new object
(memory block) is allocated (kmem_cache_alloc, kmalloc etc.).

void __ref kmemleak_alloc_percpu(const void __percpu \*ptr, size_t size, gfp_t gfp)
:   register a newly allocated __percpu object

**Parameters**

`const void __percpu *ptr`
:   __percpu pointer to beginning of the object

`size_t size`
:   size of the object

`gfp_t gfp`
:   flags used for kmemleak internal memory allocations

**Description**

This function is called from the kernel percpu allocator when a new object
(memory block) is allocated (alloc_percpu).

void __ref kmemleak_vmalloc(const struct vm_struct \*area, size_t size, gfp_t gfp)
:   register a newly vmalloc'ed object

**Parameters**

`const struct vm_struct *area`
:   pointer to vm_struct

`size_t size`
:   size of the object

`gfp_t gfp`
:   __vmalloc() flags used for kmemleak internal memory allocations

**Description**

This function is called from the [`vmalloc()`](mm-api.md#c.vmalloc "vmalloc") kernel allocator when a new
object (memory block) is allocated.

void __ref kmemleak_free(const void \*ptr)
:   unregister a previously registered object

**Parameters**

`const void *ptr`
:   pointer to beginning of the object

**Description**

This function is called from the kernel allocators when an object (memory
block) is freed (kmem_cache_free, kfree, vfree etc.).

void __ref kmemleak_free_part(const void \*ptr, size_t size)
:   partially unregister a previously registered object

**Parameters**

`const void *ptr`
:   pointer to the beginning or inside the object. This also
    represents the start of the range to be freed

`size_t size`
:   size to be unregistered

**Description**

This function is called when only a part of a memory block is freed
(usually from the bootmem allocator).

void __ref kmemleak_free_percpu(const void __percpu \*ptr)
:   unregister a previously registered __percpu object

**Parameters**

`const void __percpu *ptr`
:   __percpu pointer to beginning of the object

**Description**

This function is called from the kernel percpu allocator when an object
(memory block) is freed (free_percpu).

void __ref kmemleak_update_trace(const void \*ptr)
:   update object allocation stack trace

**Parameters**

`const void *ptr`
:   pointer to beginning of the object

**Description**

Override the object allocation stack trace for cases where the actual
allocation place is not always useful.

void __ref kmemleak_not_leak(const void \*ptr)
:   mark an allocated object as false positive

**Parameters**

`const void *ptr`
:   pointer to beginning of the object

**Description**

Calling this function on an object will cause the memory block to no longer
be reported as leak and always be scanned.

void __ref kmemleak_ignore(const void \*ptr)
:   ignore an allocated object

**Parameters**

`const void *ptr`
:   pointer to beginning of the object

**Description**

Calling this function on an object will cause the memory block to be
ignored (not scanned and not reported as a leak). This is usually done when
it is known that the corresponding block is not a leak and does not contain
any references to other allocated memory blocks.

void __ref kmemleak_scan_area(const void \*ptr, size_t size, gfp_t gfp)
:   limit the range to be scanned in an allocated object

**Parameters**

`const void *ptr`
:   pointer to beginning or inside the object. This also
    represents the start of the scan area

`size_t size`
:   size of the scan area

`gfp_t gfp`
:   [`kmalloc()`](mm-api.md#c.kmalloc "kmalloc") flags used for kmemleak internal memory allocations

**Description**

This function is used when it is known that only certain parts of an object
contain references to other objects. Kmemleak will only scan these areas
reducing the number false negatives.

void __ref kmemleak_no_scan(const void \*ptr)
:   do not scan an allocated object

**Parameters**

`const void *ptr`
:   pointer to beginning of the object

**Description**

This function notifies kmemleak not to scan the given memory block. Useful
in situations where it is known that the given object does not contain any
references to other objects. Kmemleak will not scan such objects reducing
the number of false negatives.

void __ref kmemleak_alloc_phys(phys_addr_t phys, size_t size, gfp_t gfp)
:   similar to kmemleak_alloc but taking a physical address argument

**Parameters**

`phys_addr_t phys`
:   physical address of the object

`size_t size`
:   size of the object

`gfp_t gfp`
:   [`kmalloc()`](mm-api.md#c.kmalloc "kmalloc") flags used for kmemleak internal memory allocations

void __ref kmemleak_free_part_phys(phys_addr_t phys, size_t size)
:   similar to kmemleak_free_part but taking a physical address argument

**Parameters**

`phys_addr_t phys`
:   physical address if the beginning or inside an object. This
    also represents the start of the range to be freed

`size_t size`
:   size to be unregistered

void __ref kmemleak_ignore_phys(phys_addr_t phys)
:   similar to kmemleak_ignore but taking a physical address argument

**Parameters**

`phys_addr_t phys`
:   physical address of the object

void \*devm_memremap_pages(struct [device](../driver-api/infrastructure.md#c.device "device") \*dev, struct dev_pagemap \*pgmap)
:   remap and provide memmap backing for the given resource

**Parameters**

`struct device *dev`
:   hosting device for **res**

`struct dev_pagemap *pgmap`
:   pointer to a struct dev_pagemap

**Notes**

1/ At a minimum the range and type members of **pgmap** must be initialized
:   by the caller before passing it to this function

**Description**

2/ The altmap field may optionally be initialized, in which case
:   PGMAP_ALTMAP_VALID must be set in pgmap->flags.

3/ The ref field may optionally be provided, in which pgmap->ref must be
:   'live' on entry and will be killed and reaped at
    devm_memremap_pages_release() time, or if this routine fails.

4/ range is expected to be a host memory range that could feasibly be
:   treated as a "System RAM" range, i.e. not a device mmio range, but
    this is not enforced.

struct dev_pagemap \*get_dev_pagemap(unsigned long pfn, struct dev_pagemap \*pgmap)
:   take a new live reference on the dev_pagemap for **pfn**

**Parameters**

`unsigned long pfn`
:   page frame number to lookup page_map

`struct dev_pagemap *pgmap`
:   optional known pgmap that already has a reference

**Description**

If **pgmap** is non-NULL and covers **pfn** it will be returned as-is. If **pgmap**
is non-NULL but does not cover **pfn** the reference to it will be released.

unsigned long vma_kernel_pagesize(struct vm_area_struct \*vma)
:   Page size granularity for this VMA.

**Parameters**

`struct vm_area_struct *vma`
:   The user mapping.

**Description**

Folios in this VMA will be aligned to, and at least the size of the
number of bytes returned by this function.

**Return**

The default size of the folios allocated when backing a VMA.

void put_pages_list(struct list_head \*pages)
:   release a list of pages

**Parameters**

`struct list_head *pages`
:   list of pages threaded on page->lru

**Description**

Release a list of pages which are strung together on page.lru.

void folio_add_lru(struct [folio](mm-api.md#c.folio_add_lru "folio") \*folio)
:   Add a folio to an LRU list.

**Parameters**

`struct folio *folio`
:   The folio to be added to the LRU.

**Description**

Queue the folio for addition to the LRU. The decision on whether
to add the page to the [in]active [file|anon] list is deferred until the
folio_batch is drained. This gives a chance for the caller of [`folio_add_lru()`](mm-api.md#c.folio_add_lru "folio_add_lru")
have the folio added to the active list using folio_mark_accessed().

void folio_add_lru_vma(struct [folio](mm-api.md#c.folio_add_lru_vma "folio") \*folio, struct vm_area_struct \*vma)
:   Add a folio to the appropate LRU list for this VMA.

**Parameters**

`struct folio *folio`
:   The folio to be added to the LRU.

`struct vm_area_struct *vma`
:   VMA in which the folio is mapped.

**Description**

If the VMA is mlocked, **folio** is added to the unevictable list.
Otherwise, it is treated the same way as [`folio_add_lru()`](mm-api.md#c.folio_add_lru "folio_add_lru").

void deactivate_file_folio(struct [folio](mm-api.md#c.deactivate_file_folio "folio") \*folio)
:   Deactivate a file folio.

**Parameters**

`struct folio *folio`
:   Folio to deactivate.

**Description**

This function hints to the VM that **folio** is a good reclaim candidate,
for example if its invalidation fails due to the folio being dirty
or under writeback.

**Context**

Caller holds a reference on the folio.

void folio_mark_lazyfree(struct [folio](mm-api.md#c.folio_mark_lazyfree "folio") \*folio)
:   make an anon folio lazyfree

**Parameters**

`struct folio *folio`
:   folio to deactivate

**Description**

[`folio_mark_lazyfree()`](mm-api.md#c.folio_mark_lazyfree "folio_mark_lazyfree") moves **folio** to the inactive file list.
This is done to accelerate the reclaim of **folio**.

void release_pages(release_pages_arg arg, int nr)
:   batched put_page()

**Parameters**

`release_pages_arg arg`
:   array of pages to release

`int nr`
:   number of pages

**Description**

Decrement the reference count on all the pages in **arg**. If it
fell to zero, remove the page from the LRU and free it.

Note that the argument can be an array of pages, encoded pages,
or folio pointers. We ignore any encoded bits, and turn any of
them into just a folio that gets free'd.

void folio_batch_remove_exceptionals(struct folio_batch \*fbatch)
:   Prune non-folios from a batch.

**Parameters**

`struct folio_batch *fbatch`
:   The batch to prune

**Description**

find_get_entries() fills a batch with both folios and shadow/swap/DAX
entries. This function prunes all the non-folio entries from **fbatch**
without leaving holes, so that it can be passed on to folio-only batch
operations.

void zpool_register_driver(struct zpool_driver \*driver)
:   register a zpool implementation.

**Parameters**

`struct zpool_driver *driver`
:   driver to register

int zpool_unregister_driver(struct zpool_driver \*driver)
:   unregister a zpool implementation.

**Parameters**

`struct zpool_driver *driver`
:   driver to unregister.

**Description**

Module usage counting is used to prevent using a driver
while/after unloading, so if this is called from module
exit function, this should never fail; if called from
other than the module exit function, and this returns
failure, the driver is in use and must remain available.

bool zpool_has_pool(char \*type)
:   Check if the pool driver is available

**Parameters**

`char *type`
:   The type of the zpool to check (e.g. zbud, zsmalloc)

**Description**

This checks if the **type** pool driver is available. This will try to load
the requested module, if needed, but there is no guarantee the module will
still be loaded and available immediately after calling. If this returns
true, the caller should assume the pool is available, but must be prepared
to handle the **[`zpool_create_pool()`](mm-api.md#c.zpool_create_pool "zpool_create_pool")** returning failure. However if this
returns false, the caller should assume the requested pool type is not
available; either the requested pool type module does not exist, or could
not be loaded, and calling **[`zpool_create_pool()`](mm-api.md#c.zpool_create_pool "zpool_create_pool")** with the pool type will
fail.

The **type** string must be null-terminated.

**Return**

true if **type** pool is available, false if not

struct zpool \*zpool_create_pool(const char \*type, const char \*name, gfp_t gfp)
:   Create a new zpool

**Parameters**

`const char *type`
:   The type of the zpool to create (e.g. zbud, zsmalloc)

`const char *name`
:   The name of the zpool (e.g. zram0, zswap)

`gfp_t gfp`
:   The GFP flags to use when allocating the pool.

**Description**

This creates a new zpool of the specified type. The gfp flags will be
used when allocating memory, if the implementation supports it. If the
ops param is NULL, then the created zpool will not be evictable.

Implementations must guarantee this to be thread-safe.

The **type** and **name** strings must be null-terminated.

**Return**

New zpool on success, NULL on failure.

void zpool_destroy_pool(struct [zpool](mm-api.md#c.zpool_destroy_pool "zpool") \*zpool)
:   Destroy a zpool

**Parameters**

`struct zpool *zpool`
:   The zpool to destroy.

**Description**

Implementations must guarantee this to be thread-safe,
however only when destroying different pools. The same
pool should only be destroyed once, and should not be used
after it is destroyed.

This destroys an existing zpool. The zpool should not be in use.

const char \*zpool_get_type(struct [zpool](mm-api.md#c.zpool_get_type "zpool") \*zpool)
:   Get the type of the zpool

**Parameters**

`struct zpool *zpool`
:   The zpool to check

**Description**

This returns the type of the pool.

Implementations must guarantee this to be thread-safe.

**Return**

The type of zpool.

bool zpool_malloc_support_movable(struct [zpool](mm-api.md#c.zpool_malloc_support_movable "zpool") \*zpool)
:   Check if the zpool supports allocating movable memory

**Parameters**

`struct zpool *zpool`
:   The zpool to check

**Description**

This returns if the zpool supports allocating movable memory.

Implementations must guarantee this to be thread-safe.

**Return**

true if the zpool supports allocating movable memory, false if not

int zpool_malloc(struct [zpool](mm-api.md#c.zpool_malloc "zpool") \*zpool, size_t size, gfp_t gfp, unsigned long \*handle)
:   Allocate memory

**Parameters**

`struct zpool *zpool`
:   The zpool to allocate from.

`size_t size`
:   The amount of memory to allocate.

`gfp_t gfp`
:   The GFP flags to use when allocating memory.

`unsigned long *handle`
:   Pointer to the handle to set

**Description**

This allocates the requested amount of memory from the pool.
The gfp flags will be used when allocating memory, if the
implementation supports it. The provided **handle** will be
set to the allocated object handle.

Implementations must guarantee this to be thread-safe.

**Return**

0 on success, negative value on error.

void zpool_free(struct [zpool](mm-api.md#c.zpool_free "zpool") \*zpool, unsigned long handle)
:   Free previously allocated memory

**Parameters**

`struct zpool *zpool`
:   The zpool that allocated the memory.

`unsigned long handle`
:   The handle to the memory to free.

**Description**

This frees previously allocated memory. This does not guarantee
that the pool will actually free memory, only that the memory
in the pool will become available for use by the pool.

Implementations must guarantee this to be thread-safe,
however only when freeing different handles. The same
handle should only be freed once, and should not be used
after freeing.

void \*zpool_map_handle(struct [zpool](mm-api.md#c.zpool_map_handle "zpool") \*zpool, unsigned long handle, enum zpool_mapmode mapmode)
:   Map a previously allocated handle into memory

**Parameters**

`struct zpool *zpool`
:   The zpool that the handle was allocated from

`unsigned long handle`
:   The handle to map

`enum zpool_mapmode mapmode`
:   How the memory should be mapped

**Description**

This maps a previously allocated handle into memory. The **mapmode**
param indicates to the implementation how the memory will be
used, i.e. read-only, write-only, read-write. If the
implementation does not support it, the memory will be treated
as read-write.

This may hold locks, disable interrupts, and/or preemption,
and the [`zpool_unmap_handle()`](mm-api.md#c.zpool_unmap_handle "zpool_unmap_handle") must be called to undo those
actions. The code that uses the mapped handle should complete
its operations on the mapped handle memory quickly and unmap
as soon as possible. As the implementation may use per-cpu
data, multiple handles should not be mapped concurrently on
any cpu.

**Return**

A pointer to the handle's mapped memory area.

void zpool_unmap_handle(struct [zpool](mm-api.md#c.zpool_unmap_handle "zpool") \*zpool, unsigned long handle)
:   Unmap a previously mapped handle

**Parameters**

`struct zpool *zpool`
:   The zpool that the handle was allocated from

`unsigned long handle`
:   The handle to unmap

**Description**

This unmaps a previously mapped handle. Any locks or other
actions that the implementation took in [`zpool_map_handle()`](mm-api.md#c.zpool_map_handle "zpool_map_handle")
will be undone here. The memory area returned from
[`zpool_map_handle()`](mm-api.md#c.zpool_map_handle "zpool_map_handle") should no longer be used after this.

u64 zpool_get_total_size(struct [zpool](mm-api.md#c.zpool_get_total_size "zpool") \*zpool)
:   The total size of the pool

**Parameters**

`struct zpool *zpool`
:   The zpool to check

**Description**

This returns the total size in bytes of the pool.

**Return**

Total size of the zpool in bytes.

bool zpool_can_sleep_mapped(struct [zpool](mm-api.md#c.zpool_can_sleep_mapped "zpool") \*zpool)
:   Test if zpool can sleep when do mapped.

**Parameters**

`struct zpool *zpool`
:   The zpool to test

**Description**

Some allocators enter non-preemptible context in ->map() callback (e.g.
disable pagefaults) and exit that context in ->unmap(), which limits what
we can do with the mapped object. For instance, we cannot wait for
asynchronous crypto API to decompress such an object or take mutexes
since those will call into the scheduler. This function tells us whether
we use such an allocator.

**Return**

true if zpool can sleep; false otherwise.

struct cgroup_subsys_state \*mem_cgroup_css_from_folio(struct [folio](mm-api.md#c.mem_cgroup_css_from_folio "folio") \*folio)
:   css of the memcg associated with a folio

**Parameters**

`struct folio *folio`
:   folio of interest

**Description**

If memcg is bound to the default hierarchy, css of the memcg associated
with **folio** is returned. The returned css remains associated with **folio**
until it is released.

If memcg is bound to a traditional hierarchy, the css of root_mem_cgroup
is returned.

ino_t page_cgroup_ino(struct [page](mm-api.md#c.page_cgroup_ino "page") \*page)
:   return inode number of the memcg a page is charged to

**Parameters**

`struct page *page`
:   the page

**Description**

Look up the closest online ancestor of the memory cgroup **page** is charged to
and return its inode number or 0 if **page** is not charged to any cgroup. It
is safe to call this function without holding a reference to **page**.

Note, this function is inherently racy, because there is nothing to prevent
the cgroup inode from getting torn down and potentially reallocated a moment
after [`page_cgroup_ino()`](mm-api.md#c.page_cgroup_ino "page_cgroup_ino") returns, so it only should be used by callers that
do not care (such as procfs interfaces).

void __mod_memcg_state(struct mem_cgroup \*memcg, int idx, int val)
:   update cgroup memory statistics

**Parameters**

`struct mem_cgroup *memcg`
:   the memory cgroup

`int idx`
:   the stat item - can be enum memcg_stat_item or enum node_stat_item

`int val`
:   delta to add to the counter, can be negative

void __mod_lruvec_state(struct [lruvec](mm-api.md#c.__mod_lruvec_state "lruvec") \*lruvec, enum node_stat_item idx, int val)
:   update lruvec memory statistics

**Parameters**

`struct lruvec *lruvec`
:   the lruvec

`enum node_stat_item idx`
:   the stat item

`int val`
:   delta to add to the counter, can be negative

**Description**

The lruvec is the intersection of the NUMA node and a cgroup. This
function updates the all three counters that are affected by a
change of state at this level: per-node, per-cgroup, per-lruvec.

void __count_memcg_events(struct mem_cgroup \*memcg, enum vm_event_item idx, unsigned long count)
:   account VM events in a cgroup

**Parameters**

`struct mem_cgroup *memcg`
:   the memory cgroup

`enum vm_event_item idx`
:   the event item

`unsigned long count`
:   the number of events that occurred

struct mem_cgroup \*get_mem_cgroup_from_mm(struct mm_struct \*mm)
:   Obtain a reference on given mm_struct's memcg.

**Parameters**

`struct mm_struct *mm`
:   mm from which memcg should be extracted. It can be NULL.

**Description**

Obtain a reference on mm->memcg and returns it if successful. If mm
is NULL, then the memcg is chosen as follows:
1) The active memcg, if set.
2) current->mm->memcg, if available
3) root memcg
If mem_cgroup is disabled, NULL is returned.

struct mem_cgroup \*get_mem_cgroup_from_current(void)
:   Obtain a reference on current task's memcg.

**Parameters**

`void`
:   no arguments

struct mem_cgroup \*mem_cgroup_iter(struct mem_cgroup \*root, struct mem_cgroup \*prev, struct mem_cgroup_reclaim_cookie \*reclaim)
:   iterate over memory cgroup hierarchy

**Parameters**

`struct mem_cgroup *root`
:   hierarchy root

`struct mem_cgroup *prev`
:   previously returned memcg, NULL on first invocation

`struct mem_cgroup_reclaim_cookie *reclaim`
:   cookie for shared reclaim walks, NULL for full walks

**Description**

Returns references to children of the hierarchy below **root**, or
**root** itself, or `NULL` after a full round-trip.

Caller must pass the return value in **prev** on subsequent
invocations for reference counting, or use [`mem_cgroup_iter_break()`](mm-api.md#c.mem_cgroup_iter_break "mem_cgroup_iter_break")
to cancel a hierarchy walk before the round-trip is complete.

Reclaimers can specify a node in **reclaim** to divide up the memcgs
in the hierarchy among all concurrent reclaimers operating on the
same node.

void mem_cgroup_iter_break(struct mem_cgroup \*root, struct mem_cgroup \*prev)
:   abort a hierarchy walk prematurely

**Parameters**

`struct mem_cgroup *root`
:   hierarchy root

`struct mem_cgroup *prev`
:   last visited hierarchy member as returned by [`mem_cgroup_iter()`](mm-api.md#c.mem_cgroup_iter "mem_cgroup_iter")

void mem_cgroup_scan_tasks(struct mem_cgroup \*memcg, int (\*fn)(struct task_struct\*, void\*), void \*arg)
:   iterate over tasks of a memory cgroup hierarchy

**Parameters**

`struct mem_cgroup *memcg`
:   hierarchy root

`int (*fn)(struct task_struct *, void *)`
:   function to call for each task

`void *arg`
:   argument passed to **fn**

**Description**

This function iterates over tasks attached to **memcg** or to any of its
descendants and calls **fn** for each task. If **fn** returns a non-zero
value, the function breaks the iteration loop. Otherwise, it will iterate
over all tasks and return 0.

This function must not be called for the root memory cgroup.

struct lruvec \*folio_lruvec_lock(struct [folio](mm-api.md#c.folio_lruvec_lock "folio") \*folio)
:   Lock the lruvec for a folio.

**Parameters**

`struct folio *folio`
:   Pointer to the folio.

**Description**

These functions are safe to use under any of the following conditions:
- folio locked
- folio_test_lru false
- [`folio_memcg_lock()`](mm-api.md#c.folio_memcg_lock "folio_memcg_lock")
- folio frozen (refcount of 0)

**Return**

The lruvec this folio is on with its lock held.

struct lruvec \*folio_lruvec_lock_irq(struct [folio](mm-api.md#c.folio_lruvec_lock_irq "folio") \*folio)
:   Lock the lruvec for a folio.

**Parameters**

`struct folio *folio`
:   Pointer to the folio.

**Description**

These functions are safe to use under any of the following conditions:
- folio locked
- folio_test_lru false
- [`folio_memcg_lock()`](mm-api.md#c.folio_memcg_lock "folio_memcg_lock")
- folio frozen (refcount of 0)

**Return**

The lruvec this folio is on with its lock held and interrupts
disabled.

struct lruvec \*folio_lruvec_lock_irqsave(struct [folio](mm-api.md#c.folio_lruvec_lock_irqsave "folio") \*folio, unsigned long \*flags)
:   Lock the lruvec for a folio.

**Parameters**

`struct folio *folio`
:   Pointer to the folio.

`unsigned long *flags`
:   Pointer to irqsave flags.

**Description**

These functions are safe to use under any of the following conditions:
- folio locked
- folio_test_lru false
- [`folio_memcg_lock()`](mm-api.md#c.folio_memcg_lock "folio_memcg_lock")
- folio frozen (refcount of 0)

**Return**

The lruvec this folio is on with its lock held and interrupts
disabled.

void mem_cgroup_update_lru_size(struct [lruvec](mm-api.md#c.mem_cgroup_update_lru_size "lruvec") \*lruvec, enum lru_list lru, int zid, int nr_pages)
:   account for adding or removing an lru page

**Parameters**

`struct lruvec *lruvec`
:   mem_cgroup per zone lru vector

`enum lru_list lru`
:   index of lru list the page is sitting on

`int zid`
:   zone id of the accounted pages

`int nr_pages`
:   positive when adding or negative when removing

**Description**

This function must be called under lru_lock, just before a page is added
to or just after a page is removed from an lru list.

unsigned long mem_cgroup_margin(struct mem_cgroup \*memcg)
:   calculate chargeable space of a memory cgroup

**Parameters**

`struct mem_cgroup *memcg`
:   the memory cgroup

**Description**

Returns the maximum amount of memory **mem** can be charged with, in
pages.

void mem_cgroup_print_oom_context(struct mem_cgroup \*memcg, struct task_struct \*p)
:   Print OOM information relevant to memory controller.

**Parameters**

`struct mem_cgroup *memcg`
:   The memory cgroup that went over limit

`struct task_struct *p`
:   Task that is going to be killed

**NOTE**

**memcg** and **p**'s mem_cgroup can be different when hierarchy is
enabled

void mem_cgroup_print_oom_meminfo(struct mem_cgroup \*memcg)
:   Print OOM memory information relevant to memory controller.

**Parameters**

`struct mem_cgroup *memcg`
:   The memory cgroup that went over limit

bool mem_cgroup_oom_synchronize(bool handle)
:   complete memcg OOM handling

**Parameters**

`bool handle`
:   actually kill/wait or just clean up the OOM state

**Description**

This has to be called at the end of a page fault if the memcg OOM
handler was enabled.

Memcg supports userspace OOM handling where failed allocations must
sleep on a waitqueue until the userspace task resolves the
situation. Sleeping directly in the charge context with all kinds
of locks held is not a good idea, instead we remember an OOM state
in the task and [`mem_cgroup_oom_synchronize()`](mm-api.md#c.mem_cgroup_oom_synchronize "mem_cgroup_oom_synchronize") has to be called at
the end of the page fault to complete the OOM handling.

Returns `true` if an ongoing memcg OOM situation was detected and
completed, `false` otherwise.

struct mem_cgroup \*mem_cgroup_get_oom_group(struct task_struct \*victim, struct mem_cgroup \*oom_domain)
:   get a memory cgroup to clean up after OOM

**Parameters**

`struct task_struct *victim`
:   task to be killed by the OOM killer

`struct mem_cgroup *oom_domain`
:   memcg in case of memcg OOM, NULL in case of system-wide OOM

**Description**

Returns a pointer to a memory cgroup, which has to be cleaned up
by killing all belonging OOM-killable tasks.

Caller has to call mem_cgroup_put() on the returned non-NULL memcg.

void folio_memcg_lock(struct [folio](mm-api.md#c.folio_memcg_lock "folio") \*folio)
:   Bind a folio to its memcg.

**Parameters**

`struct folio *folio`
:   The folio.

**Description**

This function prevents unlocked LRU folios from being moved to
another cgroup.

It ensures lifetime of the bound memcg. The caller is responsible
for the lifetime of the folio.

void folio_memcg_unlock(struct [folio](mm-api.md#c.folio_memcg_unlock "folio") \*folio)
:   Release the binding between a folio and its memcg.

**Parameters**

`struct folio *folio`
:   The folio.

**Description**

This releases the binding created by [`folio_memcg_lock()`](mm-api.md#c.folio_memcg_lock "folio_memcg_lock"). This does
not change the accounting of this folio to its memcg, but it does
permit others to change it.

bool consume_stock(struct mem_cgroup \*memcg, unsigned int nr_pages)
:   Try to consume stocked charge on this cpu.

**Parameters**

`struct mem_cgroup *memcg`
:   memcg to consume from.

`unsigned int nr_pages`
:   how many pages to charge.

**Description**

The charges will only happen if **memcg** matches the current cpu's memcg
stock, and at least **nr_pages** are available in that stock. Failure to
service an allocation will refill the stock.

returns true if successful, false otherwise.

void mem_cgroup_cancel_charge(struct mem_cgroup \*memcg, unsigned int nr_pages)
:   cancel an uncommitted try_charge() call.

**Parameters**

`struct mem_cgroup *memcg`
:   memcg previously charged.

`unsigned int nr_pages`
:   number of pages previously charged.

void mem_cgroup_commit_charge(struct [folio](mm-api.md#c.mem_cgroup_commit_charge "folio") \*folio, struct mem_cgroup \*memcg)
:   commit a previously successful try_charge().

**Parameters**

`struct folio *folio`
:   folio to commit the charge to.

`struct mem_cgroup *memcg`
:   memcg previously charged.

int __memcg_kmem_charge_page(struct [page](mm-api.md#c.__memcg_kmem_charge_page "page") \*page, gfp_t gfp, int order)
:   charge a kmem page to the current memory cgroup

**Parameters**

`struct page *page`
:   page to charge

`gfp_t gfp`
:   reclaim mode

`int order`
:   allocation order

**Description**

Returns 0 on success, an error code on failure.

void __memcg_kmem_uncharge_page(struct [page](mm-api.md#c.__memcg_kmem_uncharge_page "page") \*page, int order)
:   uncharge a kmem page

**Parameters**

`struct page *page`
:   page to uncharge

`int order`
:   allocation order

int mem_cgroup_move_swap_account(swp_entry_t entry, struct mem_cgroup \*from, struct mem_cgroup \*to)
:   move swap charge and swap_cgroup's record.

**Parameters**

`swp_entry_t entry`
:   swap entry to be moved

`struct mem_cgroup *from`
:   mem_cgroup which the entry is moved from

`struct mem_cgroup *to`
:   mem_cgroup which the entry is moved to

**Description**

It succeeds only when the swap_cgroup's record for this entry is the same
as the mem_cgroup's id of **from**.

Returns 0 on success, -EINVAL on failure.

The caller must have charged to **to**, IOW, called page_counter_charge() about
both res and memsw, and called css_get().

void mem_cgroup_wb_stats(struct bdi_writeback \*wb, unsigned long \*pfilepages, unsigned long \*pheadroom, unsigned long \*pdirty, unsigned long \*pwriteback)
:   retrieve writeback related stats from its memcg

**Parameters**

`struct bdi_writeback *wb`
:   bdi_writeback in question

`unsigned long *pfilepages`
:   out parameter for number of file pages

`unsigned long *pheadroom`
:   out parameter for number of allocatable pages according to memcg

`unsigned long *pdirty`
:   out parameter for number of dirty pages

`unsigned long *pwriteback`
:   out parameter for number of pages under writeback

**Description**

Determine the numbers of file, headroom, dirty, and writeback pages in
**wb**'s memcg. File, dirty and writeback are self-explanatory. Headroom
is a bit more involved.

A memcg's headroom is "min(max, high) - used". In the hierarchy, the
headroom is calculated as the lowest headroom of itself and the
ancestors. Note that this doesn't consider the actual amount of
available memory in the system. The caller should further cap
**\*pheadroom** accordingly.

struct mem_cgroup \*mem_cgroup_from_id(unsigned short id)
:   look up a memcg from a memcg id

**Parameters**

`unsigned short id`
:   the memcg id to look up

**Description**

Caller must hold [`rcu_read_lock()`](kernel-api.md#c.rcu_read_lock "rcu_read_lock").

void mem_cgroup_css_reset(struct cgroup_subsys_state \*css)
:   reset the states of a mem_cgroup

**Parameters**

`struct cgroup_subsys_state *css`
:   the target css

**Description**

Reset the states of the mem_cgroup associated with **css**. This is
invoked when the userland requests disabling on the default hierarchy
but the memcg is pinned through dependency. The memcg should stop
applying policies and should revert to the vanilla state as it may be
made visible again.

The current implementation only resets the essential configurations.
This needs to be expanded to cover all the visible parts.

int mem_cgroup_move_account(struct [page](mm-api.md#c.mem_cgroup_move_account "page") \*page, bool compound, struct mem_cgroup \*from, struct mem_cgroup \*to)
:   move account of the page

**Parameters**

`struct page *page`
:   the page

`bool compound`
:   charge the page as compound or small page

`struct mem_cgroup *from`
:   mem_cgroup which the page is moved from.

`struct mem_cgroup *to`
:   mem_cgroup which the page is moved to. **from** != **to**.

**Description**

The page must be locked and not on the LRU.

This function doesn't do "charge" to new cgroup and doesn't do "uncharge"
from old cgroup.

enum mc_target_type get_mctgt_type(struct vm_area_struct \*vma, unsigned long addr, pte_t ptent, union mc_target \*target)
:   get target type of moving charge

**Parameters**

`struct vm_area_struct *vma`
:   the vma the pte to be checked belongs

`unsigned long addr`
:   the address corresponding to the pte to be checked

`pte_t ptent`
:   the pte to be checked

`union mc_target *target`
:   the pointer the target page or swap ent will be stored(can be NULL)

**Context**

Called with pte lock held.

**Return**

- MC_TARGET_NONE - If the pte is not a target for move charge.
- MC_TARGET_PAGE - If the page corresponding to this pte is a target for
  move charge. If **target** is not NULL, the page is stored in target->page
  with extra refcnt taken (Caller should release it).
- MC_TARGET_SWAP - If the swap entry corresponding to this pte is a
  target for charge migration. If **target** is not NULL, the entry is
  stored in target->ent.
- MC_TARGET_DEVICE - Like MC_TARGET_PAGE but page is device memory and
  thus not on the lru. For now such page is charged like a regular page
  would be as it is just special memory taking the place of a regular page.
  See Documentations/vm/hmm.txt and include/linux/hmm.h

void mem_cgroup_calculate_protection(struct mem_cgroup \*root, struct mem_cgroup \*memcg)
:   check if memory consumption is in the normal range

**Parameters**

`struct mem_cgroup *root`
:   the top ancestor of the sub-tree being checked

`struct mem_cgroup *memcg`
:   the memory cgroup to check

**Description**

WARNING: This function is not stateless! It can only be used as part
:   of a top-down tree iteration, not for isolated queries.

int mem_cgroup_hugetlb_try_charge(struct mem_cgroup \*memcg, gfp_t gfp, long nr_pages)
:   try to charge the memcg for a hugetlb folio

**Parameters**

`struct mem_cgroup *memcg`
:   memcg to charge.

`gfp_t gfp`
:   reclaim mode.

`long nr_pages`
:   number of pages to charge.

**Description**

This function is called when allocating a huge page folio to determine if
the memcg has the capacity for it. It does not commit the charge yet,
as the hugetlb folio itself has not been obtained from the hugetlb pool.

Once we have obtained the hugetlb folio, we can call
[`mem_cgroup_commit_charge()`](mm-api.md#c.mem_cgroup_commit_charge "mem_cgroup_commit_charge") to commit the charge. If we fail to obtain the
folio, we should instead call [`mem_cgroup_cancel_charge()`](mm-api.md#c.mem_cgroup_cancel_charge "mem_cgroup_cancel_charge") to undo the effect
of try_charge().

Returns 0 on success. Otherwise, an error code is returned.

int mem_cgroup_swapin_charge_folio(struct [folio](mm-api.md#c.mem_cgroup_swapin_charge_folio "folio") \*folio, struct mm_struct \*mm, gfp_t gfp, swp_entry_t entry)
:   Charge a newly allocated folio for swapin.

**Parameters**

`struct folio *folio`
:   folio to charge.

`struct mm_struct *mm`
:   mm context of the victim

`gfp_t gfp`
:   reclaim mode

`swp_entry_t entry`
:   swap entry for which the folio is allocated

**Description**

This function charges a folio allocated for swapin. Please call this before
adding the folio to the swapcache.

Returns 0 on success. Otherwise, an error code is returned.

void __mem_cgroup_uncharge_list(struct list_head \*page_list)
:   uncharge a list of page

**Parameters**

`struct list_head *page_list`
:   list of pages to uncharge

**Description**

Uncharge a list of pages previously charged with
__mem_cgroup_charge().

void mem_cgroup_replace_folio(struct [folio](mm-api.md#c.folio "folio") \*old, struct [folio](mm-api.md#c.folio "folio") \*new)
:   Charge a folio's replacement.

**Parameters**

`struct folio *old`
:   Currently circulating folio.

`struct folio *new`
:   Replacement folio.

**Description**

Charge **new** as a replacement folio for **old**. **old** will
be uncharged upon free. This is only used by the page cache
(in [`replace_page_cache_folio()`](mm-api.md#c.replace_page_cache_folio "replace_page_cache_folio")).

Both folios must be locked, **new->mapping** must be set up.

void mem_cgroup_migrate(struct [folio](mm-api.md#c.folio "folio") \*old, struct [folio](mm-api.md#c.folio "folio") \*new)
:   Transfer the memcg data from the old to the new folio.

**Parameters**

`struct folio *old`
:   Currently circulating folio.

`struct folio *new`
:   Replacement folio.

**Description**

Transfer the memcg data from the old folio to the new folio for migration.
The old folio's data info will be cleared. Note that the memory counters
will remain unchanged throughout the process.

Both folios must be locked, **new->mapping** must be set up.

bool mem_cgroup_charge_skmem(struct mem_cgroup \*memcg, unsigned int nr_pages, gfp_t gfp_mask)
:   charge socket memory

**Parameters**

`struct mem_cgroup *memcg`
:   memcg to charge

`unsigned int nr_pages`
:   number of pages to charge

`gfp_t gfp_mask`
:   reclaim mode

**Description**

Charges **nr_pages** to **memcg**. Returns `true` if the charge fit within
**memcg**'s configured limit, `false` if it doesn't.

void mem_cgroup_uncharge_skmem(struct mem_cgroup \*memcg, unsigned int nr_pages)
:   uncharge socket memory

**Parameters**

`struct mem_cgroup *memcg`
:   memcg to uncharge

`unsigned int nr_pages`
:   number of pages to uncharge

void mem_cgroup_swapout(struct [folio](mm-api.md#c.mem_cgroup_swapout "folio") \*folio, swp_entry_t entry)
:   transfer a memsw charge to swap

**Parameters**

`struct folio *folio`
:   folio whose memsw charge to transfer

`swp_entry_t entry`
:   swap entry to move the charge to

**Description**

Transfer the memsw charge of **folio** to **entry**.

int __mem_cgroup_try_charge_swap(struct [folio](mm-api.md#c.__mem_cgroup_try_charge_swap "folio") \*folio, swp_entry_t entry)
:   try charging swap space for a folio

**Parameters**

`struct folio *folio`
:   folio being added to swap

`swp_entry_t entry`
:   swap entry to charge

**Description**

Try to charge **folio**'s memcg for the swap space at **entry**.

Returns 0 on success, -ENOMEM on failure.

void __mem_cgroup_uncharge_swap(swp_entry_t entry, unsigned int nr_pages)
:   uncharge swap space

**Parameters**

`swp_entry_t entry`
:   swap entry to uncharge

`unsigned int nr_pages`
:   the amount of swap space to uncharge

bool obj_cgroup_may_zswap(struct obj_cgroup \*objcg)
:   check if this cgroup can zswap

**Parameters**

`struct obj_cgroup *objcg`
:   the object cgroup

**Description**

Check if the hierarchical zswap limit has been reached.

This doesn't check for specific headroom, and it is not atomic
either. But with zswap, the size of the allocation is only known
once compression has occurred, and this optimistic pre-check avoids
spending cycles on compression when there is already no room left
or zswap is disabled altogether somewhere in the hierarchy.

void obj_cgroup_charge_zswap(struct obj_cgroup \*objcg, size_t size)
:   charge compression backend memory

**Parameters**

`struct obj_cgroup *objcg`
:   the object cgroup

`size_t size`
:   size of compressed object

**Description**

This forces the charge after [`obj_cgroup_may_zswap()`](mm-api.md#c.obj_cgroup_may_zswap "obj_cgroup_may_zswap") allowed
compression and storage in zwap for this cgroup to go ahead.

void obj_cgroup_uncharge_zswap(struct obj_cgroup \*objcg, size_t size)
:   uncharge compression backend memory

**Parameters**

`struct obj_cgroup *objcg`
:   the object cgroup

`size_t size`
:   size of compressed object

**Description**

Uncharges zswap memory on page in.

void shmem_recalc_inode(struct [inode](mm-api.md#c.shmem_recalc_inode "inode") \*inode, long alloced, long swapped)
:   recalculate the block usage of an inode

**Parameters**

`struct inode *inode`
:   inode to recalc

`long alloced`
:   the change in number of pages allocated to inode

`long swapped`
:   the change in number of pages swapped from inode

**Description**

We have to calculate the free blocks since the mm can drop
undirtied hole pages behind our back.

But normally info->alloced == inode->i_mapping->nrpages + info->swapped
So mm freed is info->alloced - (inode->i_mapping->nrpages + info->swapped)

struct file \*shmem_kernel_file_setup(const char \*name, loff_t size, unsigned long flags)
:   get an unlinked file living in tmpfs which must be kernel internal. There will be NO LSM permission checks against the underlying inode. So users of this interface must do LSM checks at a higher layer. The users are the big_key and shm implementations. LSM checks are provided at the key or shm level rather than the inode.

**Parameters**

`const char *name`
:   name for dentry (to be seen in /proc/<pid>/maps

`loff_t size`
:   size to be set for the file

`unsigned long flags`
:   VM_NORESERVE suppresses pre-accounting of the entire object size

struct file \*shmem_file_setup(const char \*name, loff_t size, unsigned long flags)
:   get an unlinked file living in tmpfs

**Parameters**

`const char *name`
:   name for dentry (to be seen in /proc/<pid>/maps

`loff_t size`
:   size to be set for the file

`unsigned long flags`
:   VM_NORESERVE suppresses pre-accounting of the entire object size

struct file \*shmem_file_setup_with_mnt(struct vfsmount \*mnt, const char \*name, loff_t size, unsigned long flags)
:   get an unlinked file living in tmpfs

**Parameters**

`struct vfsmount *mnt`
:   the tmpfs mount where the file will be created

`const char *name`
:   name for dentry (to be seen in /proc/<pid>/maps

`loff_t size`
:   size to be set for the file

`unsigned long flags`
:   VM_NORESERVE suppresses pre-accounting of the entire object size

int shmem_zero_setup(struct vm_area_struct \*vma)
:   setup a shared anonymous mapping

**Parameters**

`struct vm_area_struct *vma`
:   the vma to be mmapped is prepared by do_mmap

struct [folio](mm-api.md#c.folio "folio") \*shmem_read_folio_gfp(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, pgoff_t index, gfp_t gfp)
:   read into page cache, using specified page allocation flags.

**Parameters**

`struct address_space *mapping`
:   the folio's address_space

`pgoff_t index`
:   the folio index

`gfp_t gfp`
:   the page allocator flags to use if allocating

**Description**

This behaves as a tmpfs "read_cache_page_gfp(mapping, index, gfp)",
with any new page allocations done using the specified allocation flags.
But [`read_cache_page_gfp()`](mm-api.md#c.read_cache_page_gfp "read_cache_page_gfp") uses the ->read_folio() method: which does not
suit tmpfs, since it may have pages in swapcache, and needs to find those
for itself; although drivers/gpu/drm i915 and ttm rely upon this support.

i915_gem_object_get_pages_gtt() mixes __GFP_NORETRY | __GFP_NOWARN in
with the mapping_gfp_mask(), to avoid OOMing the machine unnecessarily.

int migrate_vma_setup(struct migrate_vma \*args)
:   prepare to migrate a range of memory

**Parameters**

`struct migrate_vma *args`
:   contains the vma, start, and pfns arrays for the migration

**Return**

negative errno on failures, 0 when 0 or more pages were migrated
without an error.

**Description**

Prepare to migrate a range of memory virtual address range by collecting all
the pages backing each virtual address in the range, saving them inside the
src array. Then lock those pages and unmap them. Once the pages are locked
and unmapped, check whether each page is pinned or not. Pages that aren't
pinned have the MIGRATE_PFN_MIGRATE flag set (by this function) in the
corresponding src array entry. Then restores any pages that are pinned, by
remapping and unlocking those pages.

The caller should then allocate destination memory and copy source memory to
it for all those entries (ie with MIGRATE_PFN_VALID and MIGRATE_PFN_MIGRATE
flag set). Once these are allocated and copied, the caller must update each
corresponding entry in the dst array with the pfn value of the destination
page and with MIGRATE_PFN_VALID. Destination pages must be locked via
[`lock_page()`](mm-api.md#c.lock_page "lock_page").

Note that the caller does not have to migrate all the pages that are marked
with MIGRATE_PFN_MIGRATE flag in src array unless this is a migration from
device memory to system memory. If the caller cannot migrate a device page
back to system memory, then it must return VM_FAULT_SIGBUS, which has severe
consequences for the userspace process, so it must be avoided if at all
possible.

For empty entries inside CPU page table (pte_none() or pmd_none() is true) we
do set MIGRATE_PFN_MIGRATE flag inside the corresponding source array thus
allowing the caller to allocate device memory for those unbacked virtual
addresses. For this the caller simply has to allocate device memory and
properly set the destination entry like for regular migration. Note that
this can still fail, and thus inside the device driver you must check if the
migration was successful for those entries after calling [`migrate_vma_pages()`](mm-api.md#c.migrate_vma_pages "migrate_vma_pages"),
just like for regular migration.

After that, the callers must call [`migrate_vma_pages()`](mm-api.md#c.migrate_vma_pages "migrate_vma_pages") to go over each entry
in the src array that has the MIGRATE_PFN_VALID and MIGRATE_PFN_MIGRATE flag
set. If the corresponding entry in dst array has MIGRATE_PFN_VALID flag set,
then [`migrate_vma_pages()`](mm-api.md#c.migrate_vma_pages "migrate_vma_pages") to migrate struct page information from the source
struct page to the destination struct page. If it fails to migrate the
struct page information, then it clears the MIGRATE_PFN_MIGRATE flag in the
src array.

At this point all successfully migrated pages have an entry in the src
array with MIGRATE_PFN_VALID and MIGRATE_PFN_MIGRATE flag set and the dst
array entry with MIGRATE_PFN_VALID flag set.

Once [`migrate_vma_pages()`](mm-api.md#c.migrate_vma_pages "migrate_vma_pages") returns the caller may inspect which pages were
successfully migrated, and which were not. Successfully migrated pages will
have the MIGRATE_PFN_MIGRATE flag set for their src array entry.

It is safe to update device page table after [`migrate_vma_pages()`](mm-api.md#c.migrate_vma_pages "migrate_vma_pages") because
both destination and source page are still locked, and the mmap_lock is held
in read mode (hence no one can unmap the range being migrated).

Once the caller is done cleaning up things and updating its page table (if it
chose to do so, this is not an obligation) it finally calls
[`migrate_vma_finalize()`](mm-api.md#c.migrate_vma_finalize "migrate_vma_finalize") to update the CPU page table to point to new pages
for successfully migrated pages or otherwise restore the CPU page table to
point to the original source pages.

void migrate_device_pages(unsigned long \*src_pfns, unsigned long \*dst_pfns, unsigned long npages)
:   migrate meta-data from src page to dst page

**Parameters**

`unsigned long *src_pfns`
:   src_pfns returned from [`migrate_device_range()`](mm-api.md#c.migrate_device_range "migrate_device_range")

`unsigned long *dst_pfns`
:   array of pfns allocated by the driver to migrate memory to

`unsigned long npages`
:   number of pages in the range

**Description**

Equivalent to [`migrate_vma_pages()`](mm-api.md#c.migrate_vma_pages "migrate_vma_pages"). This is called to migrate struct page
meta-data from source struct page to destination.

void migrate_vma_pages(struct migrate_vma \*migrate)
:   migrate meta-data from src page to dst page

**Parameters**

`struct migrate_vma *migrate`
:   migrate struct containing all migration information

**Description**

This migrates struct page meta-data from source struct page to destination
struct page. This effectively finishes the migration from source page to the
destination page.

void migrate_vma_finalize(struct migrate_vma \*migrate)
:   restore CPU page table entry

**Parameters**

`struct migrate_vma *migrate`
:   migrate struct containing all migration information

**Description**

This replaces the special migration pte entry with either a mapping to the
new page if migration was successful for that page, or to the original page
otherwise.

This also unlocks the pages and puts them back on the lru, or drops the extra
refcount, for device pages.

int migrate_device_range(unsigned long \*src_pfns, unsigned long start, unsigned long npages)
:   migrate device private pfns to normal memory.

**Parameters**

`unsigned long *src_pfns`
:   array large enough to hold migrating source device private pfns.

`unsigned long start`
:   starting pfn in the range to migrate.

`unsigned long npages`
:   number of pages to migrate.

**Description**

[`migrate_vma_setup()`](mm-api.md#c.migrate_vma_setup "migrate_vma_setup") is similar in concept to [`migrate_vma_setup()`](mm-api.md#c.migrate_vma_setup "migrate_vma_setup") except that
instead of looking up pages based on virtual address mappings a range of
device pfns that should be migrated to system memory is used instead.

This is useful when a driver needs to free device memory but doesn't know the
virtual mappings of every page that may be in device memory. For example this
is often the case when a driver is being unloaded or unbound from a device.

Like [`migrate_vma_setup()`](mm-api.md#c.migrate_vma_setup "migrate_vma_setup") this function will take a reference and lock any
migrating pages that aren't free before unmapping them. Drivers may then
allocate destination pages and start copying data from the device to CPU
memory before calling [`migrate_device_pages()`](mm-api.md#c.migrate_device_pages "migrate_device_pages").

struct wp_walk
:   Private struct for pagetable walk callbacks

**Definition**:

```
struct wp_walk {
    struct mmu_notifier_range range;
    unsigned long tlbflush_start;
    unsigned long tlbflush_end;
    unsigned long total;
};
```

**Members**

`range`
:   Range for mmu notifiers

`tlbflush_start`
:   Address of first modified pte

`tlbflush_end`
:   Address of last modified pte + 1

`total`
:   Total number of modified ptes

int wp_pte(pte_t \*pte, unsigned long addr, unsigned long end, struct mm_walk \*walk)
:   Write-protect a pte

**Parameters**

`pte_t *pte`
:   Pointer to the pte

`unsigned long addr`
:   The start of protecting virtual address

`unsigned long end`
:   The end of protecting virtual address

`struct mm_walk *walk`
:   pagetable walk callback argument

**Description**

The function write-protects a pte and records the range in
virtual address space of touched ptes for efficient range TLB flushes.

struct clean_walk
:   Private struct for the clean_record_pte function.

**Definition**:

```
struct clean_walk {
    struct wp_walk base;
    pgoff_t bitmap_pgoff;
    unsigned long *bitmap;
    pgoff_t start;
    pgoff_t end;
};
```

**Members**

`base`
:   [`struct wp_walk`](mm-api.md#c.wp_walk "wp_walk") we derive from

`bitmap_pgoff`
:   Address_space Page offset of the first bit in **bitmap**

`bitmap`
:   Bitmap with one bit for each page offset in the address_space range
    covered.

`start`
:   Address_space page offset of first modified pte relative
    to **bitmap_pgoff**

`end`
:   Address_space page offset of last modified pte relative
    to **bitmap_pgoff**

int clean_record_pte(pte_t \*pte, unsigned long addr, unsigned long end, struct mm_walk \*walk)
:   Clean a pte and record its address space offset in a bitmap

**Parameters**

`pte_t *pte`
:   Pointer to the pte

`unsigned long addr`
:   The start of virtual address to be clean

`unsigned long end`
:   The end of virtual address to be clean

`struct mm_walk *walk`
:   pagetable walk callback argument

**Description**

The function cleans a pte and records the range in
virtual address space of touched ptes for efficient TLB flushes.
It also records dirty ptes in a bitmap representing page offsets
in the address_space, as well as the first and last of the bits
touched.

unsigned long wp_shared_mapping_range(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, pgoff_t first_index, pgoff_t nr)
:   Write-protect all ptes in an address space range

**Parameters**

`struct address_space *mapping`
:   The address_space we want to write protect

`pgoff_t first_index`
:   The first page offset in the range

`pgoff_t nr`
:   Number of incremental page offsets to cover

**Note**

This function currently skips transhuge page-table entries, since
it's intended for dirty-tracking on the PTE level. It will warn on
encountering transhuge write-enabled entries, though, and can easily be
extended to handle them as well.

**Return**

The number of ptes actually write-protected. Note that
already write-protected ptes are not counted.

unsigned long clean_record_shared_mapping_range(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, pgoff_t first_index, pgoff_t nr, pgoff_t bitmap_pgoff, unsigned long \*bitmap, pgoff_t \*start, pgoff_t \*end)
:   Clean and record all ptes in an address space range

**Parameters**

`struct address_space *mapping`
:   The address_space we want to clean

`pgoff_t first_index`
:   The first page offset in the range

`pgoff_t nr`
:   Number of incremental page offsets to cover

`pgoff_t bitmap_pgoff`
:   The page offset of the first bit in **bitmap**

`unsigned long *bitmap`
:   Pointer to a bitmap of at least **nr** bits. The bitmap needs to
    cover the whole range **first_index**..\*\*first_index\*\* + **nr**.

`pgoff_t *start`
:   Pointer to number of the first set bit in **bitmap**.
    is modified as new bits are set by the function.

`pgoff_t *end`
:   Pointer to the number of the last set bit in **bitmap**.
    none set. The value is modified as new bits are set by the function.

**Description**

When this function returns there is no guarantee that a CPU has
not already dirtied new ptes. However it will not clean any ptes not
reported in the bitmap. The guarantees are as follows:

- All ptes dirty when the function starts executing will end up recorded
  in the bitmap.
- All ptes dirtied after that will either remain dirty, be recorded in the
  bitmap or both.

If a caller needs to make sure all dirty ptes are picked up and none
additional are added, it first needs to write-protect the address-space
range and make sure new writers are blocked in page_mkwrite() or
pfn_mkwrite(). And then after a TLB flush following the write-protection
pick up all dirty bits.

This function currently skips transhuge page-table entries, since
it's intended for dirty-tracking on the PTE level. It will warn on
encountering transhuge dirty entries, though, and can easily be extended
to handle them as well.

**Return**

The number of dirty ptes actually cleaned.

bool pcpu_addr_in_chunk(struct pcpu_chunk \*chunk, void \*addr)
:   check if the address is served from this chunk

**Parameters**

`struct pcpu_chunk *chunk`
:   chunk of interest

`void *addr`
:   percpu address

**Return**

True if the address is served from this chunk.

bool pcpu_check_block_hint(struct pcpu_block_md \*block, int bits, size_t align)
:   check against the contig hint

**Parameters**

`struct pcpu_block_md *block`
:   block of interest

`int bits`
:   size of allocation

`size_t align`
:   alignment of area (max PAGE_SIZE)

**Description**

Check to see if the allocation can fit in the block's contig hint.
Note, a chunk uses the same hints as a block so this can also check against
the chunk's contig hint.

void pcpu_next_md_free_region(struct pcpu_chunk \*chunk, int \*bit_off, int \*bits)
:   finds the next hint free area

**Parameters**

`struct pcpu_chunk *chunk`
:   chunk of interest

`int *bit_off`
:   chunk offset

`int *bits`
:   size of free area

**Description**

Helper function for pcpu_for_each_md_free_region. It checks
block->contig_hint and performs aggregation across blocks to find the
next hint. It modifies bit_off and bits in-place to be consumed in the
loop.

void pcpu_next_fit_region(struct pcpu_chunk \*chunk, int alloc_bits, int align, int \*bit_off, int \*bits)
:   finds fit areas for a given allocation request

**Parameters**

`struct pcpu_chunk *chunk`
:   chunk of interest

`int alloc_bits`
:   size of allocation

`int align`
:   alignment of area (max PAGE_SIZE)

`int *bit_off`
:   chunk offset

`int *bits`
:   size of free area

**Description**

Finds the next free region that is viable for use with a given size and
alignment. This only returns if there is a valid area to be used for this
allocation. block->first_free is returned if the allocation request fits
within the block to see if the request can be fulfilled prior to the contig
hint.

void \*pcpu_mem_zalloc(size_t size, gfp_t gfp)
:   allocate memory

**Parameters**

`size_t size`
:   bytes to allocate

`gfp_t gfp`
:   allocation flags

**Description**

Allocate **size** bytes. If **size** is smaller than PAGE_SIZE,
[`kzalloc()`](mm-api.md#c.kzalloc "kzalloc") is used; otherwise, the equivalent of [`vzalloc()`](mm-api.md#c.vzalloc "vzalloc") is used.
This is to facilitate passing through whitelisted flags. The
returned memory is always zeroed.

**Return**

Pointer to the allocated area on success, NULL on failure.

void pcpu_mem_free(void \*ptr)
:   free memory

**Parameters**

`void *ptr`
:   memory to free

**Description**

Free **ptr**. **ptr** should have been allocated using [`pcpu_mem_zalloc()`](mm-api.md#c.pcpu_mem_zalloc "pcpu_mem_zalloc").

void pcpu_chunk_relocate(struct pcpu_chunk \*chunk, int oslot)
:   put chunk in the appropriate chunk slot

**Parameters**

`struct pcpu_chunk *chunk`
:   chunk of interest

`int oslot`
:   the previous slot it was on

**Description**

This function is called after an allocation or free changed **chunk**.
New slot according to the changed state is determined and **chunk** is
moved to the slot. Note that the reserved chunk is never put on
chunk slots.

**Context**

pcpu_lock.

void pcpu_block_update(struct pcpu_block_md \*block, int start, int end)
:   updates a block given a free area

**Parameters**

`struct pcpu_block_md *block`
:   block of interest

`int start`
:   start offset in block

`int end`
:   end offset in block

**Description**

Updates a block given a known free area. The region [start, end) is
expected to be the entirety of the free area within a block. Chooses
the best starting offset if the contig hints are equal.

void pcpu_chunk_refresh_hint(struct pcpu_chunk \*chunk, bool full_scan)
:   updates metadata about a chunk

**Parameters**

`struct pcpu_chunk *chunk`
:   chunk of interest

`bool full_scan`
:   if we should scan from the beginning

**Description**

Iterates over the metadata blocks to find the largest contig area.
A full scan can be avoided on the allocation path as this is triggered
if we broke the contig_hint. In doing so, the scan_hint will be before
the contig_hint or after if the scan_hint == contig_hint. This cannot
be prevented on freeing as we want to find the largest area possibly
spanning blocks.

void pcpu_block_refresh_hint(struct pcpu_chunk \*chunk, int index)

**Parameters**

`struct pcpu_chunk *chunk`
:   chunk of interest

`int index`
:   index of the metadata block

**Description**

Scans over the block beginning at first_free and updates the block
metadata accordingly.

void pcpu_block_update_hint_alloc(struct pcpu_chunk \*chunk, int bit_off, int bits)
:   update hint on allocation path

**Parameters**

`struct pcpu_chunk *chunk`
:   chunk of interest

`int bit_off`
:   chunk offset

`int bits`
:   size of request

**Description**

Updates metadata for the allocation path. The metadata only has to be
refreshed by a full scan iff the chunk's contig hint is broken. Block level
scans are required if the block's contig hint is broken.

void pcpu_block_update_hint_free(struct pcpu_chunk \*chunk, int bit_off, int bits)
:   updates the block hints on the free path

**Parameters**

`struct pcpu_chunk *chunk`
:   chunk of interest

`int bit_off`
:   chunk offset

`int bits`
:   size of request

**Description**

Updates metadata for the allocation path. This avoids a blind block
refresh by making use of the block contig hints. If this fails, it scans
forward and backward to determine the extent of the free area. This is
capped at the boundary of blocks.

A chunk update is triggered if a page becomes free, a block becomes free,
or the free spans across blocks. This tradeoff is to minimize iterating
over the block metadata to update chunk_md->contig_hint.
chunk_md->contig_hint may be off by up to a page, but it will never be more
than the available space. If the contig hint is contained in one block, it
will be accurate.

bool pcpu_is_populated(struct pcpu_chunk \*chunk, int bit_off, int bits, int \*next_off)
:   determines if the region is populated

**Parameters**

`struct pcpu_chunk *chunk`
:   chunk of interest

`int bit_off`
:   chunk offset

`int bits`
:   size of area

`int *next_off`
:   return value for the next offset to start searching

**Description**

For atomic allocations, check if the backing pages are populated.

**Return**

Bool if the backing pages are populated.
next_index is to skip over unpopulated blocks in pcpu_find_block_fit.

int pcpu_find_block_fit(struct pcpu_chunk \*chunk, int alloc_bits, size_t align, bool pop_only)
:   finds the block index to start searching

**Parameters**

`struct pcpu_chunk *chunk`
:   chunk of interest

`int alloc_bits`
:   size of request in allocation units

`size_t align`
:   alignment of area (max PAGE_SIZE bytes)

`bool pop_only`
:   use populated regions only

**Description**

Given a chunk and an allocation spec, find the offset to begin searching
for a free region. This iterates over the bitmap metadata blocks to
find an offset that will be guaranteed to fit the requirements. It is
not quite first fit as if the allocation does not fit in the contig hint
of a block or chunk, it is skipped. This errs on the side of caution
to prevent excess iteration. Poor alignment can cause the allocator to
skip over blocks and chunks that have valid free areas.

**Return**

The offset in the bitmap to begin searching.
-1 if no offset is found.

int pcpu_alloc_area(struct pcpu_chunk \*chunk, int alloc_bits, size_t align, int start)
:   allocates an area from a pcpu_chunk

**Parameters**

`struct pcpu_chunk *chunk`
:   chunk of interest

`int alloc_bits`
:   size of request in allocation units

`size_t align`
:   alignment of area (max PAGE_SIZE)

`int start`
:   bit_off to start searching

**Description**

This function takes in a **start** offset to begin searching to fit an
allocation of **alloc_bits** with alignment **align**. It needs to scan
the allocation map because if it fits within the block's contig hint,
**start** will be block->first_free. This is an attempt to fill the
allocation prior to breaking the contig hint. The allocation and
boundary maps are updated accordingly if it confirms a valid
free area.

**Return**

Allocated addr offset in **chunk** on success.
-1 if no matching area is found.

int pcpu_free_area(struct pcpu_chunk \*chunk, int off)
:   frees the corresponding offset

**Parameters**

`struct pcpu_chunk *chunk`
:   chunk of interest

`int off`
:   addr offset into chunk

**Description**

This function determines the size of an allocation to free using
the boundary bitmap and clears the allocation map.

**Return**

Number of freed bytes.

struct pcpu_chunk \*pcpu_alloc_first_chunk(unsigned long tmp_addr, int map_size)
:   creates chunks that serve the first chunk

**Parameters**

`unsigned long tmp_addr`
:   the start of the region served

`int map_size`
:   size of the region served

**Description**

This is responsible for creating the chunks that serve the first chunk. The
base_addr is page aligned down of **tmp_addr** while the region end is page
aligned up. Offsets are kept track of to determine the region served. All
this is done to appease the bitmap allocator in avoiding partial blocks.

**Return**

Chunk serving the region at **tmp_addr** of **map_size**.

void pcpu_chunk_populated(struct pcpu_chunk \*chunk, int page_start, int page_end)
:   post-population bookkeeping

**Parameters**

`struct pcpu_chunk *chunk`
:   pcpu_chunk which got populated

`int page_start`
:   the start page

`int page_end`
:   the end page

**Description**

Pages in [**page_start**,\*\*page_end\*\*) have been populated to **chunk**. Update
the bookkeeping information accordingly. Must be called after each
successful population.

void pcpu_chunk_depopulated(struct pcpu_chunk \*chunk, int page_start, int page_end)
:   post-depopulation bookkeeping

**Parameters**

`struct pcpu_chunk *chunk`
:   pcpu_chunk which got depopulated

`int page_start`
:   the start page

`int page_end`
:   the end page

**Description**

Pages in [**page_start**,\*\*page_end\*\*) have been depopulated from **chunk**.
Update the bookkeeping information accordingly. Must be called after
each successful depopulation.

struct pcpu_chunk \*pcpu_chunk_addr_search(void \*addr)
:   determine chunk containing specified address

**Parameters**

`void *addr`
:   address for which the chunk needs to be determined.

**Description**

This is an internal function that handles all but static allocations.
Static percpu address values should never be passed into the allocator.

**Return**

The address of the found chunk.

void __percpu \*pcpu_alloc(size_t size, size_t align, bool reserved, gfp_t gfp)
:   the percpu allocator

**Parameters**

`size_t size`
:   size of area to allocate in bytes

`size_t align`
:   alignment of area (max PAGE_SIZE)

`bool reserved`
:   allocate from the reserved chunk if available

`gfp_t gfp`
:   allocation flags

**Description**

Allocate percpu area of **size** bytes aligned at **align**. If **gfp** doesn't
contain `GFP_KERNEL`, the allocation is atomic. If **gfp** has __GFP_NOWARN
then no warning will be triggered on invalid or failed allocation
requests.

**Return**

Percpu pointer to the allocated area on success, NULL on failure.

void __percpu \*__alloc_percpu_gfp(size_t size, size_t align, gfp_t gfp)
:   allocate dynamic percpu area

**Parameters**

`size_t size`
:   size of area to allocate in bytes

`size_t align`
:   alignment of area (max PAGE_SIZE)

`gfp_t gfp`
:   allocation flags

**Description**

Allocate zero-filled percpu area of **size** bytes aligned at **align**. If
**gfp** doesn't contain `GFP_KERNEL`, the allocation doesn't block and can
be called from any context but is a lot more likely to fail. If **gfp**
has __GFP_NOWARN then no warning will be triggered on invalid or failed
allocation requests.

**Return**

Percpu pointer to the allocated area on success, NULL on failure.

void __percpu \*__alloc_percpu(size_t size, size_t align)
:   allocate dynamic percpu area

**Parameters**

`size_t size`
:   size of area to allocate in bytes

`size_t align`
:   alignment of area (max PAGE_SIZE)

**Description**

Equivalent to __alloc_percpu_gfp(size, align, `GFP_KERNEL`).

void __percpu \*__alloc_reserved_percpu(size_t size, size_t align)
:   allocate reserved percpu area

**Parameters**

`size_t size`
:   size of area to allocate in bytes

`size_t align`
:   alignment of area (max PAGE_SIZE)

**Description**

Allocate zero-filled percpu area of **size** bytes aligned at **align**
from reserved percpu area if arch has set it up; otherwise,
allocation is served from the same dynamic area. Might sleep.
Might trigger writeouts.

**Context**

Does GFP_KERNEL allocation.

**Return**

Percpu pointer to the allocated area on success, NULL on failure.

void pcpu_balance_free(bool empty_only)
:   manage the amount of free chunks

**Parameters**

`bool empty_only`
:   free chunks only if there are no populated pages

**Description**

If empty_only is `false`, reclaim all fully free chunks regardless of the
number of populated pages. Otherwise, only reclaim chunks that have no
populated pages.

**Context**

pcpu_lock (can be dropped temporarily)

void pcpu_balance_populated(void)
:   manage the amount of populated pages

**Parameters**

`void`
:   no arguments

**Description**

Maintain a certain amount of populated pages to satisfy atomic allocations.
It is possible that this is called when physical memory is scarce causing
OOM killer to be triggered. We should avoid doing so until an actual
allocation causes the failure as it is possible that requests can be
serviced from already backed regions.

**Context**

pcpu_lock (can be dropped temporarily)

void pcpu_reclaim_populated(void)
:   scan over to_depopulate chunks and free empty pages

**Parameters**

`void`
:   no arguments

**Description**

Scan over chunks in the depopulate list and try to release unused populated
pages back to the system. Depopulated chunks are sidelined to prevent
repopulating these pages unless required. Fully free chunks are reintegrated
and freed accordingly (1 is kept around). If we drop below the empty
populated pages threshold, reintegrate the chunk if it has empty free pages.
Each chunk is scanned in the reverse order to keep populated pages close to
the beginning of the chunk.

**Context**

pcpu_lock (can be dropped temporarily)

void pcpu_balance_workfn(struct work_struct \*work)
:   manage the amount of free chunks and populated pages

**Parameters**

`struct work_struct *work`
:   unused

**Description**

For each chunk type, manage the number of fully free chunks and the number of
populated pages. An important thing to consider is when pages are freed and
how they contribute to the global counts.

size_t pcpu_alloc_size(void __percpu \*ptr)
:   the size of the dynamic percpu area

**Parameters**

`void __percpu *ptr`
:   pointer to the dynamic percpu area

**Description**

Returns the size of the **ptr** allocation. This is undefined for statically
defined percpu variables as there is no corresponding chunk->bound_map.

**Return**

The size of the dynamic percpu area.

**Context**

Can be called from atomic context.

void free_percpu(void __percpu \*ptr)
:   free percpu area

**Parameters**

`void __percpu *ptr`
:   pointer to area to free

**Description**

Free percpu area **ptr**.

**Context**

Can be called from atomic context.

bool is_kernel_percpu_address(unsigned long addr)
:   test whether address is from static percpu area

**Parameters**

`unsigned long addr`
:   address to test

**Description**

Test whether **addr** belongs to in-kernel static percpu area. Module
static percpu areas are not considered. For those, use
is_module_percpu_address().

**Return**

`true` if **addr** is from in-kernel static percpu area, `false` otherwise.

phys_addr_t per_cpu_ptr_to_phys(void \*addr)
:   convert translated percpu address to physical address

**Parameters**

`void *addr`
:   the address to be converted to physical address

**Description**

Given **addr** which is dereferenceable address obtained via one of
percpu access macros, this function translates it into its physical
address. The caller is responsible for ensuring **addr** stays valid
until this function finishes.

percpu allocator has special setup for the first chunk, which currently
supports either embedding in linear address space or vmalloc mapping,
and, from the second one, the backing allocator (currently either vm or
km) provides translation.

The addr can be translated simply without checking if it falls into the
first chunk. But the current code reflects better how percpu allocator
actually works, and the verification can discover both bugs in percpu
allocator itself and [`per_cpu_ptr_to_phys()`](mm-api.md#c.per_cpu_ptr_to_phys "per_cpu_ptr_to_phys") callers. So we keep current
code.

**Return**

The physical address for **addr**.

struct pcpu_alloc_info \*pcpu_alloc_alloc_info(int nr_groups, int nr_units)
:   allocate percpu allocation info

**Parameters**

`int nr_groups`
:   the number of groups

`int nr_units`
:   the number of units

**Description**

Allocate ai which is large enough for **nr_groups** groups containing
**nr_units** units. The returned ai's groups[0].cpu_map points to the
cpu_map array which is long enough for **nr_units** and filled with
NR_CPUS. It's the caller's responsibility to initialize cpu_map
pointer of other groups.

**Return**

Pointer to the allocated pcpu_alloc_info on success, NULL on
failure.

void pcpu_free_alloc_info(struct pcpu_alloc_info \*ai)
:   free percpu allocation info

**Parameters**

`struct pcpu_alloc_info *ai`
:   pcpu_alloc_info to free

**Description**

Free **ai** which was allocated by [`pcpu_alloc_alloc_info()`](mm-api.md#c.pcpu_alloc_alloc_info "pcpu_alloc_alloc_info").

void pcpu_dump_alloc_info(const char \*lvl, const struct pcpu_alloc_info \*ai)
:   print out information about pcpu_alloc_info

**Parameters**

`const char *lvl`
:   loglevel

`const struct pcpu_alloc_info *ai`
:   allocation info to dump

**Description**

Print out information about **ai** using loglevel **lvl**.

void pcpu_setup_first_chunk(const struct pcpu_alloc_info \*ai, void \*base_addr)
:   initialize the first percpu chunk

**Parameters**

`const struct pcpu_alloc_info *ai`
:   pcpu_alloc_info describing how to percpu area is shaped

`void *base_addr`
:   mapped address

**Description**

Initialize the first percpu chunk which contains the kernel static
percpu area. This function is to be called from arch percpu area
setup path.

**ai** contains all information necessary to initialize the first
chunk and prime the dynamic percpu allocator.

**ai->static_size** is the size of static percpu area.

**ai->reserved_size**, if non-zero, specifies the amount of bytes to
reserve after the static area in the first chunk. This reserves
the first chunk such that it's available only through reserved
percpu allocation. This is primarily used to serve module percpu
static areas on architectures where the addressing model has
limited offset range for symbol relocations to guarantee module
percpu symbols fall inside the relocatable range.

**ai->dyn_size** determines the number of bytes available for dynamic
allocation in the first chunk. The area between **ai->static_size** +
**ai->reserved_size** + **ai->dyn_size** and **ai->unit_size** is unused.

**ai->unit_size** specifies unit size and must be aligned to PAGE_SIZE
and equal to or larger than **ai->static_size** + **ai->reserved_size** +
**ai->dyn_size**.

**ai->atom_size** is the allocation atom size and used as alignment
for vm areas.

**ai->alloc_size** is the allocation size and always multiple of
**ai->atom_size**. This is larger than **ai->atom_size** if
**ai->unit_size** is larger than **ai->atom_size**.

**ai->nr_groups** and **ai->groups** describe virtual memory layout of
percpu areas. Units which should be colocated are put into the
same group. Dynamic VM areas will be allocated according to these
groupings. If **ai->nr_groups** is zero, a single group containing
all units is assumed.

The caller should have mapped the first chunk at **base_addr** and
copied static data to each unit.

The first chunk will always contain a static and a dynamic region.
However, the static region is not managed by any chunk. If the first
chunk also contains a reserved region, it is served by two chunks -
one for the reserved region and one for the dynamic region. They
share the same vm, but use offset regions in the area allocation map.
The chunk serving the dynamic region is circulated in the chunk slots
and available for dynamic allocation like any other chunk.

struct pcpu_alloc_info \*pcpu_build_alloc_info(size_t reserved_size, size_t dyn_size, size_t atom_size, pcpu_fc_cpu_distance_fn_t cpu_distance_fn)
:   build alloc_info considering distances between CPUs

**Parameters**

`size_t reserved_size`
:   the size of reserved percpu area in bytes

`size_t dyn_size`
:   minimum free size for dynamic allocation in bytes

`size_t atom_size`
:   allocation atom size

`pcpu_fc_cpu_distance_fn_t cpu_distance_fn`
:   callback to determine distance between cpus, optional

**Description**

This function determines grouping of units, their mappings to cpus
and other parameters considering needed percpu size, allocation
atom size and distances between CPUs.

Groups are always multiples of atom size and CPUs which are of
LOCAL_DISTANCE both ways are grouped together and share space for
units in the same group. The returned configuration is guaranteed
to have CPUs on different nodes on different groups and >=75% usage
of allocated virtual address space.

**Return**

On success, pointer to the new allocation_info is returned. On
failure, ERR_PTR value is returned.

int pcpu_embed_first_chunk(size_t reserved_size, size_t dyn_size, size_t atom_size, pcpu_fc_cpu_distance_fn_t cpu_distance_fn, pcpu_fc_cpu_to_node_fn_t cpu_to_nd_fn)
:   embed the first percpu chunk into bootmem

**Parameters**

`size_t reserved_size`
:   the size of reserved percpu area in bytes

`size_t dyn_size`
:   minimum free size for dynamic allocation in bytes

`size_t atom_size`
:   allocation atom size

`pcpu_fc_cpu_distance_fn_t cpu_distance_fn`
:   callback to determine distance between cpus, optional

`pcpu_fc_cpu_to_node_fn_t cpu_to_nd_fn`
:   callback to convert cpu to it's node, optional

**Description**

This is a helper to ease setting up embedded first percpu chunk and
can be called where [`pcpu_setup_first_chunk()`](mm-api.md#c.pcpu_setup_first_chunk "pcpu_setup_first_chunk") is expected.

If this function is used to setup the first chunk, it is allocated
by calling pcpu_fc_alloc and used as-is without being mapped into
vmalloc area. Allocations are always whole multiples of **atom_size**
aligned to **atom_size**.

This enables the first chunk to piggy back on the linear physical
mapping which often uses larger page size. Please note that this
can result in very sparse cpu->unit mapping on NUMA machines thus
requiring large vmalloc address space. Don't use this allocator if
vmalloc space is not orders of magnitude larger than distances
between node memory addresses (ie. 32bit NUMA machines).

**dyn_size** specifies the minimum dynamic area size.

If the needed size is smaller than the minimum or specified unit
size, the leftover is returned using pcpu_fc_free.

**Return**

0 on success, -errno on failure.

int pcpu_page_first_chunk(size_t reserved_size, pcpu_fc_cpu_to_node_fn_t cpu_to_nd_fn)
:   map the first chunk using PAGE_SIZE pages

**Parameters**

`size_t reserved_size`
:   the size of reserved percpu area in bytes

`pcpu_fc_cpu_to_node_fn_t cpu_to_nd_fn`
:   callback to convert cpu to it's node, optional

**Description**

This is a helper to ease setting up page-remapped first percpu
chunk and can be called where [`pcpu_setup_first_chunk()`](mm-api.md#c.pcpu_setup_first_chunk "pcpu_setup_first_chunk") is expected.

This is the basic allocator. Static percpu area is allocated
page-by-page into vmalloc area.

**Return**

0 on success, -errno on failure.

long copy_from_user_nofault(void \*dst, const void __user \*src, size_t size)
:   safely attempt to read from a user-space location

**Parameters**

`void *dst`
:   pointer to the buffer that shall take the data

`const void __user *src`
:   address to read from. This must be a user address.

`size_t size`
:   size of the data chunk

**Description**

Safely read from user address **src** to the buffer at **dst**. If a kernel fault
happens, handle that and return -EFAULT.

long copy_to_user_nofault(void __user \*dst, const void \*src, size_t size)
:   safely attempt to write to a user-space location

**Parameters**

`void __user *dst`
:   address to write to

`const void *src`
:   pointer to the data that shall be written

`size_t size`
:   size of the data chunk

**Description**

Safely write to address **dst** from the buffer at **src**. If a kernel fault
happens, handle that and return -EFAULT.

long strncpy_from_user_nofault(char \*dst, const void __user \*unsafe_addr, long count)
:   - Copy a NUL terminated string from unsafe user address.

**Parameters**

`char *dst`
:   Destination address, in kernel space. This buffer must be at
    least **count** bytes long.

`const void __user *unsafe_addr`
:   Unsafe user address.

`long count`
:   Maximum number of bytes to copy, including the trailing NUL.

**Description**

Copies a NUL-terminated string from unsafe user address to kernel buffer.

On success, returns the length of the string INCLUDING the trailing NUL.

If access fails, returns -EFAULT (some data may have been copied
and the trailing NUL added).

If **count** is smaller than the length of the string, copies **count**-1 bytes,
sets the last byte of **dst** buffer to NUL and returns **count**.

long strnlen_user_nofault(const void __user \*unsafe_addr, long count)
:   - Get the size of a user string INCLUDING final NUL.

**Parameters**

`const void __user *unsafe_addr`
:   The string to measure.

`long count`
:   Maximum count (including NUL)

**Description**

Get the size of a NUL-terminated string in user space without pagefault.

Returns the size of the string INCLUDING the terminating NUL.

If the string is too long, returns a number larger than **count**. User
has to check the return value against "> count".
On exception (or invalid count), returns 0.

Unlike strnlen_user, this can be used from IRQ handler etc. because
it disables pagefaults.

bool writeback_throttling_sane(struct scan_control \*sc)
:   is the usual dirty throttling mechanism available?

**Parameters**

`struct scan_control *sc`
:   scan_control in question

**Description**

The normal page dirty throttling mechanism in balance_dirty_pages() is
completely broken with the legacy memcg and direct stalling in
shrink_folio_list() is used for throttling instead, which lacks all the
niceties such as fairness, adaptive pausing, bandwidth proportional
allocation and configurability.

This function tests whether the vmscan currently in progress can assume
that the normal dirty throttling mechanism is operational.

unsigned long lruvec_lru_size(struct [lruvec](mm-api.md#c.lruvec_lru_size "lruvec") \*lruvec, enum lru_list lru, int zone_idx)
:   Returns the number of pages on the given LRU list.

**Parameters**

`struct lruvec *lruvec`
:   lru vector

`enum lru_list lru`
:   lru to use

`int zone_idx`
:   zones to consider (use MAX_NR_ZONES - 1 for the whole LRU list)

long remove_mapping(struct [address_space](../filesystems/api-summary.md#c.address_space "address_space") \*mapping, struct [folio](mm-api.md#c.remove_mapping "folio") \*folio)
:   Attempt to remove a folio from its mapping.

**Parameters**

`struct address_space *mapping`
:   The address space.

`struct folio *folio`
:   The folio to remove.

**Description**

If the folio is dirty, under writeback or if someone else has a ref
on it, removal will fail.

**Return**

The number of pages removed from the mapping. 0 if the folio
could not be removed.

**Context**

The caller should have a single refcount on the folio and
hold its lock.

void folio_putback_lru(struct [folio](mm-api.md#c.folio_putback_lru "folio") \*folio)
:   Put previously isolated folio onto appropriate LRU list.

**Parameters**

`struct folio *folio`
:   Folio to be returned to an LRU list.

**Description**

Add previously isolated **folio** to appropriate LRU list.
The folio may still be unevictable for other reasons.

**Context**

lru_lock must not be held, interrupts must be enabled.

bool folio_isolate_lru(struct [folio](mm-api.md#c.folio_isolate_lru "folio") \*folio)
:   Try to isolate a folio from its LRU list.

**Parameters**

`struct folio *folio`
:   Folio to isolate from its LRU list.

**Description**

Isolate a **folio** from an LRU list and adjust the vmstat statistic
corresponding to whatever LRU list the folio was on.

The folio will have its LRU flag cleared. If it was found on the
active list, it will have the Active flag set. If it was found on the
unevictable list, it will have the Unevictable flag set. These flags
may need to be cleared by the caller before letting the page go.

1. Must be called with an elevated refcount on the folio. This is a
   fundamental difference from isolate_lru_folios() (which is called
   without a stable reference).
2. The lru_lock must not be held.
3. Interrupts must be enabled.

**Context**

**Return**

true if the folio was removed from an LRU list.
false if the folio was not on an LRU list.

void check_move_unevictable_folios(struct folio_batch \*fbatch)
:   Move evictable folios to appropriate zone lru list

**Parameters**

`struct folio_batch *fbatch`
:   Batch of lru folios to check.

**Description**

Checks folios for evictability, if an evictable folio is in the unevictable
lru list, moves it to the appropriate evictable lru list. This function
should be only used for lru folios.

void __remove_pages(unsigned long pfn, unsigned long nr_pages, struct vmem_altmap \*altmap)
:   remove sections of pages

**Parameters**

`unsigned long pfn`
:   starting pageframe (must be aligned to start of a section)

`unsigned long nr_pages`
:   number of pages to remove (must be multiple of section size)

`struct vmem_altmap *altmap`
:   alternative device page map or `NULL` if default memmap is used

**Description**

Generic helper function to remove section mappings and sysfs entries
for the section of the memory we are removing. Caller needs to make
sure that pages are marked reserved and zones are adjust properly by
calling offline_pages().

void try_offline_node(int nid)

**Parameters**

`int nid`
:   the node ID

**Description**

Offline a node if all memory sections and cpus of the node are removed.

**NOTE**

The caller must call lock_device_hotplug() to serialize hotplug
and online/offline operations before this call.

void __remove_memory(u64 start, u64 size)
:   Remove memory if every memory block is offline

**Parameters**

`u64 start`
:   physical address of the region to remove

`u64 size`
:   size of the region to remove

**NOTE**

The caller must call lock_device_hotplug() to serialize hotplug
and online/offline operations before this call, as required by
[`try_offline_node()`](mm-api.md#c.try_offline_node "try_offline_node").

unsigned long mmu_interval_read_begin(struct mmu_interval_notifier \*interval_sub)
:   Begin a read side critical section against a VA range

**Parameters**

`struct mmu_interval_notifier *interval_sub`
:   The interval subscription

**Description**

mmu_iterval_read_begin()/mmu_iterval_read_retry() implement a
collision-retry scheme similar to seqcount for the VA range under
subscription. If the mm invokes invalidation during the critical section
then mmu_interval_read_retry() will return true.

This is useful to obtain shadow PTEs where teardown or setup of the SPTEs
require a blocking context. The critical region formed by this can sleep,
and the required 'user_lock' can also be a sleeping lock.

The caller is required to provide a 'user_lock' to serialize both teardown
and setup.

The return value should be passed to mmu_interval_read_retry().

int mmu_notifier_register(struct mmu_notifier \*subscription, struct mm_struct \*mm)
:   Register a notifier on a mm

**Parameters**

`struct mmu_notifier *subscription`
:   The notifier to attach

`struct mm_struct *mm`
:   The mm to attach the notifier to

**Description**

Must not hold mmap_lock nor any other VM related lock when calling
this registration function. Must also ensure mm_users can't go down
to zero while this runs to avoid races with mmu_notifier_release,
so mm has to be current->mm or the mm should be pinned safely such
as with get_task_mm(). If the mm is not current->mm, the mm_users
pin should be released by calling mmput after mmu_notifier_register
returns.

mmu_notifier_unregister() or [`mmu_notifier_put()`](mm-api.md#c.mmu_notifier_put "mmu_notifier_put") must be always called to
unregister the notifier.

While the caller has a mmu_notifier get the subscription->mm pointer will remain
valid, and can be converted to an active mm pointer via mmget_not_zero().

struct mmu_notifier \*mmu_notifier_get_locked(const struct mmu_notifier_ops \*ops, struct mm_struct \*mm)
:   Return the single struct mmu_notifier for the mm & ops

**Parameters**

`const struct mmu_notifier_ops *ops`
:   The operations struct being subscribe with

`struct mm_struct *mm`
:   The mm to attach notifiers too

**Description**

This function either allocates a new mmu_notifier via
ops->alloc_notifier(), or returns an already existing notifier on the
list. The value of the ops pointer is used to determine when two notifiers
are the same.

Each call to mmu_notifier_get() must be paired with a call to
[`mmu_notifier_put()`](mm-api.md#c.mmu_notifier_put "mmu_notifier_put"). The caller must hold the write side of mm->mmap_lock.

While the caller has a mmu_notifier get the mm pointer will remain valid,
and can be converted to an active mm pointer via mmget_not_zero().

void mmu_notifier_put(struct mmu_notifier \*subscription)
:   Release the reference on the notifier

**Parameters**

`struct mmu_notifier *subscription`
:   The notifier to act on

**Description**

This function must be paired with each mmu_notifier_get(), it releases the
reference obtained by the get. If this is the last reference then process
to free the notifier will be run asynchronously.

Unlike mmu_notifier_unregister() the get/put flow only calls ops->release
when the mm_struct is destroyed. Instead free_notifier is always called to
release any resources held by the user.

As ops->release is not guaranteed to be called, the user must ensure that
all sptes are dropped, and no new sptes can be established before
[`mmu_notifier_put()`](mm-api.md#c.mmu_notifier_put "mmu_notifier_put") is called.

This function can be called from the ops->release callback, however the
caller must still ensure it is called pairwise with mmu_notifier_get().

Modules calling this function must call [`mmu_notifier_synchronize()`](mm-api.md#c.mmu_notifier_synchronize "mmu_notifier_synchronize") in
their __exit functions to ensure the async work is completed.

int mmu_interval_notifier_insert(struct mmu_interval_notifier \*interval_sub, struct mm_struct \*mm, unsigned long start, unsigned long length, const struct mmu_interval_notifier_ops \*ops)
:   Insert an interval notifier

**Parameters**

`struct mmu_interval_notifier *interval_sub`
:   Interval subscription to register

`struct mm_struct *mm`
:   mm_struct to attach to

`unsigned long start`
:   Starting virtual address to monitor

`unsigned long length`
:   Length of the range to monitor

`const struct mmu_interval_notifier_ops *ops`
:   Interval notifier operations to be called on matching events

**Description**

This function subscribes the interval notifier for notifications from the
mm. Upon return the ops related to mmu_interval_notifier will be called
whenever an event that intersects with the given range occurs.

Upon return the range_notifier may not be present in the interval tree yet.
The caller must use the normal interval notifier read flow via
[`mmu_interval_read_begin()`](mm-api.md#c.mmu_interval_read_begin "mmu_interval_read_begin") to establish SPTEs for this range.

void mmu_interval_notifier_remove(struct mmu_interval_notifier \*interval_sub)
:   Remove a interval notifier

**Parameters**

`struct mmu_interval_notifier *interval_sub`
:   Interval subscription to unregister

**Description**

This function must be paired with [`mmu_interval_notifier_insert()`](mm-api.md#c.mmu_interval_notifier_insert "mmu_interval_notifier_insert"). It cannot
be called from any ops callback.

Once this returns ops callbacks are no longer running on other CPUs and
will not be called in future.

void mmu_notifier_synchronize(void)
:   Ensure all mmu_notifiers are freed

**Parameters**

`void`
:   no arguments

**Description**

This function ensures that all outstanding async SRU work from
[`mmu_notifier_put()`](mm-api.md#c.mmu_notifier_put "mmu_notifier_put") is completed. After it returns any mmu_notifier_ops
associated with an unused mmu_notifier will no longer be called.

Before using the caller must ensure that all of its mmu_notifiers have been
fully released via [`mmu_notifier_put()`](mm-api.md#c.mmu_notifier_put "mmu_notifier_put").

Modules using the [`mmu_notifier_put()`](mm-api.md#c.mmu_notifier_put "mmu_notifier_put") API should call this in their __exit
function to avoid module unloading races.

size_t balloon_page_list_enqueue(struct balloon_dev_info \*b_dev_info, struct list_head \*pages)
:   inserts a list of pages into the balloon page list.

**Parameters**

`struct balloon_dev_info *b_dev_info`
:   balloon device descriptor where we will insert a new page to

`struct list_head *pages`
:   pages to enqueue - allocated using balloon_page_alloc.

**Description**

Driver must call this function to properly enqueue balloon pages before
definitively removing them from the guest system.

**Return**

number of pages that were enqueued.

size_t balloon_page_list_dequeue(struct balloon_dev_info \*b_dev_info, struct list_head \*pages, size_t n_req_pages)
:   removes pages from balloon's page list and returns a list of the pages.

**Parameters**

`struct balloon_dev_info *b_dev_info`
:   balloon device descriptor where we will grab a page from.

`struct list_head *pages`
:   pointer to the list of pages that would be returned to the caller.

`size_t n_req_pages`
:   number of requested pages.

**Description**

Driver must call this function to properly de-allocate a previous enlisted
balloon pages before definitively releasing it back to the guest system.
This function tries to remove **n_req_pages** from the ballooned pages and
return them to the caller in the **pages** list.

Note that this function may fail to dequeue some pages even if the balloon
isn't empty - since the page list can be temporarily empty due to compaction
of isolated pages.

**Return**

number of pages that were added to the **pages** list.

[vm_fault_t](mm-api.md#c.vm_fault_t "vm_fault_t") vmf_insert_pfn_pmd(struct vm_fault \*vmf, pfn_t pfn, bool write)
:   insert a pmd size pfn

**Parameters**

`struct vm_fault *vmf`
:   Structure describing the fault

`pfn_t pfn`
:   pfn to insert

`bool write`
:   whether it's a write fault

**Description**

Insert a pmd size pfn. See [`vmf_insert_pfn()`](mm-api.md#c.vmf_insert_pfn "vmf_insert_pfn") for additional info.

**Return**

vm_fault_t value.

[vm_fault_t](mm-api.md#c.vm_fault_t "vm_fault_t") vmf_insert_pfn_pud(struct vm_fault \*vmf, pfn_t pfn, bool write)
:   insert a pud size pfn

**Parameters**

`struct vm_fault *vmf`
:   Structure describing the fault

`pfn_t pfn`
:   pfn to insert

`bool write`
:   whether it's a write fault

**Description**

Insert a pud size pfn. See [`vmf_insert_pfn()`](mm-api.md#c.vmf_insert_pfn "vmf_insert_pfn") for additional info.

**Return**

vm_fault_t value.

int io_mapping_map_user(struct io_mapping \*iomap, struct vm_area_struct \*vma, unsigned long addr, unsigned long pfn, unsigned long size)
:   remap an I/O mapping to userspace

**Parameters**

`struct io_mapping *iomap`
:   the source io_mapping

`struct vm_area_struct *vma`
:   user vma to map to

`unsigned long addr`
:   target user address to start at

`unsigned long pfn`
:   physical address of kernel memory

`unsigned long size`
:   size of map area

**Note**

this is only safe if the mm semaphore is held when called.
