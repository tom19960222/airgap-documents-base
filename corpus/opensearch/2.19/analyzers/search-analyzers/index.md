---
collection: "opensearch"
version: "2.19"
title: "Search analyzers"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/search-analyzers.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/search-analyzers.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/search-analyzers/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/search-analyzers/"
canonical_route: "/analyzers/search-analyzers/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 30
parent: "Analyzers"
---
# Search analyzers

Search analyzers are specified at query time and are used to analyze the query string when you run a full-text query on a [text](../../field-types/supported-field-types/text/index.md) field.

## Determining which search analyzer to use

To determine which analyzer to use for a query string at query time, OpenSearch examines the following parameters in order:

1. The `analyzer` parameter of the query
1. The `search_analyzer` mapping parameter of the field
1. The `analysis.analyzer.default_search` index setting
1. The `analyzer` mapping parameter of the field
1. The `standard` analyzer (default)

In most cases, specifying a search analyzer that is different from the index analyzer is not necessary and could negatively impact search result relevance or lead to unexpected search results.
{: .warning}

## Specifying a search analyzer at query time

You can override the default analyzer behavior by explicitly setting the analyzer in the query. The following query uses the `english` analyzer to stem the input terms:

```json
GET /shakespeare/_search
{
  "query": {
    "match": {
      "text_entry": {
        "query": "speak the truth",
        "analyzer": "english"
      }
    }
  }
}
```

## Specifying a search analyzer in the mappings

When defining mappings, you can provide both the `analyzer` (used at index time) and `search_analyzer` (used at query time) for any [`text`](../../field-types/supported-field-types/text/index.md) field.

### Example: Different analyzers for indexing and search

The following configuration allows different tokenization strategies for indexing and querying:

```json
PUT /testindex
{
  "mappings": {
    "properties": {
      "text_entry": {
        "type": "text",
        "analyzer": "simple",
        "search_analyzer": "whitespace"
      }
    }
  }
}
```

### Example: Using the edge n-gram analyzer for indexing and the standard analyzer for search

The following configuration enables [autocomplete](../../search-plugins/searching-data/autocomplete/index.md)-like behavior, where you can type the beginning of a word and still receive relevant matches:

```json
PUT /articles
{
  "settings": {
    "analysis": {
      "analyzer": {
        "edge_ngram_analyzer": {
          "tokenizer": "edge_ngram_tokenizer",
          "filter": ["lowercase"]
        }
      },
      "tokenizer": {
        "edge_ngram_tokenizer": {
          "type": "edge_ngram",
          "min_gram": 2,
          "max_gram": 10,
          "token_chars": ["letter", "digit"]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "edge_ngram_analyzer",
        "search_analyzer": "standard"
      }
    }
  }
}
```

The `edge_ngram_analyzer` is applied at index time, breaking input strings into partial prefixes (n-grams), which allows the index to store fragments like "se", "sea", "sear", and so on.
Use the following request to index a document:

```json
PUT /articles/_doc/1
{
  "title": "Search Analyzer in Action"
}
```

Use the following request to search for the partial word `sear` in the `title` field:

```json
POST /articles/_search
{
  "query": {
    "match": {
      "title": "sear"
    }
  }
}
```

The response demonstrates that the query containing "sear" matches the document "Search Analyzer in Action" because the n-gram tokens generated at index time include that prefix. This mirrors the [autocomplete functionality](../../search-plugins/searching-data/autocomplete/index.md), in which typing a prefix can retrieve full matches:

```json
{
  ...
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 0.2876821,
    "hits": [
      {
        "_index": "articles",
        "_id": "1",
        "_score": 0.2876821,
        "_source": {
          "title": "Search Analyzer in Action"
        }
      }
    ]
  }
}
```

## Setting a default search analyzer for an index

Specify `analysis.analyzer.default_search` to define a search analyzer for all fields unless overridden:

```json
PUT /testindex
{
  "settings": {
    "analysis": {
      "analyzer": {
        "default": {
          "type": "simple"
        },
        "default_search": {
          "type": "whitespace"
        }
      }
    }
  }
}
```

This configuration ensures consistent behavior across multiple fields, especially when using custom analyzers.

For more information about supported analyzers, see [Analyzers](../supported-analyzers/index.md).
