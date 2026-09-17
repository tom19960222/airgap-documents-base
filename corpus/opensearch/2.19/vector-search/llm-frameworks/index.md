---
collection: "opensearch"
version: "2.19"
title: "LLM framework integration"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_vector-search/llm-frameworks.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_vector-search/llm-frameworks.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/vector-search/llm-frameworks/"
canonical_url: "https://docs.opensearch.org/latest/vector-search/llm-frameworks/"
canonical_route: "/vector-search/llm-frameworks/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 75
---
# LLM framework integration

Several popular large language model (LLM) frameworks integrate with OpenSearch as a vector store, enabling you to build production-ready generative AI applications. These frameworks provide high-level abstractions and tools for working with LLMs, and their OpenSearch integrations allow you to use OpenSearch for efficient vector storage, retrieval, and similarity search:

- LangChain
    - [Semantic cache](https://python.langchain.com/docs/integrations/llm_caching/#opensearch-semantic-cache)
    - [Vector store support](https://python.langchain.com/docs/integrations/vectorstores/opensearch/)

- LlamaIndex
    - [Vector store support](https://docs.llamaindex.ai/en/stable/examples/vector_stores/OpensearchDemo/)

- FlowiseAI:
    - [Vector store support](https://docs.flowiseai.com/integrations/langchain/vector-stores/opensearch)

- Langflow:
    - [Vector store support](https://docs.langflow.org/components-vector-stores#opensearch)

- Haystack:
    - [Vector store support](https://haystack.deepset.ai/integrations/opensearch-document-store)
