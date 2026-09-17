---
collection: "opensearch"
version: "2.19"
title: "Vector search API"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_vector-search/api/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_vector-search/api/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/vector-search/api/"
canonical_url: "https://docs.opensearch.org/latest/vector-search/api/index/"
canonical_route: "/vector-search/api/"
redirect_from: ["/vector-search/api/knn/","/vector-search/api/","/search-plugins/knn/api/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 80
---
# Vector search API

In OpenSearch, vector search functionality is provided by the k-NN plugin and Neural Search plugin. The k-NN plugin provides basic k-NN functionality, while the Neural Search plugin provides automatic embedding generation at indexing and search time.

For k-NN plugin APIs, see [k-NN API](knn/index.md).

In addition to plugin-specific APIs, the following APIs support vector search functionality:

- [k-NN vector](../../field-types/supported-field-types/knn-vector/index.md)
- [k-NN query](../../query-dsl/specialized/k-nn/index.md)
- [Neural query](../../query-dsl/specialized/neural/index.md)
- [Neural sparse query](../../query-dsl/specialized/neural-sparse/index.md)
- [Ingest pipelines](../../ingest-pipelines/index.md)
- Ingest processors:
    - [ML inference](../../ingest-pipelines/processors/ml-inference/index.md)
    - [Sparse encoding](../../ingest-pipelines/processors/sparse-encoding/index.md)
    - [Text chunking](../../ingest-pipelines/processors/text-chunking/index.md)
    - [Text embedding](../../ingest-pipelines/processors/text-embedding/index.md)
    - [Text/image embedding](../../ingest-pipelines/processors/text-image-embedding/index.md)
- [Search pipelines](../../search-plugins/search-pipelines/index.md)
- Search processors:
    - [ML inference (request)](../../search-plugins/search-pipelines/ml-inference-search-request/index.md)
    - [ML inference (response)](../../search-plugins/search-pipelines/ml-inference-search-response/index.md)
    - [Neural query enricher](../../search-plugins/search-pipelines/neural-query-enricher/index.md)
    - [Neural sparse query two-phase](../../search-plugins/search-pipelines/neural-sparse-query-two-phase-processor/index.md)
    - [Normalization](../../search-plugins/search-pipelines/normalization-processor/index.md)
    - [Rerank](../../search-plugins/search-pipelines/rerank-processor/index.md)
    - [Retrieval-augmented generation](../../search-plugins/search-pipelines/rag-processor/index.md)
    - [Score ranker](../../search-plugins/search-pipelines/score-ranker-processor/index.md)
