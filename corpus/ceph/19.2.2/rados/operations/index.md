---
collection: ceph
version: "19.2.2"
title: "Cluster Operations"
source_url: https://docs.ceph.com/en/squid/rados/operations/
fetched_at: 2026-07-27T16:39:28+00:00
---
# Cluster Operations

|  |  |
| --- | --- |
| High-level Operations High-level cluster operations consist primarily of starting, stopping, and restarting a cluster with the `ceph` service; checking the cluster’s health; and, monitoring an operating cluster.  - [Operating a Cluster](operating/index.md) - [Health checks](health-checks/index.md) - [Monitoring a Cluster](monitoring/index.md) - [Monitoring OSDs and PGs](monitoring-osd-pg/index.md) - [User Management](user-management/index.md) - [PG Calc](pgcalc/index.md) | Data Placement Once you have your cluster up and running, you may begin working with data placement. Ceph supports petabyte-scale data storage clusters, with storage pools and placement groups that distribute data across the cluster using Ceph’s CRUSH algorithm.  - [Data Placement Overview](data-placement/index.md) - [Pools](pools/index.md) - [Erasure code](erasure-code/index.md) - [Cache Tiering](cache-tiering/index.md) - [Placement Groups](placement-groups/index.md) - [Placement Group States](pg-states/index.md) - [Placement Group Concepts](pg-concepts/index.md) - [Using pg-upmap](upmap/index.md) - [Operating the Read (Primary) Balancer](read-balancer/index.md) - [Balancer Module](balancer/index.md) - [CRUSH Maps](crush-map/index.md) - [Manually editing the CRUSH Map](crush-map-edits/index.md) - [Stretch Clusters](stretch-mode/index.md) - [Configuring Monitor Election Strategies](change-mon-elections/index.md) |
| Low-level Operations Low-level cluster operations consist of starting, stopping, and restarting a particular daemon within a cluster; changing the settings of a particular daemon or subsystem; and, adding a daemon to the cluster or removing a daemon from the cluster. The most common use cases for low-level operations include growing or shrinking the Ceph cluster and replacing legacy or failed hardware with new hardware.  - [Adding/Removing OSDs](add-or-rm-osds/index.md) - [Adding/Removing Monitors](add-or-rm-mons/index.md) - [Device Management](devices/index.md) - [BlueStore Migration](bluestore-migration/index.md) - [Command Reference](control/index.md) | Troubleshooting Ceph is still on the leading edge, so you may encounter situations that require you to evaluate your Ceph configuration and modify your logging and debugging settings to identify and remedy issues you are encountering with your cluster.  - [The Ceph Community](../troubleshooting/community/index.md) - [Troubleshooting Monitors](../troubleshooting/troubleshooting-mon/index.md) - [Troubleshooting OSDs](../troubleshooting/troubleshooting-osd/index.md) - [Troubleshooting PGs](../troubleshooting/troubleshooting-pg/index.md) - [Logging and Debugging](../troubleshooting/log-and-debug/index.md) - [CPU Profiling](../troubleshooting/cpu-profiling/index.md) - [Memory Profiling](../troubleshooting/memory-profiling/index.md) |

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
