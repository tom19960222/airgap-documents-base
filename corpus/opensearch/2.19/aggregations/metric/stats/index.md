---
collection: "opensearch"
version: "2.19"
title: "Stats"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_aggregations/metric/stats.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_aggregations/metric/stats.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/aggregations/metric/stats/"
canonical_url: "https://docs.opensearch.org/latest/aggregations/metric/stats/"
canonical_route: "/aggregations/metric/stats/"
redirect_from: ["/query-dsl/aggregations/metric/stats/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 110
parent: "Metric aggregations"
---
# Stats aggregations

The `stats` metric is a multi-value metric aggregation that returns all basic metrics such as `min`, `max`, `sum`, `avg`, and `value_count` in one aggregation query.

The following example returns the basic stats for the `taxful_total_price` field:

```json
GET opensearch_dashboards_sample_data_ecommerce/_search
{
  "size": 0,
  "aggs": {
    "stats_taxful_total_price": {
      "stats": {
        "field": "taxful_total_price"
      }
    }
  }
}
```

#### Example response

```json
...
"aggregations" : {
  "stats_taxful_total_price" : {
    "count" : 4675,
    "min" : 6.98828125,
    "max" : 2250.0,
    "avg" : 75.05542864304813,
    "sum" : 350884.12890625
  }
 }
}
```
