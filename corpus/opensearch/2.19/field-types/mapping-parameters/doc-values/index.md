---
collection: "opensearch"
version: "2.19"
title: "Doc values"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/mapping-parameters/doc-values.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/mapping-parameters/doc-values.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/mapping-parameters/doc-values/"
canonical_url: "https://docs.opensearch.org/latest/mappings/mapping-parameters/doc-values/"
canonical_route: "/mappings/mapping-parameters/doc-values/"
redirect_from: ["/mappings/mapping-parameters/doc-values/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Mapping and field types"
has_children: false
has_toc: false
layout: "default"
nav_order: 25
parent: "Mapping parameters"
---
# doc_values

By default, OpenSearch indexes most fields for search purposes. The `doc_values ` parameter enables document-to-term lookups for operations such as sorting, aggregations, and scripting.

The `doc_values` parameter accepts the following options.

Option | Description
:--- | :---
`true` | Enables `doc_values` for the field. Default is `true`.
`false` | Disables `doc_values` for the field.

The `doc_values` parameter is not supported for use in text fields.

---

## Example: Creating an index with `doc_values` enabled and disabled

The following example request creates an index with `doc_values` enabled for one field and disabled for another:

```json
PUT my-index-001
{
  "mappings": {
    "properties": {
      "status_code": {
        "type": "keyword"
      },
      "session_id": {
        "type": "keyword",
        "doc_values": false
      }
    }
  }
}
```
