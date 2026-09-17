---
collection: "opensearch"
version: "2.19"
title: "Get workflow steps"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_automating-configurations/api/get-workflow-steps.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_automating-configurations/api/get-workflow-steps.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/automating-configurations/api/get-workflow-steps/"
canonical_url: "https://docs.opensearch.org/latest/automating-configurations/api/get-workflow-steps/"
canonical_route: "/automating-configurations/api/get-workflow-steps/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 50
parent: "Workflow APIs"
---
# Get workflow steps

This API returns a list of workflow steps, including their required inputs, outputs, default timeout values, and required plugins. For example, for the `register_remote_model` step, the Get Workflow Steps API returns the following information:

```json
{
  "register_remote_model": {
    "inputs": [
      "name",
      "connector_id"
    ],
    "outputs": [
      "model_id",
      "register_model_status"
    ],
    "required_plugins": [
      "opensearch-ml"
    ]
  }
}
```

## Endpoints

```json
GET /_plugins/_flow_framework/workflow/_steps
GET /_plugins/_flow_framework/workflow/_steps?workflow_step=<step_name>
```

## Query parameters

The following table lists the available query parameters. All query parameters are optional.

| Parameter | Data type | Description |
| :--- | :--- | :--- |
| `workflow_step` | String | The name of the step to retrieve. Specify multiple step names as a comma-separated list. For example, `create_connector,delete_model,deploy_model`. |

#### Example request

To fetch all workflow steps, use the following request:

```json
GET /_plugins/_flow_framework/workflow/_steps
```

To fetch specific workflow steps, pass the step names to the request as a query parameter:

```json
GET /_plugins/_flow_framework/workflow/_step?workflow_steps=create_connector,delete_model,deploy_model
```

#### Example response

OpenSearch responds with the workflow steps. The order of fields in the returned steps may not exactly match the original JSON but will function identically.

To retrieve the template in YAML format, specify `Content-Type: application/yaml` in the request header:

```bash
curl -XGET "http://localhost:9200/_plugins/_flow_framework/workflow/_steps" -H 'Content-Type: application/yaml'
```

To retrieve the template in JSON format, specify `Content-Type: application/json` in the request header:

```bash
curl -XGET "http://localhost:9200/_plugins/_flow_framework/workflow/_steps" -H 'Content-Type: application/json'
```
