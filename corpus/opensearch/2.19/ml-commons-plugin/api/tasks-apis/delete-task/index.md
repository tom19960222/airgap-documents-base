---
collection: "opensearch"
version: "2.19"
title: "Delete task"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/tasks-apis/delete-task.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/tasks-apis/delete-task.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/tasks-apis/delete-task/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/tasks-apis/delete-task/"
canonical_route: "/ml-commons-plugin/api/tasks-apis/delete-task/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "ML Commons APIs"
layout: "default"
nav_order: 20
parent: "Tasks APIs"
---
# Delete a task

Deletes a task based on the `task_id`.

ML Commons does not check the task status when running the delete request. There is a risk that a currently running task could be deleted before the task completes. To check the status of a task, run `GET /_plugins/_ml/tasks/<task_id>` before task deletion.
{: .note}

### Endpoints

```json
DELETE /_plugins/_ml/tasks/<task_id>
```

#### Example request

```json
DELETE /_plugins/_ml/tasks/xQRYLX8BydmmU1x6nuD3
```

#### Example response

```json
{
  "_index" : ".plugins-ml-task",
  "_id" : "xQRYLX8BydmmU1x6nuD3",
  "_version" : 4,
  "result" : "deleted",
  "_shards" : {
    "total" : 2,
    "successful" : 2,
    "failed" : 0
  },
  "_seq_no" : 42,
  "_primary_term" : 7
}
```
