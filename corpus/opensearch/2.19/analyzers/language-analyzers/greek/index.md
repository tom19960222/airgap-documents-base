---
collection: "opensearch"
version: "2.19"
title: "Greek"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/language-analyzers/greek.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/language-analyzers/greek.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/language-analyzers/greek/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/language-analyzers/greek/"
canonical_route: "/analyzers/language-analyzers/greek/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Analyzers"
layout: "default"
nav_order: 180
parent: "Language analyzers"
---
# Greek analyzer

The built-in `greek` analyzer can be applied to a text field using the following command:

```json
PUT /greek-index
{
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "greek"
      }
    }
  }
}
```

## Stem exclusion

You can use `stem_exclusion` with this language analyzer using the following command:

```json
PUT index_with_stem_exclusion_greek_analyzer
{
  "settings": {
    "analysis": {
      "analyzer": {
        "stem_exclusion_greek_analyzer": {
          "type": "greek",
          "stem_exclusion": ["αρχή", "έγκριση"]
        }
      }
    }
  }
}
```

## Greek analyzer internals

The `greek` analyzer is built using the following components:

- Tokenizer: `standard`

- Token filters:
  - lowercase
  - stop (Greek)
  - keyword
  - stemmer (Greek)

## Custom Greek analyzer

You can create a custom Greek analyzer using the following command:

```json
PUT /greek-index
{
  "settings": {
    "analysis": {
      "filter": {
        "greek_stop": {
          "type": "stop",
          "stopwords": "_greek_"
        },
        "greek_stemmer": {
          "type": "stemmer",
          "language": "greek"
        },
        "greek_keywords": {
          "type": "keyword_marker",
          "keywords": []
        }
      },
      "analyzer": {
        "greek_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "greek_stop",
            "greek_keywords",
            "greek_stemmer"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "greek_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /greek-index/_analyze
{
  "field": "content",
  "text": "Οι φοιτητές σπουδάζουν στα ελληνικά πανεπιστήμια. Οι αριθμοί τους είναι 123456."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {"token": "φοιτητές","start_offset": 3,"end_offset": 11,"type": "<ALPHANUM>","position": 1},
    {"token": "σπουδάζ","start_offset": 12,"end_offset": 22,"type": "<ALPHANUM>","position": 2},
    {"token": "στα","start_offset": 23,"end_offset": 26,"type": "<ALPHANUM>","position": 3},
    {"token": "ελληνικά","start_offset": 27,"end_offset": 35,"type": "<ALPHANUM>","position": 4},
    {"token": "πανεπιστήμ","start_offset": 36,"end_offset": 48,"type": "<ALPHANUM>","position": 5},
    {"token": "αριθμοί","start_offset": 53,"end_offset": 60,"type": "<ALPHANUM>","position": 7},
    {"token": "τους","start_offset": 61,"end_offset": 65,"type": "<ALPHANUM>","position": 8},
    {"token": "είνα","start_offset": 66,"end_offset": 71,"type": "<ALPHANUM>","position": 9},
    {"token": "123456","start_offset": 72,"end_offset": 78,"type": "<NUM>","position": 10}
  ]
}
```
