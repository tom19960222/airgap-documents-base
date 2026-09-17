---
collection: "opensearch"
version: "2.19"
title: "Indonesian"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/language-analyzers/indonesian.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/language-analyzers/indonesian.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/language-analyzers/indonesian/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/language-analyzers/indonesian/"
canonical_route: "/analyzers/language-analyzers/indonesian/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Analyzers"
layout: "default"
nav_order: 210
parent: "Language analyzers"
---
# Indonesian analyzer

The built-in `indonesian` analyzer can be applied to a text field using the following command:

```json
PUT /indonesian-index
{
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "indonesian"
      }
    }
  }
}
```

## Stem exclusion

You can use `stem_exclusion` with this language analyzer using the following command:

```json
PUT index_with_stem_exclusion_indonesian_analyzer
{
  "settings": {
    "analysis": {
      "analyzer": {
        "stem_exclusion_indonesian_analyzer": {
          "type": "indonesian",
          "stem_exclusion": ["otoritas", "persetujuan"]
        }
      }
    }
  }
}
```

## Indonesian analyzer internals

The `indonesian` analyzer is built using the following components:

- Tokenizer: `standard`

- Token filters:
  - lowercase
  - stop (Indonesian)
  - keyword
  - stemmer (Indonesian)

## Custom Indonesian analyzer

You can create a custom Indonesian analyzer using the following command:

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
POST /indonesian-index/_analyze
{
  "field": "content",
  "text": "Mahasiswa belajar di universitas Indonesia. Nomor mereka adalah 123456."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "mahasiswa",
      "start_offset": 0,
      "end_offset": 9,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "ajar",
      "start_offset": 10,
      "end_offset": 17,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "universitas",
      "start_offset": 21,
      "end_offset": 32,
      "type": "<ALPHANUM>",
      "position": 3
    },
    {
      "token": "indonesia",
      "start_offset": 33,
      "end_offset": 42,
      "type": "<ALPHANUM>",
      "position": 4
    },
    {
      "token": "nomor",
      "start_offset": 44,
      "end_offset": 49,
      "type": "<ALPHANUM>",
      "position": 5
    },
    {
      "token": "123456",
      "start_offset": 64,
      "end_offset": 70,
      "type": "<NUM>",
      "position": 8
    }
  ]
}
```
