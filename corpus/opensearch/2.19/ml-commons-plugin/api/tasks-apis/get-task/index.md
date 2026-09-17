---
collection: "opensearch"
version: "2.19"
title: "Get task"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/tasks-apis/get-task.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/tasks-apis/get-task.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/tasks-apis/get-task/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/tasks-apis/get-task/"
canonical_route: "/ml-commons-plugin/api/tasks-apis/get-task/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "ML Commons APIs"
layout: "default"
nav_order: 10
parent: "Tasks APIs"
---
# Get task

You can retrieve information about a task using the `task_id`.

## Endpoints

```json
GET /_plugins/_ml/tasks/<task_id>
```

#### Example request

```json
GET /_plugins/_ml/tasks/MsBi1YsB0jLkkocYjD5f
```

#### Example response

The response includes information about the task.

```json
{
  "model_id" : "l7lamX8BO5w8y8Ra2oty",
  "task_type" : "TRAINING",
  "function_name" : "KMEANS",
  "state" : "COMPLETED",
  "input_type" : "SEARCH_QUERY",
  "worker_node" : "54xOe0w8Qjyze00UuLDfdA",
  "create_time" : 1647545342556,
  "last_update_time" : 1647545342587,
  "is_async" : true
}
```
