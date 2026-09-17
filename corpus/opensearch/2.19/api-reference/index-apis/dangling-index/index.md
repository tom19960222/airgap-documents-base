---
collection: "opensearch"
version: "2.19"
title: "Dangling indexes"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/index-apis/dangling-index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/index-apis/dangling-index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/index-apis/dangling-index/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/index-apis/dangling-index/"
canonical_route: "/api-reference/index-apis/dangling-index/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 32
parent: "Index APIs"
---
# Dangling indexes API
**Introduced 1.0**
{: .label .label-purple }

After a node joins a cluster, dangling indexes occur if any shards exist in the node's local directory that do not already exist in the cluster. Dangling indexes can be listed, deleted, or imported.

## Endpoints

List dangling indexes:

```json
GET /_dangling
```

Import a dangling index:

```json
POST /_dangling/<index-uuid>
```

Delete a dangling index:

```json
DELETE /_dangling/<index-uuid>
```

## Path parameters

Path parameters are required.

Path parameter | Description
:--- | :---
index-uuid | UUID of index.

## Query parameters

Query parameters are optional.

Query parameter | Data type | Description
:--- | :--- | :---
accept_data_loss | Boolean | Must be set to `true` for an `import` or `delete` because OpenSearch is unaware of where the dangling index data came from.
timeout | Time units | The amount of time to wait for a response. If no response is received in the defined time period, an error is returned. Default is `30` seconds.
cluster_manager_timeout | Time units | The amount of time to wait for a connection to the cluster manager. If no response is received in the defined time period, an error is returned. Default is `30` seconds.

## Example requests

### Sample list

````bash
GET /_dangling
````

### Sample import

````bash
POST /_dangling/msdjernajxAT23RT-BupMB?accept_data_loss=true
````

### Sample delete

````bash
DELETE /_dangling/msdjernajxAT23RT-BupMB?accept_data_loss=true
````

## Example response

````json
{
    "_nodes": {
        "total": 1,
        "successful": 1,
        "failed": 0
    },
    "cluster_name": "opensearch-cluster",
    "dangling_indices": [msdjernajxAT23RT-BupMB]
}
````
