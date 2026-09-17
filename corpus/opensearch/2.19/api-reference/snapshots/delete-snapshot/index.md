---
collection: "opensearch"
version: "2.19"
title: "Delete Snapshot"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/snapshots/delete-snapshot.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/snapshots/delete-snapshot.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/snapshots/delete-snapshot/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/snapshots/delete-snapshot/"
canonical_route: "/api-reference/snapshots/delete-snapshot/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 7
parent: "Snapshot APIs"
---
## Delete snapshot
**Introduced 1.0**
{: .label .label-purple }

Deletes a snapshot from a repository.

Deleting a snapshot that is in progress stops the snapshot operation and deletes the partially created snapshot.

* To learn more about snapshots, see [Snapshots](../../../tuning-your-cluster/availability-and-recovery/snapshots/index.md).

* To view a list of your repositories, see [cat repositories](../../cat/cat-repositories/index.md).

* To view a list of your snapshots, see [cat snapshots](../../cat/cat-snapshots/index.md).

## Path and HTTP method

```json
DELETE _snapshot/<repository>/<snapshot>
```

## Path parameters

Parameter | Data type | Description
:--- | :--- | :---
repository | String | Repository that contains the snapshot. |
snapshot | String | Snapshot to delete. |

## Example request

The following request deletes a snapshot called `my-first-snapshot` from the `my-opensearch-repo` repository:

```json
DELETE _snapshot/my-opensearch-repo/my-first-snapshot
```

## Example response

Upon success, the response returns the following JSON object:

```json
{
  "acknowledged": true
}
```

To verify that the snapshot was deleted, use the [Get snapshot](../get-snapshot/index.md) API, passing the snapshot name as the `snapshot` path parameter.
{: .note}
