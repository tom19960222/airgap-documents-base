---
collection: ceph
version: "19.2.2"
title: "ceph-volume"
source_url: https://docs.ceph.com/en/squid/ceph-volume/
fetched_at: 2026-07-27T16:38:51+00:00
---
# ceph-volume

Deploy OSDs with different device technologies like lvm or physical disks using
pluggable tools ([lvm](lvm/index.md) itself is treated like a plugin) and trying to
follow a predictable, and robust way of preparing, activating, and starting OSDs.

[Overview](intro/index.md#ceph-volume-overview) |
[Plugin Guide](../dev/ceph-volume/plugins/index.md#ceph-volume-plugins) |

**Command Line Subcommands**

There is currently support for `lvm`, and plain disks (with GPT partitions)
that may have been deployed with `ceph-disk`.

`zfs` support is available for running a FreeBSD cluster.

- [lvm](lvm/index.md#ceph-volume-lvm)
- [simple](simple/index.md#ceph-volume-simple)
- [zfs](zfs/index.md#ceph-volume-zfs)

**Node inventory**

The [inventory](inventory/index.md#ceph-volume-inventory) subcommand provides information and metadata
about a nodes physical disk inventory.

## Migrating

Starting on Ceph version 13.0.0, `ceph-disk` is deprecated. Deprecation
warnings will show up that will link to this page. It is strongly suggested
that users start consuming `ceph-volume`. There are two paths for migrating:

1. Keep OSDs deployed with `ceph-disk`: The [simple](simple/index.md#ceph-volume-simple) command
   provides a way to take over the management while disabling `ceph-disk`
   triggers.
2. Redeploy existing OSDs with `ceph-volume`: This is covered in depth on
   [Replacing an OSD](../rados/operations/add-or-rm-osds/index.md#rados-replacing-an-osd)

For details on why `ceph-disk` was removed please see the [Why was
ceph-disk replaced?](intro/index.md#ceph-disk-replaced) section.

### New deployments

For new deployments, [lvm](lvm/index.md#ceph-volume-lvm) is recommended, it can use any
logical volume as input for data OSDs, or it can setup a minimal/naive logical
volume from a device.

### Existing OSDs

If the cluster has OSDs that were provisioned with `ceph-disk`, then
`ceph-volume` can take over the management of these with
[simple](simple/index.md#ceph-volume-simple). A scan is done on the data device or OSD directory,
and `ceph-disk` is fully disabled. Encryption is fully supported.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
