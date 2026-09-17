---
collection: "opensearch"
version: "2.19"
title: "Finnish"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/language-analyzers/finnish.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/language-analyzers/finnish.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/language-analyzers/finnish/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/language-analyzers/finnish/"
canonical_route: "/analyzers/language-analyzers/finnish/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Analyzers"
layout: "default"
nav_order: 140
parent: "Language analyzers"
---
# Finnish analyzer

The built-in `finnish` analyzer can be applied to a text field using the following command:

```json
PUT /finnish-index
{
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "finnish"
      }
    }
  }
}
```

## Stem exclusion

You can use `stem_exclusion` with this language analyzer using the following command:

```json
PUT index_with_stem_exclusion_finnish_analyzer
{
  "settings": {
    "analysis": {
      "analyzer": {
        "stem_exclusion_finnish_analyzer": {
          "type": "finnish",
          "stem_exclusion": ["valta", "hyväksyntä"]
        }
      }
    }
  }
}
```

## Finnish analyzer internals

The `finnish` analyzer is built using the following components:

- Tokenizer: `standard`

- Token filters:
  - lowercase
  - stop (Finnish)
  - keyword
  - stemmer (Finnish)

## Custom Finnish analyzer

You can create a custom Finnish analyzer using the following command:

```json
PUT /finnish-index
{
  "settings": {
    "analysis": {
      "filter": {
        "finnish_stop": {
          "type": "stop",
          "stopwords": "_finnish_"
        },
        "finnish_stemmer": {
          "type": "stemmer",
          "language": "finnish"
        },
        "finnish_keywords": {
          "type": "keyword_marker",
          "keywords": ["Helsinki", "Suomi"]
        }
      },
      "analyzer": {
        "finnish_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "finnish_stop",
            "finnish_keywords",
            "finnish_stemmer"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "finnish_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /finnish-index/_analyze
{
  "field": "content",
  "text": "Opiskelijat opiskelevat Helsingissä ja Suomen yliopistoissa. Heidän numeronsa ovat 123456."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {"token": "opiskelij","start_offset": 0,"end_offset": 11,"type": "<ALPHANUM>","position": 0},
    {"token": "opiskelev","start_offset": 12,"end_offset": 23,"type": "<ALPHANUM>","position": 1},
    {"token": "helsing","start_offset": 24,"end_offset": 35,"type": "<ALPHANUM>","position": 2},
    {"token": "suome","start_offset": 39,"end_offset": 45,"type": "<ALPHANUM>","position": 4},
    {"token": "yliopisto","start_offset": 46,"end_offset": 59,"type": "<ALPHANUM>","position": 5},
    {"token": "numero","start_offset": 68,"end_offset": 77,"type": "<ALPHANUM>","position": 7},
    {"token": "123456","start_offset": 83,"end_offset": 89,"type": "<NUM>","position": 9}
  ]
}
```
