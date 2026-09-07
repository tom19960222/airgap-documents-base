---
collection: ceph
version: "20.2.4"
title: "`new-wal`"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/ceph-volume/lvm/newwal.rst
fetched_at: 2026-08-18T01:32:45Z
---
<a id="ceph-volume-lvm-newwal"></a>

# ``new-wal``

Attaches the given logical volume to the given OSD as a WAL volume.
Logical volume format is vg/lv. Fails if OSD has already got attached DB.

Attach vgname/lvname as a WAL volume to OSD 1:

```
ceph-volume lvm new-wal --osd-id 1 --osd-fsid 55BD4219-16A7-4037-BC20-0F158EFCC83D --target vgname/new_wal
```
