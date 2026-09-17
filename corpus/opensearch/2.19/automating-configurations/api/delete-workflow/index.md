---
collection: "opensearch"
version: "2.19"
title: "Delete a workflow"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_automating-configurations/api/delete-workflow.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_automating-configurations/api/delete-workflow.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/automating-configurations/api/delete-workflow/"
canonical_url: "https://docs.opensearch.org/latest/automating-configurations/api/delete-workflow/"
canonical_route: "/automating-configurations/api/delete-workflow/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 80
parent: "Workflow APIs"
---
# Delete a workflow

When you no longer need a workflow template, you can delete it by calling the Delete Workflow API.

Note that deleting a workflow only deletes the stored template---it does not deprovision its resources.

When a workflow is deleted, its corresponding status (returned by the [Workflow State API](../get-workflow-status/index.md)) is also deleted unless either the provisioning status is `IN_PROGRESS` or resources have been provisioned.

## Endpoints

```json
DELETE /_plugins/_flow_framework/workflow/<workflow_id>
```

## Path parameters

The following table lists the available path parameters.

| Parameter | Data type | Description |
| :--- | :--- | :--- |
| `workflow_id` | String | The ID of the workflow to be retrieved. Required. |

## Query parameters

The following table lists the available query parameters. All query parameters are optional.

| Parameter | Data type | Description |
| :--- | :--- | :--- |
| `clear_status` | Boolean | Determines whether to delete the workflow state (without deprovisioning resources) after deleting the template. OpenSearch deletes the workflow state only if the provisioning status is not `IN_PROGRESS`. Default is `false`. |

#### Example request

```json
DELETE /_plugins/_flow_framework/workflow/8xL8bowB8y25Tqfenm50
```

```json
DELETE /_plugins/_flow_framework/workflow/8xL8bowB8y25Tqfenm50?clear_status=true
```

#### Example response

If the workflow exists, a delete response contains the status of the deletion, where the `result` field is set to `deleted` on success or `not_found` if the workflow does not exist (it may have already been deleted):

```json
{
  "_index": ".plugins-flow_framework-templates",
  "_id": "8xL8bowB8y25Tqfenm50",
  "_version": 2,
  "result": "deleted",
  "_shards": {
    "total": 1,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 2,
  "_primary_term": 1
}
```
