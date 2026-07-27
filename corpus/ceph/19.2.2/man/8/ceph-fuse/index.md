---
collection: ceph
version: "19.2.2"
title: "ceph-fuse -- FUSE-based client for ceph"
source_url: https://docs.ceph.com/en/squid/man/8/ceph-fuse/
fetched_at: 2026-07-27T16:40:01+00:00
---
# ceph-fuse -- FUSE-based client for ceph

## Synopsis

**ceph-fuse** [-n *client.username*] [ -m *monaddr*:*port* ] *mountpoint* [ *fuse options* ]

## Description

**ceph-fuse** is a FUSE (“Filesystem in USErspace”) client for Ceph
distributed file system. It will mount a ceph file system specified via the -m
option or described by ceph.conf (see below) at the specific mount point. See
[Mount CephFS using FUSE](../../../cephfs/mount-using-fuse/index.md) for detailed information.

The file system can be unmounted with:

```
fusermount -u mountpoint
```

or by sending `SIGINT` to the `ceph-fuse` process.

## Options

Any options not recognized by ceph-fuse will be passed on to libfuse.

-o opt,[opt...]
:   Mount options.

-c ceph.conf, --conf=ceph.conf
:   Use *ceph.conf* configuration file instead of the default
    `/etc/ceph/ceph.conf` to determine monitor addresses during startup.

-m monaddress[:port]
:   Connect to specified monitor (instead of looking through ceph.conf).

-n client.{cephx-username}
:   Pass the name of CephX user whose secret key is be to used for mounting.

--id <client-id>
:   Pass the name of CephX user whose secret key is be to used for mounting.
    `--id` takes just the ID of the client in contrast to `-n`. For
    example, `--id 0` for using `client.0`.

-k <path-to-keyring>
:   Provide path to keyring; useful when it’s absent in standard locations.

--client_mountpoint/-r root_directory
:   Use root_directory as the mounted root, rather than the full Ceph tree.

-f
:   Foreground: do not daemonize after startup (run in foreground). Do not generate a pid file.

-d
:   Run in foreground, send all log output to stderr and enable FUSE debugging
    (-o debug).

-s
:   Disable multi-threaded operation.

--client_fs
:   Pass the name of Ceph FS to be mounted. Not passing this option mounts the
    default Ceph FS on the Ceph cluster.

## Availability

**ceph-fuse** is part of Ceph, a massively scalable, open-source, distributed storage system. Please refer to
the Ceph documentation at <https://docs.ceph.com> for more information.

## See also

fusermount(8),
[ceph](../ceph/index.md)(8)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
