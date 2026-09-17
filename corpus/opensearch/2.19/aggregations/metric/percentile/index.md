---
collection: "opensearch"
version: "2.19"
title: "Percentile"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_aggregations/metric/percentile.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_aggregations/metric/percentile.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/aggregations/metric/percentile/"
canonical_url: "https://docs.opensearch.org/latest/aggregations/metric/percentile/"
canonical_route: "/aggregations/metric/percentile/"
redirect_from: ["/query-dsl/aggregations/metric/percentile/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 90
parent: "Metric aggregations"
---
# Percentile aggregations

Percentile is the percentage of the data that's at or below a certain threshold value.

The `percentile` metric is a multi-value metric aggregation that lets you find outliers in your data or figure out the distribution of your data.

Like the `cardinality` metric, the `percentile` metric is also approximate.

The following example calculates the percentile in relation to the `taxful_total_price` field:

```json
GET opensearch_dashboards_sample_data_ecommerce/_search
{
  "size": 0,
  "aggs": {
    "percentile_taxful_total_price": {
      "percentiles": {
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
  "percentile_taxful_total_price" : {
    "values" : {
      "1.0" : 21.984375,
      "5.0" : 27.984375,
      "25.0" : 44.96875,
      "50.0" : 64.22061688311689,
      "75.0" : 93.0,
      "95.0" : 156.0,
      "99.0" : 222.0
    }
  }
 }
}
```

You can control the level of approximation using the optional `tdigest.compression` field. A larger value indicates that the data structure that approximates percentiles is more accurate but uses more heap space. The default value is 100.

For example, use the following request to set `compression` to `200`:

```json
GET opensearch_dashboards_sample_data_ecommerce/_search
{
  "size": 0,
  "aggs": {
    "percentile_taxful_total_price": {
      "percentiles": {
        "field": "taxful_total_price",
        "tdigest": {
          "compression": 200
        }
      }
    }
  }
}
```
