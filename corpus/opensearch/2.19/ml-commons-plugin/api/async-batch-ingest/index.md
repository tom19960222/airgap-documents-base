---
collection: "opensearch"
version: "2.19"
title: "Asynchronous batch ingestion"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/async-batch-ingest.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/async-batch-ingest.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/async-batch-ingest/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/async-batch-ingest/"
canonical_route: "/ml-commons-plugin/api/async-batch-ingest/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
has_toc: false
layout: "default"
nav_order: 35
parent: "ML Commons APIs"
---
# Asynchronous batch ingestion
**Introduced 2.17**
{: .label .label-purple }

Use the Asynchronous Batch Ingestion API to ingest data into your OpenSearch cluster from your files on remote file servers, such as Amazon Simple Storage Service (Amazon S3) or OpenAI. For detailed configuration steps, see [Asynchronous batch ingestion](../../remote-models/async-batch-ingestion/index.md).

## Endpoints

```json
POST /_plugins/_ml/_batch_ingestion
```

#### Request body fields

The following table lists the available request fields.

Field | Data type | Required/Optional | Description
:---  | :--- | :---
`index_name`| String | Required | The index name.
`field_map` | Object | Required | Maps fields from the source file to specific fields in an OpenSearch index for ingestion.
`ingest_fields` | Array | Optional | Lists fields from the source file that should be ingested directly into the OpenSearch index without any additional mapping.
`credential` | Object | Required | Contains the authentication information for accessing external data sources, such as Amazon S3 or OpenAI.
`data_source` | Object | Required | Specifies the type and location of the external file(s) from which the data is ingested.
`data_source.type` | String | Required | Specifies the type of the external data source. Valid values are `s3` and `openAI`.
`data_source.source` | Array | Required | Specifies one or more file locations from which the data is ingested. For `s3`, specify the file path to the Amazon S3 bucket (for example, `["s3://offlinebatch/output/sagemaker_batch.json.out"]`). For `openAI`, specify the file IDs for input or output files (for example, `["file-<your output file id>", "file-<your input file id>", "file-<your other file>"]`).

## Example request: Ingesting a single file

```json
POST /_plugins/_ml/_batch_ingestion
{
  "index_name": "my-nlp-index",
  "field_map": {
    "chapter": "$.content[0]",
    "title": "$.content[1]",
    "chapter_embedding": "$.SageMakerOutput[0]",
    "title_embedding": "$.SageMakerOutput[1]",
    "_id": "$.id"
  },
  "ingest_fields": ["$.id"],
  "credential": {
    "region": "us-east-1",
    "access_key": "<your access key>",
    "secret_key": "<your secret key>",
    "session_token": "<your session token>"
  },
  "data_source": {
    "type": "s3",
    "source": ["s3://offlinebatch/output/sagemaker_batch.json.out"]
  }
}
```

## Example request: Ingesting multiple files

```json
POST /_plugins/_ml/_batch_ingestion
{
  "index_name": "my-nlp-index-openai",
  "field_map": {
    "question": "source[1].$.body.input[0]",
    "answer": "source[1].$.body.input[1]",
    "question_embedding":"source[0].$.response.body.data[0].embedding",
    "answer_embedding":"source[0].$.response.body.data[1].embedding",
    "_id": ["source[0].$.custom_id", "source[1].$.custom_id"]
  },
  "ingest_fields": ["source[2].$.custom_field1", "source[2].$.custom_field2"],
  "credential": {
    "openAI_key": "<you openAI key>"
  },
  "data_source": {
    "type": "openAI",
    "source": ["file-<your output file id>", "file-<your input file id>", "file-<your other file>"]
  }
}
```

## Example response

```json
{
  "task_id": "cbsPlpEBMHcagzGbOQOx",
  "task_type": "BATCH_INGEST",
  "status": "CREATED"
}
```
