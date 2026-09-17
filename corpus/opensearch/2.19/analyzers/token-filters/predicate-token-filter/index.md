---
collection: "opensearch"
version: "2.19"
title: "Predicate token filter"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/token-filters/predicate-token-filter.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/token-filters/predicate-token-filter.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/token-filters/predicate-token-filter/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/token-filters/predicate-token-filter/"
canonical_route: "/analyzers/token-filters/predicate-token-filter/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 340
parent: "Token filters"
---
# Predicate token filter

The `predicate_token_filter` evaluates whether tokens should be kept or discarded, depending on the conditions defined in a custom script. The tokens are evaluated in the analysis predicate context. This filter supports only inline Painless scripts.

## Parameters

The `predicate_token_filter` has one required parameter: `script`. This parameter provides a condition that is used to evaluate whether the token should be kept.

## Example

The following example request creates a new index named `predicate_index` and configures an analyzer with a `predicate_token_filter`. The filter specifies to only output tokens if they are longer than 7 characters:

```json
PUT /predicate_index
{
  "settings": {
    "analysis": {
      "filter": {
        "my_predicate_filter": {
          "type": "predicate_token_filter",
          "script": {
            "source": "token.term.length() > 7"
          }
        }
      },
      "analyzer": {
        "predicate_analyzer": {
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "my_predicate_filter"
          ]
        }
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /predicate_index/_analyze
{
  "text": "The OpenSearch community is growing rapidly",
  "analyzer": "predicate_analyzer"
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "opensearch",
      "start_offset": 4,
      "end_offset": 14,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "community",
      "start_offset": 15,
      "end_offset": 24,
      "type": "<ALPHANUM>",
      "position": 2
    }
  ]
}
```
