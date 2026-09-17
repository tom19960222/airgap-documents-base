---
collection: "opensearch"
version: "2.19"
title: "Delete controller"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/controller-apis/delete-controller.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/controller-apis/delete-controller.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/controller-apis/delete-controller/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/controller-apis/delete-controller/"
canonical_route: "/ml-commons-plugin/api/controller-apis/delete-controller/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "ML Commons APIs"
layout: "default"
nav_order: 50
parent: "Controller APIs"
---
# Delete a controller
**Introduced 2.12**
{: .label .label-purple }

Use this API to delete a controller for a model based on the `model_id`.

## Endpoints

```json
DELETE /_plugins/_ml/controllers/<model_id>
```

## Path parameters

The following table lists the available path parameters.

| Parameter | Data type | Description |
| :--- | :--- | :--- |
| `model_id` | String | The model ID of the model for which to delete the controller. |

#### Example request

```json
DELETE /_plugins/_ml/controllers/MzcIJX8BA7mbufL6DOwl
```

#### Example response

```json
{
  "_index" : ".plugins-ml-controller",
  "_id" : "MzcIJX8BA7mbufL6DOwl",
  "_version" : 2,
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

## Required permissions

If you use the Security plugin, make sure you have the appropriate permissions: `cluster:admin/opensearch/ml/controllers/delete`.
