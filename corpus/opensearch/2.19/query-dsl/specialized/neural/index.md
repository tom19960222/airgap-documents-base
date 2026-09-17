---
collection: "opensearch"
version: "2.19"
title: "Neural"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_query-dsl/specialized/neural.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_query-dsl/specialized/neural.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/query-dsl/specialized/neural/"
canonical_url: "https://docs.opensearch.org/latest/query-dsl/specialized/neural/"
canonical_route: "/query-dsl/specialized/neural/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 50
parent: "Specialized queries"
---
# Neural query

Use the `neural` query for vector field search by text or image in [vector search](../../../vector-search/index.md).

## Request body fields

Include the following request fields in the `neural` query:

```json
"neural": {
  "<vector_field>": {
    "query_text": "<query_text>",
    "query_image": "<image_binary>",
    "model_id": "<model_id>",
    "k": 100
  }
}
```

The top-level `vector_field` specifies the vector field against which to run a search query. The following table lists the other neural query fields.

Field | Data type | Required/Optional | Description
:--- | :--- | :---
`query_text` | String | Optional | The query text from which to generate vector embeddings. You must specify at least one `query_text` or `query_image`.
`query_image` | String | Optional | A base-64 encoded string that corresponds to the query image from which to generate vector embeddings. You must specify at least one `query_text` or `query_image`.
`model_id` | String | Required if the default model ID is not set. For more information, see [Setting a default model on an index or field](../../../vector-search/ai-search/semantic-search/index.md#setting-a-default-model-on-an-index-or-field). | The ID of the model that will be used to generate vector embeddings from the query text. The model must be deployed in OpenSearch before it can be used in neural search. For more information, see [Using custom models within OpenSearch](../../../ml-commons-plugin/using-ml-models/index.md) and [Neural search](../../../vector-search/ai-search/index.md).
`k` | Integer | Optional | The number of results returned by the k-NN search. Only one variable, either `k`, `min_score`, or `max_distance`, can be specified. If a variable is not specified, the default is `k` with a value of `10`.
`min_score` | Float | Optional | The minimum score threshold for the search results. Only one variable, either `k`, `min_score`, or `max_distance`, can be specified. For more information, see [Radial search](../../../vector-search/specialized-operations/radial-search-knn/index.md).
`max_distance` | Float | Optional | The maximum distance threshold for the search results. Only one variable, either `k`, `min_score`, or `max_distance`, can be specified. For more information, see [Radial search](../../../vector-search/specialized-operations/radial-search-knn/index.md).
`filter` | Object | Optional | A query that can be used to reduce the number of documents considered. For more information about filter usage, see [Vector search with filters](../../../vector-search/filter-search-knn/index.md).

#### Example request

The following example shows a search with a `k` value of `100` and a filter that includes a range query and a term query:

```json
GET /my-nlp-index/_search
{
  "query": {
    "neural": {
      "passage_embedding": {
        "query_text": "Hi world",
        "query_image": "iVBORw0KGgoAAAAN...",
        "k": 100,
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
    }
  }
}
```

The following search query includes a k-NN radial search `min_score` of `0.95` and a filter that includes a range query and a term query:

```json
GET /my-nlp-index/_search
{
  "query": {
    "neural": {
      "passage_embedding": {
        "query_text": "Hi world",
        "query_image": "iVBORw0KGgoAAAAN...",
        "min_score": 0.95,
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
    }
  }
}
```

The following search query includes a k-NN radial search `max_distance` of `10` and a filter that includes a range query and a term query:

```json
GET /my-nlp-index/_search
{
  "query": {
    "neural": {
      "passage_embedding": {
        "query_text": "Hi world",
        "query_image": "iVBORw0KGgoAAAAN...",
        "max_distance": 10,
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
    }
  }
}
```
