---
collection: ceph
version: "19.2.2"
title: "Ceph iSCSI Gateway"
source_url: https://docs.ceph.com/en/squid/rbd/iscsi-overview/
fetched_at: 2026-07-27T16:40:24+00:00
---
# Ceph iSCSI Gateway

The iSCSI Gateway presents a Highly Available (HA) iSCSI target that exports
RADOS Block Device (RBD) images as SCSI disks. The iSCSI protocol allows
clients (initiators) to send SCSI commands to storage devices (targets) over a
TCP/IP network, enabling clients without native Ceph client support to access
Ceph block storage.

Each iSCSI gateway exploits the Linux IO target kernel subsystem (LIO) to
provide iSCSI protocol support. LIO utilizes userspace passthrough (TCMU) to
interact with Ceph’s librbd library and expose RBD images to iSCSI clients.
With Ceph’s iSCSI gateway you can provision a fully integrated block-storage
infrastructure with all the features and benefits of a conventional Storage
Area Network (SAN).

![](../../_images/ditaa-564a237d5600d8518d6def6745857796a057ca08.png)

> **Warning:**
>
> The iSCSI gateway is in maintenance as of November 2022. This means that
> it is no longer in active development and will not be updated to add
> new features.

- [Requirements](../iscsi-requirements/index.md)
- [Configuring the iSCSI Target](../iscsi-targets/index.md)
- [Configuring the iSCSI Initiators](../iscsi-initiators/index.md)
- [Monitoring the iSCSI Gateways](../iscsi-monitoring/index.md)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
