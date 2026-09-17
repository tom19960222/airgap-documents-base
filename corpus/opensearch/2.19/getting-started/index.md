---
collection: "opensearch"
version: "2.19"
title: "Getting started"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_getting-started/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_getting-started/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/getting-started/"
canonical_url: "https://docs.opensearch.org/latest/getting-started/"
canonical_route: "/getting-started/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_exclude: true
nav_order: 1
---
# Getting started

OpenSearch is a distributed search and analytics engine based on [Apache Lucene](https://lucene.apache.org/). After adding your data to OpenSearch, you can perform full-text searches on it with all of the features you might expect: search by field, search multiple indexes, boost fields, rank results by score, sort results by field, and aggregate results.

Unsurprisingly, builders often use a search engine like OpenSearch as the backend for a search application---think [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:FAQ/Technical#What_software_is_used_to_run_Wikipedia?) or an online store. It offers excellent performance and can scale up or down as the needs of the application grow or shrink.

An equally popular, but less obvious use case is log analytics, in which you take the logs from an application, feed them into OpenSearch, and use the rich search and visualization functionality to identify issues. For example, a malfunctioning web server might throw a 500 error 0.5% of the time, which can be hard to notice unless you have a real-time graph of all HTTP status codes that the server has thrown in the past four hours. You can use [OpenSearch Dashboards](https://docs.opensearch.org/latest/dashboards/index/) <!-- unresolved-cross-corpus-link: collection=opensearch-dashboards route=/dashboards/ --> to build these sorts of visualizations from data in OpenSearch.

## Components

OpenSearch is more than just the core engine. It also includes the following components:

- [OpenSearch Dashboards](https://docs.opensearch.org/latest/dashboards/index/) <!-- unresolved-cross-corpus-link: collection=opensearch-dashboards route=/dashboards/ -->: The OpenSearch data visualization UI.
- [Data Prepper](https://docs.opensearch.org/latest/data-prepper/) <!-- unresolved-jekyll-link: route=/data-prepper/ -->: A server-side data collector capable of filtering, enriching, transforming, normalizing, and aggregating data for downstream analysis and visualization.
- [Clients](https://docs.opensearch.org/latest/clients/) <!-- unresolved-jekyll-link: route=/clients/ -->: Language APIs that let you communicate with OpenSearch in several popular programming languages.

## Use cases

OpenSearch supports a variety of use cases, for example:

- [Observability](../observing-your-data/index.md): Visualize data-driven events by using Piped Processing Language (PPL) to explore, discover, and query data stored in OpenSearch.
- [Search](../search-plugins/index.md): Choose the best search method for your application, from regular lexical search to conversational search powered by machine learning (ML).
- [Machine learning](../ml-commons-plugin/index.md): Integrate ML models into your OpenSearch application.
- [Security analytics](../security-analytics/index.md): Investigate, detect, analyze, and respond to security threats that can jeopardize organizational success and online operations.

## Next steps

- See [Introduction to OpenSearch](intro/index.md) to learn about essential OpenSearch concepts.
