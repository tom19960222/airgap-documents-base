---
collection: "opensearch"
version: "2.19"
title: "Sum"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_aggregations/metric/sum.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_aggregations/metric/sum.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/aggregations/metric/sum/"
canonical_url: "https://docs.opensearch.org/latest/aggregations/metric/sum/"
canonical_route: "/aggregations/metric/sum/"
redirect_from: ["/query-dsl/aggregations/metric/sum/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 120
parent: "Metric aggregations"
---
# Sum aggregations

The `sum` metric is a single-value metric aggregations that returns the sum of the values of a field.

The following example calculates the total sum of the `taxful_total_price` field:

```json
GET opensearch_dashboards_sample_data_ecommerce/_search
{
  "size": 0,
  "aggs": {
    "sum_taxful_total_price": {
      "sum": {
        "field": "taxful_total_price"
      }
    }
  }
}
```

#### Example response

```json
{
  "took": 16,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 4675,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  },
  "aggregations": {
    "sum_taxful_total_price": {
      "value": 350884.12890625
    }
  }
}
```
