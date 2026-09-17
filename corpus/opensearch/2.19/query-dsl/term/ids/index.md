---
collection: "opensearch"
version: "2.19"
title: "IDs"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_query-dsl/term/ids.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_query-dsl/term/ids.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/query-dsl/term/ids/"
canonical_url: "https://docs.opensearch.org/latest/query-dsl/term/ids/"
canonical_route: "/query-dsl/term/ids/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 30
parent: "Term-level queries"
---
# IDs query

Use the `ids` query to search for documents with one or more specific document ID values in the `_id` field. For example, the following query requests documents with the IDs `34229` and `91296`:

```json
GET shakespeare/_search
{
  "query": {
    "ids": {
      "values": [
        34229,
        91296
      ]
    }
  }
}
```

## Parameters

The query accepts the following parameter.

Parameter | Data type | Description
:--- | :--- | :---
`values` | Array of strings | The document IDs to search for. Required.
`boost` | Floating-point | A floating-point value that specifies the weight of this field toward the relevance score. Values above 1.0 increase the field’s relevance. Values between 0.0 and 1.0 decrease the field’s relevance. Default is 1.0.
