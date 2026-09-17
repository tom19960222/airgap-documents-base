---
collection: "opensearch"
version: "2.19"
title: "Simple pattern"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/tokenizers/simple-pattern.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/tokenizers/simple-pattern.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/tokenizers/simple-pattern/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/tokenizers/simple-pattern/"
canonical_route: "/analyzers/tokenizers/simple-pattern/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 110
parent: "Tokenizers"
---
# Simple pattern tokenizer

The `simple_pattern` tokenizer identifies matching sequences in text based on a regular expression and uses those sequences as tokens. It extracts terms that match the regular expression. Use this tokenizer when you want to directly extract specific patterns as terms.

## Example usage

The following example request creates a new index named `my_index` and configures an analyzer with a `simple_pattern` tokenizer. The tokenizer extracts numeric terms from text:

```json
PUT /my_index
{
  "settings": {
    "analysis": {
      "tokenizer": {
        "my_pattern_tokenizer": {
          "type": "simple_pattern",
          "pattern": "\\d+"
        }
      },
      "analyzer": {
        "my_pattern_analyzer": {
          "type": "custom",
          "tokenizer": "my_pattern_tokenizer"
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
  "analyzer": "my_pattern_analyzer",
  "text": "OpenSearch-2024-10-09"
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "2024",
      "start_offset": 11,
      "end_offset": 15,
      "type": "word",
      "position": 0
    },
    {
      "token": "10",
      "start_offset": 16,
      "end_offset": 18,
      "type": "word",
      "position": 1
    },
    {
      "token": "09",
      "start_offset": 19,
      "end_offset": 21,
      "type": "word",
      "position": 2
    }
  ]
}
```

## Parameters

The `simple_pattern` tokenizer can be configured with the following parameter.

Parameter | Required/Optional | Data type | Description
:--- | :--- | :--- | :---
`pattern` | Optional | String | The pattern used to split text into tokens, specified using a [Lucene regular expression](https://lucene.apache.org/core/9_10_0/core/org/apache/lucene/util/automaton/RegExp.html). Default is an empty string, which returns the input text as one token.
