---
collection: "opensearch"
version: "2.19"
title: "Whitespace analyzer"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/supported-analyzers/whitespace.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/supported-analyzers/whitespace.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/supported-analyzers/whitespace/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/supported-analyzers/whitespace/"
canonical_route: "/analyzers/supported-analyzers/whitespace/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 120
parent: "Analyzers"
---
# Whitespace analyzer

The `whitespace` analyzer breaks text into tokens based only on white space characters (for example, spaces and tabs). It does not apply any transformations, such as lowercasing or removing stopwords, so the original case of the text is retained and punctuation is included as part of the tokens.

## Example

Use the following command to create an index named `my_whitespace_index` with a `whitespace` analyzer:

```json
PUT /my_whitespace_index
{
  "mappings": {
    "properties": {
      "my_field": {
        "type": "text",
        "analyzer": "whitespace"
      }
    }
  }
}
```

## Configuring a custom analyzer

Use the following command to configure an index with a custom analyzer that is equivalent to a `whitespace` analyzer with an added `lowercase` character filter:

```json
PUT /my_custom_whitespace_index
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_custom_whitespace_analyzer": {
          "type": "custom",
          "tokenizer": "whitespace",
          "filter": ["lowercase"]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "my_field": {
        "type": "text",
        "analyzer": "my_custom_whitespace_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /my_custom_whitespace_index/_analyze
{
  "analyzer": "my_custom_whitespace_analyzer",
  "text": "The SLOW turtle swims away! 123"
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {"token": "the","start_offset": 0,"end_offset": 3,"type": "word","position": 0},
    {"token": "slow","start_offset": 4,"end_offset": 8,"type": "word","position": 1},
    {"token": "turtle","start_offset": 9,"end_offset": 15,"type": "word","position": 2},
    {"token": "swims","start_offset": 16,"end_offset": 21,"type": "word","position": 3},
    {"token": "away!","start_offset": 22,"end_offset": 27,"type": "word","position": 4},
    {"token": "123","start_offset": 28,"end_offset": 31,"type": "word","position": 5}
  ]
}
```
