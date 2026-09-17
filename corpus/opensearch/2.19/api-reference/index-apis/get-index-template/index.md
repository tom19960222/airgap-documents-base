---
collection: "opensearch"
version: "2.19"
title: "Get index template"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/index-apis/get-index-template.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/index-apis/get-index-template.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/index-apis/get-index-template/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/index-apis/get-index-template/"
canonical_route: "/api-reference/index-apis/get-index-template/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 27
parent: "Index APIs"
---
# Get index template

The Get Index Template API returns information about one or more index templates.

## Endpoints

```json
GET /_index_template/<template-name>
```

## Query parameters

The following optional query parameters are supported.

Parameter | Type | Description
:--- | :--- | :---
`create` | Boolean | When true, the API cannot replace or update any existing index templates. Default is `false`.
`cluster_manager_timeout` | Time | The amount of time to wait for a connection to the cluster manager node. Default is `30s`.
`flat_settings` | Boolean | Whether to return settings in the flat form, which can improve readability, especially for heavily nested settings. For example, the flat form of "index": { "creation_date": "123456789" } is "index.creation_date": "123456789".

## Example requests

The following example request gets information about an index template by using a wildcard expression:

```json
GET /_index_template/h*
```

The following example request gets information about all index templates:

```json
GET /_index_template
```
