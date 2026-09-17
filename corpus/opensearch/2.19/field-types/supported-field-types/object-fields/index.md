---
collection: "opensearch"
version: "2.19"
title: "Object field types"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/supported-field-types/object-fields.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/supported-field-types/object-fields.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/supported-field-types/object-fields/"
canonical_url: "https://docs.opensearch.org/latest/mappings/supported-field-types/object-fields/"
canonical_route: "/mappings/supported-field-types/object-fields/"
redirect_from: ["/opensearch/supported-field-types/object-fields/","/field-types/object-fields/","/mappings/supported-field-types/object-fields/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 40
parent: "Supported field types"
---
# Object field types

Object field types contain values that are objects or relations. The following table lists all object field types that OpenSearch supports.

Field data type | Description
:--- | :---
[`object`](../object/index.md) | A JSON object.
[`nested`](../nested/index.md) | Used when objects in an array need to be indexed independently as separate documents.
[`flat_object`](../flat-object/index.md) | A JSON object treated as a string.
[`join`](../join/index.md) | Establishes a parent/child relationship between documents in the same index.
