---
collection: "opensearch"
version: "2.19"
title: "Shallow snapshots"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_tuning-your-cluster/availability-and-recovery/remote-store/snapshot-interoperability.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_tuning-your-cluster/availability-and-recovery/remote-store/snapshot-interoperability.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/tuning-your-cluster/availability-and-recovery/remote-store/snapshot-interoperability/"
canonical_url: "https://docs.opensearch.org/latest/tuning-your-cluster/availability-and-recovery/remote-store/snapshot-interoperability/"
canonical_route: "/tuning-your-cluster/availability-and-recovery/remote-store/snapshot-interoperability/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Availability and recovery"
layout: "default"
nav_order: 15
parent: "Remote-backed storage"
---
# Shallow snapshots

Shallow copy snapshots allow you to reference data from an entire remote-backed repository instead of storing all of the data from the segment in a snapshot repository. This makes accessing segment data faster than using normal snapshots because segment data is not stored in the snapshot repository.

## Enabling shallow snapshots

Use the [Snapshot API](../../../../api-reference/snapshots/create-repository/index.md) and set the `remote_store_index_shallow_copy` repository setting to `true` to enable shallow snapshot copies, as shown in the following example:

```bash
PUT /_snapshot/snap_repo
{
        "type": "s3",
        "settings": {
            "bucket": "test-bucket",
            "base_path": "daily-snaps",
            "remote_store_index_shallow_copy": true
        }
    }
```

Once enabled, all requests using the [Snapshot API](../../../../api-reference/snapshots/index.md) will remain the same for all snapshots. Therefore, do not disable the shallow snapshot setting after it has been enabled because disabling the setting could affect data durability.

## Considerations

Consider the following before using shallow copy snapshots:

- Shallow copy snapshots only work for remote-backed indexes.
- All nodes in the cluster must use OpenSearch 2.10 or later to take advantage of shallow copy snapshots.
- The `incremental` file count and size between the current snapshot and the last snapshot is `0` when using shallow copy snapshots.
- Searchable snapshots are not supported inside shallow copy snapshots.

## Shallow snapshot v2

Starting with OpenSearch 2.17, the shallow snapshot feature offers an improved version called `shallow snapshot v2`, which aims to makes snapshot operations more efficient and scalable by introducing the following enhancements:

* Deterministic snapshot operations: Shallow snapshot v2 makes snapshot operations more deterministic, ensuring consistent and predictable behavior.
* Minimized cluster state updates: Shallow snapshot v2 minimizes the number of cluster state updates required during snapshot operations, reducing overhead and improving performance.
* Scalability: Shallow snapshot v2 allows snapshot operations to scale independently of the number of shards in the cluster, enabling better performance and efficiency for large datasets.

Shallow snapshot v2 must be enabled separately from shallow copies.

### Enabling shallow snapshot v2

To enable shallow snapshot v2, enable the following repository settings:

- `remote_store_index_shallow_copy: true`
- `shallow_snapshot_v2: true`

The following example request creates a shallow snapshot v2 repository:

```bash
PUT /_snapshot/snap_repo
{
"type": "s3",
"settings": {
"bucket": "test-bucket",
"base_path": "daily-snaps",
"remote_store_index_shallow_copy": true,
"shallow_snapshot_v2": true
}
}
```

### Limitations

Shallow snapshot v2 has the following limitations:

* Shallow snapshot v2 only supported for remote-backed indexes.
* All nodes in the cluster must use OpenSearch 2.17 or later to take advantage of shallow snapshot v2.
