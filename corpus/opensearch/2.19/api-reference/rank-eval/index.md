---
collection: "opensearch"
version: "2.19"
title: "Ranking evaluation"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/rank-eval.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/rank-eval.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/rank-eval/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/search-apis/rank-eval/"
canonical_route: "/api-reference/search-apis/rank-eval/"
redirect_from: ["/api-reference/search-apis/rank-eval/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 60
---
# Ranking evaluation
**Introduced 1.0**
{: .label .label-purple }

The [rank](../../field-types/supported-field-types/rank/index.md) eval endpoint allows you to evaluate the quality of ranked search results.

## Endpoints

```json
GET <index_name>/_rank_eval
POST <index_name>/_rank_eval
```

## Query parameters

Query parameters are optional.

Parameter | Data type | Description
:--- | :---  | :---
ignore_unavailable | Boolean | Defaults to `false`. When set to `false` the response body will return an error if an index is closed or missing.
allow_no_indices | Boolean | Defaults to `true`. When set to `false` the response body will return an error if a wildcard expression points to indexes that are closed or missing.
expand_wildcards | String | Expand wildcard expressions for indexes that are `open`, `closed`, `hidden`, `none`, or `all`.
search_type | String | Set search type to either `query_then_fetch` or `dfs_query_then_fetch`.

## Request body fields

The request body must contain at least one parameter.

Field Type | Description
:--- | :---
id | Document or template ID.
requests | Set multiple search requests within the request field section.
ratings | Document relevance score.
k | The number of documents returned per query. Default is set to 10.
relevant_rating_threshold | The threshold at which documents are considered relevant. Default is set to 1.
normalize | Discounted cumulative gain will be calculated when set to `true`.
maximum_relevance | Sets the maximum relevance score when using the expected reciprocal rank metric.
ignore_unlabeled | Defaults to `false`. Unlabeled documents are ignored when set to `true`.
template_id | Template ID.
params | Parameters used in the template.

## Example request

````json
GET shakespeare/_rank_eval
{
  "requests": [
    {
      "id": "books_query",
      "request": {
          "query": { "match": { "text": "thou" } }
      },
      "ratings": [
        { "_index": "shakespeare", "_id": "80", "rating": 0 },
        { "_index": "shakespeare", "_id": "115", "rating": 1 },
        { "_index": "shakespeare", "_id": "117", "rating": 2 }
      ]
    },
    {
      "id": "words_query",
      "request": {
        "query": { "match": { "text": "art" } }
      },
      "ratings": [
        { "_index": "shakespeare", "_id": "115", "rating": 2 }
      ]
    }
  ]
}
````

## Example response

````json
{
  "rank_eval": {
    "metric_score": 0.7,
      "details": {
      "query_1": {
        "metric_score": 0.9,
        "unrated_docs": [
          {
            "_index": "shakespeare",
            "_id": "1234567"
          }, ...
        ],
        "hits": [
          {
            "hit": {
              "_index": "shakespeare",
              "_type": "page",
              "_id": "1234567",
              "_score": 5.123456789
            },
            "rating": 1
          }, ...
        ],
        "metric_details": {
          "precision": {
            "relevant_docs_retrieved": 3,
            "docs_retrieved": 6
          }
        }
      },
      "query_2": { [... ] }
    },
    "failures": { [... ] }
  }
}
````
