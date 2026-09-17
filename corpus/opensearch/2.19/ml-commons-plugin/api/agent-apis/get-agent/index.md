---
collection: "opensearch"
version: "2.19"
title: "Get agent"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/agent-apis/get-agent.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/agent-apis/get-agent.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/agent-apis/get-agent/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/agent-apis/get-agent/"
canonical_route: "/ml-commons-plugin/api/agent-apis/get-agent/"
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
# Get an agent
**Introduced 2.13**
{: .label .label-purple }

You can retrieve agent information using the `agent_id`.

## Endpoints

```json
GET /_plugins/_ml/agents/<agent_id>
```

## Path parameters

The following table lists the available path parameters.

| Parameter | Data type | Description |
| :--- | :--- | :--- |
| `agent_id` | String | The agent ID of the agent to retrieve. |

#### Example request

```json
GET /_plugins/_ml/agents/N8AE1osB0jLkkocYjz7D
```

#### Example response

```json
{
  "name": "Test_Agent_For_RAG",
  "type": "flow",
  "description": "this is a test agent",
  "tools": [
    {
      "type": "VectorDBTool",
      "parameters": {
        "input": "${parameters.question}",
        "source_field": """["text"]""",
        "embedding_field": "embedding",
        "index": "my_test_data",
        "model_id": "zBRyYIsBls05QaITo5ex"
      },
      "include_output_in_agent_response": false
    },
    {
      "type": "MLModelTool",
      "description": "A general tool to answer any question",
      "parameters": {
        "model_id": "ygAzT40Bdo8gePIqxk0H",
        "prompt": """

Human:You are a professional data analyst. You will always answer question based on the given context first. If the answer is not directly shown in the context, you will analyze the data and find the answer. If you don't know the answer, just say don't know.

 Context:
${parameters.VectorDBTool.output}

Human:${parameters.question}

Assistant:"""
      },
      "include_output_in_agent_response": false
    }
  ],
  "created_time": 1706821658743,
  "last_updated_time": 1706821658743
}
```

## Response body fields

For response field descriptions, see [Register Agent API request fields](../register-agent/index.md#request-body-fields).
