---
collection: "opensearch"
version: "2.19"
title: "Swedish"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/language-analyzers/swedish.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/language-analyzers/swedish.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/language-analyzers/swedish/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/language-analyzers/swedish/"
canonical_route: "/analyzers/language-analyzers/swedish/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Analyzers"
layout: "default"
nav_order: 310
parent: "Language analyzers"
---
# Swedish analyzer

The built-in `swedish` analyzer can be applied to a text field using the following command:

```json
PUT /swedish-index
{
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "swedish"
      }
    }
  }
}
```

## Stem exclusion

You can use `stem_exclusion` with this language analyzer using the following command:

```json
PUT index_with_stem_exclusion_swedish_analyzer
{
  "settings": {
    "analysis": {
      "analyzer": {
        "stem_exclusion_swedish_analyzer": {
          "type": "swedish",
          "stem_exclusion": ["myndighet", "godkännande"]
        }
      }
    }
  }
}
```

## Swedish analyzer internals

The `swedish` analyzer is built using the following components:

- Tokenizer: `standard`

- Token filters:
  - lowercase
  - stop (Swedish)
  - keyword
  - stemmer (Swedish)

## Custom Swedish analyzer

You can create a custom Swedish analyzer using the following command:

```json
PUT /swedish-index
{
  "settings": {
    "analysis": {
      "filter": {
        "swedish_stop": {
          "type": "stop",
          "stopwords": "_swedish_"
        },
        "swedish_stemmer": {
          "type": "stemmer",
          "language": "swedish"
        },
        "swedish_keywords": {
          "type": "keyword_marker",
          "keywords": []
        }
      },
      "analyzer": {
        "swedish_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "swedish_stop",
            "swedish_keywords",
            "swedish_stemmer"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "swedish_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /swedish-index/_analyze
{
  "field": "content",
  "text": "Studenter studerar vid svenska universitet. Deras nummer är 123456."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "student",
      "start_offset": 0,
      "end_offset": 9,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "studer",
      "start_offset": 10,
      "end_offset": 18,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "svensk",
      "start_offset": 23,
      "end_offset": 30,
      "type": "<ALPHANUM>",
      "position": 3
    },
    {
      "token": "universitet",
      "start_offset": 31,
      "end_offset": 42,
      "type": "<ALPHANUM>",
      "position": 4
    },
    {
      "token": "numm",
      "start_offset": 50,
      "end_offset": 56,
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
