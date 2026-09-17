---
collection: "opensearch"
version: "2.19"
title: "Classic"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/token-filters/classic.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/token-filters/classic.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/token-filters/classic/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/token-filters/classic/"
canonical_route: "/analyzers/token-filters/classic/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 50
parent: "Token filters"
---
# Classic token filter

The primary function of the classic token filter is to work alongside the classic tokenizer. It processes tokens by applying the following common transformations, which aid in text analysis and search:
 - Removal of possessive endings such as *'s*. For example, *John's* becomes *John*.
 - Removal of periods from acronyms. For example, *D.A.R.P.A.* becomes *DARPA*.

## Example

The following example request creates a new index named `custom_classic_filter` and configures an analyzer with the `classic` filter:

```json
PUT /custom_classic_filter
{
  "settings": {
    "analysis": {
      "analyzer": {
        "custom_classic": {
          "type": "custom",
          "tokenizer": "classic",
          "filter": ["classic"]
        }
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /custom_classic_filter/_analyze
{
  "analyzer": "custom_classic",
  "text": "John's co-operate was excellent."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "John",
      "start_offset": 0,
      "end_offset": 6,
      "type": "<APOSTROPHE>",
      "position": 0
    },
    {
      "token": "co",
      "start_offset": 7,
      "end_offset": 9,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "operate",
      "start_offset": 10,
      "end_offset": 17,
      "type": "<ALPHANUM>",
      "position": 2
    },
    {
      "token": "was",
      "start_offset": 18,
      "end_offset": 21,
      "type": "<ALPHANUM>",
      "position": 3
    },
    {
      "token": "excellent",
      "start_offset": 22,
      "end_offset": 31,
      "type": "<ALPHANUM>",
      "position": 4
    }
  ]
}
```
