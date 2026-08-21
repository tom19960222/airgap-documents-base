---
collection: kernel
version: "6.8"
title: "API Reference"
source_url: https://www.kernel.org/doc/html/v6.8/mm/damon/api.html
fetched_at: 2026-08-21T03:38:55+00:00
---
English

- [Chinese (Simplified)](../../translations/zh_CN/mm/damon/api.md)

# API Reference

Kernel space programs can use every feature of DAMON using below APIs. All you
need to do is including `damon.h`, which is located in `include/linux/` of
the source tree.

## Structures

struct damon_addr_range
:   Represents an address region of [**start**, **end**).

**Definition**:

```
struct damon_addr_range {
    unsigned long start;
    unsigned long end;
};
```

**Members**

`start`
:   Start address of the region (inclusive).

`end`
:   End address of the region (exclusive).

struct damon_region
:   Represents a monitoring target region.

**Definition**:

```
struct damon_region {
    struct damon_addr_range ar;
    unsigned long sampling_addr;
    unsigned int nr_accesses;
    unsigned int nr_accesses_bp;
    struct list_head list;
    unsigned int age;
};
```

**Members**

`ar`
:   The address range of the region.

`sampling_addr`
:   Address of the sample for the next access check.

`nr_accesses`
:   Access frequency of this region.

`nr_accesses_bp`
:   **nr_accesses** in basis point (0.01%) that updated for
    each sampling interval.

`list`
:   List head for siblings.

`age`
:   Age of this region.

**Description**

