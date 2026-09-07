---
collection: ceph
version: "20.2.4"
title: "`zfs`"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/ceph-volume/zfs/index.rst
fetched_at: 2026-08-18T01:32:45Z
---
<a id="ceph-volume-zfs"></a>

# ``zfs``
Implements the functionality needed to deploy OSDs from the ``zfs`` subcommand:
``ceph-volume zfs``

The current implementation only works for ZFS on FreeBSD

**Command Line Subcommands**

* [ceph-volume-zfs-inventory](inventory.md#ceph-volume-zfs-inventory)

.. not yet implemented
.. * ceph-volume-zfs-prepare <!-- unresolved-rst-link: kind=ref target=ceph-volume-zfs-prepare -->

.. * ceph-volume-zfs-activate <!-- unresolved-rst-link: kind=ref target=ceph-volume-zfs-activate -->

.. * ceph-volume-zfs-create <!-- unresolved-rst-link: kind=ref target=ceph-volume-zfs-create -->

.. * ceph-volume-zfs-list <!-- unresolved-rst-link: kind=ref target=ceph-volume-zfs-list -->

.. * ceph-volume-zfs-scan <!-- unresolved-rst-link: kind=ref target=ceph-volume-zfs-scan -->

**Internal functionality**

There are other aspects of the ``zfs`` subcommand that are internal and not
exposed to the user, these sections explain how these pieces work together,
clarifying the workflows of the tool.

[zfs](../../dev/ceph-volume/zfs.md#ceph-volume-zfs-api)
