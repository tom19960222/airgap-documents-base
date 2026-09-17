---
collection: "opensearch"
version: "2.19"
title: "Parent ID"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_query-dsl/joining/parent-id.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_query-dsl/joining/parent-id.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/query-dsl/joining/parent-id/"
canonical_url: "https://docs.opensearch.org/latest/query-dsl/joining/parent-id/"
canonical_route: "/query-dsl/joining/parent-id/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 40
parent: "Joining queries"
---
# Parent ID query

The `parent_id` query returns child documents whose parent document has the specified ID. You can establish parent/child relationships between documents in the same index by using a [join](../../../field-types/supported-field-types/join/index.md) field type.

## Example

Before you can run a `parent_id` query, your index must contain a [join](../../../field-types/supported-field-types/join/index.md) field in order to establish parent/child relationships. The index mapping request uses the following format:

```json
PUT /example_index
{
  "mappings": {
    "properties": {
      "relationship_field": {
        "type": "join",
        "relations": {
          "parent_doc": "child_doc"
        }
      }
    }
  }
}
```

For this example, first configure an index that contains documents representing products and their brands as described in the [`has_child` query example](../has-child/index.md).

To search for child documents of a specific parent document, use a `parent_id` query. The following query returns child documents (products) whose parent document has the ID `1`:

```json
GET testindex1/_search
{
  "query": {
    "parent_id": {
      "type": "product",
      "id": "1"
    }
  }
}
```

The response returns the child product:

```json
{
  "took": 57,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 0.87546873,
    "hits": [
      {
        "_index": "testindex1",
        "_id": "3",
        "_score": 0.87546873,
        "_routing": "1",
        "_source": {
          "name": "Mechanical watch",
          "sales_count": 150,
          "product_to_brand": {
            "name": "product",
            "parent": "1"
          }
        }
      }
    ]
  }
}
```

## Parameters

The following table lists all top-level parameters supported by `parent_id` queries.

| Parameter  | Required/Optional | Description  |
|:---|:---|:---|
| `type` | Required | Specifies the name of the child relationship as defined in the `join` field mapping. |
| `id` | Required | The ID of the parent document. The query returns child documents associated with this parent document. |
| `ignore_unmapped` | Optional | Indicates whether to ignore unmapped `type` fields and not return documents instead of throwing an error. You can provide this parameter when querying multiple indexes, some of which may not contain the `type` field. Default is `false`. |
