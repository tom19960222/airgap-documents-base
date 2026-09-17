---
collection: "opensearch"
version: "2.19"
title: "French"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/language-analyzers/french.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/language-analyzers/french.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/language-analyzers/french/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/language-analyzers/french/"
canonical_route: "/analyzers/language-analyzers/french/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Analyzers"
layout: "default"
nav_order: 150
parent: "Language analyzers"
---
# French analyzer

The built-in `french` analyzer can be applied to a text field using the following command:

```json
PUT /french-index
{
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "french"
      }
    }
  }
}
```

## Stem exclusion

You can use `stem_exclusion` with this language analyzer using the following command:

```json
PUT index_with_stem_exclusion_french_analyzer
{
  "settings": {
    "analysis": {
      "analyzer": {
        "stem_exclusion_french_analyzer": {
          "type": "french",
          "stem_exclusion": ["autorité", "acceptation"]
        }
      }
    }
  }
}
```

## French analyzer internals

The `french` analyzer is built using the following components:

- Tokenizer: `standard`

- Token filters:
  - elision (French)
  - lowercase
  - stop (French)
  - keyword
  - stemmer (French)

## Custom French analyzer

You can create a custom French analyzer using the following command:

```json
PUT /french-index
{
  "settings": {
    "analysis": {
      "filter": {
        "french_stop": {
          "type": "stop",
          "stopwords": "_french_"
        },
        "french_elision": {
          "type":         "elision",
          "articles_case": true,
          "articles": [
              "l", "m", "t", "qu", "n", "s",
              "j", "d", "c", "jusqu", "quoiqu",
              "lorsqu", "puisqu"
            ]
        },
        "french_stemmer": {
          "type": "stemmer",
          "language": "light_french"
        },
        "french_keywords": {
          "type": "keyword_marker",
          "keywords": []
        }
      },
      "analyzer": {
        "french_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "french_elision",
            "lowercase",
            "french_stop",
            "french_keywords",
            "french_stemmer"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "french_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /french-index/_analyze
{
  "field": "content",
  "text": "Les étudiants étudient à Paris et dans les universités françaises. Leurs numéros sont 123456."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {"token": "etudiant","start_offset": 4,"end_offset": 13,"type": "<ALPHANUM>","position": 1},
    {"token": "etudient","start_offset": 14,"end_offset": 22,"type": "<ALPHANUM>","position": 2},
    {"token": "pari","start_offset": 25,"end_offset": 30,"type": "<ALPHANUM>","position": 4},
    {"token": "universit","start_offset": 43,"end_offset": 54,"type": "<ALPHANUM>","position": 8},
    {"token": "francais","start_offset": 55,"end_offset": 65,"type": "<ALPHANUM>","position": 9},
    {"token": "numero","start_offset": 73,"end_offset": 80,"type": "<ALPHANUM>","position": 11},
    {"token": "123456","start_offset": 86,"end_offset": 92,"type": "<NUM>","position": 13}
  ]
}
```
