---
collection: "opensearch"
version: "2.19"
title: "Joining queries"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_query-dsl/joining/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_query-dsl/joining/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/query-dsl/joining/"
canonical_url: "https://docs.opensearch.org/latest/query-dsl/joining/index/"
canonical_route: "/query-dsl/joining/"
redirect_from: ["/query-dsl/joining/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 55
---
# Joining queries

OpenSearch is a distributed system in which data is spread across multiple nodes. Thus, running a SQL-like JOIN operation in OpenSearch is resource intensive. As an alternative, OpenSearch provides the following queries that perform join operations and are optimized for scaling across multiple nodes:

- Queries for searching [nested](../../field-types/supported-field-types/nested/index.md) fields:
    - `nested` queries: Act as wrappers for other queries to search [nested](../../field-types/supported-field-types/nested/index.md) fields. The nested field objects are searched as though they were indexed as separate documents.
- Queries for searching documents connected by a [join](../../field-types/supported-field-types/join/index.md) field type, which establishes a parent/child relationship between documents in the same index:
    - [`has_child`](has-child/index.md) queries: Search for parent documents whose child documents match the query.
    - [`has_parent`](has-parent/index.md) queries: Search for child documents whose parent documents match the query.
    - [`parent_id`](parent-id/index.md) queries: Search for child documents that are joined to a specific parent document.

If [`search.allow_expensive_queries`](../index.md#expensive-queries) is set to `false`, then joining queries are not executed.
{: .important}
