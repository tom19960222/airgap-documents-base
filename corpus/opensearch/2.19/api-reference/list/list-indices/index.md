---
collection: "opensearch"
version: "2.19"
title: "List indices"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/list/list-indices.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/list/list-indices.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/list/list-indices/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/list/list-indices/"
canonical_route: "/api-reference/list/list-indices/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
layout: "default"
nav_order: 25
parent: "List API"
---
# List indices
**Introduced 2.18**
{: .label .label-purple }

The list indices operation provides the following index information in a paginated format:

- The amount of disk space used by the index.
- The number of shards contained in the index.
- The index's health status.

## Endpoints

```json
GET _list/indices
GET _list/indices/<index>
```

## Query parameters

Parameter | Type | Description
:--- | :--- | :---
`bytes` | Byte size | Specifies the units for the byte size, for example, `7kb` or `6gb`. For more information, see [Supported units](../../units/index.md).
`health` | String | Limits indexes based on their health status. Supported values are `green`, `yellow`, and `red`.
`include_unloaded_segments` | Boolean | Whether to include information from segments not loaded into memory. Default is `false`.
`cluster_manager_timeout` | Time | The amount of time to wait for a connection to the cluster manager node. Default is `30s`.
`pri` | Boolean | Whether to return information only from the primary shards. Default is `false`.
`time` | Time | Specifies the time units, for example, `5d` or `7h`. For more information, see [Supported units](../../units/index.md).
`expand_wildcards` | Enum | Expands wildcard expressions to concrete indexes. Combine multiple values with commas. Supported values are `all`, `open`, `closed`, `hidden`, and `none`. Default is `open`.
`next_token` | String | Fetches the next page of indexes. When `null`, only provides the first page of indexes. Default is `null`.
`size` | Integer | The maximum number of indexes to be displayed on a single page. The number of indexes on a single page of the response is not always equal to the specified `size`. Default is `500`. Minimum is `1` and maximum value is `5000`.
`sort` | String | The order in which the indexes are displayed. If `desc`, then the most recently created indexes are displayed first. If `asc`, then the oldest indexes are displayed first. Default is `asc`.

When using the `next_token` path parameter, use the token produced by the response to see the next page of indexes. After the API returns `null`, all indexes contained in the API have been returned.
{: .tip }

## Example requests

To get information for all the indexes, use the following query and keep specifying the `next_token` as received from response until its `null`:

```json
GET _list/indices/<index>?v&next_token=token
```

To limit the information to a specific index, add the index name after your query, as shown in the following example:

```json
GET _list/indices/<index>?v
```

To get information about more than one index, separate the indexes with commas, as shown in the following example:

```json
GET _list/indices/index1,index2,index3?v&next_token=token
```

## Example response

**Plain text format**

```json
health | status | index | uuid | pri | rep | docs.count | docs.deleted | store.size | pri.store.size
green  | open | movies | UZbpfERBQ1-3GSH2bnM3sg | 1 | 1 | 1 | 0 | 7.7kb | 3.8kb
next_token MTcyOTE5NTQ5NjM5N3wub3BlbnNlYXJjaC1zYXAtbG9nLXR5cGVzLWNvbmZpZw==
```

**JSON format**

```json
{
  "next_token": "MTcyOTE5NTQ5NjM5N3wub3BlbnNlYXJjaC1zYXAtbG9nLXR5cGVzLWNvbmZpZw==",
  "indices": [
    {
      "health": "green",
      "status": "open",
      "index": "movies",
      "uuid": "UZbpfERBQ1-3GSH2bnM3sg",
      "pri": "1",
      "rep": "1",
      "docs.count": "1",
      "docs.deleted": "0",
      "store.size": "7.7kb",
      "pri.store.size": "3.8kb"
    }
  ]
}
```
