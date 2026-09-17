---
collection: "opensearch"
version: "2.19"
title: "Store"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/mapping-parameters/store.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/mapping-parameters/store.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/mapping-parameters/store/"
canonical_url: "https://docs.opensearch.org/latest/mappings/mapping-parameters/store/"
canonical_route: "/mappings/mapping-parameters/store/"
redirect_from: ["/mappings/mapping-parameters/store/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Mapping and field types"
has_children: false
has_toc: false
layout: "default"
nav_order: 180
parent: "Mapping parameters"
---
# Store

The `store` mapping parameter determines whether the value of a field should be stored separately from the `_source` and made directly retrievable using the `stored_fields` option in a search request.

By default, `store` is set to `false`, meaning that field values are not stored individually and are only available as part of the document `_source`. If `store` is set to `true`, you can disable the `_source` to save disk space and still [retrieve specific fields](../../../search-plugins/searching-data/retrieve-specific-fields/index.md).

## Example: Enabling `store` on a field

The following request creates an index named `products` in which the `model` field is stored separately from the `_source`:

```json
PUT /products
{
  "mappings": {
    "properties": {
      "model": {
        "type": "keyword",
        "store": true
      },
      "name": {
        "type": "text"
      }
    }
  }
}
```

Ingest a document into the index:

```json
PUT /products/_doc/1
{
  "model": "WM-1001",
  "name": "Wireless Mouse"
}
```

Retrieve only the stored field:

```json
POST /products/_search
{
  "query": {
    "match": {
      "name": "Mouse"
    }
  },
  "stored_fields": ["model"]
}
```

This query returns the `model` field stored separately even though the `_source` is still available.

---

## Example: Storing fields with `_source` disabled

If you want to save disk space and don't need to access the full original document later (for example, for reindexing or updates), you can disable `_source` and store only necessary fields:

```json
PUT /products_no_source
{
  "mappings": {
    "_source": {
      "enabled": false
    },
    "properties": {
      "model": {
        "type": "keyword",
        "store": true
      },
      "name": {
        "type": "text"
      }
    }
  }
}
```

Ingest a document into the index:

```json
PUT /products_no_source/_doc/1
{
  "model": "KB-2002",
  "name": "Mechanical Keyboard"
}
```

Retrieve the stored field:

```json
POST /products_no_source/_search
{
  "query": {
    "match": {
      "name": "Keyboard"
    }
  },
  "stored_fields": ["model"]
}
```

This query returns the `model` field retrieved from `stored_fields` without accessing the `_source`.

If you attempt to retrieve the `_source` as follows:

```json
GET /products_no_source/_doc/1
```

Then the `_source` in the response will be `null`. This demonstrates that the full document is no longer available and that only stored fields can be retrieved because `_source` is disabled:

```json
{
  "_index": "products_no_source",
  "_id": "1",
  "found": true,
  "_source": null
}
```
