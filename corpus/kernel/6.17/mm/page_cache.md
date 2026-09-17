---
collection: kernel
version: "6.17"
title: "Page Cache"
source_url: https://www.kernel.org/doc/html/v6.17/mm/page_cache.html
fetched_at: 2026-09-16T16:36:08+00:00
---
# Page Cache

The page cache is the primary way that the user and the rest of the kernel
interact with filesystems. It can be bypassed (e.g. with O_DIRECT),
but normal reads, writes and mmaps go through the page cache.

## Folios

The folio is the unit of memory management within the page cache.
Operations
