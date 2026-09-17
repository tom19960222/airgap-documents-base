---
collection: "opensearch"
version: "2.19"
title: "Compound queries"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_query-dsl/compound/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_query-dsl/compound/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/query-dsl/compound/"
canonical_url: "https://docs.opensearch.org/latest/query-dsl/compound/index/"
canonical_route: "/query-dsl/compound/"
redirect_from: ["/opensearch/query-dsl/compound/index/","/query-dsl/compound/index/","/query-dsl/query-dsl/compound/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 40
---
# Compound queries

Compound queries serve as wrappers for multiple leaf or compound clauses either to combine their results or to modify their behavior.

The following table lists all compound query types.

Query type | Description
:--- | :---
[`bool`](bool/index.md) (Boolean)| Combines multiple query clauses with Boolean logic.
[`boosting`](boosting/index.md) | Changes the relevance score of documents without removing them from the search results. Returns documents that match a `positive` query, but downgrades the relevance of documents in the results that match a `negative` query.
[`constant_score`](constant-score/index.md) | Wraps a query or a filter and assigns a constant score to all matching documents. This score is equal to the `boost` value.
[`dis_max`](disjunction-max/index.md) (disjunction max) | Returns documents that match one or more query clauses. If a document matches multiple query clauses, it is assigned a higher relevance score. The relevance score is calculated using the highest score from any matching clause and, optionally, the scores from the other matching clauses multiplied by the tiebreaker value.
[`function_score`](function-score/index.md) | Recalculates the relevance score of documents that are returned by a query using a function that you define.
[`hybrid`](hybrid/index.md) | Combines relevance scores from multiple queries into one score for a given document.
