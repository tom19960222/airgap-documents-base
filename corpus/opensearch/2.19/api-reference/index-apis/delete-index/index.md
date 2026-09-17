---
collection: "opensearch"
version: "2.19"
title: "Delete index"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/index-apis/delete-index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/index-apis/delete-index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/index-apis/delete-index/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/index-apis/delete-index/"
canonical_route: "/api-reference/index-apis/delete-index/"
redirect_from: ["/opensearch/rest-api/index-apis/delete-index/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 22
parent: "Index APIs"
---
# Delete index
**Introduced 1.0**
{: .label .label-purple }

If you no longer need an index, you can use the delete index API operation to delete it.

## Endpoints

```json
DELETE /<index-name>
```

## Query parameters

All parameters are optional.

Parameter | Type | Description
:--- | :--- | :---
allow_no_indices | Boolean | Whether to ignore wildcards that don't match any indexes. Default is `true`.
expand_wildcards | String | Expands wildcard expressions to different indexes. Combine multiple values with commas. Available values are all (match all indexes), open (match open indexes), closed (match closed indexes), hidden (match hidden indexes), and none (do not accept wildcard expressions), which must be used with open, closed, or both. Default is `open`.
ignore_unavailable | Boolean | If true, OpenSearch does not include missing or closed indexes in the response.
cluster_manager_timeout | Time | How long to wait for a connection to the cluster manager node. Default is `30s`.
timeout | Time | How long to wait for the response to return. Default is `30s`.

## Example request

```json
DELETE /sample-index
```

## Example response
```json
{
  "acknowledged": true
}
```
