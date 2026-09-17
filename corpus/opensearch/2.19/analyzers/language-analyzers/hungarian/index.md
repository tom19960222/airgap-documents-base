---
collection: "opensearch"
version: "2.19"
title: "Hungarian"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/language-analyzers/hungarian.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/language-analyzers/hungarian.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/language-analyzers/hungarian/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/language-analyzers/hungarian/"
canonical_route: "/analyzers/language-analyzers/hungarian/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Analyzers"
layout: "default"
nav_order: 200
parent: "Language analyzers"
---
# Hungarian analyzer

The built-in `hungarian` analyzer can be applied to a text field using the following command:

```json
PUT /hungarian-index
{
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "hungarian"
      }
    }
  }
}
```

## Stem exclusion

You can use `stem_exclusion` with this language analyzer using the following command:

```json
PUT index_with_stem_exclusion_hungarian_analyzer
{
  "settings": {
    "analysis": {
      "analyzer": {
        "stem_exclusion_hungarian_analyzer": {
          "type": "hungarian",
          "stem_exclusion": ["hatalom", "jóváhagyás"]
        }
      }
    }
  }
}
```

## Hungarian analyzer internals

The `hungarian` analyzer is built using the following components:

- Tokenizer: `standard`

- Token filters:
  - lowercase
  - stop (Hungarian)
  - keyword
  - stemmer (Hungarian)

## Custom Hungarian analyzer

You can create a custom Hungarian analyzer using the following command:

```json
PUT /hungarian-index
{
  "settings": {
    "analysis": {
      "filter": {
        "hungarian_stop": {
          "type": "stop",
          "stopwords": "_hungarian_"
        },
        "hungarian_stemmer": {
          "type": "stemmer",
          "language": "hungarian"
        },
        "hungarian_keywords": {
          "type": "keyword_marker",
          "keywords": []
        }
      },
      "analyzer": {
        "hungarian_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "hungarian_stop",
            "hungarian_keywords",
            "hungarian_stemmer"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "hungarian_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /hungarian-index/_analyze
{
  "field": "content",
  "text": "A diákok a magyar egyetemeken tanulnak. A számaik 123456."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "diák",
      "start_offset": 2,
      "end_offset": 8,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "magyar",
      "start_offset": 11,
      "end_offset": 17,
      "type": "<ALPHANUM>",
      "position": 3
    },
    {
      "token": "egyetem",
      "start_offset": 18,
      "end_offset": 29,
      "type": "<ALPHANUM>",
      "position": 4
    },
    {
      "token": "tanul",
      "start_offset": 30,
      "end_offset": 38,
      "type": "<ALPHANUM>",
      "position": 5
    },
    {
      "token": "szám",
      "start_offset": 42,
      "end_offset": 49,
      "type": "<ALPHANUM>",
      "position": 7
    },
    {
      "token": "123456",
      "start_offset": 50,
      "end_offset": 56,
      "type": "<NUM>",
      "position": 8
    }
  ]
}
```
