---
collection: "opensearch"
version: "2.19"
title: "Delete connector"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/connector-apis/delete-connector.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/connector-apis/delete-connector.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/connector-apis/delete-connector/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/connector-apis/delete-connector/"
canonical_route: "/ml-commons-plugin/api/connector-apis/delete-connector/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "ML Commons APIs"
layout: "default"
nav_order: 30
parent: "Connector APIs"
---
# Delete a connector

Deletes a standalone connector. For more information, see [Connectors](../../../remote-models/connectors/index.md).

## Endpoints

```json
DELETE /_plugins/_ml/connectors/<connector_id>
```

#### Example request

```json
DELETE /_plugins/_ml/connectors/KsAo1YsB0jLkkocY6j4U
```

#### Example response

```json
{
  "_index" : ".plugins-ml-connector",
  "_id" : "KsAo1YsB0jLkkocY6j4U",
  "_version" : 1,
  "result" : "deleted",
  "_shards" : {
    "total" : 2,
    "successful" : 2,
    "failed" : 0
  },
  "_seq_no" : 27,
  "_primary_term" : 18
}
```
