---
collection: "opensearch"
version: "2.19"
title: "NetFlow"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_security-analytics/log-types-reference/netflow.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_security-analytics/log-types-reference/netflow.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/security-analytics/log-types-reference/netflow/"
canonical_url: "https://docs.opensearch.org/latest/security-analytics/log-types-reference/netflow/"
canonical_route: "/security-analytics/log-types-reference/netflow/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 60
parent: "Supported log types"
---
# NetFlow

The `netflow` log type records NetFlow events used during integration testing.

The following code snippet contains all the `raw_field` and `ecs` mappings for this log type:

```json
"mappings": [
    {
      "raw_field":"netflow.source_ipv4_address",
      "ecs":"source.ip"
    },
    {
      "raw_field":"netflow.source_transport_port",
      "ecs":"source.port"
    },
    {
      "raw_field":"netflow.destination_ipv4_address",
      "ecs":"destination.ip"
    },
    {
      "raw_field":"netflow.destination_transport_port",
      "ecs":"destination.port"
    },
    {
      "raw_field":"http.request.method",
      "ecs":"http.request.method"
    },
    {
      "raw_field":"http.response.status_code",
      "ecs":"http.response.status_code"
    },
    {
      "raw_field":"timestamp",
      "ecs":"timestamp"
    }
  ]
```
