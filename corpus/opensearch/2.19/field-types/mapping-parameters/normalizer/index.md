---
collection: "opensearch"
version: "2.19"
title: "Normalizer"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/mapping-parameters/normalizer.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/mapping-parameters/normalizer.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/mapping-parameters/normalizer/"
canonical_url: "https://docs.opensearch.org/latest/mappings/mapping-parameters/normalizer/"
canonical_route: "/mappings/mapping-parameters/normalizer/"
redirect_from: ["/mappings/mapping-parameters/normalizer/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Mapping and field types"
has_children: false
has_toc: false
layout: "default"
nav_order: 110
parent: "Mapping parameters"
---
# Normalizer

The `normalizer` mapping parameter defines a custom normalization process for keyword fields. Unlike [analyzers](../../../analyzers/supported-analyzers/index.md) for text fields, which generate multiple tokens, [normalizers](../../../analyzers/normalizers/index.md) transform the entire field value into a single token using a set of token filters. When you define a normalizer, the keyword field is processed by the specified filters before it is stored while keeping the `_source` of the document unchanged.

## Defining a normalizer

The following request creates an index named `products` with a custom normalizer called `my_normalizer`. The normalizer is applied to the `code` field, which uses the `trim` and `lowercase` filters:

```json
PUT /products
{
  "settings": {
    "analysis": {
      "normalizer": {
        "my_normalizer": {
          "type": "custom",
          "filter": ["trim", "lowercase"]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "code": {
        "type": "keyword",
        "normalizer": "my_normalizer"
      }
    }
  }
}
```

When you ingest a document into the index, the `code` field is normalized by trimming any extra spaces and converting the text to lowercase:

```json
PUT /products/_doc/1
{
  "code": "  ABC-123 EXTRA  "
}
```

Search for the indexed document using lowercase and trimmed text in the query:

```json
POST /products/_search
{
  "query": {
    "term": {
      "code": "abc-123 extra"
    }
  }
}
```

Because the `code` field is normalized, the `term` query successfully matches the stored document:

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
          "code": "  ABC-123 EXTRA  "
        }
      }
    ]
  }
}
```
