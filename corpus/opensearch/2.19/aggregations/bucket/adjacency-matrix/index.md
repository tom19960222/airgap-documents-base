---
collection: "opensearch"
version: "2.19"
title: "Adjacency matrix"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_aggregations/bucket/adjacency-matrix.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_aggregations/bucket/adjacency-matrix.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/aggregations/bucket/adjacency-matrix/"
canonical_url: "https://docs.opensearch.org/latest/aggregations/bucket/adjacency-matrix/"
canonical_route: "/aggregations/bucket/adjacency-matrix/"
redirect_from: ["/query-dsl/aggregations/bucket/adjacency-matrix/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 10
parent: "Bucket aggregations"
---
# Adjacency matrix aggregations

The `adjacency_matrix` aggregation lets you define filter expressions and returns a matrix of the intersecting filters where each non-empty cell in the matrix represents a bucket. You can find how many documents fall within any combination of filters.

Use the `adjacency_matrix` aggregation to discover how concepts are related by visualizing the data as graphs.

For example, in the sample eCommerce dataset, to analyze how the different manufacturing companies are related:

```json
GET opensearch_dashboards_sample_data_ecommerce/_search
{
  "size": 0,
  "aggs": {
    "interactions": {
      "adjacency_matrix": {
        "filters": {
          "grpA": {
            "match": {
              "manufacturer.keyword": "Low Tide Media"
            }
          },
          "grpB": {
            "match": {
              "manufacturer.keyword": "Elitelligence"
            }
          },
          "grpC": {
            "match": {
              "manufacturer.keyword": "Oceanavigations"
            }
          }
        }
      }
    }
  }
}
```

#### Example response

 ```json
 {
   ...
   "aggregations" : {
     "interactions" : {
       "buckets" : [
         {
           "key" : "grpA",
           "doc_count" : 1553
         },
         {
           "key" : "grpA&grpB",
           "doc_count" : 590
         },
         {
           "key" : "grpA&grpC",
           "doc_count" : 329
         },
         {
           "key" : "grpB",
           "doc_count" : 1370
         },
         {
           "key" : "grpB&grpC",
           "doc_count" : 299
         },
         {
           "key" : "grpC",
           "doc_count" : 1218
         }
       ]
     }
   }
 }
```

 Let’s take a closer look at the result:

 ```json
 {
    "key" : "grpA&grpB",
    "doc_count" : 590
 }
 ```

- `grpA`: Products manufactured by Low Tide Media.
- `grpB`: Products manufactured by Elitelligence.
- `590`: Number of products that are manufactured by both.

You can use OpenSearch Dashboards to represent this data with a network graph.
