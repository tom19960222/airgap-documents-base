---
collection: ceph
version: "19.2.2"
title: "CephFS delayed deletion"
source_url: https://docs.ceph.com/en/squid/dev/delayed-delete/
fetched_at: 2026-07-27T16:41:18+00:00
---
# CephFS delayed deletion

The deletion of a file does not immediately remove its data. Each of the file’s
underlying objects must be removed independently. If these objects were removed
immediately, the client would have to send `size_of_file / stripe_size *
replication_count` messages. This would consume significant bandwith and would
slow the client unacceptably. If snapshots exist, their existence can prevent
the deletion of objects associated with them.

In these cases, such files are (1) marked as deleted on the MDS and (2) deleted
lazily.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
