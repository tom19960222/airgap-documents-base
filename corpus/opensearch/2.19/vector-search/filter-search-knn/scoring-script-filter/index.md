---
collection: "opensearch"
version: "2.19"
title: "Scoring script filter"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_vector-search/filter-search-knn/scoring-script-filter.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_vector-search/filter-search-knn/scoring-script-filter.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/vector-search/filter-search-knn/scoring-script-filter/"
canonical_url: "https://docs.opensearch.org/latest/vector-search/filter-search-knn/scoring-script-filter/"
canonical_route: "/vector-search/filter-search-knn/scoring-script-filter/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 30
parent: "Filtering data"
---
# Scoring script filter

A scoring script filter first filters the documents and then uses a brute-force exact k-NN search on the results. For example, the following query searches for hotels with a rating between 8 and 10, inclusive, that provide parking and then performs a k-NN search to return the 3 hotels that are closest to the specified `location`:

```json
POST /hotels-index/_search
{
  "size": 3,
  "query": {
    "script_score": {
      "query": {
        "bool": {
          "filter": {
            "bool": {
              "must": [
                {
                  "range": {
                    "rating": {
                      "gte": 8,
                      "lte": 10
                    }
                  }
                },
                {
                  "term": {
                    "parking": "true"
                  }
                }
              ]
            }
          }
        }
      },
      "script": {
        "source": "knn_score",
        "lang": "knn",
        "params": {
          "field": "location",
          "query_value": [
            5.0,
            4.0
          ],
          "space_type": "l2"
        }
      }
    }
  }
}
```
