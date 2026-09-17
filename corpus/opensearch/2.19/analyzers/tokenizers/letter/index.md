---
collection: "opensearch"
version: "2.19"
title: "Letter"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/tokenizers/letter.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/tokenizers/letter.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/tokenizers/letter/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/tokenizers/letter/"
canonical_route: "/analyzers/tokenizers/letter/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 60
parent: "Tokenizers"
---
# Letter tokenizer

The `letter` tokenizer splits text into words on any non-letter characters. It works well with many European languages but is ineffective with some Asian languages in which words aren't separated by spaces.

## Example usage

The following example request creates a new index named `my_index` and configures an analyzer with a `letter` tokenizer:

```json
PUT /my_index
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_letter_analyzer": {
          "type": "custom",
          "tokenizer": "letter"
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "my_letter_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST _analyze
{
  "tokenizer": "letter",
  "text": "Cats 4EVER love chasing butterflies!"
}

```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "Cats",
      "start_offset": 0,
      "end_offset": 4,
      "type": "word",
      "position": 0
    },
    {
      "token": "EVER",
      "start_offset": 6,
      "end_offset": 10,
      "type": "word",
      "position": 1
    },
    {
      "token": "love",
      "start_offset": 11,
      "end_offset": 15,
      "type": "word",
      "position": 2
    },
    {
      "token": "chasing",
      "start_offset": 16,
      "end_offset": 23,
      "type": "word",
      "position": 3
    },
    {
      "token": "butterflies",
      "start_offset": 24,
      "end_offset": 35,
      "type": "word",
      "position": 4
    }
  ]
}
```
