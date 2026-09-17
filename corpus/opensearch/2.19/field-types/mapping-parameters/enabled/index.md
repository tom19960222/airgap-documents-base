---
collection: "opensearch"
version: "2.19"
title: "Enabled"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/mapping-parameters/enabled.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/mapping-parameters/enabled.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/mapping-parameters/enabled/"
canonical_url: "https://docs.opensearch.org/latest/mappings/mapping-parameters/enabled/"
canonical_route: "/mappings/mapping-parameters/enabled/"
redirect_from: ["/mappings/mapping-parameters/enabled/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Mapping and field types"
has_children: false
has_toc: false
layout: "default"
nav_order: 40
parent: "Mapping parameters"
---
# Enabled

The `enabled` parameter allows you to control whether OpenSearch parses the contents of a field. This parameter can be applied to the top-level mapping definition and to object fields.

The `enabled` parameter accepts the following values.

Parameter | Description
:--- | :---
`true` | The field is parsed and indexed. Default is `true`.
`false` | The field is not parsed or indexed but is still retrievable from the `_source` field. When `enabled` is set to `false`, OpenSearch stores the field's value in the `_source` field but does not index or parse its contents. This can be useful for fields that you want to store but do not need to search, sort, or aggregate on.

---

## Example: Using the `enabled` parameter

In the following example request, the `session_data` field is disabled. OpenSearch stores its contents in the `_source` field but does not index or parse them:

```json
PUT my-index-002
{
  "mappings": {
    "properties": {
      "user_id": {
        "type": "keyword"
      },
      "last_updated": {
        "type": "date"
      },
      "session_data": {
        "type": "object",
        "enabled": false
      }
    }
  }
}
```
