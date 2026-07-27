---
collection: ceph
version: "19.2.2"
title: "Pool, PG and CRUSH Config Reference"
source_url: https://docs.ceph.com/en/squid/rados/configuration/pool-pg-config-ref/
fetched_at: 2026-07-27T16:39:36+00:00
---
# Pool, PG and CRUSH Config Reference

The number of placement groups that the CRUSH algorithm assigns to each pool is
determined by the values of variables in the centralized configuration database
in the monitor cluster.

Both containerized deployments of Ceph (deployments made using `cephadm` or
Rook) and non-containerized deployments of Ceph rely on the values in the
central configuration database in the monitor cluster to assign placement
groups to pools.

## Example Commands

To see the value of the variable that governs the number of placement groups in a given pool, run a command of the following form:

```
ceph config get osd osd_pool_default_pg_num
```

To set the value of the variable that governs the number of placement groups in a given pool, run a command of the following form:

```
ceph config set osd osd_pool_default_pg_num
```

## Manual Tuning

In some cases, it might be advisable to override some of the defaults. For
example, you might determine that it is wise to set a pool’s replica size and
to override the default number of placement groups in the pool. You can set
these values when running [pool](../../operations/pools.md) commands.

## See Also

See [Autoscaling placement groups](../../operations/placement-groups/index.md#pg-autoscaler).

```ini
[global]

	# By default, Ceph makes three replicas of RADOS objects. If you want
	# to maintain four copies of an object the default value--a primary
	# copy and three replica copies--reset the default values as shown in
	# 'osd_pool_default_size'. If you want to allow Ceph to accept an I/O
	# operation to a degraded PG, set 'osd_pool_default_min_size' to a
	# number less than the 'osd_pool_default_size' value.

	osd_pool_default_size = 3  # Write an object three times.
	osd_pool_default_min_size = 2 # Accept an I/O operation to a PG that has two copies of an object.

	# Note: by default, PG autoscaling is enabled and this value is used only
	# in specific circumstances. It is however still recommend to set it.
	# Ensure you have a realistic number of placement groups. We recommend
	# approximately 100 per OSD. E.g., total number of OSDs multiplied by 100
	# divided by the number of replicas (i.e., 'osd_pool_default_size'). So for
	# 10 OSDs and 'osd_pool_default_size' = 4, we'd recommend approximately
	# (100 * 10) / 4 = 250.
	# Always use the nearest power of two.
	osd_pool_default_pg_num = 256
```

mon_max_pool_pg_num
:   > The maximum number of placement groups per pool.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `64Ki`

mon_pg_stuck_threshold
:   > Number of seconds after which PGs can be considered as being stuck.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `1 minute`

mon_pg_warn_min_per_osd
:   > Raise `HEALTH_WARN` if the average number of PGs per `in` OSD is
    > under this number. A non-positive number disables this.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `0`

mon_pg_warn_min_objects
:   > Do not warn if the total number of RADOS objects in cluster is below
    > this number
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `10000`

mon_pg_warn_min_pool_objects
:   > Do not warn on pools whose RADOS object count is below this number
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `1000`

mon_pg_check_down_all_threshold
:   > Percentage threshold of `down` OSDs above which we check all PGs for
    > stale ones.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.5`

mon_pg_warn_max_object_skew
:   > Raise `HEALTH_WARN` if the average RADOS object count per PG of any
    > pool is greater than `mon_pg_warn_max_object_skew` times the average
    > RADOS object count per PG of all pools. Zero or a non-positive number
    > disables this. Note that this option applies to `ceph-mgr` daemons.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `10.0`

mon_delta_reset_interval
:   > Seconds of inactivity before we reset the PG delta to 0. We keep track
    > of the delta of the used space of each pool, so, for example, it would
    > be easier for us to understand the progress of recovery or the
    > performance of cache tier. But if there’s no activity reported for a
    > certain pool, we just reset the history of deltas of that pool.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `10.0`

osd_crush_chooseleaf_type
:   > The bucket type to use for `chooseleaf` in a CRUSH rule. Uses
    > ordinal rank rather than name.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `1`

osd_crush_initial_weight
:   > The initial CRUSH weight for newly added OSDs. The default value of
    > this option is `the size of a newly added OSD in TB`. By default,
    > the initial CRUSH weight for a newly added OSD is set to its device
    > size in TB. See [Weighting Bucket Items](../../operations/crush-map.md#weightingbucketitems) for details.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `-1.0`

osd_pool_default_crush_rule
:   > The default CRUSH rule to use when creating a replicated pool. The
    > default value of `-1` means “pick the rule with the lowest numerical
    > ID and use that”. This is to make pool creation work in the absence
    > of rule 0.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `-1`

osd_pool_erasure_code_stripe_unit
:   > Sets the default size, in bytes, of a chunk of an object stripe for
    > erasure coded pools. Every object of size S will be stored as N
    > stripes, with each data chunk receiving `stripe unit` bytes. Each
    > stripe of `N * stripe unit` bytes will be encoded/decoded
    > individually. This option can is overridden by the `stripe_unit`
    > setting in an erasure code profile.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `4Ki`

osd_pool_default_size
:   > Sets the number of replicas for objects in the pool. The default value
    > is the same as `ceph osd pool set {pool-name} size {size}`.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `3`
    >
    > allowed range:
    > :   `[0, 10]`

osd_pool_default_min_size
:   > Sets the minimum number of written replicas for objects in the pool in
    > order to acknowledge an I/O operation to the client. If minimum is
    > not met, Ceph will not acknowledge the I/O to the client, **which may
    > result in data loss**. This setting ensures a minimum number of
    > replicas when operating in `degraded` mode. The default value is
    > `0` which means no particular minimum. If `0`, minimum is `size -
    > (size / 2)`.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `0`
    >
    > allowed range:
    > :   `[0, 255]`
    >
    > see also:
    > :   [`osd_pool_default_size`](index.md#confval-osd_pool_default_size)

osd_pool_default_pg_num
:   > The default number of placement groups for a pool. The default value
    > is the same as `pg_num` with `mkpool`.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `32`
    >
    > see also:
    > :   [`osd_pool_default_pg_autoscale_mode`](index.md#confval-osd_pool_default_pg_autoscale_mode)

osd_pool_default_pgp_num
:   > The default number of placement groups for placement for a pool.
    > The default value is the same as `pgp_num` with `mkpool`.
    > PG and PGP should be equal (for now). Note: should not be set unless
    > autoscaling is disabled.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `0`
    >
    > see also:
    > :   [`osd_pool_default_pg_num`](index.md#confval-osd_pool_default_pg_num), [`osd_pool_default_pg_autoscale_mode`](index.md#confval-osd_pool_default_pg_autoscale_mode)

osd_pool_default_pg_autoscale_mode
:   > With default value on, the autoscaler starts a new pool with 1 pg,
    > unless the user specifies the pg_num.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `on`
    >
    > valid choices:
    > :   - `off`
    >     - `warn`
    >     - `on`

osd_pool_default_flags
:   > The default flags for new pools.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `0`

osd_max_pgls
:   > The maximum number of placement groups to list. A client requesting a
    > large number can tie up the Ceph OSD Daemon.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `1Ki`

osd_min_pg_log_entries
:   > The minimum number of placement group logs to maintain when trimming
    > log files.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `250`
    >
    > see also:
    > :   [`osd_max_pg_log_entries`](index.md#confval-osd_max_pg_log_entries), `osd_pg_log_dups_tracked`, `osd_target_pg_log_entries_per_osd`

osd_max_pg_log_entries
:   > The maximum number of placement group logs to maintain when trimming
    > log files.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `10000`
    >
    > see also:
    > :   [`osd_min_pg_log_entries`](index.md#confval-osd_min_pg_log_entries), `osd_pg_log_dups_tracked`, `osd_target_pg_log_entries_per_osd`

osd_default_data_pool_replay_window
:   > The time (in seconds) for an OSD to wait for a client to replay a
    > request.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `45`

osd_max_pg_per_osd_hard_ratio
:   > The ratio of number of PGs per OSD allowed by the cluster before the
    > OSD refuses to create new PGs. An OSD stops creating new PGs if the
    > number of PGs it serves exceeds `osd_max_pg_per_osd_hard_ratio` \*
    > `mon_max_pg_per_osd`.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `3.0`
    >
    > min:
    > :   `1`
    >
    > see also:
    > :   `mon_max_pg_per_osd`

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
