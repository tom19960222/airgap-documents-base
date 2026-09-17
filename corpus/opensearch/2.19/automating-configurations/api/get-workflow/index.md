---
collection: "opensearch"
version: "2.19"
title: "Get a workflow"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_automating-configurations/api/get-workflow.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_automating-configurations/api/get-workflow.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/automating-configurations/api/get-workflow/"
canonical_url: "https://docs.opensearch.org/latest/automating-configurations/api/get-workflow/"
canonical_route: "/automating-configurations/api/get-workflow/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 20
parent: "Workflow APIs"
---
# Get a workflow

The Get Workflow API retrieves the workflow template.

## Endpoints

```json
GET /_plugins/_flow_framework/workflow/<workflow_id>
```

## Path parameters

The following table lists the available path parameters.

| Parameter | Data type | Description |
| :--- | :--- | :--- |
| `workflow_id` | String | The ID of the workflow to be retrieved. Required. |

#### Example request

```json
GET /_plugins/_flow_framework/workflow/8xL8bowB8y25Tqfenm50
```

#### Example response

To retrieve a template in YAML format, specify `Content-Type: application/yaml` in the request header:

```bash
curl -XGET "http://localhost:9200/_plugins/_flow_framework/workflow/8xL8bowB8y25Tqfenm50" -H 'Content-Type: application/yaml'
```

To retrieve a template in JSON format, specify `Content-Type: application/json` in the request header:

```bash
curl -XGET "http://localhost:9200/_plugins/_flow_framework/workflow/8xL8bowB8y25Tqfenm50" -H 'Content-Type: application/json'
```

OpenSearch responds with the stored template containing the same content as the body of the [create workflow](../create-workflow/index.md) request. The order of fields in the returned template may not exactly match the original template but will function identically.
