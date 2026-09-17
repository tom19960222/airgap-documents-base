---
collection: "opensearch"
version: "2.19"
title: "Unique"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/token-filters/unique.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/token-filters/unique.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/token-filters/unique/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/token-filters/unique/"
canonical_route: "/analyzers/token-filters/unique/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 450
parent: "Token filters"
---
# Unique token filter

The `unique` token filter ensures that only unique tokens are kept during the analysis process, removing duplicate tokens that appear within a single field or text block.

## Parameters

The `unique` token filter can be configured with the following parameter.

Parameter | Required/Optional | Data type | Description
:--- | :--- | :--- | :---
`only_on_same_position` | Optional | Boolean | If `true`, the token filter acts as a `remove_duplicates` token filter and only removes tokens that are in the same position. Default is `false`.

## Example

The following example request creates a new index named `unique_example` and configures an analyzer with a `unique` filter:

```json
PUT /unique_example
{
  "settings": {
    "analysis": {
      "filter": {
        "unique_filter": {
          "type": "unique",
          "only_on_same_position": false
        }
      },
      "analyzer": {
        "unique_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "unique_filter"
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
GET /unique_example/_analyze
{
  "analyzer": "unique_analyzer",
  "text": "OpenSearch OpenSearch is powerful powerful and scalable"
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "opensearch",
      "start_offset": 0,
      "end_offset": 10,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "is",
      "start_offset": 22,
      "end_offset": 24,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "powerful",
      "start_offset": 25,
      "end_offset": 33,
      "type": "<ALPHANUM>",
      "position": 2
    },
    {
      "token": "and",
      "start_offset": 43,
      "end_offset": 46,
      "type": "<ALPHANUM>",
      "position": 3
    },
    {
      "token": "scalable",
      "start_offset": 47,
      "end_offset": 55,
      "type": "<ALPHANUM>",
      "position": 4
    }
  ]
}
```
