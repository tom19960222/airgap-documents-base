---
collection: ceph
version: "19.2.2"
title: "MDS Autoscaler Module"
source_url: https://docs.ceph.com/en/squid/mgr/mds_autoscaler/
fetched_at: 2026-07-27T16:40:55+00:00
---
# MDS Autoscaler Module

The MDS Autoscaler Module monitors file systems to ensure that sufficient MDS
daemons are available. It works by adjusting the placement specification for
the orchestrator backend of the MDS service. To enable, use:

```
ceph mgr module enable mds_autoscaler
```

The module monitors the following file-system settings to inform placement-
count adjustments:

- `max_mds` file system setting
- `standby_count_wanted` file system setting

The Ceph monitor daemons remain responsible for promoting or stopping MDS
according to these settings. The `mds_autoscaler` simply adjusts the
number of MDS daemons spawned by the orchestrator.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
