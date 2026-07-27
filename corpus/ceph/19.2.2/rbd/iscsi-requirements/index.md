---
collection: ceph
version: "19.2.2"
title: "iSCSI Gateway Requirements"
source_url: https://docs.ceph.com/en/squid/rbd/iscsi-requirements/
fetched_at: 2026-07-27T16:42:35+00:00
---
# iSCSI Gateway Requirements

It is recommended to provision two to four iSCSI gateway nodes to
realize a highly available Ceph iSCSI gateway solution.

For hardware recommendations, see [hardware recommendations](../../start/hardware-recommendations/index.md#hardware-recommendations) .

> **Note:**
>
> On iSCSI gateway nodes the memory footprint is a function of
> of the RBD images mapped and can grow to be large. Plan memory
> requirements accordingly based on the number RBD images to be mapped.

There are no specific iSCSI gateway options for the Ceph Monitors or
OSDs, but it is important to lower the default heartbeat interval for
detecting down OSDs to reduce the possibility of initiator timeouts.
The following configuration options are suggested:

```
[osd]
osd heartbeat grace = 20
osd heartbeat interval = 5
```

- Updating Running State From a Ceph Monitor Node

> ```
> ceph tell <daemon_type>.<id> config set <parameter_name> <new_value>
> ```
>
> ```
> ceph tell osd.* config set osd_heartbeat_grace 20
> ceph tell osd.* config set osd_heartbeat_interval 5
> ```

- Updating Running State On Each OSD Node

  ```
  ceph daemon <daemon_type>.<id> config set osd_client_watch_timeout 15
  ```

  ```
  ceph daemon osd.0 config set osd_heartbeat_grace 20
  ceph daemon osd.0 config set osd_heartbeat_interval 5
  ```

For more details on setting Ceph’s configuration options, see
[Configuring Ceph](../../rados/configuration/ceph-conf/index.md#configuring-ceph). Be sure to persist these settings in
`/etc/ceph.conf` or, on Mimic and later releases, in the
centralized config store.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
