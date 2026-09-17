---
collection: "opensearch"
version: "2.19"
title: "Searching data"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_vector-search/searching-data.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_vector-search/searching-data.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/vector-search/searching-data/"
canonical_url: "https://docs.opensearch.org/latest/vector-search/searching-data/"
canonical_route: "/vector-search/searching-data/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 35
---
# Searching vector data

OpenSearch supports various methods for searching vector data, tailored to how the vectors were created and indexed. This guide explains the query syntax and options for raw vector search and auto-generated embedding search.

## Search type comparison

The following table compares the search syntax and typical use cases for each vector search method.

| Feature                          | Query type  | Input format | Model required | Use case     |
|----------------------------------|------------------|------------------|---------------------|----------------------------|
| **Raw vectors**     | [`knn`](../../query-dsl/specialized/k-nn/index.md)            | Vector array     | No                  | Raw vector search          |
| **Auto-generated embeddings** | [`neural`](../../query-dsl/specialized/neural/index.md)       | Text or image data            | Yes                 | [AI search](../ai-search/index.md)            |

## Searching raw vectors

To search raw vectors, use the `knn` query type, provide the `vector` array as input, and specify the number of returned results `k`:

```json
GET /my-raw-vector-index/_search
{
  "query": {
    "knn": {
      "my_vector": {
        "vector": [0.1, 0.2, 0.3],
        "k": 2
      }
    }
  }
}
```

## Searching auto-generated embeddings

OpenSearch supports [AI-powered search methods](../ai-search/index.md), including semantic, hybrid, multimodal, and conversational search with retrieval-augmented generation (RAG). These methods automatically generate embeddings from query input.

To run an AI-powered search, use the `neural` query type. Specify the `query_text` input, the model ID of the embedding model you [configured in the ingest pipeline](../creating-vector-index/index.md#converting-data-to-embeddings-during-ingestion), and the number of returned results `k`. To exclude embeddings from being returned in search results, specify the embedding field in the `_source.excludes` parameter:

```json
GET /my-ai-search-index/_search
{
  "_source": {
    "excludes": [
      "output_embedding"
    ]
  },
  "query": {
    "neural": {
      "output_embedding": {
        "query_text": "What is AI search?",
        "model_id": "mBGzipQB2gmRjlv_dOoB",
        "k": 2
      }
    }
  }
}
```

## Working with sparse vectors

OpenSearch also supports sparse vectors. For more information, see [Neural sparse search](../ai-search/neural-sparse-search/index.md).

## Next steps

- [Getting started with semantic and hybrid search](../../tutorials/vector-search/neural-search-tutorial/index.md)
- [Filtering data](../filter-search-knn/index.md)
- [k-NN query](../../query-dsl/specialized/k-nn/index.md)
- [Neural query](../../query-dsl/specialized/neural/index.md)
