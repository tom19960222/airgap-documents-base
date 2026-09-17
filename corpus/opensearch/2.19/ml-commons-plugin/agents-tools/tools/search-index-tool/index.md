---
collection: "opensearch"
version: "2.19"
title: "Search Index tool"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/agents-tools/tools/search-index-tool.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/agents-tools/tools/search-index-tool.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/agents-tools/tools/search-index-tool/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/agents-tools/tools/search-index-tool/"
canonical_route: "/ml-commons-plugin/agents-tools/tools/search-index-tool/"
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
nav_order: 90
parent: "Tools"
---
<!-- vale off -->
# Search Index tool
**Introduced 2.13**
{: .label .label-purple }
<!-- vale on -->

The `SearchIndexTool` searches an index using a query written in query domain-specific language (DSL) and returns the query results.

## Step 1: Register a flow agent that will run the SearchIndexTool

A flow agent runs a sequence of tools in order and returns the last tool's output. To create a flow agent, send the following register agent request:

```json
POST /_plugins/_ml/agents/_register
{
  "name": "Test_Agent_For_Search_Index_Tool",
  "type": "flow",
  "description": "this is a test for search index tool",
  "memory": {
    "type": "demo"
  },
  "tools": [
    {
      "type": "SearchIndexTool"
    }
  ]
}
```

OpenSearch responds with an agent ID:

```json
{
  "agent_id": "9X7xWI0Bpc3sThaJdY9i"
}
```

## Step 2: Run the agent

Before you run the agent, make sure that you add the sample OpenSearch Dashboards `Sample eCommerce orders` dataset. To learn more, see [Adding sample data](https://docs.opensearch.org/latest/dashboards/quickstart#adding-sample-data) <!-- unresolved-cross-corpus-link: collection=opensearch-dashboards route=/dashboards/quickstart/ -->.

Then, run the agent by sending the following request. The `SearchIndexTool` takes one parameter named `input`. This parameter includes the index name and the query:

```json
POST /_plugins/_ml/agents/9X7xWI0Bpc3sThaJdY9i/_execute
{
  "parameters": {
    "input": "{\"index\": \"opensearch_dashboards_sample_data_ecommerce\", \"query\": {\"size\": 20,  \"_source\": \"email\"}}"
  }
}
```

For parameter descriptions, see [Execute parameters](#execute-parameters).

The query passed in the previous request is equivalent to the following query:

```json
GET opensearch_dashboards_sample_data_ecommerce/_search
{
  "size": 20,
  "_source": "email"
}
```

OpenSearch returns the query results:

```json
{
  "inference_results": [
    {
      "output": [
        {
          "name": "response",
          "result": """{"_index":"opensearch_dashboards_sample_data_ecommerce","_source":{"email":"eddie@underwood-family.zzz"},"_id":"_bJVWY0BAehlDanXJnAJ","_score":1.0}
{"_index":"opensearch_dashboards_sample_data_ecommerce","_source":{"email":"mary@bailey-family.zzz"},"_id":"_rJVWY0BAehlDanXJnAJ","_score":1.0}
{"_index":"opensearch_dashboards_sample_data_ecommerce","_source":{"email":"gwen@butler-family.zzz"},"_id":"_7JVWY0BAehlDanXJnAJ","_score":1.0}
{"_index":"opensearch_dashboards_sample_data_ecommerce","_source":{"email":"diane@chandler-family.zzz"},"_id":"ALJVWY0BAehlDanXJnEJ","_score":1.0}
{"_index":"opensearch_dashboards_sample_data_ecommerce","_source":{"email":"eddie@weber-family.zzz"},"_id":"AbJVWY0BAehlDanXJnEJ","_score":1.0}
{"_index":"opensearch_dashboards_sample_data_ecommerce","_source":{"email":"diane@goodwin-family.zzz"},"_id":"ArJVWY0BAehlDanXJnEJ","_score":1.0}
{"_index":"opensearch_dashboards_sample_data_ecommerce","_source":{"email":"oliver@rios-family.zzz"},"_id":"A7JVWY0BAehlDanXJnEJ","_score":1.0}
{"_index":"opensearch_dashboards_sample_data_ecommerce","_source":{"email":"abd@sutton-family.zzz"},"_id":"BLJVWY0BAehlDanXJnEJ","_score":1.0}
{"_index":"opensearch_dashboards_sample_data_ecommerce","_source":{"email":"wilhemina st.@tran-family.zzz"},"_id":"BbJVWY0BAehlDanXJnEJ","_score":1.0}
{"_index":"opensearch_dashboards_sample_data_ecommerce","_source":{"email":"rabbia al@baker-family.zzz"},"_id":"BrJVWY0BAehlDanXJnEJ","_score":1.0}
{"_index":"opensearch_dashboards_sample_data_ecommerce","_source":{"email":"rabbia al@romero-family.zzz"},"_id":"B7JVWY0BAehlDanXJnEJ","_score":1.0}
{"_index":"opensearch_dashboards_sample_data_ecommerce","_source":{"email":"eddie@gregory-family.zzz"},"_id":"CLJVWY0BAehlDanXJnEJ","_score":1.0}
{"_index":"opensearch_dashboards_sample_data_ecommerce","_source":{"email":"sultan al@pratt-family.zzz"},"_id":"CbJVWY0BAehlDanXJnEJ","_score":1.0}
{"_index":"opensearch_dashboards_sample_data_ecommerce","_source":{"email":"eddie@wolfe-family.zzz"},"_id":"CrJVWY0BAehlDanXJnEJ","_score":1.0}
{"_index":"opensearch_dashboards_sample_data_ecommerce","_source":{"email":"sultan al@thompson-family.zzz"},"_id":"C7JVWY0BAehlDanXJnEJ","_score":1.0}
{"_index":"opensearch_dashboards_sample_data_ecommerce","_source":{"email":"sultan al@boone-family.zzz"},"_id":"DLJVWY0BAehlDanXJnEJ","_score":1.0}
{"_index":"opensearch_dashboards_sample_data_ecommerce","_source":{"email":"george@hubbard-family.zzz"},"_id":"DbJVWY0BAehlDanXJnEJ","_score":1.0}
{"_index":"opensearch_dashboards_sample_data_ecommerce","_source":{"email":"boris@maldonado-family.zzz"},"_id":"DrJVWY0BAehlDanXJnEJ","_score":1.0}
{"_index":"opensearch_dashboards_sample_data_ecommerce","_source":{"email":"yahya@rivera-family.zzz"},"_id":"D7JVWY0BAehlDanXJnEJ","_score":1.0}
{"_index":"opensearch_dashboards_sample_data_ecommerce","_source":{"email":"brigitte@morris-family.zzz"},"_id":"ELJVWY0BAehlDanXJnEJ","_score":1.0}
"""
        }
      ]
    }
  ]
}
```

## Execute parameters

The following table lists all tool parameters that are available when registering an agent.

Parameter | Type | Description
:--- | :--- | :---
`input`| String | The index name and the query to use for search, in JSON format. The `index` parameter contains the name of the index and the `query` parameter contains the query formatted in Query DSL. For example, `"{\"index\": \"opensearch_dashboards_sample_data_ecommerce\", \"query\": {\"size\": 22,  \"_source\": \"category\"}}"`. The `input` parameter and the `index` and `query` parameters it contains are required.
