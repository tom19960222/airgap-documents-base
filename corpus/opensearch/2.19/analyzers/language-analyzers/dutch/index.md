---
collection: "opensearch"
version: "2.19"
title: "Dutch"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/language-analyzers/dutch.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/language-analyzers/dutch.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/language-analyzers/dutch/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/language-analyzers/dutch/"
canonical_route: "/analyzers/language-analyzers/dutch/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Analyzers"
layout: "default"
nav_order: 110
parent: "Language analyzers"
---
# Dutch analyzer

The built-in `dutch` analyzer can be applied to a text field using the following command:

```json
PUT /dutch-index
{
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "dutch"
      }
    }
  }
}
```

## Stem exclusion

You can use `stem_exclusion` with this language analyzer using the following command:

```json
PUT index_with_stem_exclusion_dutch_analyzer
{
  "settings": {
    "analysis": {
      "analyzer": {
        "stem_exclusion_dutch_analyzer": {
          "type": "dutch",
          "stem_exclusion": ["autoriteit", "goedkeuring"]
        }
      }
    }
  }
}
```

## Dutch analyzer internals

The `dutch` analyzer is built using the following components:

- Tokenizer: `standard`

- Token filters:
  - lowercase
  - stop (Dutch)
  - keyword
  - stemmer_override
  - stemmer (Dutch)

## Custom Dutch analyzer

You can create a custom Dutch analyzer using the following command:

```json
PUT /dutch-index
{
  "settings": {
    "analysis": {
      "filter": {
        "dutch_stop": {
          "type": "stop",
          "stopwords": "_dutch_"
        },
        "dutch_stemmer": {
          "type": "stemmer",
          "language": "dutch"
        },
        "dutch_keywords": {
          "type": "keyword_marker",
          "keywords": []
        },
        "dutch_override": {
          "type": "stemmer_override",
          "rules": [
            "fiets=>fiets",
            "bromfiets=>bromfiets",
            "ei=>eier",
            "kind=>kinder"
          ]
        }
      },
      "analyzer": {
        "dutch_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "dutch_stop",
            "dutch_keywords",
            "dutch_override",
            "dutch_stemmer"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "dutch_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /dutch-index/_analyze
{
  "field": "content",
  "text": "De studenten studeren in Nederland en bezoeken Amsterdam. Hun nummers zijn 123456."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {"token": "student","start_offset": 3,"end_offset": 12,"type": "<ALPHANUM>","position": 1},
    {"token": "studer","start_offset": 13,"end_offset": 21,"type": "<ALPHANUM>","position": 2},
    {"token": "nederland","start_offset": 25,"end_offset": 34,"type": "<ALPHANUM>","position": 4},
    {"token": "bezoek","start_offset": 38,"end_offset": 46,"type": "<ALPHANUM>","position": 6},
    {"token": "amsterdam","start_offset": 47,"end_offset": 56,"type": "<ALPHANUM>","position": 7},
    {"token": "nummer","start_offset": 62,"end_offset": 69,"type": "<ALPHANUM>","position": 9},
    {"token": "123456","start_offset": 75,"end_offset": 81,"type": "<NUM>","position": 11}
  ]
}
```
