---
collection: "opensearch"
version: "2.19"
title: "Reranking search results"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/search-relevance/reranking-search-results.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/search-relevance/reranking-search-results.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/search-relevance/reranking-search-results/"
canonical_url: "https://docs.opensearch.org/latest/search-plugins/search-relevance/reranking-search-results/"
canonical_route: "/search-plugins/search-relevance/reranking-search-results/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
layout: "default"
nav_order: 60
parent: "Search relevance"
---
# Reranking search results
Introduced 2.12
{: .label .label-purple }

You can rerank search results using a [`rerank` processor](../../search-pipelines/rerank-processor/index.md) in order to improve search relevance. To implement reranking, you need to configure a [search pipeline](../../search-pipelines/index.md) that runs at search time. The search pipeline intercepts search results and applies the `rerank` processor to them. The `rerank` processor evaluates the search results and sorts them based on the new scores.

You can rerank results in the following ways:

- [Using a cross-encoder model](../rerank-cross-encoder/index.md)
- [By a document field](../rerank-by-field/index.md)

## Using rerank and normalization processors together

When you use a rerank processor in conjunction with a [normalization processor](../../search-pipelines/normalization-processor/index.md) and a hybrid query, the rerank processor alters the final document scores. This is because the rerank processor operates after the normalization processor in the search pipeline.
{: .note}

The processing order is as follows:

- Normalization processor: This processor normalizes the document scores based on the configured normalization method. For more information, see [Normalization processor](../../search-pipelines/normalization-processor/index.md).
- Rerank processor: Following normalization, the rerank processor further adjusts the document scores. This adjustment can significantly impact the final ordering of search results.

This processing order has the following implications:

- Score modification: The rerank processor modifies the scores that were initially adjusted by the normalization processor, potentially leading to different ranking results than initially expected.
- Hybrid queries: In the context of hybrid queries, where multiple types of queries and scoring mechanisms are combined, this behavior is particularly noteworthy. The combined scores from the initial query are normalized first and then reranked, resulting in a two-phase scoring modification.

## Next steps

- See a complete example of [reranking using a cross-encoder model](../rerank-cross-encoder/index.md).
- See a complete example of [reranking by a document field](../rerank-by-field/index.md).
- Learn more about the [`rerank` processor](../../search-pipelines/rerank-processor/index.md).
