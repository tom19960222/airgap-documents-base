---
collection: ceph
version: "19.2.2"
title: "OSD Config Reference"
source_url: https://docs.ceph.com/en/squid/rados/configuration/osd-config-ref/
fetched_at: 2026-07-27T16:39:33+00:00
---
# OSD Config Reference

You can configure Ceph OSD Daemons in the Ceph configuration file (or in recent
releases, the central config store), but Ceph OSD
Daemons can use the default values and a very minimal configuration. A minimal
Ceph OSD Daemon configuration sets `host` and
uses default values for nearly everything else.

Ceph OSD Daemons are numerically identified in incremental fashion, beginning
with `0` using the following convention.

```
osd.0
osd.1
osd.2
```

In a configuration file, you may specify settings for all Ceph OSD Daemons in
the cluster by adding configuration settings to the `[osd]` section of your
configuration file. To add settings directly to a specific Ceph OSD Daemon
(e.g., `host`), enter it in an OSD-specific section of your configuration
file. For example:

```ini
[osd]
        osd_journal_size = 5120

[osd.0]
        host = osd-host-a

[osd.1]
        host = osd-host-b
```

## General Settings

The following settings provide a Ceph OSD Daemon’s ID, and determine paths to
data and journals. Ceph deployment scripts typically generate the UUID
automatically.

> **Warning:**
>
> **DO NOT** change the default paths for data or journals, as it
> makes it more problematic to troubleshoot Ceph later.

When using Filestore, the journal size should be at least twice the product of the expected drive
speed multiplied by `filestore_max_sync_interval`. However, the most common
practice is to partition the journal drive (often an SSD), and mount it such
that Ceph uses the entire partition for the journal.

osd_uuid
:   > The universally unique identifier (UUID) for the Ceph OSD Daemon.
    >
    > type:
    > :   `uuid`
    >
    > > **Note:**
    > >
    > > The `osd_uuid` applies to a single Ceph OSD Daemon. The `fsid` applies to the entire cluster.

osd_data
:   > The path to the OSDs data. You must create the directory when
    > deploying Ceph. You should mount a drive for OSD data at this mount
    > point. We do not recommend changing the default.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `/var/lib/ceph/osd/$cluster-$id`

osd_max_write_size
:   > The maximum size of a write in megabytes.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `90B`
    >
    > min:
    > :   `4`

osd_max_object_size
:   > The maximum size of a RADOS object in bytes.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `128Mi`

osd_client_message_size_cap
:   > The largest client data message allowed in memory.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `500Mi`

osd_class_dir
:   > The class path for RADOS class plug-ins.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `$libdir/rados-classes`

## File System Settings

Ceph builds and mounts file systems which are used for Ceph OSDs.

`osd_mkfs_options {fs-type}`

Description:
:   Options used when creating a new Ceph Filestore OSD of type {fs-type}.

Type:
:   String

Default for xfs:
:   `-f -i 2048`

Default for other file systems:
:   {empty string}

For example::
:   `osd_mkfs_options_xfs = -f -d agcount=24`

`osd_mount_options {fs-type}`

Description:
:   Options used when mounting a Ceph Filestore OSD of type {fs-type}.

Type:
:   String

Default for xfs:
:   `rw,noatime,inode64`

Default for other file systems:
:   `rw, noatime`

For example::
:   `osd_mount_options_xfs = rw, noatime, inode64, logbufs=8`

## Journal Settings

This section applies only to the older Filestore OSD back end. Since Luminous
BlueStore has been default and preferred.

By default, Ceph expects that you will provision a Ceph OSD Daemon’s journal at
the following path, which is usually a symlink to a device or partition:

```
/var/lib/ceph/osd/$cluster-$id/journal
```

When using a single device type (for example, spinning drives), the journals
should be *colocated*: the logical volume (or partition) should be in the same
device as the `data` logical volume.

When using a mix of fast (SSDs, NVMe) devices with slower ones (like spinning
drives) it makes sense to place the journal on the faster device, while
`data` occupies the slower device fully.

The default `osd_journal_size` value is 5120 (5 gigabytes), but it can be
larger, in which case it will need to be set in the `ceph.conf` file.
A value of 10 gigabytes is common in practice:

```
osd_journal_size = 10240
```

osd_journal
:   > The path to the OSD’s journal. This may be a path to a file or a block
    > device (such as a partition of an SSD). If it is a file, you must
    > create the directory to contain it. We recommend using a separate fast
    > device when the `osd_data` drive is an HDD.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `/var/lib/ceph/osd/$cluster-$id/journal`

osd_journal_size
:   > The size of the journal in megabytes.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `5Ki`

See [Journal Config Reference](../journal-ref.md) for additional details.

## Monitor OSD Interaction

