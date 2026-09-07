---
collection: ceph
version: "20.2.4"
title: "rbd-replay-prep -- prepare captured rados block device (RBD) workloads for replay"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/man/8/rbd-replay-prep.rst
fetched_at: 2026-08-18T01:32:45Z
---
:orphan:

# rbd-replay-prep -- prepare captured rados block device (RBD) workloads for replay

.. program:: rbd-replay-prep

## Synopsis

| **rbd-replay-prep** [ --window *seconds* ] [ --anonymize ] *trace_dir* *replay_file*

## Description

**rbd-replay-prep** processes raw rados block device (RBD) traces to prepare them for **rbd-replay**.

## Options

.. option:: --window seconds

   Requests further apart than 'seconds' seconds are assumed to be independent.

.. option:: --anonymize

   Anonymizes image and snap names.

.. option:: --verbose

   Print all processed events to console

## Examples

To prepare workload1-trace for replay:

```
rbd-replay-prep workload1-trace/ust/uid/1000/64-bit workload1
```

## Availability

**rbd-replay-prep** is part of Ceph, a massively scalable, open-source, distributed storage system. Please refer to
the Ceph documentation at https://docs.ceph.com for more information.

## See also

[rbd-replay](rbd-replay.md)\(8),
[rbd](../../dev/osd_internals/manifest.md#rbd)\(8)
