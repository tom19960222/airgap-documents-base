---
collection: "opensearch"
version: "2.19"
title: "Search agent"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/agent-apis/search-agent.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/agent-apis/search-agent.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/agent-apis/search-agent/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/agent-apis/search-agent/"
canonical_route: "/ml-commons-plugin/api/agent-apis/search-agent/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "ML Commons APIs"
layout: "default"
nav_order: 30
parent: "Agent APIs"
---
# Search for an agent
**Introduced 2.13**
{: .label .label-purple }

Use this command to search for agents you've already created. You can provide any OpenSearch search query in the request body.

## Endpoints

```json
GET /_plugins/_ml/agents/_search
POST /_plugins/_ml/agents/_search
```

#### Example request: Searching for all agents

```json
POST /_plugins/_ml/agents/_search
{
  "query": {
    "match_all": {}
  },
  "size": 1000
}
```

#### Example request: Searching for agents of a certain type

```json
POST /_plugins/_ml/agents/_search
{
  "query": {
    "term": {
      "type": {
        "value": "flow"
      }
    }
  }
}
```

#### Example: Searching for an agent by description

```json
GET _plugins/_ml/agents/_search
{
  "query": {
    "bool": {
      "should": [
        {
          "match": {
            "description": "test agent"
          }
        }
      ]
    }
  },
  "size": 1000
}
```

#### Example response

```json
{
  "took": 2,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 6,
      "relation": "eq"
    },
    "max_score": 0.15019803,
    "hits": [
      {
        "_index": ".plugins-ml-agent",
        "_id": "8HXlkI0BfUsSoeNTP_0P",
        "_version": 1,
        "_seq_no": 17,
        "_primary_term": 2,
        "_score": 0.13904166,
        "_source": {
          "created_time": 1707532959502,
          "last_updated_time": 1707532959502,
          "name": "Test_Agent_For_RagTool",
          "description": "this is a test flow agent",
          "type": "flow",
          "tools": [
            {
              "description": "A description of the tool",
              "include_output_in_agent_response": false,
              "type": "RAGTool",
              "parameters": {
                "inference_model_id": "gnDIbI0BfUsSoeNT_jAw",
                "embedding_model_id": "Yg7HZo0B9ggZeh2gYjtu_2",
                "input": "${parameters.question}",
                "source_field": """["text"]""",
                "embedding_field": "embedding",
                "index": "my_test_data",
                "query_type": "neural",
                "prompt": """

Human:You are a professional data analyst. You will always answer question based on the given context first. If the answer is not directly shown in the context, you will analyze the data and find the answer. If you don't know the answer, just say don't know.

 Context:
${parameters.output_field}

Human:${parameters.question}

Assistant:"""
              }
            }
          ]
        }
      }
    ]
  }
}
```

## Response body fields

For response field descriptions, see [Register Agent API request fields](../register-agent/index.md#request-body-fields).
