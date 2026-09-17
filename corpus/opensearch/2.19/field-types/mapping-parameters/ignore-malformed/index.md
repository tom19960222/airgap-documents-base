---
collection: "opensearch"
version: "2.19"
title: "Ignore malformed"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/mapping-parameters/ignore-malformed.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/mapping-parameters/ignore-malformed.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/mapping-parameters/ignore-malformed/"
canonical_url: "https://docs.opensearch.org/latest/mappings/mapping-parameters/ignore-malformed/"
canonical_route: "/mappings/mapping-parameters/ignore-malformed/"
redirect_from: ["/mappings/mapping-parameters/ignore-malformed/"]
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
# Ignore malformed

The `ignore_malformed` mapping parameter instructs the indexing engine to ignore values that do not match the field's expected format. When enabled, malformed values are not indexed, preventing entire-document rejection because of data format issues. This ensures that documents are still stored even if one or more fields contain data that cannot be parsed.

By default, `ignore_malformed` is disabled, which means that if a value cannot be parsed according to the field type, indexing will fail for the entire document.

## Example: ignore_malformed off

Create an index named `people_no_ignore` containing an `age` field of type `integer`. By default, `ignore_malformed` is set to `false`:

```json
PUT /people_no_ignore
{
  "mappings": {
    "properties": {
      "age": {
        "type": "integer"
      }
    }
  }
}
```

Index a document with a malformed value:

```json
PUT /people_no_ignore/_doc/1
{
  "age": "twenty"
}
```

The request fails because of the malformed value:

```json
{
  "error": {
    "root_cause": [
      {
        "type": "mapper_parsing_exception",
        "reason": "failed to parse field [age] of type [integer] in document with id '1'. Preview of field's value: 'twenty'"
      }
    ],
    "type": "mapper_parsing_exception",
    "reason": "failed to parse field [age] of type [integer] in document with id '1'. Preview of field's value: 'twenty'",
    "caused_by": {
      "type": "number_format_exception",
      "reason": "For input string: \"twenty\""
    }
  },
  "status": 400
}
```

## Example: ignore_malformed on

Create an index named `people_ignore` in which the `age` field has `ignore_malformed` set to `true`:

```json
PUT /people_ignore
{
  "mappings": {
    "properties": {
      "age": {
        "type": "integer",
        "ignore_malformed": true
      }
    }
  }
}
```

Index a document with a malformed value:

```json
PUT /people_ignore/_doc/1
{
  "age": "twenty"
}
```

Retrieve the document:

```json
GET /people_ignore/_doc/1
```

The response shows that the document was indexed successfully, despite having a malformed value:

```json
{
  "_index": "people_ignore",
  "_id": "1",
  "_version": 1,
  "_seq_no": 0,
  "_primary_term": 1,
  "found": true,
  "_source": {
    "age": "twenty"
  }
}
```
