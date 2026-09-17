---
collection: "opensearch"
version: "2.19"
title: "Rerank"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/search-pipelines/rerank-processor.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/search-pipelines/rerank-processor.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/search-pipelines/rerank-processor/"
canonical_url: "https://docs.opensearch.org/latest/search-plugins/search-pipelines/rerank-processor/"
canonical_route: "/search-plugins/search-pipelines/rerank-processor/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Search pipelines"
has_children: false
layout: "default"
nav_order: 110
parent: "Search processors"
---
# Rerank processor
Introduced 2.12
{: .label .label-purple }

The `rerank` search response processor intercepts and reranks search results. The processor orders documents in the search results based on their new scores.

OpenSearch supports the following rerank types.

Type | Description | Earliest available version
:--- | :--- | :---
[`ml_opensearch`](#the-ml_opensearch-rerank-type) | Applies an OpenSearch-provided cross-encoder model. | 2.12
[`by_field`](#the-by_field-rerank-type) | Applies reranking based on a user-provided field. | 2.18

## Request body fields

The following table lists all available request fields.

Field | Data type | Required/Optional | Description
:--- | :--- | :--- | :---
`<rerank_type>` | Object | Required | The rerank type for document reranking. Valid values are `ml-opensearch` and `by_field`.
`context` | Object |  Required for the `ml_opensearch` rerank type. Optional and does not affect the results for the `by_field` rerank type. | Provides the `rerank` processor with information necessary for reranking at query time.
`tag` | String | Optional | The processor's identifier.
`description` | String | Optional | A description of the processor.
`ignore_failure` | Boolean | Optional | If `true`, OpenSearch [ignores any failure](../creating-search-pipeline/index.md#ignoring-processor-failures) of this processor and continues to run the remaining processors in the search pipeline. Default is `false`.

<!-- vale off -->
## The ml_opensearch rerank type
<!-- vale on -->
Introduced 2.12
{: .label .label-purple }

To rerank results using a cross-encoder model, specify the `ml_opensearch` rerank type.

### Prerequisite

Before using the `ml_opensearch` rerank type, you must configure a cross-encoder model. For information about using an OpenSearch-provided model, see [Cross-encoder models](../../../ml-commons-plugin/pretrained-models/index.md#cross-encoder-models). For information about using a custom model, see [Custom local models](../../../ml-commons-plugin/custom-local-models/index.md).

The `ml_opensearch` rerank type supports the following fields. All fields are required.

Field  | Data type | Description
:--- | :---  | :---
`ml_opensearch.model_id` | String | The model ID of the cross-encoder model for reranking. For more information, see [Using ML models](../../../ml-commons-plugin/using-ml-models/index.md).
`context.document_fields` | Array | An array of document fields that specifies the fields from which to retrieve context for the cross-encoder model.

### Example

The following example demonstrates using a search pipeline with a `rerank` processor implemented using the `ml_opensearch` rerank type. For a complete example, see [Reranking using a cross-encoder model](../../search-relevance/rerank-cross-encoder/index.md).

### Creating a search pipeline

The following request creates a search pipeline with a `rerank` response processor:

```json
PUT /_search/pipeline/rerank_pipeline
{
  "response_processors": [
    {
      "rerank": {
        "ml_opensearch": {
          "model_id": "gnDIbI0BfUsSoeNT_jAw"
        },
        "context": {
          "document_fields": [ "title", "text_representation"]
        }
      }
    }
  ]
}
```

### Using a search pipeline

Combine an OpenSearch query with an `ext` object that contains the query context for the large language model (LLM). Provide the `query_text` that will be used to rerank the results:

```json
POST /_search?search_pipeline=rerank_pipeline
{
  "query": {
    "match": {
      "text_representation": "Where is Albuquerque?"
    }
  },
  "ext": {
    "rerank": {
      "query_context": {
        "query_text": "Where is Albuquerque?"
      }
    }
  }
}
```

Instead of specifying `query_text`, you can provide a full path to the field containing text to use for reranking. For example, if you specify a subfield `query` in the `text_representation` object, specify its path in the `query_text_path` parameter:

```json
POST /_search?search_pipeline=rerank_pipeline
{
  "query": {
    "match": {
      "text_representation": {
        "query": "Where is Albuquerque?"
      }
    }
  },
  "ext": {
    "rerank": {
      "query_context": {
        "query_text_path": "query.match.text_representation.query"
      }
    }
  }
}
```

The `query_context` object contains the following fields. You must provide either `query_text` or `query_text_path` but cannot provide both simultaneously.

Field name | Required/Optional | Description
:--- | :--- | :---
`query_text` | Exactly one of `query_text` or `query_text_path` is required. | The natural language text of the question that you want to use to rerank the search results.
`query_text_path` | Exactly one of `query_text` or `query_text_path` is required. | The full JSON path to the text of the question that you want to use to rerank the search results. The maximum number of characters allowed in the path is `1000`.

<!-- vale off -->
## The by_field rerank type
<!-- vale on -->
Introduced 2.18
{: .label .label-purple }

To rerank results by a document field, specify the `by_field` rerank type.

The `by_field` object supports the following fields.

Field  | Data type | Required/Optional | Description
:--- | :---  | :--- | :---
`target_field` | String | Required |  Specifies the field name or a dot path to the field containing the score to use for reranking.
`remove_target_field` | Boolean | Optional | If `true`, the response does not include the `target_field` used to perform reranking. Default is `false`.
`keep_previous_score` | Boolean | Optional | If `true`, the response includes a `previous_score` field, which contains the score calculated before reranking and can be useful when debugging. Default is `false`.

### Example

The following example demonstrates using a search pipeline with a `rerank` processor implemented using the `by_field` rerank type. For a complete example, see [Reranking by a document field](../../search-relevance/rerank-by-field/index.md).

### Creating a search pipeline

The following request creates a search pipeline with a `by_field` rerank type response processor that ranks the documents by the `reviews.stars` field and specifies to return the original document score:

```json
PUT /_search/pipeline/rerank_byfield_pipeline
{
  "response_processors": [
    {
      "rerank": {
        "by_field": {
          "target_field": "reviews.stars",
          "keep_previous_score" : true
        }
      }
    }
  ]
}
```

### Using the search pipeline

To apply the search pipeline to a query, provide the search pipeline name in the query parameter:

```json
POST /book-index/_search?search_pipeline=rerank_byfield_pipeline
{
  "query": {
     "match_all": {}
  }
}
```

## Next steps

- Learn more about [reranking search results](../../search-relevance/reranking-search-results/index.md).
- See a complete example of [reranking using a cross-encoder model](../../search-relevance/rerank-cross-encoder/index.md).
- See a complete example of [reranking by a document field](../../search-relevance/rerank-by-field/index.md).
- See a comprehensive example of [reranking by a field using an externally hosted cross-encoder model](../../search-relevance/rerank-by-field-cross-encoder/index.md).
