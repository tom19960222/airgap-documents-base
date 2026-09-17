---
collection: "opensearch"
version: "2.19"
title: "HTML strip"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ingest-pipelines/processors/html-strip.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ingest-pipelines/processors/html-strip.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ingest-pipelines/processors/html-strip/"
canonical_url: "https://docs.opensearch.org/latest/ingest-pipelines/processors/html-strip/"
canonical_route: "/ingest-pipelines/processors/html-strip/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 140
parent: "Ingest processors"
---
# HTML strip processor

The `html_strip` processor removes HTML tags from string fields in incoming documents. This processor is useful when indexing data from webpages or other sources that may contain HTML markup. HTML tags are replaced with newline characters (`\n`).

The following is the syntax for the `html_strip` processor:

```json
{
  "html_strip": {
    "field": "webpage"
  }
}
```

## Configuration parameters

The following table lists the required and optional parameters for the `html_strip` processor.

Parameter | Required/Optional | Description |
|-----------|-----------|-----------|
`field` | Required | The string field from which to remove HTML tags.
`target_field` | Optional | The field that receives the plain text version after stripping HTML tags. If not specified, then the field is updated in-place.
`ignore_missing` | Optional | Specifies whether the processor should ignore documents that do not contain the specified field. Default is `false`.
`description` | Optional | A description of the processor's purpose or configuration.
`if` | Optional | Specifies to conditionally execute the processor.
`ignore_failure` | Optional | Specifies to ignore processor failures. See [Handling pipeline failures](../../pipeline-failures/index.md).
`on_failure` | Optional | Specifies a list of processors to run if the processor fails during execution. These processors are executed in the order they are specified. See [Handling pipeline failures](../../pipeline-failures/index.md).
`tag` | Optional | An identifier tag for the processor. Useful for debugging in order to distinguish between processors of the same type.

## Using the processor

Follow these steps to use the processor in a pipeline.

### Step 1: Create a pipeline

The following query creates a pipeline named `strip-html-pipeline` that uses the `html_strip` processor to remove HTML tags from the description field and store the processed value in a new field named `cleaned_description`:

```json
PUT _ingest/pipeline/strip-html-pipeline
{
  "description": "A pipeline to strip HTML from description field",
  "processors": [
    {
      "html_strip": {
        "field": "description",
        "target_field": "cleaned_description"
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
POST _ingest/pipeline/strip-html-pipeline/_simulate
{
  "docs": [
    {
      "_source": {
        "description": "This is a <b>test</b> description with <i>some</i> HTML tags."
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
          "description": "This is a <b>test</b> description with <i>some</i> HTML tags.",
          "cleaned_description": "This is a test description with some HTML tags."
        },
        "_ingest": {
          "timestamp": "2024-05-22T21:46:11.227974965Z"
        }
      }
    }
  ]
}
```

### Step 3: Ingest a document

The following query ingests a document into an index named `products`:

```json
PUT products/_doc/1?pipeline=strip-html-pipeline
{
  "name": "Product 1",
  "description": "This is a <b>test</b> product with <i>some</i> HTML tags."
}
```

#### Response

The response shows that the request has indexed the document into the index `products` and will index all documents with the `description` field containing HTML tags while storing the plain text version in the `cleaned_description` field:

```json
{
  "_index": "products",
  "_id": "1",
  "_version": 1,
  "result": "created",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 0,
  "_primary_term": 1
}
```

### Step 4 (Optional): Retrieve the document

To retrieve the document, run the following query:

```json
GET products/_doc/1
```

#### Response

The response includes both the original `description` field and the `cleaned_description` field with HTML tags removed:

```json
{
  "_index": "products",
  "_id": "1",
  "_version": 1,
  "_seq_no": 0,
  "_primary_term": 1,
  "found": true,
  "_source": {
    "cleaned_description": "This is a test product with some HTML tags.",
    "name": "Product 1",
    "description": "This is a <b>test</b> product with <i>some</i> HTML tags."
  }
}
```
