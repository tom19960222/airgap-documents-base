---
collection: "opensearch"
version: "2.19"
title: "Clone index"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/index-apis/clone.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/index-apis/clone.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/index-apis/clone/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/index-apis/clone/"
canonical_route: "/api-reference/index-apis/clone/"
redirect_from: ["/opensearch/rest-api/index-apis/clone/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 15
parent: "Index APIs"
---
# Clone index
**Introduced 1.0**
{: .label .label-purple }

The clone index API operation clones all data in an existing read-only index into a new index. The new index cannot already exist.

## Endpoints

```json
POST /<source-index>/_clone/<target-index>
PUT /<source-index>/_clone/<target-index>
```

## Index naming restrictions

OpenSearch indexes have the following naming restrictions:

- All letters must be lowercase.
- Index names can't begin with underscores (`_`) or hyphens (`-`).
- Index names can't contain spaces, commas, or the following characters:

  `:`, `"`, `*`, `+`, `/`, `\`, `|`, `?`, `#`, `>`, or `<`

## Path parameter

Parameter | Type | Description
:--- | :--- | :---
&lt;source-index&gt; | String | The source index to clone.
&lt;target-index&gt; | String | The index to create and add cloned data to.

## Query parameters

Your request must include the source and target indexes. All other clone index parameters are optional.

Parameter | Type | Description
:--- | :--- | :---
wait_for_active_shards | String | The number of active shards that must be available before OpenSearch processes the request. Default is 1 (only the primary shard). Set to all or a positive integer. Values greater than 1 require replicas. For example, if you specify a value of 3, the index must have two replicas distributed across two additional nodes for the operation to succeed.
cluster_manager_timeout | Time | How long to wait for a connection to the cluster manager node. Default is `30s`.
timeout | Time | How long to wait for the request to return. Default is `30s`.
wait_for_completion | Boolean | When set to `false`, the request returns immediately instead of after the operation is finished. To monitor the operation status, use the [Tasks API](../../tasks/tasks/index.md) with the task ID returned by the request. Default is `true`.
task_execution_timeout | Time | The explicit task execution timeout. Only useful when wait_for_completion is set to `false`. Default is `1h`.

## Request body

The clone index API operation creates a new target index, so you can specify any [index settings](../../../install-and-configure/configuring-opensearch/index-settings/index.md) and [aliases](../../../im-plugin/index-alias/index.md) to apply to the target index.

## Example request

```json
PUT /sample-index1/_clone/cloned-index1
{
  "settings": {
    "index": {
      "number_of_shards": 2,
      "number_of_replicas": 1
    }
  },
  "aliases": {
    "sample-alias1": {}
  }
}
```

## Example response

```json
{
    "acknowledged": true,
    "shards_acknowledged": true,
    "index": "cloned-index1"
}
```
