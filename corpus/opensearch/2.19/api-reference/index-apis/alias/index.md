---
collection: "opensearch"
version: "2.19"
title: "Alias"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/index-apis/alias.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/index-apis/alias.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/index-apis/alias/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/alias/aliases-api/"
canonical_route: "/api-reference/alias/aliases-api/"
redirect_from: ["/opensearch/rest-api/alias/","/api-reference/alias/","/api-reference/alias/aliases-api/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 5
parent: "Index APIs"
---
# Alias
**Introduced 1.0**
{: .label .label-purple }

An alias is a virtual pointer that you can use to reference one or more indexes. Creating and updating aliases are atomic operations, so you can reindex your data and point an alias at it without any downtime.

## Endpoints

```json
POST _aliases
```

## Query parameters

All parameters are optional.

Parameter | Data Type | Description
:--- | :--- | :---
cluster_manager_timeout | Time | The amount of time to wait for a response from the cluster manager node. Default is `30s`.
timeout | Time | The amount of time to wait for a response from the cluster. Default is `30s`.

## Request body fields

In your request body, you need to specify what action to take, the alias name, and the index you want to associate with the alias. Other fields are optional.

Field | Data Type | Description | Required
:--- | :--- | :--- | :---
actions | Array | Set of actions you want to perform on the index. Valid options are: `add`, `remove`, and `remove_index`. You must have at least one action in the array. | Yes
add | N/A | Adds an alias to the specified index. | No
remove | N/A | Removes an alias from the specified index. | No
remove_index | N/A | Deletes an index. | No
index | String | Name of the index you want to associate with the alias. Supports wildcard expressions. | Yes if you don't supply an `indices` field in the body.
indices | Array | Array of index names you want to associate with the alias. | Yes if you don't supply an `index` field in the body.
alias | String | The name of the alias. | Yes if you don't supply an `aliases` field in the body.
aliases | Array | Array of alias names. | Yes if you don't supply an `alias` field in the body.
filter | Object | A filter to use with the alias, so the alias points to a filtered part of the index. | No
is_hidden | Boolean | Specifies whether the alias should be hidden from results that include wildcard expressions | No
must_exist | Boolean | Specifies whether the alias to remove must exist. | No
is_write_index | Boolean | Specifies whether the index should be a write index. An alias can only have one write index at a time. If a write request is submitted to a alias that links to multiple indexes, OpenSearch executes the request only on the write index. | No
routing | String | Used to assign a custom value to a shard for specific operations. | No
index_routing | String | Assigns a custom value to a shard only for index operations. | No
search_routing | String | Assigns a custom value to a shard only for search operations. | No

## Example request

```json
POST _aliases
{
  "actions": [
    {
      "add": {
        "index": "movies",
        "alias": "movies-alias1"
      }
    },
    {
      "remove": {
        "index": "old-index",
        "alias": "old-index-alias"
      }
    }
  ]
}
```

## Example response

```json
{
    "acknowledged": true
}
```

For more alias API operations, see [Index aliases](../../../im-plugin/index-alias/index.md).
