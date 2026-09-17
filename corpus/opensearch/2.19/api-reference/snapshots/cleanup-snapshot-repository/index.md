---
collection: "opensearch"
version: "2.19"
title: "Cleanup Snapshot Repository"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/snapshots/cleanup-snapshot-repository.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/snapshots/cleanup-snapshot-repository.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/snapshots/cleanup-snapshot-repository/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/snapshots/cleanup-snapshot-repository/"
canonical_route: "/api-reference/snapshots/cleanup-snapshot-repository/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 11
parent: "Snapshot APIs"
---
# Cleanup Snapshot Repository
Introduced 1.0
{: .label .label-purple }

The Cleanup Snapshot Repository API clears a snapshot repository of data no longer referenced by any existing snapshot.

## Endpoints

```json
POST /_snapshot/<repository>/_cleanup
```

## Path parameters

| Parameter | Data type | Description |
| :--- | :--- | :--- |
| `repository` | String | The name of the snapshot repository. |

## Query parameters

The following table lists the available query parameters. All query parameters are optional.

| Parameter |  Data type | Description |
| :--- | :--- | :--- |
| `cluster_manager_timeout` | Time | The amount of time to wait for a response from the cluster manager node. Formerly called `master_timeout`. Optional. Default is 30 seconds. |
| `timeout` | Time | The amount of time to wait for the operation to complete. Optional.|

## Example request

The following request removes all stale data from the repository `my_backup`:

```json
POST /_snapshot/my_backup/_cleanup
```

## Example response

```json
{
	"results":{
		"deleted_bytes":40,
		"deleted_blobs":8
	}
}
```

## Response body fields

| Field | Data type | Description |
| :--- | :--- | :--- |
| `deleted_bytes` | Integer | The number of bytes made available in the snapshot after data deletion. |
| `deleted_blobs` | Integer | The number of binary large objects (BLOBs) cleared from the repository by the request. |
