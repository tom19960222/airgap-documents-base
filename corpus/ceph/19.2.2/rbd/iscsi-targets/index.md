---
collection: ceph
version: "19.2.2"
title: "iSCSI Targets"
source_url: https://docs.ceph.com/en/squid/rbd/iscsi-targets/
fetched_at: 2026-07-27T16:42:36+00:00
---
# iSCSI Targets

Traditionally, block-level access to a Ceph storage cluster has been
limited to QEMU and `librbd`, which is a key enabler for adoption
within OpenStack environments. Starting with the Ceph Luminous release,
block-level access is expanding to offer standard iSCSI support allowing
wider platform usage, and potentially opening new use cases.

- Red Hat Enterprise Linux/CentOS 7.5 (or newer); Linux kernel v4.16 (or newer)
- A working Ceph Storage cluster, deployed with `ceph-ansible` or using the command-line interface
- iSCSI gateways nodes, which can either be colocated with OSD nodes or on dedicated nodes
- Separate network subnets for iSCSI front-end traffic and Ceph back-end traffic

A choice of using Ansible or the command-line interface are the
available deployment methods for installing and configuring the Ceph
iSCSI gateway:

- [Using Ansible](../iscsi-target-ansible/index.md)
- [Using the Command Line Interface](../iscsi-target-cli/index.md)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
