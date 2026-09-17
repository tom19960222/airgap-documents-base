---
collection: "opensearch"
version: "2.19"
title: "Search for a workflow state"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_automating-configurations/api/search-workflow-state.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_automating-configurations/api/search-workflow-state.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/automating-configurations/api/search-workflow-state/"
canonical_url: "https://docs.opensearch.org/latest/automating-configurations/api/search-workflow-state/"
canonical_route: "/automating-configurations/api/search-workflow-state/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 65
parent: "Workflow APIs"
---
# Search for a workflow

You can search for resources created by workflows by matching a query to a field. The fields you can search correspond to those returned by the [Get Workflow Status API](../get-workflow-status/index.md).

## Endpoints

```json
GET /_plugins/_flow_framework/workflow/state/_search
POST /_plugins/_flow_framework/workflow/state/_search
```

#### Example request: All workflows with a state of `NOT_STARTED`

```json
GET /_plugins/_flow_framework/workflow/state/_search
{
  "query": {
    "match": {
      "state": "NOT_STARTED"
    }
  }
}
```

#### Example request: All workflows that have a `resources_created` field with a `workflow_step_id` of `register_model_2`

```json
GET /_plugins/_flow_framework/workflow/state/_search
{
  "query": {
    "nested": {
      "path": "resources_created",
      "query": {
        "bool": {
          "must": [
            {
              "match": {
                "resources_created.workflow_step_id": "register_model_2"
              }
            }
          ]
        }
      }
    }
  }
}
```

#### Example response

The response contains documents matching the search parameters.
