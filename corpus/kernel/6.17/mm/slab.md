---
collection: kernel
version: "6.17"
title: "Slab Allocation"
source_url: https://www.kernel.org/doc/html/v6.17/mm/slab.html
fetched_at: 2026-09-16T16:28:34+00:00
---
# Slab Allocation

## Functions and structures

folio_slab

`folio_slab (folio)`

> Converts from folio to slab.

**Parameters**

`folio`
:   The folio.

**Description**

Currently `struct slab` is a different representation of a folio where
`folio_test_slab()` is true.

**Return**

The slab which contains this folio.

slab_folio

`slab_folio (s)`

> The folio allocated for a slab

**Parameters**

`s`
:   The slab.

**Description**

Slabs are allocated as folios that contain the individual objects and are
using some fields in the first `struct page` of the folio - those fields are
now accessed by `struct slab`. It is occasionally necessary to convert back to
a folio in order to communicate with the rest of the mm. Please use this
helper function instead of casting yourself, as the implementation may change
in the future.

page_slab

`page_slab (p)`

> Converts from first `struct page` to slab.

**Parameters**

`p`
:   The first (either head of compound or single) page of slab.

**Description**

A temporary wrapper to convert `struct page` to `struct slab` in situations where
we know the page is the compound head, or single order-0 page.

Long-term ideally everything would work with `struct slab` directly or go
through folio to `struct slab`.

**Return**

The slab which contains this page

slab_page

`slab_page (s)`

> The first `struct page` allocated for a slab

**Parameters**

`s`
:   The slab.

**Description**

A convenience wrapper for converting slab to the first `struct page` of the
underlying folio, to communicate with code not yet converted to folio or
`struct slab`.

enum slab_flags
:   How the slab flags bits are used.

**Constants**

`SL_locked`
:   Is locked with `slab_lock()`

`SL_partial`
:   On the per-node partial list

`SL_pfmemalloc`
:   Was allocated from PF_MEMALLOC reserves

**Description**

The slab flags share space with the page flags but some bits have
different interpretations. The high bits are used for information
like zone/node/section.
