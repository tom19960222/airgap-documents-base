---
collection: "opensearch"
version: "2.19"
title: "Czech"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/language-analyzers/czech.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/language-analyzers/czech.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/language-analyzers/czech/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/language-analyzers/czech/"
canonical_route: "/analyzers/language-analyzers/czech/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Analyzers"
layout: "default"
nav_order: 90
parent: "Language analyzers"
---
# Czech analyzer

The built-in `czech` analyzer can be applied to a text field using the following command:

```json
PUT /czech-index
{
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "czech"
      }
    }
  }
}
```

## Stem exclusion

You can use `stem_exclusion` with this language analyzer using the following command:

```json
PUT index_with_stem_exclusion_czech_analyzer
{
  "settings": {
    "analysis": {
      "analyzer": {
        "stem_exclusion_czech_analyzer": {
          "type": "czech",
          "stem_exclusion": ["autorita", "schválení"]
        }
      }
    }
  }
}
```

## Czech analyzer internals

The `czech` analyzer is built using the following components:

- Tokenizer: `standard`

- Token filters:
  - lowercase
  - stop (Czech)
  - keyword
  - stemmer (Czech)

## Custom Czech analyzer

You can create a custom Czech analyzer using the following command:

```json
PUT /czech-index
{
  "settings": {
    "analysis": {
      "filter": {
        "czech_stop": {
          "type": "stop",
          "stopwords": "_czech_"
        },
        "czech_stemmer": {
          "type": "stemmer",
          "language": "czech"
        },
        "czech_keywords": {
          "type":       "keyword_marker",
          "keywords":   []
        }
      },
      "analyzer": {
        "czech_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "czech_stop",
            "czech_keywords",
            "czech_stemmer"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "czech_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /czech-index/_analyze
{
  "field": "content",
  "text": "Studenti studují na českých univerzitách. Jejich čísla jsou 123456."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "student",
      "start_offset": 0,
      "end_offset": 8,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "studuj",
      "start_offset": 9,
      "end_offset": 16,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "česk",
      "start_offset": 20,
      "end_offset": 27,
      "type": "<ALPHANUM>",
      "position": 3
    },
    {
      "token": "univerzit",
      "start_offset": 28,
      "end_offset": 40,
      "type": "<ALPHANUM>",
      "position": 4
    },
    {
      "token": "čísl",
      "start_offset": 49,
      "end_offset": 54,
      "type": "<ALPHANUM>",
      "position": 6
    },
    {
      "token": "123456",
      "start_offset": 60,
      "end_offset": 66,
      "type": "<NUM>",
      "position": 8
    }
  ]
}
```
