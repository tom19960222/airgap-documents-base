---
collection: "opensearch"
version: "2.19"
title: "Condition"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/token-filters/condition.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/token-filters/condition.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/token-filters/condition/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/token-filters/condition/"
canonical_route: "/analyzers/token-filters/condition/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 70
parent: "Token filters"
---
# Condition token filter

The `condition` token filter is a special type of filter that allows you to apply other token filters conditionally based on certain criteria. This provides more control over when certain token filters should be applied during text analysis.
Multiple filters can be configured and only applied when they meet the conditions you define.
This token filter can be very useful for language-specific processing and handling of special characters.

## Parameters

There are two parameters that must be configured in order to use the `condition` token filter.

Parameter | Required/Optional | Data type | Description
:--- | :--- | :--- | :---
`filter` | Required | Array | Specifies which token filters should be applied to the tokens when the specified condition (defined by the `script` parameter) is met.
`script` | Required | Object | Configures an [inline script](../../../api-reference/script-apis/exec-script/index.md) that defines the condition that needs to be met in order for the filters specified in the `filter` parameter to be applied (only inline scripts are accepted).

## Example

The following example request creates a new index named `my_conditional_index` and configures an analyzer with a `condition` filter. This filter applies a `lowercase` filter to any tokens that contain the character sequence "um":

```json
PUT /my_conditional_index
{
  "settings": {
    "analysis": {
      "filter": {
        "my_conditional_filter": {
          "type": "condition",
          "filter": ["lowercase"],
          "script": {
            "source": "token.getTerm().toString().contains('um')"
          }
        }
      },
      "analyzer": {
        "my_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "my_conditional_filter"
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
GET /my_conditional_index/_analyze
{
  "analyzer": "my_analyzer",
  "text": "THE BLACK CAT JUMPS OVER A LAZY DOG"
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "THE",
      "start_offset": 0,
      "end_offset": 3,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "BLACK",
      "start_offset": 4,
      "end_offset": 9,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "CAT",
      "start_offset": 10,
      "end_offset": 13,
      "type": "<ALPHANUM>",
      "position": 2
    },
    {
      "token": "jumps",
      "start_offset": 14,
      "end_offset": 19,
      "type": "<ALPHANUM>",
      "position": 3
    },
    {
      "token": "OVER",
      "start_offset": 20,
      "end_offset": 24,
      "type": "<ALPHANUM>",
      "position": 4
    },
    {
      "token": "A",
      "start_offset": 25,
      "end_offset": 26,
      "type": "<ALPHANUM>",
      "position": 5
    },
    {
      "token": "LAZY",
      "start_offset": 27,
      "end_offset": 31,
      "type": "<ALPHANUM>",
      "position": 6
    },
    {
      "token": "DOG",
      "start_offset": 32,
      "end_offset": 35,
      "type": "<ALPHANUM>",
      "position": 7
    }
  ]
}
```
