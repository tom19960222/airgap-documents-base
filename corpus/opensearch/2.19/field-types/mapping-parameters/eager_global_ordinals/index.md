---
collection: "opensearch"
version: "2.19"
title: "Eager global ordinals"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/mapping-parameters/eager_global_ordinals.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/mapping-parameters/eager_global_ordinals.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/mapping-parameters/eager_global_ordinals/"
canonical_url: "https://docs.opensearch.org/latest/mappings/mapping-parameters/eager_global_ordinals/"
canonical_route: "/mappings/mapping-parameters/eager_global_ordinals/"
redirect_from: ["/mappings/mapping-parameters/eager_global_ordinals/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Mapping and field types"
has_children: false
has_toc: false
layout: "default"
nav_order: 35
parent: "Mapping parameters"
---
# Eager global ordinals

The `eager_global_ordinals` mapping parameter controls when global ordinals are built for a field. When enabled, global ordinals are computed during index refresh rather than "lazily" during query execution. This can improve performance for operations that rely on global ordinals, for example, sorting and aggregations on keyword fields. However, it may also increase index refresh times and memory usage.

Global ordinals represent a mapping from term values to integer identifiers and are used internally to quickly execute aggregations and sort operations. By loading them "eagerly," the system reduces query latency at the cost of additional upfront processing during indexing.

By default, `eager_global_ordinals` are disabled, ensuring that the cluster is optimized for indexing speed.

Global ordinals are stored in the field data cache and consume heap memory. Fields with high cardinality can consume a large amount of heap memory. To prevent memory-related issues, it is important to carefully configure the [field data circuit breaker settings](../../../install-and-configure/configuring-opensearch/circuit-breaker/index.md#field-data-circuit-breaker-settings).

## When global ordinals are used

Global ordinals are used if a search includes any of the following:

- Bucket aggregations on `keyword`, `ip`, and `flattened` fields. This includes `terms`, `composite`, `diversified_sampler`, and `significant_terms` aggregations.
- Aggregations on `text` fields that require `fielddata` to be enabled.
- Parent/child queries using a [`join`](../../../ingest-pipelines/processors/join/index.md) field, such as [`has_child`](../../../query-dsl/joining/has-child/index.md) queries or `parent` aggregations.

## Enabling eager global ordinals on a field

The following request creates an index named `products` with `eager_global_ordinals` enabled:

```json
PUT /products
{
  "mappings": {
    "properties": {
      "size": {
        "type": "keyword",
        "eager_global_ordinals": true
      }
    }
  }
}
```

The following request indexes a document:

```json
PUT /products/_doc/1
{
  "size": "ABC123"
}
```

The following request runs a `terms` aggregation:

```json
POST /products/_search
{
  "size": 0,
  "aggs": {
    "size_agg": {
      "terms": {
        "field": "size"
      }
    }
  }
}
```
