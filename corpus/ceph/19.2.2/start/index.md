---
collection: ceph
version: "19.2.2"
title: "Intro to Ceph"
source_url: https://docs.ceph.com/en/squid/start/
fetched_at: 2026-07-27T16:38:45+00:00
---
# Intro to Ceph

Ceph can be used to provide [Ceph Object Storage](../glossary/index.md#term-Ceph-Object-Storage) to [Cloud
Platforms](../glossary/index.md#term-Cloud-Platforms) and Ceph can be used to provide [Ceph Block Device](../glossary/index.md#term-Ceph-Block-Device) services
to [Cloud Platforms](../glossary/index.md#term-Cloud-Platforms). Ceph can be used to deploy a [Ceph File
System](../glossary/index.md#term-Ceph-File-System). All [Ceph Storage Cluster](../glossary/index.md#term-Ceph-Storage-Cluster) deployments begin with setting up
each [Ceph Node](../glossary/index.md#term-Ceph-Node) and then setting up the network.

A Ceph Storage Cluster requires the following: at least one Ceph Monitor and at
least one Ceph Manager, and at least as many [Ceph Object Storage
Daemon](../glossary/index.md#term-Ceph-OSD)s (OSDs) as there are copies of a given object stored in the
Ceph cluster (for example, if three copies of a given object are stored in the
Ceph cluster, then at least three OSDs must exist in that Ceph cluster).

The Ceph Metadata Server is necessary to run Ceph File System clients.

> **Note:**
>
> It is a best practice to have a Ceph Manager for each Monitor, but it is not
> necessary.

![](../_images/ditaa-7e48242b2396515796658d962798a9a3fe043816.png)

- **Monitors**: A [Ceph Monitor](../glossary/index.md#term-Ceph-Monitor) (`ceph-mon`) maintains maps of the
  cluster state, including the [monitor map](../rados/operations/monitoring/index.md#display-mon-map), manager
  map, the OSD map, the MDS map, and the CRUSH map. These maps are critical
  cluster state required for Ceph daemons to coordinate with each other.
  Monitors are also responsible for managing authentication between daemons and
  clients. At least three monitors are normally required for redundancy and
  high availability.
- **Managers**: A [Ceph Manager](../glossary/index.md#term-Ceph-Manager) daemon (`ceph-mgr`) is
  responsible for keeping track of runtime metrics and the current
  state of the Ceph cluster, including storage utilization, current
  performance metrics, and system load. The Ceph Manager daemons also
  host python-based modules to manage and expose Ceph cluster
  information, including a web-based [Ceph Dashboard](../mgr/dashboard/index.md#mgr-dashboard) and
  [REST API](https://docs.ceph.com/en/mgr/restful). At least two managers are normally required for high
  availability.
- **Ceph OSDs**: An Object Storage Daemon ([Ceph OSD](../glossary/index.md#term-Ceph-OSD),
  `ceph-osd`) stores data, handles data replication, recovery,
  rebalancing, and provides some monitoring information to Ceph
  Monitors and Managers by checking other Ceph OSD Daemons for a
  heartbeat. At least three Ceph OSDs are normally required for
  redundancy and high availability.
- **MDSes**: A [Ceph Metadata Server](../glossary/index.md#term-Ceph-Metadata-Server) (MDS, `ceph-mds`) stores metadata
  for the [Ceph File System](../glossary/index.md#term-Ceph-File-System). Ceph Metadata Servers allow CephFS users to
  run basic commands (like `ls`, `find`, etc.) without placing a burden on
  the Ceph Storage Cluster.
- **RGWs**: A [Ceph Object Gateway](../glossary/index.md#term-Ceph-Object-Gateway) (RGW, `ceph-radosgw`) daemon provides
  a RESTful gateway between applications and Ceph storage clusters. The
  S3-compatible API is most commonly used, though Swift is also available.

Ceph stores data as objects within logical storage pools. Using the
[CRUSH](../glossary/index.md#term-CRUSH) algorithm, Ceph calculates which placement group (PG) should
contain the object, and which OSD should store the placement group. The
CRUSH algorithm enables the Ceph Storage Cluster to scale, rebalance, and
recover dynamically.

### Recommendations

To begin using Ceph in production, you should review our hardware
recommendations and operating system recommendations.

- [Beginner's Guide](beginners-guide/index.md)
  - [Components of Ceph](beginners-guide/index.md#components-of-ceph)
  - [Vstart Cluster Installation and Configuration Procedure](beginners-guide/index.md#vstart-cluster-installation-and-configuration-procedure)
- [Hardware Recommendations](hardware-recommendations/index.md)
  - [CPU](hardware-recommendations/index.md#cpu)
  - [RAM](hardware-recommendations/index.md#ram)
  - [Memory](hardware-recommendations/index.md#memory)
  - [Data Storage](hardware-recommendations/index.md#data-storage)
  - [Networks](hardware-recommendations/index.md#networks)
  - [Failure Domains](hardware-recommendations/index.md#failure-domains)
  - [Minimum Hardware Recommendations](hardware-recommendations/index.md#minimum-hardware-recommendations)
- [OS Recommendations](os-recommendations/index.md)
  - [Ceph Dependencies](os-recommendations/index.md#ceph-dependencies)
  - [Platforms](os-recommendations/index.md#platforms)

### Get Involved

You can avail yourself of help or contribute documentation, source
code or bugs by getting involved in the Ceph community.

- [Get Involved in the Ceph Community!](get-involved/index.md)
- [Documenting Ceph](documenting-ceph/index.md)
  - [Location of the Documentation in the Repository](documenting-ceph/index.md#location-of-the-documentation-in-the-repository)
  - [Viewing Old Ceph Documentation](documenting-ceph/index.md#viewing-old-ceph-documentation)
  - [Making Contributions](documenting-ceph/index.md#making-contributions)
  - [Documentation Style Guide](documenting-ceph/index.md#documentation-style-guide)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
