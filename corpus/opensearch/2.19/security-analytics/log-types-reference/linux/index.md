---
collection: "opensearch"
version: "2.19"
title: "Linux"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_security-analytics/log-types-reference/linux.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_security-analytics/log-types-reference/linux.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/security-analytics/log-types-reference/linux/"
canonical_url: "https://docs.opensearch.org/latest/security-analytics/log-types-reference/linux/"
canonical_route: "/security-analytics/log-types-reference/linux/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 50
parent: "Supported log types"
---
# Linux

The `linux` log type records Linux syslog events.

The following code snippet contains all the `raw_field` and `ecs` mappings for this log type:

```json
  "mappings": [
    {
      "raw_field":"name",
      "ecs":"user.filesystem.name"
    },
    {
      "raw_field":"a0",
      "ecs":"auditd.log.a0"
    },
    {
      "raw_field":"comm",
      "ecs":"auditd.log.comm"
    },
    {
      "raw_field":"exe",
      "ecs":"auditd.log.exe"
    },
    {
      "raw_field":"uid",
      "ecs":"auditd.log.uid"
    },
    {
      "raw_field":"USER",
      "ecs":"system.auth.user"
    },
    {
      "raw_field":"User",
      "ecs":"system.auth.user"
    },
    {
      "raw_field":"Image",
      "ecs":"process.exe"
    },
    {
      "raw_field":"DestinationHostname",
      "ecs":"rsa.web.remote_domain"
    },
    {
      "raw_field":"CommandLine",
      "ecs":"process.command_line"
    },
    {
      "raw_field":"ParentImage",
      "ecs":"process.parent.executable"
    },
    {
      "raw_field":"CurrentDirectory",
      "ecs":"process.working_directory"
    },
    {
      "raw_field":"LogonId",
      "ecs":"process.real_user.id"
    },
    {
      "raw_field":"creationTime",
      "ecs":"timestamp"
    }
  ]
```
