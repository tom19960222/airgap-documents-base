---
collection: "opensearch"
version: "2.19"
title: "AI search"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_vector-search/ai-search/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_vector-search/ai-search/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/vector-search/ai-search/"
canonical_url: "https://docs.opensearch.org/latest/vector-search/ai-search/index/"
canonical_route: "/vector-search/ai-search/"
redirect_from: ["/neural-search-plugin/index/","/search-plugins/neural-search/","/vector-search/ai-search/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
model_cards: [{"heading":"Use a pretrained model provided by OpenSearch","link":"/ml-commons-plugin/pretrained-models/"},{"heading":"Upload your own model to OpenSearch","link":"/ml-commons-plugin/custom-local-models/"},{"heading":"Connect to a model hosted on an external platform","link":"/ml-commons-plugin/remote-models/index/"}]
nav_order: 45
search_method_cards: [{"heading":"Semantic search","description":"Uses dense retrieval based on text embedding models to search text data.","link":"/vector-search/ai-search/semantic-search/"},{"heading":"Hybrid search","description":"Combines keyword and semantic search to improve search relevance.","link":"/vector-search/ai-search/hybrid-search/"},{"heading":"Multimodal search","description":"Uses multimodal embedding models to search text and image data.","link":"/vector-search/ai-search/multimodal-search/"},{"heading":"Neural sparse search","description":"Uses sparse retrieval based on sparse embedding models to search text data.","link":"/vector-search/ai-search/neural-sparse-search/"},{"heading":"Conversational search with RAG","description":"Uses retrieval-augmented generation (RAG) and conversational memory to provide context-aware responses.","link":"/vector-search/ai-search/conversational-search/"}]
tutorial_cards: [{"heading":"Getting started with semantic and hybrid search","description":"Learn how to implement semantic and hybrid search","link":"/vector-search/tutorials/neural-search-tutorial/"}]
---
# AI search

AI search streamlines your workflow by generating embeddings automatically. OpenSearch converts text to vectors during indexing and querying. It creates and indexes vector embeddings for documents and then processes query text into embeddings to find and return the most relevant results.

## Prerequisite

Before using AI search, you must set up an ML model for embedding generation. When selecting a model, you have the following options:

- Use a pretrained model provided by OpenSearch. For more information, see [OpenSearch-provided pretrained models](../../ml-commons-plugin/pretrained-models/index.md).

- Upload your own model to OpenSearch. For more information, see [Custom local models](../../ml-commons-plugin/custom-local-models/index.md).

- Connect to a foundation model hosted on an external platform. For more information, see [Connecting to externally hosted models](../../ml-commons-plugin/remote-models/index.md).

---

## Tutorial

<div class="card-container">

- [Getting started with semantic and hybrid search](../../tutorials/vector-search/neural-search-tutorial/index.md)
  Learn how to implement semantic and hybrid search

</div>

---

## AI search methods

Once you set up an ML model, choose one of the following search methods.

<div class="card-container">

- [Semantic search](semantic-search/index.md)
  Uses dense retrieval based on text embedding models to search text data.

- [Hybrid search](hybrid-search/index.md)
  Combines keyword and semantic search to improve search relevance.

- [Multimodal search](multimodal-search/index.md)
  Uses multimodal embedding models to search text and image data.

- [Neural sparse search](neural-sparse-search/index.md)
  Uses sparse retrieval based on sparse embedding models to search text data.

- [Conversational search with RAG](conversational-search/index.md)
  Uses retrieval-augmented generation (RAG) and conversational memory to provide context-aware responses.

</div>
