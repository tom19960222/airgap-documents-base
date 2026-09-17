---
collection: "opensearch"
version: "2.19"
title: "Vector quantization"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_vector-search/optimizing-storage/knn-vector-quantization.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_vector-search/optimizing-storage/knn-vector-quantization.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/vector-search/optimizing-storage/knn-vector-quantization/"
canonical_url: "https://docs.opensearch.org/latest/vector-search/optimizing-storage/knn-vector-quantization/"
canonical_route: "/vector-search/optimizing-storage/knn-vector-quantization/"
redirect_from: ["/search-plugins/knn/knn-vector-quantization/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
inside_cards: [{"heading":"Lucene scalar quantization","description":"Use built-in scalar quantization for the Lucene engine","link":"/vector-search/optimizing-storage/lucene-scalar-quantization/"},{"heading":"Faiss 16-bit scalar quantization","description":"Use built-in scalar quantization for the Faiss engine","link":"/vector-search/optimizing-storage/faiss-16-bit-quantization/"},{"heading":"Faiss product quantization","description":"Use built-in product quantization for the Faiss engine","link":"/vector-search/optimizing-storage/faiss-product-quantization/"},{"heading":"Binary quantization","description":"Use built-in binary quantization for the Faiss engine","link":"/vector-search/optimizing-storage/binary-quantization/"}]
layout: "default"
nav_order: 10
outside_cards: [{"heading":"Byte vectors","description":"Quantize vectors into byte vectors","link":"/field-types/supported-field-types/knn-memory-optimized/#byte-vectors"},{"heading":"Binary vectors","description":"Quantize vectors into binary vector","link":"/field-types/supported-field-types/knn-memory-optimized/#binary-vectors"}]
parent: "Optimizing vector storage"
---
# Vector quantization

By default, OpenSearch supports the indexing and querying of vectors of type `float`, where each dimension of the vector occupies 4 bytes of memory. For use cases that require ingestion on a large scale, keeping `float` vectors can be expensive because OpenSearch needs to construct, load, save, and search graphs (for the native `faiss` and `nmslib` [deprecated] engines). To reduce the memory footprint, you can use vector quantization.

OpenSearch supports many varieties of quantization. In general, the level of quantization will provide a trade-off between the accuracy of the nearest neighbor search and the size of the memory footprint consumed by the vector search.

## Quantize vectors outside of OpenSearch

Quantize vectors outside of OpenSearch before ingesting them into an OpenSearch index.

<div class="card-container">

- [Byte vectors](../../../field-types/supported-field-types/knn-memory-optimized/index.md#byte-vectors)
  Quantize vectors into byte vectors

- [Binary vectors](../../../field-types/supported-field-types/knn-memory-optimized/index.md#binary-vectors)
  Quantize vectors into binary vector

</div>

## Quantize vectors within OpenSearch

Use OpenSearch built-in quantization to quantize vectors.

<div class="card-container">

- [Lucene scalar quantization](../lucene-scalar-quantization/index.md)
  Use built-in scalar quantization for the Lucene engine

- [Faiss 16-bit scalar quantization](../faiss-16-bit-quantization/index.md)
  Use built-in scalar quantization for the Faiss engine

- [Faiss product quantization](../faiss-product-quantization/index.md)
  Use built-in product quantization for the Faiss engine

- [Binary quantization](../binary-quantization/index.md)
  Use built-in binary quantization for the Faiss engine

</div>
