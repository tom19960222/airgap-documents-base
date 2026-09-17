---
collection: "opensearch"
version: "2.19"
title: "Whitespace"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/tokenizers/whitespace.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/tokenizers/whitespace.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/tokenizers/whitespace/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/tokenizers/whitespace/"
canonical_route: "/analyzers/tokenizers/whitespace/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 160
parent: "Tokenizers"
---
# Whitespace tokenizer

The `whitespace` tokenizer splits text on white space characters, such as spaces, tabs, and new lines. It treats each word separated by white space as a token and does not perform any additional analysis or normalization like lowercasing or punctuation removal.

## Example usage

The following example request creates a new index named `my_index` and configures an analyzer with a `whitespace` tokenizer:

```json
PUT /my_index
{
  "settings": {
    "analysis": {
      "tokenizer": {
        "whitespace_tokenizer": {
          "type": "whitespace"
        }
      },
      "analyzer": {
        "my_whitespace_analyzer": {
          "type": "custom",
          "tokenizer": "whitespace_tokenizer"
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "my_whitespace_analyzer"
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
  "analyzer": "my_whitespace_analyzer",
  "text": "OpenSearch is fast! Really fast."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "OpenSearch",
      "start_offset": 0,
      "end_offset": 10,
      "type": "word",
      "position": 0
    },
    {
      "token": "is",
      "start_offset": 11,
      "end_offset": 13,
      "type": "word",
      "position": 1
    },
    {
      "token": "fast!",
      "start_offset": 14,
      "end_offset": 19,
      "type": "word",
      "position": 2
    },
    {
      "token": "Really",
      "start_offset": 20,
      "end_offset": 26,
      "type": "word",
      "position": 3
    },
    {
      "token": "fast.",
      "start_offset": 27,
      "end_offset": 32,
      "type": "word",
      "position": 4
    }
  ]
}
```

## Parameters

The `whitespace` tokenizer can be configured with the following parameter.

Parameter | Required/Optional | Data type | Description
:--- | :--- | :--- | :---
`max_token_length` | Optional | Integer |  Sets the maximum length of the produced token. If this length is exceeded, the token is split into multiple tokens at the length configured in `max_token_length`. Default is `255`.
