---
collection: "opensearch"
version: "2.19"
title: "N-gram"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/token-filters/ngram.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/token-filters/ngram.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/token-filters/ngram/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/token-filters/ngram/"
canonical_route: "/analyzers/token-filters/ngram/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 290
parent: "Token filters"
---
# N-gram token filter

The `ngram` token filter is a powerful tool used to break down text into smaller components, known as _n-grams_, which can improve partial matching and fuzzy search capabilities. It works by splitting a token into smaller substrings of defined lengths. These filters are commonly used in search applications to support autocomplete, partial matches, and typo-tolerant search. For more information, see [Autocomplete functionality](../../../search-plugins/searching-data/autocomplete/index.md) and [Did-you-mean](../../../search-plugins/searching-data/did-you-mean/index.md).

## Parameters

The `ngram` token filter can be configured with the following parameters.

Parameter | Required/Optional | Data type | Description
:--- | :--- | :--- | :---
`min_gram` | Optional | Integer | The minimum length of the n-grams. Default is `1`.
`max_gram` | Optional | Integer | The maximum length of the n-grams. Default is `2`.
`preserve_original` | Optional | Boolean | Whether to keep the original token as one of the outputs. Default is `false`.

## Example

The following example request creates a new index named `ngram_example_index` and configures an analyzer with an `ngram` filter:

```json
PUT /ngram_example_index
{
  "settings": {
    "analysis": {
      "filter": {
        "ngram_filter": {
          "type": "ngram",
          "min_gram": 2,
          "max_gram": 3
        }
      },
      "analyzer": {
        "ngram_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "ngram_filter"
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
POST /ngram_example_index/_analyze
{
  "analyzer": "ngram_analyzer",
  "text": "Search"
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "se",
      "start_offset": 0,
      "end_offset": 6,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "sea",
      "start_offset": 0,
      "end_offset": 6,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "ea",
      "start_offset": 0,
      "end_offset": 6,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "ear",
      "start_offset": 0,
      "end_offset": 6,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "ar",
      "start_offset": 0,
      "end_offset": 6,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "arc",
      "start_offset": 0,
      "end_offset": 6,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "rc",
      "start_offset": 0,
      "end_offset": 6,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "rch",
      "start_offset": 0,
      "end_offset": 6,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "ch",
      "start_offset": 0,
      "end_offset": 6,
      "type": "<ALPHANUM>",
      "position": 0
    }
  ]
}
```
