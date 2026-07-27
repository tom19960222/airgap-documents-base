---
collection: ceph
version: "19.2.2"
title: "MDS Cache Configuration"
source_url: https://docs.ceph.com/en/squid/cephfs/cache-configuration/
fetched_at: 2026-07-27T16:39:54+00:00
---
# MDS Cache Configuration

The Metadata Server coordinates a distributed cache among all MDS and CephFS
clients. The cache serves to improve metadata access latency and allow clients
to safely (coherently) mutate metadata state (e.g. via chmod). The MDS issues
**capabilities** and **directory entry leases** to indicate what state clients
may cache and what manipulations clients may perform (e.g. writing to a file).

The MDS and clients both try to enforce a cache size. The mechanism for
specifying the MDS cache size is described below. Note that the MDS cache size
is not a hard limit. The MDS always allows clients to lookup new metadata
which is loaded into the cache. This is an essential policy as it avoids
deadlock in client requests (some requests may rely on held capabilities before
capabilities are released).

When the MDS cache is too large, the MDS will **recall** client state so cache
items become unpinned and eligible to be dropped. The MDS can only drop cache
state when no clients refer to the metadata to be dropped. Also described below
is how to configure the MDS recall settings for your workload’s needs. This is
necessary if the internal throttles on the MDS recall can not keep up with the
client workload.

## MDS Cache Size

You can limit the size of the Metadata Server (MDS) cache by a byte count. This
is done through the mds_cache_memory_limit configuration:

mds_cache_memory_limit
:   > This sets a target maximum memory usage of the MDS cache and is the
    > primary tunable to limit the MDS memory usage. The MDS will try to
    > stay under a reservation of this limit (by default 95%; 1 -
    > mds_cache_reservation) by trimming unused metadata in its cache and
    > recalling cached items in the client caches. It is possible for the
    > MDS to exceed this limit due to slow recall from clients. The
    > mds_health_cache_threshold (150%) sets a cache full threshold for when
    > the MDS signals a cluster health warning.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `4Gi`

In addition, you can specify a cache reservation by using the
mds_cache_reservation parameter for MDS operations:

