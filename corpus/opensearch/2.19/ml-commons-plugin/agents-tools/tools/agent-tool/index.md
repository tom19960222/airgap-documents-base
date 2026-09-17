---
collection: "opensearch"
version: "2.19"
title: "Agent tool"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/agents-tools/tools/agent-tool.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/agents-tools/tools/agent-tool.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/agents-tools/tools/agent-tool/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/agents-tools/tools/agent-tool/"
canonical_route: "/ml-commons-plugin/agents-tools/tools/agent-tool/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Agents and tools"
has_children: false
has_toc: false
layout: "default"
nav_order: 10
parent: "Tools"
---
<!-- vale off -->
# Agent tool
**Introduced 2.13**
{: .label .label-purple }
<!-- vale on -->

The `AgentTool` runs any agent.

## Step 1: Set up an agent for AgentTool to run

Set up any agent. For example, set up a flow agent that runs an `MLModelTool` by following the steps in the [ML Model Tool documentation](../ml-model-tool/index.md) and obtain its agent ID from [Step 3](../ml-model-tool/index.md#step-3-register-a-flow-agent-that-will-run-the-mlmodeltool):

```json
{
  "agent_id": "9X7xWI0Bpc3sThaJdY9i"
}
```

## Step 2: Register a flow agent that will run the AgentTool

A flow agent runs a sequence of tools in order and returns the last tool's output. To create a flow agent, send the following register agent request, providing the agent ID from the previous step:

```json
POST /_plugins/_ml/agents/_register
{
  "name": "Test agent tool",
  "type": "flow",
  "description": "this is a test agent",
  "tools": [
    {
      "type": "AgentTool",
      "description": "A general agent to answer any question",
      "parameters": {
        "agent_id": "9X7xWI0Bpc3sThaJdY9i"
      }
    }
  ]
}
```

For parameter descriptions, see [Register parameters](#register-parameters).

OpenSearch responds with an agent ID:

```json
{
  "agent_id": "EQyyZ40BT2tRrkdmhT7_"
}
```

## Step 3: Run the agent

Run the agent by sending the following request:

```json
POST /_plugins/_ml/agents/EQyyZ40BT2tRrkdmhT7_/_execute
{
  "parameters": {
    "question": "what's the population increase of Seattle from 2021 to 2023"
  }
}
```

OpenSearch returns the inference results:

```json
{
  "inference_results": [
    {
      "output": [
        {
          "name": "response",
          "result": " I do not have direct data on the population increase of Seattle from 2021 to 2023 in the context provided. As a data analyst, I would need to research population statistics from credible sources like the US Census Bureau to analyze population trends and make an informed estimate. Without looking up actual data, I don't have enough information to provide a specific answer to the question."
        }
      ]
    }
  ]
}
```

## Register parameters

The following table lists all tool parameters that are available when registering an agent.

Parameter	| Type | Required/Optional | Description
:--- | :--- | :--- | :---
`agent_id` | String | Required | The agent ID of the agent to run.

## Execute parameters

The following table lists all tool parameters that are available when running the agent.

Parameter	| Type | Required/Optional | Description
:--- | :--- | :--- | :---
`question` | String | Required | The natural language question to send to the LLM.
