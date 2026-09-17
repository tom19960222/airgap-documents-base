---
collection: "opensearch"
version: "2.19"
title: "Snowball"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/token-filters/snowball.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/token-filters/snowball.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/token-filters/snowball/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/token-filters/snowball/"
canonical_route: "/analyzers/token-filters/snowball/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 380
parent: "Token filters"
---
# Snowball token filter

The `snowball` token filter is a stemming filter based on the [Snowball](https://snowballstem.org/) algorithm. It supports many languages and is more efficient and accurate than the Porter stemming algorithm.

## Parameters

The `snowball` token filter can be configured with a `language` parameter that accepts the following values:

- `Arabic`
- `Armenian`
- `Basque`
- `Catalan`
- `Danish`
- `Dutch`
- `English` (default)
- `Estonian`
- `Finnish`
- `French`
- `German`
- `German2`
- `Hungarian`
- `Italian`
- `Irish`
- `Kp`
- `Lithuanian`
- `Lovins`
- `Norwegian`
- `Porter`
- `Portuguese`
- `Romanian`
- `Russian`
- `Spanish`
- `Swedish`
- `Turkish`

## Example

The following example request creates a new index named `my-snowball-index` and configures an analyzer with a `snowball` filter:

```json
PUT /my-snowball-index
{
  "settings": {
    "analysis": {
      "filter": {
        "my_snowball_filter": {
          "type": "snowball",
          "language": "English"
        }
      },
      "analyzer": {
        "my_snowball_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "my_snowball_filter"
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
GET /my-snowball-index/_analyze
{
  "analyzer": "my_snowball_analyzer",
  "text": "running runners"
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "run",
      "start_offset": 0,
      "end_offset": 7,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "runner",
      "start_offset": 8,
      "end_offset": 15,
      "type": "<ALPHANUM>",
      "position": 1
    }
  ]
}
```
