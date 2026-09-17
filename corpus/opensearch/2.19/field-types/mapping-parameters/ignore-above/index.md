---
collection: "opensearch"
version: "2.19"
title: "Ignore above"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/mapping-parameters/ignore-above.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/mapping-parameters/ignore-above.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/mapping-parameters/ignore-above/"
canonical_url: "https://docs.opensearch.org/latest/mappings/mapping-parameters/ignore-above/"
canonical_route: "/mappings/mapping-parameters/ignore-above/"
redirect_from: ["/mappings/mapping-parameters/ignore-above/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Mapping and field types"
has_children: false
has_toc: false
layout: "default"
nav_order: 45
parent: "Mapping parameters"
---
# Ignore above

The `ignore_above` mapping parameter limits the maximum number of characters for an indexed string. If a string's length exceeds the specified threshold, the value is stored with the document but is not indexed. This can help prevent the index from bloating with unusually long values and can ensure efficient queries.

By default, if you do not specify `ignore_above`, all string values will be fully indexed.

## Example: Without ignore_above

Create an index with a `keyword` field without specifying the `ignore_above` parameter:

```json
PUT /test-no-ignore
{
  "mappings": {
    "properties": {
      "sentence": {
        "type": "keyword"
      }
    }
  }
}
```

Index a document with a long string value:

```json
PUT /test-no-ignore/_doc/1
{
  "sentence": "text longer than 10 characters"
}
```

Run a term query for the full string:

```json
POST /test-no-ignore/_search
{
  "query": {
    "term": {
      "sentence": "text longer than 10 characters"
    }
  }
}
```

The document is returned because the `sentence` field was indexed:

```json
{
  ...
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 0.13353139,
    "hits": [
      {
        "_index": "test-no-ignore",
        "_id": "1",
        "_score": 0.13353139,
        "_source": {
          "sentence": "text longer than 10 characters"
        }
      }
    ]
  }
}
```

## Example: With ignore_above

Create an index with the `ignore_above` parameter set to `10` on the same field:

```json
PUT /test-ignore
{
  "mappings": {
    "properties": {
      "sentence": {
        "type": "keyword",
        "ignore_above": 10
      }
    }
  }
}
```

Index the same document with the long string value:

```json
PUT /test-ignore/_doc/1
{
  "sentence": "text longer than 10 characters"
}
```

Run a term query for the full string:

```json
POST /test-ignore/_search
{
  "query": {
    "term": {
      "sentence": "text longer than 10 characters"
    }
  }
}
```

No results are returned because the string in the `sentence` field exceeded the `ignore_above` threshold and was not indexed:

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
      "value": 0,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  }
}
```

However, the document is still present, which can be confirmed using the following request:

```json
GET test-ignore/_search
```

The returned hits include the document:

```json
{
  ...
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 1,
    "hits": [
      {
        "_index": "test-ignore",
        "_id": "1",
        "_score": 1,
        "_source": {
          "sentence": "text longer than 10 characters"
        }
      }
    ]
  }
}
```
