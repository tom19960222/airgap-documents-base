---
collection: ceph
version: "20.2.4"
title: "ceph-volume"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/ceph-volume/index.rst
fetched_at: 2026-08-18T01:32:45Z
---
<a id="ceph-volume"></a>

# ceph-volume
Deploy OSDs with different device technologies like lvm or physical disks using
pluggable tools ([lvm/index](lvm/index.md) itself is treated like a plugin) and trying to
follow a predictable, and robust way of preparing, activating, and starting OSDs.

[Overview](intro.md#ceph-volume-overview) |
[Plugin Guide](../dev/ceph-volume/plugins.md#ceph-volume-plugins) |

**Command Line Subcommands**

There is currently support for ``lvm``, and plain disks (with GPT partitions)
that may have been deployed with ``ceph-disk``.

``zfs`` support is available for running a FreeBSD cluster.

* [ceph-volume-lvm](lvm/index.md#ceph-volume-lvm)
* [ceph-volume-simple](simple/index.md#ceph-volume-simple)
* [ceph-volume-zfs](zfs/index.md#ceph-volume-zfs)

**Node inventory**

The [ceph-volume-inventory](inventory.md#ceph-volume-inventory) subcommand provides information and metadata
about a nodes physical disk inventory.

## Migrating
Starting on Ceph version 13.0.0, ``ceph-disk`` is deprecated. Deprecation
warnings will show up that will link to this page. It is strongly suggested
that users start consuming ``ceph-volume``. There are two paths for migrating:

1. Keep OSDs deployed with ``ceph-disk``: The [ceph-volume-simple](simple/index.md#ceph-volume-simple) command
   provides a way to take over the management while disabling ``ceph-disk``
   triggers.
1. Redeploy existing OSDs with ``ceph-volume``: This is covered in depth on
   [rados-replacing-an-osd](../rados/operations/add-or-rm-osds.md#rados-replacing-an-osd)

For details on why ``ceph-disk`` was removed please see the [Why was ceph-disk replaced?](intro.md#ceph-disk-replaced) section.

### New deployments
For new deployments, [ceph-volume-lvm](lvm/index.md#ceph-volume-lvm) is recommended, it can use any
logical volume as input for data OSDs, or it can setup a minimal/naive logical
volume from a device.

### Existing OSDs
If the cluster has OSDs that were provisioned with ``ceph-disk``, then
``ceph-volume`` can take over the management of these with
[ceph-volume-simple](simple/index.md#ceph-volume-simple). A scan is done on the data device or OSD directory,
and ``ceph-disk`` is fully disabled. Encryption is fully supported.

.. toctree::
   :hidden:
   :maxdepth: 3
   :caption: Contents:

   intro
   systemd
   inventory
   drive-group
   lvm/index
   lvm/activate
   lvm/batch
   lvm/encryption
   lvm/prepare
   lvm/create
   lvm/scan
   lvm/systemd
   lvm/list
   lvm/zap
   lvm/migrate
   lvm/newdb
   lvm/newwal
   simple/index
   simple/activate
   simple/scan
   simple/systemd
   zfs/index
   zfs/inventory
