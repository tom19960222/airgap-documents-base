---
collection: "opensearch"
version: "2.19"
title: "Synonym graph"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/token-filters/synonym-graph.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/token-filters/synonym-graph.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/token-filters/synonym-graph/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/token-filters/synonym-graph/"
canonical_route: "/analyzers/token-filters/synonym-graph/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 420
parent: "Token filters"
---
# Synonym graph token filter

The `synonym_graph` token filter is a more advanced version of the `synonym` token filter. It supports multiword synonyms and processes synonyms across multiple tokens, making it ideal for phrases or scenarios in which relationships between tokens are important.

## Parameters

The `synonym_graph` token filter can be configured with the following parameters.

Parameter | Required/Optional | Data type | Description
:--- | :--- | :--- | :---
`synonyms` | Either `synonyms` or `synonyms_path` must be specified | String | A list of synonym rules defined directly in the configuration.
`synonyms_path` | Either `synonyms` or `synonyms_path` must be specified | String | The file path to a file containing synonym rules (either an absolute path or a path relative to the config directory).
`lenient` | Optional | Boolean | Whether to ignore exceptions when loading the rule configurations. Default is `false`.
`format` | Optional | String | Specifies the format used to determine how OpenSearch defines and interprets synonyms. Valid values are:<br>- `solr` <br>- [`wordnet`](https://wordnet.princeton.edu/). <br> Default is `solr`.
`expand` | Optional | Boolean |  Whether to expand equivalent synonym rules. Default is `true`.<br><br>For example: <br>If `synonyms` are defined as `"quick, fast"` and `expand` is set to `true`, then the synonym rules are configured as follows:<br>- `quick => quick`<br>- `quick => fast`<br>- `fast => quick`<br>- `fast => fast`<br><br>If `expand` is set to `false`, the synonym rules are configured as follows:<br>- `quick => quick`<br>- `fast => quick`

## Example: Solr format

The following example request creates a new index named `my-index` and configures an analyzer with a `synonym_graph` filter. The filter is configured with the default `solr` rule format:

```json
PUT /my-index
{
  "settings": {
    "analysis": {
      "filter": {
        "my_synonym_graph_filter": {
          "type": "synonym_graph",
          "synonyms": [
            "sports car, race car",
            "fast car, speedy vehicle",
            "luxury car, premium vehicle",
            "electric car, EV"
          ]
        }
      },
      "analyzer": {
        "my_synonym_graph_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "my_synonym_graph_filter"
          ]
        }
      }
    }
  }
}

```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
GET /my-car-index/_analyze
{
  "analyzer": "my_synonym_graph_analyzer",
  "text": "I just bought a sports car and it is a fast car."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {"token": "i","start_offset": 0,"end_offset": 1,"type": "<ALPHANUM>","position": 0},
    {"token": "just","start_offset": 2,"end_offset": 6,"type": "<ALPHANUM>","position": 1},
    {"token": "bought","start_offset": 7,"end_offset": 13,"type": "<ALPHANUM>","position": 2},
    {"token": "a","start_offset": 14,"end_offset": 15,"type": "<ALPHANUM>","position": 3},
    {"token": "race","start_offset": 16,"end_offset": 26,"type": "SYNONYM","position": 4},
    {"token": "sports","start_offset": 16,"end_offset": 22,"type": "<ALPHANUM>","position": 4,"positionLength": 2},
    {"token": "car","start_offset": 16,"end_offset": 26,"type": "SYNONYM","position": 5,"positionLength": 2},
    {"token": "car","start_offset": 23,"end_offset": 26,"type": "<ALPHANUM>","position": 6},
    {"token": "and","start_offset": 27,"end_offset": 30,"type": "<ALPHANUM>","position": 7},
    {"token": "it","start_offset": 31,"end_offset": 33,"type": "<ALPHANUM>","position": 8},
    {"token": "is","start_offset": 34,"end_offset": 36,"type": "<ALPHANUM>","position": 9},
    {"token": "a","start_offset": 37,"end_offset": 38,"type": "<ALPHANUM>","position": 10},
    {"token": "speedy","start_offset": 39,"end_offset": 47,"type": "SYNONYM","position": 11},
    {"token": "fast","start_offset": 39,"end_offset": 43,"type": "<ALPHANUM>","position": 11,"positionLength": 2},
    {"token": "vehicle","start_offset": 39,"end_offset": 47,"type": "SYNONYM","position": 12,"positionLength": 2},
    {"token": "car","start_offset": 44,"end_offset": 47,"type": "<ALPHANUM>","position": 13}
  ]
}
```

## Example: WordNet format

The following example request creates a new index named `my-wordnet-index` and configures an analyzer with a `synonym_graph` filter. The filter is configured with the [`wordnet`](https://wordnet.princeton.edu/) rule format:

```json
PUT /my-wordnet-index
{
  "settings": {
    "analysis": {
      "filter": {
        "my_synonym_graph_filter": {
          "type": "synonym_graph",
          "format": "wordnet",
          "synonyms": [
            "s(100000001, 1, 'sports car', n, 1, 0).",
            "s(100000001, 2, 'race car', n, 1, 0).",
            "s(100000001, 3, 'fast car', n, 1, 0).",
            "s(100000001, 4, 'speedy vehicle', n, 1, 0)."
          ]
        }
      },
      "analyzer": {
        "my_synonym_graph_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "my_synonym_graph_filter"
          ]
        }
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
GET /my-wordnet-index/_analyze
{
  "analyzer": "my_synonym_graph_analyzer",
  "text": "I just bought a sports car and it is a fast car."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {"token": "i","start_offset": 0,"end_offset": 1,"type": "<ALPHANUM>","position": 0},
    {"token": "just","start_offset": 2,"end_offset": 6,"type": "<ALPHANUM>","position": 1},
    {"token": "bought","start_offset": 7,"end_offset": 13,"type": "<ALPHANUM>","position": 2},
    {"token": "a","start_offset": 14,"end_offset": 15,"type": "<ALPHANUM>","position": 3},
    {"token": "race","start_offset": 16,"end_offset": 26,"type": "SYNONYM","position": 4},
    {"token": "fast","start_offset": 16,"end_offset": 26,"type": "SYNONYM","position": 4,"positionLength": 2},
    {"token": "speedy","start_offset": 16,"end_offset": 26,"type": "SYNONYM","position": 4,"positionLength": 3},
    {"token": "sports","start_offset": 16,"end_offset": 22,"type": "<ALPHANUM>","position": 4,"positionLength": 4},
    {"token": "car","start_offset": 16,"end_offset": 26,"type": "SYNONYM","position": 5,"positionLength": 4},
    {"token": "car","start_offset": 16,"end_offset": 26,"type": "SYNONYM","position": 6,"positionLength": 3},
    {"token": "vehicle","start_offset": 16,"end_offset": 26,"type": "SYNONYM","position": 7,"positionLength": 2},
    {"token": "car","start_offset": 23,"end_offset": 26,"type": "<ALPHANUM>","position": 8},
    {"token": "and","start_offset": 27,"end_offset": 30,"type": "<ALPHANUM>","position": 9},
    {"token": "it","start_offset": 31,"end_offset": 33,"type": "<ALPHANUM>","position": 10},
    {"token": "is","start_offset": 34,"end_offset": 36,"type": "<ALPHANUM>","position": 11},
    {"token": "a","start_offset": 37,"end_offset": 38,"type": "<ALPHANUM>","position": 12},
    {"token": "sports","start_offset": 39,"end_offset": 47,"type": "SYNONYM","position": 13},
    {"token": "race","start_offset": 39,"end_offset": 47,"type": "SYNONYM","position": 13,"positionLength": 2},
    {"token": "speedy","start_offset": 39,"end_offset": 47,"type": "SYNONYM","position": 13,"positionLength": 3},
    {"token": "fast","start_offset": 39,"end_offset": 43,"type": "<ALPHANUM>","position": 13,"positionLength": 4},
    {"token": "car","start_offset": 39,"end_offset": 47,"type": "SYNONYM","position": 14,"positionLength": 4},
    {"token": "car","start_offset": 39,"end_offset": 47,"type": "SYNONYM","position": 15,"positionLength": 3},
    {"token": "vehicle","start_offset": 39,"end_offset": 47,"type": "SYNONYM","position": 16,"positionLength": 2},
    {"token": "car","start_offset": 44,"end_offset": 47,"type": "<ALPHANUM>","position": 17}
  ]
}
```
