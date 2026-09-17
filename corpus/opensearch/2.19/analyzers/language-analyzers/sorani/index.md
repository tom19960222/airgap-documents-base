---
collection: "opensearch"
version: "2.19"
title: "Sorani"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/language-analyzers/sorani.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/language-analyzers/sorani.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/language-analyzers/sorani/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/language-analyzers/sorani/"
canonical_route: "/analyzers/language-analyzers/sorani/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Analyzers"
layout: "default"
nav_order: 290
parent: "Language analyzers"
---
# Sorani analyzer

The built-in `sorani` analyzer can be applied to a text field using the following command:

```json
PUT /sorani-index
{
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "sorani"
      }
    }
  }
}
```

## Stem exclusion

You can use `stem_exclusion` with this language analyzer using the following command:

```json
PUT index_with_stem_exclusion_sorani_analyzer
{
  "settings": {
    "analysis": {
      "analyzer": {
        "stem_exclusion_sorani_analyzer": {
          "type": "sorani",
          "stem_exclusion": ["مؤسسه", "اجازه"]
        }
      }
    }
  }
}
```

## Sorani analyzer internals

The `sorani` analyzer is built using the following components:

- Tokenizer: `standard`

- Token filters:
  - normalization (Sorani)
  - lowercase
  - decimal_digit
  - stop (Sorani)
  - keyword
  - stemmer (Sorani)

## Custom Sorani analyzer

You can create a custom Sorani analyzer using the following command:

```json
PUT /sorani-index
{
  "settings": {
    "analysis": {
      "filter": {
        "sorani_stop": {
          "type": "stop",
          "stopwords": "_sorani_"
        },
        "sorani_stemmer": {
          "type": "stemmer",
          "language": "sorani"
        },
        "sorani_keywords": {
          "type": "keyword_marker",
          "keywords": []
        }
      },
      "analyzer": {
        "sorani_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "decimal_digit",
            "sorani_stop",
            "sorani_keywords",
            "sorani_stemmer"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "sorani_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /sorani-index/_analyze
{
  "field": "content",
  "text": "خوێندنی فەرمی لە هەولێرەوە. ژمارەکان ١٢٣٤٥٦."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "خوێندن",
      "start_offset": 0,
      "end_offset": 7,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "فەرم",
      "start_offset": 8,
      "end_offset": 13,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "هەولێر",
      "start_offset": 17,
      "end_offset": 26,
      "type": "<ALPHANUM>",
      "position": 3
    },
    {
      "token": "ژمار",
      "start_offset": 28,
      "end_offset": 36,
      "type": "<ALPHANUM>",
      "position": 4
    },
    {
      "token": "123456",
      "start_offset": 37,
      "end_offset": 43,
      "type": "<NUM>",
      "position": 5
    }
  ]
}
```
