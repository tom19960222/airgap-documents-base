---
collection: "opensearch"
version: "2.19"
title: "Get settings"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/index-apis/get-settings.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/index-apis/get-settings.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/index-apis/get-settings/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/index-apis/get-settings/"
canonical_route: "/api-reference/index-apis/get-settings/"
redirect_from: ["/opensearch/rest-api/index-apis/get-settings/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 45
parent: "Index APIs"
---
# Get settings
**Introduced 1.0**
{: .label .label-purple }

The get settings API operation returns all the settings in your index.

## Endpoints

```json
GET /_settings
GET /<target-index>/_settings
GET /<target-index>/_settings/<setting>
```

## Path parameters

Parameter | Data type | Description
:--- | :--- | :---
&lt;target-index&gt; | String | The index to get settings from. Can be a comma-separated list to get settings from multiple indexes, or use `_all` to return settings from all indexes within the cluster.
&lt;setting&gt; | String | Filter to return specific settings.

## Query parameters

All get settings parameters are optional.

Parameter | Data type | Description
:--- | :--- | :---
allow_no_indices | Boolean | Whether to ignore wildcards that don’t match any indexes. Default is `true`.
expand_wildcards | String | Expands wildcard expressions to different indexes. Combine multiple values with commas. Available values are `all` (match all indexes), `open` (match open indexes), `closed` (match closed indexes), `hidden` (match hidden indexes), and `none` (do not accept wildcard expressions), which must be used with `open`, `closed`, or both. Default is `open`.
flat_settings | Boolean | Whether to return settings in the flat form, which can improve readability, especially for heavily nested settings. For example, the flat form of “index”: { “creation_date”: “123456789” } is “index.creation_date”: “123456789”.
include_defaults | Boolean | Whether to include default settings, including settings used within OpenSearch plugins, in the response. Default is `false`.
ignore_unavailable | Boolean | If true, OpenSearch does not include missing or closed indexes in the response.
local | Boolean | Whether to return information from the local node only instead of the cluster manager node. Default is `false`.
cluster_manager_timeout | Time | How long to wait for a connection to the cluster manager node. Default is `30s`.

## Example request

```json
GET /sample-index1/_settings
```

## Example response

```json
{
  "sample-index1": {
    "settings": {
      "index": {
        "creation_date": "1622672553417",
        "number_of_shards": "1",
        "number_of_replicas": "1",
        "uuid": "GMEA0_TkSaamrnJSzNLzwg",
        "version": {
          "created": "135217827",
          "upgraded": "135238227"
        },
        "provided_name": "sample-index1"
      }
    }
  }
}
```
