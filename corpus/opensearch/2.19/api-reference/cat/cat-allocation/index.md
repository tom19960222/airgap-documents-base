---
collection: "opensearch"
version: "2.19"
title: "CAT allocation"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/cat/cat-allocation.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/cat/cat-allocation.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/cat/cat-allocation/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/cat/cat-allocation/"
canonical_route: "/api-reference/cat/cat-allocation/"
redirect_from: ["/opensearch/rest-api/cat/cat-allocation/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
layout: "default"
nav_order: 5
parent: "CAT API"
---
# CAT allocation
**Introduced 1.0**
{: .label .label-purple }

The CAT allocation operation lists the allocation of disk space for indexes and the number of shards on each node.

<!-- spec_insert_start
api: cat.allocation
component: endpoints
-->
## Endpoints
```json
GET /_cat/allocation
GET /_cat/allocation/{node_id}
```
<!-- spec_insert_end -->

<!-- spec_insert_start
api: cat.allocation
component: query_parameters
columns: Parameter, Data type, Description, Default
include_deprecated: false
-->
## Query parameters

The following table lists the available query parameters. All query parameters are optional.

| Parameter | Data type | Description | Default |
| :--- | :--- | :--- | :--- |
| `bytes` | String | The units used to display byte values. <br> Valid values are: `b`, `kb`, `k`, `mb`, `m`, `gb`, `g`, `tb`, `t`, `pb`, and `p`. | N/A |
| `cluster_manager_timeout` | String | A timeout for connection to the cluster manager node. | N/A |
| `format` | String | A short version of the HTTP `Accept` header, such as `json` or `yaml`. | N/A |
| `h` | List | A comma-separated list of column names to display. | N/A |
| `help` | Boolean | Returns help information. | `false` |
| `local` | Boolean | Returns local information but does not retrieve the state from cluster-manager node. | `false` |
| `s` | List | A comma-separated list of column names or column aliases to sort by. | N/A |
| `v` | Boolean | Enables verbose mode, which displays column headers. | `false` |

<!-- spec_insert_end -->

## Example requests

```json
GET _cat/allocation?v
```

To limit the information to a specific node, add the node name after your query:

```json
GET _cat/allocation/<node_name>
```

If you want to get information for more than one node, separate the node names with commas:

```json
GET _cat/allocation/node_name_1,node_name_2,node_name_3
```

## Example response

The following response shows that eight shards are allocated to each of the two nodes available:

```json
shards | disk.indices | disk.used | disk.avail | disk.total | disk.percent host | ip          | node
  8    |   989.4kb    |   25.9gb  |   32.4gb   |   58.4gb   |   44 172.18.0.4   | 172.18.0.4  | odfe-node1
  8    |   962.4kb    |   25.9gb  |   32.4gb   |   58.4gb   |   44 172.18.0.3   | 172.18.0.3  | odfe-node2
```
