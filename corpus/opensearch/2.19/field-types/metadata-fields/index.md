---
collection: "opensearch"
version: "2.19"
title: "Metadata fields"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/metadata-fields/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/metadata-fields/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/metadata-fields/"
canonical_url: "https://docs.opensearch.org/latest/mappings/metadata-fields/index/"
canonical_route: "/mappings/metadata-fields/"
redirect_from: ["/mappings/metadata-fields/index/","/field-types/metadata-fields/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 90
---
# Metadata fields

OpenSearch provides built-in metadata fields that allow you to access information about the documents in an index. These fields can be used in your queries as needed.

Metadata field | Description
:--- | :---
`_field_names` | The document fields with non-empty or non-null values.
`_ignored` | The document fields that were ignored during the indexing process due to the presence of malformed data, as specified by the `ignore_malformed` setting.
`_id` |  The unique identifier assigned to each document.
`_index` | The index in which the document is stored.
`_meta` | Stores custom metadata or additional information specific to the application or use case.
`_routing` | Allows you to specify a custom value that determines the shard assignment for a document in an OpenSearch cluster.
`_source` | Contains the original JSON representation of the document data.
