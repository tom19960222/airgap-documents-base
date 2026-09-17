---
collection: "opensearch"
version: "2.19"
title: "CAT tasks"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/cat/cat-tasks.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/cat/cat-tasks.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/cat/cat-tasks/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/cat/cat-tasks/"
canonical_route: "/api-reference/cat/cat-tasks/"
redirect_from: ["/opensearch/rest-api/cat/cat-tasks/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
layout: "default"
nav_order: 70
parent: "CAT API"
---
# CAT tasks
**Introduced 1.0**
{: .label .label-purple }

The CAT tasks operation lists the progress of all tasks currently running on your cluster.

<!-- spec_insert_start
api: cat.tasks
component: endpoints
-->
## Endpoints
```json
GET /_cat/tasks
```
<!-- spec_insert_end -->

<!-- spec_insert_start
api: cat.tasks
component: query_parameters
columns: Parameter, Data type, Description, Default
include_deprecated: false
-->
## Query parameters

The following table lists the available query parameters. All query parameters are optional.

| Parameter | Data type | Description | Default |
| :--- | :--- | :--- | :--- |
| `actions` | List | The task action names used to limit the response. | N/A |
| `detailed` | Boolean | If `true`, the response includes detailed information about shard recoveries. | `false` |
| `format` | String | A short version of the `Accept` header, such as `json` or `yaml`. | N/A |
| `h` | List | A comma-separated list of column names to display. | N/A |
| `help` | Boolean | Returns help information. | `false` |
| `nodes` | List | A comma-separated list of node IDs or names used to limit the returned information.  Use `_local` to return information from the node to which you're connecting, specify a specific node from which to get information, or keep the parameter empty to get information from all nodes. | N/A |
| `parent_task_id` | String | The parent task identifier, which is used to limit the response. | N/A |
| `s` | List | A comma-separated list of column names or column aliases to sort by. | N/A |
| `time` | String | Specifies the time units, for example, `5d` or `7h`. For more information, see [Supported units](../../units/index.md). <br> Valid values are: `nanos`, `micros`, `ms`, `s`, `m`, `h`, and `d`. | N/A |
| `v` | Boolean | Enables verbose mode, which displays column headers. | `false` |

<!-- spec_insert_end -->

## Example request

The following example request lists all tasks in progress:

```
GET _cat/tasks?v
```

## Example response

```json
action | task_id | parent_task_id | type | start_time | timestamp | running_time | ip | node
cluster:monitor/tasks/lists | 1vo54NuxSxOrbPEYdkSF0w:168062 | - | transport | 1624337809471 | 04:56:49 | 489.5ms | 172.18.0.4 | odfe-node1
```
