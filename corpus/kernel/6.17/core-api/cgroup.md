---
collection: kernel
version: "6.17"
title: "Cgroup Kernel APIs"
source_url: https://www.kernel.org/doc/html/v6.17/core-api/cgroup.html
fetched_at: 2026-09-16T16:19:25+00:00
---
# Cgroup Kernel APIs

## Device Memory Cgroup API (dmemcg)

bool dmem_cgroup_state_evict_valuable(struct dmem_cgroup_pool_state \*limit_pool, struct dmem_cgroup_pool_state \*test_pool, bool ignore_low, bool \*ret_hit_low)
:   Check if we should evict from test_pool

**Parameters**

`struct dmem_cgroup_pool_state *limit_pool`
:   The pool for which we hit limits

`struct dmem_cgroup_pool_state *test_pool`
:   The pool for which to test

`bool ignore_low`
:   Whether we have to respect low watermarks.

`bool *ret_hit_low`
:   Pointer to whether it makes sense to consider low watermark.

**Description**

This function returns true if we can evict from **test_pool**, false if not.
When returning false and **ignore_low** is false, **ret_hit_low** may
be set to true to indicate this function can be retried with **ignore_low**
set to true.

**Return**

bool

void dmem_cgroup_unregister_region(struct dmem_cgroup_region \*region)
:   Unregister a previously registered region.

**Parameters**

`struct dmem_cgroup_region *region`
:   The region to unregister.

**Description**

This function undoes dmem_cgroup_register_region.

struct dmem_cgroup_region \*dmem_cgroup_register_region(u64 size, const char \*fmt, ...)
:   Register a regions for dev cgroup.

**Parameters**

`u64 size`
:   Size of region to register, in bytes.

`const char *fmt`
:   Region parameters to register

`...`
:   variable arguments

**Description**

This function registers a node in the dmem cgroup with the
name given. After calling this function, the region can be
used for allocations.

**Return**

NULL or a `struct on` success, PTR_ERR on failure.

void dmem_cgroup_pool_state_put(struct dmem_cgroup_pool_state \*pool)
:   Drop a reference to a dmem_cgroup_pool_state

**Parameters**

`struct dmem_cgroup_pool_state *pool`
:   `dmem_cgroup_pool_state`

**Description**

Called to drop a reference to the limiting pool returned by
[`dmem_cgroup_try_charge()`](cgroup.md#c.dmem_cgroup_try_charge "dmem_cgroup_try_charge").

void dmem_cgroup_uncharge(struct dmem_cgroup_pool_state \*pool, u64 size)
:   Uncharge a pool.

**Parameters**

`struct dmem_cgroup_pool_state *pool`
:   Pool to uncharge.

`u64 size`
:   Size to uncharge.

**Description**

Undoes the effects of dmem_cgroup_try_charge.
Must be called with the returned pool as argument,
and same **index** and **size**.

int dmem_cgroup_try_charge(struct dmem_cgroup_region \*region, u64 size, struct dmem_cgroup_pool_state \*\*ret_pool, struct dmem_cgroup_pool_state \*\*ret_limit_pool)
:   Try charging a new allocation to a region.

**Parameters**

`struct dmem_cgroup_region *region`
:   dmem region to charge

`u64 size`
:   Size (in bytes) to charge.

`struct dmem_cgroup_pool_state **ret_pool`
:   On succesfull allocation, the pool that is charged.

`struct dmem_cgroup_pool_state **ret_limit_pool`
:   On a failed allocation, the limiting pool.

**Description**

This function charges the **region** region for a size of **size** bytes.

If the function succeeds, **ret_pool** is set, which must be passed to
[`dmem_cgroup_uncharge()`](cgroup.md#c.dmem_cgroup_uncharge "dmem_cgroup_uncharge") when undoing the allocation.

When this function fails with -EAGAIN and **ret_limit_pool** is non-null, it
will be set to the pool for which the limit is hit. This can be used for
eviction as argument to `dmem_cgroup_evict_valuable()`. This reference must be freed
with **[`dmem_cgroup_pool_state_put()`](cgroup.md#c.dmem_cgroup_pool_state_put "dmem_cgroup_pool_state_put")**.

**Return**

0 on success, -EAGAIN on hitting a limit, or a negative errno on failure.
