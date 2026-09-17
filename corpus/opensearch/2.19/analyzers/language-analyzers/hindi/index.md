---
collection: "opensearch"
version: "2.19"
title: "Hindi"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/language-analyzers/hindi.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/language-analyzers/hindi.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/language-analyzers/hindi/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/language-analyzers/hindi/"
canonical_route: "/analyzers/language-analyzers/hindi/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Analyzers"
layout: "default"
nav_order: 190
parent: "Language analyzers"
---
# Hindi analyzer

The built-in `hindi` analyzer can be applied to a text field using the following command:

```json
PUT /hindi-index
{
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "hindi"
      }
    }
  }
}
```

## Stem exclusion

You can use `stem_exclusion` with this language analyzer using the following command:

```json
PUT index_with_stem_exclusion_hindi_analyzer
{
  "settings": {
    "analysis": {
      "analyzer": {
        "stem_exclusion_hindi_analyzer": {
          "type": "hindi",
          "stem_exclusion": ["अधिकार", "अनुमोदन"]
        }
      }
    }
  }
}
```

## Hindi analyzer internals

The `hindi` analyzer is built using the following components:

- Tokenizer: `standard`

- Token filters:
  - lowercase
  - decimal_digit
  - keyword
  - normalization (indic)
  - normalization (Hindi)
  - stop (Hindi)
  - stemmer (Hindi)

## Custom Hindi analyzer

You can create a custom Hindi analyzer using the following command:

```json
PUT /hindi-index
{
  "settings": {
    "analysis": {
      "filter": {
        "hindi_stop": {
          "type": "stop",
          "stopwords": "_hindi_"
        },
        "hindi_stemmer": {
          "type": "stemmer",
          "language": "hindi"
        },
        "hindi_keywords": {
          "type": "keyword_marker",
          "keywords": []
        }
      },
      "analyzer": {
        "hindi_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "decimal_digit",
            "hindi_keywords",
            "indic_normalization",
            "hindi_normalization",
            "hindi_stop",
            "hindi_stemmer"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "hindi_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /hindi-index/_analyze
{
  "field": "content",
  "text": "छात्र भारतीय विश्वविद्यालयों में पढ़ते हैं। उनके नंबर १२३४५६ हैं।"
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "छातर",
      "start_offset": 0,
      "end_offset": 5,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "भारतिय",
      "start_offset": 6,
      "end_offset": 12,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "विशवविदयालय",
      "start_offset": 13,
      "end_offset": 28,
      "type": "<ALPHANUM>",
      "position": 2
    },
    {
      "token": "पढ",
      "start_offset": 33,
      "end_offset": 38,
      "type": "<ALPHANUM>",
      "position": 4
    },
    {
      "token": "नंबर",
      "start_offset": 49,
      "end_offset": 53,
      "type": "<ALPHANUM>",
      "position": 7
    },
    {
      "token": "123456",
      "start_offset": 54,
      "end_offset": 60,
      "type": "<NUM>",
      "position": 8
    }
  ]
}
```
