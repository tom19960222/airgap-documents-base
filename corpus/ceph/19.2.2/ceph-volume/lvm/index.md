---
collection: ceph
version: "19.2.2"
title: "lvm"
source_url: https://docs.ceph.com/en/squid/ceph-volume/lvm/
fetched_at: 2026-07-27T16:41:39+00:00
---
# `lvm`

Implements the functionality needed to deploy OSDs from the `lvm` subcommand:
`ceph-volume lvm`

**Command Line Subcommands**

- [prepare](prepare/index.md#ceph-volume-lvm-prepare)
- [activate](activate/index.md#ceph-volume-lvm-activate)
- [create](create/index.md#ceph-volume-lvm-create)
- [list](list/index.md#ceph-volume-lvm-list)
- [migrate](migrate/index.md#ceph-volume-lvm-migrate)
- [new-db](newdb/index.md#ceph-volume-lvm-newdb)
- [new-wal](newwal/index.md#ceph-volume-lvm-newwal)

**Internal functionality**

There are other aspects of the `lvm` subcommand that are internal and not
exposed to the user, these sections explain how these pieces work together,
clarifying the workflows of the tool.

[Systemd Units](systemd/index.md#ceph-volume-lvm-systemd) |
[lvm](../../dev/ceph-volume/lvm/index.md#ceph-volume-lvm-api)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
