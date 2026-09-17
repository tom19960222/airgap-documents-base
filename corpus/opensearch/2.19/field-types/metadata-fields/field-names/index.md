---
collection: "opensearch"
version: "2.19"
title: "Field names"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/metadata-fields/field-names.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/metadata-fields/field-names.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/metadata-fields/field-names/"
canonical_url: "https://docs.opensearch.org/latest/mappings/metadata-fields/field-names/"
canonical_route: "/mappings/metadata-fields/field-names/"
redirect_from: ["/mappings/metadata-fields/field-names/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 10
parent: "Metadata fields"
---
# Field names

The `_field_names` field indexes field names that contain non-null values. This enables the use of the `exists` query, which can identify documents that either have or do not have non-null values for a specified field.

However, `_field_names` only indexes field names when both `doc_values` and `norms` are disabled. If either `doc_values` or `norms` are enabled, then the `exists` query still functions but will not rely on the `_field_names` field.

## Mapping example

```json
{
    "mappings": {
       "_field_names": {
        "enabled": "true"
      },
    "properties": {
      },
      "title": {
        "type": "text",
        "doc_values": false,
        "norms": false
      },
      "description": {
        "type": "text",
        "doc_values": true,
        "norms": false
      },
      "price": {
        "type": "float",
        "doc_values": false,
        "norms": true
      }
    }
  }
}
```
