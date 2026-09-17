---
collection: "opensearch"
version: "2.19"
title: "Filter results"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/filter-search.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/filter-search.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/filter-search/"
canonical_url: "https://docs.opensearch.org/latest/search-plugins/filter-search/"
canonical_route: "/search-plugins/filter-search/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 36
parent: "Search options"
---
# Filter search results

You can filter searches using different methods, each suited to specific scenarios. You can apply filters at the query level, using `boolean` query clauses and `post_filter` and `aggregation` level filters, as follows:

- **Query-level filtering:** Apply `boolean` query filter clauses to filter search hits and aggregations, such as to narrow results to specific categories or brands.
- **Post-filter filtering:** Use `post_filter` to refine search hits based on user selections while preserving all aggregation options.
- **Aggregation-level filtering:** Adjust specific aggregations based on selected filters without impacting other aggregations.

## Query-level filtering with Boolean queries

Use a `boolean` query with a filter clause to apply filters to both search hits and aggregations. For example, if a shopper searches for `smartphones` from `BrandA`, a Boolean query can restrict results to only those smartphones from `BrandA`. The following steps guide you through query-level filtering.

1. Create an index `electronics` and provide the mapping using the following request:

```json
PUT /electronics
{
  "mappings": {
    "properties": {
      "brand": { "type": "keyword" },
      "category": { "type": "keyword" },
      "price": { "type": "float" },
      "features": { "type": "keyword" }
    }
  }
}
```

2. Add documents to the `electronics` index using the following request:

```json
PUT /electronics/_doc/1?refresh
{
  "brand": "BrandA",
  "category": "Smartphone",
  "price": 699.99,
  "features": ["5G", "Dual Camera"]
}
PUT /electronics/_doc/2?refresh
{
  "brand": "BrandA",
  "category": "Laptop",
  "price": 1199.99,
  "features": ["Touchscreen", "16GB RAM"]
}
PUT /electronics/_doc/3?refresh
{
  "brand": "BrandB",
  "category": "Smartphone",
  "price": 799.99,
  "features": ["5G", "Triple Camera"]
}
```

3. Apply a `boolean` filter query to display only `smartphones` from `BrandA` using the following request:

```json
GET /electronics/_search
{
  "query": {
    "bool": {
      "filter": [
        { "term": { "brand": "BrandA" }},
        { "term": { "category": "Smartphone" }}
      ]
    }
  }
}
```

## Narrowing results using `post-filter` while preserving aggregation visibility

Use `post_filter` to limit search hits while preserving all aggregation options. For example, if a shopper selects `BrandA`, results are filtered to show only `BrandA` products while maintaining the visibility of all brand options in the aggregations, as shown in the following example request:

```json
GET /electronics/_search
{
  "query": {
    "bool": {
      "filter": { "term": { "category": "Smartphone" }}
    }
  },
  "aggs": {
    "brands": {
      "terms": { "field": "brand" }
    }
  },
  "post_filter": {
    "term": { "brand": "BrandA" }
  }
}
```

The result should show `BrandA` smartphones in the search hits and all brands in the aggregations.

## Refining aggregations with aggregation-level filtering

You can use aggregation-level filtering to apply filters to specific aggregations without affecting the main aggregation to which they belong.

For example, you can use aggregation-level filtering to filter the `price_ranges` aggregation based on selected brands, `BrandA` and `BrandB`, without affecting the main `price_ranges` aggregation, as shown in the following example request. This displays price ranges relevant to the selected brands while also displaying overall price ranges for all products.

```json
GET /electronics/_search
{
  "query": {
    "bool": {
      "filter": { "term": { "category": "Smartphone" }}
    }
  },
  "aggs": {
    "price_ranges": {
      "range": {
        "field": "price",
        "ranges": [
          { "to": 500 },
          { "from": 500, "to": 1000 },
          { "from": 1000 }
        ]
      }
    },
    "filtered_brands": {
      "filter": {
        "terms": { "brand": ["BrandA", "BrandB"] }
      },
      "aggs": {
        "price_ranges": {
          "range": {
            "field": "price",
            "ranges": [
              { "to": 500 },
              { "from": 500, "to": 1000 },
              { "from": 1000 }
            ]
          }
        }
      }
    }
  }
}
```
