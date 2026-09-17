---
collection: "opensearch"
version: "2.19"
title: "Norms"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/mapping-parameters/norms.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/mapping-parameters/norms.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/mapping-parameters/norms/"
canonical_url: "https://docs.opensearch.org/latest/mappings/mapping-parameters/norms/"
canonical_route: "/mappings/mapping-parameters/norms/"
redirect_from: ["/mappings/mapping-parameters/norms/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Mapping and field types"
has_children: false
has_toc: false
layout: "default"
nav_order: 120
parent: "Mapping parameters"
---
# Norms

The `norms` mapping parameter controls whether normalization factors are computed and stored for a field. These factors are used during query scoring to adjust the relevance of the search results. However, storing `norms` increases the index size and consumes additional memory.

By default, `norms` is enabled on `text` fields, for which relevance scoring is important. Fields that do not require these scoring features, such as `keyword` fields used only for filtering, are configured with `norms` disabled.

## Disabling `norms` on a field

The following request creates an index named `products` with the `description` field as a `text` field with `norms` disabled:

```json
PUT /products
{
  "mappings": {
    "properties": {
      "description": {
        "type": "text",
        "norms": false
      }
    }
  }
}
```

To disable `norms` on a field in an existing index, use the following request:

```json
PUT /products/_mapping
{
  "properties": {
    "review": {
      "type": "text",
      "norms": false
    }
  }
}
```

Enabling `norms` on a field that has `norms` disabled is impossible and will result in the following error:

```json
{
  "error": {
    "root_cause": [
      {
        "type": "illegal_argument_exception",
        "reason": "Mapper for [description] conflicts with existing mapper:\n\tCannot update parameter [norms] from [false] to [true]"
      }
    ],
    "type": "illegal_argument_exception",
    "reason": "Mapper for [description] conflicts with existing mapper:\n\tCannot update parameter [norms] from [false] to [true]"
  },
  "status": 400
}
```
