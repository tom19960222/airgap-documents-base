---
collection: "opensearch"
version: "2.19"
title: "Term-level queries"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_query-dsl/term/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_query-dsl/term/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/query-dsl/term/"
canonical_url: "https://docs.opensearch.org/latest/query-dsl/term/index/"
canonical_route: "/query-dsl/term/"
redirect_from: ["/opensearch/query-dsl/term/","/query-dsl/term/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 20
---
# Term-level queries

Term-level queries search an index for documents that contain an exact search term. Documents returned by a term-level query are not sorted by their relevance scores.

When working with text data, use term-level queries for fields mapped as `keyword` only.

Term-level queries are not suited for searching analyzed text fields. To return analyzed fields, use a [full-text query](../full-text/index.md).

## Term-level query types

The following table lists all term-level query types.

Query type | Description
:--- | :---
[`term`](term/index.md) | Searches for documents containing an exact term in a specific field.
[`terms`](terms/index.md) | Searches for documents containing one or more terms in a specific field.
[`terms_set`](terms-set/index.md) | Searches for documents that match a minimum number of terms in a specific field.
[`ids`](ids/index.md) | Searches for documents by document ID.
[`range`](range/index.md) | Searches for documents with field values in a specific range.
[`prefix`](prefix/index.md) | Searches for documents containing terms that begin with a specific prefix.
[`exists`](exists/index.md) | Searches for documents with any indexed value in a specific field.
[`fuzzy`](fuzzy/index.md) | Searches for documents containing terms that are similar to the search term within the maximum allowed [Damerau–Levenshtein distance](https://en.wikipedia.org/wiki/Damerau–Levenshtein_distance). The Damerau–Levenshtein distance measures the number of one-character changes needed to change one term to another term.
[`wildcard`](wildcard/index.md) | Searches for documents containing terms that match a wildcard pattern.
[`regexp`](regexp/index.md) | Searches for documents containing terms that match a regular expression.
