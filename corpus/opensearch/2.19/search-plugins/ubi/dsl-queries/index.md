---
collection: "opensearch"
version: "2.19"
title: "Example UBI query DSL queries"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/ubi/dsl-queries.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/ubi/dsl-queries.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/ubi/dsl-queries/"
canonical_url: "https://docs.opensearch.org/latest/search-plugins/ubi/dsl-queries/"
canonical_route: "/search-plugins/ubi/dsl-queries/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
layout: "default"
nav_order: 15
parent: "User Behavior Insights"
---
# Example UBI query DSL queries

You can use the OpenSearch search query language, [query DSL](../../../query-dsl/index.md), to write User Behavior Insights (UBI) queries. The following example returns the number of times that each `action_name` event occurs.
For more extensive analytic queries, see [Example UBI SQL queries](../sql-queries/index.md).
#### Example request
```json
GET ubi_events/_search
{
  "size":0,
  "aggs":{
    "event_types":{
      "terms": {
        "field":"action_name",
        "size":10
      }
    }
  }
}
```

#### Example response

```json
{
  "took": 1,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 10000,
      "relation": "gte"
    },
    "max_score": null,
    "hits": []
  },
  "aggregations": {
    "event_types": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 0,
      "buckets": [
        {
          "key": "brand_filter",
          "doc_count": 3084
        },
        {
          "key": "product_hover",
          "doc_count": 3068
        },
        {
          "key": "button_click",
          "doc_count": 3054
        },
        {
          "key": "product_sort",
          "doc_count": 3012
        },
        {
          "key": "on_search",
          "doc_count": 3010
        },
        {
          "key": "type_filter",
          "doc_count": 2925
        },
        {
          "key": "login",
          "doc_count": 2433
        },
        {
          "key": "logout",
          "doc_count": 1447
        },
        {
          "key": "new_user_entry",
          "doc_count": 207
        }
      ]
    }
  }
}
```

You can run the preceding queries in the OpenSearch Dashboards [Query Workbench](https://docs.opensearch.org/latest/search-plugins/sql/workbench/) <!-- unresolved-cross-corpus-link: collection=opensearch-dashboards route=/search-plugins/sql/workbench/ -->.

A demo workbench with sample data can be found here:
[http://chorus-opensearch-edition.dev.o19s.com:5601/app/OpenSearch-query-workbench](http://chorus-OpenSearch-edition.dev.o19s.com:5601/app/OpenSearch-query-workbench).
