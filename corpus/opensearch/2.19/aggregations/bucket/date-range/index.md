---
collection: "opensearch"
version: "2.19"
title: "Date range"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_aggregations/bucket/date-range.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_aggregations/bucket/date-range.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/aggregations/bucket/date-range/"
canonical_url: "https://docs.opensearch.org/latest/aggregations/bucket/date-range/"
canonical_route: "/aggregations/bucket/date-range/"
redirect_from: ["/query-dsl/aggregations/bucket/date-range/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 30
parent: "Bucket aggregations"
---
# Date range aggregations

The `date_range` aggregation is conceptually the same as the `range` aggregation, except that it lets you perform date math.
For example, you can get all documents from the last 10 days. To make the date more readable, include the format with a `format` parameter:

```json
GET opensearch_dashboards_sample_data_logs/_search
{
  "size": 0,
  "aggs": {
    "number_of_bytes": {
      "date_range": {
        "field": "@timestamp",
        "format": "MM-yyyy",
        "ranges": [
          {
            "from": "now-10d/d",
            "to": "now"
          }
        ]
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
        "key" : "03-2021-03-2021",
        "from" : 1.6145568E12,
        "from_as_string" : "03-2021",
        "to" : 1.615451329043E12,
        "to_as_string" : "03-2021",
        "doc_count" : 0
      }
    ]
  }
 }
}
```
