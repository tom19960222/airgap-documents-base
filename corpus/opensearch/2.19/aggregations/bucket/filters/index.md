---
collection: "opensearch"
version: "2.19"
title: "Filters"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_aggregations/bucket/filters.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_aggregations/bucket/filters.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/aggregations/bucket/filters/"
canonical_url: "https://docs.opensearch.org/latest/aggregations/bucket/filters/"
canonical_route: "/aggregations/bucket/filters/"
redirect_from: ["/query-dsl/aggregations/bucket/filters/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 60
parent: "Bucket aggregations"
---
# Filters aggregations

A `filters` aggregation is the same as the `filter` aggregation, except that it lets you use multiple filter aggregations.
While the `filter` aggregation results in a single bucket, the `filters` aggregation returns multiple buckets, one for each of the defined filters.

To create a bucket for all the documents that didn't match the any of the filter queries, set the `other_bucket` property to `true`:

```json
GET opensearch_dashboards_sample_data_logs/_search
{
  "size": 0,
  "aggs": {
    "200_os": {
      "filters": {
        "other_bucket": true,
        "filters": [
          {
            "term": {
              "response.keyword": "200"
            }
          },
          {
            "term": {
              "machine.os.keyword": "osx"
            }
          }
        ]
      },
      "aggs": {
        "avg_amount": {
          "avg": {
            "field": "bytes"
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
  "200_os" : {
    "buckets" : [
      {
        "doc_count" : 12832,
        "avg_amount" : {
          "value" : 5897.852711970075
        }
      },
      {
        "doc_count" : 2825,
        "avg_amount" : {
          "value" : 5620.347256637168
        }
      },
      {
        "doc_count" : 1017,
        "avg_amount" : {
          "value" : 3247.0963618485744
        }
      }
    ]
  }
 }
}
```
