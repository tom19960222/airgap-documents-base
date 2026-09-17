---
collection: "opensearch"
version: "2.19"
title: "Wildcard"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/supported-field-types/wildcard.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/supported-field-types/wildcard.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/supported-field-types/wildcard/"
canonical_url: "https://docs.opensearch.org/latest/mappings/supported-field-types/wildcard/"
canonical_route: "/mappings/supported-field-types/wildcard/"
redirect_from: ["/mappings/supported-field-types/wildcard/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Supported field types"
has_children: false
layout: "default"
nav_order: 62
parent: "String field types"
---
# Wildcard field type
**Introduced 2.15**
{: .label .label-purple }

A `wildcard` field is a variant of a `keyword` field designed for arbitrary substring and regular expression matching.

Use a `wildcard` field when your content consists of "strings of characters" and not "text". Examples include unstructured log lines and computer code.

The `wildcard` field type is indexed differently from the `keyword` field type. Whereas `keyword` fields write the original field value to the index, the `wildcard` field type splits the field value into substrings with a length that is less than or equal to 3 and writes the substrings to the index. For example, the string `test` is split into strings `t`, `te`, `tes`, `e`, `es`, and `est`.

At search time, required substrings from the query pattern are matched against the index to produce candidate documents, which are then filtered according to the pattern in the query. For example, for the search term `test`, OpenSearch performs an indexed search for `tes AND est`. If the search term contains less than three characters, OpenSearch uses character substrings that are one or two characters long. For each matching document, if the source value is `test`, then the document is returned in the results. This excludes false positive values like `nikola tesla felt alternating current was best`.

In general, exact match queries (like [`term`](../../../query-dsl/term/term/index.md) or [`terms`](../../../query-dsl/term/term/index.md) queries) perform less effectively on `wildcard` fields than on `keyword` fields, while [`wildcard`](../../../query-dsl/term/wildcard/index.md), [`prefix`](../../../query-dsl/term/prefix/index.md), and [`regexp`](../../../query-dsl/term/regexp/index.md) queries perform better on `wildcard` fields.
{: .tip}

## Example

Create a mapping with a `wildcard` field:

```json
PUT logs
{
  "mappings" : {
    "properties" : {
      "log_line" : {
        "type" :  "wildcard"
      }
    }
  }
}
```

## Parameters

The following table lists all parameters available for `wildcard` fields.

Parameter | Description
:--- | :---
`doc_values` | A Boolean value that specifies whether the field should be stored on disk so that it can be used for aggregations, sorting, or scripting. Default is `false`.
`ignore_above` | Any string longer than this integer value should not be indexed. Default is `2147483647`.
`normalizer` | The normalizer used to preprocess values for indexing and search. By default, no normalization occurs and the original value is used. You may use the `lowercase` normalizer to perform case-insentive matching on the field.
`null_value` | A value to be used in place of `null`. Must be of the same type as the field. If this parameter is not specified, then the field is treated as missing when its value is `null`. Default is `null`.
