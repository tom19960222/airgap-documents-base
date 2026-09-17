---
collection: "opensearch"
version: "2.19"
title: "Length"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/token-filters/length.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/token-filters/length.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/token-filters/length/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/token-filters/length/"
canonical_route: "/analyzers/token-filters/length/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 240
parent: "Token filters"
---
# Length token filter

The `length` token filter is used to remove tokens that don't meet specified length criteria (minimum and maximum values) from the token stream.

## Parameters

The `length` token filter can be configured with the following parameters.

Parameter | Required/Optional | Data type | Description
:--- | :--- | :--- | :---
`min` | Optional | Integer | The minimum token length. Default is `0`.
`max` | Optional | Integer | The maximum token length. Default is `Integer.MAX_VALUE` (`2147483647`).

## Example

The following example request creates a new index named `my_index` and configures an analyzer with a `length` filter:

```json
PUT my_index
{
  "settings": {
    "analysis": {
      "analyzer": {
        "only_keep_4_to_10_characters": {
          "tokenizer": "whitespace",
          "filter": [ "length_4_to_10" ]
        }
      },
      "filter": {
        "length_4_to_10": {
          "type": "length",
          "min": 4,
          "max": 10
        }
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
GET /my_index/_analyze
{
  "analyzer": "only_keep_4_to_10_characters",
  "text": "OpenSearch is a great tool!"
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
      "token": "great",
      "start_offset": 16,
      "end_offset": 21,
      "type": "word",
      "position": 3
    },
    {
      "token": "tool!",
      "start_offset": 22,
      "end_offset": 27,
      "type": "word",
      "position": 4
    }
  ]
}
```
