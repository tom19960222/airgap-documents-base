---
collection: "opensearch"
version: "2.19"
title: "Binary"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/supported-field-types/binary.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/supported-field-types/binary.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/supported-field-types/binary/"
canonical_url: "https://docs.opensearch.org/latest/mappings/supported-field-types/binary/"
canonical_route: "/mappings/supported-field-types/binary/"
redirect_from: ["/opensearch/supported-field-types/binary/","/field-types/binary/","/mappings/supported-field-types/binary/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
layout: "default"
nav_order: 12
parent: "Supported field types"
---
# Binary field type
**Introduced 1.0**
{: .label .label-purple }

A binary field type contains a binary value in [Base64](https://en.wikipedia.org/wiki/Base64) encoding that is not searchable.

## Example

Create a mapping with a binary field:

```json
PUT testindex
{
  "mappings" : {
    "properties" :  {
      "binary_value" : {
        "type" : "binary"
      }
    }
  }
}
```

Index a document with a binary value:

```json
PUT testindex/_doc/1
{
  "binary_value" : "bGlkaHQtd29rfx4="
}
```

Use `=` as a padding character. Embedded newline characters are not allowed.
{: .note }

## Parameters

The following table lists the parameters accepted by binary field types. All parameters are optional.

Parameter | Description
:--- | :---
`doc_values` | A Boolean value that specifies whether the field should be stored on disk so that it can be used for aggregations, sorting, or scripting. Optional. Default is `false`.
`store` | A Boolean value that specifies whether the field value should be stored and can be retrieved separately from the _source field. Optional. Default is `false`.
