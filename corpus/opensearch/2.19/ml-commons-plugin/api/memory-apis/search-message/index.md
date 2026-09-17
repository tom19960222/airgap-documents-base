---
collection: "opensearch"
version: "2.19"
title: "Search message"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/memory-apis/search-message.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/memory-apis/search-message.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/memory-apis/search-message/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/memory-apis/search-message/"
canonical_route: "/ml-commons-plugin/api/memory-apis/search-message/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "ML Commons APIs"
layout: "default"
nav_order: 60
parent: "Memory APIs"
---
# Search for a message
**Introduced 2.12**
{: .label .label-purple }

Retrieves message information for [conversational search](../../../../vector-search/ai-search/conversational-search/index.md). You can send queries to the `_search` endpoint to search for matching messages within a memory.

When the Security plugin is enabled, all memories exist in a `private` security mode. Only the user who created a memory can interact with that memory and its messages.
{: .important}

## Endpoints

```json
POST /_plugins/_ml/memory/<memory_id>/_search
GET /_plugins/_ml/memory/<memory_id>/_search
```

### Path parameters

The following table lists the available path parameters.

Parameter | Data type | Description
:--- | :--- | :---
`memory_id` | String | The ID of the memory used to search for messages matching the query.

#### Example request

```json
GET /_plugins/_ml/memory/gW8Aa40BfUsSoeNTvOKI/_search
{
  "query": {
    "match": {
      "input": "interaction"
    }
  }
}
```

#### Example response

```json
{
  "took": 5,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 0.47000366,
    "hits": [
      {
        "_index": ".plugins-ml-memory-message",
        "_id": "BW8ha40BfUsSoeNT8-i3",
        "_version": 1,
        "_seq_no": 0,
        "_primary_term": 1,
        "_score": 0.47000366,
        "_source": {
          "input": "How do I make an interaction?",
          "memory_id": "gW8Aa40BfUsSoeNTvOKI",
          "trace_number": null,
          "create_time": "2024-02-02T18:43:23.566994302Z",
          "additional_info": {
            "suggestion": "api.openai.com"
          },
          "response": "Hello, this is OpenAI. Here is the answer to your question.",
          "origin": "MyFirstOpenAIWrapper",
          "parent_message_id": null,
          "prompt_template": "Hello OpenAI, can you answer this question?"
        }
      }
    ]
  }
}
```

## Response body fields

For information about response fields, see [Create Message request fields](../create-message/index.md#request-body-fields).
