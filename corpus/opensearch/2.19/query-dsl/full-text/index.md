---
collection: "opensearch"
version: "2.19"
title: "Full-text queries"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_query-dsl/full-text/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_query-dsl/full-text/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/query-dsl/full-text/"
canonical_url: "https://docs.opensearch.org/latest/query-dsl/full-text/index/"
canonical_route: "/query-dsl/full-text/"
redirect_from: ["/opensearch/query-dsl/full-text/","/query-dsl/query-dsl/full-text/","/query-dsl/full-text/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 30
---
# Full-text queries

This page lists all full-text query types and common options. There are many optional fields that you can use to create subtle search behaviors, so we recommend that you test out some basic query types against representative indexes and verify the output before you perform more advanced or complex searches with multiple options.

OpenSearch uses the Apache Lucene search library, which provides highly efficient data structures and algorithms for ingesting, indexing, searching, and aggregating data.

To learn more about search query classes, see [Lucene query JavaDocs](https://lucene.apache.org/core/8_9_0/core/org/apache/lucene/search/Query.html).

The full-text query types shown in this section use the standard analyzer, which analyzes text automatically when the query is submitted.

The following table lists all full-text query types.

Query type | Description
:--- | :---
[`intervals`](intervals/index.md) | Allows fine-grained control of the matching terms' proximity and order.
[`match`](match/index.md) | The default full-text query, which can be used for fuzzy matching and phrase or proximity searches.
[`match_bool_prefix`](match-bool-prefix/index.md) | Creates a [Boolean query](../compound/bool/index.md) that matches all terms in any position, treating the last term as a prefix.
[`match_phrase`](match-phrase/index.md) | Similar to the `match` query but matches a whole phrase up to a configurable slop.
[`match_phrase_prefix`](match-phrase-prefix/index.md) | Similar to the `match_phrase` query but matches terms as a whole phrase, treating the last term as a prefix.
[`multi_match`](multi-match/index.md) | Similar to the `match` query but is used on multiple fields.
[`query_string`](query-string/index.md) | Uses a strict syntax to specify Boolean conditions and multi-field search within a single query string.
[`simple_query_string`](simple-query-string/index.md) | A simpler, less strict version of `query_string` query.
