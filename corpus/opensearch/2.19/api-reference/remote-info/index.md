---
collection: "opensearch"
version: "2.19"
title: "Remote cluster information"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/remote-info.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/remote-info.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/remote-info/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/cluster-api/remote-info/"
canonical_route: "/api-reference/cluster-api/remote-info/"
redirect_from: ["/opensearch/rest-api/remote-info/","/api-reference/cluster-api/remote-info/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 67
---
# Remote cluster information
**Introduced 1.0**
{: .label .label-purple }

This operation provides connection information for any remote OpenSearch clusters that you've configured for the local cluster, such as the remote cluster alias, connection mode (`sniff` or `proxy`), IP addresses for seed nodes, and timeout settings.

The response is more comprehensive and useful than a call to `_cluster/settings`, which only includes the cluster alias and seed nodes.

## Endpoints

```json
GET _remote/info
```

## Example Response

```json
{
  "opensearch-cluster2": {
    "connected": true,
    "mode": "sniff",
    "seeds": [
      "172.28.0.2:9300"
    ],
    "num_nodes_connected": 1,
    "max_connections_per_cluster": 3,
    "initial_connect_timeout": "30s",
    "skip_unavailable": false
  }
}
```
