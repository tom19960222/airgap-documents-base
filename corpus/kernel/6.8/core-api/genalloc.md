---
collection: kernel
version: "6.8"
title: "The genalloc/genpool subsystem"
source_url: https://www.kernel.org/doc/html/v6.8/core-api/genalloc.html
fetched_at: 2026-08-21T03:30:18+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/core-api/genalloc.md)

# The genalloc/genpool subsystem

There are a number of memory-allocation subsystems in the kernel, each
aimed at a specific need. Sometimes, however, a kernel developer needs to
implement a new allocator for a specific range of special-purpose memory;
often that memory is located on a device somewhere. The author of the
driver for that device can certainly write a little allocator to get the
job done, but that is the way to fill the kernel with dozens of poorly
tested allocators. Back in 2005, Jes Sorensen lifted one of those
allocators from the sym53c8xx_2 driver and [posted](https://lwn.net/Articles/125842/) it as a generic module
for the creation of ad hoc memory allocators. This code was merged
for the 2.6.13 release; it has been modified considerably since then.

Code using this allocator should include <linux/genalloc.h>. The action
begins with the creation of a pool using one of:

struct gen_pool \*gen_pool_create(int min_alloc_order, int nid)
:   create a new special memory pool

**Parameters**

`int min_alloc_order`
:   log base 2 of number of bytes each bitmap bit represents

`int nid`
:   node id of the node the pool structure should be allocated on, or -1

**Description**

Create a new special memory pool that can be used to manage special purpose
memory not managed by the regular kmalloc/kfree interface.

struct gen_pool \*devm_gen_pool_create(struct [device](../driver-api/infrastructure.md#c.device "device") \*dev, int min_alloc_order, int nid, const char \*name)
:   managed gen_pool_create

**Parameters**

`struct device *dev`
:   device that provides the gen_pool

`int min_alloc_order`
:   log base 2 of number of bytes each bitmap bit represents

`int nid`
:   node selector for allocated gen_pool, `NUMA_NO_NODE` for all nodes

`const char *name`
:   name of a gen_pool or NULL, identifies a particular gen_pool on device

**Description**

Create a new special memory pool that can be used to manage special purpose
memory not managed by the regular kmalloc/kfree interface. The pool will be
automatically destroyed by the device management code.

A call to [`gen_pool_create()`](genalloc.md#c.gen_pool_create "gen_pool_create") will create a pool. The granularity of
allocations is set with min_alloc_order; it is a log-base-2 number like
those used by the page allocator, but it refers to bytes rather than pages.
So, if min_alloc_order is passed as 3, then all allocations will be a
multiple of eight bytes. Increasing min_alloc_order decreases the memory
required to track the memory in the pool. The nid parameter specifies
which NUMA node should be used for the allocation of the housekeeping
structures; it can be -1 if the caller doesn't care.

The "managed" interface [`devm_gen_pool_create()`](genalloc.md#c.devm_gen_pool_create "devm_gen_pool_create") ties the pool to a
specific device. Among other things, it will automatically clean up the
pool when the given device is destroyed.

A pool is shut down with:

void gen_pool_destroy(struct gen_pool \*pool)
:   destroy a special memory pool

**Parameters**

`struct gen_pool *pool`
:   pool to destroy

**Description**

Destroy the specified special memory pool. Verifies that there are no
outstanding allocations.

It's worth noting that, if there are still allocations outstanding from the
given pool, this function will take the rather extreme step of invoking
BUG(), crashing the entire system. You have been warned.

A freshly created pool has no memory to allocate. It is fairly useless in
that state, so one of the first orders of business is usually to add memory
to the pool. That can be done with one of:

int gen_pool_add(struct gen_pool \*pool, unsigned long addr, size_t size, int nid)
:   add a new chunk of special memory to the pool

**Parameters**

`struct gen_pool *pool`
:   pool to add new memory chunk to

`unsigned long addr`
:   starting address of memory chunk to add to pool

`size_t size`
:   size in bytes of the memory chunk to add to pool

`int nid`
:   node id of the node the chunk structure and bitmap should be
    allocated on, or -1

**Description**

Add a new chunk of special memory to the specified pool.

Returns 0 on success or a -ve errno on failure.

int gen_pool_add_owner(struct gen_pool \*pool, unsigned long virt, phys_addr_t phys, size_t size, int nid, void \*owner)
:   add a new chunk of special memory to the pool

**Parameters**

`struct gen_pool *pool`
:   pool to add new memory chunk to

`unsigned long virt`
:   virtual starting address of memory chunk to add to pool

`phys_addr_t phys`
:   physical starting address of memory chunk to add to pool

`size_t size`
:   size in bytes of the memory chunk to add to pool

`int nid`
:   node id of the node the chunk structure and bitmap should be
    allocated on, or -1

`void *owner`
:   private data the publisher would like to recall at alloc time

**Description**

Add a new chunk of special memory to the specified pool.

Returns 0 on success or a -ve errno on failure.

A call to [`gen_pool_add()`](genalloc.md#c.gen_pool_add "gen_pool_add") will place the size bytes of memory
starting at addr (in the kernel's virtual address space) into the given
pool, once again using nid as the node ID for ancillary memory allocations.
The gen_pool_add_virt() variant associates an explicit physical
address with the memory; this is only necessary if the pool will be used
for DMA allocations.

The functions for allocating memory from the pool (and putting it back)
are:

unsigned long gen_pool_alloc(struct gen_pool \*pool, size_t size)
:   allocate special memory from the pool

**Parameters**

`struct gen_pool *pool`
:   pool to allocate from

`size_t size`
:   number of bytes to allocate from the pool

**Description**

Allocate the requested number of bytes from the specified pool.
Uses the pool allocation function (with first-fit algorithm by default).
Can not be used in NMI handler on architectures without
NMI-safe cmpxchg implementation.

void \*gen_pool_dma_alloc(struct gen_pool \*pool, size_t size, dma_addr_t \*dma)
:   allocate special memory from the pool for DMA usage

**Parameters**

`struct gen_pool *pool`
:   pool to allocate from

`size_t size`
:   number of bytes to allocate from the pool

`dma_addr_t *dma`
:   dma-view physical address return value. Use `NULL` if unneeded.

**Description**

Allocate the requested number of bytes from the specified pool.
Uses the pool allocation function (with first-fit algorithm by default).
Can not be used in NMI handler on architectures without
NMI-safe cmpxchg implementation.

**Return**

virtual address of the allocated memory, or `NULL` on failure

void gen_pool_free_owner(struct gen_pool \*pool, unsigned long addr, size_t size, void \*\*owner)
:   free allocated special memory back to the pool

**Parameters**

`struct gen_pool *pool`
:   pool to free to

`unsigned long addr`
:   starting address of memory to free back to pool

`size_t size`
:   size in bytes of memory to free

`void **owner`
:   private data stashed at [`gen_pool_add()`](genalloc.md#c.gen_pool_add "gen_pool_add") time

**Description**

Free previously allocated special memory back to the specified
pool. Can not be used in NMI handler on architectures without
NMI-safe cmpxchg implementation.

As one would expect, [`gen_pool_alloc()`](genalloc.md#c.gen_pool_alloc "gen_pool_alloc") will allocate size< bytes
from the given pool. The [`gen_pool_dma_alloc()`](genalloc.md#c.gen_pool_dma_alloc "gen_pool_dma_alloc") variant allocates
memory for use with DMA operations, returning the associated physical
address in the space pointed to by dma. This will only work if the memory
was added with gen_pool_add_virt(). Note that this function
departs from the usual genpool pattern of using unsigned long values to
represent kernel addresses; it returns a void \* instead.

That all seems relatively simple; indeed, some developers clearly found it
to be too simple. After all, the interface above provides no control over
how the allocation functions choose which specific piece of memory to
return. If that sort of control is needed, the following functions will be
of interest:

unsigned long gen_pool_alloc_algo_owner(struct gen_pool \*pool, size_t size, genpool_algo_t algo, void \*data, void \*\*owner)
:   allocate special memory from the pool

**Parameters**

`struct gen_pool *pool`
:   pool to allocate from

`size_t size`
:   number of bytes to allocate from the pool

`genpool_algo_t algo`
:   algorithm passed from caller

`void *data`
:   data passed to algorithm

`void **owner`
:   optionally retrieve the chunk owner

**Description**

Allocate the requested number of bytes from the specified pool.
Uses the pool allocation function (with first-fit algorithm by default).
Can not be used in NMI handler on architectures without
NMI-safe cmpxchg implementation.

void gen_pool_set_algo(struct gen_pool \*pool, genpool_algo_t algo, void \*data)
:   set the allocation algorithm

**Parameters**

`struct gen_pool *pool`
:   pool to change allocation algorithm

`genpool_algo_t algo`
:   custom algorithm function

`void *data`
:   additional data used by **algo**

**Description**

Call **algo** for each memory allocation in the pool.
If **algo** is NULL use gen_pool_first_fit as default
memory allocation function.

Allocations with gen_pool_alloc_algo() specify an algorithm to be
used to choose the memory to be allocated; the default algorithm can be set
with [`gen_pool_set_algo()`](genalloc.md#c.gen_pool_set_algo "gen_pool_set_algo"). The data value is passed to the
algorithm; most ignore it, but it is occasionally needed. One can,
naturally, write a special-purpose algorithm, but there is a fair set
already available:

- gen_pool_first_fit is a simple first-fit allocator; this is the default
  algorithm if none other has been specified.
- gen_pool_first_fit_align forces the allocation to have a specific
  alignment (passed via data in a genpool_data_align structure).
- gen_pool_first_fit_order_align aligns the allocation to the order of the
  size. A 60-byte allocation will thus be 64-byte aligned, for example.
- gen_pool_best_fit, as one would expect, is a simple best-fit allocator.
- gen_pool_fixed_alloc allocates at a specific offset (passed in a
  genpool_data_fixed structure via the data parameter) within the pool.
  If the indicated memory is not available the allocation fails.

There is a handful of other functions, mostly for purposes like querying
the space available in the pool or iterating through chunks of memory.
Most users, however, should not need much beyond what has been described
above. With luck, wider awareness of this module will help to prevent the
writing of special-purpose memory allocators in the future.

phys_addr_t gen_pool_virt_to_phys(struct gen_pool \*pool, unsigned long addr)
:   return the physical address of memory

**Parameters**

`struct gen_pool *pool`
:   pool to allocate from

`unsigned long addr`
:   starting address of memory

**Description**

Returns the physical address on success, or -1 on error.

void gen_pool_for_each_chunk(struct gen_pool \*pool, void (\*func)(struct gen_pool \*pool, struct gen_pool_chunk \*chunk, void \*data), void \*data)
:   call func for every chunk of generic memory pool

**Parameters**

`struct gen_pool *pool`
:   the generic memory pool

`void (*func)(struct gen_pool *pool, struct gen_pool_chunk *chunk, void *data)`
:   func to call

`void *data`
:   additional data used by **func**

**Description**

Call **func** for every chunk of generic memory pool. The **func** is
called with rcu_read_lock held.

bool gen_pool_has_addr(struct gen_pool \*pool, unsigned long start, size_t size)
:   checks if an address falls within the range of a pool

**Parameters**

`struct gen_pool *pool`
:   the generic memory pool

`unsigned long start`
:   start address

`size_t size`
:   size of the region

**Description**

Check if the range of addresses falls within the specified pool. Returns
true if the entire range is contained in the pool and false otherwise.

size_t gen_pool_avail(struct gen_pool \*pool)
:   get available free space of the pool

**Parameters**

`struct gen_pool *pool`
:   pool to get available free space

**Description**

Return available free space of the specified pool.

size_t gen_pool_size(struct gen_pool \*pool)
:   get size in bytes of memory managed by the pool

**Parameters**

`struct gen_pool *pool`
:   pool to get size

**Description**

Return size in bytes of memory managed by the pool.

struct gen_pool \*gen_pool_get(struct [device](../driver-api/infrastructure.md#c.device "device") \*dev, const char \*name)
:   Obtain the gen_pool (if any) for a device

**Parameters**

`struct device *dev`
:   device to retrieve the gen_pool from

`const char *name`
:   name of a gen_pool or NULL, identifies a particular gen_pool on device

**Description**

Returns the gen_pool for the device if one is present, or NULL.

struct gen_pool \*of_gen_pool_get(struct device_node \*np, const char \*propname, int index)
:   find a pool by phandle property

**Parameters**

`struct device_node *np`
:   device node

`const char *propname`
:   property name containing phandle(s)

`int index`
:   index into the phandle array

**Description**

Returns the pool that contains the chunk starting at the physical
address of the device tree node pointed at by the phandle property,
or NULL if not found.
