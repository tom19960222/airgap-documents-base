---
collection: "opensearch"
version: "2.19"
title: "Constant keyword"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/supported-field-types/constant-keyword.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/supported-field-types/constant-keyword.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/supported-field-types/constant-keyword/"
canonical_url: "https://docs.opensearch.org/latest/mappings/supported-field-types/constant-keyword/"
canonical_route: "/mappings/supported-field-types/constant-keyword/"
redirect_from: ["/mappings/supported-field-types/constant-keyword/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Supported field types"
has_children: false
layout: "default"
nav_order: 71
parent: "String field types"
---
# Constant keyword field type
**Introduced 2.14**
{: .label .label-purple }

A constant keyword field uses the same value for all documents in the index.

When a search request spans multiple indexes, you can filter on a constant keyword field to match documents from indexes with the given constant value but not from indexes with a different value.

## Example

The following query creates a mapping with a constant keyword field:

```json
PUT romcom_movies
{
  "mappings" : {
    "properties" : {
      "genre" : {
        "type": "constant_keyword",
        "value" : "Romantic comedy"
      }
    }
  }
}
```

## Parameters

The following table lists the parameters accepted by constant keyword field types. All values are required.

Parameter | Description
:--- | :---
`value` | The string field value for all documents in the index.
