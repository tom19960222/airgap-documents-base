---
collection: "opensearch"
version: "2.19"
title: "CAT field data"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/cat/cat-field-data.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/cat/cat-field-data.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/cat/cat-field-data/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/cat/cat-field-data/"
canonical_route: "/api-reference/cat/cat-field-data/"
redirect_from: ["/opensearch/rest-api/cat/cat-field-data/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
layout: "default"
nav_order: 15
parent: "CAT API"
---
# CAT Field Data
**Introduced 1.0**
{: .label .label-purple }

The CAT Field Data operation lists the memory size used by each field per node.

<!-- spec_insert_start
api: cat.fielddata
component: endpoints
-->
## Endpoints
```json
GET /_cat/fielddata
GET /_cat/fielddata/{fields}
```
<!-- spec_insert_end -->

<!-- spec_insert_start
api: cat.fielddata
component: query_parameters
columns: Parameter, Data type, Description, Default
include_deprecated: false
-->
## Query parameters

The following table lists the available query parameters. All query parameters are optional.

| Parameter | Data type | Description | Default |
| :--- | :--- | :--- | :--- |
| `bytes` | String | The units used to display byte values. <br> Valid values are: `b`, `kb`, `k`, `mb`, `m`, `gb`, `g`, `tb`, `t`, `pb`, and `p`. | N/A |
| `fields` | List or String | A comma-separated list of fields used to limit the amount of returned information. | N/A |
| `format` | String | A short version of the `Accept` header, such as `json` or `yaml`. | N/A |
| `h` | List | A comma-separated list of column names to display. | N/A |
| `help` | Boolean | Returns help information. | `false` |
| `s` | List | A comma-separated list of column names or column aliases to sort by. | N/A |
| `v` | Boolean | Enables verbose mode, which displays column headers. | `false` |

<!-- spec_insert_end -->

## Example requests

```json
GET _cat/fielddata?v
```

To limit the information to a specific field, add the field name after your query:

```json
GET _cat/fielddata/<field_name>?v
```

If you want to get information for more than one field, separate the field names with commas:

```json
GET _cat/fielddata/field_name_1,field_name_2,field_name_3
```

## Example response

The following response shows the memory size for all fields as 284 bytes:

```json
id                     host       ip         node       field size
1vo54NuxSxOrbPEYdkSF0w 172.18.0.4 172.18.0.4 odfe-node1 _id   284b
ZaIkkUd4TEiAihqJGkp5CA 172.18.0.3 172.18.0.3 odfe-node2 _id   284b
```