**nr_accesses** is reset to zero for every [`damon_attrs->aggr_interval`](api.md#c.damon_attrs "damon_attrs") and be
increased for every [`damon_attrs->sample_interval`](api.md#c.damon_attrs "damon_attrs") if an access to the region
during the last sampling interval is found. The update of this field should
not be done with direct access but with the helper function,
[`damon_update_region_access_rate()`](api.md#c.damon_update_region_access_rate "damon_update_region_access_rate").

**nr_accesses_bp** is another representation of **nr_accesses** in basis point
(1 in 10,000) that updated for every [`damon_attrs->sample_interval`](api.md#c.damon_attrs "damon_attrs") in a
manner similar to moving sum. By the algorithm, this value becomes
**nr_accesses** \* 10000 for every [`struct damon_attrs`](api.md#c.damon_attrs "damon_attrs")->aggr_interval. This can
be used when the aggregation interval is too huge and therefore cannot wait
for it before getting the access monitoring results.

**age** is initially zero, increased for each aggregation interval, and reset
to zero again if the access frequency is significantly changed. If two
regions are merged into a new region, both **nr_accesses** and **age** of the new
region are set as region size-weighted average of those of the two regions.

struct damon_target
:   Represents a monitoring target.

**Definition**:

```
struct damon_target {
    struct pid *pid;
    unsigned int nr_regions;
    struct list_head regions_list;
    struct list_head list;
};
```

**Members**

`pid`
:   The PID of the virtual address space to monitor.

`nr_regions`
:   Number of monitoring target regions of this target.

`regions_list`
:   Head of the monitoring target regions of this target.

`list`
:   List head for siblings.

**Description**

Each monitoring context could have multiple targets. For example, a context
for virtual memory address spaces could have multiple target processes. The
**pid** should be set for appropriate [`struct damon_operations`](api.md#c.damon_operations "damon_operations") including the
virtual address spaces monitoring operations.

enum damos_action
:   Represents an action of a Data Access Monitoring-based Operation Scheme.

**Constants**

`DAMOS_WILLNEED`
:   Call `madvise()` for the region with MADV_WILLNEED.

`DAMOS_COLD`
:   Call `madvise()` for the region with MADV_COLD.

`DAMOS_PAGEOUT`
:   Call `madvise()` for the region with MADV_PAGEOUT.

`DAMOS_HUGEPAGE`
:   Call `madvise()` for the region with MADV_HUGEPAGE.

`DAMOS_NOHUGEPAGE`
:   Call `madvise()` for the region with MADV_NOHUGEPAGE.

`DAMOS_LRU_PRIO`
:   Prioritize the region on its LRU lists.

`DAMOS_LRU_DEPRIO`
:   Deprioritize the region on its LRU lists.

`DAMOS_STAT`
:   Do nothing but count the stat.

`NR_DAMOS_ACTIONS`
:   Total number of DAMOS actions

**Description**

The support of each action is up to running [`struct damon_operations`](api.md#c.damon_operations "damon_operations").
`enum DAMON_OPS_VADDR` and `enum DAMON_OPS_FVADDR` supports all actions except
`enum DAMOS_LRU_PRIO` and `enum DAMOS_LRU_DEPRIO`. `enum DAMON_OPS_PADDR`
supports only `enum DAMOS_PAGEOUT`, `enum DAMOS_LRU_PRIO`, `enum
DAMOS_LRU_DEPRIO`, and `DAMOS_STAT`.

struct damos_quota
:   Controls the aggressiveness of the given scheme.

**Definition**:

```
struct damos_quota {
    unsigned long ms;
    unsigned long sz;
    unsigned long reset_interval;
    unsigned int weight_sz;
    unsigned int weight_nr_accesses;
    unsigned int weight_age;
    unsigned long (*get_score)(void *arg);
    void *get_score_arg;
};
```

**Members**

`ms`
:   Maximum milliseconds that the scheme can use.

`sz`
:   Maximum bytes of memory that the action can be applied.

`reset_interval`
:   Charge reset interval in milliseconds.

`weight_sz`
:   Weight of the region's size for prioritization.

`weight_nr_accesses`
:   Weight of the region's nr_accesses for prioritization.

`weight_age`
:   Weight of the region's age for prioritization.

`get_score`
:   Feedback function for self-tuning quota.

`get_score_arg`
:   Parameter for **get_score**

**Description**

To avoid consuming too much CPU time or IO resources for applying the
[`struct damos`](api.md#c.damos "damos")->action to large memory, DAMON allows users to set time and/or
size quotas. The quotas can be set by writing non-zero values to `ms` and
`sz`, respectively. If the time quota is set, DAMON tries to use only up to
`ms` milliseconds within `reset_interval` for applying the action. If the
size quota is set, DAMON tries to apply the action only up to `sz` bytes
within `reset_interval`.

Internally, the time quota is transformed to a size quota using estimated
throughput of the scheme's action. DAMON then compares it against `sz` and
uses smaller one as the effective quota.

For selecting regions within the quota, DAMON prioritizes current scheme's
target memory regions using the [`struct damon_operations`](api.md#c.damon_operations "damon_operations")->get_scheme_score.
You could customize the prioritization logic by setting `weight_sz`,
`weight_nr_accesses`, and `weight_age`, because monitoring operations are
encouraged to respect those.

If **get_score** function pointer is set, DAMON calls it back with
**get_score_arg** and get the return value of it for every **reset_interval**.
Then, DAMON adjusts the effective quota using the return value as a feedback
score to the current quota, using its internal feedback loop algorithm.

The feedback loop algorithem assumes the quota input and the feedback score
output are in a positive proportional relationship, and the goal of the
tuning is getting the feedback screo value of 10,000. If **ms** and/or **sz** are
set together, those work as a hard limit quota. If neither **ms** nor **sz** are
set, the mechanism starts from the quota of one byte.

enum damos_wmark_metric
:   Represents the watermark metric.

**Constants**

`DAMOS_WMARK_NONE`
:   Ignore the watermarks of the given scheme.

`DAMOS_WMARK_FREE_MEM_RATE`
:   Free memory rate of the system in [0,1000].

`NR_DAMOS_WMARK_METRICS`
:   Total number of DAMOS watermark metrics

struct damos_watermarks
:   Controls when a given scheme should be activated.

**Definition**:

```
struct damos_watermarks {
    enum damos_wmark_metric metric;
    unsigned long interval;
    unsigned long high;
    unsigned long mid;
    unsigned long low;
};
```

**Members**

`metric`
:   Metric for the watermarks.

`interval`
:   Watermarks check time interval in microseconds.

`high`
:   High watermark.

`mid`
:   Middle watermark.

`low`
:   Low watermark.

**Description**

If `metric` is `DAMOS_WMARK_NONE`, the scheme is always active. Being active
means DAMON does monitoring and applying the action of the scheme to
appropriate memory regions. Else, DAMON checks `metric` of the system for at
least every `interval` microseconds and works as below.

If `metric` is higher than `high`, the scheme is inactivated. If `metric` is
between `mid` and `low`, the scheme is activated. If `metric` is lower than
`low`, the scheme is inactivated.

struct damos_stat
:   Statistics on a given scheme.

**Definition**:

```
struct damos_stat {
    unsigned long nr_tried;
    unsigned long sz_tried;
    unsigned long nr_applied;
    unsigned long sz_applied;
    unsigned long qt_exceeds;
};
```

**Members**

`nr_tried`
:   Total number of regions that the scheme is tried to be applied.

`sz_tried`
:   Total size of regions that the scheme is tried to be applied.

`nr_applied`
:   Total number of regions that the scheme is applied.

`sz_applied`
:   Total size of regions that the scheme is applied.

`qt_exceeds`
:   Total number of times the quota of the scheme has exceeded.

enum damos_filter_type
:   Type of memory for [`struct damos_filter`](api.md#c.damos_filter "damos_filter")

**Constants**

`DAMOS_FILTER_TYPE_ANON`
:   Anonymous pages.

`DAMOS_FILTER_TYPE_MEMCG`
:   Specific memcg's pages.

`DAMOS_FILTER_TYPE_ADDR`
:   Address range.

`DAMOS_FILTER_TYPE_TARGET`
:   Data Access Monitoring target.

`NR_DAMOS_FILTER_TYPES`
:   Number of filter types.

**Description**

The anon pages type and memcg type filters are handled by underlying
[`struct damon_operations`](api.md#c.damon_operations "damon_operations") as a part of scheme action trying, and therefore
accounted as 'tried'. In contrast, other types are handled by core layer
before trying of the action and therefore not accounted as 'tried'.

The support of the filters that handled by [`struct damon_operations`](api.md#c.damon_operations "damon_operations") depend
on the running [`struct damon_operations`](api.md#c.damon_operations "damon_operations").
`enum DAMON_OPS_PADDR` supports both anon pages type and memcg type filters,
while `enum DAMON_OPS_VADDR` and `enum DAMON_OPS_FVADDR` don't support any of
the two types.

struct damos_filter
:   DAMOS action target memory filter.

**Definition**:

```
struct damos_filter {
    enum damos_filter_type type;
    bool matching;
    union {
        unsigned short memcg_id;
        struct damon_addr_range addr_range;
        int target_idx;
    };
    struct list_head list;
};
```

**Members**

`type`
:   Type of the page.

`matching`
:   If the matching page should filtered out or in.

`{unnamed_union}`
:   anonymous

`memcg_id`
:   Memcg id of the question if **type** is DAMOS_FILTER_MEMCG.

`addr_range`
:   Address range if **type** is DAMOS_FILTER_TYPE_ADDR.

`target_idx`
:   Index of the [`struct damon_target`](api.md#c.damon_target "damon_target") of
    [`damon_ctx->adaptive_targets`](api.md#c.damon_ctx "damon_ctx") if **type** is
    DAMOS_FILTER_TYPE_TARGET.

`list`
:   List head for siblings.

**Description**

Before applying the [`damos->action`](api.md#c.damos "damos") to a memory region, DAMOS checks if each
page of the region matches to this and avoid applying the action if so.
Support of each filter type depends on the running [`struct damon_operations`](api.md#c.damon_operations "damon_operations")
and the type. Refer to [`enum damos_filter_type`](api.md#c.damos_filter_type "damos_filter_type") for more detai.

struct damos_access_pattern
:   Target access pattern of the given scheme.

**Definition**:

```
struct damos_access_pattern {
    unsigned long min_sz_region;
    unsigned long max_sz_region;
    unsigned int min_nr_accesses;
    unsigned int max_nr_accesses;
    unsigned int min_age_region;
    unsigned int max_age_region;
};
```

**Members**

`min_sz_region`
:   Minimum size of target regions.

`max_sz_region`
:   Maximum size of target regions.

`min_nr_accesses`
:   Minimum `->nr_accesses` of target regions.

`max_nr_accesses`
:   Maximum `->nr_accesses` of target regions.

`min_age_region`
:   Minimum age of target regions.

`max_age_region`
:   Maximum age of target regions.

struct damos
:   Represents a Data Access Monitoring-based Operation Scheme.

**Definition**:

```
struct damos {
    struct damos_access_pattern pattern;
    enum damos_action action;
    unsigned long apply_interval_us;
    struct damos_quota quota;
    struct damos_watermarks wmarks;
    struct list_head filters;
    struct damos_stat stat;
    struct list_head list;
};
```

**Members**

`pattern`
:   Access pattern of target regions.

`action`
:   `damo_action` to be applied to the target regions.

`apply_interval_us`
:   The time between applying the **action**.

`quota`
:   Control the aggressiveness of this scheme.

`wmarks`
:   Watermarks for automated (in)activation of this scheme.

`filters`
:   Additional set of [`struct damos_filter`](api.md#c.damos_filter "damos_filter") for `action`.

`stat`
:   Statistics of this scheme.

`list`
:   List head for siblings.

**Description**

For each **apply_interval_us**, DAMON finds regions which fit in the
`pattern` and applies `action` to those. To avoid consuming too much
CPU time or IO resources for the `action`, `quota` is used.

If **apply_interval_us** is zero, [`damon_attrs->aggr_interval`](api.md#c.damon_attrs "damon_attrs") is used instead.

To do the work only when needed, schemes can be activated for specific
system situations using `wmarks`. If all schemes that registered to the
monitoring context are inactive, DAMON stops monitoring either, and just
repeatedly checks the watermarks.

Before applying the `action` to a memory region, [`struct damon_operations`](api.md#c.damon_operations "damon_operations")
implementation could check pages of the region and skip `action` to respect
`filters`

After applying the `action` to each region, `stat_count` and `stat_sz` is
updated to reflect the number of regions and total size of regions that the
`action` is applied.

enum damon_ops_id
:   Identifier for each monitoring operations implementation

**Constants**

`DAMON_OPS_VADDR`
:   Monitoring operations for virtual address spaces

`DAMON_OPS_FVADDR`
:   Monitoring operations for only fixed ranges of virtual
    address spaces

`DAMON_OPS_PADDR`
:   Monitoring operations for the physical address space

`NR_DAMON_OPS`
:   Number of monitoring operations implementations

struct damon_operations
:   Monitoring operations for given use cases.

**Definition**:

```
struct damon_operations {
    enum damon_ops_id id;
    void (*init)(struct damon_ctx *context);
    void (*update)(struct damon_ctx *context);
    void (*prepare_access_checks)(struct damon_ctx *context);
    unsigned int (*check_accesses)(struct damon_ctx *context);
    void (*reset_aggregated)(struct damon_ctx *context);
    int (*get_scheme_score)(struct damon_ctx *context,struct damon_target *t, struct damon_region *r, struct damos *scheme);
    unsigned long (*apply_scheme)(struct damon_ctx *context,struct damon_target *t, struct damon_region *r, struct damos *scheme);
    bool (*target_valid)(struct damon_target *t);
    void (*cleanup)(struct damon_ctx *context);
};
```

**Members**

`id`
:   Identifier of this operations set.

`init`
:   Initialize operations-related data structures.

`update`
:   Update operations-related data structures.

`prepare_access_checks`
:   Prepare next access check of target regions.

`check_accesses`
:   Check the accesses to target regions.

`reset_aggregated`
:   Reset aggregated accesses monitoring results.

`get_scheme_score`
:   Get the score of a region for a scheme.

`apply_scheme`
:   Apply a DAMON-based operation scheme.

`target_valid`
:   Determine if the target is valid.

`cleanup`
:   Clean up the context.

**Description**

DAMON can be extended for various address spaces and usages. For this,
users should register the low level operations for their target address
space and usecase via the [`damon_ctx.ops`](api.md#c.damon_ctx "damon_ctx"). Then, the monitoring thread
([`damon_ctx.kdamond`](api.md#c.damon_ctx "damon_ctx")) calls **init** and **prepare_access_checks** before starting
the monitoring, **update** after each [`damon_attrs.ops_update_interval`](api.md#c.damon_attrs "damon_attrs"), and
**check_accesses**, **target_valid** and **prepare_access_checks** after each
[`damon_attrs.sample_interval`](api.md#c.damon_attrs "damon_attrs"). Finally, **reset_aggregated** is called after
each [`damon_attrs.aggr_interval`](api.md#c.damon_attrs "damon_attrs").

Each [`struct damon_operations`](api.md#c.damon_operations "damon_operations") instance having valid **id** can be registered
via [`damon_register_ops()`](api.md#c.damon_register_ops "damon_register_ops") and selected by [`damon_select_ops()`](api.md#c.damon_select_ops "damon_select_ops") later.
**init** should initialize operations-related data structures. For example,
this could be used to construct proper monitoring target regions and link
those to **damon_ctx.adaptive_targets**.
**update** should update the operations-related data structures. For example,
this could be used to update monitoring target regions for current status.
**prepare_access_checks** should manipulate the monitoring regions to be
prepared for the next access check.
**check_accesses** should check the accesses to each region that made after the
last preparation and update the number of observed accesses of each region.
It should also return max number of observed accesses that made as a result
of its update. The value will be used for regions adjustment threshold.
**reset_aggregated** should reset the access monitoring results that aggregated
by **check_accesses**.
**get_scheme_score** should return the priority score of a region for a scheme
as an integer in [0, `DAMOS_MAX_SCORE`].
**apply_scheme** is called from **kdamond** when a region for user provided
DAMON-based operation scheme is found. It should apply the scheme's action
to the region and return bytes of the region that the action is successfully
applied.
**target_valid** should check whether the target is still valid for the
monitoring.
**cleanup** is called from **kdamond** just before its termination.

struct damon_callback
:   Monitoring events notification callbacks.

**Definition**:

```
struct damon_callback {
    void *private;
    int (*before_start)(struct damon_ctx *context);
    int (*after_wmarks_check)(struct damon_ctx *context);
    int (*after_sampling)(struct damon_ctx *context);
    int (*after_aggregation)(struct damon_ctx *context);
    int (*before_damos_apply)(struct damon_ctx *context,struct damon_target *target,struct damon_region *region, struct damos *scheme);
    void (*before_terminate)(struct damon_ctx *context);
};
```

**Members**

`private`
:   User private data.

`before_start`
:   Called before starting the monitoring.

`after_wmarks_check`
:   Called after each schemes' watermarks check.

`after_sampling`
:   Called after each sampling.

`after_aggregation`
:   Called after each aggregation.

`before_damos_apply`
:   Called before applying DAMOS action.

`before_terminate`
:   Called before terminating the monitoring.

**Description**

The monitoring thread ([`damon_ctx.kdamond`](api.md#c.damon_ctx "damon_ctx")) calls **before_start** and
**before_terminate** just before starting and finishing the monitoring,
respectively. Therefore, those are good places for installing and cleaning
**private**.

The monitoring thread calls **after_wmarks_check** after each DAMON-based
operation schemes' watermarks check. If users need to make changes to the
attributes of the monitoring context while it's deactivated due to the
watermarks, this is the good place to do.

The monitoring thread calls **after_sampling** and **after_aggregation** for each
of the sampling intervals and aggregation intervals, respectively.
Therefore, users can safely access the monitoring results without additional
protection. For the reason, users are recommended to use these callback for
the accesses to the results.

If any callback returns non-zero, monitoring stops.

struct damon_attrs
:   Monitoring attributes for accuracy/overhead control.

**Definition**:

```
struct damon_attrs {
    unsigned long sample_interval;
    unsigned long aggr_interval;
    unsigned long ops_update_interval;
    unsigned long min_nr_regions;
    unsigned long max_nr_regions;
};
```

**Members**

`sample_interval`
:   The time between access samplings.

`aggr_interval`
:   The time between monitor results aggregations.

`ops_update_interval`
:   The time between monitoring operations updates.

`min_nr_regions`
:   The minimum number of adaptive monitoring
    regions.

`max_nr_regions`
:   The maximum number of adaptive monitoring
    regions.

**Description**

For each **sample_interval**, DAMON checks whether each region is accessed or
not during the last **sample_interval**. If such access is found, DAMON
aggregates the information by increasing [`damon_region->nr_accesses`](api.md#c.damon_region "damon_region") for
**aggr_interval** time. For each **aggr_interval**, the count is reset. DAMON
also checks whether the target memory regions need update (e.g., by
`mmap()` calls from the application, in case of virtual memory monitoring)
and applies the changes for each **ops_update_interval**. All time intervals
are in micro-seconds. Please refer to [`struct damon_operations`](api.md#c.damon_operations "damon_operations") and [`struct
damon_callback`](api.md#c.damon_callback "damon_callback") for more detail.

struct damon_ctx
:   Represents a context for each monitoring. This is the main interface that allows users to set the attributes and get the results of the monitoring.

**Definition**:

```
struct damon_ctx {
    struct damon_attrs attrs;
    struct task_struct *kdamond;
    struct mutex kdamond_lock;
    struct damon_operations ops;
    struct damon_callback callback;
    struct list_head adaptive_targets;
    struct list_head schemes;
};
```

**Members**

`attrs`
:   Monitoring attributes for accuracy/overhead control.

`kdamond`
:   Kernel thread who does the monitoring.

`kdamond_lock`
:   Mutex for the synchronizations with **kdamond**.

`ops`
:   Set of monitoring operations for given use cases.

`callback`
:   Set of callbacks for monitoring events notifications.

`adaptive_targets`
:   Head of monitoring targets ([`damon_target`](api.md#c.damon_target "damon_target")) list.

`schemes`
:   Head of schemes ([`damos`](api.md#c.damos "damos")) list.

**Description**

For each monitoring context, one kernel thread for the monitoring is
created. The pointer to the thread is stored in **kdamond**.

Once started, the monitoring thread runs until explicitly required to be
terminated or every monitoring target is invalid. The validity of the
targets is checked via the [`damon_operations.target_valid`](api.md#c.damon_operations "damon_operations") of **ops**. The
termination can also be explicitly requested by calling [`damon_stop()`](api.md#c.damon_stop "damon_stop").
The thread sets **kdamond** to NULL when it terminates. Therefore, users can
know whether the monitoring is ongoing or terminated by reading **kdamond**.
Reads and writes to **kdamond** from outside of the monitoring thread must
be protected by **kdamond_lock**.

Note that the monitoring thread protects only **kdamond** via **kdamond_lock**.
Accesses to other fields must be protected by themselves.

## Functions

bool damon_is_registered_ops(enum [damon_ops_id](api.md#c.damon_ops_id "damon_ops_id") id)
:   Check if a given damon_operations is registered.

**Parameters**

`enum damon_ops_id id`
:   Id of the damon_operations to check if registered.

**Return**

true if the ops is set, false otherwise.

int damon_register_ops(struct [damon_operations](api.md#c.damon_operations "damon_operations") \*ops)
:   Register a monitoring operations set to DAMON.

**Parameters**

`struct damon_operations *ops`
:   monitoring operations set to register.

**Description**

This function registers a monitoring operations set of valid [`struct
damon_operations`](api.md#c.damon_operations "damon_operations")->id so that others can find and use them later.

**Return**

0 on success, negative error code otherwise.

int damon_select_ops(struct [damon_ctx](api.md#c.damon_ctx "damon_ctx") \*ctx, enum [damon_ops_id](api.md#c.damon_ops_id "damon_ops_id") id)
:   Select a monitoring operations to use with the context.

**Parameters**

`struct damon_ctx *ctx`
:   monitoring context to use the operations.

`enum damon_ops_id id`
:   id of the registered monitoring operations to select.

**Description**

This function finds registered monitoring operations set of **id** and make
**ctx** to use it.

**Return**

0 on success, negative error code otherwise.

int damon_set_attrs(struct [damon_ctx](api.md#c.damon_ctx "damon_ctx") \*ctx, struct [damon_attrs](api.md#c.damon_attrs "damon_attrs") \*attrs)
:   Set attributes for the monitoring.

**Parameters**

`struct damon_ctx *ctx`
:   monitoring context

`struct damon_attrs *attrs`
:   monitoring attributes

**Description**

This function should be called while the kdamond is not running, or an
access check results aggregation is not ongoing (e.g., from
[`struct damon_callback`](api.md#c.damon_callback "damon_callback")->after_aggregation or
[`struct damon_callback`](api.md#c.damon_callback "damon_callback")->after_wmarks_check callbacks).

Every time interval is in micro-seconds.

**Return**

0 on success, negative error code otherwise.

void damon_set_schemes(struct [damon_ctx](api.md#c.damon_ctx "damon_ctx") \*ctx, struct [damos](api.md#c.damos "damos") \*\*schemes, ssize_t nr_schemes)
:   Set data access monitoring based operation schemes.

**Parameters**

`struct damon_ctx *ctx`
:   monitoring context

`struct damos **schemes`
:   array of the schemes

`ssize_t nr_schemes`
:   number of entries in **schemes**

**Description**

This function should not be called while the kdamond of the context is
running.

int damon_nr_running_ctxs(void)
:   Return number of currently running contexts.

**Parameters**

`void`
:   no arguments

int damon_start(struct [damon_ctx](api.md#c.damon_ctx "damon_ctx") \*\*ctxs, int nr_ctxs, bool exclusive)
:   Starts the monitorings for a given group of contexts.

**Parameters**

`struct damon_ctx **ctxs`
:   an array of the pointers for contexts to start monitoring

`int nr_ctxs`
:   size of **ctxs**

`bool exclusive`
:   exclusiveness of this contexts group

**Description**

This function starts a group of monitoring threads for a group of monitoring
contexts. One thread per each context is created and run in parallel. The
caller should handle synchronization between the threads by itself. If
**exclusive** is true and a group of threads that created by other
'[`damon_start()`](api.md#c.damon_start "damon_start")' call is currently running, this function does nothing but
returns -EBUSY.

**Return**

0 on success, negative error code otherwise.

int damon_stop(struct [damon_ctx](api.md#c.damon_ctx "damon_ctx") \*\*ctxs, int nr_ctxs)
:   Stops the monitorings for a given group of contexts.

**Parameters**

`struct damon_ctx **ctxs`
:   an array of the pointers for contexts to stop monitoring

`int nr_ctxs`
:   size of **ctxs**

**Return**

0 on success, negative error code otherwise.

int damon_set_region_biggest_system_ram_default(struct [damon_target](api.md#c.damon_target "damon_target") \*t, unsigned long \*start, unsigned long \*end)
:   Set the region of the given monitoring target as requested, or biggest 'System RAM'.

**Parameters**

`struct damon_target *t`
:   The monitoring target to set the region.

`unsigned long *start`
:   The pointer to the start address of the region.

`unsigned long *end`
:   The pointer to the end address of the region.

**Description**

This function sets the region of **t** as requested by **start** and **end**. If the
values of **start** and **end** are zero, however, this function finds the biggest
'System RAM' resource and sets the region to cover the resource. In the
latter case, this function saves the start and end addresses of the resource
in **start** and **end**, respectively.

**Return**

0 on success, negative error code otherwise.

void damon_update_region_access_rate(struct [damon_region](api.md#c.damon_region "damon_region") \*r, bool accessed, struct [damon_attrs](api.md#c.damon_attrs "damon_attrs") \*attrs)
:   Update the access rate of a region.

**Parameters**

`struct damon_region *r`
:   The DAMON region to update for its access check result.

`bool accessed`
:   Whether the region has accessed during last sampling interval.

`struct damon_attrs *attrs`
:   The damon_attrs of the DAMON context.

**Description**

Update the access rate of a region with the region's last sampling interval
access check result.

Usually this will be called by [`damon_operations->check_accesses`](api.md#c.damon_operations "damon_operations") callback.
