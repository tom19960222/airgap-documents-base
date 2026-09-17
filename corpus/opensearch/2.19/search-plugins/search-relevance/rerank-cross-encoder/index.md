---
collection: "opensearch"
version: "2.19"
title: "Reranking using a cross-encoder model"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/search-relevance/rerank-cross-encoder.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/search-relevance/rerank-cross-encoder.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/search-relevance/rerank-cross-encoder/"
canonical_url: "https://docs.opensearch.org/latest/search-plugins/search-relevance/rerank-cross-encoder/"
canonical_route: "/search-plugins/search-relevance/rerank-cross-encoder/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Search relevance"
has_children: false
layout: "default"
nav_order: 10
parent: "Reranking search results"
---
# Reranking search results using a cross-encoder model
Introduced 2.12
{: .label .label-purple }

You can rerank search results using a cross-encoder model in order to improve search relevance. To implement reranking, you need to configure a [search pipeline](../../search-pipelines/index.md) that runs at search time. The search pipeline intercepts search results and applies the [`rerank` processor](../../search-pipelines/rerank-processor/index.md) to them. The `rerank` processor evaluates the search results and sorts them based on the new scores provided by the cross-encoder model.

**PREREQUISITE**<br>
Before configuring a reranking pipeline, you must set up a cross-encoder model. For information about using an OpenSearch-provided model, see [Cross-encoder models](../../../ml-commons-plugin/pretrained-models/index.md#cross-encoder-models). For information about using a custom model, see [Custom local models](../../../ml-commons-plugin/custom-local-models/index.md).
{: .note}

## Running a search with reranking

To run a search with reranking, follow these steps:

1. [Configure a search pipeline](#step-1-configure-a-search-pipeline).
1. [Create an index for ingestion](#step-2-create-an-index-for-ingestion).
1. [Ingest documents into the index](#step-3-ingest-documents-into-the-index).
1. [Search using reranking](#step-4-search-using-reranking).

## Step 1: Configure a search pipeline

Next, configure a search pipeline with a [`rerank` processor](../../search-pipelines/rerank-processor/index.md) and specify the `ml_opensearch` rerank type. In the request, provide a model ID for the cross-encoder model and the document fields to use as context:

```json
PUT /_search/pipeline/my_pipeline
{
  "description": "Pipeline for reranking with a cross-encoder",
  "response_processors": [
    {
      "rerank": {
        "ml_opensearch": {
          "model_id": "gnDIbI0BfUsSoeNT_jAw"
        },
        "context": {
          "document_fields": [
            "passage_text"
          ]
        }
      }
    }
  ]
}
```

For more information about the request fields, see [Request fields](../../search-pipelines/rerank-processor/index.md#request-body-fields).

## Step 2: Create an index for ingestion

In order to use the `rerank` processor defined in your pipeline, create an OpenSearch index and add the pipeline created in the previous step as the default pipeline:

```json
PUT /my-index
{
  "settings": {
    "index.search.default_pipeline" : "my_pipeline"
  },
  "mappings": {
    "properties": {
      "passage_text": {
        "type": "text"
      }
    }
  }
}
```

## Step 3: Ingest documents into the index

To ingest documents into the index created in the previous step, send the following bulk request:

```json
POST /_bulk
{ "index": { "_index": "my-index" } }
{ "passage_text" : "I said welcome to them and we entered the house" }
{ "index": { "_index": "my-index" } }
{ "passage_text" : "I feel welcomed in their family" }
{ "index": { "_index": "my-index" } }
{ "passage_text" : "Welcoming gifts are great" }

```

## Step 4: Search using reranking

To perform a reranking search on your index, use any OpenSearch query and provide an additional `ext.rerank` field:

```json
POST /my-index/_search
{
  "query": {
    "match": {
      "passage_text": "how to welcome in family"
    }
  },
  "ext": {
    "rerank": {
      "query_context": {
         "query_text": "how to welcome in family"
      }
    }
  }
}
```

Alternatively, you can provide the full path to the field containing the context. For more information, see [Rerank processor example](../../search-pipelines/rerank-processor/index.md#example).

## Next steps

- Learn more about the [`rerank` processor](../../search-pipelines/rerank-processor/index.md).
- See a comprehensive example of [reranking by a field using an externally hosted cross-encoder model](../rerank-by-field-cross-encoder/index.md).
