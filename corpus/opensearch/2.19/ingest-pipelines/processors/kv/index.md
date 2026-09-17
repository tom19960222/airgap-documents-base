---
collection: "opensearch"
version: "2.19"
title: "KV"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ingest-pipelines/processors/kv.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ingest-pipelines/processors/kv.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ingest-pipelines/processors/kv/"
canonical_url: "https://docs.opensearch.org/latest/ingest-pipelines/processors/kv/"
canonical_route: "/ingest-pipelines/processors/kv/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 200
parent: "Ingest processors"
---
This documentation describes using the `kv` processor in OpenSearch ingest pipelines. Consider using the [Data Prepper `key_value` processor](https://docs.opensearch.org/latest/data-prepper/pipelines/configuration/processors/key-value/) <!-- unresolved-jekyll-link: route=/data-prepper/pipelines/configuration/processors/key-value/ -->, which runs on the OpenSearch cluster, if your use case involves large or complex datasets.
{: .note}

# KV processor

The `kv` processor automatically extracts specific event fields or messages that are in a `key=value` format. This structured format organizes your data by grouping it together based on keys and values. It's helpful for analyzing, visualizing, and using data, such as user behavior analytics, performance optimizations, or security investigations.

## Example

The following is the syntax for the `kv` processor:

```json
{
  "kv": {
    "field": "message",
    "field_split": " ",
    "value_split": " "
  }
}
```

## Configuration parameters

The following table lists the required and optional parameters for the `kv` processor.

| Parameter  | Required/Optional  | Description  |
`field`  | Required  | The name of the field containing the data to be parsed. |
`field_split` | Required | The regex pattern for key-value pair splitting. |
`value_split` | Required | The regex pattern for splitting the key from the value within a key-value pair, for example, equal sign `=` or colon `:`.
`exclude_keys` | Optional | The keys to exclude from the document. Default is `null`. |
`include_keys` | Optional | The keys for filtering and inserting. Default is to include all keys. |
`prefix` | Optional | The prefix to add to the extracted keys. Default is `null`. |
`strip_brackets` | Optional | If set to `true`, strips brackets (`()`, `<>,` or `[]`) and quotes (`'` or `"`) from extracted values. Default is `false`.
`trim_key` | Optional | The string of characters to trim from the extracted keys. |
`trim value` | Optional | The string of characters to trim from the extracted values. |
`description`  | Optional  | A brief description of the processor.  |
`if` | Optional | A condition for running the processor. |
`ignore_failure` | Optional | If set to `true`, failures are ignored. Default is `false`. |
`on_failure` | Optional | A list of processors to run if the processor fails. |
`ignore_missing`  | Optional  | Specifies whether the processor should ignore documents that do not contain the specified field. Default is `false`.  |
`tag` | Optional | An identifier tag for the processor. Useful for debugging in order to distinguish between processors of the same type. |
`target_field`  | Optional  | The name of the field in which to insert the extracted keys. Default is `null`. |

## Using the processor

Follow these steps to use the processor in a pipeline.

**Step 1: Create a pipeline**

The following query creates a pipeline, named `kv-pipeline`, that uses the `kv` processor to extract the `message` field of a document:

```json
PUT _ingest/pipeline/kv-pipeline
{
  "description" : "Pipeline that extracts user profile data",
  "processors" : [
    {
      "kv" : {
        "field" : "message",
        "field_split": " ",
        "value_split": "="
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
POST _ingest/pipeline/kv-pipeline/_simulate
{
  "docs": [
    {
      "_index": "testindex1",
      "_id": "1",
      "_source":{
         "message": "goodbye=everybody hello=world"
      }
    }
  ]
}
```

**Response**

The following example response confirms that, in addition to the original `message` field, the document contains fields generated from key-value pairs:

```json
{
  "docs": [
    {
      "doc": {
        "_index": "testindex1",
        "_id": "1",
        "_source": {
          "hello": "world",
          "message": "goodbye=everybody hello=world",
          "goodbye": "everybody"
        },
        "_ingest": {
          "timestamp": "2023-12-06T09:59:21.823292Z"
        }
      }
    }
  ]
}
```

**Step 3: Ingest a document**

The following query ingests a document into an index named `testindex1`:

```json
PUT testindex1/_doc/1?pipeline=kv-pipeline
{
  "message": "goodbye=everybody hello=world"
}
```

**Step 4 (Optional): Retrieve the document**

To retrieve the document, run the following query:

```json
GET testindex1/_doc/1
```
