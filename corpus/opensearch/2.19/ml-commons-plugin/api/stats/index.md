---
collection: "opensearch"
version: "2.19"
title: "Stats"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/stats.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/stats.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/stats/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/stats/"
canonical_route: "/ml-commons-plugin/api/stats/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 50
parent: "ML Commons APIs"
---
# Stats

Gets statistics related to the number of tasks.

## Endpoints

```json
GET /_plugins/_ml/stats
GET /_plugins/_ml/stats/<stat>
GET /_plugins/_ml/<nodeId>/stats/
GET /_plugins/_ml/<nodeId>/stats/<stat>
```

#### Example request: Get all stats for all nodes

```json
GET /_plugins/_ml/stats
```

#### Example response

```json
{
  "zbduvgCCSOeu6cfbQhTpnQ" : {
    "ml_executing_task_count" : 0
  },
  "54xOe0w8Qjyze00UuLDfdA" : {
    "ml_executing_task_count" : 0
  },
  "UJiykI7bTKiCpR-rqLYHyw" : {
    "ml_executing_task_count" : 0
  },
  "zj2_NgIbTP-StNlGZJlxdg" : {
    "ml_executing_task_count" : 0
  },
  "jjqFrlW7QWmni1tRnb_7Dg" : {
    "ml_executing_task_count" : 0
  },
  "3pSSjl5PSVqzv5-hBdFqyA" : {
    "ml_executing_task_count" : 0
  },
  "A_IiqoloTDK01uZvCjREaA" : {
    "ml_executing_task_count" : 0
  }
}
```

#### Example request: Get all stats for a specific node

```json
GET /_plugins/_ml/<nodeId>/stats/
```

#### Example request: Get a specified stat for a specific node

```json
GET /_plugins/_ml/<nodeId>/stats/<stat>
```

#### Example request: Get a specified stat for all nodes

```json
GET /_plugins/_ml/stats/<stat>
```
