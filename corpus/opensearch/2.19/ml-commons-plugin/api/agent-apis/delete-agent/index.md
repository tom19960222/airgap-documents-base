---
collection: "opensearch"
version: "2.19"
title: "Delete agent"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/agent-apis/delete-agent.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/agent-apis/delete-agent.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/agent-apis/delete-agent/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/agent-apis/delete-agent/"
canonical_route: "/ml-commons-plugin/api/agent-apis/delete-agent/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "ML Commons APIs"
layout: "default"
nav_order: 50
parent: "Agent APIs"
---
# Delete an agent
**Introduced 2.13**
{: .label .label-purple }

You can use this API to delete an agent based on the `agent_id`.

## Endpoints

```json
DELETE /_plugins/_ml/agents/<agent_id>
```

#### Example request

```json
DELETE /_plugins/_ml/agents/MzcIJX8BA7mbufL6DOwl
```

#### Example response

```json
{
  "_index" : ".plugins-ml-agent",
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
