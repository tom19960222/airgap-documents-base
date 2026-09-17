---
collection: "opensearch"
version: "2.19"
title: "Delete index template"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/index-apis/delete-index-template.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/index-apis/delete-index-template.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/index-apis/delete-index-template/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/index-apis/delete-index-template/"
canonical_route: "/api-reference/index-apis/delete-index-template/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 28
parent: "Index APIs"
---
# Delete index template

The Delete Index Template API deletes one or more index templates.

## Endpoints

```json
DELETE /_index_template/<template-name>
```

## Path parameters

Parameter | Type | Description
:--- | :--- | :---
`template-name` | String | The name of the index template. You can delete multiple templates in one request by separating the template names with commas. When multiple template names are used in the request, wildcards are not supported.

## Query parameters

The following optional query parameters are supported.

Parameter | Type | Description
:--- | :--- | :---
`cluster_manager_timeout` | Time | The amount of time to wait for a connection to the cluster manager node. Default is `30s`.
`timeout` | Time | The amount of time that the operation will wait for a response. Default is `30s`.
