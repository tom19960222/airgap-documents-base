---
collection: "opensearch"
version: "2.19"
title: "Meta"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/mapping-parameters/meta.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/mapping-parameters/meta.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/mapping-parameters/meta/"
canonical_url: "https://docs.opensearch.org/latest/mappings/mapping-parameters/meta/"
canonical_route: "/mappings/mapping-parameters/meta/"
redirect_from: ["/mappings/mapping-parameters/meta/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Mapping and field types"
has_children: false
has_toc: false
layout: "default"
nav_order: 100
parent: "Mapping parameters"
---
# Meta

The `_meta` mapping parameter allows you to attach metadata to your mapping definition. This metadata is stored alongside your mapping and is returned when the mapping is retrieved, serving solely as informational context without influencing indexing or search operations.

You can use the `_meta` mapping parameter to provide important details, such as version information, descriptions, or authorship. Metadata can also be updated by submitting a mapping update that overrides the existing metadata.

## Enabling meta on a mapping

The following request creates an index named `products` with a `_meta` mapping parameter containing version and description information:

```json
PUT /products
{
  "mappings": {
    "_meta": {
      "version": "1.0",
      "description": "Mapping for the products index."
    },
    "properties": {
      "name": {
        "type": "text"
      },
      "price": {
        "type": "float"
      }
    }
  }
}
```

### Updating metadata on an index

Use the following request to update the `_meta` mapping parameter on an index:

```json
PUT /products/_mapping
{
  "_meta": {
    "version": "1.1",
    "description": "Updated mapping for the products index.",
    "author": "Team B"
  }
}
```

### Indexing a document

After the index is created, you can index documents as usual. The `_meta` information remains with the mapping and does not affect the document indexing process:

```json
PUT /products/_doc/1
{
  "name": "Widget",
  "price": 19.99
}
```

### Retrieve the meta information

To verify that your `_meta` information is stored, you can retrieve the mapping for the index:

```json
GET /products/_mapping
```
