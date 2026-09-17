---
collection: "opensearch-dashboards"
version: "2.19"
title: "OpenSearch Dashboards"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_dashboards/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_dashboards/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/dashboards/"
canonical_url: "https://docs.opensearch.org/latest/dashboards/"
canonical_route: "/dashboards/"
redirect_from: ["/dashboards/index/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.1"
chart_version: ""
has_children: false
layout: "default"
nav_exclude: true
nav_order: 1
---
# OpenSearch Dashboards

OpenSearch Dashboards is the user interface that lets you visualize your OpenSearch data and run and scale your OpenSearch clusters.

## Getting started

| Concept | Description |
|---------|-------------|
| [OpenSearch Dashboards Quickstart](quickstart/index.md) | Learn about the basic concepts and features of OpenSearch Dashboards. |
| [OpenSearch Playground](https://playground.opensearch.org/app/home#/) | Explore features in OpenSearch Dashboards without downloading or installing anything. |
| [Install and configure OpenSearch Dashboards](https://docs.opensearch.org/latest/install-and-configure/install-dashboards/index/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/install-and-configure/install-dashboards/ --> | Get started with OpenSearch Dashboards. |
| [Create visualizations](visualize/viz-index/index.md) | Learn about visualizing data in OpenSearch Dashboards. |
| [Explore and query data](discover/index-discover/index.md) | Learn how to explore and query data in OpenSearch. |

## Query languages

Query language | Where you can use it | Description
:--- | :--- | :---
[Query domain-specific language (DSL)](https://docs.opensearch.org/latest/query-dsl/index/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/query-dsl/ --> | [Dev Tools](dev-tools/index-dev/index.md) | The primary OpenSearch query language that supports creating complex, fully customizable queries.
[Dashboards Query Language (DQL)](dql/index.md) | [Discover](discover/index-discover/index.md) and [Dashboard](dashboard/index.md) search bar | A simple text-based query language used to filter data in OpenSearch Dashboards.
[Query string query language](https://docs.opensearch.org/latest/query-dsl/full-text/query-string/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/query-dsl/full-text/query-string/ --> | [Discover](discover/index-discover/index.md) and [Dashboard](dashboard/index.md) search bar | A scaled-down query language whose syntax is based on the Apache Lucene query syntax.
[SQL](https://docs.opensearch.org/latest/search-plugins/sql/sql/index/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/search-plugins/sql/sql/ --> | [Query Workbench](query-workbench/index.md) | A traditional query language that bridges the gap between relational database concepts and the flexibility of OpenSearch’s document-oriented data storage.
[Piped Processing Language (PPL)](https://docs.opensearch.org/latest/search-plugins/sql/ppl/index/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/search-plugins/sql/ppl/ --> | [Query Workbench](query-workbench/index.md) | The primary language used with observability in OpenSearch. PPL uses a pipe syntax that chains commands into a query.

### Discover and Dashboard search bar

Using the search bar in the [Discover](discover/index-discover/index.md) and [Dashboard](dashboard/index.md) apps, you can search data with the following two languages:

- [DQL](dql/index.md)

- [Query string query (Lucene)](https://docs.opensearch.org/latest/query-dsl/full-text/query-string/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/query-dsl/full-text/query-string/ -->

The following table compares DQL and query string query language features.

DQL and query string query language | DQL | Query string query language
:--- | :--- | :---
- Wildcard expressions (DQL supports `*` only)<br> - Ranges<br> - Boolean operations<br> | - Querying nested fields | - Regular expressions<br> - Fuzziness<br> - Proximity queries<br> - Boosting

By default, the query language in the Discover search toolbar is DQL. To switch to query string syntax, select **DQL** and then turn off **OpenSearch Dashboards Query Language**. The query language changes to `Lucene`, as shown in the following image.

![Using query string syntax in OpenSearch Dashboards Discover](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/discover-lucene-syntax.png)

## Observability

| Concept | Description |
|---------|-------------|
| [Observability in OpenSearch Dashboards](https://docs.opensearch.org/latest//observing-your-data/index/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/observing-your-data/ --> | Observe, monitor, and secure data and improve performance across tools and workflows. |

## Dashboards Management

| Concept | Description |
|---------|-------------|
| [Dashboards Management](management/management-index/index.md) | Learn about the command center for customizing your OpenSearch Dashboards behavior, creating index patterns, and configuring data sources. |

## Dev Tools

| Concept | Description |
|---------|-------------|
| [Dev Tools](dev-tools/index-dev/index.md) | Learn how to run OpenSearch queries in an integrated console. |
