---
collection: "opensearch"
version: "2.19"
title: "CAT pending tasks"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/cat/cat-pending-tasks.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/cat/cat-pending-tasks.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/cat/cat-pending-tasks/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/cat/cat-pending-tasks/"
canonical_route: "/api-reference/cat/cat-pending-tasks/"
redirect_from: ["/opensearch/rest-api/cat/cat-pending-tasks/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
layout: "default"
nav_order: 45
parent: "CAT API"
---
# CAT pending tasks
**Introduced 1.0**
{: .label .label-purple }

The CAT pending tasks operation lists the progress of all pending tasks, including task priority and time in queue.

<!-- spec_insert_start
api: cat.pending_tasks
component: endpoints
-->
## Endpoints
```json
GET /_cat/pending_tasks
```
<!-- spec_insert_end -->

<!-- spec_insert_start
api: cat.pending_tasks
component: query_parameters
columns: Parameter, Data type, Description, Default
include_deprecated: false
-->
## Query parameters

The following table lists the available query parameters. All query parameters are optional.

| Parameter | Data type | Description | Default |
| :--- | :--- | :--- | :--- |
| `cluster_manager_timeout` | String | The amount of time allowed to establish a connection to the cluster manager node. | N/A |
| `format` | String | A short version of the `Accept` header, such as `json` or `yaml`. | N/A |
| `h` | List | A comma-separated list of column names to display. | N/A |
| `help` | Boolean | Returns help information. | `false` |
| `local` | Boolean | Returns local information but does not retrieve the state from the cluster manager node. | `false` |
| `s` | List | A comma-separated list of column names or column aliases to sort by. | N/A |
| `time` | String | Specifies the time units, for example, `5d` or `7h`. For more information, see [Supported units](../../units/index.md). <br> Valid values are: `nanos`, `micros`, `ms`, `s`, `m`, `h`, and `d`. | N/A |
| `v` | Boolean | Enables verbose mode, which displays column headers. | `false` |

<!-- spec_insert_end -->

## Example request

The following example request lists the progress of all pending node tasks:

```json
GET _cat/pending_tasks?v
```

## Example response

```json
insertOrder | timeInQueue | priority | source
  1786      |    1.8s     |  URGENT  | shard-started
```
