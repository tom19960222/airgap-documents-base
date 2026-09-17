---
collection: "opensearch"
version: "2.19"
title: "Search"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/"
canonical_url: "https://docs.opensearch.org/latest/search-plugins/"
canonical_route: "/search-plugins/"
redirect_from: ["/search-plugins/index/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
ai: [{"heading":"AI search","description":"Build intelligent search applications using AI models","link":"/vector-search/ai-search/"}]
has_children: false
has_toc: false
keyword: [{"heading":"Keyword (BM25) search","description":"Find exact and close matches using traditional text search","link":"/search-plugins/keyword-search/"}]
layout: "default"
nav_exclude: true
nav_order: 1
vector: [{"heading":"Vector search","description":"Search by similarity using dense or sparse vector embeddings","link":"/vector-search/"}]
---
# Search features

OpenSearch provides many features for customizing your search use cases and improving search relevance.

## Search methods

OpenSearch supports the following search methods.

### Exact matching and keywords

OpenSearch implements lexical (keyword) text search using the BM25 algorithm to match and rank documents based on term frequency and document length.

<div class="card-container">

- [Keyword (BM25) search](keyword-search/index.md)
  Find exact and close matches using traditional text search

</div>

### Similarity and meaning

OpenSearch supports similarity (k-nearest neighbor) search using dense and sparse vector embeddings to power use cases such as semantic search, retrieval-augmented generation, and multimodal image search.

<div class="card-container">

- [Vector search](../vector-search/index.md)
  Search by similarity using dense or sparse vector embeddings

</div>

### AI-powered search

OpenSearch supports AI-powered search capabilities beyond vector embeddings. OpenSearch's AI search enables search and ingestion flows to be enriched by any AI service to power the full range of AI-enhanced search use cases.

<div class="card-container">

- [AI search](../vector-search/ai-search/index.md)
  Build intelligent search applications using AI models

</div>

## Query languages

In OpenSearch, you can use the following query languages to search your data:

- [Query domain-specific language (DSL)](../query-dsl/index.md): The primary OpenSearch query language that supports creating complex, fully customizable queries.

- [Query string query language](../query-dsl/full-text/query-string/index.md): A scaled-down query language that you can use in a query parameter of a search request or in OpenSearch Dashboards.

- [SQL](sql/sql/index.md): A traditional query language that bridges the gap between traditional relational database concepts and the flexibility of OpenSearch’s document-oriented data storage.

- [Piped Processing Language (PPL)](sql/ppl/index.md): The primary language used with observability in OpenSearch. PPL uses a pipe syntax that chains commands into a query.

- [Dashboards Query Language (DQL)](https://docs.opensearch.org/latest/dashboards/dql/) <!-- unresolved-cross-corpus-link: collection=opensearch-dashboards route=/dashboards/dql/ -->: A simple text-based query language for filtering data in OpenSearch Dashboards.

## Search performance

OpenSearch offers several ways to improve search performance:

- [Asynchronous search](async/index.md): Runs resource-intensive queries asynchronously.

- [Concurrent segment search](concurrent-segment-search/index.md): Searches segments concurrently.

## Search relevance

OpenSearch provides the following search relevance features:

- [Compare Search Results](search-relevance/compare-search-results/index.md): A search comparison tool in OpenSearch Dashboards that you can use to compare results from two queries side by side.

- [Querqy](querqy/index.md): Offers query rewriting capability.

- [User Behavior Insights](ubi/index.md): Links user behavior to user queries to improve search quality.

## Search results

OpenSearch supports the following commonly used operations on search results:

- [Paginate](searching-data/paginate/index.md)
- [Paginate with Point in Time](searching-data/point-in-time/index.md)
- [Sort](searching-data/sort/index.md)
- [Highlight search terms](searching-data/highlight/index.md)
- [Autocomplete](searching-data/autocomplete/index.md)
- [Did-you-mean](searching-data/did-you-mean/index.md)

## Search pipelines

You can process search queries and search results with [search pipelines](search-pipelines/index.md).
