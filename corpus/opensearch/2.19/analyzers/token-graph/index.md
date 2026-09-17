---
collection: "opensearch"
version: "2.19"
title: "Token graphs"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/token-graph.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/token-graph.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/token-graph/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/token-graph/"
canonical_route: "/analyzers/token-graph/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 150
---
# Token graphs

Token graphs show how tokens relate to each other during text analysis, particularly when handling multi-word synonyms or compound words. They help ensure accurate query matching and phrase expansion.

Each token is assigned the following metadata:

- `position` – The location of the token in the text

- `positionLength` – How many positions the token spans (used in multi-word expressions)

Token graphs use this information to build a graph structure of token relationships, which is later used during query parsing. Graph-aware token filters, such as [`synonym_graph`](../token-filters/synonym-graph/index.md) and [`word_delimiter_graph`](../token-filters/word-delimiter-graph/index.md), enable you to match phrases more accurately.

The following diagram depicts the relationship between `position` and `positionLength` when using [`synonym_graph`](../token-filters/synonym-graph/index.md). The "NYC" token is assigned a `position` of `0` and a `positionLength` of `3`.

<img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/nyc-token-graph.png" alt="token graph" width="700">

## Using token graphs during indexing and querying

At index time, `positionLength` is ignored and token graphs are not used.

During query execution, various query types can leverage token graphs, with the following being the most frequently used:

- [`match`](../../query-dsl/full-text/match/index.md)
- [`match_phrase`](../../query-dsl/full-text/match-phrase/index.md)

## Example: Synonym compared to synonym graph

To better understand the difference between graph-aware token filters and standard token filters, you can use the following steps to compare the [`synonym`](../token-filters/synonym/index.md) token filter with the [`synonym_graph`](../token-filters/synonym-graph/index.md) token filter:

1. Create an index with a [`synonym`](../token-filters/synonym/index.md) token filter (not graph aware):

    ```json
    PUT /synonym_index
    {
      "settings": {
        "analysis": {
          "filter": {
            "my_synonyms": {
              "type": "synonym",
              "synonyms": ["ssd => solid state drive"]
            }
          },
          "analyzer": {
            "my_analyzer": {
              "tokenizer": "standard",
              "filter": ["lowercase", "my_synonyms"]
            }
          }
        }
      },
      "mappings": {
        "properties": {
          "content": {
            "type": "text",
            "analyzer": "my_analyzer"
          }
        }
      }
    }
    ```

2. Create an index with a [`synonym_graph`](../token-filters/synonym-graph/index.md) token filter (graph aware):

    ```json
    PUT /synonym_graph_index
    {
      "settings": {
        "analysis": {
          "filter": {
            "my_synonyms": {
              "type": "synonym_graph",
              "synonyms": ["ssd => solid state drive"]
            }
          },
          "analyzer": {
            "my_analyzer": {
              "tokenizer": "standard",
              "filter": ["lowercase", "my_synonyms"]
            }
          }
        }
      },
      "mappings": {
        "properties": {
          "content": {
            "type": "text",
            "analyzer": "my_analyzer"
          }
        }
      }
    }
    ```

3. Create the same document in each index:

    ```json
    PUT /synonym_index/_doc/1
    { "content": "ssd is critical" }
    ```

    ```json
    PUT /synonym_graph_index/_doc/1
    { "content": "ssd is critical" }
    ```

4. Search the non-graph-aware index:

    ```json
    POST /synonym_index/_search
    {
      "query": {
        "match_phrase": {
          "content": "solid state drive is critical"
        }
      }
    }
    ```

    The response contains no hits:

    ```json
    {
      "took": 13,
      "timed_out": false,
      "_shards": {
        "total": 1,
        "successful": 1,
        "skipped": 0,
        "failed": 0
      },
      "hits": {
        "total": {
          "value": 0,
          "relation": "eq"
        },
        "max_score": null,
        "hits": []
      }
    }
    ```

5. Search the graph-aware index:

    ```json
    POST /synonym_graph_index/_search
    {
      "query": {
        "match_phrase": {
          "content": "solid state drive is critical"
        }
      }
    }
    ```

    The response contains one hit:

    ```json
    {
      "took": 9,
      "timed_out": false,
      "_shards": {
        "total": 1,
        "successful": 1,
        "skipped": 0,
        "failed": 0
      },
      "hits": {
        "total": {
          "value": 1,
          "relation": "eq"
        },
        "max_score": 1.4384103,
        "hits": [
          {
            "_index": "synonym_graph_index",
            "_id": "1",
            "_score": 1.4384103,
            "_source": {
              "content": "ssd is critical"
            }
          }
        ]
      }
    }
    ```

A hit occurs when using the graph-aware token filter because during the [`match_phrase`](../../query-dsl/full-text/match-phrase/index.md) query, an additional subquery is generated using the token graph. The following diagram illustrates the token graph created by the graph-aware token filter.

<img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/ssd-token-graph.png" alt="token graph" width="700">
