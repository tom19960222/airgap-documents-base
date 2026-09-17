---
collection: "opensearch"
version: "2.19"
title: "KStem"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/token-filters/kstem.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/token-filters/kstem.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/token-filters/kstem/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/token-filters/kstem/"
canonical_route: "/analyzers/token-filters/kstem/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 220
parent: "Token filters"
---
# KStem token filter

The `kstem` token filter is a stemming filter used to reduce words to their root forms. The filter is a lightweight algorithmic stemmer designed for the English language that performs the following stemming operations:

- Reduces plurals to their singular form.
- Converts different verb tenses to their base form.
- Removes common derivational endings, such as "-ing" or "-ed".

The `kstem` token filter is equivalent to the a `stemmer` filter configured with a `light_english` language. It provides a more conservative stemming compared to other stemming filters like `porter_stem`.

The `kstem` token filter is based on the Lucene KStemFilter. For more information, see the [Lucene documentation](https://lucene.apache.org/core/9_10_0/analysis/common/org/apache/lucene/analysis/en/KStemFilter.html).

## Example

The following example request creates a new index named `my_kstem_index` and configures an analyzer with a `kstem` filter:

```json
PUT /my_kstem_index
{
  "settings": {
    "analysis": {
      "filter": {
        "kstem_filter": {
          "type": "kstem"
        }
      },
      "analyzer": {
        "my_kstem_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "kstem_filter"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "my_kstem_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /my_kstem_index/_analyze
{
  "analyzer": "my_kstem_analyzer",
  "text": "stops stopped"
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "stop",
      "start_offset": 0,
      "end_offset": 5,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "stop",
      "start_offset": 6,
      "end_offset": 13,
      "type": "<ALPHANUM>",
      "position": 1
    }
  ]
}
```
