---
collection: "opensearch"
version: "2.19"
title: "Coerce"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/mapping-parameters/coerce.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/mapping-parameters/coerce.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/mapping-parameters/coerce/"
canonical_url: "https://docs.opensearch.org/latest/mappings/mapping-parameters/coerce/"
canonical_route: "/mappings/mapping-parameters/coerce/"
redirect_from: ["/mappings/mapping-parameters/coerce/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Mapping and field types"
has_children: false
has_toc: false
layout: "default"
nav_order: 15
parent: "Mapping parameters"
---
# Coerce

The `coerce` mapping parameter controls how values are converted to the expected field data type during indexing. This parameter lets you verify that your data is formatted and indexed properly, following the expected field types. This improves the accuracy of your search results.

---

## Examples

The following examples demonstrate how to use the `coerce` mapping parameter.

#### Indexing a document with `coerce` enabled

```json
PUT products
{
  "mappings": {
    "properties": {
      "price": {
        "type": "integer",
        "coerce": true
      }
    }
  }
}

PUT products/_doc/1
{
  "name": "Product A",
  "price": "19.99"
}
```

In this example, the `price` field is defined as an `integer` type with `coerce` set to `true`. When indexing the document, the string value `19.99` is coerced to the integer `19`.

#### Indexing a document with `coerce` disabled

```json
PUT orders
{
  "mappings": {
    "properties": {
      "quantity": {
        "type": "integer",
        "coerce": false
      }
    }
  }
}

PUT orders/_doc/1
{
  "item": "Widget",
  "quantity": "10"
}
```

In this example, the `quantity` field is defined as an `integer` type with `coerce` set to `false`. When indexing the document, the string value `10` is not coerced, and the document is rejected because of the type mismatch.

#### Setting the index-level coercion setting

```json
PUT inventory
{
  "settings": {
    "index.mapping.coerce": false
  },
  "mappings": {
    "properties": {
      "stock_count": {
        "type": "integer",
        "coerce": true
      },
      "sku": {
        "type": "keyword"
      }
    }
  }
}

PUT inventory/_doc/1
{
  "sku": "ABC123",
  "stock_count": "50"
}
```

In this example, the index-level `index.mapping.coerce` setting is set to `false`, which disables coercion for the index. However, the `stock_count` field overrides this setting and enables coercion for this specific field.
