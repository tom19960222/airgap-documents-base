---
collection: ceph
version: "19.2.2"
title: "drive-group"
source_url: https://docs.ceph.com/en/squid/ceph-volume/drive-group/
fetched_at: 2026-07-27T16:41:38+00:00
---
# `drive-group`

The drive-group subcommand allows for passing [Advanced OSD Service Specifications](../../cephadm/services/osd/index.md#drivegroups) specifications
straight to ceph-volume as json. ceph-volume will then attempt to deploy this
drive groups via the batch subcommand.

The specification can be passed via a file, string argument or on stdin.
See the subcommand help for further details:

```
# ceph-volume drive-group --help
```

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
