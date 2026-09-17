---
collection: "opensearch"
version: "2.19"
title: "Text embedding"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ingest-pipelines/processors/text-embedding.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ingest-pipelines/processors/text-embedding.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ingest-pipelines/processors/text-embedding/"
canonical_url: "https://docs.opensearch.org/latest/ingest-pipelines/processors/text-embedding/"
canonical_route: "/ingest-pipelines/processors/text-embedding/"
redirect_from: ["/api-reference/ingest-apis/processors/text-embedding/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 260
parent: "Ingest processors"
---
# Text embedding processor

The `text_embedding` processor is used to generate vector embeddings from text fields for [semantic search](../../../vector-search/ai-search/semantic-search/index.md).

**PREREQUISITE**<br>
Before using the `text_embedding` processor, you must set up a machine learning (ML) model. For more information, see [Choosing a model](../../../ml-commons-plugin/integrating-ml-models/index.md#choosing-a-model).
{: .note}

The following is the syntax for the `text_embedding` processor:

```json
{
  "text_embedding": {
    "model_id": "<model_id>",
    "field_map": {
      "<input_field>": "<vector_field>"
    }
  }
}
```

## Configuration parameters

The following table lists the required and optional parameters for the `text_embedding` processor.

| Parameter  | Data type | Required/Optional  | Description  |
|:---|:---|:---|:---|
`model_id` | String | Required | The ID of the model that will be used to generate the embeddings. The model must be deployed in OpenSearch before it can be used in neural search. For more information, see [Using custom models within OpenSearch](../../../ml-commons-plugin/using-ml-models/index.md) and [Semantic search](../../../vector-search/ai-search/semantic-search/index.md).
`field_map` | Object | Required | Contains key-value pairs that specify the mapping of a text field to a vector field.
`field_map.<input_field>` | String | Required | The name of the field from which to obtain text for generating text embeddings.
`field_map.<vector_field>`  | String | Required | The name of the vector field in which to store the generated text embeddings.
`description`  | String | Optional  | A brief description of the processor.  |
`tag` | String | Optional | An identifier tag for the processor. Useful for debugging to distinguish between processors of the same type. |
`batch_size` | Integer | Optional | Specifies the number of documents to be batched and processed each time. Default is `1`. |
`if` | String containing a Boolean expression | Optional | A condition for running the processor.|
`ignore_failure` | Boolean | Optional | Specifies whether the processor continues execution even if it encounters an error. If set to `true`, the processor failure is ignored. Default is `false`.|
`on_failure` | List | Optional | A list of processors to run if the processor fails. |

## Using the processor

Follow these steps to use the processor in a pipeline. You must provide a model ID when creating the processor. For more information, see [Using custom models within OpenSearch](../../../ml-commons-plugin/using-ml-models/index.md).

**Step 1: Create a pipeline.**

The following example request creates an ingest pipeline where the text from `passage_text` will be converted into text embeddings and the embeddings will be stored in `passage_embedding`:

```json
PUT /_ingest/pipeline/nlp-ingest-pipeline
{
  "description": "A text embedding pipeline",
  "processors": [
    {
      "text_embedding": {
        "model_id": "bQ1J8ooBpBj3wT4HVUsb",
        "field_map": {
          "passage_text": "passage_embedding"
        }
      }
    }
  ]
}
```

**Step 2 (Optional): Test the pipeline.**

It is recommended that you test your pipeline before you ingest documents.
{: .tip}

To test the pipeline, run the following query:

```json
POST _ingest/pipeline/nlp-ingest-pipeline/_simulate
{
  "docs": [
    {
      "_index": "testindex1",
      "_id": "1",
      "_source":{
         "passage_text": "hello world"
      }
    }
  ]
}
```

#### Response

The response confirms that in addition to the `passage_text` field, the processor has generated text embeddings in the `passage_embedding` field:

```json
{
  "docs": [
    {
      "doc": {
        "_index": "testindex1",
        "_id": "1",
        "_source": {
          "passage_embedding": [
            -0.048237972,
            -0.07612712,
            0.3262124,
            ...
            -0.16352308
          ],
          "passage_text": "hello world"
        },
        "_ingest": {
          "timestamp": "2023-10-05T15:15:19.691345393Z"
        }
      }
    }
  ]
}
```

Once you have created an ingest pipeline, you need to create an index for ingestion and ingest documents into the index. To learn more, see [Step 2: Create an index for ingestion](../../../vector-search/ai-search/semantic-search/index.md#step-2-create-an-index-for-ingestion) and [Step 3: Ingest documents into the index](../../../vector-search/ai-search/semantic-search/index.md#step-3-ingest-documents-into-the-index) of [Semantic search](../../../vector-search/ai-search/semantic-search/index.md).

## Next steps

- To learn how to use the `neural` query for text search, see [Neural query](../../../query-dsl/specialized/neural/index.md).
- To learn more about semantic search, see [Semantic search](../../../vector-search/ai-search/semantic-search/index.md).
- To learn more about using models in OpenSearch, see [Choosing a model](../../../ml-commons-plugin/integrating-ml-models/index.md#choosing-a-model).
- For a comprehensive example, see [Getting started with semantic and hybrid search](../../../tutorials/vector-search/neural-search-tutorial/index.md).
