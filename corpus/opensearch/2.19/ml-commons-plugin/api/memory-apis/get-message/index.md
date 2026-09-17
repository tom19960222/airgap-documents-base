---
collection: "opensearch"
version: "2.19"
title: "Get message"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/memory-apis/get-message.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/memory-apis/get-message.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/memory-apis/get-message/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/memory-apis/get-message/"
canonical_route: "/ml-commons-plugin/api/memory-apis/get-message/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "ML Commons APIs"
layout: "default"
nav_order: 50
parent: "Memory APIs"
---
# Get message
**Introduced 2.12**
{: .label .label-purple }

Use this API to retrieve message information for [conversational search](../../../../vector-search/ai-search/conversational-search/index.md).

To retrieve message information, you can:

- [Get a message by ID](#get-a-message-by-id).
- [Get all messages within a memory](#get-all-messages-within-a-memory).

When the Security plugin is enabled, all memories exist in a `private` security mode. Only the user who created a memory can interact with that memory and its messages.
{: .important}

## Get a message by ID

You can retrieve message information by using the `message_id`.

### Endpoints

```json
GET /_plugins/_ml/memory/message/<message_id>
```

### Path parameters

The following table lists the available path parameters.

Parameter | Data type | Description
:--- | :--- | :---
`message_id` | String | The ID of the message to retrieve.

#### Example request

```json
GET /_plugins/_ml/memory/message/0m8ya40BfUsSoeNTj-pU
```

#### Example response

```json
{
  "memory_id": "gW8Aa40BfUsSoeNTvOKI",
  "message_id": "0m8ya40BfUsSoeNTj-pU",
  "create_time": "2024-02-02T19:01:32.113621539Z",
  "input": null,
  "prompt_template": null,
  "response": "Hello, this is OpenAI. Here is the answer to your question.",
  "origin": null,
  "additional_info": {
    "suggestion": "api.openai.com"
  }
}
```

For information about response fields, see [Create Message request fields](../create-message/index.md#request-body-fields).

## Get all messages within a memory

Use this command to get a list of messages for a certain memory.

### Endpoints

```json
GET /_plugins/_ml/memory/<memory_id>/messages
```

### Path parameters

The following table lists the available path parameters.

Parameter | Data type | Description
:--- | :--- | :---
`memory_id` | String | The ID of the memory for which to retrieve messages.

#### Example request

```json
GET /_plugins/_ml/memory/gW8Aa40BfUsSoeNTvOKI/messages
```

```json
POST /_plugins/_ml/message/_search
{
  "query": {
    "match_all": {}
  },
  "size": 1000
}
```

#### Example response

```json
{
  "messages": [
    {
      "memory_id": "gW8Aa40BfUsSoeNTvOKI",
      "message_id": "BW8ha40BfUsSoeNT8-i3",
      "create_time": "2024-02-02T18:43:23.566994302Z",
      "input": "How do I make an interaction?",
      "prompt_template": "Hello OpenAI, can you answer this question?",
      "response": "Hello, this is OpenAI. Here is the answer to your question.",
      "origin": "MyFirstOpenAIWrapper",
      "additional_info": {
        "suggestion": "api.openai.com"
      }
    },
    {
      "memory_id": "gW8Aa40BfUsSoeNTvOKI",
      "message_id": "0m8ya40BfUsSoeNTj-pU",
      "create_time": "2024-02-02T19:01:32.113621539Z",
      "input": null,
      "prompt_template": null,
      "response": "Hello, this is OpenAI. Here is the answer to your question.",
      "origin": null,
      "additional_info": {
        "suggestion": "api.openai.com"
      }
    }
  ]
}
```

## Response body fields

For information about response fields, see [Create Message request fields](../create-message/index.md#request-body-fields).
