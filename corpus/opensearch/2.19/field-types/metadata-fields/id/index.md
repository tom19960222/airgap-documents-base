---
collection: "opensearch"
version: "2.19"
title: "ID"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/metadata-fields/id.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/metadata-fields/id.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/metadata-fields/id/"
canonical_url: "https://docs.opensearch.org/latest/mappings/metadata-fields/id/"
canonical_route: "/mappings/metadata-fields/id/"
redirect_from: ["/mappings/metadata-fields/id/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 20
parent: "Metadata fields"
---
# ID

Each document in OpenSearch has a unique `_id` field. This field is indexed, allowing you to retrieve documents using the GET API or the [`ids` query](../../../query-dsl/term/ids/index.md).

If you do not provide an `_id` value, then OpenSearch automatically generates one for the document.
{: .note}

The following example request creates an index named `test-index1` and adds two documents with different `_id` values:

```json
PUT test-index1/_doc/1
{
  "text": "Document with ID 1"
}

PUT test-index1/_doc/2?refresh=true
{
  "text": "Document with ID 2"
}
```

You can then query the documents using the `_id` field, as shown in the following example request:

```json
GET test-index1/_search
{
  "query": {
    "terms": {
      "_id": ["1", "2"]
    }
  }
}
```

The response returns both documents with `_id` values of `1` and `2`:

```json
{
  "took": 10,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 2,
      "relation": "eq"
    },
    "max_score": 1,
    "hits": [
      {
        "_index": "test-index1",
        "_id": "1",
        "_score": 1,
        "_source": {
          "text": "Document with ID 1"
        }
      },
      {
        "_index": "test-index1",
        "_id": "2",
        "_score": 1,
        "_source": {
          "text": "Document with ID 2"
        }
      }
    ]
  }
```

## Limitations of the `_id` field

While the `_id` field can be used in various queries, it is restricted from use in aggregations, sorting, and scripting. If you need to sort or aggregate on the `_id` field, it is recommended to duplicate the `_id` content into another field with `doc_values` enabled. Refer to [IDs query](../../../query-dsl/term/ids/index.md) for an example.
