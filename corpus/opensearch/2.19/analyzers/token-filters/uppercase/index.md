---
collection: "opensearch"
version: "2.19"
title: "Uppercase"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/token-filters/uppercase.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/token-filters/uppercase.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/token-filters/uppercase/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/token-filters/uppercase/"
canonical_route: "/analyzers/token-filters/uppercase/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 460
parent: "Token filters"
---
# Uppercase token filter

The `uppercase` token filter is used to convert all tokens (words) to uppercase during analysis.

## Example

The following example request creates a new index named `uppercase_example` and configures an analyzer with an `uppercase` filter:

```json
PUT /uppercase_example
{
  "settings": {
    "analysis": {
      "filter": {
        "uppercase_filter": {
          "type": "uppercase"
        }
      },
      "analyzer": {
        "uppercase_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "uppercase_filter"
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
GET /uppercase_example/_analyze
{
  "analyzer": "uppercase_analyzer",
  "text": "OpenSearch is powerful"
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "OPENSEARCH",
      "start_offset": 0,
      "end_offset": 10,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "IS",
      "start_offset": 11,
      "end_offset": 13,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "POWERFUL",
      "start_offset": 14,
      "end_offset": 22,
      "type": "<ALPHANUM>",
      "position": 2
    }
  ]
}
```
