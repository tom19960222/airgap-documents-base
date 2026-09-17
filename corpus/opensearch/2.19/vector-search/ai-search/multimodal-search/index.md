---
collection: "opensearch"
version: "2.19"
title: "Multimodal search"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_vector-search/ai-search/multimodal-search.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_vector-search/ai-search/multimodal-search.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/vector-search/ai-search/multimodal-search/"
canonical_url: "https://docs.opensearch.org/latest/vector-search/ai-search/multimodal-search/"
canonical_route: "/vector-search/ai-search/multimodal-search/"
redirect_from: ["/search-plugins/neural-multimodal-search/","/search-plugins/multimodal-search/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
layout: "default"
nav_order: 40
parent: "AI search"
---
# Multimodal search
Introduced 2.11
{: .label .label-purple }

Use multimodal search to search text and image data using multimodal embedding models.

**PREREQUISITE**<br>
Before using text search, you must set up a multimodal embedding model. For more information, see [Choosing a model](../../../ml-commons-plugin/integrating-ml-models/index.md#choosing-a-model).
{: .note}

## Configuring multimodal search

There are two ways to configure multimodal search:

- [**Automated workflow**](#automated-workflow) (Recommended for quick setup): Automatically create an ingest pipeline and index with minimal configuration.
- [**Manual setup**](#manual-setup) (Recommended for custom configurations): Manually configure each component for greater flexibility and control.

## Automated workflow

OpenSearch provides a [workflow template](../../../automating-configurations/workflow-templates/index.md#multimodal-search) that automatically creates both an ingest pipeline and an index. You must provide the model ID for the configured model when creating a workflow. Review the multimodal search workflow template [defaults](https://github.com/opensearch-project/flow-framework/blob/main/src/main/resources/defaults/multi-modal-search-defaults.json) to determine whether you need to update any of the parameters. For example, if the model dimensionality is different from the default (`1024`), specify the dimensionality of your model in the `output_dimension` parameter. To create the default multimodal search workflow, send the following request:

```json
POST /_plugins/_flow_framework/workflow?use_case=multimodal_search&provision=true
{
"create_ingest_pipeline.model_id": "mBGzipQB2gmRjlv_dOoB"
}
```

OpenSearch responds with a workflow ID for the created workflow:

```json
{
  "workflow_id" : "U_nMXJUBq_4FYQzMOS4B"
}
```

To check the workflow status, send the following request:

```json
GET /_plugins/_flow_framework/workflow/U_nMXJUBq_4FYQzMOS4B/_status
```

Once the workflow completes, the `state` changes to `COMPLETED`. The workflow creates the following components:

- An ingest pipeline named `nlp-ingest-pipeline`
- An index named `my-nlp-index`

You can now continue with [steps 3 and 4](#step-3-ingest-documents-into-the-index) to ingest documents into the index and search the index.

## Manual setup

To manually configure multimodal search with text and image embeddings, follow these steps:

1. [Create an ingest pipeline](#step-1-create-an-ingest-pipeline).
1. [Create an index for ingestion](#step-2-create-an-index-for-ingestion).
1. [Ingest documents into the index](#step-3-ingest-documents-into-the-index).
1. [Search the index](#step-4-search-the-index).

## Step 1: Create an ingest pipeline

To generate vector embeddings, you need to create an [ingest pipeline](../../../api-reference/ingest-apis/index.md) that contains a [`text_image_embedding` processor](../../../ingest-pipelines/processors/text-image-embedding/index.md), which will convert the text or image in a document field to vector embeddings. The processor's `field_map` determines the text and image fields from which to generate vector embeddings and the output vector field in which to store the embeddings.

The following example request creates an ingest pipeline where the text from `image_description` and an image from `image_binary` will be converted into text embeddings and the embeddings will be stored in `vector_embedding`:

```json
PUT /_ingest/pipeline/nlp-ingest-pipeline
{
  "description": "A text/image embedding pipeline",
  "processors": [
    {
      "text_image_embedding": {
        "model_id": "-fYQAosBQkdnhhBsK593",
        "embedding": "vector_embedding",
        "field_map": {
          "text": "image_description",
          "image": "image_binary"
        }
      }
    }
  ]
}
```

## Step 2: Create an index for ingestion

In order to use the text embedding processor defined in your pipeline, create a vector index, adding the pipeline created in the previous step as the default pipeline. Ensure that the fields defined in the `field_map` are mapped as correct types. Continuing with the example, the `vector_embedding` field must be mapped as a k-NN vector with a dimension that matches the model dimension. Similarly, the `image_description` field should be mapped as `text`, and the `image_binary` should be mapped as `binary`.

The following example request creates a vector index that is set up with a default ingest pipeline:

```json
PUT /my-nlp-index
{
  "settings": {
    "index.knn": true,
    "default_pipeline": "nlp-ingest-pipeline",
    "number_of_shards": 2
  },
  "mappings": {
    "properties": {
      "vector_embedding": {
        "type": "knn_vector",
        "dimension": 1024,
        "method": {
          "name": "hnsw",
          "engine": "lucene",
          "parameters": {}
        }
      },
      "image_description": {
        "type": "text"
      },
      "image_binary": {
        "type": "binary"
      }
    }
  }
}
```

For more information about creating a vector index and its supported methods, see [Creating a vector index](../../creating-vector-index/index.md).

## Step 3: Ingest documents into the index

To ingest documents into the index created in the previous step, send the following request:

```json
PUT /nlp-index/_doc/1
{
 "image_description": "Orange table",
 "image_binary": "iVBORw0KGgoAAAANSUI..."
}
```

Before the document is ingested into the index, the ingest pipeline runs the `text_image_embedding` processor on the document, generating vector embeddings for the `image_description` and `image_binary` fields. In addition to the original `image_description` and `image_binary` fields, the indexed document includes the `vector_embedding` field, which contains the combined vector embeddings.

## Step 4: Search the index

To perform a vector search on your index, use the `neural` query clause either in the [Search for a Model API](../../api/knn/index.md#search-for-a-model) or [Query DSL](../../../query-dsl/index.md) queries. You can refine the results by using a [vector search filter](../../filter-search-knn/index.md). You can search by text, image, or both text and image.

The following example request uses a neural query to search for text and image:

```json
GET /my-nlp-index/_search
{
  "size": 10,
  "query": {
    "neural": {
      "vector_embedding": {
        "query_text": "Orange table",
        "query_image": "iVBORw0KGgoAAAANSUI...",
        "model_id": "-fYQAosBQkdnhhBsK593",
        "k": 5
      }
    }
  }
}
```

To eliminate passing the model ID with each neural query request, you can set a default model on a vector index or a field. To learn more, see [Setting a default model on an index or field](../semantic-search/index.md##setting-a-default-model-on-an-index-or-field).

## Next steps

- Explore our [tutorials](../../../tutorials/vector-search/index.md) to learn how to build AI search applications.
