---
collection: ceph
version: "20.2.4"
title: "`lvm`"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/ceph-volume/lvm/index.rst
fetched_at: 2026-08-18T01:32:45Z
---
<a id="ceph-volume-lvm"></a>

# ``lvm``
Implements the functionality needed to deploy OSDs from the ``lvm`` subcommand:
``ceph-volume lvm``

**Command Line Subcommands**

* [ceph-volume-lvm-prepare](prepare.md#ceph-volume-lvm-prepare)

* [ceph-volume-lvm-activate](activate.md#ceph-volume-lvm-activate)

* [ceph-volume-lvm-create](create.md#ceph-volume-lvm-create)

* [ceph-volume-lvm-list](list.md#ceph-volume-lvm-list)

* [ceph-volume-lvm-migrate](migrate.md#ceph-volume-lvm-migrate)

* [ceph-volume-lvm-newdb](newdb.md#ceph-volume-lvm-newdb)

* [ceph-volume-lvm-newwal](newwal.md#ceph-volume-lvm-newwal)

.. not yet implemented
.. * ceph-volume-lvm-scan <!-- unresolved-rst-link: kind=ref target=ceph-volume-lvm-scan -->

**Internal functionality**

There are other aspects of the ``lvm`` subcommand that are internal and not
exposed to the user, these sections explain how these pieces work together,
clarifying the workflows of the tool.

[Systemd Units](systemd.md#ceph-volume-lvm-systemd) |
[lvm](../../dev/ceph-volume/lvm.md#ceph-volume-lvm-api)
