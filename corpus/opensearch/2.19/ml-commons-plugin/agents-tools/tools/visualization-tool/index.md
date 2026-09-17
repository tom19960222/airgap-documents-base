---
collection: "opensearch"
version: "2.19"
title: "Visualization tool"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/agents-tools/tools/visualization-tool.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/agents-tools/tools/visualization-tool.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/agents-tools/tools/visualization-tool/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/agents-tools/tools/visualization-tool/"
canonical_route: "/ml-commons-plugin/agents-tools/tools/visualization-tool/"
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
nav_order: 120
parent: "Tools"
---
# Visualization tool
**Introduced 2.13**
{: .label .label-purple }

Use the `VisualizationTool` to find visualizations relevant to a question.

## Step 1: Register a flow agent that will run the VisualizationTool

A flow agent runs a sequence of tools in order and returns the last tool's output. To create a flow agent, send the following register agent request:

```json
POST /_plugins/_ml/agents/_register
{
  "name": "Test_Agent_For_Visualization_tool",
  "type": "flow",
  "description": "this is a test agent for the VisuailizationTool",
  "tools": [
      {
      "type": "VisualizationTool",
      "name": "DemoVisualizationTool",
      "parameters": {
        "index": ".kibana",
        "input": "${parameters.question}",
        "size": 3
      }
    }
  ]
}
```

For parameter descriptions, see [Register parameters](#register-parameters).

OpenSearch responds with an agent ID:

```json
{
  "agent_id": "9X7xWI0Bpc3sThaJdY9i"
}
```

## Step 2: Run the agent

Before you run the agent, make sure that you add the sample OpenSearch Dashboards `Sample eCommerce orders` dataset. To learn more, see [Adding sample data](https://docs.opensearch.org/latest/dashboards/quickstart#adding-sample-data) <!-- unresolved-cross-corpus-link: collection=opensearch-dashboards route=/dashboards/quickstart/ -->.

Then, run the agent by sending the following request:

```json
POST /_plugins/_ml/agents/9X7xWI0Bpc3sThaJdY9i/_execute
{
  "parameters": {
    "question": "what's the revenue for today?"
  }
}
```

By default, OpenSearch returns the top three matching visualizations. You can use the `size` parameter to specify the number of results returned. The output is returned in CSV format. The output includes two columns: `Title` (the visualization title displayed in OpenSearch Dashboards) and `Id` (a unique ID for this visualization):

```json
{
  "inference_results": [
    {
      "output": [
        {
          "name": "response",
          "result": """Title,Id
[eCommerce] Total Revenue,10f1a240-b891-11e8-a6d9-e546fe2bba5f
"""
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
`input` | String | Required | The user input used to match visualizations.
`index` | String | Optional | The index to search. Default is `.kibana` (the system index for OpenSearch Dashboards data).
`size` | Integer | Optional | The number of visualizations to return. Default is `3`.

## Execute parameters

The following table lists all tool parameters that are available when running the agent.

Parameter	| Type | Required/Optional | Description
:--- | :--- | :--- | :---
`question` | String | Required | The natural language question to send to the LLM.
