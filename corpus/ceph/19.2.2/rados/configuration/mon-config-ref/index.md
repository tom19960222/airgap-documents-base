---
collection: ceph
version: "19.2.2"
title: "Monitor Config Reference"
source_url: https://docs.ceph.com/en/squid/rados/configuration/mon-config-ref/
fetched_at: 2026-07-27T16:39:32+00:00
---
# Monitor Config Reference

Understanding how to configure a [Ceph Monitor](../../../glossary/index.md#term-Ceph-Monitor) is an important part of
building a reliable [Ceph Storage Cluster](../../../glossary/index.md#term-Ceph-Storage-Cluster). **All Ceph Storage Clusters
have at least one monitor**. The monitor complement usually remains fairly
consistent, but you can add, remove or replace a monitor in a cluster. See
[Adding/Removing a Monitor](../../operations/add-or-rm-mons.md) for details.

## Background

Ceph Monitors maintain a “master copy” of the [Cluster Map](../../../glossary/index.md#term-Cluster-Map).

The [Cluster Map](../../../glossary/index.md#term-Cluster-Map) makes it possible for [Ceph client](../../../glossary/index.md#term-Ceph-Client)s to
determine the location of all Ceph Monitors, Ceph OSD Daemons, and Ceph
Metadata Servers. Clients do this by connecting to one Ceph Monitor and
retrieving a current cluster map. Ceph clients must connect to a Ceph Monitor
before they can read from or write to Ceph OSD Daemons or Ceph Metadata
Servers. A Ceph client that has a current copy of the cluster map and the CRUSH
algorithm can compute the location of any RADOS object within the cluster. This
makes it possible for Ceph clients to talk directly to Ceph OSD Daemons. Direct
communication between clients and Ceph OSD Daemons improves upon traditional
storage architectures that required clients to communicate with a central
component. See [Scalability and High Availability](../../../architecture.md#scalability-and-high-availability) for more on this subject.

The Ceph Monitor’s primary function is to maintain a master copy of the cluster
map. Monitors also provide authentication and logging services. All changes in
the monitor services are written by the Ceph Monitor to a single Paxos
instance, and Paxos writes the changes to a key/value store. This provides
strong consistency. Ceph Monitors are able to query the most recent version of
the cluster map during sync operations, and they use the key/value store’s
snapshots and iterators (using RocksDB) to perform store-wide synchronization.

![](../../../_images/ditaa-d93220ac740fbc1df6152f91b390a95f9b36f9c5.png)

### Cluster Maps

The cluster map is a composite of maps, including the monitor map, the OSD map,
the placement group map and the metadata server map. The cluster map tracks a
number of important things: which processes are `in` the Ceph Storage Cluster;
which processes that are `in` the Ceph Storage Cluster are `up` and running
or `down`; whether, the placement groups are `active` or `inactive`, and
`clean` or in some other state; and, other details that reflect the current
state of the cluster such as the total amount of storage space, and the amount
of storage used.

When there is a significant change in the state of the cluster--e.g., a Ceph OSD
Daemon goes down, a placement group falls into a degraded state, etc.--the
cluster map gets updated to reflect the current state of the cluster.
Additionally, the Ceph Monitor also maintains a history of the prior states of
the cluster. The monitor map, OSD map, placement group map and metadata server
map each maintain a history of their map versions. We call each version an
“epoch.”

When operating your Ceph Storage Cluster, keeping track of these states is an
important part of your system administration duties. See [Monitoring a Cluster](../../operations/monitoring.md)
and [Monitoring OSDs and PGs](../../operations/monitoring-osd-pg.md) for additional details.

### Monitor Quorum

Our Configuring ceph section provides a trivial [Ceph configuration file](../ceph-conf/index.md#monitors) that
provides for one monitor in the test cluster. A cluster will run fine with a
single monitor; however, **a single monitor is a single-point-of-failure**. To
ensure high availability in a production Ceph Storage Cluster, you should run
Ceph with multiple monitors so that the failure of a single monitor **WILL NOT**
bring down your entire cluster.

When a Ceph Storage Cluster runs multiple Ceph Monitors for high availability,
Ceph Monitors use [Paxos](https://en.wikipedia.org/wiki/Paxos_(computer_science)) to establish consensus about the master cluster map.
A consensus requires a majority of monitors running to establish a quorum for
consensus about the cluster map (e.g., 1; 2 out of 3; 3 out of 5; 4 out of 6;
etc.).

mon_force_quorum_join
:   > Force monitor to join quorum even if it has been previously removed
    > from the map
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`

### Consistency

When you add monitor settings to your Ceph configuration file, you need to be
aware of some of the architectural aspects of Ceph Monitors. **Ceph imposes
strict consistency requirements** for a Ceph monitor when discovering another
Ceph Monitor within the cluster. Although Ceph Clients and other Ceph daemons
use the Ceph configuration file to discover monitors, monitors discover each
other using the monitor map (monmap), not the Ceph configuration file.

A Ceph Monitor always refers to the local copy of the monmap when discovering
other Ceph Monitors in the Ceph Storage Cluster. Using the monmap instead of the
Ceph configuration file avoids errors that could break the cluster (e.g., typos
in `ceph.conf` when specifying a monitor address or port). Since monitors use
monmaps for discovery and they share monmaps with clients and other Ceph
daemons, **the monmap provides monitors with a strict guarantee that their
consensus is valid.**

Strict consistency also applies to updates to the monmap. As with any other
updates on the Ceph Monitor, changes to the monmap always run through a
distributed consensus algorithm called [Paxos](https://en.wikipedia.org/wiki/Paxos_(computer_science)). The Ceph Monitors must agree on
each update to the monmap, such as adding or removing a Ceph Monitor, to ensure
that each monitor in the quorum has the same version of the monmap. Updates to
the monmap are incremental so that Ceph Monitors have the latest agreed upon
version, and a set of previous versions. Maintaining a history enables a Ceph
Monitor that has an older version of the monmap to catch up with the current
state of the Ceph Storage Cluster.

If Ceph Monitors were to discover each other through the Ceph configuration file
instead of through the monmap, additional risks would be introduced because
Ceph configuration files are not updated and distributed automatically. Ceph
Monitors might inadvertently use an older Ceph configuration file, fail to
recognize a Ceph Monitor, fall out of a quorum, or develop a situation where
[Paxos](https://en.wikipedia.org/wiki/Paxos_(computer_science)) is not able to determine the current state of the system accurately.

### Bootstrapping Monitors

In most configuration and deployment cases, tools that deploy Ceph help
bootstrap the Ceph Monitors by generating a monitor map for you (e.g.,
`cephadm`, etc). A Ceph Monitor requires a few explicit
settings:

- **Filesystem ID**: The `fsid` is the unique identifier for your
  object store. Since you can run multiple clusters on the same
  hardware, you must specify the unique ID of the object store when
  bootstrapping a monitor. Deployment tools usually do this for you
  (e.g., `cephadm` can call a tool like `uuidgen`), but you
  may specify the `fsid` manually too.
- **Monitor ID**: A monitor ID is a unique ID assigned to each monitor within
  the cluster. It is an alphanumeric value, and by convention the identifier
  usually follows an alphabetical increment (e.g., `a`, `b`, etc.). This
  can be set in a Ceph configuration file (e.g., `[mon.a]`, `[mon.b]`, etc.),
  by a deployment tool, or using the `ceph` commandline.
- **Keys**: The monitor must have secret keys. A deployment tool such as
  `cephadm` usually does this for you, but you may
  perform this step manually too. See [Monitor Keyrings](../../../dev/mon-bootstrap.md#secret-keys) for details.

For additional details on bootstrapping, see [Bootstrapping a Monitor](../../../dev/mon-bootstrap.md).

## Configuring Monitors

To apply configuration settings to the entire cluster, enter the configuration
settings under `[global]`. To apply configuration settings to all monitors in
your cluster, enter the configuration settings under `[mon]`. To apply
configuration settings to specific monitors, specify the monitor instance
(e.g., `[mon.a]`). By convention, monitor instance names use alpha notation.

```ini
[global]

[mon]

[mon.a]

[mon.b]

[mon.c]
```

### Minimum Configuration

The bare minimum monitor settings for a Ceph monitor via the Ceph configuration
file include a hostname and a network address for each monitor. You can configure
these under `[mon]` or under the entry for a specific monitor.

```ini
[global]
        mon_host = 10.0.0.2,10.0.0.3,10.0.0.4
```

```ini
[mon.a]
        host = hostname1
        mon_addr = 10.0.0.10:6789
```

See the [Network Configuration Reference](../network-config-ref.md) for details.

> **Note:**
>
> This minimum configuration for monitors assumes that a deployment
> tool generates the `fsid` and the `mon.` key for you.

Once you deploy a Ceph cluster, you **SHOULD NOT** change the IP addresses of
monitors. However, if you decide to change the monitor’s IP address, you
must follow a specific procedure. See [Changing a Monitor’s IP Address](../../operations/add-or-rm-mons/index.md#changing-a-monitor-s-ip-address) for
details.

Monitors can also be found by clients by using DNS SRV records. See [Monitor lookup through DNS](../mon-lookup-dns.md) for details.

### Cluster ID

Each Ceph Storage Cluster has a unique identifier (`fsid`). If specified, it
usually appears under the `[global]` section of the configuration file.
Deployment tools usually generate the `fsid` and store it in the monitor map,
so the value may not appear in a configuration file. The `fsid` makes it
possible to run daemons for multiple clusters on the same hardware.

fsid
:   > The cluster ID. One per cluster. May be generated by a deployment tool
    > if not specified.
    >
    > type:
    > :   `uuid`
    >
    > > **Note:**
    > >
    > > Do not set this value if you use a deployment tool that does it for you.

### Initial Members

We recommend running a production Ceph Storage Cluster with at least three Ceph
Monitors to ensure high availability. When you run multiple monitors, you may
specify the initial monitors that must be members of the cluster in order to
establish a quorum. This may reduce the time it takes for your cluster to come
online.

```ini
[mon]
        mon_initial_members = a,b,c
```

mon_initial_members
:   > The IDs of initial monitors in a cluster during startup. If specified,
    > Ceph requires an odd number of monitors to form an initial quorum
    > (e.g., 3).
    >
    > type:
    > :   `str`
    >
    > > **Note:**
    > >
    > > A *majority* of monitors in your cluster must be able to reach each other in order to establish a quorum. You can decrease the initial number of monitors to establish a quorum with this setting.

### Data

Ceph provides a default path where Ceph Monitors store data. For optimal
performance in a production Ceph Storage Cluster, we recommend running Ceph
Monitors on separate hosts and drives from Ceph OSD Daemons. As RocksDB uses
`mmap()` for writing the data, Ceph Monitors flush their data from memory to disk
very often, which can interfere with Ceph OSD Daemon workloads if the data
store is co-located with the OSD Daemons.

In Ceph versions 0.58 and earlier, Ceph Monitors store their data in plain files. This
approach allows users to inspect monitor data with common tools like `ls`
and `cat`. However, this approach didn’t provide strong consistency.

In Ceph versions 0.59 and later, Ceph Monitors store their data as key/value
pairs. Ceph Monitors require [ACID](https://en.wikipedia.org/wiki/ACID) transactions. Using a data store prevents
recovering Ceph Monitors from running corrupted versions through Paxos, and it
enables multiple modification operations in one single atomic batch, among other
advantages.

Generally, we do not recommend changing the default data location. If you modify
the default location, we recommend that you make it uniform across Ceph Monitors
by setting it in the `[mon]` section of the configuration file.

mon_data
:   > The monitor’s data location.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `/var/lib/ceph/mon/$cluster-$id`

mon_data_size_warn
:   > Raise `HEALTH_WARN` status when a monitor’s data store grows to be
    > larger than this size, 15GB by default.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `15Gi`

mon_data_avail_warn
:   > Raise `HEALTH_WARN` status when the filesystem that houses a
    > monitor’s data store reports that its available capacity is less than
    > or equal to this percentage .
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `30`

mon_data_avail_crit
:   > Raise `HEALTH_ERR` status when the filesystem that houses a
    > monitor’s data store reports that its available capacity is less than
    > or equal to this percentage.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `5`

mon_warn_on_crush_straw_calc_version_zero
:   > Raise `HEALTH_WARN` when the CRUSH `straw_calc_version` is zero.
    > See [CRUSH map tunables](../../operations/crush-map/index.md#crush-map-tunables) for details.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`

mon_warn_on_legacy_crush_tunables
:   > Raise `HEALTH_WARN` when CRUSH tunables are too old (older than
    > `mon_min_crush_required_version`)
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`
    >
    > see also:
    > :   [`mon_crush_min_required_version`](index.md#confval-mon_crush_min_required_version)

mon_crush_min_required_version
:   > The minimum tunable profile required by the cluster. See [CRUSH
    > map tunables](../../operations/crush-map/index.md#crush-map-tunables) for details.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `hammer`
    >
    > see also:
    > :   [`mon_warn_on_legacy_crush_tunables`](index.md#confval-mon_warn_on_legacy_crush_tunables)

mon_warn_on_osd_down_out_interval_zero
:   > Raise `HEALTH_WARN` when `mon_osd_down_out_interval` is zero.
    > Having this option set to zero on the leader acts much like the
    > `noout` flag. It’s hard to figure out what’s going wrong with
    > clusters without the `noout` flag set but acting like that just the
    > same, so we report a warning in this case.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`
    >
    > see also:
    > :   [`mon_osd_down_out_interval`](../mon-osd-interaction/index.md#confval-mon_osd_down_out_interval)

mon_warn_on_slow_ping_ratio
:   > Raise `HEALTH_WARN` when any heartbeat between OSDs exceeds
    > `mon_warn_on_slow_ping_ratio` of `osd_heartbeat_grace`.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.05`
    >
    > see also:
    > :   [`osd_heartbeat_grace`](../mon-osd-interaction/index.md#confval-osd_heartbeat_grace), [`mon_warn_on_slow_ping_time`](index.md#confval-mon_warn_on_slow_ping_time)

mon_warn_on_slow_ping_time
:   > Override `mon_warn_on_slow_ping_ratio` with a specific value. Raise
    > `HEALTH_WARN` if any heartbeat between OSDs exceeds
    > `mon_warn_on_slow_ping_time` milliseconds. The default is 0
    > (disabled).
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.0`
    >
    > see also:
    > :   [`mon_warn_on_slow_ping_ratio`](index.md#confval-mon_warn_on_slow_ping_ratio)

mon_warn_on_pool_no_redundancy
:   > Raise `HEALTH_WARN` if any pool is configured with no replicas.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`
    >
    > see also:
    > :   [`osd_pool_default_size`](../pool-pg-config-ref/index.md#confval-osd_pool_default_size), [`osd_pool_default_min_size`](../pool-pg-config-ref/index.md#confval-osd_pool_default_min_size)

mon_cache_target_full_warn_ratio
:   > Position between pool’s `cache_target_full` and
    > `target_max_object` where we start warning
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.66`

mon_health_to_clog
:   > Enable sending a health summary to the cluster log periodically.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`

mon_health_to_clog_tick_interval
:   > How often (in seconds) the monitor sends a health summary to the
    > cluster log (a non-positive number disables). If current health
    > summary is empty or identical to the last time, monitor will not send
    > it to cluster log.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `1 minute`

mon_health_to_clog_interval
:   > How often (in seconds) the monitor sends a health summary to the
    > cluster log (a non-positive number disables). Monitors will always
    > send a summary to the cluster log whether or not it differs from the
    > previous summary.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `10 minutes`
    >
    > see also:
    > :   [`mon_health_to_clog`](index.md#confval-mon_health_to_clog)

### Storage Capacity

When a Ceph Storage Cluster gets close to its maximum capacity
(see``mon_osd_full ratio``), Ceph prevents you from writing to or reading from OSDs
as a safety measure to prevent data loss. Therefore, letting a
production Ceph Storage Cluster approach its full ratio is not a good practice,
because it sacrifices high availability. The default full ratio is `.95`, or
95% of capacity. This a very aggressive setting for a test cluster with a small
number of OSDs.

> **Tip:**
>
> When monitoring your cluster, be alert to warnings related to the
> `nearfull` ratio. This means that a failure of some OSDs could result
> in a temporary service disruption if one or more OSDs fails. Consider adding
> more OSDs to increase storage capacity.

A common scenario for test clusters involves a system administrator removing an
OSD from the Ceph Storage Cluster, watching the cluster rebalance, then removing
another OSD, and another, until at least one OSD eventually reaches the full
ratio and the cluster locks up. We recommend a bit of capacity
planning even with a test cluster. Planning enables you to gauge how much spare
capacity you will need in order to maintain high availability. Ideally, you want
to plan for a series of Ceph OSD Daemon failures where the cluster can recover
to an `active+clean` state without replacing those OSDs
immediately. Cluster operation continues in the `active+degraded` state, but this
is not ideal for normal operation and should be addressed promptly.

The following diagram depicts a simplistic Ceph Storage Cluster containing 33
Ceph Nodes with one OSD per host, each OSD reading from
and writing to a 3TB drive. So this exemplary Ceph Storage Cluster has a maximum
actual capacity of 99TB. With a `mon osd full ratio` of `0.95`, if the Ceph
Storage Cluster falls to 5TB of remaining capacity, the cluster will not allow
Ceph Clients to read and write data. So the Ceph Storage Cluster’s operating
capacity is 95TB, not 99TB.

![](../../../_images/ditaa-711402e8fde8ea6a9ae1a39bb27a1b5431a0d8de.png)

It is normal in such a cluster for one or two OSDs to fail. A less frequent but
reasonable scenario involves a rack’s router or power supply failing, which
brings down multiple OSDs simultaneously (e.g., OSDs 7-12). In such a scenario,
you should still strive for a cluster that can remain operational and achieve an
`active + clean` state--even if that means adding a few hosts with additional
OSDs in short order. If your capacity utilization is too high, you may not lose
data, but you could still sacrifice data availability while resolving an outage
within a failure domain if capacity utilization of the cluster exceeds the full
ratio. For this reason, we recommend at least some rough capacity planning.

Identify two numbers for your cluster:

1. The number of OSDs.
2. The total capacity of the cluster

If you divide the total capacity of your cluster by the number of OSDs in your
cluster, you will find the mean average capacity of an OSD within your cluster.
Consider multiplying that number by the number of OSDs you expect will fail
simultaneously during normal operations (a relatively small number). Finally
multiply the capacity of the cluster by the full ratio to arrive at a maximum
operating capacity; then, subtract the number of amount of data from the OSDs
you expect to fail to arrive at a reasonable full ratio. Repeat the foregoing
process with a higher number of OSD failures (e.g., a rack of OSDs) to arrive at
a reasonable number for a near full ratio.

The following settings only apply on cluster creation and are then stored in
the OSDMap. To clarify, in normal operation the values that are used by OSDs
are those found in the OSDMap, not those in the configuration file or central
config store.

```ini
[global]
        mon_osd_full_ratio = .80
        mon_osd_backfillfull_ratio = .75
        mon_osd_nearfull_ratio = .70
```

`mon_osd_full_ratio`

Description:
:   The threshold percentage of device space utilized before an OSD is
    considered `full`.

Type:
:   Float

Default:
:   `0.95`

`mon_osd_backfillfull_ratio`

Description:
:   The threshold percentage of device space utilized before an OSD is
    considered too `full` to backfill.

Type:
:   Float

Default:
:   `0.90`

`mon_osd_nearfull_ratio`

Description:
:   The threshold percentage of device space used before an OSD is
    considered `nearfull`.

Type:
:   Float

Default:
:   `0.85`

> **Tip:**
>
> If some OSDs are nearfull, but others have plenty of capacity, you
> may have an inaccurate CRUSH weight set for the nearfull OSDs.

> **Tip:**
>
> These settings only apply during cluster creation. Afterwards they need
> to be changed in the OSDMap using `ceph osd set-nearfull-ratio` and
> `ceph osd set-full-ratio`

### Heartbeat

Ceph monitors know about the cluster by requiring reports from each OSD, and by
receiving reports from OSDs about the status of their neighboring OSDs. Ceph
provides reasonable default settings for monitor/OSD interaction; however, you
may modify them as needed. See [Monitor/OSD Interaction](../mon-osd-interaction.md) for details.

### Monitor Store Synchronization

When you run a production cluster with multiple monitors (recommended), each
monitor checks to see if a neighboring monitor has a more recent version of the
cluster map (e.g., a map in a neighboring monitor with one or more epoch numbers
higher than the most current epoch in the map of the instant monitor).
Periodically, one monitor in the cluster may fall behind the other monitors to
the point where it must leave the quorum, synchronize to retrieve the most
current information about the cluster, and then rejoin the quorum. For the
purposes of synchronization, monitors may assume one of three roles:

1. **Leader**: The Leader is the first monitor to achieve the most recent
   Paxos version of the cluster map.
2. **Provider**: The Provider is a monitor that has the most recent version
   of the cluster map, but wasn’t the first to achieve the most recent version.
3. **Requester:** A Requester is a monitor that has fallen behind the leader
   and must synchronize in order to retrieve the most recent information about
   the cluster before it can rejoin the quorum.

These roles enable a leader to delegate synchronization duties to a provider,
which prevents synchronization requests from overloading the leader--improving
performance. In the following diagram, the requester has learned that it has
fallen behind the other monitors. The requester asks the leader to synchronize,
and the leader tells the requester to synchronize with a provider.

![](../../../_images/ditaa-af0ce2210eafb917a47884a8edbcbc94b581639b.png)

Synchronization always occurs when a new monitor joins the cluster. During
runtime operations, monitors may receive updates to the cluster map at different
times. This means the leader and provider roles may migrate from one monitor to
another. If this happens while synchronizing (e.g., a provider falls behind the
leader), the provider can terminate synchronization with a requester.

Once synchronization is complete, Ceph performs trimming across the cluster.
Trimming requires that the placement groups are `active+clean`.

mon_sync_timeout
:   > Number of seconds the monitor will wait for the next update message
    > from its sync provider before it gives up and bootstrap again.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `1 minute`

mon_sync_max_payload_size
:   > The maximum size for a sync payload (in bytes).
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `1Mi`

paxos_max_join_drift
:   > The maximum Paxos iterations before we must first sync the monitor
    > data stores. When a monitor finds that its peer is too far ahead of
    > it, it will first sync with data stores before moving on.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `10`

paxos_stash_full_interval
:   > How often (in commits) to stash a full copy of the PaxosService state.
    > Current this setting only affects `mds`, `mon`, `auth` and
    > `mgr` PaxosServices.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `25`

paxos_propose_interval
:   > Gather updates for this time interval before proposing a map update.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `1.0`

paxos_min
:   > The minimum number of Paxos states to keep around
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `500`

paxos_min_wait
:   > The minimum amount of time to gather updates after a period of
    > inactivity.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.05`

paxos_trim_min
:   > Number of extra proposals tolerated before trimming
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `250`

paxos_trim_max
:   > The maximum number of extra proposals to trim at a time
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `500`

paxos_service_trim_min
:   > The minimum amount of versions to trigger a trim (0 disables it)
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `250`

paxos_service_trim_max
:   > The maximum amount of versions to trim during a single proposal (0
    > disables it)
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `500`

paxos_service_trim_max_multiplier
:   > factor by which paxos_service_trim_max will be multiplied to get a new
    > upper bound when trim sizes are high (0 disables it)
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `20`
    >
    > min:
    > :   `0`

mon_mds_force_trim_to
:   > Force monitor to trim mdsmaps up to but not including this FSMap
    > epoch. A value of 0 disables (the default) this config. This command
    > is potentially dangerous, use with care.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `0`

mon_osd_force_trim_to
:   > Force monitor to trim osdmaps to this point, even if there is PGs not
    > clean at the specified epoch (0 disables it. dangerous, use with care)
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `0`

mon_osd_cache_size
:   > The size of osdmaps cache, not to rely on underlying store’s cache
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `500`

mon_election_timeout
:   > On election proposer, maximum waiting time for all ACKs in seconds.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `5.0`

mon_lease
:   > The length (in seconds) of the lease on the monitor’s versions.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `5.0`

mon_lease_renew_interval_factor
:   > `mon_lease` \* `mon_lease_renew_interval_factor` will be the
    > interval for the Leader to renew the other monitor’s leases. The
    > factor should be less than `1.0`.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.6`
    >
    > allowed range:
    > :   `[0, 0.9999999]`
    >
    > see also:
    > :   [`mon_lease`](index.md#confval-mon_lease)

mon_lease_ack_timeout_factor
:   > The Leader will wait `mon_lease` \* `mon_lease_ack_timeout_factor`
    > for the Providers to acknowledge the lease extension.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `2.0`
    >
    > allowed range:
    > :   `[1.0001, 100]`
    >
    > see also:
    > :   [`mon_lease`](index.md#confval-mon_lease)

mon_accept_timeout_factor
:   > The Leader will wait `mon_lease` \* `mon_accept_timeout_factor`
    > for the Requester(s) to accept a Paxos update. It is also used during
    > the Paxos recovery phase for similar purposes.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `2.0`
    >
    > see also:
    > :   [`mon_lease`](index.md#confval-mon_lease)

mon_min_osdmap_epochs
:   > Minimum number of OSD map epochs to keep at all times.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `500`

mon_max_log_epochs
:   > Maximum number of Log epochs the monitor should keep.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `500`

### Clock

Ceph daemons pass critical messages to each other, which must be processed
before daemons reach a timeout threshold. If the clocks in Ceph monitors
are not synchronized, it can lead to a number of anomalies. For example:

- Daemons ignoring received messages (e.g., timestamps outdated)
- Timeouts triggered too soon/late when a message wasn’t received in time.

See [Monitor Store Synchronization](index.md#monitor-store-synchronization) for details.

> **Tip:**
>
> You must configure NTP or PTP daemons on your Ceph monitor hosts to
> ensure that the monitor cluster operates with synchronized clocks.
> It can be advantageous to have monitor hosts sync with each other
> as well as with multiple quality upstream time sources.

Clock drift may still be noticeable with NTP even though the discrepancy is not
yet harmful. Ceph’s clock drift / clock skew warnings may get triggered even
though NTP maintains a reasonable level of synchronization. Increasing your
clock drift may be tolerable under such circumstances; however, a number of
factors such as workload, network latency, configuring overrides to default
timeouts and the [Monitor Store Synchronization](index.md#monitor-store-synchronization) settings may influence
the level of acceptable clock drift without compromising Paxos guarantees.

Ceph provides the following tunable options to allow you to find
acceptable values.

mon_tick_interval
:   > A monitor’s tick interval in seconds.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `5`

mon_clock_drift_allowed
:   > allowed clock drift (in seconds) between mons before issuing a health
    > warning
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.05`

mon_clock_drift_warn_backoff
:   > exponential backoff factor for logging clock drift warnings in the
    > cluster log
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `5.0`

mon_timecheck_interval
:   > The time check interval (clock drift check) in seconds for the Leader.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `5 minutes`

mon_timecheck_skew_interval
:   > The time check interval (clock drift check) in seconds when in
    > presence of a skew in seconds for the Leader.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `30.0`
    >
    > see also:
    > :   [`mon_timecheck_interval`](index.md#confval-mon_timecheck_interval)

### Client

mon_client_hunt_interval
:   > The client will try a new monitor every `N` seconds until it
    > establishes a connection.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `3.0`

mon_client_ping_interval
:   > The client will ping the monitor every `N` seconds.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `10.0`

mon_client_max_log_entries_per_message
:   > The maximum number of log entries a monitor will generate per client
    > message.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `1000`

mon_client_bytes
:   > The amount of client message data allowed in memory (in bytes).
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `100Mi`

## Pool settings

Since version v0.94 there is support for pool flags which allow or disallow changes to be made to pools.
Monitors can also disallow removal of pools if appropriately configured. The inconvenience of this guardrail
is far outweighed by the number of accidental pool (and thus data) deletions it prevents.

mon_allow_pool_delete
:   > Should monitors allow pools to be removed, regardless of what the pool
    > flags say?
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`

osd_pool_default_ec_fast_read
:   > Whether to turn on fast read on the pool or not. It will be used as
    > the default setting of newly created erasure coded pools if
    > `fast_read` is not specified at create time.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`

osd_pool_default_flag_hashpspool
:   > set hashpspool (better hashing scheme) flag on new pools
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`

osd_pool_default_flag_nodelete
:   > Set the `nodelete` flag on new pools, which prevents pool removal.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`

osd_pool_default_flag_nopgchange
:   > Set the `nopgchange` flag on new pools. Does not allow the number of
    > PGs to be changed.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`

osd_pool_default_flag_nosizechange
:   > Set the `nosizechange` flag on new pools. Does not allow the
    > `size` to be changed.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`

For more information about the pool flags see [Pool values](../../operations/pools/index.md#setpoolvalues).

## Miscellaneous

mon_max_osd
:   > The maximum number of OSDs allowed in the cluster.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `10000`

mon_globalid_prealloc
:   > The number of global IDs to pre-allocate for clients and daemons in
    > the cluster.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `10000`

mon_subscribe_interval
:   > The refresh interval (in seconds) for subscriptions. The subscription
    > mechanism enables obtaining cluster maps and log information.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `1 day`

mon_stat_smooth_intervals
:   > Ceph will smooth statistics over the last `N` PG maps.
    >
    > type:
    > :   `uint`
    >
    > default:
    > :   `6`
    >
    > min:
    > :   `1`

mon_probe_timeout
:   > Number of seconds the monitor will wait to find peers before
    > bootstrapping.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `2.0`

mon_daemon_bytes
:   > The message memory cap for metadata server and OSD messages (in
    > bytes).
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `400Mi`

mon_max_log_entries_per_event
:   > The maximum number of log entries per event.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `4096`

mon_osd_prime_pg_temp
:   > Enables or disables priming the PGMap with the previous OSDs when an
    > `out` OSD comes back into the cluster. With the `true` setting,
    > clients will continue to use the previous OSDs until the newly `in`
    > OSDs for a PG have peered.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`

mon_osd_prime_pg_temp_max_time
:   > How much time in seconds the monitor should spend trying to prime the
    > PGMap when an out OSD comes back into the cluster.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.5`

mon_osd_prime_pg_temp_max_estimate
:   > Maximum estimate of time spent on each PG before we prime all PGs in
    > parallel.
    >
    > type:
    > :   `float`
    >
    > default:
    > :   `0.25`

mon_mds_skip_sanity
:   > Skip safety assertions on FSMap (in case of bugs where we want to
    > continue anyway). Monitor terminates if the FSMap sanity check fails,
    > but we can disable it by enabling this option.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`

mon_max_mdsmap_epochs
:   > The maximum number of mdsmap epochs to trim during a single proposal.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `500`

mon_config_key_max_entry_size
:   > The maximum size of config-key entry (in bytes)
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `64Ki`

mon_scrub_interval
:   > How often the monitor scrubs its store by comparing the stored
    > checksums with the computed ones for all stored keys. (0 disables it.
    > dangerous, use with care)
    >
    > type:
    > :   `secs`
    >
    > default:
    > :   `1 day`

mon_scrub_max_keys
:   > The maximum number of keys to scrub each time.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `100`

mon_compact_on_start
:   > Compact the database used as Ceph Monitor store on `ceph-mon` start.
    > A manual compaction helps to shrink the monitor database and improve
    > the performance of it if the regular compaction fails to work.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`

mon_compact_on_bootstrap
:   > Compact the database used as Ceph Monitor store on bootstrap. Monitors
    > probe each other to establish a quorum after bootstrap. If a monitor
    > times out before joining the quorum, it will start over and bootstrap
    > again.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`

mon_compact_on_trim
:   > Compact a certain prefix (including paxos) when we trim its old
    > states.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`

mon_cpu_threads
:   > Number of threads for performing CPU intensive work on monitor.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `4`

mon_osd_mapping_pgs_per_chunk
:   > We calculate the mapping from placement group to OSDs in chunks. This
    > option specifies the number of placement groups per chunk.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `4096`

mon_session_timeout
:   > Monitor will terminate inactive sessions stay idle over this time
    > limit.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `5 minutes`

mon_osd_cache_size_min
:   > The minimum amount of bytes to be kept mapped in memory for osd
    > monitor caches.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `128Mi`

mon_memory_target
:   > The amount of bytes pertaining to OSD monitor caches and KV cache to
    > be kept mapped in memory with cache auto-tuning enabled.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `2Gi`

mon_memory_autotune
:   > Autotune the cache memory used for OSD monitors and KV database.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`

## NVMe-oF Monitor Client

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
