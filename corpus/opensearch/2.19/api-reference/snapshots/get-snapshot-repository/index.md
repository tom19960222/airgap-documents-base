---
collection: "opensearch"
version: "2.19"
title: "Get Snapshot Repository"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/snapshots/get-snapshot-repository.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/snapshots/get-snapshot-repository.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/snapshots/get-snapshot-repository/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/snapshots/get-snapshot-repository/"
canonical_route: "/api-reference/snapshots/get-snapshot-repository/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 2
parent: "Snapshot APIs"
---
# Get snapshot repository.
**Introduced 1.0**
{: .label .label-purple }

Retrieves information about a snapshot repository.

To learn more about repositories, see [Register repository](../../../tuning-your-cluster/availability-and-recovery/snapshots/snapshot-restore/index.md#register-repository).

You can also get details about a snapshot during and after snapshot creation. See [Get snapshot status](../get-snapshot-status/index.md).
{: .note}

## Endpoints

```json
GET /_snapshot/<repository>
```

## Path parameters

| Parameter | Data type | Description |
| :--- | :--- | :--- |
| repository | String | A comma-separated list of snapshot repository names to retrieve. Wildcard (`*`) expressions are supported including combining wildcards with exclude patterns starting with `-`. |

## Query parameters

| Parameter | Data type | Description |
:--- | :--- | :---
| local | Boolean | Whether to get information from the local node. Optional, defaults to `false`.|
| cluster_manager_timeout | Time | Amount of time to wait for a connection to the cluster manager node. Optional, defaults to 30 seconds. |

## Example request

The following request retrieves information for the `my-opensearch-repo` repository:

````json
GET /_snapshot/my-opensearch-repo
````

## Example response

Upon success, the response returns repositry information. This sample is for an `s3` repository type.

````json
{
  "my-opensearch-repo" : {
    "type" : "s3",
    "settings" : {
      "bucket" : "my-open-search-bucket",
      "base_path" : "snapshots"
    }
  }
}
````

## Response body fields

| Field | Data type | Description |
| :--- | :--- | :--- |
| type | string | Bucket type: `fs` (file system) or `s3` (s3 bucket) |
| bucket | string | S3 bucket name. |
| base_path | string | Folder within the bucket where snapshots are stored. |
