---
collection: ceph
version: "19.2.2"
title: "zfs"
source_url: https://docs.ceph.com/en/squid/ceph-volume/zfs/
fetched_at: 2026-07-27T16:41:45+00:00
---
# `zfs`

Implements the functionality needed to deploy OSDs from the `zfs` subcommand:
`ceph-volume zfs`

The current implementation only works for ZFS on FreeBSD

**Command Line Subcommands**

- [inventory](inventory/index.md#ceph-volume-zfs-inventory)

**Internal functionality**

There are other aspects of the `zfs` subcommand that are internal and not
exposed to the user, these sections explain how these pieces work together,
clarifying the workflows of the tool.

[zfs](../../dev/ceph-volume/zfs/index.md#ceph-volume-zfs-api)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
