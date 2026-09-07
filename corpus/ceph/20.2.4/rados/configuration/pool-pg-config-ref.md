---
collection: ceph
version: "20.2.4"
title: "Pool, PG and CRUSH Config Reference"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/rados/configuration/pool-pg-config-ref.rst
fetched_at: 2026-08-18T01:32:45Z
---
<a id="rados-config-pool-pg-crush-ref"></a>

# Pool, PG and CRUSH Config Reference

.. index:: pools; configuration

The number of placement groups that the CRUSH algorithm assigns to each pool is
determined by the values of variables in the centralized configuration database
in the monitor cluster.

Both containerized deployments of Ceph (deployments made using ``cephadm`` or
Rook) and non-containerized deployments of Ceph rely on the values in the
central configuration database in the monitor cluster to assign placement
groups to pools.

## Example Commands

To see the value of the variable that governs the number of placement groups in a given pool, run a command of the following form:

```bash
ceph config get osd osd_pool_default_pg_num
```

To set the value of the variable that governs the number of placement groups in a given pool, run a command of the following form:

```bash
ceph config set osd osd_pool_default_pg_num
```

## Manual Tuning
In some cases, it might be advisable to override some of the defaults. For
example, you might determine that it is wise to set a pool's replica size and
to override the default number of placement groups in the pool. You can set
these values when running [pool](../operations/pools.md) commands.

## See Also

See [pg-autoscaler](../operations/placement-groups.md#pg-autoscaler).

Included file `doc/rados/configuration/pool-pg.conf`:

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

.. confval:: mon_max_pool_pg_num

.. confval:: mon_pg_stuck_threshold

.. confval:: mon_pg_warn_min_per_osd

.. confval:: mon_pg_warn_min_objects

.. confval:: mon_pg_warn_min_pool_objects

.. confval:: mon_pg_check_down_all_threshold

.. confval:: mon_pg_warn_max_object_skew

.. confval:: mon_delta_reset_interval

.. confval:: osd_crush_chooseleaf_type

.. confval:: osd_crush_initial_weight

.. confval:: osd_pool_default_crush_rule

.. confval:: osd_pool_erasure_code_stripe_unit

.. confval:: osd_pool_default_size

.. confval:: osd_pool_default_min_size

.. confval:: osd_pool_default_pg_num

.. confval:: osd_pool_default_pgp_num

.. confval:: osd_pool_default_pg_autoscale_mode

.. confval:: osd_pool_default_flags

.. confval:: osd_max_pgls

.. confval:: osd_min_pg_log_entries

.. confval:: osd_max_pg_log_entries

.. confval:: osd_default_data_pool_replay_window

.. confval:: osd_max_pg_per_osd_hard_ratio

.. confval:: osd_pool_default_flag_ec_optimizations
