---
collection: "opensearch"
version: "2.19"
title: "Delete model group"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/model-group-apis/delete-model-group.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/model-group-apis/delete-model-group.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/model-group-apis/delete-model-group/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/model-group-apis/delete-model-group/"
canonical_route: "/ml-commons-plugin/api/model-group-apis/delete-model-group/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "ML Commons APIs"
layout: "default"
nav_order: 50
parent: "Model group APIs"
---
# Delete a model group

You can only delete a model group if it does not contain any model versions.
{: .important}

If model access control is enabled on your cluster, only the owner or users with matching backend roles can delete the model group. Any users can delete any public model group.

If model access control is disabled on your cluster, users with the `delete model group API` permission can delete any model group.

Admin users can delete any model group.
{: .note}

When you delete the last model version in a model group, that model group is automatically deleted from the index.
{: .important}

For more information, see [Model access control](../../../model-access-control/index.md).

#### Example request

```json
DELETE _plugins/_ml/model_groups/<model_group_id>
```

#### Example response

```json
{
  "_index": ".plugins-ml-model-group",
  "_id": "l8nnQogByXnLJ-QNpEk2",
  "_version": 5,
  "result": "deleted",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 70,
  "_primary_term": 23
}
```
