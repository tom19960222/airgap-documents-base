---
collection: "opensearch"
version: "2.19"
title: "Microsoft 365"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_security-analytics/log-types-reference/m365.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_security-analytics/log-types-reference/m365.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/security-analytics/log-types-reference/m365/"
canonical_url: "https://docs.opensearch.org/latest/security-analytics/log-types-reference/m365/"
canonical_route: "/security-analytics/log-types-reference/m365/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 55
parent: "Supported log types"
---
# Microsoft 365

The `m365` log type collects a range of data for Microsoft 365, such as the following:

- Records from call details
- Performance data
- SQL Server events
- Security events
- Access control activity

The following code snippet contains all the `raw_field` and `ecs` mappings for this log type:

```json
"mappings": [
    {
      "raw_field":"eventSource",
      "ecs":"rsa.misc.event_source"
    },
    {
      "raw_field":"eventName",
      "ecs":"rsa.misc.event_desc"
    },
    {
      "raw_field":"status",
      "ecs":"rsa.misc.status"
    },
    {
      "raw_field":"Payload",
      "ecs":"rsa.misc.payload_dst"
    }
  ]
```
