---
collection: "opensearch"
version: "2.19"
title: "Analyzers"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/supported-analyzers/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/supported-analyzers/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/supported-analyzers/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/supported-analyzers/index/"
canonical_route: "/analyzers/supported-analyzers/"
redirect_from: ["/analyzers/supported-analyzers/index/"]
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
# Analyzers

The following sections list all analyzers that OpenSearch supports.

## Built-in analyzers

The following table lists the built-in analyzers that OpenSearch provides. The last column of the table contains the result of applying the analyzer to the string `It’s fun to contribute a brand-new PR or 2 to OpenSearch!`.

Analyzer | Analysis performed | Analyzer output
:--- | :--- | :---
[**Standard**](standard/index.md) (default) | - Parses strings into tokens at word boundaries <br> - Removes most punctuation <br> - Converts tokens to lowercase | [`it’s`, `fun`, `to`, `contribute`, `a`,`brand`, `new`, `pr`, `or`, `2`, `to`, `opensearch`]
[**Simple**](simple/index.md) | - Parses strings into tokens on any non-letter character <br> - Removes non-letter characters <br> - Converts tokens to lowercase  | [`it`, `s`, `fun`, `to`, `contribute`, `a`,`brand`, `new`, `pr`, `or`, `to`, `opensearch`]
[**Whitespace**](whitespace/index.md) | - Parses strings into tokens on white space | [`It’s`, `fun`, `to`, `contribute`, `a`,`brand-new`, `PR`, `or`, `2`, `to`, `OpenSearch!`]
[**Stop**](stop/index.md) | - Parses strings into tokens on any non-letter character <br> - Removes non-letter characters <br> - Removes stop words <br> - Converts tokens to lowercase | [`s`, `fun`, `contribute`, `brand`, `new`, `pr`, `opensearch`]
[**Keyword**](keyword/index.md) (no-op) | - Outputs the entire string unchanged | [`It’s fun to contribute a brand-new PR or 2 to OpenSearch!`]
[**Pattern**](pattern/index.md)| - Parses strings into tokens using regular expressions <br> - Supports converting strings to lowercase <br> - Supports removing stop words | [`it`, `s`, `fun`, `to`, `contribute`, `a`,`brand`, `new`, `pr`, `or`, `2`, `to`, `opensearch`]
[**Language**](../language-analyzers/index.md) | Performs analysis specific to a certain language (for example, `english`). | [`fun`, `contribut`, `brand`, `new`, `pr`, `2`, `opensearch`]
[**Fingerprint**](fingerprint/index.md) | - Parses strings on any non-letter character <br> - Normalizes characters by converting them to ASCII <br> - Converts tokens to lowercase <br> - Sorts, deduplicates, and concatenates tokens into a single token <br> - Supports removing stop words | [`2 a brand contribute fun it's new opensearch or pr to`] <br> Note that the apostrophe was converted to its ASCII counterpart.

## Language analyzers

OpenSearch supports multiple language analyzers. For more information, see [Language analyzers](../language-analyzers/index.md).

## Additional analyzers

The following table lists the additional analyzers that OpenSearch supports.

| Analyzer       | Analysis performed                                                                                       |
|:---------------|:---------------------------------------------------------------------------------------------------------|
| [`phone`](phone-analyzers/index.md#the-phone-analyzer)       | An [index analyzer](../index-analyzers/index.md) for parsing phone numbers.  |
| [`phone-search`](phone-analyzers/index.md#the-phone-search-analyzer) | A [search analyzer](../search-analyzers/index.md) for parsing phone numbers. |
