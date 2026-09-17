---
collection: "opensearch"
version: "2.19"
title: "String field types"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/supported-field-types/string.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/supported-field-types/string.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/supported-field-types/string/"
canonical_url: "https://docs.opensearch.org/latest/mappings/supported-field-types/string/"
canonical_route: "/mappings/supported-field-types/string/"
redirect_from: ["/opensearch/supported-field-types/string/","/field-types/string/","/mappings/supported-field-types/string/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 45
parent: "Supported field types"
---
# String field types

String field types contain text values or values derived from text. The following table lists all string field types that OpenSearch supports.

Field data type | Description
:--- | :---
[`keyword`](../keyword/index.md) | A string that is not analyzed. Useful for exact-value search.
[`text`](../text/index.md) | A string that is analyzed. Useful for full-text search.
[`match_only_text`](../match-only-text/index.md) | A space-optimized version of a `text` field.
[`token_count`](../token-count/index.md)  | Counts the number of tokens in a string.
[`constant_keyword`](../constant-keyword/index.md)  | Similar to `keyword` but uses a single value for all documents.
[`wildcard`](../wildcard/index.md)  | A variation of `keyword` with efficient substring and regular expression matching.
