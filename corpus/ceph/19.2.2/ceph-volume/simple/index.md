---
collection: ceph
version: "19.2.2"
title: "simple"
source_url: https://docs.ceph.com/en/squid/ceph-volume/simple/
fetched_at: 2026-07-27T16:41:43+00:00
---
# `simple`

Implements the functionality needed to manage OSDs from the `simple` subcommand:
`ceph-volume simple`

**Command Line Subcommands**

- [scan](scan/index.md#ceph-volume-simple-scan)
- [activate](activate/index.md#ceph-volume-simple-activate)
- [systemd](systemd/index.md#ceph-volume-simple-systemd)

By *taking over* management, it disables all `ceph-disk` systemd units used
to trigger devices at startup, relying on basic (customizable) JSON
configuration and systemd for starting up OSDs.

This process involves two steps:

1. [Scan](scan/index.md#ceph-volume-simple-scan) the running OSD or the data device
2. [Activate](activate/index.md#ceph-volume-simple-activate) the scanned OSD

The scanning will infer everything that `ceph-volume` needs to start the OSD,
so that when activation is needed, the OSD can start normally without getting
interference from `ceph-disk`.

As part of the activation process the systemd units for `ceph-disk` in charge
of reacting to `udev` events, are linked to `/dev/null` so that they are
fully inactive.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
