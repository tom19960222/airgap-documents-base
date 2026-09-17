---
collection: "opensearch"
version: "2.19"
title: "WAF"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_security-analytics/log-types-reference/waf.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_security-analytics/log-types-reference/waf.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/security-analytics/log-types-reference/waf/"
canonical_url: "https://docs.opensearch.org/latest/security-analytics/log-types-reference/waf/"
canonical_route: "/security-analytics/log-types-reference/waf/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 95
parent: "Supported log types"
---
The `waf` log type monitors web application firewall (WAF) logs. The role of a WAF is to monitor and filter HTTP traffic flowing between a web application and the internet. A WAF prevents common security attacks, such as cross-site scripting (XSS) and SQL injection (SQLi).

The following code snippet contains all the `raw_field` and `ecs` mappings for this log type:

```json
  "mappings": [
    {
      "raw_field":"cs-method",
      "ecs":"waf.request.method"
    },
    {
      "raw_field":"httpRequest.httpMethod",
      "ecs":"waf.request.method"
    },
    {
      "raw_field":"cs-uri-query",
      "ecs":"waf.request.uri_query"
    },
    {
      "raw_field":"httpRequest.uri",
      "ecs":"waf.request.uri_query"
    },
    {
      "raw_field":"httpRequest.args",
      "ecs":"waf.request.uri_query"
    },
    {
      "raw_field":"cs-user-agent",
      "ecs":"waf.request.headers.user_agent"
    },
    {
      "raw_field":"httpRequest.headers",
      "ecs":"waf.request.headers"
    },
    {
      "raw_field":"sc-status",
      "ecs":"waf.response.code"
    },
    {
      "raw_field":"responseCodeSent",
      "ecs":"waf.response.code"
    },
    {
      "raw_field":"timestamp",
      "ecs":"timestamp"
    },
    {
      "raw_field":"httpRequest.headers.value",
      "ecs":"waf.request.headers.value"
    },
    {
      "raw_field":"httpRequest.headers.name",
      "ecs":"waf.request.headers.name"
    }
  ]
```
