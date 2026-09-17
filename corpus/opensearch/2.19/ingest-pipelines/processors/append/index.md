---
collection: "opensearch"
version: "2.19"
title: "Append"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ingest-pipelines/processors/append.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ingest-pipelines/processors/append.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ingest-pipelines/processors/append/"
canonical_url: "https://docs.opensearch.org/latest/ingest-pipelines/processors/append/"
canonical_route: "/ingest-pipelines/processors/append/"
redirect_from: ["/api-reference/ingest-apis/processors/append/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 10
parent: "Ingest processors"
---
This documentation describes using the `append` processor in OpenSearch ingest pipelines. Consider using the [Data Prepper `add_entries` processor](https://docs.opensearch.org/latest/data-prepper/pipelines/configuration/processors/add-entries/) <!-- unresolved-jekyll-link: route=/data-prepper/pipelines/configuration/processors/add-entries/ -->, which runs on the OpenSearch cluster, if your use case involves large or complex datasets.
{: .note}

# Append processor

The `append` processor is used to add values to a field:

- If the field is an array, the `append` processor appends the specified values to that array.
- If the field is a scalar field, the `append` processor converts it to an array and appends the specified values to that array.
- If the field does not exist, the `append` processor creates an array with the specified values.

### Syntax

The following is the syntax for the `append` processor:

```json
{
  "append": {
    "field": "your_target_field",
    "value": ["your_appended_value"]
  }
}
```

## Configuration parameters

The following table lists the required and optional parameters for the `append` processor.

Parameter | Required/Optional | Description |
|-----------|-----------|-----------|
`field`  | Required  | The name of the field containing the data to be appended. Supports [template snippets](../../create-ingest/index.md#template-snippets).|
`value`  | Required  | The value to be appended. This can be a static value or a dynamic value derived from existing fields. Supports [template snippets](../../create-ingest/index.md#template-snippets). |
`description`  | Optional  | A brief description of the processor.  |
`if` | Optional | A condition for running the processor. |
`ignore_failure` | Optional | Specifies whether the processor continues execution even if it encounters errors. If set to `true`, failures are ignored. Default is `false`. |
`allow_duplicates` | Optional | Specifies whether to append the values already contained in the field. If `true`, duplicate values are appended. Otherwise, they are skipped. |
`on_failure` | Optional | A list of processors to run if the processor fails. |
`tag` | Optional | An identifier tag for the processor. Useful for debugging in order to distinguish between processors of the same type. |

## Using the processor

Follow these steps to use the processor in a pipeline.

**Step 1: Create a pipeline**

The following query creates a pipeline, named `user-behavior`, that has one append processor. It appends the `page_view` of each new document ingested into OpenSearch to an array field named `event_types`:

```json
PUT _ingest/pipeline/user-behavior
{
  "description": "Pipeline that appends event type",
  "processors": [
    {
      "append": {
        "field": "event_types",
        "value": ["page_view"]
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
POST _ingest/pipeline/user-behavior/_simulate
{
  "docs":[
    {
      "_source":{
      }
    }
  ]
}
```

**Response**

The following response confirms that the pipeline is working as expected:

```json
{
  "docs": [
    {
      "doc": {
        "_index": "_index",
        "_id": "_id",
        "_source": {
          "event_types": [
            "page_view"
          ]
        },
        "_ingest": {
          "timestamp": "2023-08-28T16:55:10.621805166Z"
        }
      }
    }
  ]
}
```

**Step 3: Ingest a document**

The following query ingests a document into an index named `testindex1`:

```json
PUT testindex1/_doc/1?pipeline=user-behavior
{
}
```

**Step 4 (Optional): Retrieve the document**

To retrieve the document, run the following query:

```json
GET testindex1/_doc/1
```

Because the document does not contain an `event_types` field, an array field is created and the event is appended to the array:

```json
{
  "_index": "testindex1",
  "_id": "1",
  "_version": 2,
  "_seq_no": 1,
  "_primary_term": 1,
  "found": true,
  "_source": {
    "event_types": [
      "page_view"
    ]
  }
}
```
