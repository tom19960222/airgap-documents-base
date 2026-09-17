---
collection: "opensearch"
version: "2.19"
title: "Trim"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ingest-pipelines/processors/trim.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ingest-pipelines/processors/trim.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ingest-pipelines/processors/trim/"
canonical_url: "https://docs.opensearch.org/latest/ingest-pipelines/processors/trim/"
canonical_route: "/ingest-pipelines/processors/trim/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 300
parent: "Ingest processors"
---
# Trim processor

The `trim` processor is used to remove leading and trailing white space characters from a specified field.

The following is the syntax for the `trim` processor:

```json
{
  "trim": {
    "field": "field_to_trim",
    "target_field": "trimmed_field"
  }
}
```

## Configuration parameters

The following table lists the required and optional parameters for the `trim` processor.

Parameter | Required/Optional | Description
:---|:---|:---
`field` | Required | The field containing the text to be trimmed.
`target_field` | Required | The field in which the trimmed text is stored. If not specified, then the field is updated in-place.
`ignore_missing` | Optional | Specifies whether the processor should ignore documents that do not contain the specified field. If set to `true`, then the processor ignores missing values in the field and leaves the `target_field` unchanged. Default is `false`.
`description` | Optional | A brief description of the processor.
`if` | Optional | A condition for running the processor.
`ignore_failure` | Optional | Specifies whether the processor continues execution even if it encounters an error. If set to `true`, then failures are ignored. Default is `false`.
`on_failure` | Optional | A list of processors to run if the processor fails.
`tag` | Optional | An identifier tag for the processor. Useful for debugging in order to distinguish between processors of the same type.

## Using the processor

Follow these steps to use the processor in a pipeline.

### Step 1: Create a pipeline

The following query creates a pipeline named `trim_pipeline` that uses the `trim` processor to remove leading and trailing white space from the `raw_text` field and store the trimmed text in the `trimmed_text` field:

```json
PUT _ingest/pipeline/trim_pipeline
{
  "description": "Trim leading and trailing white space",
  "processors": [
    {
      "trim": {
        "field": "raw_text",
        "target_field": "trimmed_text"
      }
    }
  ]
}
```

### Step 2 (Optional): Test the pipeline

It is recommended that you test your pipeline before you ingest documents.
{: .tip}

To test the pipeline, run the following query:

```json
POST _ingest/pipeline/trim_pipeline/_simulate
{
  "docs": [
    {
      "_source": {
        "raw_text": "   Hello, world!   "
      }
    }
  ]
}
```

#### Response

The following example response confirms that the pipeline is working as expected:

```json
{
  "docs": [
    {
      "doc": {
        "_index": "_index",
        "_id": "_id",
        "_source": {
          "raw_text": "   Hello, world!   ",
          "trimmed_text": "Hello, world!"
        },
        "_ingest": {
          "timestamp": "2024-04-26T20:58:17.418006805Z"
        }
      }
    }
  ]
}
```

### Step 3: Ingest a document

The following query ingests a document into an index named `testindex1`:

```json
PUT testindex1/_doc/1?pipeline=trim_pipeline
{
  "message": "   This is a test document.   "
}
```

#### Response

The request indexes the document into the index `testindex1` and indexes all documents with the `raw_text` field, which is processed by the `trim_pipeline`, to populate the `trimmed_text` field, as shown in the following response:

```json
  "_index": "testindex1",
  "_id": "1",
  "_version": 68,
  "result": "updated",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 70,
  "_primary_term": 47
}
```

### Step 4 (Optional): Retrieve the document

To retrieve the document, run the following query:

```json
GET testindex1/_doc/1
```

The response includes the `trimmed_text` field with the leading and trailing white space removed:

```json
{
  "_index": "testindex1",
  "_id": "1",
  "_version": 69,
  "_seq_no": 71,
  "_primary_term": 47,
  "found": true,
  "_source": {
    "raw_text": "   This is a test document.   ",
    "trimmed_text": "This is a test document."
  }
}
```
