---
collection: "opensearch"
version: "2.19"
title: "Pipeline"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ingest-pipelines/processors/pipeline.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ingest-pipelines/processors/pipeline.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ingest-pipelines/processors/pipeline/"
canonical_url: "https://docs.opensearch.org/latest/ingest-pipelines/processors/pipeline/"
canonical_route: "/ingest-pipelines/processors/pipeline/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 220
parent: "Ingest processors"
---
# Pipeline processor

The `pipeline` processor allows a pipeline to reference and include another predefined pipeline. This can be useful when you have a set of common processors that need to be shared across multiple pipelines. Instead of redefining those common processors in each pipeline, you can create a separate base pipeline containing the shared processors and then reference that base pipeline from other pipelines using the pipeline processor.

The following is the syntax for the `pipeline` processor:

```json
{
  "pipeline": {
    "name": "general-pipeline"
  }
}
```

## Configuration parameters

The following table lists the required and optional parameters for the `pipeline` processor.

Parameter | Required/Optional | Description |
|-----------|-----------|-----------|
`name` | Required	| The name of the pipeline to execute.
`description` | Optional | A description of the processor's purpose or configuration.
`if` | Optional | Specifies to conditionally execute the processor.
`ignore_failure` | Optional | Specifies to ignore processor failures. See [Handling pipeline failures](../../pipeline-failures/index.md).
`on_failure` | Optional | Specifies to handle processor failures. See [Handling pipeline failures](../../pipeline-failures/index.md).
`tag` | Optional | An identifier for the processor. Useful for debugging and metrics.

## Using the processor

Follow these steps to use the processor in a pipeline.

### Step 1: Create a pipeline

The following query creates a general pipeline named `general-pipeline` and then creates a new pipeline named `outer-pipeline`, which references the `general-pipeline`:

```json
PUT _ingest/pipeline/general_pipeline
{
  "description": "a general pipeline",
  "processors": [
    {
      "uppercase": {
        "field": "protocol"
      },
      "remove": {
        "field": "name"
      }
    }
  ]
}
```

```json
PUT _ingest/pipeline/outer-pipeline
{
  "description": "an outer pipeline referencing the general pipeline",
  "processors": [
    {
      "pipeline": {
        "name": "general-pipeline"
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
POST _ingest/pipeline/outer-pipeline/_simulate
{
  "docs": [
    {
      "_source": {
        "protocol": "https",
        "name":"test"
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
          "protocol": "HTTPS"
        },
        "_ingest": {
          "timestamp": "2024-05-24T02:43:43.700735801Z"
        }
      }
    }
  ]
}
```

### Step 3: Ingest a document

The following query ingests a document into an index named `testindex1`:

```json
POST testindex1/_doc/1?pipeline=outer-pipeline
{
  "protocol": "https",
  "name": "test"
}
```

#### Response

The request indexes the document with the `protocol` field converted to uppercase and the field name removed from the index `testindex1`, as shown in the following response:

```json
{
  "_index": "testindex1",
  "_id": "1",
  "_version": 2,
  "result": "created",
  "_shards": {
    "total": 2,
    "successful": 2,
    "failed": 0
  },
  "_seq_no": 1,
  "_primary_term": 1
}
```

### Step 4 (Optional): Retrieve the document

To retrieve the document, run the following query:

```json
GET testindex1/_doc/1
```

#### Response

The response shows the document with the `protocol` field converted to uppercase and the field name removed:

```json
{
  "_index": "testindex1",
  "_id": "1",
  "_version": 2,
  "_seq_no": 1,
  "_primary_term": 1,
  "found": true,
  "_source": {
    "protocol": "HTTPS"
  }
}
```
