---
collection: "opensearch"
version: "2.19"
title: "Analyzer"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/mapping-parameters/analyzer.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/mapping-parameters/analyzer.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/mapping-parameters/analyzer/"
canonical_url: "https://docs.opensearch.org/latest/mappings/mapping-parameters/analyzer/"
canonical_route: "/mappings/mapping-parameters/analyzer/"
redirect_from: ["/mappings/mapping-parameters/analyzer/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Mapping and field types"
has_children: false
has_toc: false
layout: "default"
nav_order: 5
parent: "Mapping parameters"
---
# Analyzer

The `analyzer` mapping parameter is used to define the text analysis process that applies to a text field during both index and search operations.

The key functions of the `analyzer` mapping parameter are:

1. **Tokenization:** The analyzer determines how the text is broken down into individual tokens (words, numbers) that can be indexed and searched. Each generated token must not exceed 32,766 bytes in order to avoid indexing failures.

2. **Normalization:** The analyzer can apply various normalization techniques, such as converting text to lowercase, removing stop words, and stemming/lemmatizing words.

3. **Consistency:** By defining the same analyzer for both index and search operations, you ensure that the text analysis process is consistent, which helps improve the relevance of search results.

4. **Customization:** OpenSearch allows you to define custom analyzers by specifying the tokenizer, character filters, and token filters to be used. This gives you fine-grained control over the text analysis process.

For information about specific analyzer parameters, such as `analyzer`, `search_analyzer`, or `search_quote_analyzer`, see [Search analyzers](../../../analyzers/search-analyzers/index.md).
{: .note}

------------

## Example

The following example configuration defines a custom analyzer called `my_custom_analyzer`:

```json
PUT my_index
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_custom_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "my_stop_filter",
            "my_stemmer"
          ]
        }
      },
      "filter": {
        "my_stop_filter": {
          "type": "stop",
          "stopwords": ["the", "a", "and", "or"]
        },
        "my_stemmer": {
          "type": "stemmer",
          "language": "english"
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "my_text_field": {
        "type": "text",
        "analyzer": "my_custom_analyzer",
        "search_analyzer": "standard",
        "search_quote_analyzer": "my_custom_analyzer"
      }
    }
  }
}
```

In this example, the `my_custom_analyzer` uses the standard tokenizer, converts all tokens to lowercase, applies a custom stop word filter, and applies an English stemmer.

You can then map a text field so that it uses this custom analyzer for both index and search operations:

```json
"mappings": {
  "properties": {
    "my_text_field": {
      "type": "text",
      "analyzer": "my_custom_analyzer"
    }
  }
}
```
