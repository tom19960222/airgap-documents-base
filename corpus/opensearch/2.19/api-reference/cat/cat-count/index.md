---
collection: "opensearch"
version: "2.19"
title: "CAT count"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/cat/cat-count.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/cat/cat-count.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/cat/cat-count/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/cat/cat-count/"
canonical_route: "/api-reference/cat/cat-count/"
redirect_from: ["/opensearch/rest-api/cat/cat-count/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
layout: "default"
nav_order: 10
parent: "CAT API"
---
# CAT count
**Introduced 1.0**
{: .label .label-purple }

The CAT count operation lists the number of documents in your cluster.

<!-- spec_insert_start
api: cat.count
component: endpoints
-->
## Endpoints
```json
GET /_cat/count
GET /_cat/count/{index}
```
<!-- spec_insert_end -->

<!-- spec_insert_start
api: cat.count
component: query_parameters
columns: Parameter, Data type, Description, Default
include_deprecated: false
-->
## Query parameters

The following table lists the available query parameters. All query parameters are optional.

| Parameter | Data type | Description | Default |
| :--- | :--- | :--- | :--- |
| `format` | String | A short version of the `Accept` header, such as `json` or `yaml`. | N/A |
| `h` | List | A comma-separated list of column names to display. | N/A |
| `help` | Boolean | Returns help information. | `false` |
| `s` | List | A comma-separated list of column names or column aliases to sort by. | N/A |
| `v` | Boolean | Enables verbose mode, which displays column headers. | `false` |

<!-- spec_insert_end -->

## Example requests

```json
GET _cat/count?v
```

To see the number of documents in a specific index or alias, add the index or alias name after your query:

```json
GET _cat/count/<index_or_alias>?v
```

If you want to get information for more than one index or alias, separate the index or alias names with commas:

```json
GET _cat/count/index_or_alias_1,index_or_alias_2,index_or_alias_3
```

## Example response

The following response shows the overall document count as 1625:

```json
epoch      | timestamp | count
1624237738 | 01:08:58  | 1625
```
