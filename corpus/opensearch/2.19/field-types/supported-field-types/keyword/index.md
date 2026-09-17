---
collection: "opensearch"
version: "2.19"
title: "Keyword"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/supported-field-types/keyword.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/supported-field-types/keyword.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/supported-field-types/keyword/"
canonical_url: "https://docs.opensearch.org/latest/mappings/supported-field-types/keyword/"
canonical_route: "/mappings/supported-field-types/keyword/"
redirect_from: ["/opensearch/supported-field-types/keyword/","/field-types/keyword/","/mappings/supported-field-types/keyword/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Supported field types"
has_children: false
layout: "default"
nav_order: 46
parent: "String field types"
---
# Keyword field type
**Introduced 1.0**
{: .label .label-purple }

A keyword field type contains a string that is not analyzed. It allows only exact, case-sensitive matches.

By default, keyword fields are both indexed (because `index` is enabled) and stored on disk (because `doc_values` is enabled). To reduce disk space, you can specify not to index keyword fields by setting `index` to `false`.

If you need to use a field for full-text search, map it as [`text`](../text/index.md) instead.
{: .note }

## Example

The following query creates a mapping with a keyword field. Setting `index` to `false` specifies to store the `genre` field on disk and to retrieve it using `doc_values`:

```json
PUT movies
{
  "mappings" : {
    "properties" : {
      "genre" : {
        "type" :  "keyword",
        "index" : false
      }
    }
  }
}
```

## Parameters

The following table lists the parameters accepted by keyword field types. All parameters are optional.

Parameter | Description
:--- | :---
`boost` | A floating-point value that specifies the weight of this field toward the relevance score. Values above 1.0 increase the field's relevance. Values between 0.0 and 1.0 decrease the field's relevance. Default is 1.0.
`doc_values` | A Boolean value that specifies whether the field should be stored on disk so that it can be used for aggregations, sorting, or scripting. Default is `true`.
`eager_global_ordinals` | Specifies whether global ordinals should be loaded eagerly on refresh. If the field is often used for aggregations, this parameter should be set to `true`. Default is `false`.
`fields` | To index the same string in several ways (for example, as a keyword and text), provide the fields parameter. You can specify one version of the field to be used for search and another to be used for sorting and aggregations.
`ignore_above` | Any string longer than this integer value should not be indexed. Default is 2147483647. Default dynamic mapping creates a keyword subfield for which `ignore_above` is set to 256.
`index` | A Boolean value that specifies whether the field should be searchable. Default is `true`. To reduce disk space, set `index` to `false`.
`index_options` | Information to be stored in the index that will be considered when calculating relevance scores. Can be set to `freqs` for term frequency. Default is `docs`.
`meta` | Accepts metadata for this field.
[`normalizer`](../../../analyzers/normalizers/index.md) | Specifies how to preprocess this field before indexing (for example, make it lowercase). Default is `null` (no preprocessing).
`norms` | A Boolean value that specifies whether the field length should be used when calculating relevance scores. Default is `false`.
[`null_value`](../index.md#null-value) | A value to be used in place of `null`. Must be of the same type as the field. If this parameter is not specified, the field is treated as missing when its value is `null`. Default is `null`.
`similarity` | The ranking algorithm for calculating relevance scores. Default is `BM25`.
`split_queries_on_whitespace` | A Boolean value that specifies whether full-text queries should be split on white space. Default is `false`.
`store` | A Boolean value that specifies whether the field value should be stored and can be retrieved separately from the `_source` field. Default is `false`.
