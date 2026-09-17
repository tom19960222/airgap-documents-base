---
collection: "opensearch"
version: "2.19"
title: "Autocomplete field types"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/supported-field-types/autocomplete.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/supported-field-types/autocomplete.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/supported-field-types/autocomplete/"
canonical_url: "https://docs.opensearch.org/latest/mappings/supported-field-types/autocomplete/"
canonical_route: "/mappings/supported-field-types/autocomplete/"
redirect_from: ["/opensearch/supported-field-types/autocomplete/","/field-types/autocomplete/","/mappings/supported-field-types/autocomplete/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 50
parent: "Supported field types"
---
# Autocomplete field types

The following table lists all autocomplete field types that OpenSearch supports.

Field data type | Description
:--- | :---
[`completion`](../completion/index.md) | A completion suggester that provides autocomplete functionality using prefix completion. You need to upload a list of all possible completions into the index before using this feature.
[`search_as_you_type`](../search-as-you-type/index.md) | Provides search-as-you-type functionality using both prefix and infix completion.
