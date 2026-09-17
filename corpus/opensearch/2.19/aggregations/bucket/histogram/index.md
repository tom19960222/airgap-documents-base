---
collection: "opensearch"
version: "2.19"
title: "Histogram"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_aggregations/bucket/histogram.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_aggregations/bucket/histogram.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/aggregations/bucket/histogram/"
canonical_url: "https://docs.opensearch.org/latest/aggregations/bucket/histogram/"
canonical_route: "/aggregations/bucket/histogram/"
redirect_from: ["/query-dsl/aggregations/bucket/histogram/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 100
parent: "Bucket aggregations"
---
# Histogram aggregations

The `histogram` aggregation buckets documents based on a specified interval.

With `histogram` aggregations, you can visualize the distributions of values in a given range of documents very easily. Now OpenSearch doesn’t give you back an actual graph of course, that’s what OpenSearch Dashboards is for. But it'll give you the JSON response that you can use to construct your own graph.

The following example buckets the `number_of_bytes` field by 10,000 intervals:

```json
GET opensearch_dashboards_sample_data_logs/_search
{
  "size": 0,
  "aggs": {
    "number_of_bytes": {
      "histogram": {
        "field": "bytes",
        "interval": 10000
      }
    }
  }
}
```

#### Example response

```json
...
"aggregations" : {
  "number_of_bytes" : {
    "buckets" : [
      {
        "key" : 0.0,
        "doc_count" : 13372
      },
      {
        "key" : 10000.0,
        "doc_count" : 702
      }
    ]
  }
 }
}
```
