---
collection: "opensearch"
version: "2.19"
title: "Russian"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/language-analyzers/russian.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/language-analyzers/russian.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/language-analyzers/russian/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/language-analyzers/russian/"
canonical_route: "/analyzers/language-analyzers/russian/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Analyzers"
layout: "default"
nav_order: 280
parent: "Language analyzers"
---
# Russian analyzer

The built-in `russian` analyzer can be applied to a text field using the following command:

```json
PUT /russian-index
{
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "russian"
      }
    }
  }
}
```

## Stem exclusion

You can use `stem_exclusion` with this language analyzer using the following command:

```json
PUT index_with_stem_exclusion_russian_analyzer
{
  "settings": {
    "analysis": {
      "analyzer": {
        "stem_exclusion_russian_analyzer": {
          "type": "russian",
          "stem_exclusion": ["авторитет", "одобрение"]
        }
      }
    }
  }
}
```

## Russian analyzer internals

The `russian` analyzer is built using the following components:

- Tokenizer: `standard`

- Token filters:
  - lowercase
  - stop (Russian)
  - keyword
  - stemmer (Russian)

## Custom Russian analyzer

You can create a custom Russian analyzer using the following command:

```json
PUT /russian-index
{
  "settings": {
    "analysis": {
      "filter": {
        "russian_stop": {
          "type": "stop",
          "stopwords": "_russian_"
        },
        "russian_stemmer": {
          "type": "stemmer",
          "language": "russian"
        },
        "russian_keywords": {
          "type": "keyword_marker",
          "keywords": []
        }
      },
      "analyzer": {
        "russian_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "russian_stop",
            "russian_keywords",
            "russian_stemmer"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "russian_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /russian-index/_analyze
{
  "field": "content",
  "text": "Студенты учатся в университетах России. Их номера 123456."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "студент",
      "start_offset": 0,
      "end_offset": 8,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "учат",
      "start_offset": 9,
      "end_offset": 15,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "университет",
      "start_offset": 18,
      "end_offset": 31,
      "type": "<ALPHANUM>",
      "position": 3
    },
    {
      "token": "росс",
      "start_offset": 32,
      "end_offset": 38,
      "type": "<ALPHANUM>",
      "position": 4
    },
    {
      "token": "номер",
      "start_offset": 43,
      "end_offset": 49,
      "type": "<ALPHANUM>",
      "position": 6
    },
    {
      "token": "123456",
      "start_offset": 50,
      "end_offset": 56,
      "type": "<NUM>",
      "position": 7
    }
  ]
}
```
