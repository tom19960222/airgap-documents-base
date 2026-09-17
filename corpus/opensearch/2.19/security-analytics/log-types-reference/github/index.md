---
collection: "opensearch"
version: "2.19"
title: "GitHub"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_security-analytics/log-types-reference/github.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_security-analytics/log-types-reference/github.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/security-analytics/log-types-reference/github/"
canonical_url: "https://docs.opensearch.org/latest/security-analytics/log-types-reference/github/"
canonical_route: "/security-analytics/log-types-reference/github/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 40
parent: "Supported log types"
---
# GitHub

The `github` log type monitors workflows created by [GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions).

The following code snippet contains all the `raw_field` and `ecs` mappings for this log type:

```json
  "mappings": [
    {
      "raw_field":"action",
      "ecs":"github.action"
    }
  ]
```
