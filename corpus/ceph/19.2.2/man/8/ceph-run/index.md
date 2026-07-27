---
collection: ceph
version: "19.2.2"
title: "ceph-run -- restart daemon on core dump"
source_url: https://docs.ceph.com/en/squid/man/8/ceph-run/
fetched_at: 2026-07-27T16:42:01+00:00
---
# ceph-run -- restart daemon on core dump

## Synopsis

**ceph-run** *command* …

## Description

**ceph-run** is a simple wrapper that will restart a daemon if it exits
with a signal indicating it crashed and possibly core dumped (that is,
signals 3, 4, 5, 6, 8, or 11).

The command should run the daemon in the foreground. For Ceph daemons,
that means the `-f` option.

## Options

None

## Availability

**ceph-run** is part of Ceph, a massively scalable, open-source, distributed storage system. Please refer to
the Ceph documentation at <https://docs.ceph.com> for more information.

## See also

[ceph](../ceph/index.md)(8),
[ceph-mon](../ceph-mon/index.md)(8),
[ceph-mds](../ceph-mds/index.md)(8),
[ceph-osd](../ceph-osd/index.md)(8)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
