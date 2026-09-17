---
collection: "opensearch"
version: "2.19"
title: "Simple analyzer"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/supported-analyzers/simple.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/supported-analyzers/simple.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/supported-analyzers/simple/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/supported-analyzers/simple/"
canonical_route: "/analyzers/supported-analyzers/simple/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 100
parent: "Analyzers"
---
# Simple analyzer

The `simple` analyzer is a very basic analyzer that breaks text into terms at non-letter characters and lowercases the terms. Unlike the `standard` analyzer, the `simple` analyzer treats everything except for alphabetic characters as delimiters, meaning that it does not recognize numbers, punctuation, or special characters as part of the tokens.

## Example

Use the following command to create an index named `my_simple_index` with a `simple` analyzer:

```json
PUT /my_simple_index
{
  "mappings": {
    "properties": {
      "my_field": {
        "type": "text",
        "analyzer": "simple"
      }
    }
  }
}
```

## Configuring a custom analyzer

Use the following command to configure an index with a custom analyzer that is equivalent to a `simple` analyzer with an added `html_strip` character filter:

```json
PUT /my_custom_simple_index
{
  "settings": {
    "analysis": {
      "char_filter": {
        "html_strip": {
          "type": "html_strip"
        }
      },
      "tokenizer": {
        "my_lowercase_tokenizer": {
          "type": "lowercase"
        }
      },
      "analyzer": {
        "my_custom_simple_analyzer": {
          "type": "custom",
          "char_filter": ["html_strip"],
          "tokenizer": "my_lowercase_tokenizer",
          "filter": ["lowercase"]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "my_field": {
        "type": "text",
        "analyzer": "my_custom_simple_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /my_custom_simple_index/_analyze
{
  "analyzer": "my_custom_simple_analyzer",
  "text": "<p>The slow turtle swims over to dogs &copy; 2024!</p>"
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {"token": "the","start_offset": 3,"end_offset": 6,"type": "word","position": 0},
    {"token": "slow","start_offset": 7,"end_offset": 11,"type": "word","position": 1},
    {"token": "turtle","start_offset": 12,"end_offset": 18,"type": "word","position": 2},
    {"token": "swims","start_offset": 19,"end_offset": 24,"type": "word","position": 3},
    {"token": "over","start_offset": 25,"end_offset": 29,"type": "word","position": 4},
    {"token": "to","start_offset": 30,"end_offset": 32,"type": "word","position": 5},
    {"token": "dogs","start_offset": 33,"end_offset": 37,"type": "word","position": 6}
  ]
}
```
