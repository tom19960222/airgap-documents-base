---
collection: "opensearch"
version: "2.19"
title: "Machine learning"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/"
canonical_route: "/ml-commons-plugin/"
redirect_from: ["/ml-commons-plugin/index/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
algorithms: [{"heading":"Supported algorithms","link":"/ml-commons-plugin/algorithms/","description":"Learn about the natively supported clustering, pattern detection, and statistical analysis algorithms"}]
has_children: false
has_toc: false
layout: "default"
models: [{"heading":"Deploy local models to your cluster","link":"/ml-commons-plugin/using-ml-models/","list":["<b>Pretrained models</b>: Use OpenSearch-provided models for immediate implementation","<b>Custom models</b>: Upload and serve your own models"]},{"heading":"Connect to externally hosted models","link":"/ml-commons-plugin/remote-models/","description":"Connect to models hosted on Amazon Bedrock, Amazon SageMaker, OpenAI, Cohere, DeepSeek, and other platforms"}]
more_cards: [{"heading":"Get started with AI search","description":"Build your first semantic search application using this hands-on tutorial","link":"/vector-search/tutorials/neural-search-tutorial/"},{"heading":"AI search","description":"Discover AI search, from <b>semantic</b>, <b>hybrid</b>, and <b>multimodal</b> search to <b>RAG</b>","link":"/vector-search/ai-search/"},{"heading":"Tutorials","description":"Follow step-by-step tutorials to integrate AI capabilities into your applications","link":"/vector-search/tutorials/"},{"heading":"ML API reference","description":"Explore comprehensive documentation for machine learning API operations","link":"/ml-commons-plugin/api/"}]
nav_exclude: true
nav_order: 1
oa-toolkit: [{"heading":"OpenSearch Assistant Toolkit","link":"/ml-commons-plugin/opensearch-assistant/","list":["Agents for task orchestration","Tools for specific operations","Configuration automation"]}]
---
# Machine learning

OpenSearch offers two distinct approaches to machine learning (ML): using ML models for tasks like semantic search and text generation, and running statistical algorithms for data analysis. Choose the approach that best fits your use case.

## ML models for search and AI/ML-powered applications

OpenSearch supports ML models that you can use to enhance search relevance through semantic understanding. You can either deploy models directly within your OpenSearch cluster or connect to models hosted on external platforms. These models can transform text into vector embeddings, enabling semantic search capabilities, or provide advanced features like text generation and question answering. For more information, see [Integrating ML models](integrating-ml-models/index.md).

<div class="card-container">

- [Deploy local models to your cluster](using-ml-models/index.md)
  - Pretrained models: Use OpenSearch-provided models for immediate implementation
  - Custom models: Upload and serve your own models

- [Connect to externally hosted models](remote-models/index.md)
  Connect to models hosted on Amazon Bedrock, Amazon SageMaker, OpenAI, Cohere, DeepSeek, and other platforms

</div>

## OpenSearch Assistant and automation

OpenSearch Assistant Toolkit helps you create AI-powered assistants for OpenSearch Dashboards.

<div class="card-container">

- [OpenSearch Assistant Toolkit](opensearch-assistant/index.md)
  - Agents for task orchestration
  - Tools for specific operations
  - Configuration automation

</div>

## Built-in algorithms for data analysis

OpenSearch includes built-in algorithms that analyze your data directly within your cluster, enabling tasks like anomaly detection, data clustering, and predictive analytics without requiring external ML models.

<div class="card-container">

- [Supported algorithms](algorithms/index.md)
  Learn about the natively supported clustering, pattern detection, and statistical analysis algorithms

</div>

## Build your solution

<div class="card-container">

- [Get started with AI search](../tutorials/vector-search/neural-search-tutorial/index.md)
  Build your first semantic search application using this hands-on tutorial

- [AI search](../vector-search/ai-search/index.md)
  Discover AI search, from semantic, hybrid, and multimodal search to RAG

- [Tutorials](../tutorials/vector-search/index.md)
  Follow step-by-step tutorials to integrate AI capabilities into your applications

- [ML API reference](api/index.md)
  Explore comprehensive documentation for machine learning API operations

</div>
