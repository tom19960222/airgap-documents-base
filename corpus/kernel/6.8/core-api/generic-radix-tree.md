---
collection: kernel
version: "6.8"
title: "Generic radix trees/sparse arrays"
source_url: https://www.kernel.org/doc/html/v6.8/core-api/generic-radix-tree.html
fetched_at: 2026-08-21T03:30:02+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/core-api/generic-radix-tree.md)

# Generic radix trees/sparse arrays

Very simple and minimalistic, supporting arbitrary size entries up to
PAGE_SIZE.

A genradix is defined with the type it will store, like so:

static GENRADIX(struct foo) foo_genradix;

The main operations are:

- genradix_init(radix) - initialize an empty genradix
- genradix_free(radix) - free all memory owned by the genradix and
  reinitialize it
- genradix_ptr(radix, idx) - gets a pointer to the entry at idx, returning
  NULL if that entry does not exist
- genradix_ptr_alloc(radix, idx, gfp) - gets a pointer to an entry,
  allocating it if necessary
- genradix_for_each(radix, iter, p) - iterate over each entry in a genradix

The radix tree allocates one page of entries at a time, so entries may exist
that were never explicitly allocated - they will be initialized to all
zeroes.

Internally, a genradix is just a radix tree of pages, and indexing works in
terms of byte offsets. The wrappers in this header file use sizeof on the
type the radix contains to calculate a byte offset from the index - see
__idx_to_offset.

## generic radix tree functions

genradix_init

`genradix_init (_radix)`

> initialize a genradix

**Parameters**

`_radix`
:   genradix to initialize

**Description**

Does not fail

genradix_free

`genradix_free (_radix)`

> free all memory owned by a genradix

**Parameters**

`_radix`
:   the genradix to free

**Description**

After freeing, **_radix** will be reinitialized and empty

genradix_ptr

`genradix_ptr (_radix, _idx)`

> get a pointer to a genradix entry

**Parameters**

`_radix`
:   genradix to access

`_idx`
:   index to fetch

**Description**

Returns a pointer to entry at **_idx**, or NULL if that entry does not exist.

genradix_ptr_alloc

`genradix_ptr_alloc (_radix, _idx, _gfp)`

> get a pointer to a genradix entry, allocating it if necessary

**Parameters**

`_radix`
:   genradix to access

`_idx`
:   index to fetch

`_gfp`
:   gfp mask

**Description**

Returns a pointer to entry at **_idx**, or NULL on allocation failure

genradix_iter_init

`genradix_iter_init (_radix, _idx)`

> initialize a genradix_iter

**Parameters**

`_radix`
:   genradix that will be iterated over

`_idx`
:   index to start iterating from

genradix_iter_peek

`genradix_iter_peek (_iter, _radix)`

> get first entry at or above iterator's current position

**Parameters**

`_iter`
:   a genradix_iter

`_radix`
:   genradix being iterated over

**Description**

If no more entries exist at or above **_iter**'s current position, returns NULL

genradix_iter_peek_prev

`genradix_iter_peek_prev (_iter, _radix)`

> get first entry at or below iterator's current position

**Parameters**

`_iter`
:   a genradix_iter

`_radix`
:   genradix being iterated over

**Description**

If no more entries exist at or below **_iter**'s current position, returns NULL

genradix_for_each

`genradix_for_each (_radix, _iter, _p)`

> iterate over entry in a genradix

**Parameters**

`_radix`
:   genradix to iterate over

`_iter`
:   a genradix_iter to track current position

`_p`
:   pointer to genradix entry type

**Description**

On every iteration, **_p** will point to the current entry, and **_iter.pos**
will be the current entry's index.

genradix_for_each_reverse

`genradix_for_each_reverse (_radix, _iter, _p)`

> iterate over entry in a genradix, reverse order

**Parameters**

`_radix`
:   genradix to iterate over

`_iter`
:   a genradix_iter to track current position

`_p`
:   pointer to genradix entry type

**Description**

On every iteration, **_p** will point to the current entry, and **_iter.pos**
will be the current entry's index.

genradix_prealloc

`genradix_prealloc (_radix, _nr, _gfp)`

> preallocate entries in a generic radix tree

**Parameters**

`_radix`
:   genradix to preallocate

`_nr`
:   number of entries to preallocate

`_gfp`
:   gfp mask

**Description**

Returns 0 on success, -ENOMEM on failure
