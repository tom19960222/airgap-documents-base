---
collection: "opensearch"
version: "2.19"
title: "Get controller"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/controller-apis/get-controller.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/controller-apis/get-controller.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/controller-apis/get-controller/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/controller-apis/get-controller/"
canonical_route: "/ml-commons-plugin/api/controller-apis/get-controller/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "ML Commons APIs"
layout: "default"
nav_order: 20
parent: "Controller APIs"
---
# Get a controller
**Introduced 2.12**
{: .label .label-purple }

Use this API to retrieve information about a controller for a model by model ID.

### Endpoints

```json
GET /_plugins/_ml/controllers/<model_id>
```

## Path parameters

The following table lists the available path parameters.

| Parameter | Data type | Description |
| :--- | :--- | :--- |
| `model_id` | String | The model ID of the model for which to retrieve the controller. |

#### Example request

```json
GET /_plugins/_ml/controllers/T_S-cY0BKCJ3ot9qr0aP
```

#### Example response

```json
{
  "model_id": "T_S-cY0BKCJ3ot9qr0aP",
  "user_rate_limiter": {
    "user1": {
      "limit": "4",
      "unit": "MINUTES"
    },
    "user2": {
      "limit": "4",
      "unit": "MINUTES"
    }
  }
}
```

If there is no controller defined for the model, OpenSearch returns an error:

```json
{
  "error": {
    "root_cause": [
      {
        "type": "status_exception",
        "reason": "Failed to find model controller with the provided model ID: T_S-cY0BKCJ3ot9qr0aP"
      }
    ],
    "type": "status_exception",
    "reason": "Failed to find model controller with the provided model ID: T_S-cY0BKCJ3ot9qr0aP"
  },
  "status": 404
}
```

## Response body fields

For response field descriptions, see [Create Controller API request fields](../create-controller/index.md#request-body-fields).

## Required permissions

If you use the Security plugin, make sure you have the appropriate permissions: `cluster:admin/opensearch/ml/controllers/get`.
