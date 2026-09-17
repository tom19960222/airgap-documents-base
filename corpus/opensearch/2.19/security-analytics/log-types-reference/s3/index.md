---
collection: "opensearch"
version: "2.19"
title: "Amazon S3"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_security-analytics/log-types-reference/s3.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_security-analytics/log-types-reference/s3.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/security-analytics/log-types-reference/s3/"
canonical_url: "https://docs.opensearch.org/latest/security-analytics/log-types-reference/s3/"
canonical_route: "/security-analytics/log-types-reference/s3/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 24
parent: "Supported log types"
---
# Amazon S3

The `s3` log type tracks network requests for access to Amazon S3 buckets.

The following code snippet contains all the `raw_field` and `ecs` mappings for this log type:

```json
  "mappings": [
    {
      "raw_field":"eventName",
      "ecs":"aws.cloudtrail.event_name"
    },
    {
      "raw_field":"eventSource",
      "ecs":"aws.cloudtrail.event_source"
    },
    {
      "raw_field":"eventTime",
      "ecs":"timestamp"
    }
  ]
```
