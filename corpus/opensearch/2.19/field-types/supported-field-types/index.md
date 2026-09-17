---
collection: "opensearch"
version: "2.19"
title: "Supported field types"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/supported-field-types/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/supported-field-types/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/supported-field-types/"
canonical_url: "https://docs.opensearch.org/latest/mappings/supported-field-types/index/"
canonical_route: "/mappings/supported-field-types/"
redirect_from: ["/opensearch/supported-field-types/","/mappings/supported-field-types/index/","/field-types/supported-field-types/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 80
---
# Supported field types

You can specify data types for your fields when creating a mapping. The following table lists all data field types that OpenSearch supports.

Category | Field types and descriptions
:--- | :---
Alias | [`alias`](alias/index.md): An additional name for an existing field.
Binary | [`binary`](binary/index.md):  A binary value in Base64 encoding.
[Numeric](numeric/index.md) | A numeric value (`byte`, `double`, `float`, `half_float`, `integer`, `long`, [`unsigned_long`](unsigned-long/index.md), `scaled_float`, `short`).
Boolean | [`boolean`](boolean/index.md): A Boolean value.
[Date](dates/index.md)|  [`date`](date/index.md): A date stored in milliseconds. <br> [`date_nanos`](date-nanos/index.md): A date stored in nanoseconds.
IP | [`ip`](ip/index.md): An IP address in IPv4 or IPv6 format.
[Range](range/index.md) | A range of values (`integer_range`, `long_range`, `double_range`, `float_range`, `date_range`, `ip_range`).
[Object](object-fields/index.md)| [`object`](object/index.md): A JSON object. <br>[`nested`](nested/index.md): Used when objects in an array need to be indexed independently as separate documents.<br>[`flat_object`](flat-object/index.md): A JSON object treated as a string.<br>[`join`](join/index.md): Establishes a parent/child relationship between documents in the same index.
[String](string/index.md)|[`keyword`](keyword/index.md): Contains a string that is not analyzed.<br> [`text`](text/index.md): Contains a string that is analyzed.<br> [`match_only_text`](match-only-text/index.md): A space-optimized version of a `text` field.<br>[`token_count`](token-count/index.md): Stores the number of analyzed tokens in a string. <br>[`wildcard`](wildcard/index.md): A variation of `keyword` with efficient substring and regular expression matching.
[Autocomplete](autocomplete/index.md) |[`completion`](completion/index.md): Provides autocomplete functionality through a completion suggester.<br> [`search_as_you_type`](search-as-you-type/index.md): Provides search-as-you-type functionality using both prefix and infix completion.
[Geographic](geographic/index.md)| [`geo_point`](geo-point/index.md): A geographic point.<br>[`geo_shape`](geo-shape/index.md): A geographic shape.
[Rank](rank/index.md) | Boosts or decreases the relevance score of documents (`rank_feature`, `rank_features`).
k-NN vector | [`knn_vector`](knn-vector/index.md): Allows indexing a k-NN vector into OpenSearch and performing different kinds of k-NN search.
Percolator | [`percolator`](percolator/index.md): Specifies to treat this field as a query.
Derived | [`derived`](derived/index.md): Creates new fields dynamically by executing scripts on existing fields.
Star-tree | [`star_tree`](star-tree/index.md): Precomputes aggregations and stores them in a [star-tree index](https://docs.pinot.apache.org/basics/indexing/star-tree-index), accelerating the performance of aggregation queries.

## Arrays

There is no dedicated array field type in OpenSearch. Instead, you can pass an array of values into any field. All values in the array must have the same field type.

```json
PUT testindex1/_doc/1
{
  "number": 1
}

PUT testindex1/_doc/2
{
  "number": [1, 2, 3]
}
```

## Multifields

Multifields are used to index the same field differently. Strings are often mapped as `text` for full-text queries and `keyword` for exact-value queries.

Multifields can be created using the `fields` parameter. For example, you can map a book `title` to be of type `text` and keep a `title.raw` subfield of type `keyword`.

```json
PUT books
{
  "mappings" : {
    "properties" : {
      "title" : {
        "type" : "text",
        "fields" : {
          "raw" : {
            "type" : "keyword"
          }
        }
      }
    }
  }
}
```

## Null value

Setting a field's value to `null`, an empty array, or an array of `null` values makes this field equivalent to an empty field. Therefore, you cannot search for documents that have `null` in this field.

To make a field searchable for `null` values, you can specify its `null_value` parameter in the index's mappings. Then, all `null` values passed to this field will be replaced with the specified `null_value`.

The `null_value` parameter must be of the same type as the field. For example, if your field is a string, the `null_value` for this field must also be a string.
{: .note}

### Example

Create a mapping to replace `null` values in the `emergency_phone` field with the string "NONE":

```json
PUT testindex
{
  "mappings": {
    "properties": {
      "name": {
        "type": "keyword"
      },
      "emergency_phone": {
        "type": "keyword",
        "null_value": "NONE"
      }
    }
  }
}
```

Index three documents into testindex. The `emergency_phone` fields of documents 1 and 3 contain `null`, while the `emergency_phone` field of document 2 has an empty array:

```json
PUT testindex/_doc/1
{
  "name": "Akua Mansa",
  "emergency_phone": null
}
```

```json
PUT testindex/_doc/2
{
  "name": "Diego Ramirez",
  "emergency_phone" : []
}
```

```json
PUT testindex/_doc/3
{
  "name": "Jane Doe",
  "emergency_phone": [null, null]
}
```

Search for people who do not have an emergency phone:

```json
GET testindex/_search
{
  "query": {
    "term": {
      "emergency_phone": "NONE"
    }
  }
}
```

The response contains documents 1 and 3 but not document 2 because only explicit `null` values are replaced with the string "NONE":

```json
{
  "took" : 1,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score" : 0.18232156,
    "hits" : [
      {
        "_index" : "testindex",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 0.18232156,
        "_source" : {
          "name" : "Akua Mansa",
          "emergency_phone" : null
        }
      },
      {
        "_index" : "testindex",
        "_type" : "_doc",
        "_id" : "3",
        "_score" : 0.18232156,
        "_source" : {
          "name" : "Jane Doe",
          "emergency_phone" : [
            null,
            null
          ]
        }
      }
    ]
  }
}
```

The `_source` field still contains explicit `null` values because it is not affected by the `null_value`.
{: .note}
