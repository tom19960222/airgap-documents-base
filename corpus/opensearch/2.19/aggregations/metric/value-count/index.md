---
collection: "opensearch"
version: "2.19"
title: "Value count"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_aggregations/metric/value-count.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_aggregations/metric/value-count.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/aggregations/metric/value-count/"
canonical_url: "https://docs.opensearch.org/latest/aggregations/metric/value-count/"
canonical_route: "/aggregations/metric/value-count/"
redirect_from: ["/query-dsl/aggregations/metric/value-count/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 140
parent: "Metric aggregations"
---
# Value count aggregations

The `value_count` metric is a single-value metric aggregation that calculates the number of values that an aggregation is based on.

For example, you can use the `value_count` metric with the `avg` metric to find how many numbers the aggregation uses to calculate an average value.

```json
GET opensearch_dashboards_sample_data_ecommerce/_search
{
  "size": 0,
   "aggs": {
    "number_of_values": {
      "value_count": {
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
    "number_of_values" : {
      "value" : 4675
    }
  }
}
```
