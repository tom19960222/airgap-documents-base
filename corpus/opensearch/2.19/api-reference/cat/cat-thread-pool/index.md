---
collection: "opensearch"
version: "2.19"
title: "CAT thread pool"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/cat/cat-thread-pool.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/cat/cat-thread-pool.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/cat/cat-thread-pool/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/cat/cat-thread-pool/"
canonical_route: "/api-reference/cat/cat-thread-pool/"
redirect_from: ["/opensearch/rest-api/cat/cat-thread-pool/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
layout: "default"
nav_order: 75
parent: "CAT API"
---
# CAT thread pool
**Introduced 1.0**
{: .label .label-purple }

The CAT thread pool operation lists the active, queued, and rejected threads of different thread pools on each node.

<!-- spec_insert_start
api: cat.thread_pool
component: endpoints
-->
## Endpoints
```json
GET /_cat/thread_pool
GET /_cat/thread_pool/{thread_pool_patterns}
```
<!-- spec_insert_end -->

<!-- spec_insert_start
api: cat.thread_pool
component: query_parameters
columns: Parameter, Data type, Description, Default
include_deprecated: false
-->
## Query parameters

The following table lists the available query parameters. All query parameters are optional.

| Parameter | Data type | Description | Default |
| :--- | :--- | :--- | :--- |
| `cluster_manager_timeout` | String | A timeout for connection to the cluster manager node. | N/A |
| `format` | String | A short version of the `Accept` header, such as `json` or `yaml`. | N/A |
| `h` | List | A comma-separated list of column names to display. | N/A |
| `help` | Boolean | Returns help information. | `false` |
| `local` | Boolean | Returns local information but does not retrieve the state from the cluster manager node. | `false` |
| `s` | List | A comma-separated list of column names or column aliases to sort by. | N/A |
| `size` | Integer | The multiplier in which to display values. | N/A |
| `v` | Boolean | Enables verbose mode, which displays column headers. | `false` |

<!-- spec_insert_end -->

## Example requests

The following example request gives information about thread pools on all nodes:

```json
GET _cat/thread_pool?v
```

If you want to get information for more than one thread pool, separate the thread pool names with commas:

```json
GET _cat/thread_pool/thread_pool_name_1,thread_pool_name_2,thread_pool_name_3
```

If you want to limit the information to a specific thread pool, add the thread pool name after your query:

```json
GET _cat/thread_pool/<thread_pool_name>?v
```

## Example response

```json
node_name  name                      active queue rejected
odfe-node2 ad-batch-task-threadpool    0     0        0
odfe-node2 ad-threadpool               0     0        0
odfe-node2 analyze                     0     0        0s
```
