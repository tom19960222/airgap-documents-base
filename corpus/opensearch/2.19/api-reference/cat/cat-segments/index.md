---
collection: "opensearch"
version: "2.19"
title: "CAT segments"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/cat/cat-segments.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/cat/cat-segments.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/cat/cat-segments/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/cat/cat-segments/"
canonical_route: "/api-reference/cat/cat-segments/"
redirect_from: ["/opensearch/rest-api/cat/cat-segments/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
layout: "default"
nav_order: 55
parent: "CAT API"
---
# CAT segments
**Introduced 1.0**
{: .label .label-purple }

The cat segments operation lists Lucene segment-level information for each index.

<!-- spec_insert_start
api: cat.segments
component: endpoints
-->
## Endpoints
```json
GET /_cat/segments
GET /_cat/segments/{index}
```
<!-- spec_insert_end -->

<!-- spec_insert_start
api: cat.segments
component: query_parameters
columns: Parameter, Data type, Description, Default
include_deprecated: false
-->
## Query parameters

The following table lists the available query parameters. All query parameters are optional.

| Parameter | Data type | Description | Default |
| :--- | :--- | :--- | :--- |
| `bytes` | String | The units used to display byte values. <br> Valid values are: `b`, `kb`, `k`, `mb`, `m`, `gb`, `g`, `tb`, `t`, `pb`, and `p`. | N/A |
| `cluster_manager_timeout` | String | The amount of time allowed to establish a connection to the cluster manager node. | N/A |
| `format` | String | A short version of the `Accept` header, such as `json` or `yaml`. | N/A |
| `h` | List | A comma-separated list of column names to display. | N/A |
| `help` | Boolean | Returns help information. | `false` |
| `s` | List | A comma-separated list of column names or column aliases to sort by. | N/A |
| `v` | Boolean | Enables verbose mode, which displays column headers. | `false` |

<!-- spec_insert_end -->

## Example requests

```json
GET _cat/segments?v
```

To see only the information about segments of a specific index, add the index name after your query.

```json
GET _cat/segments/<index>?v
```

If you want to get information for more than one index, separate the indexes with commas:

```json
GET _cat/segments/index1,index2,index3
```

## Example response

```json
index | shard | prirep | ip | segment | generation | docs.count | docs.deleted | size | size.memory | committed | searchable | version | compound
movies | 0 | p | 172.18.0.4 | _0 | 0 | 1 | 0 | 3.5kb | 1364 | true | true | 8.7.0 | true
movies | 0 | r | 172.18.0.3 | _0 | 0 | 1 | 0 | 3.5kb | 1364 | true | true | 8.7.0 | true
```

## Limiting the response size

To limit the number of indexes returned, configure the `cat.segments.response.limit.number_of_indices` setting. For more information, see [Cluster-level CAT response limit settings](../../../install-and-configure/configuring-opensearch/cluster-settings/index.md#cluster-level-cat-response-limit-settings).
