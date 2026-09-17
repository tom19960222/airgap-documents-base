---
collection: "opensearch"
version: "2.19"
title: "Source"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/metadata-fields/source.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/metadata-fields/source.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/metadata-fields/source/"
canonical_url: "https://docs.opensearch.org/latest/mappings/metadata-fields/source/"
canonical_route: "/mappings/metadata-fields/source/"
redirect_from: ["/mappings/metadata-fields/source/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 40
parent: "Metadata fields"
---
# Source

The `_source` field contains the original JSON document body that was indexed. While this field is not searchable, it is stored so that the full document can be returned when executing fetch requests, such as `get` and `search`.

## Disabling the field

You can disable the `_source` field by setting the `enabled` parameter to `false`, as shown in the following example request:

```json
PUT sample-index1
{
  "mappings": {
    "_source": {
      "enabled": false
    }
  }
}
```

Disabling the `_source` field can impact the availability of certain features, such as the `update`, `update_by_query`, and `reindex` APIs, as well as the ability to debug queries or aggregations using the original indexed document.
{: .warning}

## Including or excluding fields

You can selectively control the contents of the `_source` field by using the `includes` and `excludes` parameters. This allows you to prune the stored `_source` field after it is indexed but before it is saved, as shown in the following example request:

```json
PUT logs
{
  "mappings": {
    "_source": {
      "includes": [
        "*.count",
        "meta.*"
      ],
      "excludes": [
        "meta.description",
        "meta.other.*"
      ]
    }
  }
}
```

These fields are not stored in the `_source`, but you can still search them because the data remains indexed.
