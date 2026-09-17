---
collection: "opensearch"
version: "2.19"
title: "Google Workspace"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_security-analytics/log-types-reference/gworkspace.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_security-analytics/log-types-reference/gworkspace.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/security-analytics/log-types-reference/gworkspace/"
canonical_url: "https://docs.opensearch.org/latest/security-analytics/log-types-reference/gworkspace/"
canonical_route: "/security-analytics/log-types-reference/gworkspace/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 45
parent: "Supported log types"
---
# Google Workspace

The `gworkspace` log type monitors Google Workspace log entries, such as the following:

- Admin actions
- Group and group membership actions
- Events related to logins

The following code snippet contains all the `raw_field` and `ecs` mappings for this log type:

```json
  "mappings": [
    {
      "raw_field":"eventSource",
      "ecs":"google_workspace.admin.service.name"
    },
    {
      "raw_field":"eventName",
      "ecs":"google_workspace.event.name"
    },
    {
      "raw_field":"new_value",
      "ecs":"google_workspace.admin.new_value"
    }
  ]
```
