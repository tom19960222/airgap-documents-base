---
collection: "opensearch"
version: "2.19"
title: "Keyword repeat"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/token-filters/keyword-repeat.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/token-filters/keyword-repeat.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/token-filters/keyword-repeat/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/token-filters/keyword-repeat/"
canonical_route: "/analyzers/token-filters/keyword-repeat/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 210
parent: "Token filters"
---
# Keyword repeat token filter

The `keyword_repeat` token filter emits the keyword version of a token into a token stream. This filter is typically used when you want to retain both the original token and its modified version after further token transformations, such as stemming or synonym expansion. The duplicated tokens allow the original, unchanged version of the token to remain in the final analysis alongside the modified versions.

The `keyword_repeat` token filter should be placed before stemming filters. Stemming is not applied to every token, thus you may have duplicate tokens in the same position after stemming. To remove duplicate tokens, use the `remove_duplicates` token filter after the stemmer.
{: .note}

## Example

The following example request creates a new index named `my_index` and configures an analyzer with a `keyword_repeat` filter:

```json
PUT /my_index
{
  "settings": {
    "analysis": {
      "filter": {
        "my_kstem": {
          "type": "kstem"
        },
        "my_lowercase": {
          "type": "lowercase"
        }
      },
      "analyzer": {
        "my_custom_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "my_lowercase",
            "keyword_repeat",
            "my_kstem"
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
POST /my_index/_analyze
{
  "analyzer": "my_custom_analyzer",
  "text": "Stopped quickly"
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "stopped",
      "start_offset": 0,
      "end_offset": 7,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "stop",
      "start_offset": 0,
      "end_offset": 7,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "quickly",
      "start_offset": 8,
      "end_offset": 15,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "quick",
      "start_offset": 8,
      "end_offset": 15,
      "type": "<ALPHANUM>",
      "position": 1
    }
  ]
}
```

You can further examine the impact of the `keyword_repeat` token filter by adding the following parameters to the `_analyze` query:

```json
POST /my_index/_analyze
{
  "analyzer": "my_custom_analyzer",
  "text": "Stopped quickly",
  "explain": true,
  "attributes": "keyword"
}
```

The response includes detailed information, such as tokenization, filtering, and the application of specific token filters:

```json
{
  "detail": {
    "custom_analyzer": true,
    "charfilters": [],
    "tokenizer": {
      "name": "standard",
      "tokens": [
        {"token": "OpenSearch","start_offset": 0,"end_offset": 10,"type": "<ALPHANUM>","position": 0},
        {"token": "helped","start_offset": 11,"end_offset": 17,"type": "<ALPHANUM>","position": 1},
        {"token": "many","start_offset": 18,"end_offset": 22,"type": "<ALPHANUM>","position": 2},
        {"token": "employers","start_offset": 23,"end_offset": 32,"type": "<ALPHANUM>","position": 3}
      ]
    },
    "tokenfilters": [
      {
        "name": "lowercase",
        "tokens": [
          {"token": "opensearch","start_offset": 0,"end_offset": 10,"type": "<ALPHANUM>","position": 0},
          {"token": "helped","start_offset": 11,"end_offset": 17,"type": "<ALPHANUM>","position": 1},
          {"token": "many","start_offset": 18,"end_offset": 22,"type": "<ALPHANUM>","position": 2},
          {"token": "employers","start_offset": 23,"end_offset": 32,"type": "<ALPHANUM>","position": 3}
        ]
      },
      {
        "name": "keyword_marker_filter",
        "tokens": [
          {"token": "opensearch","start_offset": 0,"end_offset": 10,"type": "<ALPHANUM>","position": 0,"keyword": true},
          {"token": "helped","start_offset": 11,"end_offset": 17,"type": "<ALPHANUM>","position": 1,"keyword": false},
          {"token": "many","start_offset": 18,"end_offset": 22,"type": "<ALPHANUM>","position": 2,"keyword": false},
          {"token": "employers","start_offset": 23,"end_offset": 32,"type": "<ALPHANUM>","position": 3,"keyword": false}
        ]
      },
      {
        "name": "kstem_filter",
        "tokens": [
          {"token": "opensearch","start_offset": 0,"end_offset": 10,"type": "<ALPHANUM>","position": 0,"keyword": true},
          {"token": "help","start_offset": 11,"end_offset": 17,"type": "<ALPHANUM>","position": 1,"keyword": false},
          {"token": "many","start_offset": 18,"end_offset": 22,"type": "<ALPHANUM>","position": 2,"keyword": false},
          {"token": "employer","start_offset": 23,"end_offset": 32,"type": "<ALPHANUM>","position": 3,"keyword": false}
        ]
      }
    ]
  }
}
```
