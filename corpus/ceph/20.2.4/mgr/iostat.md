---
collection: ceph
version: "20.2.4"
title: "iostat"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/mgr/iostat.rst
fetched_at: 2026-08-18T01:32:45Z
---
.. _mgr-iostat-overview:

# iostat

The `iostat` module reports metrics for cluster throughpout and IOPS.

## Enabling

To determine whether the `iostat` module is enabled, run the following
command:

```bash
ceph mgr module ls
```

To enable the `iostat` module, run the following command:

```bash
ceph mgr module enable iostat
```

To execute the module, run the following command:

```bash
ceph iostat
```

To change the frequency at which the statistics are printed, use the `-p`
option:

```bash
ceph iostat -p <period in seconds>
```

For example, use the following command to print the statistics every 5
seconds:

```bash
ceph iostat -p 5
```

To stop the module, press `Ctrl-C`.
