---
collection: "opensearch"
version: "2.19"
title: "Metric aggregations"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_aggregations/metric/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_aggregations/metric/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/aggregations/metric/"
canonical_url: "https://docs.opensearch.org/latest/aggregations/metric/index/"
canonical_route: "/aggregations/metric/"
redirect_from: ["/opensearch/metric-agg/","/query-dsl/aggregations/metric-agg/","/aggregations/metric-agg/","/query-dsl/aggregations/metric/","/aggregations/metric/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 2
---
# Metric aggregations

Metric aggregations let you perform simple calculations such as finding the minimum, maximum, and average values of a field.

## Types of metric aggregations

There are two types of metric aggregations: single-value metric aggregations and multi-value metric aggregations.

### Single-value metric aggregations

Single-value metric aggregations return a single metric, for example, `sum`, `min`, `max`, `avg`, `cardinality`, or `value_count`.

### Multi-value metric aggregations

Multi-value metric aggregations return more than one metric. These include `stats`, `extended_stats`, `matrix_stats`, `percentile`, `percentile_ranks`, `geo_bound`, `top_hits`, and `scripted_metric`.

## Supported metric aggregations

OpenSearch supports the following metric aggregations:

- [Average](average/index.md)
- [Cardinality](cardinality/index.md)
- [Extended stats](extended-stats/index.md)
- [Geobounds](geobounds/index.md)
- [Matrix stats](matrix-stats/index.md)
- [Maximum](maximum/index.md)
- [Minimum](minimum/index.md)
- [Percentile ranks](percentile-ranks/index.md)
- [Percentile](percentile/index.md)
- [Scripted metric](scripted-metric/index.md)
- [Stats](stats/index.md)
- [Sum](sum/index.md)
- [Top hits](top-hits/index.md)
- [Value count](value-count/index.md)
