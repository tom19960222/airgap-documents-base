---
collection: "opensearch"
version: "2.19"
title: "Execute agent"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/agent-apis/execute-agent.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/agent-apis/execute-agent.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/agent-apis/execute-agent/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/agent-apis/execute-agent/"
canonical_route: "/ml-commons-plugin/api/agent-apis/execute-agent/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "ML Commons APIs"
layout: "default"
nav_order: 20
parent: "Agent APIs"
---
# Execute an agent
**Introduced 2.13**
{: .label .label-purple }

When an agent is executed, it runs the tools with which it is configured.

### Endpoints

```json
POST /_plugins/_ml/agents/<agent_id>/_execute
```

## Request body fields

The following table lists the available request fields.

Field | Data type | Required/Optional | Description
:---  | :--- | :---
`parameters`| Object | Required | The parameters required by the agent.
`parameters.verbose`| Boolean | Optional | Provides verbose output.

#### Example request

```json
POST /_plugins/_ml/agents/879v9YwBjWKCe6Kg12Tx/_execute
{
  "parameters": {
    "question": "what's the population increase of Seattle from 2021 to 2023"
  }
}
```

#### Example response

```json
{
  "inference_results": [
    {
      "output": [
        {
          "result": """ Based on the given context, the key information is:

The metro area population of Seattle in 2021 was 3,461,000.
The metro area population of Seattle in 2023 is 3,519,000.

To calculate the population increase from 2021 to 2023:

Population in 2023 (3,519,000) - Population in 2021 (3,461,000) = 58,000

Therefore, the population increase of Seattle from 2021 to 2023 is 58,000."""
        }
      ]
    }
  ]
}
```
