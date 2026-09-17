---
collection: "opensearch"
version: "2.19"
title: "Meta"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/metadata-fields/meta.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/metadata-fields/meta.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/metadata-fields/meta/"
canonical_url: "https://docs.opensearch.org/latest/mappings/metadata-fields/meta/"
canonical_route: "/mappings/metadata-fields/meta/"
redirect_from: ["/mappings/metadata-fields/meta/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 30
parent: "Metadata fields"
---
# Meta

The `_meta` field is a mapping property that allows you to attach custom metadata to your index mappings. This metadata can be used by your application to store information relevant to your use case, such as versioning, ownership, categorization, or auditing.

## Usage

You can define the `_meta` field when creating a new index or updating an existing index's mapping, as shown in the following example request:

```json
PUT my-index
{
  "mappings": {
    "_meta": {
      "application": "MyApp",
      "version": "1.2.3",
      "author": "John Doe"
    },
    "properties": {
      "title": {
        "type": "text"
      },
      "description": {
        "type": "text"
      }
    }
  }
}

```

In this example, three custom metadata fields are added: `application`, `version`, and `author`. These fields can be used by your application to store any relevant information about the index, such as the application it belongs to, the application version, or the author of the index.

You can update the `_meta` field using the [Put Mapping API](../../../api-reference/index-apis/put-mapping/index.md) operation, as shown in the following example request:

```json
PUT my-index/_mapping
{
  "_meta": {
    "application": "MyApp",
    "version": "1.3.0",
    "author": "Jane Smith"
  }
}
```

## Retrieving `meta` information

You can retrieve the `_meta` information for an index using the [Get Mapping API](../../index.md#get-a-mapping) operation, as shown in the following example request:

```json
GET my-index/_mapping
```

The response returns the full index mapping, including the `_meta` field:

```json
{
  "my-index": {
    "mappings": {
      "_meta": {
        "application": "MyApp",
        "version": "1.3.0",
        "author": "Jane Smith"
      },
      "properties": {
        "description": {
          "type": "text"
        },
        "title": {
          "type": "text"
        }
      }
    }
  }
}
```
