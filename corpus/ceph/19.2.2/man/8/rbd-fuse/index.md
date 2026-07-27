---
collection: ceph
version: "19.2.2"
title: "rbd-fuse -- expose rbd images as files"
source_url: https://docs.ceph.com/en/squid/man/8/rbd-fuse/
fetched_at: 2026-07-27T16:40:26+00:00
---
# rbd-fuse -- expose rbd images as files

## Synopsis

**rbd-fuse** [ -p pool ] [-c conffile] *mountpoint* [ *fuse options* ]

## Note

**rbd-fuse** is not recommended for any production or high performance workloads.

## Description

**rbd-fuse** is a FUSE (“Filesystem in USErspace”) client for RADOS
block device (rbd) images. Given a pool containing rbd images,
it will mount a userspace file system allowing access to those images
as regular files at **mountpoint**.

The file system can be unmounted with:

```
fusermount -u mountpoint
```

or by sending `SIGINT` to the `rbd-fuse` process.

## Options

Any options not recognized by rbd-fuse will be passed on to libfuse.

-c ceph.conf
:   Use *ceph.conf* configuration file instead of the default
    `/etc/ceph/ceph.conf` to determine monitor addresses during startup.

-p pool
:   Use *pool* as the pool to search for rbd images. Default is `rbd`.

## Availability

**rbd-fuse** is part of Ceph, a massively scalable, open-source, distributed storage system. Please refer to
the Ceph documentation at <https://docs.ceph.com> for more information.

## See also

fusermount(8),
[rbd](../rbd/index.md)(8)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
