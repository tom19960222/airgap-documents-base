---
collection: ceph
version: "20.2.4"
title: "`drive-group`"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/ceph-volume/drive-group.rst
fetched_at: 2026-08-18T01:32:45Z
---
<a id="ceph-volume-drive-group"></a>

# ``drive-group``
The drive-group subcommand allows for passing [drivegroups](../cephadm/services/osd.md#drivegroups) specifications
straight to ceph-volume as json. ceph-volume will then attempt to deploy this
drive groups via the batch subcommand.

The specification can be passed via a file, string argument or on stdin.
See the subcommand help for further details:

```bash
ceph-volume drive-group --help
```
