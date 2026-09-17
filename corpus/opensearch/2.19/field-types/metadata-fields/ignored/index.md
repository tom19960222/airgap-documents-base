---
collection: "opensearch"
version: "2.19"
title: "Ignored"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/metadata-fields/ignored.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/metadata-fields/ignored.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/metadata-fields/ignored/"
canonical_url: "https://docs.opensearch.org/latest/mappings/metadata-fields/ignored/"
canonical_route: "/mappings/metadata-fields/ignored/"
redirect_from: ["/mappings/metadata-fields/ignored/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 25
parent: "Metadata fields"
---
# Ignored

The `_ignored` field helps you manage issues related to malformed data in your documents. This field is used to index and store field names that were ignored during the indexing process as a result of the `ignore_malformed` setting being enabled in the [index mapping](../../index.md).

The `_ignored` field allows you to search for and identify documents containing fields that were ignored as well as for the specific field names that were ignored. This can be useful for troubleshooting.

You can query the `_ignored` field using the `term`, `terms`, and `exists` queries, and the results will be included in the search hits.

The `_ignored` field is only populated when the `ignore_malformed` setting is enabled in your index mapping. If `ignore_malformed` is set to `false` (the default value), then malformed fields will cause the entire document to be rejected, and the `_ignored` field will not be populated.
{: .note}

The following example request shows you how to use the `_ignored` field:

```json
GET _search
{
  "query": {
    "exists": {
      "field": "_ignored"
    }
  }
}
```

---

#### Example indexing request with the `_ignored` field

The following example request adds a new document to the `test-ignored` index with `ignore_malformed` set to `true` so that no error is thrown during indexing:

```json
PUT test-ignored
{
  "mappings": {
    "properties": {
      "title": {
        "type": "text"
      },
      "length": {
        "type": "long",
        "ignore_malformed": true
      }
    }
  }
}

POST test-ignored/_doc
{
  "title": "correct text",
  "length": "not a number"
}

GET test-ignored/_search
{
  "query": {
    "exists": {
      "field": "_ignored"
    }
  }
}
```

#### Example reponse

```json
{
  "took": 42,
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
        "_index": "test-ignored",
        "_id": "qcf0wZABpEYH7Rw9OT7F",
        "_score": 1,
        "_ignored": [
          "length"
        ],
        "_source": {
          "title": "correct text",
          "length": "not a number"
        }
      }
    ]
  }
}
```

---

## Ignoring a specified field

You can use a `term` query to find documents in which a specific field was ignored, as shown in the following example request:

```json
GET _search
{
  "query": {
    "term": {
      "_ignored": "created_at"
    }
  }
}
```

#### Reponse

```json
{
  "took": 51,
  "timed_out": false,
  "_shards": {
    "total": 45,
    "successful": 45,
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
