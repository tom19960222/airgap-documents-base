---
collection: ceph
version: "20.2.4"
title: "`create`"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/ceph-volume/lvm/create.rst
fetched_at: 2026-08-18T01:32:45Z
---
<a id="ceph-volume-lvm-create"></a>

# ``create``
This subcommand wraps the two-step process to provision a new osd (calling
``prepare`` first and then ``activate``) into a single
one. The reason to prefer ``prepare`` and then ``activate`` is to gradually
introduce new OSDs into a cluster, and avoiding large amounts of data being
rebalanced.

The single-call process unifies exactly what [ceph-volume-lvm-prepare](prepare.md#ceph-volume-lvm-prepare) and
[ceph-volume-lvm-activate](activate.md#ceph-volume-lvm-activate) do, with the convenience of doing it all at
once.

There is nothing different to the process except the OSD will become up and in
immediately after completion.

The backing objectstore can be specified with:

* [--bluestore](prepare.md#ceph-volume-lvm-prepare-bluestore)

All command line flags and options are the same as ``ceph-volume lvm prepare``.
Please refer to [ceph-volume-lvm-prepare](prepare.md#ceph-volume-lvm-prepare) for details.
