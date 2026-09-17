---
collection: "opensearch"
version: "2.19"
title: "Exists"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_query-dsl/term/exists.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_query-dsl/term/exists.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/query-dsl/term/exists/"
canonical_url: "https://docs.opensearch.org/latest/query-dsl/term/exists/"
canonical_route: "/query-dsl/term/exists/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 10
parent: "Term-level queries"
---
# Exists query

Use the `exists` query to search for documents that contain a specific field.

An indexed value will not exist for a document field in any of the following cases:

- The field has `"index" : false` specified in the mapping.
- The field in the source JSON is `null` or `[]`.
- The length of the field value exceeds the `ignore_above` setting in the mapping.
- The field value is malformed and `ignore_malformed` is defined in the mapping.

An indexed value will exist for a document field in any of the following cases:

- The value is an array that contains one or more null elements and one or more non-null elements (for example, `["one", null]`).
- The value is an empty string (`""` or `"-"`).
- The value is a custom `null_value`, as defined in the field mapping.

## Example

For example, consider an index that contains the following two documents:

```json
PUT testindex/_doc/1
{
  "title": "The wind rises"
}
```

```json
PUT testindex/_doc/2
{
  "title": "Gone with the wind",
  "description": "A 1939 American epic historical film"
}
```

The following query searches for documents that contain the `description` field:

```json
GET testindex/_search
{
  "query": {
    "exists": {
      "field": "description"
    }
  }
}
```

The response contains the matching document:

```json
{
  "took": 3,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 1,
    "hits": [
      {
        "_index": "testindex",
        "_id": "2",
        "_score": 1,
        "_source": {
          "title": "Gone with the wind",
          "description": "A 1939 American epic historical film"
        }
      }
    ]
  }
}
```

## Finding documents with missing indexed values

To find documents with missing indexed values, you can use the `must_not` [Boolean query](../../compound/bool/index.md) with the inner `exists` query. For example, the following request searches for documents in which the `description` field is missing:

```json
GET testindex/_search
{
  "query": {
    "bool": {
      "must_not": {
        "exists": {
          "field": "description"
        }
      }
    }
  }
}
```

The response contains the matching document:

```json
{
  "took": 19,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 0,
    "hits": [
      {
        "_index": "testindex",
        "_id": "1",
        "_score": 0,
        "_source": {
          "title": "The wind rises"
        }
      }
    ]
  }
}
```

## Parameters

The query accepts the name of the field (`<field>`) as a top-level parameter.

Parameter | Data type | Description
:--- | :--- | :---
`boost` | Floating-point | A floating-point value that specifies the weight of this field toward the relevance score. Values above 1.0 increase the field’s relevance. Values between 0.0 and 1.0 decrease the field’s relevance. Default is 1.0.
