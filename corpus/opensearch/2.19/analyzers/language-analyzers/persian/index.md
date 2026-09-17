---
collection: "opensearch"
version: "2.19"
title: "Persian"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/language-analyzers/persian.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/language-analyzers/persian.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/language-analyzers/persian/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/language-analyzers/persian/"
canonical_route: "/analyzers/language-analyzers/persian/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Analyzers"
layout: "default"
nav_order: 250
parent: "Language analyzers"
---
# Persian analyzer

The built-in `persian` analyzer can be applied to a text field using the following command:

```json
PUT /persian-index
{
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "persian"
      }
    }
  }
}
```

## Stem exclusion

You can use `stem_exclusion` with this language analyzer using the following command:

```json
PUT index_with_stem_exclusion_persian_analyzer
{
  "settings": {
    "analysis": {
      "analyzer": {
        "stem_exclusion_persian_analyzer": {
          "type": "persian",
          "stem_exclusion": ["حکومت", "تأیید"]
        }
      }
    }
  }
}
```

## Persian analyzer internals

The `persian` analyzer is built using the following components:

- Tokenizer: `standard`

- Char filter: `mapping`

- Token filters:
  - lowercase
  - decimal_digit
  - normalization (Arabic)
  - normalization (Persian)
  - keyword
  - stemmer (Norwegian)

## Custom Persian analyzer

You can create a custom Persian analyzer using the following command:

```json
PUT /persian-index
{
  "settings": {
    "analysis": {
      "filter": {
        "persian_stop": {
          "type": "stop",
          "stopwords": "_persian_"
        },
        "persian_keywords": {
          "type": "keyword_marker",
          "keywords": []
        }
      },
      "char_filter": {
        "null_width_replace_with_space": {
            "type":       "mapping",
            "mappings": [ "\\u200C=>\\u0020"]
        }
      },
      "analyzer": {
        "persian_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "char_filter": [ "null_width_replace_with_space" ],
          "filter": [
            "lowercase",
            "decimal_digit",
            "arabic_normalization",
            "persian_normalization",
            "persian_stop"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "persian_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /persian-index/_analyze
{
  "field": "content",
  "text": "دانشجویان در دانشگاه‌های ایرانی تحصیل می‌کنند. شماره‌های آن‌ها ۱۲۳۴۵۶ است."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {"token": "دانشجويان","start_offset": 0,"end_offset": 9,"type": "<ALPHANUM>","position": 0},
    {"token": "دانشگاه","start_offset": 13,"end_offset": 20,"type": "<ALPHANUM>","position": 2},
    {"token": "ايراني","start_offset": 25,"end_offset": 31,"type": "<ALPHANUM>","position": 4},
    {"token": "تحصيل","start_offset": 32,"end_offset": 37,"type": "<ALPHANUM>","position": 5},
    {"token": "شماره","start_offset": 47,"end_offset": 52,"type": "<ALPHANUM>","position": 8},
    {"token": "123456","start_offset": 63,"end_offset": 69,"type": "<NUM>","position": 12}
  ]
}
```
