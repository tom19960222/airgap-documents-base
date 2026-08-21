---
collection: kernel
version: "6.8"
title: "Kernel Samepage Merging"
source_url: https://www.kernel.org/doc/html/v6.8/mm/ksm.html
fetched_at: 2026-08-21T03:39:51+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/mm/ksm.md)

# Kernel Samepage Merging

KSM is a memory-saving de-duplication feature, enabled by CONFIG_KSM=y,
added to the Linux kernel in 2.6.32. See `mm/ksm.c` for its implementation,
and <http://lwn.net/Articles/306704/> and <https://lwn.net/Articles/330589/>

The userspace interface of KSM is described in [Kernel Samepage Merging](../admin-guide/mm/ksm.md)

## Design

### Overview

A few notes about the KSM scanning process,
to make it easier to understand the data structures below:

In order to reduce excessive scanning, KSM sorts the memory pages by their
contents into a data structure that holds pointers to the pages' locations.

Since the contents of the pages may change at any moment, KSM cannot just
insert the pages into a normal sorted tree and expect it to find anything.
Therefore KSM uses two data structures - the stable and the unstable tree.

The stable tree holds pointers to all the merged pages (ksm pages), sorted
by their contents. Because each such page is write-protected, searching on
this tree is fully assured to be working (except when pages are unmapped),
and therefore this tree is called the stable tree.

The stable tree node includes information required for reverse
mapping from a KSM page to virtual addresses that map this page.

In order to avoid large latencies of the rmap walks on KSM pages,
KSM maintains two types of nodes in the stable tree:

- the regular nodes that keep the reverse mapping structures in a
  linked list
- the "chains" that link nodes ("dups") that represent the same
  write protected memory content, but each "dup" corresponds to a
  different KSM page copy of that content

Internally, the regular nodes, "dups" and "chains" are represented
using the same struct ksm_stable_node structure.

In addition to the stable tree, KSM uses a second data structure called the
unstable tree: this tree holds pointers to pages which have been found to
be "unchanged for a period of time". The unstable tree sorts these pages
by their contents, but since they are not write-protected, KSM cannot rely
upon the unstable tree to work correctly - the unstable tree is liable to
be corrupted as its contents are modified, and so it is called unstable.

KSM solves this problem by several techniques:

1. The unstable tree is flushed every time KSM completes scanning all
   memory areas, and then the tree is rebuilt again from the beginning.
2. KSM will only insert into the unstable tree, pages whose hash value
   has not changed since the previous scan of all memory areas.
3. The unstable tree is a RedBlack Tree - so its balancing is based on the
   colors of the nodes and not on their contents, assuring that even when
   the tree gets "corrupted" it won't get out of balance, so scanning time
   remains the same (also, searching and inserting nodes in an rbtree uses
   the same algorithm, so we have no overhead when we flush and rebuild).
4. KSM never flushes the stable tree, which means that even if it were to
   take 10 attempts to find a page in the unstable tree, once it is found,
   it is secured in the stable tree. (When we scan a new page, we first
   compare it against the stable tree, and then against the unstable tree.)

If the merge_across_nodes tunable is unset, then KSM maintains multiple
stable trees and multiple unstable trees: one of each for each NUMA node.

### Reverse mapping

KSM maintains reverse mapping information for KSM pages in the stable
tree.

If a KSM page is shared between less than `max_page_sharing` VMAs,
the node of the stable tree that represents such KSM page points to a
list of struct ksm_rmap_item and the `page->mapping` of the
KSM page points to the stable tree node.

When the sharing passes this threshold, KSM adds a second dimension to
the stable tree. The tree node becomes a "chain" that links one or
more "dups". Each "dup" keeps reverse mapping information for a KSM
page with `page->mapping` pointing to that "dup".

Every "chain" and all "dups" linked into a "chain" enforce the
invariant that they represent the same write protected memory content,
even if each "dup" will be pointed by a different KSM page copy of
that content.

This way the stable tree lookup computational complexity is unaffected
if compared to an unlimited list of reverse mappings. It is still
enforced that there cannot be KSM page content duplicates in the
stable tree itself.

The deduplication limit enforced by `max_page_sharing` is required
to avoid the virtual memory rmap lists to grow too large. The rmap
walk has O(N) complexity where N is the number of rmap_items
(i.e. virtual mappings) that are sharing the page, which is in turn
capped by `max_page_sharing`. So this effectively spreads the linear
O(N) computational complexity from rmap walk context over different
KSM pages. The ksmd walk over the stable_node "chains" is also O(N),
but N is the number of stable_node "dups", not the number of
rmap_items, so it has not a significant impact on ksmd performance. In
practice the best stable_node "dup" candidate will be kept and found
at the head of the "dups" list.

High values of `max_page_sharing` result in faster memory merging
(because there will be fewer stable_node dups queued into the
stable_node chain->hlist to check for pruning) and higher
deduplication factor at the expense of slower worst case for rmap
walks for any KSM page which can happen during swapping, compaction,
NUMA balancing and page migration.

The `stable_node_dups/stable_node_chains` ratio is also affected by the
`max_page_sharing` tunable, and an high ratio may indicate fragmentation
in the stable_node dups, which could be solved by introducing
fragmentation algorithms in ksmd which would refile rmap_items from
one stable_node dup to another stable_node dup, in order to free up
stable_node "dups" with few rmap_items in them, but that may increase
the ksmd CPU usage and possibly slowdown the readonly computations on
the KSM pages of the applications.

The whole list of stable_node "dups" linked in the stable_node
"chains" is scanned periodically in order to prune stale stable_nodes.
The frequency of such scans is defined by
`stable_node_chains_prune_millisecs` sysfs tunable.

### Reference

struct ksm_scan
:   cursor for scanning

**Definition**:

```
struct ksm_scan {
    struct ksm_mm_slot *mm_slot;
    unsigned long address;
    struct ksm_rmap_item **rmap_list;
    unsigned long seqnr;
};
```

**Members**

`mm_slot`
:   the current mm_slot we are scanning

`address`
:   the next address inside that to be scanned

`rmap_list`
:   link to the next rmap to be scanned in the rmap_list

`seqnr`
:   count of completed full scans (needed when removing unstable node)

**Description**

There is only the one ksm_scan instance of this cursor structure.

--
Izik Eidus,
Hugh Dickins, 17 Nov 2009
