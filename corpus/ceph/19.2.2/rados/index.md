---
collection: ceph
version: "19.2.2"
title: "Ceph Storage Cluster"
source_url: https://docs.ceph.com/en/squid/rados/
fetched_at: 2026-07-27T16:38:46+00:00
---
# Ceph Storage Cluster

The [Ceph Storage Cluster](../glossary/index.md#term-Ceph-Storage-Cluster) is the foundation for all Ceph deployments.
Based upon RADOS, Ceph
Storage Clusters consist of several types of daemons:

> 1. a [Ceph OSD Daemon](../glossary/index.md#term-Ceph-OSD-Daemon) (OSD) stores data as objects on a storage node
> 2. a [Ceph Monitor](../glossary/index.md#term-Ceph-Monitor) (MON) maintains a master copy of the cluster map.
> 3. a [Ceph Manager](../glossary/index.md#term-Ceph-Manager) manager daemon

A Ceph Storage Cluster might contain thousands of storage nodes. A
minimal system has at least one Ceph Monitor and two Ceph OSD
Daemons for data replication.

The Ceph File System, Ceph Object Storage and Ceph Block Devices read data from
and write data to the Ceph Storage Cluster.

### Config and Deploy

Ceph Storage Clusters have a few required settings, but most configuration
settings have default values. A typical deployment uses a deployment tool
to define a cluster and bootstrap a monitor. See [Cephadm](../cephadm/index.md#cephadm) for details.

- [Configuration](configuration/index.md)
  - [Storage devices](configuration/storage-devices/index.md)
  - [Configuring Ceph](configuration/ceph-conf/index.md)
  - [Common Settings](configuration/common/index.md)
  - [Networks](configuration/common/index.md#networks)
  - [Temporary Directory](configuration/common/index.md#temporary-directory)
  - [Monitors](configuration/common/index.md#monitors)
  - [Authentication](configuration/common/index.md#authentication)
  - [OSDs](configuration/common/index.md#osds)
  - [Heartbeats](configuration/common/index.md#heartbeats)
  - [Logs / Debugging](configuration/common/index.md#logs-debugging)
  - [Example ceph.conf](configuration/common/index.md#example-ceph-conf)
  - [Naming Clusters (deprecated)](configuration/common/index.md#naming-clusters-deprecated)
  - [Network Settings](configuration/network-config-ref/index.md)
  - [Messenger v2 protocol](configuration/msgr2/index.md)
  - [Auth Settings](configuration/auth-config-ref/index.md)
  - [Monitor Settings](configuration/mon-config-ref/index.md)
  - [Looking up Monitors through DNS](configuration/mon-lookup-dns/index.md)
  - [Heartbeat Settings](configuration/mon-osd-interaction/index.md)
  - [OSD Settings](configuration/osd-config-ref/index.md)
  - [DmClock Settings](configuration/mclock-config-ref/index.md)
  - [BlueStore Settings](configuration/bluestore-config-ref/index.md)
  - [FileStore Settings](configuration/filestore-config-ref/index.md)
  - [Journal Settings](configuration/journal-ref/index.md)
  - [Pool, PG & CRUSH Settings](configuration/pool-pg-config-ref/index.md)
  - [General Settings](configuration/general-config-ref/index.md)

### Operations

Once you have deployed a Ceph Storage Cluster, you may begin operating
your cluster.

- [Operations](operations/index.md)
  - [Operating a Cluster](operations/operating/index.md)
  - [Health checks](operations/health-checks/index.md)
  - [Monitoring a Cluster](operations/monitoring/index.md)
  - [Monitoring OSDs and PGs](operations/monitoring-osd-pg/index.md)
  - [User Management](operations/user-management/index.md)
  - [PG Calc](operations/pgcalc/index.md)
  - [Data Placement Overview](operations/data-placement/index.md)
  - [Pools](operations/pools/index.md)
  - [Erasure code](operations/erasure-code/index.md)
  - [Cache Tiering](operations/cache-tiering/index.md)
  - [Placement Groups](operations/placement-groups/index.md)
  - [Placement Group States](operations/pg-states/index.md)
  - [Placement Group Concepts](operations/pg-concepts/index.md)
  - [Using pg-upmap](operations/upmap/index.md)
  - [Operating the Read (Primary) Balancer](operations/read-balancer/index.md)
  - [Balancer Module](operations/balancer/index.md)
  - [CRUSH Maps](operations/crush-map/index.md)
  - [Manually editing the CRUSH Map](operations/crush-map-edits/index.md)
  - [Stretch Clusters](operations/stretch-mode/index.md)
  - [Configuring Monitor Election Strategies](operations/change-mon-elections/index.md)
  - [Adding/Removing OSDs](operations/add-or-rm-osds/index.md)
  - [Adding/Removing Monitors](operations/add-or-rm-mons/index.md)
  - [Device Management](operations/devices/index.md)
  - [BlueStore Migration](operations/bluestore-migration/index.md)
  - [Command Reference](operations/control/index.md)
  - [The Ceph Community](troubleshooting/community/index.md)
  - [Troubleshooting Monitors](troubleshooting/troubleshooting-mon/index.md)
  - [Troubleshooting OSDs](troubleshooting/troubleshooting-osd/index.md)
  - [Troubleshooting PGs](troubleshooting/troubleshooting-pg/index.md)
  - [Logging and Debugging](troubleshooting/log-and-debug/index.md)
  - [CPU Profiling](troubleshooting/cpu-profiling/index.md)
  - [Memory Profiling](troubleshooting/memory-profiling/index.md)

- [Man Pages](man/index.md)

### APIs

Most Ceph deployments use [Ceph Block Devices](../rbd/index.md), [Ceph Object Storage](../radosgw/index.md) and/or the
[Ceph File System](../cephfs/index.md). You may also develop applications that talk directly to
the Ceph Storage Cluster.

- [APIs](api/index.md)
  - [Introduction to librados](api/librados-intro/index.md)
  - [librados (C)](api/librados/index.md)
  - [librados (C++)](api/libradospp/index.md)
  - [librados (Python)](api/python/index.md)
  - [libcephsqlite (SQLite)](api/libcephsqlite/index.md)
  - [object class](api/objclass-sdk/index.md)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
