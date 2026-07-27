---
collection: ceph
version: "19.2.2"
title: "iostat"
source_url: https://docs.ceph.com/en/squid/mgr/iostat/
fetched_at: 2026-07-27T16:40:54+00:00
---
# iostat

The `iostat` module reports metrics for cluster throughpout and IOPS.

## Enabling

To determine whether the `iostat` module is enabled, run the following
command:

```
ceph mgr module ls
```

To enable the `iostat` module, run the following command:

```
ceph mgr module enable iostat
```

To execute the module, run the following command:

```
ceph iostat
```

To change the frequency at which the statistics are printed, use the `-p`
option:

```
ceph iostat -p <period in seconds>
```

For example, use the following command to print the statistics every 5
seconds:

```
ceph iostat -p 5
```

To stop the module, press `Ctrl-C`.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
