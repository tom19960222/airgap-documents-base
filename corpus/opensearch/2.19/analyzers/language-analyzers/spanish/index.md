---
collection: "opensearch"
version: "2.19"
title: "Spanish"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/language-analyzers/spanish.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/language-analyzers/spanish.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/language-analyzers/spanish/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/language-analyzers/spanish/"
canonical_route: "/analyzers/language-analyzers/spanish/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Analyzers"
layout: "default"
nav_order: 300
parent: "Language analyzers"
---
# Spanish analyzer

The built-in `spanish` analyzer can be applied to a text field using the following command:

```json
PUT /spanish-index
{
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "spanish"
      }
    }
  }
}
```

## Stem exclusion

You can use `stem_exclusion` with this language analyzer using the following command:

```json
PUT index_with_stem_exclusion_spanish_analyzer
{
  "settings": {
    "analysis": {
      "analyzer": {
        "stem_exclusion_spanish_analyzer": {
          "type": "spanish",
          "stem_exclusion": ["autoridad", "aprobación"]
        }
      }
    }
  }
}
```

## Spanish analyzer internals

The `spanish` analyzer is built using the following components:

- Tokenizer: `standard`

- Token filters:
  - lowercase
  - stop (Spanish)
  - keyword
  - stemmer (Spanish)

## Custom Spanish analyzer

You can create a custom Spanish analyzer using the following command:

```json
PUT /spanish-index
{
  "settings": {
    "analysis": {
      "filter": {
        "spanish_stop": {
          "type": "stop",
          "stopwords": "_spanish_"
        },
        "spanish_stemmer": {
          "type": "stemmer",
          "language": "light_spanish"
        },
        "spanish_keywords": {
          "type": "keyword_marker",
          "keywords": []
        }
      },
      "analyzer": {
        "spanish_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "spanish_stop",
            "spanish_keywords",
            "spanish_stemmer"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "spanish_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /spanish-index/_analyze
{
  "field": "content",
  "text": "Los estudiantes estudian en universidades españolas. Sus números son 123456."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "estudiant",
      "start_offset": 4,
      "end_offset": 15,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "estudian",
      "start_offset": 16,
      "end_offset": 24,
      "type": "<ALPHANUM>",
      "position": 2
    },
    {
      "token": "universidad",
      "start_offset": 28,
      "end_offset": 41,
      "type": "<ALPHANUM>",
      "position": 4
    },
    {
      "token": "español",
      "start_offset": 42,
      "end_offset": 51,
      "type": "<ALPHANUM>",
      "position": 5
    },
    {
      "token": "numer",
      "start_offset": 57,
      "end_offset": 64,
      "type": "<ALPHANUM>",
      "position": 7
    },
    {
      "token": "123456",
      "start_offset": 69,
      "end_offset": 75,
      "type": "<NUM>",
      "position": 9
    }
  ]
}
```
