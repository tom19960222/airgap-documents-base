---
collection: ceph
version: "20.2.4"
title: "MDS Autoscaler Module"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/mgr/mds_autoscaler.rst
fetched_at: 2026-08-18T01:32:45Z
---
# MDS Autoscaler Module

The MDS Autoscaler Module monitors file systems to ensure that sufficient MDS
daemons are available. It works by adjusting the placement specification for
the orchestrator backend of the MDS service. To enable, use:

```bash
ceph mgr module enable mds_autoscaler
```

The module monitors the following file-system settings to inform placement-
count adjustments:

- `max_mds` file system setting
- `standby_count_wanted` file system setting

The Ceph monitor daemons remain responsible for promoting or stopping MDS
according to these settings. The `mds_autoscaler` simply adjusts the
number of MDS daemons spawned by the orchestrator.

.. note: There is no CLI as of the Tentacle release. There are no module
   configurations as of the Tentacle release. Enable or disable the module to
   turn the functionality on or off.
