---
collection: "opensearch"
version: "2.19"
title: "Italian"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/language-analyzers/italian.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/language-analyzers/italian.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/language-analyzers/italian/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/language-analyzers/italian/"
canonical_route: "/analyzers/language-analyzers/italian/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Analyzers"
layout: "default"
nav_order: 220
parent: "Language analyzers"
---
# Italian analyzer

The built-in `italian` analyzer can be applied to a text field using the following command:

```json
PUT /italian-index
{
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "italian"
      }
    }
  }
}
```

## Stem exclusion

You can use `stem_exclusion` with this language analyzer using the following command:

```json
PUT index_with_stem_exclusion_italian_analyzer
{
  "settings": {
    "analysis": {
      "analyzer": {
        "stem_exclusion_italian_analyzer": {
          "type": "italian",
          "stem_exclusion": ["autorità", "approvazione"]
        }
      }
    }
  }
}
```

## Italian analyzer internals

The `italian` analyzer is built using the following components:

- Tokenizer: `standard`

- Token filters:
  - elision (Italian)
  - lowercase
  - stop (Italian)
  - keyword
  - stemmer (Italian)

## Custom Italian analyzer

You can create a custom Italian analyzer using the following command:

```json
PUT /italian-index
{
  "settings": {
    "analysis": {
      "filter": {
        "italian_stop": {
          "type": "stop",
          "stopwords": "_italian_"
        },
        "italian_elision": {
          "type": "elision",
          "articles": [
                "c", "l", "all", "dall", "dell",
                "nell", "sull", "coll", "pell",
                "gl", "agl", "dagl", "degl", "negl",
                "sugl", "un", "m", "t", "s", "v", "d"
          ],
          "articles_case": true
        },
        "italian_stemmer": {
          "type": "stemmer",
          "language": "light_italian"
        },
        "italian_keywords": {
          "type": "keyword_marker",
          "keywords": []
        }
      },
      "analyzer": {
        "italian_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "italian_elision",
            "lowercase",
            "italian_stop",
            "italian_keywords",
            "italian_stemmer"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "italian_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /italian-index/_analyze
{
  "field": "content",
  "text": "Gli studenti studiano nelle università italiane. I loro numeri sono 123456."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {"token": "student","start_offset": 4,"end_offset": 12,"type": "<ALPHANUM>","position": 1},
    {"token": "studian","start_offset": 13,"end_offset": 21,"type": "<ALPHANUM>","position": 2},
    {"token": "universit","start_offset": 28,"end_offset": 38,"type": "<ALPHANUM>","position": 4},
    {"token": "italian","start_offset": 39,"end_offset": 47,"type": "<ALPHANUM>","position": 5},
    {"token": "numer","start_offset": 56,"end_offset": 62,"type": "<ALPHANUM>","position": 8},
    {"token": "123456","start_offset": 68,"end_offset": 74,"type": "<NUM>","position": 10}
  ]
}
```
