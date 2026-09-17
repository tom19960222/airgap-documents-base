---
collection: "opensearch"
version: "2.19"
title: "Galician"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/language-analyzers/galician.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/language-analyzers/galician.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/language-analyzers/galician/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/language-analyzers/galician/"
canonical_route: "/analyzers/language-analyzers/galician/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Analyzers"
layout: "default"
nav_order: 160
parent: "Language analyzers"
---
# Galician analyzer

The built-in `galician` analyzer can be applied to a text field using the following command:

```json
PUT /galician-index
{
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "galician"
      }
    }
  }
}
```

## Stem exclusion

You can use `stem_exclusion` with this language analyzer using the following command:

```json
PUT index_with_stem_exclusion_galician_analyzer
{
  "settings": {
    "analysis": {
      "analyzer": {
        "stem_exclusion_galician_analyzer": {
          "type": "galician",
          "stem_exclusion": ["autoridade", "aceptación"]
        }
      }
    }
  }
}
```

## Galician analyzer internals

The `galician` analyzer is built using the following components:

- Tokenizer: `standard`

- Token filters:
  - lowercase
  - stop (French)
  - keyword
  - stemmer (French)

## Custom Galician analyzer

You can create a custom Galician analyzer using the following command:

```json
PUT /galician-index
{
  "settings": {
    "analysis": {
      "filter": {
        "galician_stop": {
          "type": "stop",
          "stopwords": "_galician_"
        },
        "galician_stemmer": {
          "type": "stemmer",
          "language": "galician"
        },
        "galician_keywords": {
          "type": "keyword_marker",
          "keywords": []
        }
      },
      "analyzer": {
        "galician_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "galician_stop",
            "galician_keywords",
            "galician_stemmer"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "galician_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /galician-index/_analyze
{
  "field": "content",
  "text": "Os estudantes estudan en Santiago e nas universidades galegas. Os seus números son 123456."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {"token": "estud","start_offset": 3,"end_offset": 13,"type": "<ALPHANUM>","position": 1},
    {"token": "estud","start_offset": 14,"end_offset": 21,"type": "<ALPHANUM>","position": 2},
    {"token": "santiag","start_offset": 25,"end_offset": 33,"type": "<ALPHANUM>","position": 4},
    {"token": "univers","start_offset": 40,"end_offset": 53,"type": "<ALPHANUM>","position": 7},
    {"token": "galeg","start_offset": 54,"end_offset": 61,"type": "<ALPHANUM>","position": 8},
    {"token": "numer","start_offset": 71,"end_offset": 78,"type": "<ALPHANUM>","position": 11},
    {"token": "son","start_offset": 79,"end_offset": 82,"type": "<ALPHANUM>","position": 12},
    {"token": "123456","start_offset": 83,"end_offset": 89,"type": "<NUM>","position": 13}
  ]
}
```
