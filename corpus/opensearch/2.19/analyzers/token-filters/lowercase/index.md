---
collection: "opensearch"
version: "2.19"
title: "Lowercase"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/token-filters/lowercase.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/token-filters/lowercase.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/token-filters/lowercase/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/token-filters/lowercase/"
canonical_route: "/analyzers/token-filters/lowercase/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 260
parent: "Token filters"
---
# Lowercase token filter

The `lowercase` token filter is used to convert all characters in the token stream to lowercase, making searches case insensitive.

## Parameters

The `lowercase` token filter can be configured with the following parameter.

Parameter | Required/Optional | Description
:--- | :--- | :---
 `language` | Optional | Specifies a language-specific token filter. Valid values are: <br>- [`greek`](https://lucene.apache.org/core/8_7_0/analyzers-common/org/apache/lucene/analysis/el/GreekLowerCaseFilter.html) <br>-  [`irish`](https://lucene.apache.org/core/8_7_0/analyzers-common/org/apache/lucene/analysis/ga/IrishLowerCaseFilter.html) <br>-  [`turkish`](https://lucene.apache.org/core/8_7_0/analyzers-common/org/apache/lucene/analysis/tr/TurkishLowerCaseFilter.html). <br> Default is the [Lucene LowerCaseFilter](https://lucene.apache.org/core/8_7_0/analyzers-common/org/apache/lucene/analysis/core/LowerCaseFilter.html).

## Example

The following example request creates a new index named `custom_lowercase_example`. It configures an analyzer with a `lowercase` filter and specifies `greek` as the `language`:

```json
PUT /custom_lowercase_example
{
  "settings": {
    "analysis": {
      "analyzer": {
        "greek_lowercase_example": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": ["greek_lowercase"]
        }
      },
      "filter": {
        "greek_lowercase": {
          "type": "lowercase",
          "language": "greek"
        }
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
GET /custom_lowercase_example/_analyze
{
  "analyzer": "greek_lowercase_example",
  "text": "Αθήνα ΕΛΛΑΔΑ"
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "αθηνα",
      "start_offset": 0,
      "end_offset": 5,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "ελλαδα",
      "start_offset": 6,
      "end_offset": 12,
      "type": "<ALPHANUM>",
      "position": 1
    }
  ]
}
```
