---
collection: kernel
version: "6.8"
title: "High Memory Handling"
source_url: https://www.kernel.org/doc/html/v6.8/mm/highmem.html
fetched_at: 2026-08-21T03:39:44+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/mm/highmem.md)

# High Memory Handling

By: Peter Zijlstra <[a.p.zijlstra@chello.nl](mailto:a.p.zijlstra%40chello.nl)>

- [What Is High Memory?](highmem.md#what-is-high-memory)
- [Temporary Virtual Mappings](highmem.md#temporary-virtual-mappings)
- [Cost of Temporary Mappings](highmem.md#cost-of-temporary-mappings)
- [i386 PAE](highmem.md#i386-pae)
- [Functions](highmem.md#functions)

## [What Is High Memory?](highmem.md#id1)

High memory (highmem) is used when the size of physical memory approaches or
exceeds the maximum size of virtual memory. At that point it becomes
impossible for the kernel to keep all of the available physical memory mapped
at all times. This means the kernel needs to start using temporary mappings of
the pieces of physical memory that it wants to access.

The part of (physical) memory not covered by a permanent mapping is what we
refer to as 'highmem'. There are various architecture dependent constraints on
where exactly that border lies.

In the i386 arch, for example, we choose to map the kernel into every process's
VM space so that we don't have to pay the full TLB invalidation costs for
kernel entry/exit. This means the available virtual memory space (4GiB on
i386) has to be divided between user and kernel space.

The traditional split for architectures using this approach is 3:1, 3GiB for
userspace and the top 1GiB for kernel space:

```
+--------+ 0xffffffff
| Kernel |
+--------+ 0xc0000000
|        |
| User   |
|        |
+--------+ 0x00000000
```

This means that the kernel can at most map 1GiB of physical memory at any one
time, but because we need virtual address space for other things - including
temporary maps to access the rest of the physical memory - the actual direct
map will typically be less (usually around ~896MiB).

Other architectures that have mm context tagged TLBs can have separate kernel
and user maps. Some hardware (like some ARMs), however, have limited virtual
space when they use mm context tags.

## [Temporary Virtual Mappings](highmem.md#id2)

The kernel contains several ways of creating temporary mappings. The following
list shows them in order of preference of use.

- [`kmap_local_page()`](highmem.md#c.kmap_local_page "kmap_local_page"), [`kmap_local_folio()`](highmem.md#c.kmap_local_folio "kmap_local_folio") - These functions are used to create
  short term mappings. They can be invoked from any context (including
  interrupts) but the mappings can only be used in the context which acquired
  them. The only differences between them consist in the first taking a pointer
  to a struct page and the second taking a pointer to [`struct folio`](../core-api/mm-api.md#c.folio "folio") and the byte
  offset within the folio which identifies the page.

  These functions should always be used, whereas [`kmap_atomic()`](highmem.md#c.kmap_atomic "kmap_atomic") and [`kmap()`](highmem.md#c.kmap "kmap") have
  been deprecated.

  These mappings are thread-local and CPU-local, meaning that the mapping
  can only be accessed from within this thread and the thread is bound to the
  CPU while the mapping is active. Although preemption is never disabled by
  this function, the CPU can not be unplugged from the system via
  CPU-hotplug until the mapping is disposed.

  It's valid to take pagefaults in a local kmap region, unless the context
  in which the local mapping is acquired does not allow it for other reasons.

  As said, pagefaults and preemption are never disabled. There is no need to
  disable preemption because, when context switches to a different task, the
  maps of the outgoing task are saved and those of the incoming one are
  restored.

  [`kmap_local_page()`](highmem.md#c.kmap_local_page "kmap_local_page"), as well as [`kmap_local_folio()`](highmem.md#c.kmap_local_folio "kmap_local_folio") always returns valid virtual
  kernel addresses and it is assumed that [`kunmap_local()`](highmem.md#c.kunmap_local "kunmap_local") will never fail.

  On CONFIG_HIGHMEM=n kernels and for low memory pages they return the
  virtual address of the direct mapping. Only real highmem pages are
  temporarily mapped. Therefore, users may call a plain [`page_address()`](highmem.md#c.page_address "page_address")
  for pages which are known to not come from ZONE_HIGHMEM. However, it is
  always safe to use kmap_local_{page,folio}() / [`kunmap_local()`](highmem.md#c.kunmap_local "kunmap_local").

  While they are significantly faster than [`kmap()`](highmem.md#c.kmap "kmap"), for the highmem case they
  come with restrictions about the pointers validity. Contrary to [`kmap()`](highmem.md#c.kmap "kmap")
  mappings, the local mappings are only valid in the context of the caller
  and cannot be handed to other contexts. This implies that users must
  be absolutely sure to keep the use of the return address local to the
  thread which mapped it.

  Most code can be designed to use thread local mappings. User should
  therefore try to design their code to avoid the use of [`kmap()`](highmem.md#c.kmap "kmap") by mapping
  pages in the same thread the address will be used and prefer
  [`kmap_local_page()`](highmem.md#c.kmap_local_page "kmap_local_page") or [`kmap_local_folio()`](highmem.md#c.kmap_local_folio "kmap_local_folio").

  Nesting [`kmap_local_page()`](highmem.md#c.kmap_local_page "kmap_local_page") and [`kmap_atomic()`](highmem.md#c.kmap_atomic "kmap_atomic") mappings is allowed to a certain
  extent (up to KMAP_TYPE_NR) but their invocations have to be strictly ordered
  because the map implementation is stack based. See [`kmap_local_page()`](highmem.md#c.kmap_local_page "kmap_local_page") kdocs
  (included in the "Functions" section) for details on how to manage nested
  mappings.
- [`kmap_atomic()`](highmem.md#c.kmap_atomic "kmap_atomic"). This function has been deprecated; use [`kmap_local_page()`](highmem.md#c.kmap_local_page "kmap_local_page").

  NOTE: Conversions to [`kmap_local_page()`](highmem.md#c.kmap_local_page "kmap_local_page") must take care to follow the mapping
  restrictions imposed on [`kmap_local_page()`](highmem.md#c.kmap_local_page "kmap_local_page"). Furthermore, the code between
  calls to [`kmap_atomic()`](highmem.md#c.kmap_atomic "kmap_atomic") and [`kunmap_atomic()`](highmem.md#c.kunmap_atomic "kunmap_atomic") may implicitly depend on the side
  effects of atomic mappings, i.e. disabling page faults or preemption, or both.
  In that case, explicit calls to pagefault_disable() or preempt_disable() or
  both must be made in conjunction with the use of [`kmap_local_page()`](highmem.md#c.kmap_local_page "kmap_local_page").

  [Legacy documentation]

  This permits a very short duration mapping of a single page. Since the
  mapping is restricted to the CPU that issued it, it performs well, but
  the issuing task is therefore required to stay on that CPU until it has
  finished, lest some other task displace its mappings.

  [`kmap_atomic()`](highmem.md#c.kmap_atomic "kmap_atomic") may also be used by interrupt contexts, since it does not
  sleep and the callers too may not sleep until after [`kunmap_atomic()`](highmem.md#c.kunmap_atomic "kunmap_atomic") is
  called.

  Each call of [`kmap_atomic()`](highmem.md#c.kmap_atomic "kmap_atomic") in the kernel creates a non-preemptible section
  and disable pagefaults. This could be a source of unwanted latency. Therefore
  users should prefer [`kmap_local_page()`](highmem.md#c.kmap_local_page "kmap_local_page") instead of [`kmap_atomic()`](highmem.md#c.kmap_atomic "kmap_atomic").

  It is assumed that k[un]map_atomic() won't fail.
- [`kmap()`](highmem.md#c.kmap "kmap"). This function has been deprecated; use [`kmap_local_page()`](highmem.md#c.kmap_local_page "kmap_local_page").

  NOTE: Conversions to [`kmap_local_page()`](highmem.md#c.kmap_local_page "kmap_local_page") must take care to follow the mapping
  restrictions imposed on [`kmap_local_page()`](highmem.md#c.kmap_local_page "kmap_local_page"). In particular, it is necessary to
  make sure that the kernel virtual memory pointer is only valid in the thread
  that obtained it.

  [Legacy documentation]

  This should be used to make short duration mapping of a single page with no
  restrictions on preemption or migration. It comes with an overhead as mapping
  space is restricted and protected by a global lock for synchronization. When
  mapping is no longer needed, the address that the page was mapped to must be
  released with [`kunmap()`](highmem.md#c.kunmap "kunmap").

  Mapping changes must be propagated across all the CPUs. [`kmap()`](highmem.md#c.kmap "kmap") also
  requires global TLB invalidation when the kmap's pool wraps and it might
  block when the mapping space is fully utilized until a slot becomes
  available. Therefore, [`kmap()`](highmem.md#c.kmap "kmap") is only callable from preemptible context.

  All the above work is necessary if a mapping must last for a relatively
  long time but the bulk of high-memory mappings in the kernel are
  short-lived and only used in one place. This means that the cost of
  [`kmap()`](highmem.md#c.kmap "kmap") is mostly wasted in such cases. [`kmap()`](highmem.md#c.kmap "kmap") was not intended for long
  term mappings but it has morphed in that direction and its use is
  strongly discouraged in newer code and the set of the preceding functions
  should be preferred.

  On 64-bit systems, calls to [`kmap_local_page()`](highmem.md#c.kmap_local_page "kmap_local_page"), [`kmap_atomic()`](highmem.md#c.kmap_atomic "kmap_atomic") and [`kmap()`](highmem.md#c.kmap "kmap") have
  no real work to do because a 64-bit address space is more than sufficient to
  address all the physical memory whose pages are permanently mapped.
- [`vmap()`](../core-api/mm-api.md#c.vmap "vmap"). This can be used to make a long duration mapping of multiple
  physical pages into a contiguous virtual space. It needs global
  synchronization to unmap.

## [Cost of Temporary Mappings](highmem.md#id3)

The cost of creating temporary mappings can be quite high. The arch has to
manipulate the kernel's page tables, the data TLB and/or the MMU's registers.

If CONFIG_HIGHMEM is not set, then the kernel will try and create a mapping
simply with a bit of arithmetic that will convert the page struct address into
a pointer to the page contents rather than juggling mappings about. In such a
case, the unmap operation may be a null operation.

If CONFIG_MMU is not set, then there can be no temporary mappings and no
highmem. In such a case, the arithmetic approach will also be used.

## [i386 PAE](highmem.md#id4)

The i386 arch, under some circumstances, will permit you to stick up to 64GiB
of RAM into your 32-bit machine. This has a number of consequences:

- Linux needs a page-frame structure for each page in the system and the
  pageframes need to live in the permanent mapping, which means:
- you can have 896M/sizeof(struct page) page-frames at most; with struct
  page being 32-bytes that would end up being something in the order of 112G
  worth of pages; the kernel, however, needs to store more than just
  page-frames in that memory...
- PAE makes your page tables larger - which slows the system down as more
  data has to be accessed to traverse in TLB fills and the like. One
  advantage is that PAE has more PTE bits and can provide advanced features
  like NX and PAT.

The general recommendation is that you don't use more than 8GiB on a 32-bit
machine - although more might work for you and your workload, you're pretty
much on your own - don't expect kernel developers to really care much if things
come apart.

## [Functions](highmem.md#id5)

void \*kmap(struct [page](highmem.md#c.kmap "page") \*page)
:   Map a page for long term usage

**Parameters**

`struct page *page`
:   Pointer to the page to be mapped

**Return**

The virtual address of the mapping

**Description**

Can only be invoked from preemptible task context because on 32bit
systems with CONFIG_HIGHMEM enabled this function might sleep.

For systems with CONFIG_HIGHMEM=n and for pages in the low memory area
this returns the virtual address of the direct kernel mapping.

The returned virtual address is globally visible and valid up to the
point where it is unmapped via [`kunmap()`](highmem.md#c.kunmap "kunmap"). The pointer can be handed to
other contexts.

For highmem pages on 32bit systems this can be slow as the mapping space
is limited and protected by a global lock. In case that there is no
mapping slot available the function blocks until a slot is released via
[`kunmap()`](highmem.md#c.kunmap "kunmap").

void kunmap(struct [page](highmem.md#c.kunmap "page") \*page)
:   Unmap the virtual address mapped by [`kmap()`](highmem.md#c.kmap "kmap")

**Parameters**

`struct page *page`
:   Pointer to the page which was mapped by [`kmap()`](highmem.md#c.kmap "kmap")

**Description**

Counterpart to [`kmap()`](highmem.md#c.kmap "kmap"). A NOOP for CONFIG_HIGHMEM=n and for mappings of
pages in the low memory area.

struct page \*kmap_to_page(void \*addr)
:   Get the page for a kmap'ed address

**Parameters**

`void *addr`
:   The address to look up

**Return**

The page which is mapped to **addr**.

void kmap_flush_unused(void)
:   Flush all unused kmap mappings in order to remove stray mappings

**Parameters**

`void`
:   no arguments

void \*kmap_local_page(struct [page](highmem.md#c.kmap_local_page "page") \*page)
:   Map a page for temporary usage

**Parameters**

`struct page *page`
:   Pointer to the page to be mapped

**Return**

The virtual address of the mapping

**Description**

Can be invoked from any context, including interrupts.

Requires careful handling when nesting multiple mappings because the map
management is stack based. The unmap has to be in the reverse order of
the map operation:

addr1 = kmap_local_page(page1);
addr2 = kmap_local_page(page2);
...
kunmap_local(addr2);
kunmap_local(addr1);

Unmapping addr1 before addr2 is invalid and causes malfunction.

Contrary to [`kmap()`](highmem.md#c.kmap "kmap") mappings the mapping is only valid in the context of
the caller and cannot be handed to other contexts.

On CONFIG_HIGHMEM=n kernels and for low memory pages this returns the
virtual address of the direct mapping. Only real highmem pages are
temporarily mapped.

While [`kmap_local_page()`](highmem.md#c.kmap_local_page "kmap_local_page") is significantly faster than [`kmap()`](highmem.md#c.kmap "kmap") for the highmem
case it comes with restrictions about the pointer validity.

On HIGHMEM enabled systems mapping a highmem page has the side effect of
disabling migration in order to keep the virtual address stable across
preemption. No caller of [`kmap_local_page()`](highmem.md#c.kmap_local_page "kmap_local_page") can rely on this side effect.

void \*kmap_local_folio(struct [folio](highmem.md#c.kmap_local_folio "folio") \*folio, size_t offset)
:   Map a page in this folio for temporary usage

**Parameters**

`struct folio *folio`
:   The folio containing the page.

`size_t offset`
:   The byte offset within the folio which identifies the page.

**Description**

Requires careful handling when nesting multiple mappings because the map
management is stack based. The unmap has to be in the reverse order of
the map operation:

```
addr1 = kmap_local_folio(folio1, offset1);
addr2 = kmap_local_folio(folio2, offset2);
...
kunmap_local(addr2);
kunmap_local(addr1);
```

Unmapping addr1 before addr2 is invalid and causes malfunction.

Contrary to [`kmap()`](highmem.md#c.kmap "kmap") mappings the mapping is only valid in the context of
the caller and cannot be handed to other contexts.

On CONFIG_HIGHMEM=n kernels and for low memory pages this returns the
virtual address of the direct mapping. Only real highmem pages are
temporarily mapped.

While it is significantly faster than [`kmap()`](highmem.md#c.kmap "kmap") for the highmem case it
comes with restrictions about the pointer validity.

On HIGHMEM enabled systems mapping a highmem page has the side effect of
disabling migration in order to keep the virtual address stable across
preemption. No caller of [`kmap_local_folio()`](highmem.md#c.kmap_local_folio "kmap_local_folio") can rely on this side effect.

**Context**

Can be invoked from any context.

**Return**

The virtual address of **offset**.

void \*kmap_atomic(struct [page](highmem.md#c.kmap_atomic "page") \*page)
:   Atomically map a page for temporary usage - Deprecated!

**Parameters**

`struct page *page`
:   Pointer to the page to be mapped

**Return**

The virtual address of the mapping

**Description**

In fact a wrapper around [`kmap_local_page()`](highmem.md#c.kmap_local_page "kmap_local_page") which also disables pagefaults
and, depending on PREEMPT_RT configuration, also CPU migration and
preemption. Therefore users should not count on the latter two side effects.

Mappings should always be released by [`kunmap_atomic()`](highmem.md#c.kunmap_atomic "kunmap_atomic").

Do not use in new code. Use [`kmap_local_page()`](highmem.md#c.kmap_local_page "kmap_local_page") instead.

It is used in atomic context when code wants to access the contents of a
page that might be allocated from high memory (see __GFP_HIGHMEM), for
example a page in the pagecache. The API has two functions, and they
can be used in a manner similar to the following:

```
// Find the page of interest.
struct page *page = find_get_page(mapping, offset);

// Gain access to the contents of that page.
void *vaddr = kmap_atomic(page);

// Do something to the contents of that page.
memset(vaddr, 0, PAGE_SIZE);

// Unmap that page.
kunmap_atomic(vaddr);
```

Note that the [`kunmap_atomic()`](highmem.md#c.kunmap_atomic "kunmap_atomic") call takes the result of the [`kmap_atomic()`](highmem.md#c.kmap_atomic "kmap_atomic")
call, not the argument.

If you need to map two pages because you want to copy from one page to
another you need to keep the kmap_atomic calls strictly nested, like:

vaddr1 = kmap_atomic(page1);
vaddr2 = kmap_atomic(page2);

memcpy(vaddr1, vaddr2, PAGE_SIZE);

kunmap_atomic(vaddr2);
kunmap_atomic(vaddr1);

struct [folio](../core-api/mm-api.md#c.folio "folio") \*vma_alloc_zeroed_movable_folio(struct vm_area_struct \*vma, unsigned long vaddr)
:   Allocate a zeroed page for a VMA.

**Parameters**

`struct vm_area_struct *vma`
:   The VMA the page is to be allocated for.

`unsigned long vaddr`
:   The virtual address the page will be inserted into.

**Description**

This function will allocate a page suitable for inserting into this
VMA at this virtual address. It may be allocated from highmem or
the movable zone. An architecture may provide its own implementation.

**Return**

A folio containing one allocated and zeroed page or NULL if
we are out of memory.

void \*folio_zero_tail(struct [folio](highmem.md#c.folio_zero_tail "folio") \*folio, size_t offset, void \*kaddr)
:   Zero the tail of a folio.

**Parameters**

`struct folio *folio`
:   The folio to zero.

`size_t offset`
:   The byte offset in the folio to start zeroing at.

`void *kaddr`
:   The address the folio is currently mapped to.

**Description**

If you have already used [`kmap_local_folio()`](highmem.md#c.kmap_local_folio "kmap_local_folio") to map a folio, written
some data to it and now need to zero the end of the folio (and flush
the dcache), you can use this function. If you do not have the
folio kmapped (eg the folio has been partially populated by DMA),
use [`folio_zero_range()`](highmem.md#c.folio_zero_range "folio_zero_range") or [`folio_zero_segment()`](highmem.md#c.folio_zero_segment "folio_zero_segment") instead.

**Return**

An address which can be passed to [`kunmap_local()`](highmem.md#c.kunmap_local "kunmap_local").

void folio_fill_tail(struct [folio](highmem.md#c.folio_fill_tail "folio") \*folio, size_t offset, const char \*from, size_t len)
:   Copy some data to a folio and pad with zeroes.

**Parameters**

`struct folio *folio`
:   The destination folio.

`size_t offset`
:   The offset into **folio** at which to start copying.

`const char *from`
:   The data to copy.

`size_t len`
:   How many bytes of data to copy.

**Description**

This function is most useful for filesystems which support inline data.
When they want to copy data from the inode into the page cache, this
function does everything for them. It supports large folios even on
HIGHMEM configurations.

size_t memcpy_from_file_folio(char \*to, struct [folio](highmem.md#c.memcpy_from_file_folio "folio") \*folio, loff_t pos, size_t len)
:   Copy some bytes from a file folio.

**Parameters**

`char *to`
:   The destination buffer.

`struct folio *folio`
:   The folio to copy from.

`loff_t pos`
:   The position in the file.

`size_t len`
:   The maximum number of bytes to copy.

**Description**

Copy up to **len** bytes from this folio. This may be limited by PAGE_SIZE
if the folio comes from HIGHMEM, and by the size of the folio.

**Return**

The number of bytes copied from the folio.

void folio_zero_segments(struct [folio](highmem.md#c.folio_zero_segments "folio") \*folio, size_t start1, size_t xend1, size_t start2, size_t xend2)
:   Zero two byte ranges in a folio.

**Parameters**

`struct folio *folio`
:   The folio to write to.

`size_t start1`
:   The first byte to zero.

`size_t xend1`
:   One more than the last byte in the first range.

`size_t start2`
:   The first byte to zero in the second range.

`size_t xend2`
:   One more than the last byte in the second range.

void folio_zero_segment(struct [folio](highmem.md#c.folio_zero_segment "folio") \*folio, size_t start, size_t xend)
:   Zero a byte range in a folio.

**Parameters**

`struct folio *folio`
:   The folio to write to.

`size_t start`
:   The first byte to zero.

`size_t xend`
:   One more than the last byte to zero.

void folio_zero_range(struct [folio](highmem.md#c.folio_zero_range "folio") \*folio, size_t start, size_t length)
:   Zero a byte range in a folio.

**Parameters**

`struct folio *folio`
:   The folio to write to.

`size_t start`
:   The first byte to zero.

`size_t length`
:   The number of bytes to zero.

void folio_release_kmap(struct [folio](highmem.md#c.folio_release_kmap "folio") \*folio, void \*addr)
:   Unmap a folio and drop a refcount.

**Parameters**

`struct folio *folio`
:   The folio to release.

`void *addr`
:   The address previously returned by a call to [`kmap_local_folio()`](highmem.md#c.kmap_local_folio "kmap_local_folio").

**Description**

It is common, eg in directory handling to kmap a folio. This function
unmaps the folio and drops the refcount that was being held to keep the
folio alive while we accessed it.

void \*kmap_high(struct [page](highmem.md#c.kmap_high "page") \*page)
:   map a highmem page into memory

**Parameters**

`struct page *page`
:   `struct page` to map

**Description**

Returns the page's virtual memory address.

We cannot call this from interrupts, as it may block.

void \*kmap_high_get(struct [page](highmem.md#c.kmap_high_get "page") \*page)
:   pin a highmem page into memory

**Parameters**

`struct page *page`
:   `struct page` to pin

**Description**

Returns the page's current virtual memory address, or NULL if no mapping
exists. If and only if a non null address is returned then a
matching call to [`kunmap_high()`](highmem.md#c.kunmap_high "kunmap_high") is necessary.

This can be called from any context.

void kunmap_high(struct [page](highmem.md#c.kunmap_high "page") \*page)
:   unmap a highmem page into memory

**Parameters**

`struct page *page`
:   `struct page` to unmap

**Description**

If ARCH_NEEDS_KMAP_HIGH_GET is not defined then this may be called
only from user context.

void \*page_address(const struct [page](highmem.md#c.page_address "page") \*page)
:   get the mapped virtual address of a page

**Parameters**

`const struct page *page`
:   `struct page` to get the virtual address of

**Description**

Returns the page's virtual address.

void set_page_address(struct [page](highmem.md#c.set_page_address "page") \*page, void \*virtual)
:   set a page's virtual address

**Parameters**

`struct page *page`
:   `struct page` to set

`void *virtual`
:   virtual address to use

kunmap_atomic

`kunmap_atomic (__addr)`

> Unmap the virtual address mapped by [`kmap_atomic()`](highmem.md#c.kmap_atomic "kmap_atomic") - deprecated!

**Parameters**

`__addr`
:   Virtual address to be unmapped

**Description**

Unmaps an address previously mapped by [`kmap_atomic()`](highmem.md#c.kmap_atomic "kmap_atomic") and re-enables
pagefaults. Depending on PREEMP_RT configuration, re-enables also
migration and preemption. Users should not count on these side effects.

Mappings should be unmapped in the reverse order that they were mapped.
See [`kmap_local_page()`](highmem.md#c.kmap_local_page "kmap_local_page") for details on nesting.

**__addr** can be any address within the mapped page, so there is no need
to subtract any offset that has been added. In contrast to [`kunmap()`](highmem.md#c.kunmap "kunmap"),
this function takes the address returned from [`kmap_atomic()`](highmem.md#c.kmap_atomic "kmap_atomic"), not the
page passed to it. The compiler will warn you if you pass the page.

kunmap_local

`kunmap_local (__addr)`

> Unmap a page mapped via [`kmap_local_page()`](highmem.md#c.kmap_local_page "kmap_local_page").

**Parameters**

`__addr`
:   An address within the page mapped

**Description**

**__addr** can be any address within the mapped page. Commonly it is the
address return from [`kmap_local_page()`](highmem.md#c.kmap_local_page "kmap_local_page"), but it can also include offsets.

Unmapping should be done in the reverse order of the mapping. See
[`kmap_local_page()`](highmem.md#c.kmap_local_page "kmap_local_page") for details.
