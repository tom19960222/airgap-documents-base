---
collection: "opensearch"
version: "2.19"
title: "Arabic"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/language-analyzers/arabic.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/language-analyzers/arabic.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/language-analyzers/arabic/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/language-analyzers/arabic/"
canonical_route: "/analyzers/language-analyzers/arabic/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Analyzers"
layout: "default"
nav_order: 10
parent: "Language analyzers"
---
# Arabic analyzer

The built-in `arabic` analyzer can be applied to a text field using the following command:

```json
PUT /arabic-index
{
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "arabic"
      }
    }
  }
}
```

## Stem exclusion

You can use `stem_exclusion` with this language analyzer using the following command:

```json
PUT index_with_stem_exclusion_arabic
{
  "settings": {
    "analysis": {
      "analyzer": {
        "stem_exclusion_arabic_analyzer":{
          "type":"arabic",
          "stem_exclusion":["تكنولوجيا","سلطة "]
        }
      }
    }
  }
}
```

## Arabic analyzer internals

The `arabic` analyzer is built using the following components:

- Tokenizer: `standard`

- Token filters:
  - lowercase
  - decimal_digit
  - stop (Arabic)
  - normalization (Arabic)
  - keyword
  - stemmer (Arabic)

## Custom Arabic analyzer

You can create a custom Arabic analyzer using the following command:

```json
PUT /arabic-index
{
  "settings": {
    "analysis": {
      "filter": {
        "arabic_stop": {
          "type": "stop",
          "stopwords": "_arabic_"
        },
        "arabic_stemmer": {
          "type": "stemmer",
          "language": "arabic"
        },
        "arabic_normalization": {
          "type": "arabic_normalization"
        },
        "decimal_digit": {
          "type": "decimal_digit"
        },
        "arabic_keywords": {
          "type":       "keyword_marker",
          "keywords":   []
        }
      },
      "analyzer": {
        "arabic_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "arabic_normalization",
            "decimal_digit",
            "arabic_stop",
            "arabic_keywords",
            "arabic_stemmer"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "arabic_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /arabic-index/_analyze
{
  "field": "content",
  "text": "الطلاب يدرسون في الجامعات العربية. أرقامهم ١٢٣٤٥٦."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "طلاب",
      "start_offset": 0,
      "end_offset": 6,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "يدرس",
      "start_offset": 7,
      "end_offset": 13,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "جامع",
      "start_offset": 17,
      "end_offset": 25,
      "type": "<ALPHANUM>",
      "position": 3
    },
    {
      "token": "عرب",
      "start_offset": 26,
      "end_offset": 33,
      "type": "<ALPHANUM>",
      "position": 4
    },
    {
      "token": "ارقامهم",
      "start_offset": 35,
      "end_offset": 42,
      "type": "<ALPHANUM>",
      "position": 5
    },
    {
      "token": "123456",
      "start_offset": 43,
      "end_offset": 49,
      "type": "<NUM>",
      "position": 6
    }
  ]
}
```
