---
collection: ceph
version: "19.2.2"
title: "Ceph Object Gateway Config Reference"
source_url: https://docs.ceph.com/en/squid/radosgw/config-ref/
fetched_at: 2026-07-27T16:40:31+00:00
---
# Ceph Object Gateway Config Reference

The following settings may added to the Ceph configuration file (i.e., usually
`ceph.conf`) under the `[client.radosgw.{instance-name}]` section. The
settings may contain default values. If you do not specify each setting in the
Ceph configuration file, the default value will be set automatically.

Configuration variables set under the `[client.radosgw.{instance-name}]`
section will not apply to rgw or radosgw-admin commands without an instance-name
specified in the command. Thus variables meant to be applied to all RGW
instances or all radosgw-admin options can be put into the `[global]` or the
`[client]` section to avoid specifying `instance-name`.

rgw_frontends
:   > Configures the HTTP frontend(s). The configuration for multiple
    > frontends can be provided in a comma-delimited list. Each frontend
    > configuration may include a list of options separated by spaces, where
    > each option is in the form “key=value” or “key”. See [HTTP Frontends](../frontends.md)
    > for more on supported options.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `beast port=7480`

rgw_data
:   > Sets the location of the data files for Ceph RADOS Gateway.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `/var/lib/ceph/radosgw/$cluster-$id`

rgw_enable_apis
:   > Enables the specified APIs.
    >
    > > > **Note:**
    > > >
    > > > Enabling the `s3` API is a requirement for
    > > > any `radosgw` instance that is meant to
    > > > participate in a [multi-site](../multisite.md)
    > > > configuration.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `s3, s3website, swift, swift_auth, admin, sts, iam, notifications`

rgw_cache_enabled
:   > Whether the Ceph Object Gateway cache is enabled.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`
    >
    > see also:
    > :   [`rgw_cache_lru_size`](index.md#confval-rgw_cache_lru_size)

rgw_cache_lru_size
:   > The number of entries in the Ceph Object Gateway cache.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `25000`
    >
    > see also:
    > :   [`rgw_cache_enabled`](index.md#confval-rgw_cache_enabled)

rgw_dns_name
:   > The DNS names of the served domains. See also the `hostnames`
    > setting within zonegroups.
    >
    > type:
    > :   `str`

rgw_script_uri
:   > The alternative value for the `SCRIPT_URI` if not set in the
    > request.
    >
    > type:
    > :   `str`

rgw_request_uri
:   > The alternative value for the `REQUEST_URI` if not set in the
    > request.
    >
    > type:
    > :   `str`

rgw_print_continue
:   > Enable `100-continue` if it is operational.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`

