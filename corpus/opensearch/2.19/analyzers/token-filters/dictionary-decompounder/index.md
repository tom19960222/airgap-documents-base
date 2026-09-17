---
collection: "opensearch"
version: "2.19"
title: "Dictionary decompounder"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/token-filters/dictionary-decompounder.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/token-filters/dictionary-decompounder.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/token-filters/dictionary-decompounder/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/token-filters/dictionary-decompounder/"
canonical_route: "/analyzers/token-filters/dictionary-decompounder/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 110
parent: "Token filters"
---
# Dictionary decompounder token filter

The `dictionary_decompounder` token filter is used to split compound words into their constituent parts based on a predefined dictionary. This filter is particularly useful for languages like German, Dutch, or Finnish, in which compound words are common, so breaking them down can improve search relevance. The `dictionary_decompounder` token filter determines whether each token (word) can be split into smaller tokens based on a list of known words. If the token can be split into known words, the filter generates the subtokens for the token.

## Parameters

The `dictionary_decompounder` token filter has the following parameters.

Parameter | Required/Optional | Data type | Description
:--- | :--- | :--- | :---
`word_list` | Required unless `word_list_path` is configured | Array of strings | The dictionary of words that the filter uses to split compound words.
`word_list_path` | Required unless `word_list` is configured | String | A file path to a text file containing the dictionary words. Accepts either an absolute path or a path relative to the `config` directory. The dictionary file must be UTF-8 encoded, and each word must be listed on a separate line.
`min_word_size` | Optional | Integer | The minimum length of the entire compound word that will be considered for splitting. If a compound word is shorter than this value, it is not split. Default is `5`.
`min_subword_size` | Optional | Integer | The minimum length for any subword. If a subword is shorter than this value, it is not included in the output. Default is `2`.
`max_subword_size` | Optional | Integer | The maximum length for any subword. If a subword is longer than this value, it is not included in the output. Default is `15`.
`only_longest_match` | Optional | Boolean | If set to `true`, only the longest matching subword will be returned. Default is `false`.

## Example

The following example request creates a new index named `decompound_example` and configures an analyzer with the `dictionary_decompounder` filter:

```json
PUT /decompound_example
{
  "settings": {
    "analysis": {
      "filter": {
        "my_dictionary_decompounder": {
          "type": "dictionary_decompounder",
          "word_list": ["slow", "green", "turtle"]
        }
      },
      "analyzer": {
        "my_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": ["lowercase", "my_dictionary_decompounder"]
        }
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /decompound_example/_analyze
{
  "analyzer": "my_analyzer",
  "text": "slowgreenturtleswim"
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "slowgreenturtleswim",
      "start_offset": 0,
      "end_offset": 19,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "slow",
      "start_offset": 0,
      "end_offset": 19,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "green",
      "start_offset": 0,
      "end_offset": 19,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "turtle",
      "start_offset": 0,
      "end_offset": 19,
      "type": "<ALPHANUM>",
      "position": 0
    }
  ]
}
```
