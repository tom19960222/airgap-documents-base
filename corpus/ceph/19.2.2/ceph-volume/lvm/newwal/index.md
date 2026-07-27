---
collection: ceph
version: "19.2.2"
title: "new-wal"
source_url: https://docs.ceph.com/en/squid/ceph-volume/lvm/newwal/
fetched_at: 2026-07-27T16:41:43+00:00
---
# `new-wal`

Attaches the given logical volume to the given OSD as a WAL volume.
Logical volume format is vg/lv. Fails if OSD has already got attached DB.

Attach vgname/lvname as a WAL volume to OSD 1:

```
ceph-volume lvm new-wal --osd-id 1 --osd-fsid 55BD4219-16A7-4037-BC20-0F158EFCC83D --target vgname/new_wal
```

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
