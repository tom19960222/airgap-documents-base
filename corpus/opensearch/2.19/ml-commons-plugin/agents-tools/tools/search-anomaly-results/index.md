---
collection: "opensearch"
version: "2.19"
title: "Search Anomaly Results tool"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/agents-tools/tools/search-anomaly-results.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/agents-tools/tools/search-anomaly-results.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/agents-tools/tools/search-anomaly-results/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/agents-tools/tools/search-anomaly-results/"
canonical_route: "/ml-commons-plugin/agents-tools/tools/search-anomaly-results/"
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
nav_order: 80
parent: "Tools"
---
<!-- vale off -->
# Search Anomaly Results tool
**Introduced 2.13**
{: .label .label-purple }
<!-- vale on -->

The `SearchAnomalyResultsTool` retrieves information about anomaly detector results. For more information about anomaly detectors, see [Anomaly detection](../../../../observing-your-data/ad/index.md).

## Step 1: Register a flow agent that will run the SearchAnomalyResultsTool

A flow agent runs a sequence of tools in order and returns the last tool's output. To create a flow agent, send the following register agent request:

```json
POST /_plugins/_ml/agents/_register
{
  "name": "Test_Agent_For_Search_Anomaly_Results_Tool",
  "type": "flow",
  "description": "this is a test agent for the SearchAnomalyResultsTool",
  "memory": {
    "type": "demo"
  },
  "tools": [
    {
      "type": "SearchAnomalyResultsTool",
      "name": "DemoSearchAnomalyResultsTool",
      "parameters": {}
    }
  ]
}
```

For parameter descriptions, see [Register parameters](#register-parameters).

OpenSearch responds with an agent ID:

```json
{
  "agent_id": "HuJZYo0B9RaBCvhuUlpy"
}
```

## Step 2: Run the agent

Run the agent by sending the following request:

```json
POST /_plugins/_ml/agents/HuJZYo0B9RaBCvhuUlpy/_execute
{
  "parameters": {
    "question": "Do I have any anomalies?"
  }
}
```

OpenSearch responds with a list of individual anomaly detectors set up on your cluster (where each result contains the detector ID, the anomaly grade, and the confidence level) and the total number of anomaly results found:

```json
{
  "inference_results": [
    {
      "output": [
        {
          "name": "response",
          "result": "AnomalyResults=[{detectorId=ef9lYo0Bk4MTqircmjnm,grade=1.0,confidence=0.9403051246569198}{detectorId=E-JlYo0B9RaBCvhunFtw,grade=1.0,confidence=0.9163498216870274}]TotalAnomalyResults=2"
        }
      ]
    }
  ]
}
```

If no anomalies are found, OpenSearch responds with an empty array in the results:

```json
{
  "inference_results": [
    {
      "output": [
        {
          "name": "response",
          "result": "AnomalyResults=[]TotalAnomalyResults=0"
        }
      ]
    }
  ]
}
```

## Register parameters

The following table lists all tool parameters that are available when registering an agent. All parameters are optional.

Parameter	| Type | Description
:--- | :--- | :---
`detectorId`	| String	| The ID of the detector from which to return results.
`realTime`	| Boolean | Whether to return real-time anomaly detector results. Set this parameter to `false` to return only historical analysis results.
`anomalyGradeThreshold` | Float	| The minimum anomaly grade for the returned anomaly detector results. Anomaly grade is a number between 0 and 1 that indicates how anomalous a data point is.
`dataStartTime` | Long	| The earliest time for which to return anomaly detector results, in epoch milliseconds.
`dataEndTime` | Long |	The latest time for which to return anomaly detector results, in epoch milliseconds.
`sortOrder`	|String | The sort order for the results. Valid values are `asc` (ascending) and `desc` (descending). Default is `desc`.
`sortString`| String |	Specifies the detector field by which to sort the results. Default is `data_start_time`.
`size`	| Integer |	The number of results to return. Default is `20`.
`startIndex`| Integer |	The paginated index of the result to start from. Default is `0`.

## Execute parameters

The following table lists all tool parameters that are available when running the agent.

Parameter	| Type | Required/Optional | Description
:--- | :--- | :--- | :---
`question` | String | Required | The natural language question to send to the LLM.
