---
collection: "opensearch"
version: "2.19"
title: "Uppercase"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ingest-pipelines/processors/uppercase.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ingest-pipelines/processors/uppercase.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ingest-pipelines/processors/uppercase/"
canonical_url: "https://docs.opensearch.org/latest/ingest-pipelines/processors/uppercase/"
canonical_route: "/ingest-pipelines/processors/uppercase/"
redirect_from: ["/api-reference/ingest-apis/processors/uppercase/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 310
parent: "Ingest processors"
---
This documentation describes using the `uppercase` processor in OpenSearch ingest pipelines. Consider using the [Data Prepper `uppercase_string` processor](https://docs.opensearch.org/latest/data-prepper/pipelines/configuration/processors/uppercase-string/) <!-- unresolved-jekyll-link: route=/data-prepper/pipelines/configuration/processors/uppercase-string/ -->, which runs on the OpenSearch cluster, if your use case involves large or complex datasets.
{: .note}

# Uppercase processor

The `uppercase` processor converts all the text in a specific field to uppercase letters.

## Syntax

The following is the syntax for the `uppercase` processor:

```json
{
  "uppercase": {
    "field": "field_name"
  }
}
```

## Configuration parameters

The following table lists the required and optional parameters for the `uppercase` processor.

| Parameter  | Required/Optional  | Description  |
|---|---|---|
`field`  | Required  | The name of the field containing the data to be appended. Supports [template snippets](../../create-ingest/index.md#template-snippets). |
`description`  | Optional  | A brief description of the processor.  |
`if` | Optional | A condition for running the processor. |
`ignore_failure` | Optional |  Specifies whether the processor continues execution even if it encounters errors. If set to `true`, failures are ignored. Default is `false`. |
`ignore_missing`  | Optional  | Specifies whether the processor should ignore documents that do not contain the specified field. If set to `true`, the processor does not modify the document if the field does not exist or is `null`. Default is `false`.  |
`on_failure` | Optional | A list of processors to run if the processor fails. |
`tag` | Optional | An identifier tag for the processor. Useful for debugging in order to distinguish between processors of the same type. |
`target_field`  | Optional  | The name of the field in which to store the parsed data. Default is `field`. By default, `field` is updated in place. |

## Using the processor

Follow these steps to use the processor in a pipeline.

**Step 1: Create a pipeline**

The following query creates a pipeline, named `uppercase`, that converts the text in the `field` field to uppercase:

```json
PUT _ingest/pipeline/uppercase
{
  "processors": [
    {
      "uppercase": {
        "field": "name"
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
POST _ingest/pipeline/uppercase/_simulate
{
  "docs": [
    {
      "_index": "testindex1",
      "_id": "1",
      "_source": {
        "name": "John"
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
          "name": "JOHN"
        },
        "_ingest": {
          "timestamp": "2023-08-28T19:54:42.289624792Z"
        }
      }
    }
  ]
}
```

**Step 3: Ingest a document**

The following query ingests a document into an index named `testindex1`:

```json
PUT testindex1/_doc/1?pipeline=uppercase
{
  "name": "John"
}
```

**Step 4 (Optional): Retrieve the document**

To retrieve the document, run the following query:

```json
GET testindex1/_doc/1
```
