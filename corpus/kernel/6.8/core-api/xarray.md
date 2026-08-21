---
collection: kernel
version: "6.8"
title: "XArray"
source_url: https://www.kernel.org/doc/html/v6.8/core-api/xarray.html
fetched_at: 2026-08-21T03:29:58+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/core-api/xarray.md)

# XArray

Author
:   Matthew Wilcox

## Overview

The XArray is an abstract data type which behaves like a very large array
of pointers. It meets many of the same needs as a hash or a conventional
resizable array. Unlike a hash, it allows you to sensibly go to the
next or previous entry in a cache-efficient manner. In contrast to a
resizable array, there is no need to copy data or change MMU mappings in
order to grow the array. It is more memory-efficient, parallelisable
and cache friendly than a doubly-linked list. It takes advantage of
RCU to perform lookups without locking.

The XArray implementation is efficient when the indices used are densely
clustered; hashing the object and using the hash as the index will not
perform well. The XArray is optimised for small indices, but still has
good performance with large indices. If your index can be larger than
`ULONG_MAX` then the XArray is not the data type for you. The most
important user of the XArray is the page cache.

Normal pointers may be stored in the XArray directly. They must be 4-byte
aligned, which is true for any pointer returned from [`kmalloc()`](mm-api.md#c.kmalloc "kmalloc") and
alloc_page(). It isn't true for arbitrary user-space pointers,
nor for function pointers. You can store pointers to statically allocated
objects, as long as those objects have an alignment of at least 4.

You can also store integers between 0 and `LONG_MAX` in the XArray.
You must first convert it into an entry using [`xa_mk_value()`](xarray.md#c.xa_mk_value "xa_mk_value").
When you retrieve an entry from the XArray, you can check whether it is
a value entry by calling [`xa_is_value()`](xarray.md#c.xa_is_value "xa_is_value"), and convert it back to
an integer by calling [`xa_to_value()`](xarray.md#c.xa_to_value "xa_to_value").

Some users want to tag the pointers they store in the XArray. You can
call [`xa_tag_pointer()`](xarray.md#c.xa_tag_pointer "xa_tag_pointer") to create an entry with a tag, [`xa_untag_pointer()`](xarray.md#c.xa_untag_pointer "xa_untag_pointer")
to turn a tagged entry back into an untagged pointer and [`xa_pointer_tag()`](xarray.md#c.xa_pointer_tag "xa_pointer_tag")
to retrieve the tag of an entry. Tagged pointers use the same bits that
are used to distinguish value entries from normal pointers, so you must
decide whether they want to store value entries or tagged pointers in
any particular XArray.

The XArray does not support storing [`IS_ERR()`](kernel-api.md#c.IS_ERR "IS_ERR") pointers as some
conflict with value entries or internal entries.

An unusual feature of the XArray is the ability to create entries which
occupy a range of indices. Once stored to, looking up any index in
the range will return the same entry as looking up any other index in
the range. Storing to any index will store to all of them. Multi-index
entries can be explicitly split into smaller entries, or storing `NULL`
into any entry will cause the XArray to forget about the range.

## Normal API

Start by initialising an XArray, either with [`DEFINE_XARRAY()`](xarray.md#c.DEFINE_XARRAY "DEFINE_XARRAY")
for statically allocated XArrays or [`xa_init()`](xarray.md#c.xa_init "xa_init") for dynamically
allocated ones. A freshly-initialised XArray contains a `NULL`
pointer at every index.

You can then set entries using [`xa_store()`](xarray.md#c.xa_store "xa_store") and get entries
using [`xa_load()`](xarray.md#c.xa_load "xa_load"). xa_store will overwrite any entry with the
new entry and return the previous entry stored at that index. You can
use [`xa_erase()`](xarray.md#c.xa_erase "xa_erase") instead of calling [`xa_store()`](xarray.md#c.xa_store "xa_store") with a
`NULL` entry. There is no difference between an entry that has never
been stored to, one that has been erased and one that has most recently
had `NULL` stored to it.

You can conditionally replace an entry at an index by using
[`xa_cmpxchg()`](xarray.md#c.xa_cmpxchg "xa_cmpxchg"). Like cmpxchg(), it will only succeed if
the entry at that index has the 'old' value. It also returns the entry
which was at that index; if it returns the same entry which was passed as
'old', then [`xa_cmpxchg()`](xarray.md#c.xa_cmpxchg "xa_cmpxchg") succeeded.

If you want to only store a new entry to an index if the current entry
at that index is `NULL`, you can use [`xa_insert()`](xarray.md#c.xa_insert "xa_insert") which
returns `-EBUSY` if the entry is not empty.

You can copy entries out of the XArray into a plain array by calling
[`xa_extract()`](xarray.md#c.xa_extract "xa_extract"). Or you can iterate over the present entries in the XArray
by calling [`xa_for_each()`](xarray.md#c.xa_for_each "xa_for_each"), [`xa_for_each_start()`](xarray.md#c.xa_for_each_start "xa_for_each_start") or [`xa_for_each_range()`](xarray.md#c.xa_for_each_range "xa_for_each_range").
You may prefer to use [`xa_find()`](xarray.md#c.xa_find "xa_find") or [`xa_find_after()`](xarray.md#c.xa_find_after "xa_find_after") to move to the next
present entry in the XArray.

Calling [`xa_store_range()`](xarray.md#c.xa_store_range "xa_store_range") stores the same entry in a range
of indices. If you do this, some of the other operations will behave
in a slightly odd way. For example, marking the entry at one index
may result in the entry being marked at some, but not all of the other
indices. Storing into one index may result in the entry retrieved by
some, but not all of the other indices changing.

Sometimes you need to ensure that a subsequent call to [`xa_store()`](xarray.md#c.xa_store "xa_store")
will not need to allocate memory. The [`xa_reserve()`](xarray.md#c.xa_reserve "xa_reserve") function
will store a reserved entry at the indicated index. Users of the
normal API will see this entry as containing `NULL`. If you do
not need to use the reserved entry, you can call [`xa_release()`](xarray.md#c.xa_release "xa_release")
to remove the unused entry. If another user has stored to the entry
in the meantime, [`xa_release()`](xarray.md#c.xa_release "xa_release") will do nothing; if instead you
want the entry to become `NULL`, you should use [`xa_erase()`](xarray.md#c.xa_erase "xa_erase").
Using [`xa_insert()`](xarray.md#c.xa_insert "xa_insert") on a reserved entry will fail.

If all entries in the array are `NULL`, the [`xa_empty()`](xarray.md#c.xa_empty "xa_empty") function
will return `true`.

Finally, you can remove all entries from an XArray by calling
[`xa_destroy()`](xarray.md#c.xa_destroy "xa_destroy"). If the XArray entries are pointers, you may wish
to free the entries first. You can do this by iterating over all present
entries in the XArray using the [`xa_for_each()`](xarray.md#c.xa_for_each "xa_for_each") iterator.

### Search Marks

Each entry in the array has three bits associated with it called marks.
Each mark may be set or cleared independently of the others. You can
iterate over marked entries by using the [`xa_for_each_marked()`](xarray.md#c.xa_for_each_marked "xa_for_each_marked") iterator.

You can enquire whether a mark is set on an entry by using
[`xa_get_mark()`](xarray.md#c.xa_get_mark "xa_get_mark"). If the entry is not `NULL`, you can set a mark on it
by using [`xa_set_mark()`](xarray.md#c.xa_set_mark "xa_set_mark") and remove the mark from an entry by calling
[`xa_clear_mark()`](xarray.md#c.xa_clear_mark "xa_clear_mark"). You can ask whether any entry in the XArray has a
particular mark set by calling [`xa_marked()`](xarray.md#c.xa_marked "xa_marked"). Erasing an entry from the
XArray causes all marks associated with that entry to be cleared.

Setting or clearing a mark on any index of a multi-index entry will
affect all indices covered by that entry. Querying the mark on any
index will return the same result.

There is no way to iterate over entries which are not marked; the data
structure does not allow this to be implemented efficiently. There are
not currently iterators to search for logical combinations of bits (eg
iterate over all entries which have both `XA_MARK_1` and `XA_MARK_2`
set, or iterate over all entries which have `XA_MARK_0` or `XA_MARK_2`
set). It would be possible to add these if a user arises.

### Allocating XArrays

If you use [`DEFINE_XARRAY_ALLOC()`](xarray.md#c.DEFINE_XARRAY_ALLOC "DEFINE_XARRAY_ALLOC") to define the XArray, or
initialise it by passing `XA_FLAGS_ALLOC` to [`xa_init_flags()`](xarray.md#c.xa_init_flags "xa_init_flags"),
the XArray changes to track whether entries are in use or not.

You can call [`xa_alloc()`](xarray.md#c.xa_alloc "xa_alloc") to store the entry at an unused index
in the XArray. If you need to modify the array from interrupt context,
you can use [`xa_alloc_bh()`](xarray.md#c.xa_alloc_bh "xa_alloc_bh") or [`xa_alloc_irq()`](xarray.md#c.xa_alloc_irq "xa_alloc_irq") to disable
interrupts while allocating the ID.

Using [`xa_store()`](xarray.md#c.xa_store "xa_store"), [`xa_cmpxchg()`](xarray.md#c.xa_cmpxchg "xa_cmpxchg") or [`xa_insert()`](xarray.md#c.xa_insert "xa_insert") will
also mark the entry as being allocated. Unlike a normal XArray, storing
`NULL` will mark the entry as being in use, like [`xa_reserve()`](xarray.md#c.xa_reserve "xa_reserve").
To free an entry, use [`xa_erase()`](xarray.md#c.xa_erase "xa_erase") (or [`xa_release()`](xarray.md#c.xa_release "xa_release") if
you only want to free the entry if it's `NULL`).

By default, the lowest free entry is allocated starting from 0. If you
want to allocate entries starting at 1, it is more efficient to use
[`DEFINE_XARRAY_ALLOC1()`](xarray.md#c.DEFINE_XARRAY_ALLOC1 "DEFINE_XARRAY_ALLOC1") or `XA_FLAGS_ALLOC1`. If you want to
allocate IDs up to a maximum, then wrap back around to the lowest free
ID, you can use [`xa_alloc_cyclic()`](xarray.md#c.xa_alloc_cyclic "xa_alloc_cyclic").

You cannot use `XA_MARK_0` with an allocating XArray as this mark
is used to track whether an entry is free or not. The other marks are
available for your use.

### Memory allocation

The [`xa_store()`](xarray.md#c.xa_store "xa_store"), [`xa_cmpxchg()`](xarray.md#c.xa_cmpxchg "xa_cmpxchg"), [`xa_alloc()`](xarray.md#c.xa_alloc "xa_alloc"),
[`xa_reserve()`](xarray.md#c.xa_reserve "xa_reserve") and [`xa_insert()`](xarray.md#c.xa_insert "xa_insert") functions take a gfp_t
parameter in case the XArray needs to allocate memory to store this entry.
If the entry is being deleted, no memory allocation needs to be performed,
and the GFP flags specified will be ignored.

It is possible for no memory to be allocatable, particularly if you pass
a restrictive set of GFP flags. In that case, the functions return a
special value which can be turned into an errno using [`xa_err()`](xarray.md#c.xa_err "xa_err").
If you don't need to know exactly which error occurred, using
[`xa_is_err()`](xarray.md#c.xa_is_err "xa_is_err") is slightly more efficient.

### Locking

When using the Normal API, you do not have to worry about locking.
The XArray uses RCU and an internal spinlock to synchronise access:

No lock needed:
:   - [`xa_empty()`](xarray.md#c.xa_empty "xa_empty")
    - [`xa_marked()`](xarray.md#c.xa_marked "xa_marked")

Takes RCU read lock:
:   - [`xa_load()`](xarray.md#c.xa_load "xa_load")
    - [`xa_for_each()`](xarray.md#c.xa_for_each "xa_for_each")
    - [`xa_for_each_start()`](xarray.md#c.xa_for_each_start "xa_for_each_start")
    - [`xa_for_each_range()`](xarray.md#c.xa_for_each_range "xa_for_each_range")
    - [`xa_find()`](xarray.md#c.xa_find "xa_find")
    - [`xa_find_after()`](xarray.md#c.xa_find_after "xa_find_after")
    - [`xa_extract()`](xarray.md#c.xa_extract "xa_extract")
    - [`xa_get_mark()`](xarray.md#c.xa_get_mark "xa_get_mark")

Takes xa_lock internally:
:   - [`xa_store()`](xarray.md#c.xa_store "xa_store")
    - [`xa_store_bh()`](xarray.md#c.xa_store_bh "xa_store_bh")
    - [`xa_store_irq()`](xarray.md#c.xa_store_irq "xa_store_irq")
    - [`xa_insert()`](xarray.md#c.xa_insert "xa_insert")
    - [`xa_insert_bh()`](xarray.md#c.xa_insert_bh "xa_insert_bh")
    - [`xa_insert_irq()`](xarray.md#c.xa_insert_irq "xa_insert_irq")
    - [`xa_erase()`](xarray.md#c.xa_erase "xa_erase")
    - [`xa_erase_bh()`](xarray.md#c.xa_erase_bh "xa_erase_bh")
    - [`xa_erase_irq()`](xarray.md#c.xa_erase_irq "xa_erase_irq")
    - [`xa_cmpxchg()`](xarray.md#c.xa_cmpxchg "xa_cmpxchg")
    - [`xa_cmpxchg_bh()`](xarray.md#c.xa_cmpxchg_bh "xa_cmpxchg_bh")
    - [`xa_cmpxchg_irq()`](xarray.md#c.xa_cmpxchg_irq "xa_cmpxchg_irq")
    - [`xa_store_range()`](xarray.md#c.xa_store_range "xa_store_range")
    - [`xa_alloc()`](xarray.md#c.xa_alloc "xa_alloc")
    - [`xa_alloc_bh()`](xarray.md#c.xa_alloc_bh "xa_alloc_bh")
    - [`xa_alloc_irq()`](xarray.md#c.xa_alloc_irq "xa_alloc_irq")
    - [`xa_reserve()`](xarray.md#c.xa_reserve "xa_reserve")
    - [`xa_reserve_bh()`](xarray.md#c.xa_reserve_bh "xa_reserve_bh")
    - [`xa_reserve_irq()`](xarray.md#c.xa_reserve_irq "xa_reserve_irq")
    - [`xa_destroy()`](xarray.md#c.xa_destroy "xa_destroy")
    - [`xa_set_mark()`](xarray.md#c.xa_set_mark "xa_set_mark")
    - [`xa_clear_mark()`](xarray.md#c.xa_clear_mark "xa_clear_mark")

Assumes xa_lock held on entry:
:   - [`__xa_store()`](xarray.md#c.__xa_store "__xa_store")
    - [`__xa_insert()`](xarray.md#c.__xa_insert "__xa_insert")
    - [`__xa_erase()`](xarray.md#c.__xa_erase "__xa_erase")
    - [`__xa_cmpxchg()`](xarray.md#c.__xa_cmpxchg "__xa_cmpxchg")
    - [`__xa_alloc()`](xarray.md#c.__xa_alloc "__xa_alloc")
    - [`__xa_set_mark()`](xarray.md#c.__xa_set_mark "__xa_set_mark")
    - [`__xa_clear_mark()`](xarray.md#c.__xa_clear_mark "__xa_clear_mark")

If you want to take advantage of the lock to protect the data structures
that you are storing in the XArray, you can call xa_lock()
before calling [`xa_load()`](xarray.md#c.xa_load "xa_load"), then take a reference count on the
object you have found before calling xa_unlock(). This will
prevent stores from removing the object from the array between looking
up the object and incrementing the refcount. You can also use RCU to
avoid dereferencing freed memory, but an explanation of that is beyond
the scope of this document.

The XArray does not disable interrupts or softirqs while modifying
the array. It is safe to read the XArray from interrupt or softirq
context as the RCU lock provides enough protection.

If, for example, you want to store entries in the XArray in process
context and then erase them in softirq context, you can do that this way:

```
void foo_init(struct foo *foo)
{
    xa_init_flags(&foo->array, XA_FLAGS_LOCK_BH);
}

int foo_store(struct foo *foo, unsigned long index, void *entry)
{
    int err;

    xa_lock_bh(&foo->array);
    err = xa_err(__xa_store(&foo->array, index, entry, GFP_KERNEL));
    if (!err)
        foo->count++;
    xa_unlock_bh(&foo->array);
    return err;
}

/* foo_erase() is only called from softirq context */
void foo_erase(struct foo *foo, unsigned long index)
{
    xa_lock(&foo->array);
    __xa_erase(&foo->array, index);
    foo->count--;
    xa_unlock(&foo->array);
}
```

If you are going to modify the XArray from interrupt or softirq context,
you need to initialise the array using [`xa_init_flags()`](xarray.md#c.xa_init_flags "xa_init_flags"), passing
`XA_FLAGS_LOCK_IRQ` or `XA_FLAGS_LOCK_BH`.

The above example also shows a common pattern of wanting to extend the
coverage of the xa_lock on the store side to protect some statistics
associated with the array.

Sharing the XArray with interrupt context is also possible, either
using xa_lock_irqsave() in both the interrupt handler and process
context, or xa_lock_irq() in process context and xa_lock()
in the interrupt handler. Some of the more common patterns have helper
functions such as [`xa_store_bh()`](xarray.md#c.xa_store_bh "xa_store_bh"), [`xa_store_irq()`](xarray.md#c.xa_store_irq "xa_store_irq"),
[`xa_erase_bh()`](xarray.md#c.xa_erase_bh "xa_erase_bh"), [`xa_erase_irq()`](xarray.md#c.xa_erase_irq "xa_erase_irq"), [`xa_cmpxchg_bh()`](xarray.md#c.xa_cmpxchg_bh "xa_cmpxchg_bh")
and [`xa_cmpxchg_irq()`](xarray.md#c.xa_cmpxchg_irq "xa_cmpxchg_irq").

Sometimes you need to protect access to the XArray with a mutex because
that lock sits above another mutex in the locking hierarchy. That does
not entitle you to use functions like [`__xa_erase()`](xarray.md#c.__xa_erase "__xa_erase") without taking
the xa_lock; the xa_lock is used for lockdep validation and will be used
for other purposes in the future.

The [`__xa_set_mark()`](xarray.md#c.__xa_set_mark "__xa_set_mark") and [`__xa_clear_mark()`](xarray.md#c.__xa_clear_mark "__xa_clear_mark") functions are also
available for situations where you look up an entry and want to atomically
set or clear a mark. It may be more efficient to use the advanced API
in this case, as it will save you from walking the tree twice.

## Advanced API

The advanced API offers more flexibility and better performance at the
cost of an interface which can be harder to use and has fewer safeguards.
No locking is done for you by the advanced API, and you are required
to use the xa_lock while modifying the array. You can choose whether
to use the xa_lock or the RCU lock while doing read-only operations on
the array. You can mix advanced and normal operations on the same array;
indeed the normal API is implemented in terms of the advanced API. The
advanced API is only available to modules with a GPL-compatible license.

The advanced API is based around the xa_state. This is an opaque data
structure which you declare on the stack using the [`XA_STATE()`](xarray.md#c.XA_STATE "XA_STATE") macro.
This macro initialises the xa_state ready to start walking around the
XArray. It is used as a cursor to maintain the position in the XArray
and let you compose various operations together without having to restart
from the top every time. The contents of the xa_state are protected by
the [`rcu_read_lock()`](kernel-api.md#c.rcu_read_lock "rcu_read_lock") or the xas_lock(). If you need to drop whichever of
those locks is protecting your state and tree, you must call [`xas_pause()`](xarray.md#c.xas_pause "xas_pause")
so that future calls do not rely on the parts of the state which were
left unprotected.

The xa_state is also used to store errors. You can call
[`xas_error()`](xarray.md#c.xas_error "xas_error") to retrieve the error. All operations check whether
the xa_state is in an error state before proceeding, so there's no need
for you to check for an error after each call; you can make multiple
calls in succession and only check at a convenient point. The only
errors currently generated by the XArray code itself are `ENOMEM` and
`EINVAL`, but it supports arbitrary errors in case you want to call
[`xas_set_err()`](xarray.md#c.xas_set_err "xas_set_err") yourself.

If the xa_state is holding an `ENOMEM` error, calling [`xas_nomem()`](xarray.md#c.xas_nomem "xas_nomem")
will attempt to allocate more memory using the specified gfp flags and
cache it in the xa_state for the next attempt. The idea is that you take
the xa_lock, attempt the operation and drop the lock. The operation
attempts to allocate memory while holding the lock, but it is more
likely to fail. Once you have dropped the lock, [`xas_nomem()`](xarray.md#c.xas_nomem "xas_nomem")
can try harder to allocate more memory. It will return `true` if it
is worth retrying the operation (i.e. that there was a memory error *and*
more memory was allocated). If it has previously allocated memory, and
that memory wasn't used, and there is no error (or some error that isn't
`ENOMEM`), then it will free the memory previously allocated.

### Internal Entries

The XArray reserves some entries for its own purposes. These are never
exposed through the normal API, but when using the advanced API, it's
possible to see them. Usually the best way to handle them is to pass them
to [`xas_retry()`](xarray.md#c.xas_retry "xas_retry"), and retry the operation if it returns `true`.

|  |  |  |
| --- | --- | --- |
| Name | Test | Usage |
| Node | xa_is_node() | An XArray node. May be visible when using a multi-index xa_state. |
| Sibling | [`xa_is_sibling()`](xarray.md#c.xa_is_sibling "xa_is_sibling") | A non-canonical entry for a multi-index entry. The value indicates which slot in this node has the canonical entry. |
| Retry | [`xa_is_retry()`](xarray.md#c.xa_is_retry "xa_is_retry") | This entry is currently being modified by a thread which has the xa_lock. The node containing this entry may be freed at the end of this RCU period. You should restart the lookup from the head of the array. |
| Zero | [`xa_is_zero()`](xarray.md#c.xa_is_zero "xa_is_zero") | Zero entries appear as `NULL` through the Normal API, but occupy an entry in the XArray which can be used to reserve the index for future use. This is used by allocating XArrays for allocated entries which are `NULL`. |

Other internal entries may be added in the future. As far as possible, they
will be handled by [`xas_retry()`](xarray.md#c.xas_retry "xas_retry").

### Additional functionality

The [`xas_create_range()`](xarray.md#c.xas_create_range "xas_create_range") function allocates all the necessary memory
to store every entry in a range. It will set ENOMEM in the xa_state if
it cannot allocate memory.

You can use [`xas_init_marks()`](xarray.md#c.xas_init_marks "xas_init_marks") to reset the marks on an entry
to their default state. This is usually all marks clear, unless the
XArray is marked with `XA_FLAGS_TRACK_FREE`, in which case mark 0 is set
and all other marks are clear. Replacing one entry with another using
[`xas_store()`](xarray.md#c.xas_store "xas_store") will not reset the marks on that entry; if you want
the marks reset, you should do that explicitly.

The [`xas_load()`](xarray.md#c.xas_load "xas_load") will walk the xa_state as close to the entry
as it can. If you know the xa_state has already been walked to the
entry and need to check that the entry hasn't changed, you can use
[`xas_reload()`](xarray.md#c.xas_reload "xas_reload") to save a function call.

If you need to move to a different index in the XArray, call
[`xas_set()`](xarray.md#c.xas_set "xas_set"). This resets the cursor to the top of the tree, which
will generally make the next operation walk the cursor to the desired
spot in the tree. If you want to move to the next or previous index,
call [`xas_next()`](xarray.md#c.xas_next "xas_next") or [`xas_prev()`](xarray.md#c.xas_prev "xas_prev"). Setting the index does
not walk the cursor around the array so does not require a lock to be
held, while moving to the next or previous index does.

You can search for the next present entry using [`xas_find()`](xarray.md#c.xas_find "xas_find"). This
is the equivalent of both [`xa_find()`](xarray.md#c.xa_find "xa_find") and [`xa_find_after()`](xarray.md#c.xa_find_after "xa_find_after");
if the cursor has been walked to an entry, then it will find the next
entry after the one currently referenced. If not, it will return the
entry at the index of the xa_state. Using [`xas_next_entry()`](xarray.md#c.xas_next_entry "xas_next_entry") to
move to the next present entry instead of [`xas_find()`](xarray.md#c.xas_find "xas_find") will save
a function call in the majority of cases at the expense of emitting more
inline code.

The [`xas_find_marked()`](xarray.md#c.xas_find_marked "xas_find_marked") function is similar. If the xa_state has
not been walked, it will return the entry at the index of the xa_state,
if it is marked. Otherwise, it will return the first marked entry after
the entry referenced by the xa_state. The [`xas_next_marked()`](xarray.md#c.xas_next_marked "xas_next_marked")
function is the equivalent of [`xas_next_entry()`](xarray.md#c.xas_next_entry "xas_next_entry").

When iterating over a range of the XArray using [`xas_for_each()`](xarray.md#c.xas_for_each "xas_for_each")
or [`xas_for_each_marked()`](xarray.md#c.xas_for_each_marked "xas_for_each_marked"), it may be necessary to temporarily stop
the iteration. The [`xas_pause()`](xarray.md#c.xas_pause "xas_pause") function exists for this purpose.
After you have done the necessary work and wish to resume, the xa_state
is in an appropriate state to continue the iteration after the entry
you last processed. If you have interrupts disabled while iterating,
then it is good manners to pause the iteration and reenable interrupts
every `XA_CHECK_SCHED` entries.

The [`xas_get_mark()`](xarray.md#c.xas_get_mark "xas_get_mark"), [`xas_set_mark()`](xarray.md#c.xas_set_mark "xas_set_mark") and [`xas_clear_mark()`](xarray.md#c.xas_clear_mark "xas_clear_mark") functions require
the xa_state cursor to have been moved to the appropriate location in the
XArray; they will do nothing if you have called [`xas_pause()`](xarray.md#c.xas_pause "xas_pause") or [`xas_set()`](xarray.md#c.xas_set "xas_set")
immediately before.

You can call [`xas_set_update()`](xarray.md#c.xas_set_update "xas_set_update") to have a callback function
called each time the XArray updates a node. This is used by the page
cache workingset code to maintain its list of nodes which contain only
shadow entries.

### Multi-Index Entries

The XArray has the ability to tie multiple indices together so that
operations on one index affect all indices. For example, storing into
any index will change the value of the entry retrieved from any index.
Setting or clearing a mark on any index will set or clear the mark
on every index that is tied together. The current implementation
only allows tying ranges which are aligned powers of two together;
eg indices 64-127 may be tied together, but 2-6 may not be. This may
save substantial quantities of memory; for example tying 512 entries
together will save over 4kB.

You can create a multi-index entry by using [`XA_STATE_ORDER()`](xarray.md#c.XA_STATE_ORDER "XA_STATE_ORDER")
or [`xas_set_order()`](xarray.md#c.xas_set_order "xas_set_order") followed by a call to [`xas_store()`](xarray.md#c.xas_store "xas_store").
Calling [`xas_load()`](xarray.md#c.xas_load "xas_load") with a multi-index xa_state will walk the
xa_state to the right location in the tree, but the return value is not
meaningful, potentially being an internal entry or `NULL` even when there
is an entry stored within the range. Calling [`xas_find_conflict()`](xarray.md#c.xas_find_conflict "xas_find_conflict")
will return the first entry within the range or `NULL` if there are no
entries in the range. The [`xas_for_each_conflict()`](xarray.md#c.xas_for_each_conflict "xas_for_each_conflict") iterator will
iterate over every entry which overlaps the specified range.

If [`xas_load()`](xarray.md#c.xas_load "xas_load") encounters a multi-index entry, the xa_index
in the xa_state will not be changed. When iterating over an XArray
or calling [`xas_find()`](xarray.md#c.xas_find "xas_find"), if the initial index is in the middle
of a multi-index entry, it will not be altered. Subsequent calls
or iterations will move the index to the first index in the range.
Each entry will only be returned once, no matter how many indices it
occupies.

Using [`xas_next()`](xarray.md#c.xas_next "xas_next") or [`xas_prev()`](xarray.md#c.xas_prev "xas_prev") with a multi-index xa_state is not
supported. Using either of these functions on a multi-index entry will
reveal sibling entries; these should be skipped over by the caller.

Storing `NULL` into any index of a multi-index entry will set the
entry at every index to `NULL` and dissolve the tie. A multi-index
entry can be split into entries occupying smaller ranges by calling
[`xas_split_alloc()`](xarray.md#c.xas_split_alloc "xas_split_alloc") without the xa_lock held, followed by taking the lock
and calling [`xas_split()`](xarray.md#c.xas_split "xas_split").

## Functions and structures

void \*xa_mk_value(unsigned long v)
:   Create an XArray entry from an integer.

**Parameters**

`unsigned long v`
:   Value to store in XArray.

**Context**

Any context.

**Return**

An entry suitable for storing in the XArray.

unsigned long xa_to_value(const void \*entry)
:   Get value stored in an XArray entry.

**Parameters**

`const void *entry`
:   XArray entry.

**Context**

Any context.

**Return**

The value stored in the XArray entry.

bool xa_is_value(const void \*entry)
:   Determine if an entry is a value.

**Parameters**

`const void *entry`
:   XArray entry.

**Context**

Any context.

**Return**

True if the entry is a value, false if it is a pointer.

void \*xa_tag_pointer(void \*p, unsigned long tag)
:   Create an XArray entry for a tagged pointer.

**Parameters**

`void *p`
:   Plain pointer.

`unsigned long tag`
:   Tag value (0, 1 or 3).

**Description**

If the user of the XArray prefers, they can tag their pointers instead
of storing value entries. Three tags are available (0, 1 and 3).
These are distinct from the xa_mark_t as they are not replicated up
through the array and cannot be searched for.

**Context**

Any context.

**Return**

An XArray entry.

void \*xa_untag_pointer(void \*entry)
:   Turn an XArray entry into a plain pointer.

**Parameters**

`void *entry`
:   XArray entry.

**Description**

If you have stored a tagged pointer in the XArray, call this function
to get the untagged version of the pointer.

**Context**

Any context.

**Return**

A pointer.

unsigned int xa_pointer_tag(void \*entry)
:   Get the tag stored in an XArray entry.

**Parameters**

`void *entry`
:   XArray entry.

**Description**

If you have stored a tagged pointer in the XArray, call this function
to get the tag of that pointer.

**Context**

Any context.

**Return**

A tag.

bool xa_is_zero(const void \*entry)
:   Is the entry a zero entry?

**Parameters**

`const void *entry`
:   Entry retrieved from the XArray

**Description**

The normal API will return NULL as the contents of a slot containing
a zero entry. You can only see zero entries by using the advanced API.

**Return**

`true` if the entry is a zero entry.

bool xa_is_err(const void \*entry)
:   Report whether an XArray operation returned an error

**Parameters**

`const void *entry`
:   Result from calling an XArray function

**Description**

If an XArray operation cannot complete an operation, it will return
a special value indicating an error. This function tells you
whether an error occurred; [`xa_err()`](xarray.md#c.xa_err "xa_err") tells you which error occurred.

**Context**

Any context.

**Return**

`true` if the entry indicates an error.

int xa_err(void \*entry)
:   Turn an XArray result into an errno.

**Parameters**

`void *entry`
:   Result from calling an XArray function.

**Description**

If an XArray operation cannot complete an operation, it will return
a special pointer value which encodes an errno. This function extracts
the errno from the pointer value, or returns 0 if the pointer does not
represent an errno.

**Context**

Any context.

**Return**

A negative errno or 0.

struct xa_limit
:   Represents a range of IDs.

**Definition**:

```
struct xa_limit {
    u32 max;
    u32 min;
};
```

**Members**

`max`
:   The maximum ID to allocate (inclusive).

`min`
:   The lowest ID to allocate (inclusive).

**Description**

This structure is used either directly or via the XA_LIMIT() macro
to communicate the range of IDs that are valid for allocation.
Three common ranges are predefined for you:
\* xa_limit_32b - [0 - UINT_MAX]
\* xa_limit_31b - [0 - INT_MAX]
\* xa_limit_16b - [0 - USHRT_MAX]

struct xarray
:   The anchor of the XArray.

**Definition**:

```
struct xarray {
    spinlock_t xa_lock;
};
```

**Members**

`xa_lock`
:   Lock that protects the contents of the XArray.

**Description**

To use the xarray, define it statically or embed it in your data structure.
It is a very small data structure, so it does not usually make sense to
allocate it separately and keep a pointer to it in your data structure.

You may use the xa_lock to protect your own data structures as well.

DEFINE_XARRAY_FLAGS

`DEFINE_XARRAY_FLAGS (name, flags)`

> Define an XArray with custom flags.

**Parameters**

`name`
:   A string that names your XArray.

`flags`
:   XA_FLAG values.

**Description**

This is intended for file scope definitions of XArrays. It declares
and initialises an empty XArray with the chosen name and flags. It is
equivalent to calling [`xa_init_flags()`](xarray.md#c.xa_init_flags "xa_init_flags") on the array, but it does the
initialisation at compiletime instead of runtime.

DEFINE_XARRAY

`DEFINE_XARRAY (name)`

> Define an XArray.

**Parameters**

`name`
:   A string that names your XArray.

**Description**

This is intended for file scope definitions of XArrays. It declares
and initialises an empty XArray with the chosen name. It is equivalent
to calling [`xa_init()`](xarray.md#c.xa_init "xa_init") on the array, but it does the initialisation at
compiletime instead of runtime.

DEFINE_XARRAY_ALLOC

`DEFINE_XARRAY_ALLOC (name)`

> Define an XArray which allocates IDs starting at 0.

**Parameters**

`name`
:   A string that names your XArray.

**Description**

This is intended for file scope definitions of allocating XArrays.
See also [`DEFINE_XARRAY()`](xarray.md#c.DEFINE_XARRAY "DEFINE_XARRAY").

DEFINE_XARRAY_ALLOC1

`DEFINE_XARRAY_ALLOC1 (name)`

> Define an XArray which allocates IDs starting at 1.

**Parameters**

`name`
:   A string that names your XArray.

**Description**

This is intended for file scope definitions of allocating XArrays.
See also [`DEFINE_XARRAY()`](xarray.md#c.DEFINE_XARRAY "DEFINE_XARRAY").

void xa_init_flags(struct [xarray](xarray.md#c.xarray "xarray") \*xa, gfp_t flags)
:   Initialise an empty XArray with flags.

**Parameters**

`struct xarray *xa`
:   XArray.

`gfp_t flags`
:   XA_FLAG values.

**Description**

If you need to initialise an XArray with special flags (eg you need
to take the lock from interrupt context), use this function instead
of [`xa_init()`](xarray.md#c.xa_init "xa_init").

**Context**

Any context.

void xa_init(struct [xarray](xarray.md#c.xarray "xarray") \*xa)
:   Initialise an empty XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

**Description**

An empty XArray is full of NULL entries.

**Context**

Any context.

bool xa_empty(const struct [xarray](xarray.md#c.xarray "xarray") \*xa)
:   Determine if an array has any present entries.

**Parameters**

`const struct xarray *xa`
:   XArray.

**Context**

Any context.

**Return**

`true` if the array contains only NULL pointers.

bool xa_marked(const struct [xarray](xarray.md#c.xarray "xarray") \*xa, xa_mark_t mark)
:   Inquire whether any entry in this array has a mark set

**Parameters**

`const struct xarray *xa`
:   Array

`xa_mark_t mark`
:   Mark value

**Context**

Any context.

**Return**

`true` if any entry has this mark set.

xa_for_each_range

`xa_for_each_range (xa, index, entry, start, last)`

> Iterate over a portion of an XArray.

**Parameters**

`xa`
:   XArray.

`index`
:   Index of **entry**.

`entry`
:   Entry retrieved from array.

`start`
:   First index to retrieve from array.

`last`
:   Last index to retrieve from array.

**Description**

During the iteration, **entry** will have the value of the entry stored
in **xa** at **index**. You may modify **index** during the iteration if you
want to skip or reprocess indices. It is safe to modify the array
during the iteration. At the end of the iteration, **entry** will be set
to NULL and **index** will have a value less than or equal to max.

[`xa_for_each_range()`](xarray.md#c.xa_for_each_range "xa_for_each_range") is O(n.log(n)) while [`xas_for_each()`](xarray.md#c.xas_for_each "xas_for_each") is O(n). You have
to handle your own locking with [`xas_for_each()`](xarray.md#c.xas_for_each "xas_for_each"), and if you have to unlock
after each iteration, it will also end up being O(n.log(n)).
[`xa_for_each_range()`](xarray.md#c.xa_for_each_range "xa_for_each_range") will spin if it hits a retry entry; if you intend to
see retry entries, you should use the [`xas_for_each()`](xarray.md#c.xas_for_each "xas_for_each") iterator instead.
The [`xas_for_each()`](xarray.md#c.xas_for_each "xas_for_each") iterator will expand into more inline code than
[`xa_for_each_range()`](xarray.md#c.xa_for_each_range "xa_for_each_range").

**Context**

Any context. Takes and releases the RCU lock.

xa_for_each_start

`xa_for_each_start (xa, index, entry, start)`

> Iterate over a portion of an XArray.

**Parameters**

`xa`
:   XArray.

`index`
:   Index of **entry**.

`entry`
:   Entry retrieved from array.

`start`
:   First index to retrieve from array.

**Description**

During the iteration, **entry** will have the value of the entry stored
in **xa** at **index**. You may modify **index** during the iteration if you
want to skip or reprocess indices. It is safe to modify the array
during the iteration. At the end of the iteration, **entry** will be set
to NULL and **index** will have a value less than or equal to max.

[`xa_for_each_start()`](xarray.md#c.xa_for_each_start "xa_for_each_start") is O(n.log(n)) while [`xas_for_each()`](xarray.md#c.xas_for_each "xas_for_each") is O(n). You have
to handle your own locking with [`xas_for_each()`](xarray.md#c.xas_for_each "xas_for_each"), and if you have to unlock
after each iteration, it will also end up being O(n.log(n)).
[`xa_for_each_start()`](xarray.md#c.xa_for_each_start "xa_for_each_start") will spin if it hits a retry entry; if you intend to
see retry entries, you should use the [`xas_for_each()`](xarray.md#c.xas_for_each "xas_for_each") iterator instead.
The [`xas_for_each()`](xarray.md#c.xas_for_each "xas_for_each") iterator will expand into more inline code than
[`xa_for_each_start()`](xarray.md#c.xa_for_each_start "xa_for_each_start").

**Context**

Any context. Takes and releases the RCU lock.

xa_for_each

`xa_for_each (xa, index, entry)`

> Iterate over present entries in an XArray.

**Parameters**

`xa`
:   XArray.

`index`
:   Index of **entry**.

`entry`
:   Entry retrieved from array.

**Description**

During the iteration, **entry** will have the value of the entry stored
in **xa** at **index**. You may modify **index** during the iteration if you want
to skip or reprocess indices. It is safe to modify the array during the
iteration. At the end of the iteration, **entry** will be set to NULL and
**index** will have a value less than or equal to max.

[`xa_for_each()`](xarray.md#c.xa_for_each "xa_for_each") is O(n.log(n)) while [`xas_for_each()`](xarray.md#c.xas_for_each "xas_for_each") is O(n). You have
to handle your own locking with [`xas_for_each()`](xarray.md#c.xas_for_each "xas_for_each"), and if you have to unlock
after each iteration, it will also end up being O(n.log(n)). [`xa_for_each()`](xarray.md#c.xa_for_each "xa_for_each")
will spin if it hits a retry entry; if you intend to see retry entries,
you should use the [`xas_for_each()`](xarray.md#c.xas_for_each "xas_for_each") iterator instead. The [`xas_for_each()`](xarray.md#c.xas_for_each "xas_for_each")
iterator will expand into more inline code than [`xa_for_each()`](xarray.md#c.xa_for_each "xa_for_each").

**Context**

Any context. Takes and releases the RCU lock.

xa_for_each_marked

`xa_for_each_marked (xa, index, entry, filter)`

> Iterate over marked entries in an XArray.

**Parameters**

`xa`
:   XArray.

`index`
:   Index of **entry**.

`entry`
:   Entry retrieved from array.

`filter`
:   Selection criterion.

**Description**

During the iteration, **entry** will have the value of the entry stored
in **xa** at **index**. The iteration will skip all entries in the array
which do not match **filter**. You may modify **index** during the iteration
if you want to skip or reprocess indices. It is safe to modify the array
during the iteration. At the end of the iteration, **entry** will be set to
NULL and **index** will have a value less than or equal to max.

[`xa_for_each_marked()`](xarray.md#c.xa_for_each_marked "xa_for_each_marked") is O(n.log(n)) while [`xas_for_each_marked()`](xarray.md#c.xas_for_each_marked "xas_for_each_marked") is O(n).
You have to handle your own locking with [`xas_for_each()`](xarray.md#c.xas_for_each "xas_for_each"), and if you have
to unlock after each iteration, it will also end up being O(n.log(n)).
[`xa_for_each_marked()`](xarray.md#c.xa_for_each_marked "xa_for_each_marked") will spin if it hits a retry entry; if you intend to
see retry entries, you should use the [`xas_for_each_marked()`](xarray.md#c.xas_for_each_marked "xas_for_each_marked") iterator
instead. The [`xas_for_each_marked()`](xarray.md#c.xas_for_each_marked "xas_for_each_marked") iterator will expand into more inline
code than [`xa_for_each_marked()`](xarray.md#c.xa_for_each_marked "xa_for_each_marked").

**Context**

Any context. Takes and releases the RCU lock.

void \*xa_store_bh(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index, void \*entry, gfp_t gfp)
:   Store this entry in the XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index into array.

`void *entry`
:   New entry.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

This function is like calling [`xa_store()`](xarray.md#c.xa_store "xa_store") except it disables softirqs
while holding the array lock.

**Context**

Any context. Takes and releases the xa_lock while
disabling softirqs.

**Return**

The old entry at this index or [`xa_err()`](xarray.md#c.xa_err "xa_err") if an error happened.

void \*xa_store_irq(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index, void \*entry, gfp_t gfp)
:   Store this entry in the XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index into array.

`void *entry`
:   New entry.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

This function is like calling [`xa_store()`](xarray.md#c.xa_store "xa_store") except it disables interrupts
while holding the array lock.

**Context**

Process context. Takes and releases the xa_lock while
disabling interrupts.

**Return**

The old entry at this index or [`xa_err()`](xarray.md#c.xa_err "xa_err") if an error happened.

void \*xa_erase_bh(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index)
:   Erase this entry from the XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index of entry.

**Description**

After this function returns, loading from **index** will return `NULL`.
If the index is part of a multi-index entry, all indices will be erased
and none of the entries will be part of a multi-index entry.

**Context**

Any context. Takes and releases the xa_lock while
disabling softirqs.

**Return**

The entry which used to be at this index.

void \*xa_erase_irq(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index)
:   Erase this entry from the XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index of entry.

**Description**

After this function returns, loading from **index** will return `NULL`.
If the index is part of a multi-index entry, all indices will be erased
and none of the entries will be part of a multi-index entry.

**Context**

Process context. Takes and releases the xa_lock while
disabling interrupts.

**Return**

The entry which used to be at this index.

void \*xa_cmpxchg(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index, void \*old, void \*entry, gfp_t gfp)
:   Conditionally replace an entry in the XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index into array.

`void *old`
:   Old value to test against.

`void *entry`
:   New value to place in array.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

If the entry at **index** is the same as **old**, replace it with **entry**.
If the return value is equal to **old**, then the exchange was successful.

**Context**

Any context. Takes and releases the xa_lock. May sleep
if the **gfp** flags permit.

**Return**

The old value at this index or [`xa_err()`](xarray.md#c.xa_err "xa_err") if an error happened.

void \*xa_cmpxchg_bh(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index, void \*old, void \*entry, gfp_t gfp)
:   Conditionally replace an entry in the XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index into array.

`void *old`
:   Old value to test against.

`void *entry`
:   New value to place in array.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

This function is like calling [`xa_cmpxchg()`](xarray.md#c.xa_cmpxchg "xa_cmpxchg") except it disables softirqs
while holding the array lock.

**Context**

Any context. Takes and releases the xa_lock while
disabling softirqs. May sleep if the **gfp** flags permit.

**Return**

The old value at this index or [`xa_err()`](xarray.md#c.xa_err "xa_err") if an error happened.

void \*xa_cmpxchg_irq(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index, void \*old, void \*entry, gfp_t gfp)
:   Conditionally replace an entry in the XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index into array.

`void *old`
:   Old value to test against.

`void *entry`
:   New value to place in array.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

This function is like calling [`xa_cmpxchg()`](xarray.md#c.xa_cmpxchg "xa_cmpxchg") except it disables interrupts
while holding the array lock.

**Context**

Process context. Takes and releases the xa_lock while
disabling interrupts. May sleep if the **gfp** flags permit.

**Return**

The old value at this index or [`xa_err()`](xarray.md#c.xa_err "xa_err") if an error happened.

int xa_insert(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index, void \*entry, gfp_t gfp)
:   Store this entry in the XArray unless another entry is already present.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index into array.

`void *entry`
:   New entry.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

Inserting a NULL entry will store a reserved entry (like [`xa_reserve()`](xarray.md#c.xa_reserve "xa_reserve"))
if no entry is present. Inserting will fail if a reserved entry is
present, even though loading from this index will return NULL.

**Context**

Any context. Takes and releases the xa_lock. May sleep if
the **gfp** flags permit.

**Return**

0 if the store succeeded. -EBUSY if another entry was present.
-ENOMEM if memory could not be allocated.

int xa_insert_bh(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index, void \*entry, gfp_t gfp)
:   Store this entry in the XArray unless another entry is already present.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index into array.

`void *entry`
:   New entry.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

Inserting a NULL entry will store a reserved entry (like [`xa_reserve()`](xarray.md#c.xa_reserve "xa_reserve"))
if no entry is present. Inserting will fail if a reserved entry is
present, even though loading from this index will return NULL.

**Context**

Any context. Takes and releases the xa_lock while
disabling softirqs. May sleep if the **gfp** flags permit.

**Return**

0 if the store succeeded. -EBUSY if another entry was present.
-ENOMEM if memory could not be allocated.

int xa_insert_irq(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index, void \*entry, gfp_t gfp)
:   Store this entry in the XArray unless another entry is already present.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index into array.

`void *entry`
:   New entry.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

Inserting a NULL entry will store a reserved entry (like [`xa_reserve()`](xarray.md#c.xa_reserve "xa_reserve"))
if no entry is present. Inserting will fail if a reserved entry is
present, even though loading from this index will return NULL.

**Context**

Process context. Takes and releases the xa_lock while
disabling interrupts. May sleep if the **gfp** flags permit.

**Return**

0 if the store succeeded. -EBUSY if another entry was present.
-ENOMEM if memory could not be allocated.

int xa_alloc(struct [xarray](xarray.md#c.xarray "xarray") \*xa, u32 \*id, void \*entry, struct [xa_limit](xarray.md#c.xa_limit "xa_limit") limit, gfp_t gfp)
:   Find somewhere to store this entry in the XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`u32 *id`
:   Pointer to ID.

`void *entry`
:   New entry.

`struct xa_limit limit`
:   Range of ID to allocate.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

Finds an empty entry in **xa** between **limit.min** and **limit.max**,
stores the index into the **id** pointer, then stores the entry at
that index. A concurrent lookup will not see an uninitialised **id**.

Must only be operated on an xarray initialized with flag XA_FLAGS_ALLOC set
in [`xa_init_flags()`](xarray.md#c.xa_init_flags "xa_init_flags").

**Context**

Any context. Takes and releases the xa_lock. May sleep if
the **gfp** flags permit.

**Return**

0 on success, -ENOMEM if memory could not be allocated or
-EBUSY if there are no free entries in **limit**.

int xa_alloc_bh(struct [xarray](xarray.md#c.xarray "xarray") \*xa, u32 \*id, void \*entry, struct [xa_limit](xarray.md#c.xa_limit "xa_limit") limit, gfp_t gfp)
:   Find somewhere to store this entry in the XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`u32 *id`
:   Pointer to ID.

`void *entry`
:   New entry.

`struct xa_limit limit`
:   Range of ID to allocate.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

Finds an empty entry in **xa** between **limit.min** and **limit.max**,
stores the index into the **id** pointer, then stores the entry at
that index. A concurrent lookup will not see an uninitialised **id**.

Must only be operated on an xarray initialized with flag XA_FLAGS_ALLOC set
in [`xa_init_flags()`](xarray.md#c.xa_init_flags "xa_init_flags").

**Context**

Any context. Takes and releases the xa_lock while
disabling softirqs. May sleep if the **gfp** flags permit.

**Return**

0 on success, -ENOMEM if memory could not be allocated or
-EBUSY if there are no free entries in **limit**.

int xa_alloc_irq(struct [xarray](xarray.md#c.xarray "xarray") \*xa, u32 \*id, void \*entry, struct [xa_limit](xarray.md#c.xa_limit "xa_limit") limit, gfp_t gfp)
:   Find somewhere to store this entry in the XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`u32 *id`
:   Pointer to ID.

`void *entry`
:   New entry.

`struct xa_limit limit`
:   Range of ID to allocate.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

Finds an empty entry in **xa** between **limit.min** and **limit.max**,
stores the index into the **id** pointer, then stores the entry at
that index. A concurrent lookup will not see an uninitialised **id**.

Must only be operated on an xarray initialized with flag XA_FLAGS_ALLOC set
in [`xa_init_flags()`](xarray.md#c.xa_init_flags "xa_init_flags").

**Context**

Process context. Takes and releases the xa_lock while
disabling interrupts. May sleep if the **gfp** flags permit.

**Return**

0 on success, -ENOMEM if memory could not be allocated or
-EBUSY if there are no free entries in **limit**.

int xa_alloc_cyclic(struct [xarray](xarray.md#c.xarray "xarray") \*xa, u32 \*id, void \*entry, struct [xa_limit](xarray.md#c.xa_limit "xa_limit") limit, u32 \*next, gfp_t gfp)
:   Find somewhere to store this entry in the XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`u32 *id`
:   Pointer to ID.

`void *entry`
:   New entry.

`struct xa_limit limit`
:   Range of allocated ID.

`u32 *next`
:   Pointer to next ID to allocate.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

Finds an empty entry in **xa** between **limit.min** and **limit.max**,
stores the index into the **id** pointer, then stores the entry at
that index. A concurrent lookup will not see an uninitialised **id**.
The search for an empty entry will start at **next** and will wrap
around if necessary.

Must only be operated on an xarray initialized with flag XA_FLAGS_ALLOC set
in [`xa_init_flags()`](xarray.md#c.xa_init_flags "xa_init_flags").

**Context**

Any context. Takes and releases the xa_lock. May sleep if
the **gfp** flags permit.

**Return**

0 if the allocation succeeded without wrapping. 1 if the
allocation succeeded after wrapping, -ENOMEM if memory could not be
allocated or -EBUSY if there are no free entries in **limit**.

int xa_alloc_cyclic_bh(struct [xarray](xarray.md#c.xarray "xarray") \*xa, u32 \*id, void \*entry, struct [xa_limit](xarray.md#c.xa_limit "xa_limit") limit, u32 \*next, gfp_t gfp)
:   Find somewhere to store this entry in the XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`u32 *id`
:   Pointer to ID.

`void *entry`
:   New entry.

`struct xa_limit limit`
:   Range of allocated ID.

`u32 *next`
:   Pointer to next ID to allocate.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

Finds an empty entry in **xa** between **limit.min** and **limit.max**,
stores the index into the **id** pointer, then stores the entry at
that index. A concurrent lookup will not see an uninitialised **id**.
The search for an empty entry will start at **next** and will wrap
around if necessary.

Must only be operated on an xarray initialized with flag XA_FLAGS_ALLOC set
in [`xa_init_flags()`](xarray.md#c.xa_init_flags "xa_init_flags").

**Context**

Any context. Takes and releases the xa_lock while
disabling softirqs. May sleep if the **gfp** flags permit.

**Return**

0 if the allocation succeeded without wrapping. 1 if the
allocation succeeded after wrapping, -ENOMEM if memory could not be
allocated or -EBUSY if there are no free entries in **limit**.

int xa_alloc_cyclic_irq(struct [xarray](xarray.md#c.xarray "xarray") \*xa, u32 \*id, void \*entry, struct [xa_limit](xarray.md#c.xa_limit "xa_limit") limit, u32 \*next, gfp_t gfp)
:   Find somewhere to store this entry in the XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`u32 *id`
:   Pointer to ID.

`void *entry`
:   New entry.

`struct xa_limit limit`
:   Range of allocated ID.

`u32 *next`
:   Pointer to next ID to allocate.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

Finds an empty entry in **xa** between **limit.min** and **limit.max**,
stores the index into the **id** pointer, then stores the entry at
that index. A concurrent lookup will not see an uninitialised **id**.
The search for an empty entry will start at **next** and will wrap
around if necessary.

Must only be operated on an xarray initialized with flag XA_FLAGS_ALLOC set
in [`xa_init_flags()`](xarray.md#c.xa_init_flags "xa_init_flags").

**Context**

Process context. Takes and releases the xa_lock while
disabling interrupts. May sleep if the **gfp** flags permit.

**Return**

0 if the allocation succeeded without wrapping. 1 if the
allocation succeeded after wrapping, -ENOMEM if memory could not be
allocated or -EBUSY if there are no free entries in **limit**.

int xa_reserve(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index, gfp_t gfp)
:   Reserve this index in the XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index into array.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

Ensures there is somewhere to store an entry at **index** in the array.
If there is already something stored at **index**, this function does
nothing. If there was nothing there, the entry is marked as reserved.
Loading from a reserved entry returns a `NULL` pointer.

If you do not use the entry that you have reserved, call [`xa_release()`](xarray.md#c.xa_release "xa_release")
or [`xa_erase()`](xarray.md#c.xa_erase "xa_erase") to free any unnecessary memory.

**Context**

Any context. Takes and releases the xa_lock.
May sleep if the **gfp** flags permit.

**Return**

0 if the reservation succeeded or -ENOMEM if it failed.

int xa_reserve_bh(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index, gfp_t gfp)
:   Reserve this index in the XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index into array.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

A softirq-disabling version of [`xa_reserve()`](xarray.md#c.xa_reserve "xa_reserve").

**Context**

Any context. Takes and releases the xa_lock while
disabling softirqs.

**Return**

0 if the reservation succeeded or -ENOMEM if it failed.

int xa_reserve_irq(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index, gfp_t gfp)
:   Reserve this index in the XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index into array.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

An interrupt-disabling version of [`xa_reserve()`](xarray.md#c.xa_reserve "xa_reserve").

**Context**

Process context. Takes and releases the xa_lock while
disabling interrupts.

**Return**

0 if the reservation succeeded or -ENOMEM if it failed.

void xa_release(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index)
:   Release a reserved entry.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index of entry.

**Description**

After calling [`xa_reserve()`](xarray.md#c.xa_reserve "xa_reserve"), you can call this function to release the
reservation. If the entry at **index** has been stored to, this function
will do nothing.

bool xa_is_sibling(const void \*entry)
:   Is the entry a sibling entry?

**Parameters**

`const void *entry`
:   Entry retrieved from the XArray

**Return**

`true` if the entry is a sibling entry.

bool xa_is_retry(const void \*entry)
:   Is the entry a retry entry?

**Parameters**

`const void *entry`
:   Entry retrieved from the XArray

**Return**

`true` if the entry is a retry entry.

bool xa_is_advanced(const void \*entry)
:   Is the entry only permitted for the advanced API?

**Parameters**

`const void *entry`
:   Entry to be stored in the XArray.

**Return**

`true` if the entry cannot be stored by the normal API.

xa_update_node_t
:   **Typedef**: A callback function from the XArray.

**Syntax**

> `void xa_update_node_t (struct xa_node *node)`

**Parameters**

`struct xa_node *node`
:   The node which is being processed

**Description**

This function is called every time the XArray updates the count of
present and value entries in a node. It allows advanced users to
maintain the private_list in the node.

**Context**

The xa_lock is held and interrupts may be disabled.
Implementations should not drop the xa_lock, nor re-enable
interrupts.

XA_STATE

`XA_STATE (name, array, index)`

> Declare an XArray operation state.

**Parameters**

`name`
:   Name of this operation state (usually xas).

`array`
:   Array to operate on.

`index`
:   Initial index of interest.

**Description**

Declare and initialise an xa_state on the stack.

XA_STATE_ORDER

`XA_STATE_ORDER (name, array, index, order)`

> Declare an XArray operation state.

**Parameters**

`name`
:   Name of this operation state (usually xas).

`array`
:   Array to operate on.

`index`
:   Initial index of interest.

`order`
:   Order of entry.

**Description**

Declare and initialise an xa_state on the stack. This variant of
[`XA_STATE()`](xarray.md#c.XA_STATE "XA_STATE") allows you to specify the 'order' of the element you
want to operate on.`

int xas_error(const struct xa_state \*xas)
:   Return an errno stored in the xa_state.

**Parameters**

`const struct xa_state *xas`
:   XArray operation state.

**Return**

0 if no error has been noted. A negative errno if one has.

void xas_set_err(struct xa_state \*xas, long err)
:   Note an error in the xa_state.

**Parameters**

`struct xa_state *xas`
:   XArray operation state.

`long err`
:   Negative error number.

**Description**

Only call this function with a negative **err**; zero or positive errors
will probably not behave the way you think they should. If you want
to clear the error from an xa_state, use [`xas_reset()`](xarray.md#c.xas_reset "xas_reset").

bool xas_invalid(const struct xa_state \*xas)
:   Is the xas in a retry or error state?

**Parameters**

`const struct xa_state *xas`
:   XArray operation state.

**Return**

`true` if the xas cannot be used for operations.

bool xas_valid(const struct xa_state \*xas)
:   Is the xas a valid cursor into the array?

**Parameters**

`const struct xa_state *xas`
:   XArray operation state.

**Return**

`true` if the xas can be used for operations.

bool xas_is_node(const struct xa_state \*xas)
:   Does the xas point to a node?

**Parameters**

`const struct xa_state *xas`
:   XArray operation state.

**Return**

`true` if the xas currently references a node.

void xas_reset(struct xa_state \*xas)
:   Reset an XArray operation state.

**Parameters**

`struct xa_state *xas`
:   XArray operation state.

**Description**

Resets the error or walk state of the **xas** so future walks of the
array will start from the root. Use this if you have dropped the
xarray lock and want to reuse the xa_state.

**Context**

Any context.

bool xas_retry(struct xa_state \*xas, const void \*entry)
:   Retry the operation if appropriate.

**Parameters**

`struct xa_state *xas`
:   XArray operation state.

`const void *entry`
:   Entry from xarray.

**Description**

The advanced functions may sometimes return an internal entry, such as
a retry entry or a zero entry. This function sets up the **xas** to restart
the walk from the head of the array if needed.

**Context**

Any context.

**Return**

true if the operation needs to be retried.

void \*xas_reload(struct xa_state \*xas)
:   Refetch an entry from the xarray.

**Parameters**

`struct xa_state *xas`
:   XArray operation state.

**Description**

Use this function to check that a previously loaded entry still has
the same value. This is useful for the lockless pagecache lookup where
we walk the array with only the RCU lock to protect us, lock the page,
then check that the page hasn't moved since we looked it up.

The caller guarantees that **xas** is still valid. If it may be in an
error or restart state, call [`xas_load()`](xarray.md#c.xas_load "xas_load") instead.

**Return**

The entry at this location in the xarray.

void xas_set(struct xa_state \*xas, unsigned long index)
:   Set up XArray operation state for a different index.

**Parameters**

`struct xa_state *xas`
:   XArray operation state.

`unsigned long index`
:   New index into the XArray.

**Description**

Move the operation state to refer to a different index. This will
have the effect of starting a walk from the top; see [`xas_next()`](xarray.md#c.xas_next "xas_next")
to move to an adjacent index.

void xas_advance(struct xa_state \*xas, unsigned long index)
:   Skip over sibling entries.

**Parameters**

`struct xa_state *xas`
:   XArray operation state.

`unsigned long index`
:   Index of last sibling entry.

**Description**

Move the operation state to refer to the last sibling entry.
This is useful for loops that normally want to see sibling
entries but sometimes want to skip them. Use [`xas_set()`](xarray.md#c.xas_set "xas_set") if you
want to move to an index which is not part of this entry.

void xas_set_order(struct xa_state \*xas, unsigned long index, unsigned int order)
:   Set up XArray operation state for a multislot entry.

**Parameters**

`struct xa_state *xas`
:   XArray operation state.

`unsigned long index`
:   Target of the operation.

`unsigned int order`
:   Entry occupies 2^\*\*order\*\* indices.

void xas_set_update(struct xa_state \*xas, [xa_update_node_t](xarray.md#c.xa_update_node_t "xa_update_node_t") update)
:   Set up XArray operation state for a callback.

**Parameters**

`struct xa_state *xas`
:   XArray operation state.

`xa_update_node_t update`
:   Function to call when updating a node.

**Description**

The XArray can notify a caller after it has updated an xa_node.
This is advanced functionality and is only needed by the page
cache and swap cache.

void \*xas_next_entry(struct xa_state \*xas, unsigned long max)
:   Advance iterator to next present entry.

**Parameters**

`struct xa_state *xas`
:   XArray operation state.

`unsigned long max`
:   Highest index to return.

**Description**

[`xas_next_entry()`](xarray.md#c.xas_next_entry "xas_next_entry") is an inline function to optimise xarray traversal for
speed. It is equivalent to calling [`xas_find()`](xarray.md#c.xas_find "xas_find"), and will call [`xas_find()`](xarray.md#c.xas_find "xas_find")
for all the hard cases.

**Return**

The next present entry after the one currently referred to by **xas**.

void \*xas_next_marked(struct xa_state \*xas, unsigned long max, xa_mark_t mark)
:   Advance iterator to next marked entry.

**Parameters**

`struct xa_state *xas`
:   XArray operation state.

`unsigned long max`
:   Highest index to return.

`xa_mark_t mark`
:   Mark to search for.

**Description**

[`xas_next_marked()`](xarray.md#c.xas_next_marked "xas_next_marked") is an inline function to optimise xarray traversal for
speed. It is equivalent to calling [`xas_find_marked()`](xarray.md#c.xas_find_marked "xas_find_marked"), and will call
[`xas_find_marked()`](xarray.md#c.xas_find_marked "xas_find_marked") for all the hard cases.

**Return**

The next marked entry after the one currently referred to by **xas**.

xas_for_each

`xas_for_each (xas, entry, max)`

> Iterate over a range of an XArray.

**Parameters**

`xas`
:   XArray operation state.

`entry`
:   Entry retrieved from the array.

`max`
:   Maximum index to retrieve from array.

**Description**

The loop body will be executed for each entry present in the xarray
between the current xas position and **max**. **entry** will be set to
the entry retrieved from the xarray. It is safe to delete entries
from the array in the loop body. You should hold either the RCU lock
or the xa_lock while iterating. If you need to drop the lock, call
[`xas_pause()`](xarray.md#c.xas_pause "xas_pause") first.

xas_for_each_marked

`xas_for_each_marked (xas, entry, max, mark)`

> Iterate over a range of an XArray.

**Parameters**

`xas`
:   XArray operation state.

`entry`
:   Entry retrieved from the array.

`max`
:   Maximum index to retrieve from array.

`mark`
:   Mark to search for.

**Description**

The loop body will be executed for each marked entry in the xarray
between the current xas position and **max**. **entry** will be set to
the entry retrieved from the xarray. It is safe to delete entries
from the array in the loop body. You should hold either the RCU lock
or the xa_lock while iterating. If you need to drop the lock, call
[`xas_pause()`](xarray.md#c.xas_pause "xas_pause") first.

xas_for_each_conflict

`xas_for_each_conflict (xas, entry)`

> Iterate over a range of an XArray.

**Parameters**

`xas`
:   XArray operation state.

`entry`
:   Entry retrieved from the array.

**Description**

The loop body will be executed for each entry in the XArray that
lies within the range specified by **xas**. If the loop terminates
normally, **entry** will be `NULL`. The user may break out of the loop,
which will leave **entry** set to the conflicting entry. The caller
may also call xa_set_err() to exit the loop while setting an error
to record the reason.

void \*xas_prev(struct xa_state \*xas)
:   Move iterator to previous index.

**Parameters**

`struct xa_state *xas`
:   XArray operation state.

**Description**

If the **xas** was in an error state, it will remain in an error state
and this function will return `NULL`. If the **xas** has never been walked,
it will have the effect of calling [`xas_load()`](xarray.md#c.xas_load "xas_load"). Otherwise one will be
subtracted from the index and the state will be walked to the correct
location in the array for the next operation.

If the iterator was referencing index 0, this function wraps
around to `ULONG_MAX`.

**Return**

The entry at the new index. This may be `NULL` or an internal
entry.

void \*xas_next(struct xa_state \*xas)
:   Move state to next index.

**Parameters**

`struct xa_state *xas`
:   XArray operation state.

**Description**

If the **xas** was in an error state, it will remain in an error state
and this function will return `NULL`. If the **xas** has never been walked,
it will have the effect of calling [`xas_load()`](xarray.md#c.xas_load "xas_load"). Otherwise one will be
added to the index and the state will be walked to the correct
location in the array for the next operation.

If the iterator was referencing index `ULONG_MAX`, this function wraps
around to 0.

**Return**

The entry at the new index. This may be `NULL` or an internal
entry.

void \*xas_load(struct xa_state \*xas)
:   Load an entry from the XArray (advanced).

**Parameters**

`struct xa_state *xas`
:   XArray operation state.

**Description**

Usually walks the **xas** to the appropriate state to load the entry
stored at xa_index. However, it will do nothing and return `NULL` if
**xas** is in an error state. [`xas_load()`](xarray.md#c.xas_load "xas_load") will never expand the tree.

If the xa_state is set up to operate on a multi-index entry, [`xas_load()`](xarray.md#c.xas_load "xas_load")
may return `NULL` or an internal entry, even if there are entries
present within the range specified by **xas**.

**Context**

Any context. The caller should hold the xa_lock or the RCU lock.

**Return**

Usually an entry in the XArray, but see description for exceptions.

bool xas_nomem(struct xa_state \*xas, gfp_t gfp)
:   Allocate memory if needed.

**Parameters**

`struct xa_state *xas`
:   XArray operation state.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

If we need to add new nodes to the XArray, we try to allocate memory
with GFP_NOWAIT while holding the lock, which will usually succeed.
If it fails, **xas** is flagged as needing memory to continue. The caller
should drop the lock and call [`xas_nomem()`](xarray.md#c.xas_nomem "xas_nomem"). If [`xas_nomem()`](xarray.md#c.xas_nomem "xas_nomem") succeeds,
the caller should retry the operation.

Forward progress is guaranteed as one node is allocated here and
stored in the xa_state where it will be found by xas_alloc(). More
nodes will likely be found in the slab allocator, but we do not tie
them up here.

**Return**

true if memory was needed, and was successfully allocated.

void xas_free_nodes(struct xa_state \*xas, struct xa_node \*top)
:   Free this node and all nodes that it references

**Parameters**

`struct xa_state *xas`
:   Array operation state.

`struct xa_node *top`
:   Node to free

**Description**

This node has been removed from the tree. We must now free it and all
of its subnodes. There may be RCU walkers with references into the tree,
so we must replace all entries with retry markers.

void xas_create_range(struct xa_state \*xas)
:   Ensure that stores to this range will succeed

**Parameters**

`struct xa_state *xas`
:   XArray operation state.

**Description**

Creates all of the slots in the range covered by **xas**. Sets **xas** to
create single-index entries and positions it at the beginning of the
range. This is for the benefit of users which have not yet been
converted to use multi-index entries.

void \*xas_store(struct xa_state \*xas, void \*entry)
:   Store this entry in the XArray.

**Parameters**

`struct xa_state *xas`
:   XArray operation state.

`void *entry`
:   New entry.

**Description**

If **xas** is operating on a multi-index entry, the entry returned by this
function is essentially meaningless (it may be an internal entry or it
may be `NULL`, even if there are non-NULL entries at some of the indices
covered by the range). This is not a problem for any current users,
and can be changed if needed.

**Return**

The old entry at this index.

bool xas_get_mark(const struct xa_state \*xas, xa_mark_t mark)
:   Returns the state of this mark.

**Parameters**

`const struct xa_state *xas`
:   XArray operation state.

`xa_mark_t mark`
:   Mark number.

**Return**

true if the mark is set, false if the mark is clear or **xas**
is in an error state.

void xas_set_mark(const struct xa_state \*xas, xa_mark_t mark)
:   Sets the mark on this entry and its parents.

**Parameters**

`const struct xa_state *xas`
:   XArray operation state.

`xa_mark_t mark`
:   Mark number.

**Description**

Sets the specified mark on this entry, and walks up the tree setting it
on all the ancestor entries. Does nothing if **xas** has not been walked to
an entry, or is in an error state.

void xas_clear_mark(const struct xa_state \*xas, xa_mark_t mark)
:   Clears the mark on this entry and its parents.

**Parameters**

`const struct xa_state *xas`
:   XArray operation state.

`xa_mark_t mark`
:   Mark number.

**Description**

Clears the specified mark on this entry, and walks back to the head
attempting to clear it on all the ancestor entries. Does nothing if
**xas** has not been walked to an entry, or is in an error state.

void xas_init_marks(const struct xa_state \*xas)
:   Initialise all marks for the entry

**Parameters**

`const struct xa_state *xas`
:   Array operations state.

**Description**

Initialise all marks for the entry specified by **xas**. If we're tracking
free entries with a mark, we need to set it on all entries. All other
marks are cleared.

This implementation is not as efficient as it could be; we may walk
up the tree multiple times.

void xas_split_alloc(struct xa_state \*xas, void \*entry, unsigned int order, gfp_t gfp)
:   Allocate memory for splitting an entry.

**Parameters**

`struct xa_state *xas`
:   XArray operation state.

`void *entry`
:   New entry which will be stored in the array.

`unsigned int order`
:   Current entry order.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

This function should be called before calling [`xas_split()`](xarray.md#c.xas_split "xas_split").
If necessary, it will allocate new nodes (and fill them with **entry**)
to prepare for the upcoming split of an entry of **order** size into
entries of the order stored in the **xas**.

**Context**

May sleep if **gfp** flags permit.

void xas_split(struct xa_state \*xas, void \*entry, unsigned int order)
:   Split a multi-index entry into smaller entries.

**Parameters**

`struct xa_state *xas`
:   XArray operation state.

`void *entry`
:   New entry to store in the array.

`unsigned int order`
:   Current entry order.

**Description**

The size of the new entries is set in **xas**. The value in **entry** is
copied to all the replacement entries.

**Context**

Any context. The caller should hold the xa_lock.

void xas_pause(struct xa_state \*xas)
:   Pause a walk to drop a lock.

**Parameters**

`struct xa_state *xas`
:   XArray operation state.

**Description**

Some users need to pause a walk and drop the lock they're holding in
order to yield to a higher priority thread or carry out an operation
on an entry. Those users should call this function before they drop
the lock. It resets the **xas** to be suitable for the next iteration
of the loop after the user has reacquired the lock. If most entries
found during a walk require you to call [`xas_pause()`](xarray.md#c.xas_pause "xas_pause"), the [`xa_for_each()`](xarray.md#c.xa_for_each "xa_for_each")
iterator may be more appropriate.

Note that [`xas_pause()`](xarray.md#c.xas_pause "xas_pause") only works for forward iteration. If a user needs
to pause a reverse iteration, we will need a xas_pause_rev().

void \*xas_find(struct xa_state \*xas, unsigned long max)
:   Find the next present entry in the XArray.

**Parameters**

`struct xa_state *xas`
:   XArray operation state.

`unsigned long max`
:   Highest index to return.

**Description**

If the **xas** has not yet been walked to an entry, return the entry
which has an index >= xas.xa_index. If it has been walked, the entry
currently being pointed at has been processed, and so we move to the
next entry.

If no entry is found and the array is smaller than **max**, the iterator
is set to the smallest index not yet in the array. This allows **xas**
to be immediately passed to [`xas_store()`](xarray.md#c.xas_store "xas_store").

**Return**

The entry, if found, otherwise `NULL`.

void \*xas_find_marked(struct xa_state \*xas, unsigned long max, xa_mark_t mark)
:   Find the next marked entry in the XArray.

**Parameters**

`struct xa_state *xas`
:   XArray operation state.

`unsigned long max`
:   Highest index to return.

`xa_mark_t mark`
:   Mark number to search for.

**Description**

If the **xas** has not yet been walked to an entry, return the marked entry
which has an index >= xas.xa_index. If it has been walked, the entry
currently being pointed at has been processed, and so we return the
first marked entry with an index > xas.xa_index.

If no marked entry is found and the array is smaller than **max**, **xas** is
set to the bounds state and xas->xa_index is set to the smallest index
not yet in the array. This allows **xas** to be immediately passed to
[`xas_store()`](xarray.md#c.xas_store "xas_store").

If no entry is found before **max** is reached, **xas** is set to the restart
state.

**Return**

The entry, if found, otherwise `NULL`.

void \*xas_find_conflict(struct xa_state \*xas)
:   Find the next present entry in a range.

**Parameters**

`struct xa_state *xas`
:   XArray operation state.

**Description**

The **xas** describes both a range and a position within that range.

**Context**

Any context. Expects xa_lock to be held.

**Return**

The next entry in the range covered by **xas** or `NULL`.

void \*xa_load(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index)
:   Load an entry from an XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   index into array.

**Context**

Any context. Takes and releases the RCU lock.

**Return**

The entry at **index** in **xa**.

void \*__xa_erase(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index)
:   Erase this entry from the XArray while locked.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index into array.

**Description**

After this function returns, loading from **index** will return `NULL`.
If the index is part of a multi-index entry, all indices will be erased
and none of the entries will be part of a multi-index entry.

**Context**

Any context. Expects xa_lock to be held on entry.

**Return**

The entry which used to be at this index.

void \*xa_erase(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index)
:   Erase this entry from the XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index of entry.

**Description**

After this function returns, loading from **index** will return `NULL`.
If the index is part of a multi-index entry, all indices will be erased
and none of the entries will be part of a multi-index entry.

**Context**

Any context. Takes and releases the xa_lock.

**Return**

The entry which used to be at this index.

void \*__xa_store(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index, void \*entry, gfp_t gfp)
:   Store this entry in the XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index into array.

`void *entry`
:   New entry.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

You must already be holding the xa_lock when calling this function.
It will drop the lock if needed to allocate memory, and then reacquire
it afterwards.

**Context**

Any context. Expects xa_lock to be held on entry. May
release and reacquire xa_lock if **gfp** flags permit.

**Return**

The old entry at this index or [`xa_err()`](xarray.md#c.xa_err "xa_err") if an error happened.

void \*xa_store(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index, void \*entry, gfp_t gfp)
:   Store this entry in the XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index into array.

`void *entry`
:   New entry.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

After this function returns, loads from this index will return **entry**.
Storing into an existing multi-index entry updates the entry of every index.
The marks associated with **index** are unaffected unless **entry** is `NULL`.

**Context**

Any context. Takes and releases the xa_lock.
May sleep if the **gfp** flags permit.

**Return**

The old entry at this index on success, xa_err(-EINVAL) if **entry**
cannot be stored in an XArray, or xa_err(-ENOMEM) if memory allocation
failed.

void \*__xa_cmpxchg(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index, void \*old, void \*entry, gfp_t gfp)
:   Store this entry in the XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index into array.

`void *old`
:   Old value to test against.

`void *entry`
:   New entry.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

You must already be holding the xa_lock when calling this function.
It will drop the lock if needed to allocate memory, and then reacquire
it afterwards.

**Context**

Any context. Expects xa_lock to be held on entry. May
release and reacquire xa_lock if **gfp** flags permit.

**Return**

The old entry at this index or [`xa_err()`](xarray.md#c.xa_err "xa_err") if an error happened.

int __xa_insert(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index, void \*entry, gfp_t gfp)
:   Store this entry in the XArray if no entry is present.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index into array.

`void *entry`
:   New entry.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

Inserting a NULL entry will store a reserved entry (like [`xa_reserve()`](xarray.md#c.xa_reserve "xa_reserve"))
if no entry is present. Inserting will fail if a reserved entry is
present, even though loading from this index will return NULL.

**Context**

Any context. Expects xa_lock to be held on entry. May
release and reacquire xa_lock if **gfp** flags permit.

**Return**

0 if the store succeeded. -EBUSY if another entry was present.
-ENOMEM if memory could not be allocated.

void \*xa_store_range(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long first, unsigned long last, void \*entry, gfp_t gfp)
:   Store this entry at a range of indices in the XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long first`
:   First index to affect.

`unsigned long last`
:   Last index to affect.

`void *entry`
:   New entry.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

After this function returns, loads from any index between **first** and **last**,
inclusive will return **entry**.
Storing into an existing multi-index entry updates the entry of every index.
The marks associated with **index** are unaffected unless **entry** is `NULL`.

**Context**

Process context. Takes and releases the xa_lock. May sleep
if the **gfp** flags permit.

**Return**

`NULL` on success, xa_err(-EINVAL) if **entry** cannot be stored in
an XArray, or xa_err(-ENOMEM) if memory allocation failed.

int xa_get_order(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index)
:   Get the order of an entry.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index of the entry.

**Return**

A number between 0 and 63 indicating the order of the entry.

int __xa_alloc(struct [xarray](xarray.md#c.xarray "xarray") \*xa, u32 \*id, void \*entry, struct [xa_limit](xarray.md#c.xa_limit "xa_limit") limit, gfp_t gfp)
:   Find somewhere to store this entry in the XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`u32 *id`
:   Pointer to ID.

`void *entry`
:   New entry.

`struct xa_limit limit`
:   Range for allocated ID.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

Finds an empty entry in **xa** between **limit.min** and **limit.max**,
stores the index into the **id** pointer, then stores the entry at
that index. A concurrent lookup will not see an uninitialised **id**.

Must only be operated on an xarray initialized with flag XA_FLAGS_ALLOC set
in [`xa_init_flags()`](xarray.md#c.xa_init_flags "xa_init_flags").

**Context**

Any context. Expects xa_lock to be held on entry. May
release and reacquire xa_lock if **gfp** flags permit.

**Return**

0 on success, -ENOMEM if memory could not be allocated or
-EBUSY if there are no free entries in **limit**.

int __xa_alloc_cyclic(struct [xarray](xarray.md#c.xarray "xarray") \*xa, u32 \*id, void \*entry, struct [xa_limit](xarray.md#c.xa_limit "xa_limit") limit, u32 \*next, gfp_t gfp)
:   Find somewhere to store this entry in the XArray.

**Parameters**

`struct xarray *xa`
:   XArray.

`u32 *id`
:   Pointer to ID.

`void *entry`
:   New entry.

`struct xa_limit limit`
:   Range of allocated ID.

`u32 *next`
:   Pointer to next ID to allocate.

`gfp_t gfp`
:   Memory allocation flags.

**Description**

Finds an empty entry in **xa** between **limit.min** and **limit.max**,
stores the index into the **id** pointer, then stores the entry at
that index. A concurrent lookup will not see an uninitialised **id**.
The search for an empty entry will start at **next** and will wrap
around if necessary.

Must only be operated on an xarray initialized with flag XA_FLAGS_ALLOC set
in [`xa_init_flags()`](xarray.md#c.xa_init_flags "xa_init_flags").

**Context**

Any context. Expects xa_lock to be held on entry. May
release and reacquire xa_lock if **gfp** flags permit.

**Return**

0 if the allocation succeeded without wrapping. 1 if the
allocation succeeded after wrapping, -ENOMEM if memory could not be
allocated or -EBUSY if there are no free entries in **limit**.

void __xa_set_mark(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index, xa_mark_t mark)
:   Set this mark on this entry while locked.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index of entry.

`xa_mark_t mark`
:   Mark number.

**Description**

Attempting to set a mark on a `NULL` entry does not succeed.

**Context**

Any context. Expects xa_lock to be held on entry.

void __xa_clear_mark(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index, xa_mark_t mark)
:   Clear this mark on this entry while locked.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index of entry.

`xa_mark_t mark`
:   Mark number.

**Context**

Any context. Expects xa_lock to be held on entry.

bool xa_get_mark(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index, xa_mark_t mark)
:   Inquire whether this mark is set on this entry.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index of entry.

`xa_mark_t mark`
:   Mark number.

**Description**

This function uses the RCU read lock, so the result may be out of date
by the time it returns. If you need the result to be stable, use a lock.

**Context**

Any context. Takes and releases the RCU lock.

**Return**

True if the entry at **index** has this mark set, false if it doesn't.

void xa_set_mark(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index, xa_mark_t mark)
:   Set this mark on this entry.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index of entry.

`xa_mark_t mark`
:   Mark number.

**Description**

Attempting to set a mark on a `NULL` entry does not succeed.

**Context**

Process context. Takes and releases the xa_lock.

void xa_clear_mark(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long index, xa_mark_t mark)
:   Clear this mark on this entry.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long index`
:   Index of entry.

`xa_mark_t mark`
:   Mark number.

**Description**

Clearing a mark always succeeds.

**Context**

Process context. Takes and releases the xa_lock.

void \*xa_find(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long \*indexp, unsigned long max, xa_mark_t filter)
:   Search the XArray for an entry.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long *indexp`
:   Pointer to an index.

`unsigned long max`
:   Maximum index to search to.

`xa_mark_t filter`
:   Selection criterion.

**Description**

Finds the entry in **xa** which matches the **filter**, and has the lowest
index that is at least **indexp** and no more than **max**.
If an entry is found, **indexp** is updated to be the index of the entry.
This function is protected by the RCU read lock, so it may not find
entries which are being simultaneously added. It will not return an
`XA_RETRY_ENTRY`; if you need to see retry entries, use [`xas_find()`](xarray.md#c.xas_find "xas_find").

**Context**

Any context. Takes and releases the RCU lock.

**Return**

The entry, if found, otherwise `NULL`.

void \*xa_find_after(struct [xarray](xarray.md#c.xarray "xarray") \*xa, unsigned long \*indexp, unsigned long max, xa_mark_t filter)
:   Search the XArray for a present entry.

**Parameters**

`struct xarray *xa`
:   XArray.

`unsigned long *indexp`
:   Pointer to an index.

`unsigned long max`
:   Maximum index to search to.

`xa_mark_t filter`
:   Selection criterion.

**Description**

Finds the entry in **xa** which matches the **filter** and has the lowest
index that is above **indexp** and no more than **max**.
If an entry is found, **indexp** is updated to be the index of the entry.
This function is protected by the RCU read lock, so it may miss entries
which are being simultaneously added. It will not return an
`XA_RETRY_ENTRY`; if you need to see retry entries, use [`xas_find()`](xarray.md#c.xas_find "xas_find").

**Context**

Any context. Takes and releases the RCU lock.

**Return**

The pointer, if found, otherwise `NULL`.

unsigned int xa_extract(struct [xarray](xarray.md#c.xarray "xarray") \*xa, void \*\*dst, unsigned long start, unsigned long max, unsigned int n, xa_mark_t filter)
:   Copy selected entries from the XArray into a normal array.

**Parameters**

`struct xarray *xa`
:   The source XArray to copy from.

`void **dst`
:   The buffer to copy entries into.

`unsigned long start`
:   The first index in the XArray eligible to be selected.

`unsigned long max`
:   The last index in the XArray eligible to be selected.

`unsigned int n`
:   The maximum number of entries to copy.

`xa_mark_t filter`
:   Selection criterion.

**Description**

Copies up to **n** entries that match **filter** from the XArray. The
copied entries will have indices between **start** and **max**, inclusive.

The **filter** may be an XArray mark value, in which case entries which are
marked with that mark will be copied. It may also be `XA_PRESENT`, in
which case all entries which are not `NULL` will be copied.

The entries returned may not represent a snapshot of the XArray at a
moment in time. For example, if another thread stores to index 5, then
index 10, calling [`xa_extract()`](xarray.md#c.xa_extract "xa_extract") may return the old contents of index 5
and the new contents of index 10. Indices not modified while this
function is running will not be skipped.

If you need stronger guarantees, holding the xa_lock across calls to this
function will prevent concurrent modification.

**Context**

Any context. Takes and releases the RCU lock.

**Return**

The number of entries copied.

void xa_delete_node(struct xa_node \*node, [xa_update_node_t](xarray.md#c.xa_update_node_t "xa_update_node_t") update)
:   Private interface for workingset code.

**Parameters**

`struct xa_node *node`
:   Node to be removed from the tree.

`xa_update_node_t update`
:   Function to call to update ancestor nodes.

**Context**

xa_lock must be held on entry and will not be released.

void xa_destroy(struct [xarray](xarray.md#c.xarray "xarray") \*xa)
:   Free all internal data structures.

**Parameters**

`struct xarray *xa`
:   XArray.

**Description**

After calling this function, the XArray is empty and has freed all memory
allocated for its internal data structures. You are responsible for
freeing the objects referenced by the XArray.

**Context**

Any context. Takes and releases the xa_lock, interrupt-safe.
