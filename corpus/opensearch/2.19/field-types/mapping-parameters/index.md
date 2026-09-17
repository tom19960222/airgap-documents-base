---
collection: "opensearch"
version: "2.19"
title: "Mapping parameters"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/mapping-parameters/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/mapping-parameters/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/mapping-parameters/"
canonical_url: "https://docs.opensearch.org/latest/mappings/mapping-parameters/index/"
canonical_route: "/mappings/mapping-parameters/"
redirect_from: ["/mappings/mapping-parameters/index/","/field-types/mapping-parameters/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 75
---
# Mapping parameters

Mapping parameters are used to configure the behavior of index fields. For parameter use cases, see a mapping parameter's respective page.

The following table lists OpenSearch mapping parameters.

Parameter | Description
:--- | :---
[`analyzer`](analyzer/index.md) | Specifies the analyzer used to analyze string fields. Default is the `standard` analyzer, which is a general-purpose analyzer that splits text on white space and punctuation, converts to lowercase, and removes stop words. Allowed values are `standard`, `simple`, or `whitespace`.
[`boost`](boost/index.md) | Specifies a field-level boost factor applied at query time. Allows you to increase or decrease the relevance score of a specific field during search queries. Default boost value is `1.0`, which means that no boost is applied. Allowed values are any positive floating-point number.
[`coerce`](coerce/index.md) | Controls how values are converted to the expected field data type during indexing. Default value is `true`, which means that OpenSearch tries to coerce the value to the expected value type. Allowed values are `true` or `false`.
[`copy_to`](copy-to/index.md) | Copies the value of a field to another field. There is no default value for this parameter. Optional.
[`doc_values`](doc-values/index.md) | Specifies whether a field should be stored on disk to make sorting and aggregation faster. Default value is `true`, which means that the doc values are enabled. Allowed values are a single field name or a list of field names.
[`dynamic`](dynamic/index.md) | Determines whether new fields should be added dynamically. Default value is `true`, which means that new fields can be added dynamically. Allowed values are `true`, `false`, or `strict`.
[`enabled`](enabled/index.md) | Specifies whether the field is enabled or disabled. Default value is `true`, which means that the field is enabled. Allowed values are `true` or `false`.
[`format`](format/index.md) | Specifies the date format for date fields. There is no default value for this parameter. Allowed values are any valid date format string, such as `yyyy-MM-dd` or `epoch_millis`.
[`ignore_above`](ignore-above/index.md) | Skips indexing values that exceed the specified length. Default value is `2147483647`, which means that there is no limit on the field value length. Allowed values are any positive integer.
[`ignore_malformed`](ignore-malformed/index.md) | Specifies whether malformed values should be ignored. Default value is `false`, which means that malformed values are not ignored. Allowed values are `true` or `false`.
[`index`](index-parameter/index.md) | Specifies whether a field should be indexed. Default value is `true`, which means that the field is indexed. Allowed values are `true` or `false`.
[`index_options`](index-options/index.md) | Specifies what information should be stored in an index for scoring purposes. Default value is `docs`, which means that only the document numbers are stored in the index. Allowed values are `docs`, `freqs`, `positions`, or `offsets`.
