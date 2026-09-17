---
collection: "opensearch"
version: "2.19"
title: "Index"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/mapping-parameters/index-parameter.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/mapping-parameters/index-parameter.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/mapping-parameters/index-parameter/"
canonical_url: "https://docs.opensearch.org/latest/mappings/mapping-parameters/index-parameter/"
canonical_route: "/mappings/mapping-parameters/index-parameter/"
redirect_from: ["/mappings/mapping-parameters/index-parameter/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Mapping and field types"
has_children: false
has_toc: false
layout: "default"
nav_order: 60
parent: "Mapping parameters"
---
# Index

The `index` mapping parameter controls whether a field is searchable by including it in the inverted index. When set to `true`, the field is indexed and available for queries. When set to `false`, the field is stored in the document but not indexed, making it non-searchable. If you do not need to search a particular field, disabling indexing for that field can reduce index size and improve indexing performance. For example, you can disable indexing on large text fields or metadata that is only used for display.

By default, all field types are indexed.

## Supported data types

The `index` mapping parameter can be applied to the following data types:

- [Text](../../supported-field-types/text/index.md)
- [Keyword](../../supported-field-types/keyword/index.md)
- [Boolean](../../supported-field-types/boolean/index.md)
- [IP address](../../supported-field-types/ip/index.md)
- [Date field types](../../supported-field-types/dates/index.md)
- [Numeric field types](../../supported-field-types/numeric/index.md)

## Enabling indexing on a field

The following request creates an index named `products` with a `description` field that is indexed (the default behavior):

```json
PUT /products
{
  "mappings": {
    "properties": {
      "description": {
        "type": "text"
      }
    }
  }
}
```

Index a document using the following request:

```json
PUT /products/_doc/1
{
  "description": "This product has a searchable description."
}
```

Query the description field:

```json
POST /products/_search
{
  "query": {
    "match": {
      "description": "searchable"
    }
  }
}
```

The following response confirms that the indexed document was successfully matched by the query:

```json
{
  ...
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 0.2876821,
    "hits": [
      {
        "_index": "products",
        "_id": "1",
        "_score": 0.2876821,
        "_source": {
          "description": "This product has a searchable description."
        }
      }
    ]
  }
}
```

## Disabling indexing on a field

Create an index named `products-no-index` with a `description` field that is not indexed:

```json
PUT /products-no-index
{
  "mappings": {
    "properties": {
      "description": {
        "type": "text",
        "index": false
      }
    }
  }
}
```

Index a document using the following request:

```json
PUT /products-no-index/_doc/1
{
  "description": "This product has a non-searchable description."
}
```

Query `products-no-index` using the `description` field:

```json
POST /products-no-index/_search
{
  "query": {
    "match": {
      "description": "non-searchable"
    }
  }
}
```

The following error response indicates that the search query failed because the description field is not indexed:

```json
{
  "error": {
    "root_cause": [
      {
        "type": "query_shard_exception",
        "reason": "failed to create query: Cannot search on field [description] since it is not indexed.",
        "index": "products-no-index",
        "index_uuid": "yX2F4En1RqOBbf3YWihGCQ"
      }
    ],
    "type": "search_phase_execution_exception",
    "reason": "all shards failed",
    "phase": "query",
    "grouped": true,
    "failed_shards": [
      {
        "shard": 0,
        "index": "products-no-index",
        "node": "0tmy2tf7TKW8qCmya9sG2g",
        "reason": {
          "type": "query_shard_exception",
          "reason": "failed to create query: Cannot search on field [description] since it is not indexed.",
          "index": "products-no-index",
          "index_uuid": "yX2F4En1RqOBbf3YWihGCQ",
          "caused_by": {
            "type": "illegal_argument_exception",
            "reason": "Cannot search on field [description] since it is not indexed."
          }
        }
      }
    ]
  },
  "status": 400
}
```
