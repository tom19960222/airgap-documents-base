---
collection: ceph
version: "19.2.2"
title: "mount.fuse.ceph -- mount ceph-fuse from /etc/fstab."
source_url: https://docs.ceph.com/en/squid/man/8/mount.fuse.ceph/
fetched_at: 2026-07-27T16:40:02+00:00
---
# mount.fuse.ceph -- mount ceph-fuse from /etc/fstab.

## Synopsis

**mount.fuse.ceph** [-h] [-o OPTIONS [*OPTIONS* …]]
device [*device* …]
mountpoint [*mount point* …]

## Description

**mount.fuse.ceph** is a helper for mounting ceph-fuse from
`/etc/fstab`.

To use mount.fuse.ceph, add an entry in `/etc/fstab` like:

```
DEVICE    PATH        TYPE        OPTIONS
none      /mnt/ceph   fuse.ceph   ceph.id=admin,_netdev,defaults  0 0
none      /mnt/ceph   fuse.ceph   ceph.name=client.admin,_netdev,defaults  0 0
none      /mnt/ceph   fuse.ceph   ceph.id=myuser,ceph.conf=/etc/ceph/foo.conf,_netdev,defaults  0 0
```

ceph-fuse options are specified in the `OPTIONS` column and must begin
with ‘`ceph.`’ prefix. This way ceph related fs options will be passed to
ceph-fuse and others will be ignored by ceph-fuse.

## Options

ceph.id=<username>
:   Specify that the ceph-fuse will authenticate as the given user.

ceph.name=client.admin
:   Specify that the ceph-fuse will authenticate as client.admin

ceph.conf=/etc/ceph/foo.conf
:   Sets ‘conf’ option to /etc/ceph/foo.conf via ceph-fuse command line.

Any valid ceph-fuse options can be passed this way.

## Additional Info

The old format /etc/fstab entries are also supported:

```
DEVICE                              PATH        TYPE        OPTIONS
id=admin                            /mnt/ceph   fuse.ceph   defaults   0 0
id=myuser,conf=/etc/ceph/foo.conf   /mnt/ceph   fuse.ceph   defaults   0 0
```

## Availability

**mount.fuse.ceph** is part of Ceph, a massively scalable, open-source, distributed storage system. Please
refer to the Ceph documentation at <https://docs.ceph.com> for more
information.

## See also

[ceph-fuse](../ceph-fuse/index.md)(8),
[ceph](../ceph/index.md)(8)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