mds_cache_reservation
:   > The cache reservation (memory or inodes) for the MDS cache to
    > maintain. Once the MDS begins dipping into its reservation, it will
    > recall client state until its cache size shrinks to restore the
    > reservation.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.05`

The cache reservation is
limited as a percentage of the memory and is set to 5% by default. The intent
of this parameter is to have the MDS maintain an extra reserve of memory for
its cache for new metadata operations to use. As a consequence, the MDS should
in general operate below its memory limit because it will recall old state from
clients in order to drop unused metadata in its cache.

If the MDS cannot keep its cache under the target size, the MDS will send a
health alert to the Monitors indicating the cache is too large. This is
controlled by the mds_health_cache_threshold configuration which is by
default 150% of the maximum cache size:

mds_health_cache_threshold
:   > threshold for cache size to generate health warning
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `1.5`

Because the cache limit is not a hard limit, potential bugs in the CephFS
client, MDS, or misbehaving applications might cause the MDS to exceed its
cache size. The health warnings are intended to help the operator detect this
situation and make necessary adjustments or investigate buggy clients.

## MDS Cache Trimming

There are two configurations for throttling the rate of cache trimming in the MDS:

mds_cache_trim_threshold
:   > threshold for number of dentries that can be trimmed
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `256Ki`

mds_cache_trim_decay_rate
:   > decay rate for trimming MDS cache throttle
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `1.0`

The intent of the throttle is to prevent the MDS from spending too much time
trimming its cache. This may limit its ability to handle client requests or
perform other upkeep.

The trim configurations control an internal **decay counter**. Anytime metadata
is trimmed from the cache, the counter is incremented. The threshold sets the
maximum size of the counter while the decay rate indicates the exponential half
life for the counter. If the MDS is continually removing items from its cache,
it will reach a steady state of `-ln(0.5)/rate*threshold` items removed per
second.

> **Note:**
>
> Increasing the value of the configuration setting
> `mds_cache_trim_decay_rate` leads to the MDS spending less time
> trimming the cache. To increase the cache trimming rate, set a lower
> value.

The defaults are conservative and may need to be changed for production MDS with
large cache sizes.

## MDS Recall

MDS limits its recall of client state (capabilities/leases) to prevent creating
too much work for itself handling release messages from clients. This is controlled
via the following configurations:

The maximum number of capabilities to recall from a single client in a given recall
event:

mds_recall_max_caps
:   > maximum number of caps to recall from client session in single recall
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `30000B`

The threshold and decay rate for the decay counter on a session:

mds_recall_max_decay_threshold
:   > decay threshold for throttle on recalled caps on a session
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `128Ki`

mds_recall_max_decay_rate
:   > decay rate for throttle on recalled caps on a session
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `1.5`

The session decay counter controls the rate of recall for an individual
session. The behavior of the counter works the same as for cache trimming
above. Each capability that is recalled increments the counter.

There is also a global decay counter that throttles for all session recall:

mds_recall_global_max_decay_threshold
:   > decay threshold for throttle on recalled caps globally
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `128Ki`

its decay rate is the same as `mds_recall_max_decay_rate`. Any recalled
capability for any session also increments this counter.

If clients are slow to release state, the warning “failing to respond to cache
pressure” or `MDS_HEALTH_CLIENT_RECALL` will be reported. Each session’s rate
of release is monitored by another decay counter configured by:

mds_recall_warning_threshold
:   > decay threshold for warning on slow session cap recall
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `256Ki`

mds_recall_warning_decay_rate
:   > decay rate for warning on slow session cap recall
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `60.0`

Each time a capability is released, the counter is incremented. If clients do
not release capabilities quickly enough and there is cache pressure, the
counter will indicate if the client is slow to release state.

Some workloads and client behaviors may require faster recall of client state
to keep up with capability acquisition. It is recommended to increase the above
counters as needed to resolve any slow recall warnings in the cluster health
state.

## MDS Cap Acquisition Throttle

A trivial “find” command on a large directory hierarchy will cause the client
to receive caps significantly faster than it will release. The MDS will try
to have the client reduce its caps below the `mds_max_caps_per_client` limit
but the recall throttles prevent it from catching up to the pace of acquisition.
So the readdir is throttled to control cap acquisition via the following
configurations:

The threshold and decay rate for the readdir cap acquisition decay counter:

mds_session_cap_acquisition_throttle
:   > threshold at which the cap acquisition decay counter throttles
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `100000`

mds_session_cap_acquisition_decay_rate
:   > The half-life for the session cap acquisition counter of caps acquired
    > by readdir. This is used for throttling readdir requests from clients.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `30.0`

The cap acquisition decay counter controls the rate of cap acquisition via
readdir. The behavior of the decay counter is the same as for cache trimming or
caps recall. Each readdir call increments the counter by the number of files in
the result.

mds_session_max_caps_throttle_ratio
:   > ratio of mds_max_caps_per_client that client must exceed before
    > readdir may be throttled by cap acquisition throttle
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `1.1`

mds_cap_acquisition_throttle_retry_request_timeout
:   > timeout in seconds after which a client request is retried due to cap
    > acquisition throttling
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.5`

If the number of caps acquired by the client per session is greater than the
`mds_session_max_caps_throttle_ratio` and cap acquisition decay counter is
greater than `mds_session_cap_acquisition_throttle`, the readdir is throttled.
The readdir request is retried after `mds_cap_acquisition_throttle_retry_request_timeout`
seconds.

## Session Liveness

The MDS also keeps track of whether sessions are quiescent. If a client session
is not utilizing its capabilities or is otherwise quiet, the MDS will begin
recalling state from the session even if it’s not under cache pressure. This
helps the MDS avoid future work when the cluster workload is hot and cache
pressure is forcing the MDS to recall state. The expectation is that a client
not utilizing its capabilities is unlikely to use those capabilities anytime
in the near future.

Determining whether a given session is quiescent is controlled by the following
configuration variables:

