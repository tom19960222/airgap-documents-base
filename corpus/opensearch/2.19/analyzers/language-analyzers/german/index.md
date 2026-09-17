---
collection: "opensearch"
version: "2.19"
title: "German"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/language-analyzers/german.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/language-analyzers/german.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/language-analyzers/german/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/language-analyzers/german/"
canonical_route: "/analyzers/language-analyzers/german/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Analyzers"
layout: "default"
nav_order: 170
parent: "Language analyzers"
---
# German analyzer

The built-in `german` analyzer can be applied to a text field using the following command:

```json
PUT /german-index
{
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "german"
      }
    }
  }
}
```

## Stem exclusion

You can use `stem_exclusion` with this language analyzer using the following command:

```json
PUT index_with_stem_exclusion_german_analyzer
{
  "settings": {
    "analysis": {
      "analyzer": {
        "stem_exclusion_german_analyzer": {
          "type": "german",
          "stem_exclusion": ["Autorität", "Genehmigung"]
        }
      }
    }
  }
}
```

## German analyzer internals

The `german` analyzer is built using the following components:

- Tokenizer: `standard`

- Token filters:
  - lowercase
  - stop (German)
  - keyword
  - normalization (German)
  - stemmer (German)

## Custom German analyzer

You can create a custom German analyzer using the following command:

```json
PUT /german-index
{
  "settings": {
    "analysis": {
      "filter": {
        "german_stop": {
          "type": "stop",
          "stopwords": "_german_"
        },
        "german_stemmer": {
          "type": "stemmer",
          "language": "light_german"
        },
        "german_keywords": {
          "type": "keyword_marker",
          "keywords": []
        }
      },
      "analyzer": {
        "german_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "german_stop",
            "german_keywords",
            "german_normalization",
            "german_stemmer"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "german_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /german-index/_analyze
{
  "field": "content",
  "text": "Die Studenten studieren an den deutschen Universitäten. Ihre Nummern sind 123456."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "student",
      "start_offset": 4,
      "end_offset": 13,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "studi",
      "start_offset": 14,
      "end_offset": 23,
      "type": "<ALPHANUM>",
      "position": 2
    },
    {
      "token": "deutsch",
      "start_offset": 31,
      "end_offset": 40,
      "type": "<ALPHANUM>",
      "position": 5
    },
    {
      "token": "universitat",
      "start_offset": 41,
      "end_offset": 54,
      "type": "<ALPHANUM>",
      "position": 6
    },
    {
      "token": "numm",
      "start_offset": 61,
      "end_offset": 68,
      "type": "<ALPHANUM>",
      "position": 8
    },
    {
      "token": "123456",
      "start_offset": 74,
      "end_offset": 80,
      "type": "<NUM>",
      "position": 10
    }
  ]
}
```
