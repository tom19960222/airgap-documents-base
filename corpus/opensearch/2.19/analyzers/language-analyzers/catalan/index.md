---
collection: "opensearch"
version: "2.19"
title: "Catalan"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/language-analyzers/catalan.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/language-analyzers/catalan.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/language-analyzers/catalan/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/language-analyzers/catalan/"
canonical_route: "/analyzers/language-analyzers/catalan/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Analyzers"
layout: "default"
nav_order: 70
parent: "Language analyzers"
---
# Catalan analyzer

The built-in `catalan` analyzer can be applied to a text field using the following command:

```json
PUT /catalan-index
{
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "catalan"
      }
    }
  }
}
```

## Stem exclusion

You can use `stem_exclusion` with this language analyzer using the following command:

```json
PUT index_with_stem_exclusion_catalan_analyzer
{
  "settings": {
    "analysis": {
      "analyzer": {
        "stem_exclusion_catalan_analyzer": {
          "type": "catalan",
          "stem_exclusion": ["autoritat", "aprovació"]
        }
      }
    }
  }
}
```

## Catalan analyzer internals

The `catalan` analyzer is built using the following components:

- Tokenizer: `standard`

- Token filters:
  - elision (Catalan)
  - lowercase
  - stop (Catalan)
  - keyword
  - stemmer (Catalan)

## Custom Catalan analyzer

You can create a custom Catalan analyzer using the following command:

```json
PUT /catalan-index
{
  "settings": {
    "analysis": {
      "filter": {
        "catalan_stop": {
          "type": "stop",
          "stopwords": "_catalan_"
        },
        "catalan_elision": {
          "type":       "elision",
          "articles":   [ "d", "l", "m", "n", "s", "t"],
          "articles_case": true
        },
        "catalan_stemmer": {
          "type": "stemmer",
          "language": "catalan"
        },
        "catalan_keywords": {
          "type":       "keyword_marker",
          "keywords":   []
        }
      },
      "analyzer": {
        "catalan_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "catalan_elision",
            "lowercase",
            "catalan_stop",
            "catalan_keywords",
            "catalan_stemmer"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "catalan_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /catalan-index/_analyze
{
  "field": "content",
  "text": "Els estudiants estudien a les universitats catalanes. Els seus números són 123456."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {"token": "estud","start_offset": 4,"end_offset": 14,"type": "<ALPHANUM>","position": 1},
    {"token": "estud","start_offset": 15,"end_offset": 23,"type": "<ALPHANUM>","position": 2},
    {"token": "univer","start_offset": 30,"end_offset": 42,"type": "<ALPHANUM>","position": 5},
    {"token": "catalan","start_offset": 43,"end_offset": 52,"type": "<ALPHANUM>","position": 6},
    {"token": "numer","start_offset": 63,"end_offset": 70,"type": "<ALPHANUM>","position": 9},
    {"token": "123456","start_offset": 75,"end_offset": 81,"type": "<NUM>","position": 11}
  ]
}
```