mds_session_cache_liveness_magnitude
:   > This is the order of magnitude difference (in base 2) of the internal
    > liveness decay counter and the number of capabilities the session
    > holds. When this difference occurs, the MDS treats the session as
    > quiescent and begins recalling capabilities.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `10B`
    >
    > see also:
    > :   [`mds_session_cache_liveness_decay_rate`](index.md#confval-mds_session_cache_liveness_decay_rate)

mds_session_cache_liveness_decay_rate
:   > This determines how long a session needs to be quiescent before the
    > MDS begins preemptively recalling capabilities. The default of 5
    > minutes will cause 10 halvings of the decay counter after 1 hour, or
    > 1/1024. The default magnitude of 10 (1^10 or 1024) is chosen so that
    > the MDS considers a previously chatty session (approximately) to be
    > quiescent after 1 hour.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `5 minutes`
    >
    > see also:
    > :   [`mds_session_cache_liveness_magnitude`](index.md#confval-mds_session_cache_liveness_magnitude)

The configuration `mds_session_cache_liveness_decay_rate` indicates the
half-life for the decay counter tracking the use of capabilities by the client.
Each time a client manipulates or acquires a capability, the MDS will increment
the counter. This is a rough but effective way to monitor the utilization of the
client cache.

The `mds_session_cache_liveness_magnitude` is a base-2 magnitude difference
of the liveness decay counter and the number of capabilities outstanding for
the session. So if the client has `1*2^20` (1M) capabilities outstanding and
only uses **less** than `1*2^(20-mds_session_cache_liveness_magnitude)` (1K
using defaults), the MDS will consider the client to be quiescent and begin
recall.

## Capability Limit

The MDS also tries to prevent a single client from acquiring too many
capabilities. This helps prevent recovery from taking a long time in some
situations. It is not generally necessary for a client to have such a large
cache. The limit is configured via:

mds_max_caps_per_client
:   > maximum number of capabilities a client may hold
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `1Mi`

It is not recommended to set this value above 5M but it may be helpful with
some workloads.

## Dealing with “clients failing to respond to cache pressure” messages

Every second (or every interval set by the `mds_cache_trim_interval`
configuration paramater), the MDS runs the “cache trim” procedure. One of the
steps of this procedure is “recall client state”. During this step, the MDS
checks every client (session) to determine whether it needs to recall caps.
If any of the following are true, then the MDS needs to recall caps:

1. the cache is full (the `mds_cache_memory_limit` has been exceeded) and
   needs some inodes to be released
2. the client exceeds `mds_max_caps_per_client` (1M by default)
3. the client is inactive

To determine whether a client (a session) is inactive, the session’s
`cache_liveness` parameters is checked and compared with the value:

```
(num_caps >> mds_session_cache_liveness_magnitude)
```

where `mds_session_cache_liveness_magnitude` is a config param (`10` by
default). If `cache_liveness` is smaller than this calculated value, the
session is considered inactive and the MDS sends a “recall caps” request for
all cached caps (the actual recall value is `num_caps -
mds_min_caps_per_client(100)`).

Under certain circumstances, many “recall caps” requests can be sent so quickly
that the health warning is generated: “clients failing to respond to cache
pressure”. If the client does not release the caps fast enough, the MDS repeats
the “recall caps” request one second later. This means that the MDS will send
“recall caps” again and again. The “total” counter of “recall caps” for the
session will grow and grow, and will eventually exceed the “mon warning limit”.

A throttling mechanism, controlled by the `mds_recall_max_decay_threshold`
parameter (126K by default), is available for reducing the rate of “recall
caps” counter growth, but sometimes it is not enough to slow the “recall caps”
counter’s growth rate. If altering the `mds_recall_max_decay_threshold` value
does not sufficiently reduce the rate of the “recall caps” counter’s growth,
decrease `mds_recall_max_caps` incrementally until the “clients failing to
respond to cache pressure” messages no longer appear in the logs.

### Example Scenario

Here is an example. A client is having 20k caps cached. At some moment the
server decides the client is inactive (because the session’s `cache_liveness`
value is low). It starts to ask the client to release caps down to
`mds_min_caps_per_client` value (100 by default). Every second, it
sends recall_caps asking to release `caps_num - mds_min_caps_per_client` caps
(but not more than `mds_recall_max_caps`, which is 30k by default). A client
is starting to release, but is releasing with a rate of (for example) only 100
caps per second.

So in the first second of time, the mds sends recall_caps = 20k - 100 the
second second recall_caps = (20k - 100) - 100 the third second recall_caps =
(20k - 200) - 100 and so on. And every time it sends recall_caps it updates the
session’s recall_caps value, which is calculated how many recall_caps sent in
the last minute. I.e. the counter is growing quickly, eventually exceeding
mds_recall_warning_threshold, which is 128K by default, and ceph starts to
report “failing to respond to cache pressure” warning in the status. Now,
after we set mds_recall_max_caps to 3K, in this situation the mds server sends
only 3K recall_caps per second, and the maximum value the session’s recall_caps
value may have (if the mds is sending 3K every second for at least one minute)
is 60 \* 3K = 180K. This means that it is still possible to achieve
`mds_recall_warning_threshold` but only if a client does not “respond” for a
long time, and as your experiments show it is not the case.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
