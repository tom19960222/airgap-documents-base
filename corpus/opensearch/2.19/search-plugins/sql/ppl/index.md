---
collection: "opensearch"
version: "2.19"
title: "PPL"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/sql/ppl/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/sql/ppl/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/sql/ppl/"
canonical_url: "https://docs.opensearch.org/latest/sql-and-ppl/ppl/index/"
canonical_route: "/sql-and-ppl/ppl/"
redirect_from: ["/search-plugins/sql/ppl/","/search-plugins/ppl/","/observability-plugin/ppl/","/search-plugins/ppl/endpoint/","/search-plugins/ppl/protocol/","/sql-and-ppl/ppl/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 5
parent: "SQL and PPL"
---
# PPL

Piped Processing Language (PPL) is a query language that focuses on processing data in a sequential, step-by-step manner. PPL uses the pipe (`|`) operator to combine commands to find and retrieve data. It is particularly well suited for analyzing observability data, such as logs, metrics, and traces, due to its ability to handle semi-structured data efficiently.

## PPL syntax

The following example shows the basic PPL syntax:

```sql
search source=<index-name> | <command_1> | <command_2> | ... | <command_n>
```

See [Syntax](syntax/index.md) for specific PPL syntax examples.

## PPL commands

PPL filters, transforms, and aggregates data using a series of commands. See [Commands](functions/index.md) for a description and an example of each command.

## Using PPL within OpenSearch

The SQL plugin is required to run PPL queries in OpenSearch. If you're running a minimal distribution of OpenSearch, you might have to [install the SQL plugin](../../../install-and-configure/plugins/index.md) before using PPL.
{: .note}

You can run PPL queries interactively in OpenSearch Dashboards or programmatically using the ``_ppl`` endpoint.

In OpenSearch Dashboards, the [Query Workbench tool](https://playground.opensearch.org/app/opensearch-query-workbench#/) provides an interactive testing environment, documented in [Query Workbench documentation](https://docs.opensearch.org/latest/dashboards/query-workbench/) <!-- unresolved-cross-corpus-link: collection=opensearch-dashboards route=/dashboards/query-workbench/ -->.

To run a PPL query using the API, see [SQL and PPL API](../sql-ppl-api/index.md).

## Developer documentation

Developers can find information in the following resources:

- [Piped Processing Language](https://github.com/opensearch-project/piped-processing-language) specification
- [OpenSearch PPL Reference Manual](https://github.com/opensearch-project/sql/blob/main/docs/user/ppl/index.rst)
- [Observability](https://github.com/opensearch-project/dashboards-observability/) using [PPL-based visualizations](https://github.com/opensearch-project/dashboards-observability#event-analytics)
- PPL [Data Types](https://github.com/opensearch-project/sql/blob/main/docs/user/ppl/general/datatypes.rst)
- [Cross-cluster search](https://github.com/opensearch-project/sql/blob/main/docs/user/ppl/admin/cross_cluster_search.rst#using-cross-cluster-search-in-ppl) in PPL
