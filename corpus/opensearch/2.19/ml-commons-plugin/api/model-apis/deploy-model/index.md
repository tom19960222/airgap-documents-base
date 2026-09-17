---
collection: "opensearch"
version: "2.19"
title: "Deploy model"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/model-apis/deploy-model.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/model-apis/deploy-model.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/model-apis/deploy-model/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/model-apis/deploy-model/"
canonical_route: "/ml-commons-plugin/api/model-apis/deploy-model/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "ML Commons APIs"
layout: "default"
nav_order: 20
parent: "Model APIs"
---
# Deploy a model

The deploy model operation reads the model's chunks from the model index and then creates an instance of the model to cache in memory. This operation requires the `model_id`.

Starting with OpenSearch version 2.13, [externally hosted models](../../../remote-models/index.md) are deployed automatically by default when you send a Predict API request for the first time. To disable automatic deployment for an externally hosted model, set `plugins.ml_commons.model_auto_deploy.enable` to `false`:

```json
PUT _cluster/settings
{
  "persistent": {
    "plugins.ml_commons.model_auto_deploy.enable": "false"
  }
}
```

For information about user access for this API, see [Model access control considerations](../index.md#model-access-control-considerations).

## Endpoints

```json
POST /_plugins/_ml/models/<model_id>/_deploy
```

#### Example request: Deploying to all available ML nodes

In this example request, OpenSearch deploys the model to any available OpenSearch ML node:

```json
POST /_plugins/_ml/models/WWQI44MBbzI2oUKAvNUt/_deploy
```

#### Example request: Deploying to a specific node

If you want to reserve the memory of other ML nodes within your cluster, you can deploy your model to a specific node(s) by specifying the `node_ids` in the request body:

```json
POST /_plugins/_ml/models/WWQI44MBbzI2oUKAvNUt/_deploy
{
    "node_ids": ["4PLK7KJWReyX0oWKnBA8nA"]
}
```

#### Example response

```json
{
  "task_id" : "hA8P44MBhyWuIwnfvTKP",
  "status" : "DEPLOYING"
}
```

## Check the status of model deployment

To see the status of your model deployment and retrieve the model ID created for the new model version, pass the `task_id` as a path parameter to the Tasks API:

```json
GET /_plugins/_ml/tasks/hA8P44MBhyWuIwnfvTKP
```

The response contains the model ID of the model version:

```json
{
  "model_id": "Qr1YbogBYOqeeqR7sI9L",
  "task_type": "DEPLOY_MODEL",
  "function_name": "TEXT_EMBEDDING",
  "state": "COMPLETED",
  "worker_node": [
    "N77RInqjTSq_UaLh1k0BUg"
  ],
  "create_time": 1685478486057,
  "last_update_time": 1685478491090,
  "is_async": true
}
```

If a cluster or node is restarted, then you need to redeploy the model. To learn how to set up automatic redeployment, see [Enable auto redeploy](../../../cluster-settings/index.md#enable-auto-redeploy).
{: .tip}
