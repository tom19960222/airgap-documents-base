---
collection: "opensearch"
version: "2.19"
title: "Global"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_aggregations/bucket/global.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_aggregations/bucket/global.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/aggregations/bucket/global/"
canonical_url: "https://docs.opensearch.org/latest/aggregations/bucket/global/"
canonical_route: "/aggregations/bucket/global/"
redirect_from: ["/query-dsl/aggregations/bucket/global/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 90
parent: "Bucket aggregations"
---
# Global aggregations

The `global` aggregations lets you break out of the aggregation context of a filter aggregation. Even if you have included a filter query that narrows down a set of documents, the `global` aggregation aggregates on all documents as if the filter query wasn't there. It ignores the `filter` aggregation and implicitly assumes the `match_all` query.

The following example returns the `avg` value of the `taxful_total_price` field from all documents in the index:

```json
GET opensearch_dashboards_sample_data_ecommerce/_search
{
  "size": 0,
  "query": {
    "range": {
      "taxful_total_price": {
        "lte": 50
      }
    }
  },
  "aggs": {
    "total_avg_amount": {
      "global": {},
      "aggs": {
        "avg_price": {
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
  "total_avg_amount" : {
    "doc_count" : 4675,
    "avg_price" : {
      "value" : 75.05542864304813
    }
  }
 }
}
```

You can see that the average value for the `taxful_total_price` field is 75.05 and not the 38.36 as seen in the `filter` example when the query matched.
