---
collection: "opensearch"
version: "2.19"
title: "Elision"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/token-filters/elision.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/token-filters/elision.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/token-filters/elision/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/token-filters/elision/"
canonical_route: "/analyzers/token-filters/elision/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 130
parent: "Token filters"
---
# Elision token filter

The `elision` token filter is used to remove elided characters from words in certain languages. Elision typically occurs in languages such as French, in which words are often contracted and combined with the following word, typically by omitting a vowel and replacing it with an apostrophe.

The `elision` token filter is already preconfigured in the following [language analyzers](../../language-analyzers/index.md): `catalan`, `french`, `irish`, and `italian`.
{: .note}

## Parameters

The custom `elision` token filter can be configured with the following parameters.

Parameter | Required/Optional | Data type | Description
:--- | :--- | :--- | :---
`articles` | Required if `articles_path` is not configured | Array of strings | Defines which articles or short words should be removed when they appear as part of an elision.
`articles_path` | Required if `articles` is not configured | String | Specifies the path to a custom list of articles that should be removed during the analysis process.
`articles_case` | Optional | Boolean | Specifies whether the filter is case sensitive when matching elisions. Default is `false`.

## Example

The default set of French elisions is `l'`, `m'`, `t'`, `qu'`, `n'`, `s'`, `j'`, `d'`, `c'`, `jusqu'`, `quoiqu'`, `lorsqu'`, and `puisqu'`. You can update this by configuring the `french_elision` token filter. The following example request creates a new index named `french_texts` and configures an analyzer with a `french_elision` filter:

```json
PUT /french_texts
{
  "settings": {
    "analysis": {
      "filter": {
        "french_elision": {
          "type": "elision",
          "articles": [ "l", "t", "m", "d", "n", "s", "j" ]
        }
      },
      "analyzer": {
        "french_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": ["lowercase", "french_elision"]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "text": {
        "type": "text",
        "analyzer": "french_analyzer"
      }
    }
  }
}

```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /french_texts/_analyze
{
  "analyzer": "french_analyzer",
  "text": "L'étudiant aime l'école et le travail."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "étudiant",
      "start_offset": 0,
      "end_offset": 10,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "aime",
      "start_offset": 11,
      "end_offset": 15,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "école",
      "start_offset": 16,
      "end_offset": 23,
      "type": "<ALPHANUM>",
      "position": 2
    },
    {
      "token": "et",
      "start_offset": 24,
      "end_offset": 26,
      "type": "<ALPHANUM>",
      "position": 3
    },
    {
      "token": "le",
      "start_offset": 27,
      "end_offset": 29,
      "type": "<ALPHANUM>",
      "position": 4
    },
    {
      "token": "travail",
      "start_offset": 30,
      "end_offset": 37,
      "type": "<ALPHANUM>",
      "position": 5
    }
  ]
}
```
