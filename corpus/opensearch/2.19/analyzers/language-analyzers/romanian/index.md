---
collection: "opensearch"
version: "2.19"
title: "Romanian"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/language-analyzers/romanian.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/language-analyzers/romanian.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/language-analyzers/romanian/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/language-analyzers/romanian/"
canonical_route: "/analyzers/language-analyzers/romanian/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Analyzers"
layout: "default"
nav_order: 270
parent: "Language analyzers"
---
# Romanian analyzer

The built-in `romanian` analyzer can be applied to a text field using the following command:

```json
PUT /romanian-index
{
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "romanian"
      }
    }
  }
}
```

## Stem exclusion

You can use `stem_exclusion` with this language analyzer using the following command:

```json
PUT index_with_stem_exclusion_romanian_analyzer
{
  "settings": {
    "analysis": {
      "analyzer": {
        "stem_exclusion_romanian_analyzer": {
          "type": "romanian",
          "stem_exclusion": ["autoritate", "aprobat"]
        }
      }
    }
  }
}
```

## Romanian analyzer internals

The `romanian` analyzer is built using the following components:

- Tokenizer: `standard`

- Token filters:
  - lowercase
  - stop (Romanian)
  - keyword
  - stemmer (Romanian)

## Custom Romanian analyzer

You can create a custom Romanian analyzer using the following command:

```json
PUT /romanian-index
{
  "settings": {
    "analysis": {
      "filter": {
        "romanian_stop": {
          "type": "stop",
          "stopwords": "_romanian_"
        },
        "romanian_stemmer": {
          "type": "stemmer",
          "language": "romanian"
        },
        "romanian_keywords": {
          "type": "keyword_marker",
          "keywords": []
        }
      },
      "analyzer": {
        "romanian_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "romanian_stop",
            "romanian_keywords",
            "romanian_stemmer"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "romanian_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /romanian-index/_analyze
{
  "field": "content",
  "text": "Studenții învață la universitățile din România. Numerele lor sunt 123456."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "studenț",
      "start_offset": 0,
      "end_offset": 9,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "învaț",
      "start_offset": 10,
      "end_offset": 16,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "universităț",
      "start_offset": 20,
      "end_offset": 34,
      "type": "<ALPHANUM>",
      "position": 3
    },
    {
      "token": "român",
      "start_offset": 39,
      "end_offset": 46,
      "type": "<ALPHANUM>",
      "position": 5
    },
    {
      "token": "numer",
      "start_offset": 48,
      "end_offset": 56,
      "type": "<ALPHANUM>",
      "position": 6
    },
    {
      "token": "123456",
      "start_offset": 66,
      "end_offset": 72,
      "type": "<NUM>",
      "position": 9
    }
  ]
}
```
