---
collection: ceph
version: "19.2.2"
title: "Configuration"
source_url: https://docs.ceph.com/en/squid/rados/configuration/
fetched_at: 2026-07-27T16:39:28+00:00
---
# Configuration

Each Ceph process, daemon, or utility draws its configuration from several
sources on startup. Such sources can include (1) a local configuration, (2) the
monitors, (3) the command line, and (4) environment variables.

Configuration options can be set globally so that they apply (1) to all
daemons, (2) to all daemons or services of a particular type, or (3) to only a
specific daemon, process, or client.

|  |  |
| --- | --- |
| Configuring the Object Store For general object store configuration, refer to the following:  - [Storage devices](storage-devices/index.md) - [Configuring Ceph](ceph-conf/index.md) | Reference To optimize the performance of your cluster, refer to the following:  - [Common Settings](common/index.md) - [Networks](common/index.md#networks) - [Temporary Directory](common/index.md#temporary-directory) - [Monitors](common/index.md#monitors) - [Authentication](common/index.md#authentication) - [OSDs](common/index.md#osds) - [Heartbeats](common/index.md#heartbeats) - [Logs / Debugging](common/index.md#logs-debugging) - [Example ceph.conf](common/index.md#example-ceph-conf) - [Naming Clusters (deprecated)](common/index.md#naming-clusters-deprecated) - [Network Settings](network-config-ref/index.md) - [Messenger v2 protocol](msgr2/index.md) - [Auth Settings](auth-config-ref/index.md) - [Monitor Settings](mon-config-ref/index.md) - [Looking up Monitors through DNS](mon-lookup-dns/index.md) - [Heartbeat Settings](mon-osd-interaction/index.md) - [OSD Settings](osd-config-ref/index.md) - [DmClock Settings](mclock-config-ref/index.md) - [BlueStore Settings](bluestore-config-ref/index.md) - [FileStore Settings](filestore-config-ref/index.md) - [Journal Settings](journal-ref/index.md) - [Pool, PG & CRUSH Settings](pool-pg-config-ref/index.md) - [General Settings](general-config-ref/index.md) |

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
