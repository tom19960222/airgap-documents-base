---
collection: "opensearch"
version: "2.19"
title: "Concepts"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_vector-search/getting-started/concepts.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_vector-search/getting-started/concepts.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/vector-search/getting-started/concepts/"
canonical_url: "https://docs.opensearch.org/latest/vector-search/getting-started/concepts/"
canonical_route: "/vector-search/getting-started/concepts/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 40
parent: "Getting started"
---
# Concepts

This page defines key terms and techniques related to vector search in OpenSearch.

## Vector representations

- [**_Vector embeddings_**](../vector-search-basics/index.md#vector-embeddings) are numerical representations of data—such as text, images, or audio—that encode meaning or features into a high-dimensional space. These embeddings enable similarity-based comparisons for search and machine learning (ML) tasks.

- **_Dense vectors_** are high-dimensional numerical representations where most elements have nonzero values. They are typically produced by deep learning models and are used in semantic search and ML applications.

- **_Sparse vectors_** contain mostly zero values and are often used in techniques like neural sparse search to efficiently represent and retrieve information.

## Vector search fundamentals

- [**_Vector search_**](../vector-search-basics/index.md), also known as _similarity search_ or _nearest neighbor search_, is a technique for finding items that are most similar to a given input vector. It is widely used in applications such as recommendation systems, image retrieval, and natural language processing.

- A [**_space_**](../vector-search-basics/index.md#calculating-similarity) defines how similarity or distance between two vectors is measured. Different spaces use different distance metrics, such as Euclidean distance or cosine similarity, to determine how closely vectors resemble each other.

- A [**_method_**](../../../field-types/supported-field-types/knn-methods-engines/index.md) refers to the algorithm used to organize vector data during indexing and retrieve relevant results during search in approximate k-NN search. Different methods balance trade-offs between accuracy, speed, and memory usage.

- An [**_engine_**](../../../field-types/supported-field-types/knn-methods-engines/index.md) is the underlying library that implements vector search methods. It determines how vectors are indexed, stored, and retrieved during similarity search operations.

## k-NN search

- **_k-nearest neighbors (k-NN) search_** finds the k most similar vectors to a given query vector in an index. The similarity is determined based on a specified distance metric.

- [**_Exact k-NN search_**](../../vector-search-techniques/knn-score-script/index.md) performs a brute-force comparison between a query vector and all vectors in an index, computing the exact nearest neighbors. This approach provides high accuracy but can be computationally expensive for large datasets.

- [**_Approximate k-NN search_**](../../vector-search-techniques/approximate-knn/index.md) reduces computational complexity by using indexing techniques that speed up search operations while maintaining high accuracy. These methods restructure the index or reduce the dimensionality of vectors to improve performance.

## Query types

- A [**_k-NN query_**](../../../query-dsl/specialized/k-nn/index.md) searches vector fields using a query vector.

- A [**_neural query_**](../../../query-dsl/specialized/neural/index.md) searches vector fields using text or image data.

- A [**_neural sparse query_**](../../../query-dsl/specialized/neural-sparse/index.md) searches vector fields using raw text or sparse vector tokens.

## Search techniques

- [**_Semantic search_**](../../ai-search/semantic-search/index.md) interprets the intent and contextual meaning of a query rather than relying solely on exact keyword matches. This approach improves the relevance of search results, especially for natural language queries.

- [**_Hybrid search_**](../../ai-search/hybrid-search/index.md) combines lexical (keyword-based) search with semantic (vector-based) search to improve search relevance. This approach ensures that results include both exact keyword matches and conceptually similar content.

- [**_Multimodal search_**](../../ai-search/multimodal-search/index.md) enables you to search across multiple types of data, such as text and images. It allows queries in one format (for example, text) to retrieve results in another (for example, images).

- [**_Radial search_**](../../specialized-operations/radial-search-knn/index.md) retrieves all vectors within a specified distance or similarity threshold from a query vector. It is useful for tasks that require finding all relevant matches within a given range rather than retrieving a fixed number of nearest neighbors.

- [**_Neural sparse search_**](../../ai-search/neural-sparse-search/index.md) uses an inverted index, similar to BM25, to efficiently retrieve relevant documents based on sparse vector representations. This approach maintains the efficiency of traditional lexical search while incorporating semantic understanding.

- [**_Conversational search_**](../../ai-search/conversational-search/index.md) allows you to interact with a search system using natural language queries and refine results through follow-up questions. This approach enhances the user experience by making search more intuitive and interactive.

- [**_Retrieval-augmented generation (RAG)_**](../../ai-search/conversational-search/index.md#rag) enhances large language models (LLMs) by retrieving relevant information from an index and incorporating it into the model's response. This approach improves the accuracy and relevance of generated text.

## Indexing and storage techniques

- [**_Text chunking_**](../../ingesting-data/text-chunking/index.md) involves splitting long documents or text passages into smaller segments to improve search retrieval and relevance. Chunking helps vector search models process large amounts of text more effectively.

- [**_Vector quantization_**](../../optimizing-storage/knn-vector-quantization/index.md) is a technique for reducing the storage size of vector embeddings by approximating them using a smaller set of representative vectors. This process enables efficient storage and retrieval in large-scale vector search applications.

- **_Scalar quantization (SQ)_** reduces vector precision by mapping floating-point values to a limited set of discrete values, decreasing memory requirements while preserving search accuracy.

- **_Product quantization (PQ)_** divides high-dimensional vectors into smaller subspaces and quantizes each subspace separately, enabling efficient approximate nearest neighbor search with reduced memory usage.

- **_Binary quantization_** compresses vector representations by converting numerical values to binary formats. This technique reduces storage requirements and accelerates similarity computations.

- [**_Disk-based vector search_**](../../optimizing-storage/disk-based-vector-search/index.md) stores vector embeddings on disk rather than in memory, using binary quantization to reduce memory consumption while maintaining search efficiency.