Ceph OSD Daemons check each other’s heartbeats and report to monitors
periodically. Ceph can use default values in many cases. However, if your
network has latency issues, you may need to adopt longer intervals. See
[Configuring Monitor/OSD Interaction](../mon-osd-interaction.md) for a detailed discussion of heartbeats.

## Data Placement

See [Pool & PG Config Reference](../pool-pg-config-ref.md) for details.

## Scrubbing

One way that Ceph ensures data integrity is by “scrubbing” placement groups.
Ceph scrubbing is analogous to `fsck` on the object storage layer. Ceph
generates a catalog of all objects in each placement group and compares each
primary object to its replicas, ensuring that no objects are missing or
mismatched. Light scrubbing checks the object size and attributes, and is
usually done daily. Deep scrubbing reads the data and uses checksums to ensure
data integrity, and is usually done weekly. The freqeuncies of both light
scrubbing and deep scrubbing are determined by the cluster’s configuration,
which is fully under your control and subject to the settings explained below
in this section.

Although scrubbing is important for maintaining data integrity, it can reduce
the performance of the Ceph cluster. You can adjust the following settings to
increase or decrease the frequency and depth of scrubbing operations.

osd_max_scrubs
:   > The maximum number of simultaneous scrub operations for a Ceph OSD
    > Daemon.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `3`

