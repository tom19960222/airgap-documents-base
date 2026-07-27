---
collection: ceph
version: "19.2.2"
title: "Client Configuration"
source_url: https://docs.ceph.com/en/squid/cephfs/client-config-ref/
fetched_at: 2026-07-27T16:39:59+00:00
---
# Client Configuration

## Updating Client Configuration

Certain client configurations can be applied at runtime. To check if a configuration option can be applied (taken into affect by a client) at runtime, use the config help command:

```
ceph config help debug_client
 debug_client - Debug level for client
 (str, advanced)                                                                                                                      Default: 0/5
 Can update at runtime: true

 The value takes the form 'N' or 'N/M' where N and M are values between 0 and 99.  N is the debug level to log (all values below this are included), and M is the level to gather and buffer in memory.  In the event of a crash, the most recent items <= M are dumped to the log file.
```

config help tells if a given configuration can be applied at runtime along with the defaults and a description of the configuration option.

To update a configuration option at runtime, use the config set command:

```
ceph config set client debug_client 20/20
```

Note that this changes a given configuration for all clients.

To check configured options use the config get command:

```
ceph config get client
 WHO    MASK LEVEL    OPTION                    VALUE     RO
 client      advanced debug_client              20/20
 global      advanced osd_pool_default_min_size 1
 global      advanced osd_pool_default_size     3
```

## Client Config Reference

client_acl_type
:   > Set the ACL type. Currently, only possible value is `"posix_acl"` to
    > enable POSIX ACL, or an empty string. This option only takes effect
    > when the `fuse_default_permissions` is set to `false`.
    >
    > type:
    > :   `str`

client_cache_mid
:   > Set client cache midpoint. The midpoint splits the least recently used
    > lists into a hot and warm list.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.75`

client_cache_size
:   > Set the number of inodes that the client keeps in the metadata cache.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `16Ki`

client_caps_release_delay
:   > Set the delay between capability releases in seconds. The delay sets
    > how many seconds a client waits to release capabilities that it no
    > longer needs in case the capabilities are needed for another user
    > space operation.
    >
    > type:
    > :   `secs`
    >
    > default:
    > :   `5`

client_debug_force_sync_read
:   > If set to `true`, clients read data directly from OSDs instead of
    > using a local page cache.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`

client_dirsize_rbytes
:   > This option enables a CephFS feature that stores the recursive
    > directory size (the bytes used by files in the directory and its
    > descendents) in the st_size field of the stat structure.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`

client_max_inline_size
:   > Set the maximum size of inlined data stored in a file inode rather
    > than in a separate data object in RADOS. This setting only applies if
    > the `inline_data` flag is set on the MDS map.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `4Ki`

client_metadata
:   > Comma-delimited strings for client metadata sent to each MDS, in
    > addition to the automatically generated version, host name, and other
    > metadata.
    >
    > type:
    > :   `str`

client_mount_gid
:   > Set the group ID of CephFS mount.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `-1`

client_mount_timeout
:   > Set the timeout for CephFS mount in seconds.
    >
    > type:
    > :   `secs`
    >
    > default:
    > :   `5 minutes`

client_mount_uid
:   > Set the user ID of CephFS mount.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `-1`

client_mountpoint
:   > Directory to mount on the CephFS file system. An alternative to the
    > `-r` option of the `ceph-fuse` command.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `/`

client_oc
:   > enable object caching
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`

client_oc_max_dirty
:   > Set the maximum number of dirty bytes in the object cache.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `100Mi`

client_oc_max_dirty_age
:   > Set the maximum age in seconds of dirty data in the object cache
    > before writeback.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `5.0`

client_oc_max_objects
:   > Set the maximum number of objects in the object cache.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `1000`

client_oc_size
:   > Set how many bytes of data will the client cache.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `200Mi`

client_oc_target_dirty
:   > Set the target size of dirty data. We recommend to keep this number
    > low.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `8Mi`

client_permissions
:   > Check client permissions on all I/O operations.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`

client_quota_df
:   > Report root directory quota for the `statfs` operation.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`

client_readahead_max_bytes
:   > Set the maximum number of bytes that the client reads ahead for future
    > read operations. Overridden by the `client_readahead_max_periods`
    > setting.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `0B`

client_readahead_max_periods
:   > Set the number of file layout periods (object size \* number of
    > stripes) that the client reads ahead. Overrides the
    > `client_readahead_max_bytes` setting.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `4`

client_readahead_min
:   > Set the minimum number bytes that the client reads ahead.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `128Ki`

client_reconnect_stale
:   > reconnect when the session becomes stale
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`

client_snapdir
:   > Set the snapshot directory name.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `.snap`

client_tick_interval
:   > Set the interval in seconds between capability renewal and other
    > upkeep.
    >
    > type:
    > :   `secs`
    >
    > default:
    > :   `1`

client_use_random_mds
:   > Choose random MDS for each request.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`

fuse_default_permissions
:   > When set to `false`, `ceph-fuse` utility checks does its own
    > permissions checking, instead of relying on the permissions
    > enforcement in FUSE. Set to `false` together with the `client acl
    > type=posix_acl` option to enable POSIX ACL.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`

fuse_max_write
:   > Set the maximum number of bytes in a single write operation. A value
    > of 0 indicates no change; the FUSE default of 128 kbytes remains in
    > force.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `0B`

fuse_disable_pagecache
:   > If set to `true`, kernel page cache is disabled for `ceph-fuse`
    > mounts. When multiple clients read/write to a file at the same time,
    > readers may get stale data from page cache. Due to limitations of
    > FUSE, `ceph-fuse` can’t disable page cache dynamically.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`

### Developer Options

> **Important:**
>
> These options are internal. They are listed here only to complete the list of options.

client_debug_getattr_caps
:   > type:
    > :   `bool`
    >
    > default:
    > :   `false`

client_debug_inject_tick_delay
:   > type:
    > :   `secs`
    >
    > default:
    > :   `0`

client_inject_fixed_oldest_tid
:   > type:
    > :   `bool`
    >
    > default:
    > :   `false`

client_inject_release_failure
:   > type:
    > :   `bool`
    >
    > default:
    > :   `false`

client_trace
:   > file containing trace of client operations
    >
    > type:
    > :   `str`

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
