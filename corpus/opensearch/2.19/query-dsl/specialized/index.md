---
collection: "opensearch"
version: "2.19"
title: "Specialized queries"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_query-dsl/specialized/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_query-dsl/specialized/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/query-dsl/specialized/"
canonical_url: "https://docs.opensearch.org/latest/query-dsl/specialized/index/"
canonical_route: "/query-dsl/specialized/"
redirect_from: ["/query-dsl/specialized/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 65
---
# Specialized queries

OpenSearch supports the following specialized queries:

- `distance_feature`: Calculates document scores based on the dynamically calculated distance between the origin and a document's `date`, `date_nanos`, or `geo_point` fields. This query can skip non-competitive hits.

- `more_like_this`: Finds documents similar to the provided text, document, or collection of documents.

- [`knn`](k-nn/index.md): Used for searching raw vectors during [vector search](../../vector-search/index.md).

- [`neural`](neural/index.md): Used for searching by text or image in [vector search](../../vector-search/ai-search/index.md).

- [`neural_sparse`](neural-sparse/index.md): Used for vector field search in [sparse neural search](../../vector-search/ai-search/neural-sparse-search/index.md).

- `percolate`: Finds queries (stored as documents) that match the provided document.

- `rank_feature`: Calculates scores based on the values of numeric features. This query can skip non-competitive hits.

- `script`: Uses a script as a filter.

- [`script_score`](script-score/index.md): Calculates a custom score for matching documents using a script.

- `wrapper`: Accepts other queries as JSON or YAML strings.
