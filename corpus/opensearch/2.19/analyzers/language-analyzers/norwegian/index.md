---
collection: "opensearch"
version: "2.19"
title: "Norwegian"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/language-analyzers/norwegian.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/language-analyzers/norwegian.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/language-analyzers/norwegian/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/language-analyzers/norwegian/"
canonical_route: "/analyzers/language-analyzers/norwegian/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Analyzers"
layout: "default"
nav_order: 240
parent: "Language analyzers"
---
# Norwegian analyzer

The built-in `norwegian` analyzer can be applied to a text field using the following command:

```json
PUT /norwegian-index
{
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "norwegian"
      }
    }
  }
}
```

## Stem exclusion

You can use `stem_exclusion` with this language analyzer using the following command:

```json
PUT index_with_stem_exclusion_norwegian_analyzer
{
  "settings": {
    "analysis": {
      "analyzer": {
        "stem_exclusion_norwegian_analyzer": {
          "type": "norwegian",
          "stem_exclusion": ["autoritet", "godkjenning"]
        }
      }
    }
  }
}
```

## Norwegian analyzer internals

The `norwegian` analyzer is built using the following components:

- Tokenizer: `standard`

- Token filters:
  - lowercase
  - stop (Norwegian)
  - keyword
  - stemmer (Norwegian)

## Custom Norwegian analyzer

You can create a custom Norwegian analyzer using the following command:

```json
PUT /norwegian-index
{
  "settings": {
    "analysis": {
      "filter": {
        "norwegian_stop": {
          "type": "stop",
          "stopwords": "_norwegian_"
        },
        "norwegian_stemmer": {
          "type": "stemmer",
          "language": "norwegian"
        },
        "norwegian_keywords": {
          "type": "keyword_marker",
          "keywords": []
        }
      },
      "analyzer": {
        "norwegian_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "norwegian_stop",
            "norwegian_keywords",
            "norwegian_stemmer"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "norwegian_analyzer"
      }
    }
  }
}

```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /norwegian-index/_analyze
{
  "field": "content",
  "text": "Studentene studerer ved norske universiteter. Deres nummer er 123456."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {"token": "student","start_offset": 0,"end_offset": 10,"type": "<ALPHANUM>","position": 0},
    {"token": "studer","start_offset": 11,"end_offset": 19,"type": "<ALPHANUM>","position": 1},
    {"token": "norsk","start_offset": 24,"end_offset": 30,"type": "<ALPHANUM>","position": 3},
    {"token": "universitet","start_offset": 31,"end_offset": 44,"type": "<ALPHANUM>","position": 4},
    {"token": "numm","start_offset": 52,"end_offset": 58,"type": "<ALPHANUM>","position": 6},
    {"token": "123456","start_offset": 62,"end_offset": 68,"type": "<NUM>","position": 8}
  ]
}
```
