---
collection: "opensearch"
version: "2.19"
title: "Filter"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_aggregations/bucket/filter.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_aggregations/bucket/filter.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/aggregations/bucket/filter/"
canonical_url: "https://docs.opensearch.org/latest/aggregations/bucket/filter/"
canonical_route: "/aggregations/bucket/filter/"
redirect_from: ["/query-dsl/aggregations/bucket/filter/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 50
parent: "Bucket aggregations"
---
# Filter aggregations

A `filter` aggregation is a query clause, exactly like a search query — `match` or `term` or `range`. You can use the `filter` aggregation to narrow down the entire set of documents to a specific set before creating buckets.

The following example shows the `avg` aggregation running within the context of a filter. The `avg` aggregation only aggregates the documents that match the `range` query:

```json
GET opensearch_dashboards_sample_data_ecommerce/_search
{
  "size": 0,
  "aggs": {
    "low_value": {
      "filter": {
        "range": {
          "taxful_total_price": {
            "lte": 50
          }
        }
      },
      "aggs": {
        "avg_amount": {
          "avg": {
            "field": "taxful_total_price"
          }
        }
      }
    }
  }
}
```

#### Example response

```json
...
"aggregations" : {
  "low_value" : {
    "doc_count" : 1633,
    "avg_amount" : {
      "value" : 38.363175998928355
    }
  }
 }
}
```
