---
collection: "opensearch"
version: "2.19"
title: "Bengali"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/language-analyzers/bengali.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/language-analyzers/bengali.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/language-analyzers/bengali/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/language-analyzers/bengali/"
canonical_route: "/analyzers/language-analyzers/bengali/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Analyzers"
layout: "default"
nav_order: 40
parent: "Language analyzers"
---
# Bengali analyzer

The built-in `bengali` analyzer can be applied to a text field using the following command:

```json
PUT /bengali-index
{
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "bengali"
      }
    }
  }
}
```

## Stem exclusion

You can use `stem_exclusion` with this language analyzer using the following command:

```json
PUT index_with_stem_exclusion_bengali_analyzer
{
  "settings": {
    "analysis": {
      "analyzer": {
        "stem_exclusion_bengali_analyzer": {
          "type": "bengali",
          "stem_exclusion": ["কর্তৃপক্ষ", "অনুমোদন"]
        }
      }
    }
  }
}
```

## Bengali analyzer internals

The `bengali` analyzer is built using the following components:

- Tokenizer: `standard`

- Token filters:
  - lowercase
  - decimal_digit
  - indic_normalization
  - normalization (Bengali)
  - stop (Bengali)
  - keyword
  - stemmer (Bengali)

## Custom Bengali analyzer

You can create a custom Bengali analyzer using the following command:

```json
PUT /bengali-index
{
  "settings": {
    "analysis": {
      "filter": {
        "bengali_stop": {
          "type": "stop",
          "stopwords": "_bengali_"
        },
        "bengali_stemmer": {
          "type": "stemmer",
          "language": "bengali"
        },
        "bengali_keywords": {
          "type":       "keyword_marker",
          "keywords":   []
        }
      },
      "analyzer": {
        "bengali_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "decimal_digit",
            "indic_normalization",
            "bengali_normalization",
            "bengali_stop",
            "bengali_keywords",
            "bengali_stemmer"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "bengali_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /bengali-index/_analyze
{
  "field": "content",
  "text": "ছাত্ররা বিশ্ববিদ্যালয়ে পড়াশোনা করে। তাদের নম্বরগুলি ১২৩৪৫৬।"
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {"token": "ছাত্র","start_offset": 0,"end_offset": 7,"type": "<ALPHANUM>","position": 0},
    {"token": "বিসসবিদালয়","start_offset": 8,"end_offset": 23,"type": "<ALPHANUM>","position": 1},
    {"token": "পরাসোন","start_offset": 24,"end_offset": 32,"type": "<ALPHANUM>","position": 2},
    {"token": "তা","start_offset": 38,"end_offset": 43,"type": "<ALPHANUM>","position": 4},
    {"token": "নমমর","start_offset": 44,"end_offset": 53,"type": "<ALPHANUM>","position": 5},
    {"token": "123456","start_offset": 54,"end_offset": 60,"type": "<NUM>","position": 6}
  ]
}
```
