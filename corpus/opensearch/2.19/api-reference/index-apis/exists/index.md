---
collection: "opensearch"
version: "2.19"
title: "Index exists"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/index-apis/exists.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/index-apis/exists.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/index-apis/exists/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/index-apis/exists/"
canonical_route: "/api-reference/index-apis/exists/"
redirect_from: ["/opensearch/rest-api/index-apis/exists/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 19
parent: "Index APIs"
---
# Index exists
**Introduced 1.0**
{: .label .label-purple }

The index exists API operation returns whether or not an index already exists.

## Endpoints

```json
HEAD /<index-name>
```

## Query parameters

All parameters are optional.

Parameter | Type | Description
:--- | :--- | :---
allow_no_indices | Boolean | Whether to ignore wildcards that don't match any indexes. Default is `true`.
expand_wildcards | String | Expands wildcard expressions to different indexes. Combine multiple values with commas. Available values are all (match all indexes), open (match open indexes), closed (match closed indexes), hidden (match hidden indexes), and none (do not accept wildcard expressions). Default is `open`.
flat_settings | Boolean | Whether to return settings in the flat form, which can improve readability, especially for heavily nested settings. For example, the flat form of "index": { "creation_date": "123456789" } is "index.creation_date": "123456789".
include_defaults | Boolean | Whether to include default settings as part of the response. This parameter is useful for identifying the names and current values of settings you want to update.
ignore_unavailable | Boolean | If true, OpenSearch does not search for missing or closed indexes. Default is `false`.
local | Boolean | Whether to return information from only the local node instead of from the cluster manager node. Default is `false`.

## Example request

```json
HEAD /sample-index
```

## Example response

The index exists API operation returns only one of two possible response codes: `200` -- the index exists, and `404` -- the index does not exist.
