---
collection: ceph
version: "19.2.2"
title: "rbd-replay-prep -- prepare captured rados block device (RBD) workloads for replay"
source_url: https://docs.ceph.com/en/squid/man/8/rbd-replay-prep/
fetched_at: 2026-07-27T16:40:28+00:00
---
# rbd-replay-prep -- prepare captured rados block device (RBD) workloads for replay

## Synopsis

**rbd-replay-prep** [ --window *seconds* ] [ --anonymize ] *trace_dir* *replay_file*

## Description

**rbd-replay-prep** processes raw rados block device (RBD) traces to prepare them for **rbd-replay**.

## Options

--window seconds
:   Requests further apart than ‘seconds’ seconds are assumed to be independent.

--anonymize
:   Anonymizes image and snap names.

--verbose
:   Print all processed events to console

## Examples

To prepare workload1-trace for replay:

```
rbd-replay-prep workload1-trace/ust/uid/1000/64-bit workload1
```

## Availability

**rbd-replay-prep** is part of Ceph, a massively scalable, open-source, distributed storage system. Please refer to
the Ceph documentation at <https://docs.ceph.com> for more information.

## See also

[rbd-replay](../rbd-replay/index.md)(8),
[rbd](../rbd/index.md)(8)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
