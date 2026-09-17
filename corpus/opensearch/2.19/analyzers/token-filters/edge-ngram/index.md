---
collection: "opensearch"
version: "2.19"
title: "Edge n-gram"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/token-filters/edge-ngram.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/token-filters/edge-ngram.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/token-filters/edge-ngram/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/token-filters/edge-ngram/"
canonical_route: "/analyzers/token-filters/edge-ngram/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 120
parent: "Token filters"
---
# Edge n-gram token filter
The `edge_ngram` token filter is very similar to the `ngram` token filter, where a particular string is split into substrings of different lengths. The `edge_ngram` token filter, however, generates n-grams (substrings) only from the beginning (edge) of a token. It's particularly useful in scenarios like autocomplete or prefix matching, where you want to match the beginning of words or phrases as the user types them.

## Parameters

The `edge_ngram` token filter can be configured with the following parameters.

Parameter | Required/Optional | Data type | Description
:--- | :--- | :--- | :---
`min_gram` | Optional | Integer | The minimum length of the n-grams that will be generated. Default is `1`.
`max_gram` | Optional | Integer | The maximum length of the n-grams that will be generated. Default is `1` for the `edge_ngram` filter and `2` for custom token filters. Avoid setting this parameter to a low value. If the value is set too low, only very short n-grams will be generated and the search term will not be found. For example, if `max_gram` is set to `3` and you index the word "banana", the longest generated token will be "ban". If the user searches for "banana", no matches will be returned. You can use the `truncate` token filter as a search analyzer to mitigate this risk.
`preserve_original` | Optional | Boolean | Includes the original token in the output. Default is `false` .

## Example

The following example request creates a new index named `edge_ngram_example` and configures an analyzer with the `edge_ngram` filter:

```json
PUT /edge_ngram_example
{
  "settings": {
    "analysis": {
      "filter": {
        "my_edge_ngram": {
          "type": "edge_ngram",
          "min_gram": 3,
          "max_gram": 4
        }
      },
      "analyzer": {
        "my_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": ["lowercase", "my_edge_ngram"]
        }
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /edge_ngram_example/_analyze
{
  "analyzer": "my_analyzer",
  "text": "slow green turtle"
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "slo",
      "start_offset": 0,
      "end_offset": 4,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "slow",
      "start_offset": 0,
      "end_offset": 4,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "gre",
      "start_offset": 5,
      "end_offset": 10,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "gree",
      "start_offset": 5,
      "end_offset": 10,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "tur",
      "start_offset": 11,
      "end_offset": 17,
      "type": "<ALPHANUM>",
      "position": 2
    },
    {
      "token": "turt",
      "start_offset": 11,
      "end_offset": 17,
      "type": "<ALPHANUM>",
      "position": 2
    }
  ]
}
```
