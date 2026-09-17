---
collection: "opensearch"
version: "2.19"
title: "Search for a workflow"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_automating-configurations/api/search-workflow.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_automating-configurations/api/search-workflow.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/automating-configurations/api/search-workflow/"
canonical_url: "https://docs.opensearch.org/latest/automating-configurations/api/search-workflow/"
canonical_route: "/automating-configurations/api/search-workflow/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 60
parent: "Workflow APIs"
---
# Search for a workflow

You can retrieve created workflows with their `workflow_id` or search for workflows by using a query matching a field. You can use the `use_case` field to search for similar workflows.

## Endpoints

```json
GET /_plugins/_flow_framework/workflow/_search
POST /_plugins/_flow_framework/workflow/_search
```

#### Example request: All created workflows

```json
GET /_plugins/_flow_framework/workflow/_search
{
  "query": {
    "match_all": {}
  }
}
```

#### Example request: All workflows with a `use_case` of `REMOTE_MODEL_DEPLOYMENT`

```json
GET /_plugins/_flow_framework/workflow/_search
{
  "query": {
    "match": {
      "use_case": "REMOTE_MODEL_DEPLOYMENT"
    }
  }
}
```

#### Example response

OpenSearch responds with a list of workflow templates matching the search parameters.
