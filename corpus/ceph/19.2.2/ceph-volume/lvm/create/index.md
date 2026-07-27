---
collection: ceph
version: "19.2.2"
title: "create"
source_url: https://docs.ceph.com/en/squid/ceph-volume/lvm/create/
fetched_at: 2026-07-27T16:41:40+00:00
---
# `create`

This subcommand wraps the two-step process to provision a new osd (calling
`prepare` first and then `activate`) into a single
one. The reason to prefer `prepare` and then `activate` is to gradually
introduce new OSDs into a cluster, and avoiding large amounts of data being
rebalanced.

The single-call process unifies exactly what [prepare](../prepare/index.md#ceph-volume-lvm-prepare) and
[activate](../activate/index.md#ceph-volume-lvm-activate) do, with the convenience of doing it all at
once.

There is nothing different to the process except the OSD will become up and in
immediately after completion.

The backing objectstore can be specified with:

- [--bluestore](../prepare/index.md#ceph-volume-lvm-prepare-bluestore)

All command line flags and options are the same as `ceph-volume lvm prepare`.
Please refer to [prepare](../prepare/index.md#ceph-volume-lvm-prepare) for details.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
