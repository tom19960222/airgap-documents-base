---
collection: "opensearch"
version: "2.19"
title: "Update model group"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/model-group-apis/update-model-group.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/model-group-apis/update-model-group.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/model-group-apis/update-model-group/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/model-group-apis/update-model-group/"
canonical_route: "/ml-commons-plugin/api/model-group-apis/update-model-group/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "ML Commons APIs"
layout: "default"
nav_order: 20
parent: "Model group APIs"
---
# Update a model group

To update a model group, send a `PUT` request to the `model_groups` endpoint and provide the ID of the model group you want to update.

When updating a model group, the following restrictions apply:

- The model owner or an admin user can update all fields. Any user who shares one or more backend roles with the model group can update the `name` and `description` fields only.
- When updating the `access_mode` to `restricted`, you must specify either `backend_roles` or `add_all_backend_roles` but not both.
- When updating the `name`, ensure the name is globally unique in the cluster.

For more information, see [Model access control](../../../model-access-control/index.md).

## Path and HTTP method

```json
PUT /_plugins/_ml/model_groups/<model_group_id>
```

## Request body fields

Refer to [Request fields](#request-body-fields) for request field descriptions.

#### Example request

```json
PUT /_plugins/_ml/model_groups/<model_group_id>
{
    "name": "model_group_test",
    "description": "This is the updated description",
    "add_all_backend_roles": true
}
```

## Updating a model group in a cluster where model access control is disabled

If model access control is disabled on your cluster (one of the [prerequisites](ml-commons-plugin/model-access-control/#model-access-control-prerequisites) <!-- unresolved-jekyll-link: target=ml-commons-plugin/model-access-control/#model-access-control-prerequisites --> is not met), you can update only the `name` and `description` of a model group but cannot update any of the access parameters (`model_access_name`, `backend_roles`, or `add_backend_roles`).
