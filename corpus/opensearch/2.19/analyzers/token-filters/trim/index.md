---
collection: "opensearch"
version: "2.19"
title: "Trim"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/token-filters/trim.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/token-filters/trim.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/token-filters/trim/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/token-filters/trim/"
canonical_route: "/analyzers/token-filters/trim/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 430
parent: "Token filters"
---
# Trim token filter

The `trim` token filter removes leading and trailing white space characters from tokens.

Many popular tokenizers, such as `standard`, `keyword`, and `whitespace` tokenizers, automatically strip leading and trailing white space characters during tokenization. When using these tokenizers, there is no need to configure an additional `trim` token filter.
{: .note}

## Example

The following example request creates a new index named `my_pattern_trim_index` and configures an analyzer with a `trim` filter and a `pattern` tokenizer, which does not remove leading and trailing white space characters:

```json
PUT /my_pattern_trim_index
{
  "settings": {
    "analysis": {
      "filter": {
        "my_trim_filter": {
          "type": "trim"
        }
      },
      "tokenizer": {
        "my_pattern_tokenizer": {
          "type": "pattern",
          "pattern": ","
        }
      },
      "analyzer": {
        "my_pattern_trim_analyzer": {
          "type": "custom",
          "tokenizer": "my_pattern_tokenizer",
          "filter": [
            "lowercase",
            "my_trim_filter"
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
GET /my_pattern_trim_index/_analyze
{
  "analyzer": "my_pattern_trim_analyzer",
  "text": " OpenSearch ,  is ,   powerful  "
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "opensearch",
      "start_offset": 0,
      "end_offset": 12,
      "type": "word",
      "position": 0
    },
    {
      "token": "is",
      "start_offset": 13,
      "end_offset": 18,
      "type": "word",
      "position": 1
    },
    {
      "token": "powerful",
      "start_offset": 19,
      "end_offset": 32,
      "type": "word",
      "position": 2
    }
  ]
}
```
