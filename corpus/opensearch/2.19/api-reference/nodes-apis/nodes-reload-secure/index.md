---
collection: "opensearch"
version: "2.19"
title: "Nodes reload secure settings"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/nodes-apis/nodes-reload-secure.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/nodes-apis/nodes-reload-secure.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/nodes-apis/nodes-reload-secure/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/nodes-apis/nodes-reload-secure/"
canonical_route: "/api-reference/nodes-apis/nodes-reload-secure/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 50
parent: "Nodes APIs"
---
# Nodes reload secure settings
**Introduced 1.0**
{: .label .label-purple }

The nodes reload secure settings endpoint allows you to change secure settings on a node and reload the secure settings without restarting the node.

## Endpoints

```json
POST _nodes/reload_secure_settings
POST _nodes/<nodeId>/reload_secure_settings
```

## Path parameter

You can include the following optional path parameter in your request.

Parameter | Type | Description
:--- | :--- | :---
nodeId | String | A comma-separated list of nodeIds used to filter results. Supports [node filters](../index.md#node-filters). Defaults to `_all`.

## Request body fields

The request may include an optional object containing the password for the OpenSearch keystore.

```json
{
  "secure_settings_password": "keystore_password"
}
```

## Example request

The following is an example API request:

```
POST _nodes/reload_secure_settings
```

## Example response

The following is an example response:

```json
{
  "_nodes" : {
    "total" : 1,
    "successful" : 1,
    "failed" : 0
  },
  "cluster_name" : "opensearch-cluster",
  "nodes" : {
    "t7uqHu4SSuWObK3ElkCRfw" : {
      "name" : "opensearch-node1"
    }
  }
}
```

## Required permissions

If you use the Security plugin, make sure you set the following permissions: `cluster:manage/nodes`.
