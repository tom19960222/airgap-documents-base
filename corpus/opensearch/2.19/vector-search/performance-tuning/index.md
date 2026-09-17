---
collection: "opensearch"
version: "2.19"
title: "Performance tuning"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_vector-search/performance-tuning.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_vector-search/performance-tuning.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/vector-search/performance-tuning/"
canonical_url: "https://docs.opensearch.org/latest/vector-search/performance-tuning/"
canonical_route: "/vector-search/performance-tuning/"
redirect_from: ["/search-plugins/knn/performance-tuning/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
layout: "default"
nav_order: 70
---
# Performance tuning

This topic provides performance tuning recommendations for improving indexing and search performance for approximate k-NN (ANN) search. At a high level, k-NN works according to these principles:
* Vector indexes are created per `knn_vector` field/Lucene segment pair.
* Queries execute sequentially on segments in the shard (as with any other OpenSearch query).
* The coordinator node selects the final `size` neighbors from the neighbors returned by each shard.

The following sections provide recommendations regarding comparing ANN to exact k-NN with a scoring script.

## Recommendations for engines and cluster node sizing

Each of the three engines used for ANN search has attributes that make it more sensible to use than the others in a given situation. Use the following information to help determine which engine will best meet your requirements.

To optimize for indexing throughput, Faiss is a good option. For relatively smaller datasets (up to a few million vectors), the Lucene engine demonstrates better latencies and recall. At the same time, the size of the index is smallest compared to the other engines, which allows it to use smaller AWS instances for data nodes. For further considerations, see [Choosing the right method](../../field-types/supported-field-types/knn-methods-engines/index.md#choosing-the-right-method) and [Memory estimation](../../field-types/supported-field-types/knn-methods-engines/index.md#memory-estimation).

When considering cluster node sizing, a general approach is to first establish an even distribution of the index across the cluster. However, there are other considerations. To help make these choices, you can refer to the OpenSearch managed service guidance in the [Sizing domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/sizing-domains.html) section.

## Improving recall

Recall depends on multiple factors, such as the number of vectors, dimensions, segments, and so on. Searching a large number of small segments and aggregating the results leads to better recall than searching a small number of large segments and aggregating the results. Larger native library indexes are more likely to lose recall if you're using smaller algorithm parameters. Choosing larger values for algorithm parameters should help solve this issue but sacrifices search latency and indexing time. It's important to understand your system's requirements for latency and accuracy and then choose the number of segments based on experimentation.

The default parameters work for a broader set of use cases, but make sure to run your own experiments on your datasets and choose the appropriate values. For index-level settings, see [Index settings](../settings/index.md#index-settings).

## ANN compared to scoring script

The standard k-NN query and custom scoring options perform differently. Run tests with a representative set of documents to see if the search results and latencies match your expectations.

Custom scoring works best if the initial filter reduces the number of documents to no more than 20,000. Increasing the shard count can improve latency, but be sure to keep the shard size within the [recommended guidelines](../../getting-started/intro/index.md#primary-and-replica-shards).
