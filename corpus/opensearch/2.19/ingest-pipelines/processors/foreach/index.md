---
collection: "opensearch"
version: "2.19"
title: "Foreach"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ingest-pipelines/processors/foreach.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ingest-pipelines/processors/foreach.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ingest-pipelines/processors/foreach/"
canonical_url: "https://docs.opensearch.org/latest/ingest-pipelines/processors/foreach/"
canonical_route: "/ingest-pipelines/processors/foreach/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 110
parent: "Ingest processors"
---
<!-- vale off -->
# Foreach processor
<!-- vale on -->

The `foreach` processor is used to iterate over a list of values in an input document and apply a transformation to each value. This can be useful for tasks like processing all the elements in an array consistently, such as converting all elements in a string to lowercase or uppercase.

The following is the syntax for the `foreach` processor:

```json
{
  "foreach": {
    "field": "<field_name>",
    "processor": {
      "<processor_type>": {
        "<processor_config>": "<processor_value>"
      }
    }
  }
}
```

## Configuration parameters

The following table lists the required and optional parameters for the `foreach` processor.

Parameter | Required/Optional | Description |
|-----------|-----------|-----------|
`field` | Required | The array field to iterate over.
`processor` | Required | The processor to execute against each field.
`ignore_missing` | Optional | If `true` and the specified field does not exist or is null, then the processor will quietly exit without modifying the document.
`description` | Optional | A brief description of the processor.
`if` | Optional | A condition for running the processor.
`ignore_failure` | Optional | Specifies whether the processor continues execution even if it encounters an error. If set to `true`, then failures are ignored. Default is `false`.
`on_failure` | Optional | A list of processors to run if the processor fails.
`tag` | Optional | An identifier tag for the processor. Useful for debugging in order to distinguish between processors of the same type.

## Using the processor

Follow these steps to use the processor in a pipeline.

### Step 1: Create a pipeline

The following query creates a pipeline named `test-foreach` that uses the `foreach` processor to iterate over each element in the `protocols` field:

```json
PUT _ingest/pipeline/test-foreach
{
  "description": "Lowercase all the elements in an array",
  "processors": [
    {
      "foreach": {
        "field": "protocols",
        "processor": {
          "lowercase": {
            "field": "_ingest._value"
          }
        }
      }
```

### Step 2 (Optional): Test the pipeline

It is recommended that you test your pipeline before you ingest documents.
{: .tip}

To test the pipeline, run the following query:

```json
POST _ingest/pipeline/test-foreach/_simulate
{
  "docs": [
    {
      "_index": "testindex1",
      "_id": "1",
      "_source": {
        "protocols": ["HTTP","HTTPS","TCP","UDP"]
      }
    }
  ]
}
```

#### Response

The following example response confirms that the pipeline is working as expected, showing that the four elements have been lowercased:

```json
{
  "docs": [
    {
      "doc": {
        "_index": "testindex1",
        "_id": "1",
        "_source": {
          "protocols": [
            "http",
            "https",
            "tcp",
            "udp"
          ]
        },
        "_ingest": {
          "_value": null,
          "timestamp": "2024-05-23T02:44:10.8201Z"
        }
      }
    }
  ]
}

```

### Step 3: Ingest a document

The following query ingests a document into an index named `testindex1`:

```json
POST testindex1/_doc/1?pipeline=test-foreach
{
  "protocols": ["HTTP","HTTPS","TCP","UDP"]
}
```

#### Response

The request indexes the document into the index `testindex1` and applies the pipeline before indexing:

```json
{
  "_index": "testindex1",
  "_id": "1",
  "_version": 6,
  "result": "created",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 5,
  "_primary_term": 67
}
```

### Step 4 (Optional): Retrieve the document

To retrieve the document, run the following query:

```json
GET testindex1/_doc/1
```

#### Response

The response shows the document with the extracted JSON data from the `users` field:

```json
{
  "_index": "testindex1",
  "_id": "1",
  "_version": 6,
  "_seq_no": 5,
  "_primary_term": 67,
  "found": true,
  "_source": {
    "protocols": [
      "http",
      "https",
      "tcp",
      "udp"
    ]
  }
}

{
  "docs": [
    {
      "doc": {
        "_index": "testindex1",
        "_id": "1",
        "_source": {
          "protocols": [
            "http",
            "https",
            "tcp",
            "udp"
          ]
        },
        "_ingest": {
          "_value": null,
          "timestamp": "2024-05-23T02:44:10.8201Z"
        }
      }
    }
  ]
}
```