rgw_remote_addr_param
:   > The remote address parameter. For example, the HTTP field containing
    > the remote address, or the `X-Forwarded-For` address if a reverse
    > proxy is operational.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `REMOTE_ADDR`
    >
    > see also:
    > :   [`rgw_enable_ops_log`](index.md#confval-rgw_enable_ops_log)

rgw_op_thread_timeout
:   > The timeout in seconds for open threads.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `10 minutes`

rgw_op_thread_suicide_timeout
:   > The time `timeout` in seconds before a Ceph Object Gateway process
    > dies. Disabled if set to `0`.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `0`

rgw_thread_pool_size
:   > The size of the thread pool.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `512`

rgw_num_control_oids
:   > The number of notification objects used for cache synchronization
    > between different `rgw` instances.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `8`

rgw_init_timeout
:   > The number of seconds before Ceph Object Gateway gives up on
    > initialization.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `5 minutes`

rgw_mime_types_file
:   > The path and location of the MIME-types file. Used for Swift auto-
    > detection of object types.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `/etc/mime.types`

rgw_s3_success_create_obj_status
:   > The alternate success status response for `create-obj`.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `0`

rgw_resolve_cname
:   > Whether `rgw` should use DNS CNAME record of the request hostname
    > field (if hostname is not equal to `rgw dns name`).
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`

rgw_obj_stripe_size
:   > The size of an object stripe for Ceph Object Gateway objects. See
    > [Architecture](../../architecture.md#data-striping) for details on striping.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `4Mi`

rgw_extended_http_attrs
:   > Add new set of attributes that could be set on an entity (user, bucket
    > or object). These extra attributes can be set through HTTP header
    > fields when putting the entity or modifying it using POST method. If
    > set, these attributes will return as HTTP fields when doing GET/HEAD
    > on the entity.
    >
    > type:
    > :   `str`
    >
    > example:
    > :   content_foo, content_bar, x-foo-bar

rgw_exit_timeout_secs
:   > Number of seconds to wait for a process before exiting
    > unconditionally.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `2 minutes`

rgw_get_obj_window_size
:   > The window size in bytes for a single object read request
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `16Mi`

rgw_get_obj_max_req_size
:   > The maximum request size of a single get operation sent to the Ceph
    > Storage Cluster.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `4Mi`

rgw_multipart_min_part_size
:   > When doing a multipart upload, each part (other than the last part)
    > must be at least this size.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `5Mi`

rgw_relaxed_s3_bucket_names
:   > Enables relaxed S3 bucket names rules for US region buckets.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`

rgw_list_buckets_max_chunk
:   > The maximum number of buckets to retrieve in a single operation when
    > listing user buckets.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `1000`

rgw_override_bucket_index_max_shards
:   > Represents the number of shards for the bucket index object, a value
    > of zero indicates there is no sharding. It is not recommended to set a
    > value too large (e.g. thousand) as it increases the cost for bucket
    > listing. This variable should be set in the client or global sections
    > so that it is automatically applied to radosgw-admin commands.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `0`

rgw_curl_wait_timeout_ms
:   > The timeout in milliseconds for certain `curl` calls.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `1000`

rgw_copy_obj_progress
:   > Enables output of object progress during long copy operations.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`

rgw_copy_obj_progress_every_bytes
:   > The minimum bytes between copy progress output.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `1Mi`

rgw_max_copy_obj_concurrent_io
:   > Number of refcount operations to process concurrently when executing
    > copy_obj
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `10`

rgw_admin_entry
:   > The entry point for an admin request URL.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `admin`

rgw_content_length_compat
:   > Enable compatibility handling of FCGI requests with both
    > `CONTENT_LENGTH` and `HTTP_CONTENT_LENGTH` set.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`

rgw_bucket_quota_ttl
:   > The amount of time in seconds cached quota information is trusted.
    > After this timeout, the quota information will be re-fetched from the
    > cluster.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `10 minutes`

rgw_user_quota_bucket_sync_interval
:   > The amount of time in seconds bucket quota information is accumulated
    > before syncing to the cluster. During this time, other RGW instances
    > will not see the changes in bucket quota stats from operations on this
    > instance.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `3 minutes`

rgw_user_quota_sync_interval
:   > The amount of time in seconds user quota information is accumulated
    > before syncing to the cluster. During this time, other RGW instances
    > will not see the changes in user quota stats from operations on this
    > instance.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `1 day`

rgw_bucket_default_quota_max_objects
:   > Default max number of objects per bucket. Set on new users, if no
    > other quota is specified. Has no effect on existing users. This
    > variable should be set in the client or global sections so that it is
    > automatically applied to radosgw-admin commands.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `-1`

rgw_bucket_default_quota_max_size
:   > Default max capacity per bucket, in bytes. Set on new users, if no
    > other quota is specified. Has no effect on existing users.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `-1`

rgw_user_default_quota_max_objects
:   > Default max number of objects for a user. This includes all objects in
    > all buckets owned by the user. Set on new users, if no other quota is
    > specified. Has no effect on existing users.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `-1`

rgw_user_default_quota_max_size
:   > The value for user max size quota in bytes set on new users, if no
    > other quota is specified. Has no effect on existing users.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `-1`

rgw_account_default_quota_max_objects
:   > Default max number of objects for a account. This includes all objects
    > in all buckets owned by the account. Set on new accounts if no other
    > quota is specified. Has no effect on existing accounts.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `-1`

rgw_account_default_quota_max_size
:   > The value for account max size quota in bytes set on new accounts, if
    > no other quota is specified. Has no effect on existing accounts.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `-1`

rgw_verify_ssl
:   > Verify SSL certificates while making requests.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`
    >
    > see also:
    > :   [`rgw_keystone_verify_ssl`](index.md#confval-rgw_keystone_verify_ssl)

rgw_max_chunk_size
:   > The chunk size is the size of RADOS I/O requests that RGW sends when
    > accessing data objects. RGW read and write operations will never
    > request more than this amount in a single request. This also defines
    > the RGW head object size, as head operations need to be atomic, and
    > anything larger than this would require more than a single operation.
    > When RGW objects are written to the default storage class, up to this
    > amount of payload data will be stored alongside metadata in the head
    > object.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `4Mi`

## Lifecycle Settings

Bucket Lifecycle (LC) configuration can be used to manage your objects so that
they are stored effectively throughout their lifetimes. In past releases,
lifecycle processing was rate-limited by single-threaded processing. As of the
Nautilus release, the Ceph Object Gateway allows for parallel-thread processing
of bucket lifecycles across additional Ceph Object Gateway instances and
replaces in-order index-shard enumeration with a random ordered sequence.

Two options in particular are relevant to adjusting the aggressiveness of
lifecycle processing:

rgw_lc_max_worker
:   > This option specifies the number of lifecycle worker threads to run in
    > parallel, thereby processing bucket and index shards simultaneously.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `3`

rgw_lc_max_wp_worker
:   > This option specifies the number of threads in each lifecycle workers
    > work pool. This option can help accelerate processing each bucket.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `3`

These values can be tuned based upon your specific workload to further increase
the aggressiveness of lifecycle processing. For a workload with a large number
of buckets (thousands), raise the number of workers by increasing
[`rgw_lc_max_worker`](index.md#confval-rgw_lc_max_worker) from the default value of 3. But for a workload
with a higher number of objects per bucket (hundreds of thousands), raise the
number of parallel threads by increasing [`rgw_lc_max_wp_worker`](index.md#confval-rgw_lc_max_wp_worker) from
the default value of 3.

> **Note:**
>
> Before increasing either of these values, validate the current
> Cluster performance and Ceph Object Gateway utilization.

The lifecycle maintenance thread must also be enabled on at least one RGW
daemon for each zone.

rgw_enable_lc_threads
:   > The lifecycle maintenance thread is responsible for lifecycle related
    > maintenance work. The thread itself can be disabled, but in order for
    > lifecycle to work correctly, at least one RGW in each zone needs to
    > have this thread running. Having the thread enabled on multiple RGW
    > processes within the same zone can spread some of the maintenance work
    > between them.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`
    >
    > see also:
    > :   [`rgw_enable_gc_threads`](index.md#confval-rgw_enable_gc_threads), `rgw_enable_quota_threads`

## Garbage Collection Settings

The Ceph Object Gateway allocates storage for new objects immediately.

The Ceph Object Gateway purges the storage space used for deleted and overwritten
objects in the Ceph Storage cluster some time after the gateway deletes the
objects from the bucket index. The process of purging the deleted object data
from the Ceph Storage cluster is known as Garbage Collection or GC.

To view the queue of objects awaiting garbage collection, execute the following

```
radosgw-admin gc list
```

> **Note:**
>
> Specify `--include-all` to list all entries, including unexpired
> Garbage Collection objects.

Garbage collection is a background activity that may
execute continuously or during times of low loads, depending upon how the
administrator configures the Ceph Object Gateway. By default, the Ceph Object
Gateway conducts GC operations continuously. Since GC operations are a normal
part of Ceph Object Gateway operations, especially with object delete
operations, objects eligible for garbage collection exist most of the time.

Some workloads may temporarily or permanently outpace the rate of garbage
collection activity. This is especially true of delete-heavy workloads, where
many objects get stored for a short period of time and then deleted. For these
types of workloads, administrators can increase the priority of garbage
collection operations relative to other operations with the following
configuration parameters.

rgw_gc_max_objs
:   > The maximum number of objects that may be handled by garbage
    > collection in one garbage collection processing cycle. Please do not
    > change this value after the first deployment.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `32`
    >
    > see also:
    > :   [`rgw_gc_obj_min_wait`](index.md#confval-rgw_gc_obj_min_wait), [`rgw_gc_processor_max_time`](index.md#confval-rgw_gc_processor_max_time), [`rgw_gc_processor_period`](index.md#confval-rgw_gc_processor_period), [`rgw_gc_max_concurrent_io`](index.md#confval-rgw_gc_max_concurrent_io)

rgw_gc_obj_min_wait
:   > The minimum wait time before a deleted object may be removed and
    > handled by garbage collection processing.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `2 hours`
    >
    > see also:
    > :   [`rgw_gc_max_objs`](index.md#confval-rgw_gc_max_objs), [`rgw_gc_processor_max_time`](index.md#confval-rgw_gc_processor_max_time), [`rgw_gc_processor_period`](index.md#confval-rgw_gc_processor_period), [`rgw_gc_max_concurrent_io`](index.md#confval-rgw_gc_max_concurrent_io)

rgw_gc_processor_max_time
:   > The maximum time between the beginning of two consecutive garbage
    > collection processing cycles.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `1 hour`
    >
    > see also:
    > :   [`rgw_gc_max_objs`](index.md#confval-rgw_gc_max_objs), [`rgw_gc_obj_min_wait`](index.md#confval-rgw_gc_obj_min_wait), [`rgw_gc_processor_period`](index.md#confval-rgw_gc_processor_period), [`rgw_gc_max_concurrent_io`](index.md#confval-rgw_gc_max_concurrent_io)

rgw_gc_processor_period
:   > The cycle time for garbage collection processing.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `1 hour`
    >
    > see also:
    > :   [`rgw_gc_max_objs`](index.md#confval-rgw_gc_max_objs), [`rgw_gc_obj_min_wait`](index.md#confval-rgw_gc_obj_min_wait), [`rgw_gc_processor_max_time`](index.md#confval-rgw_gc_processor_max_time), [`rgw_gc_max_concurrent_io`](index.md#confval-rgw_gc_max_concurrent_io), `rgw_gc_max_trim_chunk`

rgw_gc_max_concurrent_io
:   > The maximum number of concurrent IO operations that the RGW garbage
    > collection thread will use when purging old data.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `10`
    >
    > see also:
    > :   [`rgw_gc_max_objs`](index.md#confval-rgw_gc_max_objs), [`rgw_gc_obj_min_wait`](index.md#confval-rgw_gc_obj_min_wait), [`rgw_gc_processor_max_time`](index.md#confval-rgw_gc_processor_max_time), `rgw_gc_max_trim_chunk`

Tuning Garbage Collection for Delete Heavy Workloads:

As an initial step towards tuning Ceph Garbage Collection to be more
aggressive the following options are suggested to be increased from their
default configuration values:

```
rgw_gc_max_concurrent_io = 20
rgw_gc_max_trim_chunk = 64
```

> **Note:**
>
> Modifying these values requires a restart of the RGW service.

Once these values have been increased from default please monitor for performance of the cluster during Garbage Collection to verify no adverse performance issues due to the increased values.

At least one RGW in each zone must have the garbage collection maintenance
thread running:

rgw_enable_gc_threads
:   > The garbage collection maintenance thread is responsible for garbage
    > collector maintenance work. The thread itself can be disabled, but in
    > order for garbage collection to work correctly, at least one RGW in
    > each zone needs to have this thread running. Having the thread
    > enabled on multiple RGW processes within the same zone can spread some
    > of the maintenance work between them.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`
    >
    > see also:
    > :   `rgw_enable_quota_threads`, [`rgw_enable_lc_threads`](index.md#confval-rgw_enable_lc_threads)

## Multisite Settings

New in version Jewel.

You may include the following settings in your Ceph configuration
file under each `[client.radosgw.{instance-name}]` instance.

rgw_zone
:   > The name of the zone for the gateway instance. If no zone is set, a
    > cluster-wide default can be configured with the command `radosgw-
    > admin zone default`.
    >
    > type:
    > :   `str`
    >
    > see also:
    > :   [`rgw_zonegroup`](index.md#confval-rgw_zonegroup), [`rgw_realm`](index.md#confval-rgw_realm)

rgw_zonegroup
:   > The name of the zonegroup for the gateway instance. If no zonegroup is
    > set, a cluster-wide default can be configured with the command
    > `radosgw-admin zonegroup default`.
    >
    > type:
    > :   `str`
    >
    > see also:
    > :   [`rgw_zone`](index.md#confval-rgw_zone), [`rgw_realm`](index.md#confval-rgw_realm)

rgw_realm
:   > The name of the realm for the gateway instance. If no realm is set, a
    > cluster-wide default can be configured with the command `radosgw-
    > admin realm default`.
    >
    > type:
    > :   `str`

rgw_run_sync_thread
:   > If there are other zones in the realm to sync from, spawn threads to
    > handle the sync of data and metadata.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`

rgw_data_log_window
:   > The data log entries window in seconds.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `30`

rgw_data_log_changes_size
:   > RGW will trigger update to the data log if the number of pending
    > entries reached this number.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `1000`

rgw_data_log_obj_prefix
:   > The object name prefix for the data log.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `data_log`

rgw_data_log_num_shards
:   > The number of shards (objects) on which to keep the data changes log.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `128`

rgw_md_log_max_shards
:   > The maximum number of shards for the metadata log.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `64`

rgw_data_sync_poll_interval
:   > Once multisite’s incremental sync of a datalog shard is caught up with
    > its source, it will wait this long (in seconds) before polling for
    > more changes.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `20`
    >
    > see also:
    > :   [`rgw_meta_sync_poll_interval`](index.md#confval-rgw_meta_sync_poll_interval)

rgw_meta_sync_poll_interval
:   > Once multisite’s incremental sync of a mdlog shard is caught up with
    > its source, it will wait this long (in seconds) before polling for
    > more changes.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `20`
    >
    > see also:
    > :   [`rgw_data_sync_poll_interval`](index.md#confval-rgw_data_sync_poll_interval)

rgw_bucket_sync_spawn_window
:   > The maximum number of items that bucket sync is willing to process in
    > parallel (per remote bilog shard).
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `20`
    >
    > see also:
    > :   [`rgw_data_sync_spawn_window`](index.md#confval-rgw_data_sync_spawn_window), [`rgw_meta_sync_spawn_window`](index.md#confval-rgw_meta_sync_spawn_window)

rgw_data_sync_spawn_window
:   > The maximum number of items that data sync is willing to process in
    > parallel (per remote datalog shard).
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `20`
    >
    > see also:
    > :   [`rgw_bucket_sync_spawn_window`](index.md#confval-rgw_bucket_sync_spawn_window), [`rgw_meta_sync_spawn_window`](index.md#confval-rgw_meta_sync_spawn_window)

rgw_meta_sync_spawn_window
:   > The maximum number of items that metadata sync is willing to process
    > in parallel (per remote mdlog shard).
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `20`
    >
    > see also:
    > :   [`rgw_bucket_sync_spawn_window`](index.md#confval-rgw_bucket_sync_spawn_window), [`rgw_data_sync_spawn_window`](index.md#confval-rgw_data_sync_spawn_window)

> **Important:**
>
> The values of [`rgw_data_log_num_shards`](index.md#confval-rgw_data_log_num_shards) and
> [`rgw_md_log_max_shards`](index.md#confval-rgw_md_log_max_shards) should not be changed after sync has
> started.

## S3 Settings

rgw_s3_auth_use_ldap
:   > Should S3 authentication use LDAP.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`

## Swift Settings

rgw_enforce_swift_acls
:   > Enforces the Swift Access Control List (ACL) settings.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`

rgw_swift_tenant_name
:   > Tenant name that is used when constructing the swift path.
    >
    > type:
    > :   `str`
    >
    > see also:
    > :   [`rgw_swift_account_in_url`](index.md#confval-rgw_swift_account_in_url)

rgw_swift_token_expiration
:   > The time in seconds for expiring a Swift token.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `1 day`

rgw_swift_url
:   > The URL for the Ceph Object Gateway Swift API.
    >
    > type:
    > :   `str`
    >
    > see also:
    > :   [`rgw_swift_auth_entry`](index.md#confval-rgw_swift_auth_entry)

rgw_swift_url_prefix
:   > The URL prefix for the Swift API, to distinguish it from
    > the S3 API endpoint. The default is `swift`, which
    > makes the Swift API available at the URL
    > `http://host:port/swift/v1` (or
    > `http://host:port/swift/v1/AUTH_%(tenant_id)s` if
    > `rgw swift account in url` is enabled).
    >
    > For compatibility, setting this configuration variable
    > to the empty string causes the default `swift` to be
    > used; if you do want an empty prefix, set this option to
    > `/`.
    >
    > > **Warning:**
    > >
    > > If you set this option to `/`, you must
    > > disable the S3 API by modifying `rgw
    > > enable apis` to exclude `s3`. It is not
    > > possible to operate radosgw with `rgw
    > > swift url prefix = /` and simultaneously
    > > support both the S3 and Swift APIs. If you
    > > do need to support both APIs without
    > > prefixes, deploy multiple radosgw instances
    > > to listen on different hosts (or ports)
    > > instead, enabling some for S3 and some for
    > > Swift.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `swift`
    >
    > example:
    > :   /swift-testing

rgw_swift_auth_url
:   > Default url to which RGW connects and verifies tokens for v1 auth (if
    > not using internal swift auth).
    >
    > type:
    > :   `str`

rgw_swift_auth_entry
:   > The entry point for a Swift auth URL.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `auth`
    >
    > see also:
    > :   [`rgw_swift_url`](index.md#confval-rgw_swift_url)

rgw_swift_account_in_url
:   > Whether or not the Swift account name should be included
    > in the Swift API URL.
    > If set to `false` (the default), then the Swift API
    > will listen on a URL formed like
    > `http://host:port/<rgw_swift_url_prefix>/v1`, and the
    > account name (commonly a Keystone project UUID if
    > radosgw is configured with [Keystone integration](../keystone.md)) will be inferred from request
    > headers.
    > If set to `true`, the Swift API URL will be
    > `http://host:port/<rgw_swift_url_prefix>/v1/AUTH_<account_name>`
    > (or
    > `http://host:port/<rgw_swift_url_prefix>/v1/AUTH_<keystone_project_id
    > >`)
    > instead, and the Keystone `object-store` endpoint must
    > accordingly be configured to include the
    > `AUTH_%(tenant_id)s` suffix.
    > You **must** set this option to `true` (and update the
    > Keystone service catalog) if you want radosgw to support
    > publicly-readable containers and [temporary URLs](../swift/tempurl.md).
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`
    >
    > see also:
    > :   [`rgw_swift_tenant_name`](index.md#confval-rgw_swift_tenant_name)

rgw_swift_versioning_enabled
:   > Enables the Object Versioning of OpenStack Object Storage API.
    > This allows clients to put the `X-Versions-Location` attribute
    > on containers that should be versioned. The attribute specifies
    > the name of container storing archived versions. It must be owned
    > by the same user that the versioned container due to access
    > control verification - ACLs are NOT taken into consideration.
    > Those containers cannot be versioned by the S3 object versioning
    > mechanism.
    >
    > A slightly different attribute, `X-History-Location`, which is also
    > understood by
    > [OpenStack Swift](https://docs.openstack.org/swift/latest/api/object_versioning.html)
    > for handling `DELETE` operations, is currently not supported.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`

rgw_trust_forwarded_https
:   > When a proxy in front of radosgw is used for ssl termination, radosgw
    > does not know whether incoming http connections are secure. Enable
    > this option to trust the `Forwarded` and `X-Forwarded-Proto`
    > headers sent by the proxy when determining whether the connection is
    > secure. This is required for some features, such as server side
    > encryption. (Never enable this setting if you do not have a trusted
    > proxy in front of radosgw, or else malicious users will be able to set
    > these headers in any request.)
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`
    >
    > see also:
    > :   `rgw_crypt_require_ssl`

## Logging Settings

rgw_log_nonexistent_bucket
:   > Enables Ceph Object Gateway to log a request for a non-existent
    > bucket.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`
    >
    > see also:
    > :   [`rgw_enable_ops_log`](index.md#confval-rgw_enable_ops_log)

rgw_log_object_name
:   > The logging format for an object name. See man page *date*
    > for details about format specifiers.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `%Y-%m-%d-%H-%i-%n`
    >
    > see also:
    > :   [`rgw_enable_ops_log`](index.md#confval-rgw_enable_ops_log)

rgw_log_object_name_utc
:   > Whether a logged object name includes a UTC time. If `false`, it
    > uses the local time.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`
    >
    > see also:
    > :   [`rgw_enable_ops_log`](index.md#confval-rgw_enable_ops_log), [`rgw_log_object_name`](index.md#confval-rgw_log_object_name)

rgw_usage_max_shards
:   > The maximum number of shards for usage logging.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `32`
    >
    > see also:
    > :   [`rgw_enable_usage_log`](index.md#confval-rgw_enable_usage_log)

rgw_usage_max_user_shards
:   > The maximum number of shards used for a single user’s usage logging.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `1`
    >
    > min:
    > :   `1`
    >
    > see also:
    > :   [`rgw_enable_usage_log`](index.md#confval-rgw_enable_usage_log)

rgw_enable_ops_log
:   > Enable logging for each successful Ceph Object Gateway operation.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`
    >
    > see also:
    > :   [`rgw_log_nonexistent_bucket`](index.md#confval-rgw_log_nonexistent_bucket), [`rgw_log_object_name`](index.md#confval-rgw_log_object_name), [`rgw_ops_log_rados`](index.md#confval-rgw_ops_log_rados), [`rgw_ops_log_socket_path`](index.md#confval-rgw_ops_log_socket_path), `rgw_ops_log_file_path`

rgw_enable_usage_log
:   > Enable the usage log
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`
    >
    > see also:
    > :   [`rgw_usage_max_shards`](index.md#confval-rgw_usage_max_shards)

rgw_ops_log_rados
:   > Whether the operations log should be written to the Ceph Storage
    > Cluster backend.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`
    >
    > see also:
    > :   [`rgw_enable_ops_log`](index.md#confval-rgw_enable_ops_log), [`rgw_log_object_name_utc`](index.md#confval-rgw_log_object_name_utc), [`rgw_log_object_name`](index.md#confval-rgw_log_object_name)

rgw_ops_log_socket_path
:   > The Unix domain socket for writing operations logs.
    >
    > type:
    > :   `str`
    >
    > see also:
    > :   [`rgw_enable_ops_log`](index.md#confval-rgw_enable_ops_log), [`rgw_ops_log_data_backlog`](index.md#confval-rgw_ops_log_data_backlog)

rgw_ops_log_data_backlog
:   > The maximum data backlog data size for operations logs written to a
    > Unix domain socket.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `5Mi`
    >
    > see also:
    > :   [`rgw_enable_ops_log`](index.md#confval-rgw_enable_ops_log), [`rgw_ops_log_socket_path`](index.md#confval-rgw_ops_log_socket_path)

rgw_usage_log_flush_threshold
:   > The number of dirty merged entries in the usage log before flushing
    > synchronously.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `1024`
    >
    > see also:
    > :   [`rgw_enable_usage_log`](index.md#confval-rgw_enable_usage_log), [`rgw_usage_log_tick_interval`](index.md#confval-rgw_usage_log_tick_interval)

rgw_usage_log_tick_interval
:   > Flush pending usage log data every `n` seconds.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `30`
    >
    > see also:
    > :   [`rgw_enable_usage_log`](index.md#confval-rgw_enable_usage_log), [`rgw_usage_log_flush_threshold`](index.md#confval-rgw_usage_log_flush_threshold)

rgw_log_http_headers
:   > Comma-delimited list of HTTP headers to include with ops log entries.
    > Header names are case insensitive, and use the full header name with
    > words separated by underscores.
    >
    > type:
    > :   `str`
    >
    > example:
    > :   http_x_forwarded_for, http_x_special_k

## Keystone Settings

rgw_keystone_url
:   > The URL to the Keystone server.
    >
    > type:
    > :   `str`

rgw_keystone_api_version
:   > The version (2 or 3) of OpenStack Identity API that should be used for
    > communication with the Keystone server.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `2`

rgw_keystone_admin_domain
:   > The name of OpenStack domain with admin privilege when using OpenStack
    > Identity API v3.
    >
    > type:
    > :   `str`

rgw_keystone_admin_project
:   > The name of OpenStack project with admin privilege when using
    > OpenStack Identity API v3. If left unspecified, value of `rgw
    > keystone admin tenant` will be used instead.
    >
    > type:
    > :   `str`

rgw_keystone_admin_token
:   > The Keystone admin token (shared secret). In Ceph RGW authentication
    > with the admin token has priority over authentication with the admin
    > credentials (`rgw_keystone_admin_user`,
    > `rgw_keystone_admin_password`, `rgw_keystone_admin_tenant`,
    > `rgw_keystone_admin_project`, `rgw_keystone_admin_domain`). The
    > Keystone admin token has been deprecated, but can be used to integrate
    > with older environments. It is preferred to instead configure
    > `rgw_keystone_admin_token_path` to avoid exposing the token.
    >
    > type:
    > :   `str`

rgw_keystone_admin_token_path
:   > Path to a file containing the Keystone admin token (shared secret).
    > In Ceph RadosGW authentication with the admin token has priority over
    > authentication with the admin credentials
    > (`rgw_keystone_admin_user`, `rgw_keystone_admin_password`,
    > `rgw_keystone_admin_tenant`, `rgw_keystone_admin_project`,
    > `rgw_keystone_admin_domain`). The Keystone admin token has been
    > deprecated, but can be used to integrate with older environments.
    >
    > type:
    > :   `str`

rgw_keystone_admin_tenant
:   > The name of OpenStack tenant with admin privilege (Service Tenant)
    > when using OpenStack Identity API v2
    >
    > type:
    > :   `str`

rgw_keystone_admin_user
:   > The name of OpenStack user with admin privilege for Keystone
    > authentication (Service User) when using OpenStack Identity API v2
    >
    > type:
    > :   `str`

rgw_keystone_admin_password
:   > The password for OpenStack admin user when using OpenStack Identity
    > API v2. It is preferred to instead configure
    > `rgw_keystone_admin_password_path` to avoid exposing the token.
    >
    > type:
    > :   `str`

rgw_keystone_admin_password_path
:   > Path to a file containing the password for OpenStack admin user when
    > using OpenStack Identity API v2.
    >
    > type:
    > :   `str`

rgw_keystone_accepted_roles
:   > The roles required to serve requests.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `Member, admin`

rgw_keystone_token_cache_size
:   > The maximum number of entries in each Keystone token cache.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `10000`

rgw_keystone_verify_ssl
:   > Verify SSL certificates while making token requests to keystone.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`

rgw_keystone_service_token_enabled
:   > The service token support allows the incoming request to contain a
    > X-Service-Token header with a Keystone token that if it has acceptable
    > roles allows using an expired token in the X-Auth-Token header.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`
    >
    > see also:
    > :   [`rgw_keystone_service_token_accepted_roles`](index.md#confval-rgw_keystone_service_token_accepted_roles), [`rgw_keystone_expired_token_cache_expiration`](index.md#confval-rgw_keystone_expired_token_cache_expiration)

rgw_keystone_service_token_accepted_roles
:   > The users that created the service token given must have one of these
    > roles to be considered a valid service user.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `admin`
    >
    > see also:
    > :   [`rgw_keystone_service_token_enabled`](index.md#confval-rgw_keystone_service_token_enabled)

rgw_keystone_expired_token_cache_expiration
:   > The expired token that is allowed when a valid service token is given
    > need a new expiration date for the caching. This is the seconds to add
    > to the current time and then set on an expired token that is verified
    > with a service token.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `3600`
    >
    > see also:
    > :   [`rgw_keystone_service_token_enabled`](index.md#confval-rgw_keystone_service_token_enabled)

## Server-side encryption Settings

rgw_crypt_s3_kms_backend
:   > Where the SSE-KMS encryption keys are stored. Supported KMS systems
    > are OpenStack Barbican (`barbican`, the default) and HashiCorp Vault
    > (`vault`).
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `barbican`
    >
    > valid choices:
    > :   - `barbican`
    >     - `vault`
    >     - `testing`
    >     - `kmip`

## Barbican Settings

rgw_barbican_url
:   > The URL for the Barbican server.
    >
    > type:
    > :   `str`

rgw_keystone_barbican_user
:   > The name of the OpenStack user with access to the [Barbican](../barbican.md) secrets
    > used for [Encryption](../encryption.md).
    >
    > type:
    > :   `str`

rgw_keystone_barbican_password
:   > The password associated with the [Barbican](../barbican.md) user.
    >
    > type:
    > :   `str`

rgw_keystone_barbican_tenant
:   > The name of the OpenStack tenant associated with the [Barbican](../barbican.md) user
    > when using OpenStack Identity API v2.
    >
    > type:
    > :   `str`

rgw_keystone_barbican_project
:   > The name of the OpenStack project associated with the [Barbican](../barbican.md) user
    > when using OpenStack Identity API v3.
    >
    > type:
    > :   `str`

rgw_keystone_barbican_domain
:   > The name of the OpenStack domain associated with the [Barbican](../barbican.md) user
    > when using OpenStack Identity API v3.
    >
    > type:
    > :   `str`

## HashiCorp Vault Settings

rgw_crypt_vault_auth
:   > Type of authentication method to be used. The only method currently
    > supported is `token`.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `token`
    >
    > valid choices:
    > :   - `token`
    >     - `agent`
    >
    > see also:
    > :   [`rgw_crypt_s3_kms_backend`](index.md#confval-rgw_crypt_s3_kms_backend), [`rgw_crypt_vault_addr`](index.md#confval-rgw_crypt_vault_addr), [`rgw_crypt_vault_token_file`](index.md#confval-rgw_crypt_vault_token_file)

rgw_crypt_vault_token_file
:   > If authentication method is ‘token’, provide a path to the token file,
    > which for security reasons should readable only by Rados Gateway.
    >
    > type:
    > :   `str`
    >
    > see also:
    > :   [`rgw_crypt_s3_kms_backend`](index.md#confval-rgw_crypt_s3_kms_backend), [`rgw_crypt_vault_auth`](index.md#confval-rgw_crypt_vault_auth), [`rgw_crypt_vault_addr`](index.md#confval-rgw_crypt_vault_addr)

rgw_crypt_vault_addr
:   > Vault server base address, e.g. `http://vaultserver:8200`.
    >
    > type:
    > :   `str`
    >
    > see also:
    > :   [`rgw_crypt_s3_kms_backend`](index.md#confval-rgw_crypt_s3_kms_backend), [`rgw_crypt_vault_auth`](index.md#confval-rgw_crypt_vault_auth), [`rgw_crypt_vault_prefix`](index.md#confval-rgw_crypt_vault_prefix)

rgw_crypt_vault_prefix
:   > The Vault secret URL prefix, which can be used to restrict access to a
    > particular subset of the secret space, e.g. `/v1/secret/data`.
    >
    > type:
    > :   `str`
    >
    > see also:
    > :   [`rgw_crypt_s3_kms_backend`](index.md#confval-rgw_crypt_s3_kms_backend), [`rgw_crypt_vault_addr`](index.md#confval-rgw_crypt_vault_addr), [`rgw_crypt_vault_auth`](index.md#confval-rgw_crypt_vault_auth)

rgw_crypt_vault_secret_engine
:   > Vault Secret Engine to be used to retrieve encryption keys: choose
    > between kv-v2, transit.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `transit`
    >
    > see also:
    > :   [`rgw_crypt_s3_kms_backend`](index.md#confval-rgw_crypt_s3_kms_backend), [`rgw_crypt_vault_auth`](index.md#confval-rgw_crypt_vault_auth), [`rgw_crypt_vault_addr`](index.md#confval-rgw_crypt_vault_addr)

rgw_crypt_vault_namespace
:   > If set, Vault Namespace provides tenant isolation for teams and
    > individuals on the same Vault Enterprise instance, e.g.
    > `acme/tenant1`
    >
    > type:
    > :   `str`
    >
    > see also:
    > :   [`rgw_crypt_s3_kms_backend`](index.md#confval-rgw_crypt_s3_kms_backend), [`rgw_crypt_vault_auth`](index.md#confval-rgw_crypt_vault_auth), [`rgw_crypt_vault_addr`](index.md#confval-rgw_crypt_vault_addr)

## SSE-S3 Settings

rgw_crypt_sse_s3_backend
:   > Where the SSE-S3 encryption keys are stored. The only valid choice is
    > HashiCorp Vault (`vault`).
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `vault`
    >
    > valid choices:
    > :   - `vault`

rgw_crypt_sse_s3_vault_secret_engine
:   > Vault Secret Engine to be used to retrieve encryption keys. The
    > only valid choice here is transit.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `transit`
    >
    > see also:
    > :   [`rgw_crypt_sse_s3_backend`](index.md#confval-rgw_crypt_sse_s3_backend), [`rgw_crypt_sse_s3_vault_auth`](index.md#confval-rgw_crypt_sse_s3_vault_auth), [`rgw_crypt_sse_s3_vault_addr`](index.md#confval-rgw_crypt_sse_s3_vault_addr)

rgw_crypt_sse_s3_key_template
:   > This is the template for per-bucket sse-s3 keys. This string may
    > include `%bucket_id` which will be expanded out to the bucket
    > marker, a unique uuid assigned to that bucket. It could contain
    > `%owner_id`, which will expand out to the owner’s id. Any other use
    > of % is reserved and should not be used. If the template contains
    > `%bucket_id`, associated bucket keys will be automatically removed
    > when the bucket is removed.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `%bucket_id`
    >
    > see also:
    > :   [`rgw_crypt_sse_s3_backend`](index.md#confval-rgw_crypt_sse_s3_backend), [`rgw_crypt_sse_s3_vault_auth`](index.md#confval-rgw_crypt_sse_s3_vault_auth), [`rgw_crypt_sse_s3_vault_addr`](index.md#confval-rgw_crypt_sse_s3_vault_addr)

rgw_crypt_sse_s3_vault_auth
:   > Type of authentication method to be used. The only method currently
    > supported is `token`.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `token`
    >
    > valid choices:
    > :   - `token`
    >     - `agent`
    >
    > see also:
    > :   [`rgw_crypt_sse_s3_backend`](index.md#confval-rgw_crypt_sse_s3_backend), [`rgw_crypt_sse_s3_vault_addr`](index.md#confval-rgw_crypt_sse_s3_vault_addr), [`rgw_crypt_sse_s3_vault_token_file`](index.md#confval-rgw_crypt_sse_s3_vault_token_file)

rgw_crypt_sse_s3_vault_token_file
:   > If authentication method is ‘token’, provide a path to the token file,
    > which for security reasons should readable only by Rados Gateway.
    >
    > type:
    > :   `str`
    >
    > see also:
    > :   [`rgw_crypt_sse_s3_backend`](index.md#confval-rgw_crypt_sse_s3_backend), [`rgw_crypt_sse_s3_vault_auth`](index.md#confval-rgw_crypt_sse_s3_vault_auth), [`rgw_crypt_sse_s3_vault_addr`](index.md#confval-rgw_crypt_sse_s3_vault_addr)

rgw_crypt_sse_s3_vault_addr
:   > Vault server base address, e.g. `http://vaultserver:8200`.
    >
    > type:
    > :   `str`
    >
    > see also:
    > :   [`rgw_crypt_sse_s3_backend`](index.md#confval-rgw_crypt_sse_s3_backend), [`rgw_crypt_sse_s3_vault_auth`](index.md#confval-rgw_crypt_sse_s3_vault_auth), [`rgw_crypt_sse_s3_vault_prefix`](index.md#confval-rgw_crypt_sse_s3_vault_prefix)

rgw_crypt_sse_s3_vault_prefix
:   > The Vault secret URL prefix, which can be used to restrict access to a
    > particular subset of the secret space, e.g. `/v1/secret/data`.
    >
    > type:
    > :   `str`
    >
    > see also:
    > :   [`rgw_crypt_sse_s3_backend`](index.md#confval-rgw_crypt_sse_s3_backend), [`rgw_crypt_sse_s3_vault_addr`](index.md#confval-rgw_crypt_sse_s3_vault_addr), [`rgw_crypt_sse_s3_vault_auth`](index.md#confval-rgw_crypt_sse_s3_vault_auth)

rgw_crypt_sse_s3_vault_namespace
:   > If set, Vault Namespace provides tenant isolation for teams and
    > individuals on the same Vault Enterprise instance, e.g.
    > `acme/tenant1`
    >
    > type:
    > :   `str`
    >
    > see also:
    > :   [`rgw_crypt_sse_s3_backend`](index.md#confval-rgw_crypt_sse_s3_backend), [`rgw_crypt_sse_s3_vault_auth`](index.md#confval-rgw_crypt_sse_s3_vault_auth), [`rgw_crypt_sse_s3_vault_addr`](index.md#confval-rgw_crypt_sse_s3_vault_addr)

rgw_crypt_sse_s3_vault_verify_ssl
:   > Should RGW verify the vault server SSL certificate.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`

rgw_crypt_sse_s3_vault_ssl_cacert
:   > Path for custom ca certificate for accessing vault server
    >
    > type:
    > :   `str`

rgw_crypt_sse_s3_vault_ssl_clientcert
:   > Path for custom client certificate for accessing vault server
    >
    > type:
    > :   `str`

rgw_crypt_sse_s3_vault_ssl_clientkey
:   > Path for private key required for client cert
    >
    > type:
    > :   `str`

### QoS settings

New in version Nautilus.

The older and now non-default``civetweb`` frontend has a threading model that uses a thread per
connection and hence is automatically throttled by [`rgw_thread_pool_size`](index.md#confval-rgw_thread_pool_size)
when accepting connections. The newer and default `beast` frontend is
not limited by the thread pool size when it comes to accepting new
connections, so a scheduler abstraction was introduced in the Nautilus release
to support additional methods of scheduling requests.

Currently the scheduler defaults to a throttler that limits active
connections to a configured limit. QoS rate limiting based on mClock is currently
*experimental* phase and not recommended for production. The current
implementation of the *dmclock_client* op queue divides RGW ops into admin, auth
(swift auth, sts) metadata, and data requests.

rgw_max_concurrent_requests
:   > Maximum number of concurrent HTTP requests that the beast frontend
    > will process. Tuning this can help to limit memory usage under heavy
    > load.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `1024`
    >
    > see also:
    > :   [`rgw_frontends`](index.md#confval-rgw_frontends)

rgw_scheduler_type
:   > The RGW scheduler to use. Valid values are ``` throttler` and
    > ``dmclock ```. Currently defaults to `throttler` which throttles Beast
    > frontend requests. ``` dmclock` is *experimental* and requires the
    > ``dmclock ``` to be included in the `experimental_feature_enabled`
    > configuration option.
    >
    > The options below tune the experimental dmclock scheduler. For
    > additional reading on dmclock, see [QoS Based on mClock](../../rados/configuration/osd-config-ref/index.md#dmclock-qos). op_class for
    > the flags below is
    > one of `admin`, `auth`, `metadata`, or `data`.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `throttler`

rgw_dmclock_auth_res
:   > mclock reservation for object data requests
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `200.0`
    >
    > see also:
    > :   [`rgw_dmclock_auth_wgt`](index.md#confval-rgw_dmclock_auth_wgt), [`rgw_dmclock_auth_lim`](index.md#confval-rgw_dmclock_auth_lim)

rgw_dmclock_auth_wgt
:   > mclock weight for object data requests
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `100.0`
    >
    > see also:
    > :   [`rgw_dmclock_auth_res`](index.md#confval-rgw_dmclock_auth_res), [`rgw_dmclock_auth_lim`](index.md#confval-rgw_dmclock_auth_lim)

rgw_dmclock_auth_lim
:   > mclock limit for object data requests
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.0`
    >
    > see also:
    > :   [`rgw_dmclock_auth_res`](index.md#confval-rgw_dmclock_auth_res), [`rgw_dmclock_auth_wgt`](index.md#confval-rgw_dmclock_auth_wgt)

rgw_dmclock_admin_res
:   > mclock reservation for admin requests
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `100.0`
    >
    > see also:
    > :   [`rgw_dmclock_admin_wgt`](index.md#confval-rgw_dmclock_admin_wgt), [`rgw_dmclock_admin_lim`](index.md#confval-rgw_dmclock_admin_lim)

rgw_dmclock_admin_wgt
:   > mclock weight for admin requests
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `100.0`
    >
    > see also:
    > :   [`rgw_dmclock_admin_res`](index.md#confval-rgw_dmclock_admin_res), [`rgw_dmclock_admin_lim`](index.md#confval-rgw_dmclock_admin_lim)

rgw_dmclock_admin_lim
:   > mclock limit for admin requests
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.0`
    >
    > see also:
    > :   [`rgw_dmclock_admin_res`](index.md#confval-rgw_dmclock_admin_res), [`rgw_dmclock_admin_wgt`](index.md#confval-rgw_dmclock_admin_wgt)

rgw_dmclock_data_res
:   > mclock reservation for object data requests
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `500.0`
    >
    > see also:
    > :   [`rgw_dmclock_data_wgt`](index.md#confval-rgw_dmclock_data_wgt), [`rgw_dmclock_data_lim`](index.md#confval-rgw_dmclock_data_lim)

rgw_dmclock_data_wgt
:   > mclock weight for object data requests
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `500.0`
    >
    > see also:
    > :   [`rgw_dmclock_data_res`](index.md#confval-rgw_dmclock_data_res), [`rgw_dmclock_data_lim`](index.md#confval-rgw_dmclock_data_lim)

rgw_dmclock_data_lim
:   > mclock limit for object data requests
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.0`
    >
    > see also:
    > :   [`rgw_dmclock_data_res`](index.md#confval-rgw_dmclock_data_res), [`rgw_dmclock_data_wgt`](index.md#confval-rgw_dmclock_data_wgt)

rgw_dmclock_metadata_res
:   > mclock reservation for metadata requests
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `500.0`
    >
    > see also:
    > :   [`rgw_dmclock_metadata_wgt`](index.md#confval-rgw_dmclock_metadata_wgt), [`rgw_dmclock_metadata_lim`](index.md#confval-rgw_dmclock_metadata_lim)

rgw_dmclock_metadata_wgt
:   > mclock weight for metadata requests
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `500.0`
    >
    > see also:
    > :   [`rgw_dmclock_metadata_res`](index.md#confval-rgw_dmclock_metadata_res), [`rgw_dmclock_metadata_lim`](index.md#confval-rgw_dmclock_metadata_lim)

rgw_dmclock_metadata_lim
:   > mclock limit for metadata requests
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.0`
    >
    > see also:
    > :   [`rgw_dmclock_metadata_res`](index.md#confval-rgw_dmclock_metadata_res), [`rgw_dmclock_metadata_wgt`](index.md#confval-rgw_dmclock_metadata_wgt)

## D4N Settings

D4N is a caching architecture that utilizes Redis to speed up S3 object storage
operations by establishing shared databases among Ceph Object Gateway (RGW) daemons.

The D4N architecture can only function on one Redis instance at a time.
The address is configurable and can be changed by accessing the parameters
below.

rgw_d4n_host
:   > The rgw directory host
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `127.0.0.1`

rgw_d4n_port
:   > The rgw directory port
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `6379`

## Topic persistency settings

Topic persistency will repeatedly push notifications until they succeed.
For more information, see [Bucket Notifications](../notifications.md).

The default behavior is to push indefinitely and as frequently as possible.
With these settings you can control how long and how often to retry an
unsuccessful notification by configuring the maximum retention time and/or or
maximum number of retries.
The interval between push retries can be configured via the sleep duration
parameter.

All of these options default to the value 0, which means that persistent
retention is indefinite, and notifications are retried as frequently as possible.

rgw_topic_persistency_time_to_live
:   > The rgw retention of persistent topics by time (seconds)
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `0`

rgw_topic_persistency_max_retries
:   > The maximum number sending a persistent notification would be tried.
    > Note that the value of one would mean no retries, and the value of
    > zero would mean that the notification would be tried indefinitely
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `0`

rgw_topic_persistency_sleep_duration
:   > The minimum time (in seconds) between two tries of the same persistent
    > notification. note that the actual time between the tries may be
    > longer
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `0`

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
