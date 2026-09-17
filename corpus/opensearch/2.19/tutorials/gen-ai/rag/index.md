---
collection: "opensearch"
version: "2.19"
title: "RAG"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_tutorials/gen-ai/rag/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_tutorials/gen-ai/rag/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/tutorials/gen-ai/rag/"
canonical_url: "https://docs.opensearch.org/latest/tutorials/gen-ai/rag/index/"
canonical_route: "/tutorials/gen-ai/rag/"
redirect_from: ["/vector-search/tutorials/rag/","/vector-search/tutorials/conversational-search/","/tutorials/vector-search/rag/","/tutorials/gen-ai/rag/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
conversational_search: [{"heading":"Conversational search using Cohere Command","link":"/tutorials/gen-ai/rag/conversational-search-cohere/","list":["<b>Platform:</b> OpenSearch","<b>Model:</b> Cohere Command","<b>Deployment:</b> Provider API"]},{"heading":"Conversational search using OpenAI","link":"/tutorials/gen-ai/rag/conversational-search-openai/","list":["<b>Platform:</b> OpenSearch","<b>Model:</b> OpenAI GPT-4o","<b>Deployment:</b> Provider API"]},{"heading":"Conversational search using Anthropic Claude on Amazon Bedrock","link":"/tutorials/gen-ai/rag/conversational-search-claude-bedrock/","list":["<b>Platform:</b> OpenSearch","<b>Model:</b> Anthropic Claude","<b>Deployment:</b> Amazon Bedrock API"]}]
has_children: true
has_toc: false
layout: "default"
nav_order: 10
parent: "Generative AI"
rag: [{"heading":"Retrieval-augmented generation (RAG) using the DeepSeek Chat API","link":"/tutorials/gen-ai/rag/rag-deepseek-chat/","list":["<b>Platform:</b> OpenSearch, Amazon OpenSearch Service","<b>Model:</b> DeepSeek Chat","<b>Deployment:</b> Provider API"]},{"heading":"RAG using DeepSeek-R1 on Amazon Bedrock","link":"/tutorials/gen-ai/rag/rag-deepseek-r1-bedrock/","list":["<b>Platform:</b> OpenSearch, Amazon OpenSearch Service","<b>Model:</b> DeepSeek-R1","<b>Deployment:</b> Amazon Bedrock"]},{"heading":"RAG using DeepSeek-R1 in Amazon SageMaker","link":"/tutorials/gen-ai/rag/rag-deepseek-r1-sagemaker/","list":["<b>Platform:</b> OpenSearch, Amazon OpenSearch Service","<b>Model:</b> DeepSeek-R1","<b>Deployment:</b> Amazon SageMaker"]}]
---
# RAG tutorials

The following machine learning (ML) tutorials show you how to implement retrieval-augmeted generation (RAG).

<div class="card-container">

- [Retrieval-augmented generation (RAG) using the DeepSeek Chat API](rag-deepseek-chat/index.md)
  - Platform: OpenSearch, Amazon OpenSearch Service
  - Model: DeepSeek Chat
  - Deployment: Provider API

- [RAG using DeepSeek-R1 on Amazon Bedrock](rag-deepseek-r1-bedrock/index.md)
  - Platform: OpenSearch, Amazon OpenSearch Service
  - Model: DeepSeek-R1
  - Deployment: Amazon Bedrock

- [RAG using DeepSeek-R1 in Amazon SageMaker](rag-deepseek-r1-sagemaker/index.md)
  - Platform: OpenSearch, Amazon OpenSearch Service
  - Model: DeepSeek-R1
  - Deployment: Amazon SageMaker

</div>

## Conversational search with RAG tutorials

The following tutorials show you how to implement conversational search with RAG.

<div class="card-container">

- [Conversational search using Cohere Command](conversational-search-cohere/index.md)
  - Platform: OpenSearch
  - Model: Cohere Command
  - Deployment: Provider API

- [Conversational search using OpenAI](conversational-search-openai/index.md)
  - Platform: OpenSearch
  - Model: OpenAI GPT-4o
  - Deployment: Provider API

- [Conversational search using Anthropic Claude on Amazon Bedrock](conversational-search-claude-bedrock/index.md)
  - Platform: OpenSearch
  - Model: Anthropic Claude
  - Deployment: Amazon Bedrock API

</div>
