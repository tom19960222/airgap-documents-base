---
collection: "opensearch"
version: "2.19"
title: "Bucket aggregations"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_aggregations/bucket/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_aggregations/bucket/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/aggregations/bucket/"
canonical_url: "https://docs.opensearch.org/latest/aggregations/bucket/index/"
canonical_route: "/aggregations/bucket/"
redirect_from: ["/opensearch/bucket-agg/","/query-dsl/aggregations/bucket-agg/","/query-dsl/aggregations/bucket/","/aggregations/bucket-agg/","/aggregations/bucket/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 3
---
# Bucket aggregations

Bucket aggregations categorize sets of documents as buckets. The type of bucket aggregation determines the bucket for a given document.

You can use bucket aggregations to implement faceted navigation (usually placed as a sidebar on a search result landing page) to help your users filter the results.

## Supported bucket aggregations

OpenSearch supports the following bucket aggregations:

- [Adjacency matrix](adjacency-matrix/index.md)
- [Children](children/index.md)
- [Date histogram](date-histogram/index.md)
- [Date range](date-range/index.md)
- [Diversified sampler](diversified-sampler/index.md)
- [Filter](filter/index.md)
- [Filters](filters/index.md)
- [Geodistance](geo-distance/index.md)
- [Geohash grid](geohash-grid/index.md)
- [Geohex grid](geohex-grid/index.md)
- [Geotile grid](geotile-grid/index.md)
- [Global](global/index.md)
- [Histogram](histogram/index.md)
- [IP range](ip-range/index.md)
- [Missing](missing/index.md)
- [Multi-terms](multi-terms/index.md)
- [Nested](nested/index.md)
- [Range](range/index.md)
- [Reverse nested](reverse-nested/index.md)
- [Sampler](sampler/index.md)
- [Significant terms](significant-terms/index.md)
- [Significant text](significant-text/index.md)
- [Terms](terms/index.md)
