---
collection: "opensearch"
version: "2.19"
title: "Create index"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/index-apis/create-index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/index-apis/create-index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/index-apis/create-index/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/index-apis/create-index/"
canonical_route: "/api-reference/index-apis/create-index/"
redirect_from: ["/opensearch/rest-api/index-apis/create-index/","/opensearch/rest-api/create-index/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 21
parent: "Index APIs"
---
# Create index
**Introduced 1.0**
{: .label .label-purple }

While you can create an index by using a document as a base, you can also create an empty index for later use.

When creating an index, you can specify its mappings, settings, and aliases.

## Endpoints

```json
PUT <index>
```

## Index naming restrictions

OpenSearch indexes have the following naming restrictions:

- All letters must be lowercase.
- Index names can't begin with underscores (`_`) or hyphens (`-`).
- Index names can't contain spaces, commas, or the following characters:

  `:`, `"`, `*`, `+`, `/`, `\`, `|`, `?`, `#`, `>`, or `<`

## Path parameters

Parameter | Data type | Description
:--- | :--- | :---
index | String | The index name. Must conform to the [index naming restrictions](#index-naming-restrictions). Required.

## Query parameters

You can include the following query parameters in your request. All parameters are optional.

Parameter | Type | Description
:--- | :--- | :---
wait_for_active_shards | String | Specifies the number of active shards that must be available before OpenSearch processes the request. Default is 1 (only the primary shard). Set to `all` or a positive integer. Values greater than 1 require replicas. For example, if you specify a value of 3, the index must have two replicas distributed across two additional nodes for the request to succeed.
cluster_manager_timeout | Time | How long to wait for a connection to the cluster manager node. Default is `30s`.
timeout | Time | How long to wait for the request to return. Default is `30s`.

## Request body

As part of your request, you can optionally specify [index settings](../../../install-and-configure/configuring-opensearch/index-settings/index.md), [mappings](../../../field-types/index.md), [aliases](../../../im-plugin/index-alias/index.md), and [index context](../../../im-plugin/index-context/index.md).

## Example request

```json
PUT /sample-index1
{
  "settings": {
    "index": {
      "number_of_shards": 2,
      "number_of_replicas": 1
    }
  },
  "mappings": {
    "properties": {
      "age": {
        "type": "integer"
      }
    }
  },
  "aliases": {
    "sample-alias1": {}
  }
}
```
