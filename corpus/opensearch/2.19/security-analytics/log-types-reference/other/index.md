---
collection: "opensearch"
version: "2.19"
title: "Other log type mappings"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_security-analytics/log-types-reference/other.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_security-analytics/log-types-reference/other.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/security-analytics/log-types-reference/other/"
canonical_url: "https://docs.opensearch.org/latest/security-analytics/log-types-reference/other/"
canonical_route: "/security-analytics/log-types-reference/other/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 110
parent: "Supported log types"
---
# Other log type mappings

Security Analytics supports field mappings that are not specific to a single service or system. These mapping types are separated into the following categories:

- Application: Records application logs.
- Advanced Persistent Threat (APT): Records logs commonly associated with APT attacks.
- Compliance: Records logs related to compliance.
- macOS: Records event logs when using a Mac device to access a network.
- Proxy: Records logs related to proxy events.
- Web: Records logs related to network access from the web.

Each log type contains the same field mappings, as shown in the following code snippet:

```json
  "mappings": [
    {
      "raw_field":"record_type",
      "ecs":"dns.answers.type"
    },
    {
      "raw_field":"query",
      "ecs":"dns.question.name"
    },
    {
      "raw_field":"parent_domain",
      "ecs":"dns.question.registered_domain"
    },
    {
      "raw_field":"creationTime",
      "ecs":"timestamp"
    }
  ]
```
