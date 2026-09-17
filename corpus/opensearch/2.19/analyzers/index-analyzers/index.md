---
collection: "opensearch"
version: "2.19"
title: "Index analyzers"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/index-analyzers.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/index-analyzers.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/index-analyzers/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/index-analyzers/"
canonical_route: "/analyzers/index-analyzers/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 20
parent: "Analyzers"
---
# Index analyzers

Index analyzers are specified at indexing time and are used to analyze [text](../../field-types/supported-field-types/text/index.md) fields when indexing a document.

## Determining which index analyzer to use

To determine which analyzer to use for a field when a document is indexed, OpenSearch examines the following parameters in order:

1. The `analyzer` mapping parameter of the field
1. The `analysis.analyzer.default` index setting
1. The `standard` analyzer (default)

When specifying an index analyzer, keep in mind that in most cases, specifying an analyzer for each `text` field in an index works best. Analyzing both the text field (at indexing time) and the query string (at query time) with the same analyzer ensures that the search uses the same terms as those that are stored in the index.
{: .important }

For information about verifying which analyzer is associated with which field, see [Verifying analyzer settings](../index.md#verifying-analyzer-settings).

## Specifying an index analyzer for a field

When creating index mappings, you can supply the `analyzer` parameter for each [text](../../field-types/supported-field-types/text/index.md) field. For example, the following request specifies the `simple` analyzer for the `text_entry` field:

```json
PUT testindex
{
  "mappings": {
    "properties": {
      "text_entry": {
        "type": "text",
        "analyzer": "simple"
      }
    }
  }
}
```

## Specifying a default index analyzer for an index

If you want to use the same analyzer for all text fields in an index, you can specify it in the `analysis.analyzer.default` setting as follows:

```json
PUT testindex
{
  "settings": {
    "analysis": {
      "analyzer": {
        "default": {
          "type": "simple"
        }
      }
    }
  }
}
```

If you don't specify a default analyzer, the `standard` analyzer is used.
{: .note}
