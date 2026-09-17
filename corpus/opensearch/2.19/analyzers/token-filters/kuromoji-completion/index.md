---
collection: "opensearch"
version: "2.19"
title: "Kuromoji completion"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/token-filters/kuromoji-completion.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/token-filters/kuromoji-completion.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/token-filters/kuromoji-completion/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/token-filters/kuromoji-completion/"
canonical_route: "/analyzers/token-filters/kuromoji-completion/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 230
parent: "Token filters"
---
# Kuromoji completion token filter

The `kuromoji_completion` token filter is used to stem Katakana words in Japanese, which are often used to represent foreign words or loanwords. This filter is especially useful for autocompletion or suggest queries, in which partial matches on Katakana words can be expanded to include their full forms.

To use this token filter, you must first install the `analysis-kuromoji` plugin on all nodes by running `bin/opensearch-plugin install analysis-kuromoji` and then restart the cluster. For more information about installing additional plugins, see [Additional plugins](../../../install-and-configure/additional-plugins/index.md).

## Example

The following example request creates a new index named `kuromoji_sample` and configures an analyzer with a `kuromoji_completion` filter:

```json
PUT kuromoji_sample
{
  "settings": {
    "index": {
      "analysis": {
        "analyzer": {
          "my_analyzer": {
            "tokenizer": "kuromoji_tokenizer",
            "filter": [
              "my_katakana_stemmer"
            ]
          }
        },
        "filter": {
          "my_katakana_stemmer": {
            "type": "kuromoji_completion"
          }
        }
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer with text that translates to "use a computer":

```json
POST /kuromoji_sample/_analyze
{
  "analyzer": "my_analyzer",
  "text": "コンピューターを使う"
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "コンピューター", // The original Katakana word "computer".
      "start_offset": 0,
      "end_offset": 7,
      "type": "word",
      "position": 0
    },
    {
      "token": "konpyuーtaー", // Romanized version (Romaji) of "コンピューター".
      "start_offset": 0,
      "end_offset": 7,
      "type": "word",
      "position": 0
    },
    {
      "token": "konnpyuーtaー", // Another possible romanized version of "コンピューター" (with a slight variation in the spelling).
      "start_offset": 0,
      "end_offset": 7,
      "type": "word",
      "position": 0
    },
    {
      "token": "を", // A Japanese particle, "wo" or "o"
      "start_offset": 7,
      "end_offset": 8,
      "type": "word",
      "position": 1
    },
    {
      "token": "wo", // Romanized form of the particle "を" (often pronounced as "o").
      "start_offset": 7,
      "end_offset": 8,
      "type": "word",
      "position": 1
    },
    {
      "token": "o", // Another version of the romanization.
      "start_offset": 7,
      "end_offset": 8,
      "type": "word",
      "position": 1
    },
    {
      "token": "使う", // The verb "use" in Kanji.
      "start_offset": 8,
      "end_offset": 10,
      "type": "word",
      "position": 2
    },
    {
      "token": "tukau", // Romanized version of "使う"
      "start_offset": 8,
      "end_offset": 10,
      "type": "word",
      "position": 2
    },
    {
      "token": "tsukau", // Another romanized version of "使う", where "tsu" is more phonetically correct
      "start_offset": 8,
      "end_offset": 10,
      "type": "word",
      "position": 2
    }
  ]
}
```
