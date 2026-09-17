---
collection: "opensearch"
version: "2.19"
title: "CAT templates"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/cat/cat-templates.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/cat/cat-templates.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/cat/cat-templates/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/cat/cat-templates/"
canonical_route: "/api-reference/cat/cat-templates/"
redirect_from: ["/opensearch/rest-api/cat/cat-templates/"]
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
# CAT templates
**Introduced 1.0**
{: .label .label-purple }

The CAT templates operation lists the names, patterns, order numbers, and version numbers of index templates.

<!-- spec_insert_start
api: cat.templates
component: endpoints
-->
## Endpoints
```json
GET /_cat/templates
GET /_cat/templates/{name}
```
<!-- spec_insert_end -->

<!-- spec_insert_start
api: cat.templates
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
| `v` | Boolean | Enables verbose mode, which displays column headers. | `false` |

<!-- spec_insert_end -->

## Example requests

The following example request returns information about all templates:

```json
GET _cat/templates?v
```

If you want to get information for a specific template or pattern:

```json
GET _cat/templates/<template_name_or_pattern>
```

## Example response

```
name | index_patterns order version composed_of
tenant_template | [opensearch-dashboards*] | 0  |
```

To learn more about index templates, see [Index templates](../../../im-plugin/index-templates/index.md).