osd_scrub_begin_hour
:   > This restricts scrubbing to this hour of the day or later. Use
    > `osd_scrub_begin_hour = 0` and `osd_scrub_end_hour = 0` to allow
    > scrubbing the entire day. Along with `osd_scrub_end_hour`, they
    > define a time window, in which the scrubs can happen. But a scrub will
    > be performed no matter whether the time window allows or not, as long
    > as the placement group’s scrub interval exceeds
    > `osd_scrub_max_interval`.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `0`
    >
    > allowed range:
    > :   `[0, 23]`
    >
    > see also:
    > :   [`osd_scrub_end_hour`](index.md#confval-osd_scrub_end_hour)

osd_scrub_end_hour
:   > This restricts scrubbing to the hour earlier than this. Use
    > `osd_scrub_begin_hour = 0` and `osd_scrub_end_hour = 0` to allow
    > scrubbing for the entire day. Along with `osd_scrub_begin_hour`,
    > they define a time window, in which the scrubs can happen. But a scrub
    > will be performed no matter whether the time window allows or not, as
    > long as the placement group’s scrub interval exceeds
    > `osd_scrub_max_interval`.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `0`
    >
    > allowed range:
    > :   `[0, 23]`
    >
    > see also:
    > :   [`osd_scrub_begin_hour`](index.md#confval-osd_scrub_begin_hour)

osd_scrub_begin_week_day
:   > This restricts scrubbing to this day of the week or later. 0 =
    > Sunday, 1 = Monday, etc. Use `osd_scrub_begin_week_day = 0` and
    > `osd_scrub_end_week_day = 0` to allow scrubbing for the entire week.
    > Along with `osd_scrub_end_week_day`, they define a time window in
    > which scrubs can happen. But a scrub will be performed no matter
    > whether the time window allows or not, when the PG’s scrub interval
    > exceeds `osd_scrub_max_interval`.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `0`
    >
    > allowed range:
    > :   `[0, 6]`
    >
    > see also:
    > :   [`osd_scrub_end_week_day`](index.md#confval-osd_scrub_end_week_day)

osd_scrub_end_week_day
:   > This restricts scrubbing to days of the week earlier than this. 0 =
    > Sunday, 1 = Monday, etc. Use `osd_scrub_begin_week_day = 0` and
    > `osd_scrub_end_week_day = 0` to allow scrubbing for the entire week.
    > Along with `osd_scrub_begin_week_day`, they define a time window, in
    > which the scrubs can happen. But a scrub will be performed no matter
    > whether the time window allows or not, as long as the placement
    > group’s scrub interval exceeds `osd_scrub_max_interval`.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `0`
    >
    > allowed range:
    > :   `[0, 6]`
    >
    > see also:
    > :   [`osd_scrub_begin_week_day`](index.md#confval-osd_scrub_begin_week_day)

osd_scrub_during_recovery
:   > Allow scrub during recovery. Setting this to `false` will disable
    > scheduling new scrub (and deep--scrub) while there is active recovery.
    > Already running scrubs will be continued. This might be useful to
    > reduce load on busy clusters.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`

osd_scrub_load_threshold
:   > The normalized maximum load. Ceph will not scrub when the system load
    > (as defined by `getloadavg() / number of online CPUs`) is higher
    > than this number. Default is `0.5`.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.5`

osd_scrub_min_interval
:   > The desired interval in seconds between scrubs of a specific PG when
    > the Ceph Storage Cluster load is low.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `1 day`
    >
    > see also:
    > :   [`osd_scrub_max_interval`](index.md#confval-osd_scrub_max_interval)

osd_scrub_max_interval
:   > The maximum interval in seconds for scrubbing the Ceph OSD Daemon
    > irrespective of cluster load.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `7 days`
    >
    > see also:
    > :   [`osd_scrub_min_interval`](index.md#confval-osd_scrub_min_interval)

osd_scrub_chunk_min
:   > The minimum number of objects to scrub during single operation. Also
    > serves as a minimal chunk size even after scrubbing is preempted by
    > client operations and the effective chunk size is halved.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `5`
    >
    > see also:
    > :   [`osd_scrub_chunk_max`](index.md#confval-osd_scrub_chunk_max)

osd_shallow_scrub_chunk_min
:   > The minimum number of object store chunks to scrub during single
    > operation. Not applicable to deep scrubs. Ceph blocks writes to single
    > chunk during scrub.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `50`
    >
    > see also:
    > :   [`osd_shallow_scrub_chunk_max`](index.md#confval-osd_shallow_scrub_chunk_max), [`osd_scrub_chunk_min`](index.md#confval-osd_scrub_chunk_min)

osd_scrub_chunk_max
:   > The maximum number of objects to deep-scrub during single internal
    > scrub operation. Large values would improve scrubbing performance but
    > may adversely affect client operations latency.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `15`
    >
    > see also:
    > :   [`osd_scrub_chunk_min`](index.md#confval-osd_scrub_chunk_min)

osd_shallow_scrub_chunk_max
:   > The maximum number of object store chunks to scrub during single
    > operation. Not applicable to deep scrubs.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `100`
    >
    > see also:
    > :   [`osd_shallow_scrub_chunk_min`](index.md#confval-osd_shallow_scrub_chunk_min), [`osd_scrub_chunk_max`](index.md#confval-osd_scrub_chunk_max)

osd_scrub_sleep
:   > Sleep time in seconds before scrubbing the next group of objects (the
    > next chunk). Increasing this value will slow down the overall rate of
    > scrubbing, reducing scrub impact on client operations.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.0`
    >
    > > **Note:**
    > >
    > > This setting is ignored when the mClock scheduler is used.

osd_deep_scrub_interval
:   > The interval for “deep” scrubbing (fully reading all data). The
    > `osd_scrub_load_threshold` does not affect this setting.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `7 days`

osd_scrub_interval_randomize_ratio
:   > Add a random delay to `osd_scrub_min_interval` when scheduling the
    > next scrub job for a PG. The delay is a random value less than
    > `osd_scrub_min_interval` \* `osd_scrub_interval_randomized_ratio`.
    > The default setting spreads scrubs throughout the allowed time window
    > of `[1, 1.5]` \* `osd_scrub_min_interval`.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.5`
    >
    > see also:
    > :   [`osd_scrub_min_interval`](index.md#confval-osd_scrub_min_interval)

osd_deep_scrub_stride
:   > Read size when doing a deep scrub.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `512Ki`

osd_scrub_auto_repair
:   > Setting this to `true` will enable automatic PG repair when errors
    > are found by scrubs or deep-scrubs. However, if more than
    > `osd_scrub_auto_repair_num_errors` damaged objects are found a
    > repair is NOT performed.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`

osd_scrub_auto_repair_num_errors
:   > Scrub will not perform automatic repair if more than this many damaged
    > objects are found.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `5`
    >
    > see also:
    > :   [`osd_scrub_auto_repair`](index.md#confval-osd_scrub_auto_repair)

## Operations

osd_op_num_shards
:   > The number of shards allocated for a given OSD. Each shard has its own
    > processing queue. PGs on the OSD are distributed evenly in the shard.
    > This setting overrides _ssd and _hdd if non-zero.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `0`

osd_op_num_shards_hdd
:   > the number of shards allocated for a given OSD (for rotational media).
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `1`
    >
    > see also:
    > :   [`osd_op_num_shards`](index.md#confval-osd_op_num_shards)

osd_op_num_shards_ssd
:   > the number of shards allocated for a given OSD (for solid state
    > media).
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `8`
    >
    > see also:
    > :   [`osd_op_num_shards`](index.md#confval-osd_op_num_shards)

osd_op_num_threads_per_shard
:   > The number of worker threads spawned per OSD shard for a given OSD.
    > Each worker thread when operational processes items in the shard
    > queue. This setting overrides _ssd and _hdd if non-zero.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `0`

osd_op_num_threads_per_shard_hdd
:   > The number of worker threads spawned per OSD shard for a given OSD
    > (for rotational media).
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `5`
    >
    > see also:
    > :   [`osd_op_num_threads_per_shard`](index.md#confval-osd_op_num_threads_per_shard)

osd_op_num_threads_per_shard_ssd
:   > The number of worker threads spawned per OSD shard for a given OSD
    > (for solid state media).
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `2`
    >
    > see also:
    > :   [`osd_op_num_threads_per_shard`](index.md#confval-osd_op_num_threads_per_shard)

osd_op_queue
:   > This sets the type of queue to be used for prioritizing ops within
    > each OSD. Both queues feature a strict sub-queue which is dequeued
    > before the normal queue. The normal queue is different between
    > implementations. The WeightedPriorityQueue (`wpq`) dequeues
    > operations in relation to their priorities to prevent starvation of
    > any queue. WPQ should help in cases where a few OSDs are more
    > overloaded than others. The mClockQueue (`mclock_scheduler`)
    > prioritizes operations based on which class they belong to (recovery,
    > scrub, snaptrim, client op, osd subop). See [QoS Based on mClock](index.md#qos-based-on-mclock).
    > Requires a restart.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `mclock_scheduler`
    >
    > valid choices:
    > :   - `wpq`
    >     - `mclock_scheduler`
    >     - `debug_random`
    >
    > see also:
    > :   [`osd_op_queue_cut_off`](index.md#confval-osd_op_queue_cut_off)

osd_op_queue_cut_off
:   > This selects which priority ops will be sent to the strict queue
    > verses the normal queue. The `low` setting sends all replication ops
    > and higher to the strict queue, while the `high` option sends only
    > replication acknowledgment ops and higher to the strict queue. Setting
    > this to `high` should help when a few OSDs in the cluster are very
    > busy especially when combined with `wpq` in the `osd_op_queue`
    > setting. OSDs that are very busy handling replication traffic could
    > starve primary client traffic on these OSDs without these settings.
    > Requires a restart.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `high`
    >
    > valid choices:
    > :   - `low`
    >     - `high`
    >     - `debug_random`
    >
    > see also:
    > :   [`osd_op_queue`](index.md#confval-osd_op_queue)

osd_client_op_priority
:   > The priority set for client operations. This value is relative to
    > that of `osd_recovery_op_priority` below. The default strongly
    > favors client ops over recovery.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `63`

osd_recovery_op_priority
:   > The priority of recovery operations vs client operations, if not
    > specified by the pool’s `recovery_op_priority`. The default value
    > prioritizes client ops (see above) over recovery ops. You may adjust
    > the tradeoff of client impact against the time to restore cluster
    > health by lowering this value for increased prioritization of client
    > ops, or by increasing it to favor recovery.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `3`

osd_scrub_priority
:   > The default work queue priority for scheduled scrubs when the pool
    > doesn’t specify a value of `scrub_priority`. This can be boosted to
    > the value of `osd_client_op_priority` when scrubs are blocking
    > client operations.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `5`

osd_requested_scrub_priority
:   > The priority set for user requested scrub on the work queue. If this
    > value were to be smaller than `osd_client_op_priority` it can be
    > boosted to the value of `osd_client_op_priority` when scrub is
    > blocking client operations.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `5`

osd_snap_trim_priority
:   > The priority set for the snap trim work queue.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `5`

osd_snap_trim_sleep
:   > Time in seconds to sleep before next snap trim op. Increasing this
    > value will slow down snap trimming. This option overrides backend
    > specific variants.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.0`
    >
    > > **Note:**
    > >
    > > This setting is ignored when the mClock scheduler is used.

osd_snap_trim_sleep_hdd
:   > Time in seconds to sleep before next snap trim for HDDs
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `5.0`
    >
    > > **Note:**
    > >
    > > This setting is ignored when the mClock scheduler is used.

osd_snap_trim_sleep_ssd
:   > Time in seconds to sleep before next snap trim op for SSD OSDs
    > (including NVMe).
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.0`
    >
    > > **Note:**
    > >
    > > This setting is ignored when the mClock scheduler is used.

osd_snap_trim_sleep_hybrid
:   > Time in seconds to sleep before next snap trim op when OSD data is on
    > an HDD and the OSD journal or WAL+DB is on an SSD.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `2.0`
    >
    > > **Note:**
    > >
    > > This setting is ignored when the mClock scheduler is used.

osd_op_thread_timeout
:   > The Ceph OSD Daemon operation thread timeout in seconds.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `15`

osd_op_complaint_time
:   > An operation becomes complaint worthy after the specified number of
    > seconds have elapsed.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `30.0`

osd_op_history_size
:   > The maximum number of completed operations to track.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `20`

osd_op_history_duration
:   > The oldest completed operation to track.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `600`

osd_op_log_threshold
:   > How many operations logs to display at once.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `5`

osd_op_thread_suicide_timeout
:   > type:
    > :   `int`
    >
    > default:
    > :   `150`

> **Note:**
>
> See <https://old.ceph.com/planet/dealing-with-some-osd-timeouts/> for
> more on `osd_op_thread_suicide_timeout`. Be aware that this is a link to a
> reworking of a blog post from 2017, and that its conclusion will direct you
> back to this page “for more information”.

### QoS Based on mClock

Ceph’s use of mClock is now more refined and can be used by following the
steps as described in [mClock Config Reference](../mclock-config-ref.md).

#### Core Concepts

Ceph’s QoS support is implemented using a queueing scheduler
based on [the dmClock algorithm](https://www.usenix.org/legacy/event/osdi10/tech/full_papers/Gulati.pdf). This algorithm allocates the I/O
resources of the Ceph cluster in proportion to weights, and enforces
the constraints of minimum reservation and maximum limitation, so that
the services can compete for the resources fairly. Currently the
*mclock_scheduler* operation queue divides Ceph services involving I/O
resources into following buckets:

- client op: the iops issued by client
- osd subop: the iops issued by primary OSD
- snap trim: the snap trimming related requests
- pg recovery: the recovery related requests
- pg scrub: the scrub related requests

And the resources are partitioned using following three sets of tags. In other
words, the share of each type of service is controlled by three tags:

1. reservation: the minimum IOPS allocated for the service.
2. limitation: the maximum IOPS allocated for the service.
3. weight: the proportional share of capacity if extra capacity or system
   oversubscribed.

In Ceph, operations are graded with “cost”. And the resources allocated
for serving various services are consumed by these “costs”. So, for
example, the more reservation a services has, the more resource it is
guaranteed to possess, as long as it requires. Assuming there are 2
services: recovery and client ops:

- recovery: (r:1, l:5, w:1)
- client ops: (r:2, l:0, w:9)

The settings above ensure that the recovery won’t get more than 5
requests per second serviced, even if it requires so (see CURRENT
IMPLEMENTATION NOTE below), and no other services are competing with
it. But if the clients start to issue large amount of I/O requests,
neither will they exhaust all the I/O resources. 1 request per second
is always allocated for recovery jobs as long as there are any such
requests. So the recovery jobs won’t be starved even in a cluster with
high load. And in the meantime, the client ops can enjoy a larger
portion of the I/O resource, because its weight is “9”, while its
competitor “1”. In the case of client ops, it is not clamped by the
limit setting, so it can make use of all the resources if there is no
recovery ongoing.

CURRENT IMPLEMENTATION NOTE: the current implementation enforces the limit
values. Therefore, if a service crosses the enforced limit, the op remains
in the operation queue until the limit is restored.

#### Subtleties of mClock

The reservation and limit values have a unit of requests per
second. The weight, however, does not technically have a unit and the
weights are relative to one another. So if one class of requests has a
weight of 1 and another a weight of 9, then the latter class of
requests should get 9 executed at a 9 to 1 ratio as the first class.
However that will only happen once the reservations are met and those
values include the operations executed under the reservation phase.

Even though the weights do not have units, one must be careful in
choosing their values due how the algorithm assigns weight tags to
requests. If the weight is *W*, then for a given class of requests,
the next one that comes in will have a weight tag of *1/W* plus the
previous weight tag or the current time, whichever is larger. That
means if *W* is sufficiently large and therefore *1/W* is sufficiently
small, the calculated tag may never be assigned as it will get a value
of the current time. The ultimate lesson is that values for weight
should not be too large. They should be under the number of requests
one expects to be serviced each second.

#### Caveats

There are some factors that can reduce the impact of the mClock op
queues within Ceph. First, requests to an OSD are sharded by their
placement group identifier. Each shard has its own mClock queue and
these queues neither interact nor share information among them. The
number of shards can be controlled with the configuration options
[`osd_op_num_shards`](index.md#confval-osd_op_num_shards), [`osd_op_num_shards_hdd`](index.md#confval-osd_op_num_shards_hdd), and
[`osd_op_num_shards_ssd`](index.md#confval-osd_op_num_shards_ssd). A lower number of shards will increase the
impact of the mClock queues, but may have other deleterious effects.
This is especially the case if there are insufficient shard worker
threads. The number of shard worker threads can be controlled with the
configuration options [`osd_op_num_threads_per_shard`](index.md#confval-osd_op_num_threads_per_shard),
[`osd_op_num_threads_per_shard_hdd`](index.md#confval-osd_op_num_threads_per_shard_hdd) and
[`osd_op_num_threads_per_shard_ssd`](index.md#confval-osd_op_num_threads_per_shard_ssd).

Second, requests are transferred from the operation queue to the
operation sequencer, in which they go through the phases of
execution. The operation queue is where mClock resides and mClock
determines the next op to transfer to the operation sequencer. The
number of operations allowed in the operation sequencer is a complex
issue. In general we want to keep enough operations in the sequencer
so it’s always getting work done on some operations while it’s waiting
for disk and network access to complete on other operations. On the
other hand, once an operation is transferred to the operation
sequencer, mClock no longer has control over it. Therefore to maximize
the impact of mClock, we want to keep as few operations in the
operation sequencer as possible. So we have an inherent tension.

The configuration options that influence the number of operations in
the operation sequencer are [`bluestore_throttle_bytes`](../bluestore-config-ref/index.md#confval-bluestore_throttle_bytes),
[`bluestore_throttle_deferred_bytes`](../bluestore-config-ref/index.md#confval-bluestore_throttle_deferred_bytes),
[`bluestore_throttle_cost_per_io`](../bluestore-config-ref/index.md#confval-bluestore_throttle_cost_per_io),
[`bluestore_throttle_cost_per_io_hdd`](../bluestore-config-ref/index.md#confval-bluestore_throttle_cost_per_io_hdd), and
[`bluestore_throttle_cost_per_io_ssd`](../bluestore-config-ref/index.md#confval-bluestore_throttle_cost_per_io_ssd).

A third factor that affects the impact of the mClock algorithm is that
we’re using a distributed system, where requests are made to multiple
OSDs and each OSD has (can have) multiple shards. Yet we’re currently
using the mClock algorithm, which is not distributed (note: dmClock is
the distributed version of mClock).

Various organizations and individuals are currently experimenting with
mClock as it exists in this code base along with their modifications
to the code base. We hope you’ll share you’re experiences with your
mClock and dmClock experiments on the `ceph-devel` mailing list.

osd_async_recovery_min_cost
:   > A mixture measure of number of current log entries difference and
    > historical missing objects, above which we switch to use asynchronous
    > recovery when appropriate
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `100`

osd_push_per_object_cost
:   > the overhead for serving a push op
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `1000B`

osd_mclock_scheduler_client_res
:   > IO proportion reserved for each client (default).
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.0`
    >
    > allowed range:
    > :   `[0, 1.0]`
    >
    > see also:
    > :   [`osd_op_queue`](index.md#confval-osd_op_queue)

osd_mclock_scheduler_client_wgt
:   > IO share for each client (default) over reservation.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `1`
    >
    > see also:
    > :   [`osd_op_queue`](index.md#confval-osd_op_queue)

osd_mclock_scheduler_client_lim
:   > IO limit for each client (default) over reservation.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.0`
    >
    > allowed range:
    > :   `[0, 1.0]`
    >
    > see also:
    > :   [`osd_op_queue`](index.md#confval-osd_op_queue)

osd_mclock_scheduler_background_recovery_res
:   > IO proportion reserved for background recovery (default).
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.0`
    >
    > allowed range:
    > :   `[0, 1.0]`
    >
    > see also:
    > :   [`osd_op_queue`](index.md#confval-osd_op_queue)

osd_mclock_scheduler_background_recovery_wgt
:   > IO share for each background recovery over reservation.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `1`
    >
    > see also:
    > :   [`osd_op_queue`](index.md#confval-osd_op_queue)

osd_mclock_scheduler_background_recovery_lim
:   > IO limit for background recovery over reservation.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.0`
    >
    > allowed range:
    > :   `[0, 1.0]`
    >
    > see also:
    > :   [`osd_op_queue`](index.md#confval-osd_op_queue)

osd_mclock_scheduler_background_best_effort_res
:   > IO proportion reserved for background best_effort (default).
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.0`
    >
    > allowed range:
    > :   `[0, 1.0]`
    >
    > see also:
    > :   [`osd_op_queue`](index.md#confval-osd_op_queue)

osd_mclock_scheduler_background_best_effort_wgt
:   > IO share for each background best_effort over reservation.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `1`
    >
    > see also:
    > :   [`osd_op_queue`](index.md#confval-osd_op_queue)

osd_mclock_scheduler_background_best_effort_lim
:   > IO limit for background best_effort over reservation.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.0`
    >
    > allowed range:
    > :   `[0, 1.0]`
    >
    > see also:
    > :   [`osd_op_queue`](index.md#confval-osd_op_queue)

## Backfilling

When you add or remove Ceph OSD Daemons to a cluster, CRUSH will
rebalance the cluster by moving placement groups to or from Ceph OSDs
to restore balanced utilization. The process of migrating placement groups and
the objects they contain can reduce the cluster’s operational performance
considerably. To maintain operational performance, Ceph performs this migration
with ‘backfilling’, which allows Ceph to set backfill operations to a lower
priority than requests to read or write data.

> **Note:**
>
> Some of these settings are automatically reset if the [mClock](../mclock-config-ref.md)
> scheduler is active, see [mClock backfill](../mclock-config-ref.md#recovery-backfill-options).

osd_max_backfills
:   > The maximum number of backfills allowed to or from a single OSD. Note
    > that this is applied separately for read and write operations. This
    > setting is automatically reset when the mClock scheduler is used.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `1`
    >
    > see also:
    > :   [`osd_mclock_override_recovery_settings`](../mclock-config-ref/index.md#confval-osd_mclock_override_recovery_settings)

osd_backfill_scan_min
:   > The minimum number of objects per backfill scan.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `64`

osd_backfill_scan_max
:   > The maximum number of objects per backfill scan.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `512`

osd_backfill_retry_interval
:   > The number of seconds to wait before retrying backfill requests.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `30.0`

## OSD Map

OSD maps reflect the OSD daemons operating in the cluster. Over time, the
number of map epochs increases. Ceph provides some settings to ensure that
Ceph performs well as the OSD map grows larger.

osd_map_dedup
:   > Enable removing duplicates in the OSD map.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`

osd_map_cache_size
:   > The number of OSD maps to keep cached.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `50`

osd_map_message_max
:   > The maximum map entries allowed per MOSDMap message.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `40`

## Recovery

When the cluster starts or when a Ceph OSD Daemon crashes and restarts, the OSD
begins peering with other Ceph OSD Daemons before writes can occur. See
[Monitoring OSDs and PGs](../../operations/monitoring-osd-pg.md#peering) for details.

If a Ceph OSD Daemon crashes and comes back online, usually it will be out of
sync with other Ceph OSD Daemons containing more recent versions of objects in
the placement groups. When this happens, the Ceph OSD Daemon goes into recovery
mode and seeks to get the latest copy of the data and bring its map back up to
date. Depending upon how long the Ceph OSD Daemon was down, the OSD’s objects
and placement groups may be significantly out of date. Also, if a failure domain
went down (e.g., a rack), more than one Ceph OSD Daemon may come back online at
the same time. This can make the recovery process time consuming and resource
intensive.

To maintain operational performance, Ceph performs recovery with limitations on
the number recovery requests, threads and object chunk sizes which allows Ceph
perform well in a degraded state.

> **Note:**
>
> Some of these settings are automatically reset if the [mClock](../mclock-config-ref.md)
> scheduler is active, see [mClock backfill](../mclock-config-ref.md#recovery-backfill-options).

osd_recovery_delay_start
:   > After peering completes, Ceph will delay for the specified number of
    > seconds before starting to recover RADOS objects.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.0`

osd_recovery_max_active
:   > The number of active recovery requests per OSD at one time. More
    > requests will accelerate recovery, but the requests places an
    > increased load on the cluster.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `0`
    >
    > see also:
    > :   [`osd_recovery_max_active_hdd`](index.md#confval-osd_recovery_max_active_hdd), [`osd_recovery_max_active_ssd`](index.md#confval-osd_recovery_max_active_ssd), [`osd_mclock_override_recovery_settings`](../mclock-config-ref/index.md#confval-osd_mclock_override_recovery_settings)
    >
    > > **Note:**
    > >
    > > This value is only used if it is non-zero. Normally it is `0`, which means that the `hdd` or `ssd` values (below) are used, depending on the type of the primary device backing the OSD. This setting is automatically reset when the mClock scheduler is used.

osd_recovery_max_active_hdd
:   > The number of active recovery requests per OSD at one time, if the
    > primary device is rotational.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `3`
    >
    > see also:
    > :   [`osd_recovery_max_active`](index.md#confval-osd_recovery_max_active), [`osd_recovery_max_active_ssd`](index.md#confval-osd_recovery_max_active_ssd), [`osd_mclock_override_recovery_settings`](../mclock-config-ref/index.md#confval-osd_mclock_override_recovery_settings)
    >
    > > **Note:**
    > >
    > > This setting is automatically reset when the mClock scheduler is used.

osd_recovery_max_active_ssd
:   > The number of active recovery requests per OSD at one time, if the
    > primary device is non-rotational (i.e., an SSD).
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `10`
    >
    > see also:
    > :   [`osd_recovery_max_active`](index.md#confval-osd_recovery_max_active), [`osd_recovery_max_active_hdd`](index.md#confval-osd_recovery_max_active_hdd), [`osd_mclock_override_recovery_settings`](../mclock-config-ref/index.md#confval-osd_mclock_override_recovery_settings)
    >
    > > **Note:**
    > >
    > > This setting is automatically reset when the mClock scheduler is used.

osd_recovery_max_chunk
:   > the maximum total size of data chunks a recovery op can carry.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `8Mi`

osd_recovery_max_single_start
:   > The maximum number of recovery operations per OSD that will be newly
    > started when an OSD is recovering.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `1`

osd_recover_clone_overlap
:   > Preserves clone overlap during recovery. Should always be set to
    > `true`.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`

osd_recovery_sleep
:   > Time in seconds to sleep before the next recovery or backfill op.
    > Increasing this value will slow down recovery operation while client
    > operations will be less impacted.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.0`
    >
    > > **Note:**
    > >
    > > This setting is ignored when the mClock scheduler is used.

osd_recovery_sleep_hdd
:   > Time in seconds to sleep before next recovery or backfill op for HDDs.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.1`
    >
    > > **Note:**
    > >
    > > This setting is ignored when the mClock scheduler is used.

osd_recovery_sleep_ssd
:   > Time in seconds to sleep before the next recovery or backfill op for
    > SSDs.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.0`
    >
    > see also:
    > :   [`osd_recovery_sleep`](index.md#confval-osd_recovery_sleep)
    >
    > > **Note:**
    > >
    > > This setting is ignored when the mClock scheduler is used.

osd_recovery_sleep_hybrid
:   > Time in seconds to sleep before the next recovery or backfill op when
    > OSD data is on HDD and OSD journal / WAL+DB is on SSD.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.025`
    >
    > see also:
    > :   [`osd_recovery_sleep`](index.md#confval-osd_recovery_sleep)
    >
    > > **Note:**
    > >
    > > This setting is ignored when the mClock scheduler is used.

osd_recovery_sleep_degraded
:   > Time in seconds to sleep before the next recovery or backfill op when
    > PGs are degraded. Increasing this value will slow down recovery ops
    > while client ops will be less impacted.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.0`

osd_recovery_sleep_degraded_hdd
:   > Time in seconds to sleep before next recovery or backfill op for HDDs
    > when PGs are degraded.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.1`

osd_recovery_sleep_degraded_ssd
:   > Time in seconds to sleep before the next recovery or backfill op for
    > SSDs when PGs are degraded.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.0`
    >
    > see also:
    > :   [`osd_recovery_sleep_degraded`](index.md#confval-osd_recovery_sleep_degraded)

osd_recovery_sleep_degraded_hybrid
:   > Time in seconds to sleep before the next recovery or backfill op when
    > PGs are degraded and OSD data is on HDD and OSD journal / WAL+DB is on
    > SSD.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.025`
    >
    > see also:
    > :   [`osd_recovery_sleep_degraded`](index.md#confval-osd_recovery_sleep_degraded)

osd_recovery_priority
:   > The default priority set for recovery work queue. Not related to a
    > pool’s `recovery_priority`.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `5`

## Tiering

osd_agent_max_ops
:   > The maximum number of simultaneous flushing ops per tiering agent in
    > the high speed mode.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `4`

osd_agent_max_low_ops
:   > The maximum number of simultaneous flushing ops per tiering agent in
    > the low speed mode.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `2`

See [cache target dirty high ratio](../../operations/pools.md#cache-target-dirty-high-ratio) for when the tiering agent flushes dirty
objects within the high speed mode.

## Miscellaneous

osd_default_notify_timeout
:   > The OSD default notification timeout (in seconds).
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `30`

osd_check_for_log_corruption
:   > Check log files for corruption. Can be computationally expensive.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`

osd_delete_sleep
:   > Time in seconds to sleep before the next removal transaction. This
    > throttles the PG deletion process.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.0`
    >
    > > **Note:**
    > >
    > > This setting is ignored when the mClock scheduler is used.

osd_delete_sleep_hdd
:   > Time in seconds to sleep before next removal transaction for HDDs.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `5.0`
    >
    > > **Note:**
    > >
    > > This setting is ignored when the mClock scheduler is used.

osd_delete_sleep_ssd
:   > Time in seconds to sleep before next removal transaction for SSDs
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `1.0`
    >
    > > **Note:**
    > >
    > > This setting is ignored when the mClock scheduler is used.

osd_delete_sleep_hybrid
:   > Time in seconds to sleep before next removal transaction when OSD data
    > is on HDD and OSD journal or WAL+DB is on SSD
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `1.0`
    >
    > > **Note:**
    > >
    > > This setting is ignored when the mClock scheduler is used.

osd_command_max_records
:   > Limits the number of lost objects to return.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `256`

osd_fast_fail_on_connection_refused
:   > If this option is enabled, crashed OSDs are marked down immediately by
    > connected peers and MONs (assuming that the crashed OSD host
    > survives). Disable it to restore old behavior, at the expense of
    > possible long I/O stalls when OSDs crash in the middle of I/O
    > operations.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
