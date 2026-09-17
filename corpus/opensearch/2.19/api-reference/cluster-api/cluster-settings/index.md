---
collection: "opensearch"
version: "2.19"
title: "Cluster settings"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/cluster-api/cluster-settings.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/cluster-api/cluster-settings.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/cluster-api/cluster-settings/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/cluster-api/cluster-settings/"
canonical_route: "/api-reference/cluster-api/cluster-settings/"
redirect_from: ["/api-reference/cluster-settings/","/opensearch/rest-api/cluster-settings/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 50
parent: "Cluster APIs"
---
# Cluster settings
**Introduced 1.0**
{: .label .label-purple }

The cluster settings operation lets you check the current settings for your cluster, review default settings, and change settings. When you update a setting using the API, OpenSearch applies it to all nodes in the cluster.

## Endpoints

```json
GET _cluster/settings
PUT _cluster/settings
```

## Path parameters

All parameters are optional.

Parameter | Data type | Description
:--- | :--- | :---
flat_settings | Boolean | Whether to return settings in the flat form, which can improve readability, especially for heavily nested settings. For example, the flat form of `"cluster": { "max_shards_per_node": 500 }` is `"cluster.max_shards_per_node": "500"`.
include_defaults (GET only) | Boolean | Whether to include default settings as part of the response. This parameter is useful for identifying the names and current values of settings you want to update.
cluster_manager_timeout | Time unit | The amount of time to wait for a response from the cluster manager node. Default is `30 seconds`.
timeout (PUT only) | Time unit | The amount of time to wait for a response from the cluster. Default is `30 seconds`.

## Request body fields

The GET operation has no request body fields. All cluster setting field parameters are optional.

Not all cluster settings can be updated using the cluster settings API. You will receive the error message `"setting [cluster.some.setting], not dynamically updateable"` when trying to configure these settings through the API.
{: .note }

For a listing of all cluster settings, see [Configuring OpenSearch](../../../install-and-configure/configuring-opensearch/index.md).

## Example requests

The following example request show how to use the cluster settings API.

### Check default cluster settings

The following example request checks for default cluster settings:

```json
GET _cluster/settings?include_defaults=true
```

### Update cluster setting

The following example updates the `cluster.max_shards_per_node` setting. For a PUT operation, the request body must contain `transient` or `persistent`, along with the setting you want to update:

```json
PUT _cluster/settings
{
   "persistent":{
      "cluster.max_shards_per_node": 500
   }
}
```

For more information about transient settings, persistent settings, and precedence, see [OpenSearch configuration](../../../install-and-configure/configuring-opensearch/index.md).

## Example response

The following example response shows that the persistent cluster setting, `max_shard_per_node`, has been updated:

```json
{
   "acknowledged":true,
   "persistent":{
      "cluster":{
         "max_shards_per_node":"500"
      }
   },
   "transient":{}
}
```
