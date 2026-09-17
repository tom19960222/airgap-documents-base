---
collection: "opensearch"
version: "2.19"
title: "Delete model"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/model-apis/delete-model.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/model-apis/delete-model.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/model-apis/delete-model/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/model-apis/delete-model/"
canonical_route: "/ml-commons-plugin/api/model-apis/delete-model/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "ML Commons APIs"
layout: "default"
nav_order: 50
parent: "Model APIs"
---
# Delete a model

Deletes a model based on the `model_id`.

When you delete the last model version in a model group, that model group is automatically deleted from the index.
{: .important}

For information about user access for this API, see [Model access control considerations](../index.md#model-access-control-considerations).

## Endpoints

```json
DELETE /_plugins/_ml/models/<model_id>
```

#### Example request

```json
DELETE /_plugins/_ml/models/MzcIJX8BA7mbufL6DOwl
```

#### Example response

```json
{
  "_index" : ".plugins-ml-model",
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

## Safely deleting a model
Introduced 2.19
{: .label .label-purple }

To prevent accidental deletion of models in active use by agents, search pipelines, ingest pipelines, or other components, you can enable a safety check. If the safety check is enabled and you attempt to delete a model that is in current use, OpenSearch returns an error message. To proceed with deletion:

- Identify any components using the model and either delete them or update them so that they use other models.
- Once all dependencies are cleared, delete the model.

For information about enabling this feature, see [Safely delete models](../../../cluster-settings/index.md#safely-delete-models).
