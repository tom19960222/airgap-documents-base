---
collection: ceph
version: "19.2.2"
title: "systemd"
source_url: https://docs.ceph.com/en/squid/ceph-volume/lvm/systemd/
fetched_at: 2026-07-27T16:41:41+00:00
---
# systemd

Upon startup, it will identify the logical volume using [LVM tags](../../../glossary/index.md#term-LVM-tags),
finding a matching ID and later ensuring it is the right one with
the [OSD uuid](../../../glossary/index.md#term-OSD-UUID).

After identifying the correct volume it will then proceed to mount it by using
the OSD destination conventions, that is:

```
/var/lib/ceph/osd/<cluster name>-<osd id>
```

For our example OSD with an id of `0`, that means the identified device will
be mounted at:

```
/var/lib/ceph/osd/ceph-0
```

Once that process is complete, a call will be made to start the OSD:

```
systemctl start ceph-osd@0
```

The systemd portion of this process is handled by the `ceph-volume lvm
trigger` sub-command, which is only in charge of parsing metadata coming from
systemd and startup, and then dispatching to `ceph-volume lvm activate` which
would proceed with activation.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
