---
collection: "opensearch"
version: "2.19"
title: "Count"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/count.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/count.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/count/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/search-apis/count/"
canonical_route: "/api-reference/search-apis/count/"
redirect_from: ["/opensearch/rest-api/count/","/api-reference/search-apis/count/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 21
---
# Count
**Introduced 1.0**
{: .label .label-purple }

The count API gives you quick access to the number of documents that match a query.
You can also use it to check the document count of an index, data stream, or cluster.

## Endpoints

```json
GET <target>/_count/<id>
POST <target>/_count/<id>
```

## Query parameters

All parameters are optional.

Parameter | Type | Description
:--- | :--- | :---
`allow_no_indices` | Boolean | If false, the request returns an error if any wildcard expression or index alias targets any closed or missing indexes. Default is `false`.
`analyzer` | String | The analyzer to use in the query string.
`analyze_wildcard` | Boolean | Specifies whether to analyze wildcard and prefix queries. Default is `false`.
`default_operator` | String | Indicates whether the default operator for a string query should be `AND` or `OR`. Default is `OR`.
`df` | String | The default field in case a field prefix is not provided in the query string.
`expand_wildcards` | String | Specifies the type of index that wildcard expressions can match. Supports comma-separated values. Valid values are `all` (match any index), `open` (match open, non-hidden indexes), `closed` (match closed, non-hidden indexes), `hidden` (match hidden indexes), and `none` (deny wildcard expressions). Default is `open`.
`ignore_unavailable` | Boolean | Specifies whether to include missing or closed indexes in the response. Default is `false`.
`lenient` | Boolean | Specifies whether OpenSearch should accept requests if queries have format errors (for example, querying a text field for an integer). Default is `false`.
`min_score` | Float |	Include only documents with a minimum `_score` value in the result.
`routing` | String | Value used to route the operation to a specific shard.
`preference` | String | Specifies which shard or node OpenSearch should perform the count operation on.
`terminate_after` | Integer | The maximum number of documents OpenSearch should process before terminating the request.

## Example requests

To see the number of documents that match a query:

```json
GET opensearch_dashboards_sample_data_logs/_count
{
  "query": {
    "term": {
      "response": "200"
    }
  }
}
```

The following call to the search API produces equivalent results:

```json
GET opensearch_dashboards_sample_data_logs/_search
{
  "query": {
    "term": {
      "response": "200"
    }
  },
  "size": 0,
  "track_total_hits": true
}
```

To see the number of documents in an index:

```json
GET opensearch_dashboards_sample_data_logs/_count
```

To check for the number of documents in a [data stream](../../im-plugin/data-streams/index.md), replace the index name with the data stream name.

To see the number of documents in your cluster:

```json
GET _count
```

Alternatively, you could use the [cat indexes](../cat/cat-indices/index.md) and [cat count](../cat/cat-count/index.md) APIs to see the number of documents per index or data stream.
{: .note }

## Example response

```json
{
  "count" : 14074,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  }
}
```
