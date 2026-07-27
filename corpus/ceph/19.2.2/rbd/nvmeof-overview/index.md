---
collection: ceph
version: "19.2.2"
title: "Ceph NVMe-oF Gateway"
source_url: https://docs.ceph.com/en/squid/rbd/nvmeof-overview/
fetched_at: 2026-07-27T16:40:25+00:00
---
# Ceph NVMe-oF Gateway

The NVMe-oF Gateway presents an NVMe-oF target that exports
RADOS Block Device (RBD) images as NVMe namespaces. The NVMe-oF protocol allows
clients (initiators) to send NVMe commands to storage devices (targets) over a
TCP/IP network, enabling clients without native Ceph client support to access
Ceph block storage.

Each NVMe-oF gateway consists of an [SPDK](https://spdk.io/) NVMe-oF target
with `bdev_rbd` and a control daemon. Ceph’s NVMe-oF gateway can be used to
provision a fully integrated block-storage infrastructure with all the features
and benefits of a conventional Storage Area Network (SAN).

![](../../_images/ditaa-9e5887433bb6b7bce4395e60112d743e3f38aafa.png)

- [Requirements](../nvmeof-requirements/index.md)
- [Configuring the NVME-oF Target](../nvmeof-target-configure/index.md)
- [Configuring the NVMe-oF Initiators](../nvmeof-initiators/index.md)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
