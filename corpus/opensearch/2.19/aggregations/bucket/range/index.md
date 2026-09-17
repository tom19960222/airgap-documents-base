---
collection: "opensearch"
version: "2.19"
title: "Range"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_aggregations/bucket/range.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_aggregations/bucket/range.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/aggregations/bucket/range/"
canonical_url: "https://docs.opensearch.org/latest/aggregations/bucket/range/"
canonical_route: "/aggregations/bucket/range/"
redirect_from: ["/query-dsl/aggregations/bucket/range/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 150
parent: "Bucket aggregations"
---
# Range aggregations

The `range` aggregation lets you define the range for each bucket.

For example, you can find the number of bytes between 1000 and 2000, 2000 and 3000, and 3000 and 4000.
Within the `range` parameter, you can define ranges as objects of an array.

```json
GET opensearch_dashboards_sample_data_logs/_search
{
  "size": 0,
  "aggs": {
    "number_of_bytes_distribution": {
      "range": {
        "field": "bytes",
        "ranges": [
          {
            "from": 1000,
            "to": 2000
          },
          {
            "from": 2000,
            "to": 3000
          },
          {
            "from": 3000,
            "to": 4000
          }
        ]
      }
    }
  }
}
```

The response includes the `from` key values and excludes the `to` key values:

#### Example response

```json
...
"aggregations" : {
  "number_of_bytes_distribution" : {
    "buckets" : [
      {
        "key" : "1000.0-2000.0",
        "from" : 1000.0,
        "to" : 2000.0,
        "doc_count" : 805
      },
      {
        "key" : "2000.0-3000.0",
        "from" : 2000.0,
        "to" : 3000.0,
        "doc_count" : 1369
      },
      {
        "key" : "3000.0-4000.0",
        "from" : 3000.0,
        "to" : 4000.0,
        "doc_count" : 1422
      }
    ]
  }
 }
}
```
