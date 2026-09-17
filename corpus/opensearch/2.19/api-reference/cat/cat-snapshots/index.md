---
collection: "opensearch"
version: "2.19"
title: "CAT snapshots"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/cat/cat-snapshots.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/cat/cat-snapshots.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/cat/cat-snapshots/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/cat/cat-snapshots/"
canonical_route: "/api-reference/cat/cat-snapshots/"
redirect_from: ["/opensearch/rest-api/cat/cat-snapshots/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
layout: "default"
nav_order: 65
parent: "CAT API"
---
# CAT snapshots
**Introduced 1.0**
{: .label .label-purple }

The CAT snapshots operation lists all snapshots for a repository.

<!-- spec_insert_start
api: cat.snapshots
component: endpoints
-->
## Endpoints
```json
GET /_cat/snapshots
GET /_cat/snapshots/{repository}
```
<!-- spec_insert_end -->

<!-- spec_insert_start
api: cat.snapshots
component: query_parameters
columns: Parameter, Data type, Description, Default
include_deprecated: false
-->
## Query parameters

The following table lists the available query parameters.

| Parameter | Data type | Description | Default |
| :--- | :--- | :--- | :--- |
| `repository` | List or String | **(Required)** A comma-separated list of snapshot repositories used to limit the request. Accepts wildcard expressions. `_all` returns all repositories. If any repository fails during the request, OpenSearch returns an error. | N/A |
| `cluster_manager_timeout` | String | The amount of time allowed to establish a connection to the cluster manager node. | N/A |
| `format` | String | A short version of the `Accept` header, such as `json` or `yaml`. | N/A |
| `h` | List | A comma-separated list of column names to display. | N/A |
| `help` | Boolean | Returns help information. | `false` |
| `ignore_unavailable` | Boolean | When `true`, the response does not include information from unavailable snapshots. | `false` |
| `s` | List | A comma-separated list of column names or column aliases to sort by. | N/A |
| `time` | String | Specifies the time units, for example, `5d` or `7h`. For more information, see [Supported units](../../units/index.md). <br> Valid values are: `nanos`, `micros`, `ms`, `s`, `m`, `h`, and `d`. | N/A |
| `v` | Boolean | Enables verbose mode, which displays column headers. | `false` |

<!-- spec_insert_end -->

## Example request

The following example request lists all snapshots:

```
GET _cat/snapshots?v
```

## Example response

```json
index | shard | prirep | state   | docs | store | ip |       | node
plugins | 0   |   p    | STARTED |   0  |  208b | 172.18.0.4 | odfe-node1
plugins | 0   |   r    | STARTED |   0  |  208b | 172.18.0.3 |  odfe-node2
```
