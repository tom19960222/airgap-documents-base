---
collection: "opensearch"
version: "2.19"
title: "Create or update mappings"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/index-apis/put-mapping.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/index-apis/put-mapping.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/index-apis/put-mapping/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/index-apis/put-mapping/"
canonical_route: "/api-reference/index-apis/put-mapping/"
redirect_from: ["/opensearch/rest-api/index-apis/put-mapping/","/opensearch/rest-api/index-apis/update-mapping/","/opensearch/rest-api/update-mapping/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 30
parent: "Index APIs"
---
# Create or update mappings
**Introduced 1.0**
{: .label .label-purple }

If you want to create or add mappings and fields to an index, you can use the put mapping API operation. For an existing mapping, this operation updates the mapping.

You can't use this operation to update mappings that already map to existing data in the index. You must first create a new index with your desired mappings, and then use the [reindex API operation](../../document-apis/reindex/index.md) to map all the documents from your old index to the new index. If you don't want any downtime while you re-index your indexes, you can use [aliases](../../../im-plugin/index-alias/index.md).

## Endpoints

```json
PUT /<target-index>/_mapping
PUT /<target-index1>,<target-index2>/_mapping
```

## Path parameters

The only required path parameter is the index with which to associate the mapping. If you don't specify an index, you will get an error. You can specify a single index, or multiple indexes separated by a comma as follows:

```json
PUT /<target-index>/_mapping
PUT /<target-index1>,<target-index2>/_mapping
```

## Query parameters

Optionally, you can add query parameters to make a more specific request. For example, to skip any missing or closed indexes in the response, you can add the `ignore_unavailable` query parameter to your request as follows:

```json
PUT /sample-index/_mapping?ignore_unavailable
```

The following table defines the put mapping query parameters:

Parameter | Data type | Description
:--- | :--- | :---
allow_no_indices | Boolean | Whether to ignore wildcards that don’t match any indexes. Default is `true`.
expand_wildcards | String | Expands wildcard expressions to different indexes. Combine multiple values with commas. Available values are `all` (match all indexes), `open` (match open indexes), `closed` (match closed indexes), `hidden` (match hidden indexes), and `none` (do not accept wildcard expressions), which must be used with `open`, `closed`, or both. Default is `open`.
ignore_unavailable | Boolean | If true, OpenSearch does not include missing or closed indexes in the response.
cluster_manager_timeout | Time | How long to wait for a connection to the cluster manager node. Default is `30s`.
timeout | Time | How long to wait for the response to return. Default is `30s`.
write_index_only | Boolean | Whether OpenSearch should apply mapping updates only to the write index.

## Request body fields

### properties

The request body must contain `properties`, which has all of the mappings that you want to create or update.

```json
{
  "properties":{
    "color":{
      "type": "text"
    },
    "year":{
      "type": "integer"
    }
  }
}
```

### dynamic

You can make the document structure match the structure of the index mapping by setting the `dynamic` request body field to `strict`, as seen in the following example:

```json
{
  "dynamic": "strict",
  "properties":{
    "color":{
      "type": "text"
    }
  }
}
```

## Example request

The following request creates a new mapping for the `sample-index` index:

```json
PUT /sample-index/_mapping

{
  "properties": {
    "age": {
      "type": "integer"
    },
    "occupation":{
      "type": "text"
    }
  }
}
```

## Example response

Upon success, the response returns `"acknowledged": true`.

```json
{
    "acknowledged": true
}
```
