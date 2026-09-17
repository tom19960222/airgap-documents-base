---
collection: "opensearch"
version: "2.19"
title: "Normalization"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/token-filters/normalization.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/token-filters/normalization.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/token-filters/normalization/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/token-filters/normalization/"
canonical_route: "/analyzers/token-filters/normalization/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 300
parent: "Token filters"
---
# Normalization token filter

The `normalization` token filter is designed to adjust and simplify text in a way that reduces variations, particularly variations in special characters. It is primarily used to handle variations in writing by standardizing characters in specific languages.

The following `normalization` token filters are available:

- [arabic_normalization](https://lucene.apache.org/core/8_7_0/analyzers-common/org/apache/lucene/analysis/ar/ArabicNormalizer.html)
- [german_normalization](https://lucene.apache.org/core/8_7_0/analyzers-common/org/apache/lucene/analysis/de/GermanNormalizationFilter.html)
- [hindi_normalization](https://lucene.apache.org/core/8_7_0/analyzers-common/org/apache/lucene/analysis/hi/HindiNormalizer.html)
- [indic_normalization](https://lucene.apache.org/core/8_7_0/analyzers-common/org/apache/lucene/analysis/in/IndicNormalizer.html)
- [sorani_normalization](https://lucene.apache.org/core/8_7_0/analyzers-common/org/apache/lucene/analysis/ckb/SoraniNormalizer.html)
- [persian_normalization](https://lucene.apache.org/core/8_7_0/analyzers-common/org/apache/lucene/analysis/fa/PersianNormalizer.html)
- [scandinavian_normalization](https://lucene.apache.org/core/8_7_0/analyzers-common/org/apache/lucene/analysis/miscellaneous/ScandinavianNormalizationFilter.html)
- [scandinavian_folding](https://lucene.apache.org/core/8_7_0/analyzers-common/org/apache/lucene/analysis/miscellaneous/ScandinavianFoldingFilter.html)
- [serbian_normalization](https://lucene.apache.org/core/8_7_0/analyzers-common/org/apache/lucene/analysis/sr/SerbianNormalizationFilter.html)

## Example

The following example request creates a new index named `german_normalizer_example` and configures an analyzer with a `german_normalization` filter:

```json
PUT /german_normalizer_example
{
  "settings": {
    "analysis": {
      "filter": {
        "german_normalizer": {
          "type": "german_normalization"
        }
      },
      "analyzer": {
        "german_normalizer_analyzer": {
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "german_normalizer"
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
POST /german_normalizer_example/_analyze
{
  "text": "Straße München",
  "analyzer": "german_normalizer_analyzer"
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "strasse",
      "start_offset": 0,
      "end_offset": 6,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "munchen",
      "start_offset": 7,
      "end_offset": 14,
      "type": "<ALPHANUM>",
      "position": 1
    }
  ]
}
```
