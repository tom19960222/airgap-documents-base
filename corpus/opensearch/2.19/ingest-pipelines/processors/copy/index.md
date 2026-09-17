---
collection: "opensearch"
version: "2.19"
title: "Copy"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ingest-pipelines/processors/copy.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ingest-pipelines/processors/copy.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ingest-pipelines/processors/copy/"
canonical_url: "https://docs.opensearch.org/latest/ingest-pipelines/processors/copy/"
canonical_route: "/ingest-pipelines/processors/copy/"
redirect_from: ["/api-reference/ingest-apis/processors/copy/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 35
parent: "Ingest processors"
---
This documentation describes using the `copy` processor in OpenSearch ingest pipelines. Consider using the [Data Prepper `copy_values` processor](https://docs.opensearch.org/latest/data-prepper/pipelines/configuration/processors/copy-values/) <!-- unresolved-jekyll-link: route=/data-prepper/pipelines/configuration/processors/copy-values/ -->, which runs on the OpenSearch cluster, if your use case involves large or complex datasets.
{: .note}

# Copy processor

The `copy` processor copies an entire object in an existing field to another field.

## Syntax

The following is the syntax for the `copy` processor:

```json
{
    "copy": {
      "source_field": "source_field",
      "target_field": "target_field",
      "ignore_missing": true,
      "override_target": true,
      "remove_source": true
    }
}
```

## Configuration parameters

The following table lists the required and optional parameters for the `copy` processor.

| Parameter  | Required/Optional  | Description  |
|---|---|---|
`source_field`  | Required  | The name of the field to be copied. Supports [template snippets](../../create-ingest/index.md#template-snippets). |
`target_field`  | Required  | The name of the field to be copied to. Supports [template snippets](../../create-ingest/index.md#template-snippets). |
`ignore_missing`  | Optional  | Specifies whether the processor should ignore documents that do not contain the specified `source_field`. If set to `true`, the processor does not modify the document if the `source_field` does not exist or is `null`. Default is `false`. |
`override_target`  | Optional  | Specifies whether the processor should override the `target_field` if it already exists in the document. If set to `true`, the processor overrides the value of `target_field` if it already exists. Default is `false`. |
`remove_source`  | Optional  | Specifies whether the processor should remove the `source_field` after it has been copied. If set to `true`, the processor removes the `source_field` from the document. Default is `false`. |
`description`  | Optional  | A brief description of the processor.  |
`if` | Optional | A condition for running the processor. |
`ignore_failure` | Optional | Specifies whether the processor continues execution even if it encounters an error. If set to `true`, the failure is ignored. Default is `false`. |
`on_failure` | Optional | A list of processors to run if the processor fails. |
`tag` | Optional | An identifier tag for the processor. Useful for debugging in order to distinguish between processors of the same type. |

## Using the processor

Follow these steps to use the processor in a pipeline.

**Step 1: Create a pipeline**

The following query creates a pipeline named `copy_object` that copies a nested object from one field to the root level:

```json
PUT /_ingest/pipeline/copy_object
{
  "description": "Pipeline that copies object.",
  "processors": [
    {
      "copy": {
        "source_field": "message.content",
        "target_field":"content",
        "ignore_missing": true,
        "override_target": true,
        "remove_source": true
      }
    }
  ]
}
```

**Step 2 (Optional): Test the pipeline**

It is recommended that you test your pipeline before you ingest documents.
{: .tip}

To test the pipeline, run the following query:

```json
POST _ingest/pipeline/copy_object/_simulate
{
  "docs": [
    {
      "_index": "testindex1",
      "_id": "1",
      "_source":{
         "message": {
          "content": {
            "foo": "bar",
            "zoo": [1, 2, 3]
          }
         }
      }
    }
  ]
}
```

**Response**

The following example response confirms that the pipeline is working as expected:

```json
{
  "docs": [
    {
      "doc": {
        "_index": "testindex1",
        "_id": "1",
        "_source": {
          "content": {
            "foo": "bar",
            "zoo": [1, 2, 3]
          }
        },
        "_ingest": {
          "timestamp": "2023-08-24T18:02:13.218986756Z"
        }
      }
    }
  ]
}
```

**Step 3: Ingest a document**

The following query ingests a document into an index named `testindex1`:

```json
PUT testindex1/_doc/1?pipeline=copy_object
{
  "content": {
    "foo": "bar",
    "zoo": [1, 2, 3]
  }
}
```

**Step 4 (Optional): Retrieve the document**

To retrieve the document, run the following query:

```json
GET testindex1/_doc/1
```
