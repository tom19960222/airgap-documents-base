---
collection: "opensearch"
version: "2.19"
title: "Search analyzer"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/mapping-parameters/search-analyzer.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/mapping-parameters/search-analyzer.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/mapping-parameters/search-analyzer/"
canonical_url: "https://docs.opensearch.org/latest/mappings/mapping-parameters/search-analyzer/"
canonical_route: "/mappings/mapping-parameters/search-analyzer/"
redirect_from: ["/mappings/mapping-parameters/search-analyzer/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Mapping and field types"
has_children: false
has_toc: false
layout: "default"
nav_order: 160
parent: "Mapping parameters"
---
# Search analyzer

The `search_analyzer` mapping parameter specifies the analyzer to be used at search time for a [`text`](../../supported-field-types/text/index.md) field. This allows the analyzer used for indexing to differ from the one used for search, offering greater control over how search terms are interpreted and matched.

By default, the same analyzer is used for both indexing and search. However, using a custom `search_analyzer` can be helpful when you want to apply looser or stricter matching rules during search, such as using [`stemming`](../../../analyzers/stemming/index.md) or removing stopwords only at search time. For more information and use cases, see [Search analyzers](../../../analyzers/search-analyzers/index.md).
{: .note}

## Example

The following example creates a field that uses an `edge_ngram_analyzer` configured with an [`edge_ngram_tokenizer`](../../../analyzers/tokenizers/edge-n-gram/index.md) for indexing and a [`standard` analyzer](../../../analyzers/supported-analyzers/standard/index.md) for search:

```json
PUT /articles
{
  "settings": {
    "analysis": {
      "analyzer": {
        "edge_ngram_analyzer": {
          "tokenizer": "edge_ngram_tokenizer",
          "filter": ["lowercase"]
        }
      },
      "tokenizer": {
        "edge_ngram_tokenizer": {
          "type": "edge_ngram",
          "min_gram": 2,
          "max_gram": 10,
          "token_chars": ["letter", "digit"]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "edge_ngram_analyzer",
        "search_analyzer": "standard"
      }
    }
  }
}
```

For a full explanation of how search analyzers work as well as more examples, see [Search analyzers](../../../analyzers/search-analyzers/index.md).
