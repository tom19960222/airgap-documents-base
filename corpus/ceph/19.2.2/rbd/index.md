---
collection: ceph
version: "19.2.2"
title: "Ceph Block Device"
source_url: https://docs.ceph.com/en/squid/rbd/
fetched_at: 2026-07-27T16:38:46+00:00
---
# Ceph Block Device

A block is a sequence of bytes (often 512).
Block-based storage interfaces are a mature and common way to store data on
media including HDDs, SSDs, CDs, floppy disks, and even tape.
The ubiquity of block device interfaces is a perfect fit for interacting
with mass data storage including Ceph.

Ceph block devices are thin-provisioned, resizable, and store data striped over
multiple OSDs. Ceph block devices leverage
RADOS capabilities
including snapshotting, replication and strong consistency. Ceph block
storage clients communicate with Ceph clusters through kernel modules or
the `librbd` library.

![](../_images/ditaa-9c4dce3fc347721433a81021ea03daac92997c1a.png)

> **Note:**
>
> Kernel modules can use Linux page caching. For `librbd`-based
> applications, Ceph supports [RBD Caching](rbd-config-ref/index.md).

Ceph’s block devices deliver high performance with vast scalability to
[kernel modules](rbd-ko/index.md), or to KVMs such as [QEMU](qemu-rbd/index.md), and
cloud-based computing systems like [OpenStack](rbd-openstack.md), [OpenNebula](https://docs.opennebula.io/stable/open_cluster_deployment/storage_setup/ceph_ds.html) and [CloudStack](rbd-cloudstack.md)
that rely on libvirt and QEMU to integrate with Ceph block devices. You can use
the same cluster to operate the [Ceph RADOS Gateway](../radosgw/index.md#object-gateway), the
[Ceph File System](../cephfs/index.md#ceph-file-system), and Ceph block devices simultaneously.

> **Important:**
>
> To use Ceph Block Devices, you must have access to a running
> Ceph cluster.

- [Basic Commands](rados-rbd-cmds/index.md)

- [Operations](rbd-operations/index.md)
  - [Snapshots](rbd-snapshot/index.md)
  - [Exclusive Locking](rbd-exclusive-locks/index.md)
  - [Mirroring](rbd-mirroring/index.md)
  - [Live-Migration](rbd-live-migration/index.md)
  - [Persistent Read-only Cache](rbd-persistent-read-only-cache/index.md)
  - [Persistent Write Log Cache](rbd-persistent-write-log-cache/index.md)
  - [Encryption](rbd-encryption/index.md)
  - [Config Settings (librbd)](rbd-config-ref/index.md)
  - [RBD Replay](rbd-replay/index.md)

- [Integrations](rbd-integrations/index.md)
  - [Kernel Modules](rbd-ko/index.md)
  - [QEMU](qemu-rbd/index.md)
  - [libvirt](libvirt/index.md)
  - [Kubernetes](rbd-kubernetes/index.md)
  - [Nomad](rbd-nomad/index.md)
  - [OpenStack](rbd-openstack/index.md)
  - [CloudStack](rbd-cloudstack/index.md)
  - [LIO iSCSI Gateway](iscsi-overview/index.md)
  - [Windows](rbd-windows/index.md)
  - [NVMe-oF Gateway](nvmeof-overview/index.md)

- [Manpages](man/index.md)
  - [rbd](../man/8/rbd/index.md)
  - [rbd-fuse](../man/8/rbd-fuse/index.md)
  - [rbd-nbd](../man/8/rbd-nbd/index.md)
  - [rbd-ggate](../man/8/rbd-ggate/index.md)
  - [rbd-map](../man/8/rbdmap/index.md)
  - [ceph-rbdnamer](../man/8/ceph-rbdnamer/index.md)
  - [rbd-replay-prep](../man/8/rbd-replay-prep/index.md)
  - [rbd-replay](../man/8/rbd-replay/index.md)
  - [rbd-replay-many](../man/8/rbd-replay-many/index.md)

- [APIs](api/index.md)
  - [librbd (Python)](api/librbdpy/index.md)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
