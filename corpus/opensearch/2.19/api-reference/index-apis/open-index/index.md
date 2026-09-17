---
collection: "opensearch"
version: "2.19"
title: "Open index"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/index-apis/open-index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/index-apis/open-index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/index-apis/open-index/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/index-apis/open-index/"
canonical_route: "/api-reference/index-apis/open-index/"
redirect_from: ["/opensearch/rest-api/index-apis/open-index/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 17
parent: "Index APIs"
---
# Open index
**Introduced 1.0**
{: .label .label-purple }

The open index API operation opens a closed index, letting you add or search for data within the index.

## Endpoints

```json
POST /<index>/_open
```

## Path parameters

Parameter | Type | Description
:--- | :--- | :---
&lt;index&gt; | String | The index to open. Can be a comma-separated list of multiple index names. Use `_all` or * to open all indexes.

## Query parameters

All parameters are optional.

Parameter | Type | Description
:--- | :--- | :---
allow_no_indices | Boolean | Whether to ignore wildcards that don't match any indexes. Default is `true`.
expand_wildcards | String | Expands wildcard expressions to different indexes. Combine multiple values with commas. Available values are all (match all indexes), open (match open indexes), closed (match closed indexes), hidden (match hidden indexes), and none (do not accept wildcard expressions). Default is `open`.
ignore_unavailable | Boolean | If true, OpenSearch does not search for missing or closed indexes. Default is `false`.
wait_for_active_shards | String | Specifies the number of active shards that must be available before OpenSearch processes the request. Default is 1 (only the primary shard). Set to all or a positive integer. Values greater than 1 require replicas. For example, if you specify a value of 3, the index must have two replicas distributed across two additional nodes for the request to succeed.
cluster_manager_timeout | Time | How long to wait for a connection to the cluster manager node. Default is `30s`.
timeout | Time | How long to wait for a response from the cluster. Default is `30s`.
wait_for_completion | Boolean | When set to `false`, the request returns immediately instead of after the operation is finished. To monitor the operation status, use the [Tasks API](../../tasks/tasks/index.md) with the task ID returned by the request. Default is `true`.
task_execution_timeout | Time | The explicit task execution timeout. Only useful when wait_for_completion is set to `false`. Default is `1h`.

## Example request

```json
POST /sample-index/_open
```

## Example response
```json
{
  "acknowledged": true,
  "shards_acknowledged": true
}
```
