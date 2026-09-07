---
collection: ceph
version: "20.2.4"
title: "scan"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/ceph-volume/lvm/scan.rst
fetched_at: 2026-08-18T01:32:45Z
---
# scan
This sub-command will allow to discover Ceph volumes previously setup by the
tool by looking into the system's logical volumes and their tags.

As part of the [ceph-volume-lvm-prepare](prepare.md#ceph-volume-lvm-prepare) process, the logical volumes are assigned
a few tags with important pieces of information.

> **Note:** This sub-command is not yet implemented
