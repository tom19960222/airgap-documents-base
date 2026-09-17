---
collection: "opensearch"
version: "2.19"
title: "Keyword analyzer"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/supported-analyzers/keyword.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/supported-analyzers/keyword.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/supported-analyzers/keyword/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/supported-analyzers/keyword/"
canonical_route: "/analyzers/supported-analyzers/keyword/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 80
parent: "Analyzers"
---
# Keyword analyzer

The `keyword` analyzer doesn't tokenize text at all. Instead, it treats the entire input as a single token and does not break it into individual tokens. The `keyword` analyzer is often used for fields containing email addresses, URLs, or product IDs and in other cases where tokenization is not desirable.

## Example

Use the following command to create an index named `my_keyword_index` with a `keyword` analyzer:

```json
PUT /my_keyword_index
{
  "mappings": {
    "properties": {
      "my_field": {
        "type": "text",
        "analyzer": "keyword"
      }
    }
  }
}
```

## Configuring a custom analyzer

Use the following command to configure an index with a custom analyzer that is equivalent to the `keyword` analyzer:

```json
PUT /my_custom_keyword_index
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_keyword_analyzer": {
          "tokenizer": "keyword"
        }
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /my_custom_keyword_index/_analyze
{
  "analyzer": "my_keyword_analyzer",
  "text": "Just one token"
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "Just one token",
      "start_offset": 0,
      "end_offset": 14,
      "type": "word",
      "position": 0
    }
  ]
}
```
