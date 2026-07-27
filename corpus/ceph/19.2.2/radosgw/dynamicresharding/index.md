---
collection: ceph
version: "19.2.2"
title: "RGW Dynamic Bucket Index Resharding"
source_url: https://docs.ceph.com/en/squid/radosgw/dynamicresharding/
fetched_at: 2026-07-27T16:40:39+00:00
---
# RGW Dynamic Bucket Index Resharding

New in version Luminous.

A large bucket index can lead to performance problems, which can
be addressed by sharding bucket indexes.
Until Luminous, changing the number of bucket shards (resharding)
needed to be done offline, with RGW services disabled.
Since the Luminous release Ceph has supported online bucket resharding.

Each bucket index shard can handle its entries efficiently up until
reaching a certain threshold. If this threshold is
exceeded the system can suffer from performance issues. The dynamic
resharding feature detects this situation and automatically increases
the number of shards used by a bucket’s index, resulting in a
reduction of the number of entries in each shard. This
process is transparent to the user. Writes to the target bucket
are blocked (but reads are not) briefly during resharding process.

By default dynamic bucket index resharding can only increase the
number of bucket index shards to 1999, although this upper-bound is a
configuration parameter (see [Configuration](index.md#configuration) below). When
possible, the process chooses a prime number of shards in order to
spread the number of entries across the bucket index
shards more evenly.

Detection of resharding opportunities runs as a background process
that periodically
scans all buckets. A bucket that requires resharding is added to
a queue. A thread runs in the background and processes the queueued
resharding tasks, one at a time and in order.

## Multisite

With Ceph releases prior to Reef, the Ceph Object Gateway (RGW) does not support
dynamic resharding in a
multisite deployment. For information on dynamic resharding, see
[Resharding](../zone-features/index.md#feature-resharding) in the RGW multisite documentation.

## Configuration

rgw_dynamic_resharding
:   > If true, RGW will dynamically increase the number of shards in buckets
    > that have a high number of objects per shard.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`
    >
    > see also:
    > :   [`rgw_max_objs_per_shard`](index.md#confval-rgw_max_objs_per_shard), [`rgw_max_dynamic_shards`](index.md#confval-rgw_max_dynamic_shards)

rgw_max_objs_per_shard
:   > This is the max number of objects per bucket index shard that RGW will
    > allow with dynamic resharding. RGW will trigger an automatic reshard
    > operation on the bucket if it exceeds this number.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `100000`
    >
    > see also:
    > :   [`rgw_dynamic_resharding`](index.md#confval-rgw_dynamic_resharding), [`rgw_max_dynamic_shards`](index.md#confval-rgw_max_dynamic_shards)

rgw_max_dynamic_shards
:   > This is the maximum number of bucket index shards that dynamic
    > sharding is able to create on its own. This does not limit user
    > requested resharding. Ideally this value is a prime number.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `1999`
    >
    > min:
    > :   `1`
    >
    > see also:
    > :   [`rgw_dynamic_resharding`](index.md#confval-rgw_dynamic_resharding), [`rgw_max_objs_per_shard`](index.md#confval-rgw_max_objs_per_shard)

rgw_reshard_bucket_lock_duration
:   > Number of seconds the timeout on the reshard locks (bucket reshard
    > lock and reshard log lock) are set to. As a reshard proceeds these
    > locks can be renewed/extended. If too short, reshards cannot complete
    > and will fail, causing a future reshard attempt. If too long a hung or
    > crashed reshard attempt will keep the bucket locked for an extended
    > period, not allowing RGW to detect the failed reshard attempt and
    > recover.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `360`
    >
    > min:
    > :   `30`

rgw_reshard_thread_interval
:   > Number of seconds between processing of reshard log entries
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `600`
    >
    > min:
    > :   `10`

rgw_reshard_num_logs
:   > type:
    > :   `uint`
    >
    > default:
    > :   `16`
    >
    > min:
    > :   `1`

## Admin Commands

### Add a Bucket to the Resharding Queue

```
radosgw-admin reshard add --bucket <bucket_name> --num-shards <new number of shards>
```

### List Resharding Queue

```
radosgw-admin reshard list
```

### Process Tasks on the Resharding Queue

```
radosgw-admin reshard process
```

### Bucket Resharding Status

```
radosgw-admin reshard status --bucket <bucket_name>
```

The output is a JSON array of 3 properties (`reshard_status`, `new_bucket_instance_id`, `num_shards`) per shard.

For example, the output at each dynamic resharding stage is shown below:

1. Before resharding occurred:

   ```
   [
       {
           "reshard_status": "not-resharding",
           "new_bucket_instance_id": "",
           "num_shards": -1
       }
   ]
   ```
2. During resharding:

   ```
   [
       {
           "reshard_status": "in-progress",
           "new_bucket_instance_id": "1179f470-2ebf-4630-8ec3-c9922da887fd.8652.1",
           "num_shards": 2
       },
       {
           "reshard_status": "in-progress",
           "new_bucket_instance_id": "1179f470-2ebf-4630-8ec3-c9922da887fd.8652.1",
           "num_shards": 2
       }
   ]
   ```
3. After resharding completed:

   ```
   [
       {
           "reshard_status": "not-resharding",
           "new_bucket_instance_id": "",
           "num_shards": -1
       },
       {
           "reshard_status": "not-resharding",
           "new_bucket_instance_id": "",
           "num_shards": -1
       }
   ]
   ```

### Cancel Pending Bucket Resharding

> **Note:**
>
> Bucket resharding tasks cannot be canceled once they transition to
> the `in-progress` state from the initial `not-resharding` state.

```
radosgw-admin reshard cancel --bucket <bucket_name>
```

### Manual Immediate Bucket Resharding

```
radosgw-admin bucket reshard --bucket <bucket_name> --num-shards <new number of shards>
```

When choosing a number of shards, the administrator must anticipate each
bucket’s peak number of objects. Ideally one should aim for no
more than 100000 entries per shard at any given time.

Additionally, bucket index shards that are prime numbers are more effective
in evenly distributing bucket index entries.
For example, 7001 bucket index shards is better than 7000
since the former is prime. A variety of web sites have lists of prime
numbers; search for “list of prime numbers” with your favorite
search engine to locate some web sites.

### Setting a Bucket’s Minimum Number of Shards

```
radosgw-admin bucket set-min-shards --bucket <bucket_name> --num-shards <min number of shards>
```

Since dynamic resharding can now reduce the number of shards,
administrators may want to prevent the number of shards from becoming
too low, for example if the expect the number of objects to increase
in the future. This command allows administrators to set a per-bucket
minimum. This does not, however, prevent administrators from manually
resharding to a lower number of shards.

## Troubleshooting

Clusters prior to Luminous 12.2.11 and Mimic 13.2.5 left behind stale bucket
instance entries, which were not automatically cleaned up. This issue also affected
lifecycle policies, which were no longer applied to resharded buckets. Both of
these issues can be remediated by running `radosgw-admin` commands.

### Stale Instance Management

List the stale instances in a cluster that may be cleaned up:

```
radosgw-admin reshard stale-instances list
```

Clean up the stale instances in a cluster:

```
radosgw-admin reshard stale-instances delete
```

> **Note:**
>
> Cleanup of stale instances should not be done in a multisite deployment.

### Lifecycle Fixes

For clusters with resharded instances, it is highly likely that the old
lifecycle processes would have flagged and deleted lifecycle processing as the
bucket instance changed during a reshard. While this is fixed for buckets
deployed on newer Ceph releases (from Mimic 13.2.6 and Luminous 12.2.12),
older buckets that had lifecycle policies and that have undergone
resharding must be fixed manually.

The command to do so is:

```
radosgw-admin lc reshard fix --bucket {bucketname}
```

If the `--bucket` argument is not provided, this
command will try to fix lifecycle policies for all the buckets in the cluster.

### Object Expirer Fixes

Objects subject to Swift object expiration on older clusters may have
been dropped from the log pool and never deleted after the bucket was
resharded. This would happen if their expiration time was before the
cluster was upgraded, but if their expiration was after the upgrade
the objects would be correctly handled. To manage these expire-stale
objects, `radosgw-admin` provides two subcommands.

Listing:

```
radosgw-admin objects expire-stale list --bucket {bucketname}
```

Displays a list of object names and expiration times in JSON format.

Deleting:

```
radosgw-admin objects expire-stale rm --bucket {bucketname}
```

Initiates deletion of such objects, displaying a list of object names, expiration times, and deletion status in JSON format.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
