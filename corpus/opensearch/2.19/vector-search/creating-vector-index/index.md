---
collection: "opensearch"
version: "2.19"
title: "Creating a vector index"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_vector-search/creating-vector-index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_vector-search/creating-vector-index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/vector-search/creating-vector-index/"
canonical_url: "https://docs.opensearch.org/latest/vector-search/creating-vector-index/"
canonical_route: "/vector-search/creating-vector-index/"
redirect_from: ["/vector-search/creating-a-vector-db/","/search-plugins/knn/knn-index/","/vector-search/creating-vector-index/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 20
---
# Creating a vector index

Creating a vector index in OpenSearch involves a common core process with some variations depending on the type of vector search. This guide outlines the key elements shared across all vector indexes and the differences specific to supported use cases.

Before you start, review the options for generating embeddings to help you decide on the option suitable for your use case. For more information, see [Preparing vectors](../getting-started/vector-search-options/index.md).
{: .tip}

## Overview

To create a vector index, set the `index.knn` parameter to `true`in the `settings`:

```json
PUT /test-index
{
  "settings": {
    "index.knn": true
  },
  "mappings": {
    "properties": {
      "my_vector": {
        "type": "knn_vector",
        "dimension": 3,
        "space_type": "l2",
        "mode": "on_disk",
        "method": {
          "name": "hnsw"
        }
      }
    }
  }
}
```

Creating a vector index involves the following key steps:

1. **Enable k-nearest neighbors (k-NN) search**:
   Set `index.knn` to `true` in the index settings to enable k-NN search functionality.

1. **Define a vector field**:
   Specify the field that will store the vector data. When defining a `knn_vector` field in OpenSearch, you can select from different data types to balance storage requirements and performance. By default, k-NN vectors are float vectors, but you can also choose byte or binary vectors for more efficient storage. For more information, see [k-NN vector](../../field-types/supported-field-types/knn-vector/index.md).

1. **Specify the dimension**:
   Set the `dimension` property to match the size of the vectors used.

1. (Optional) **Choose a space type**:
   Select a distance metric for similarity comparisons, such as `l2` (Euclidean distance) or `cosinesimil`. For more information, see [Spaces](../../field-types/supported-field-types/knn-spaces/index.md).

1. (Optional) **Select a workload mode and/or compression level**:
   Select a workload mode and/or compression level in order to optimize vector storage. For more information, see [Optimizing vector storage](../optimizing-storage/index.md).

1. (Optional, advanced) **Select a method**:
   Configure the indexing method, such as HNSW or IVF, used to optimize vector search performance. For more information, see [Methods and engines](../../field-types/supported-field-types/knn-methods-engines/index.md).

## Implementation options

Based on your vector generation approach, choose one of the following implementation options:

- [Store raw vectors or embeddings generated outside of OpenSearch](#storing-raw-vectors-or-embeddings-generated-outside-of-opensearch): Ingest pregenerated embeddings or raw vectors into your index for raw vector search.
- [Convert data to embeddings during ingestion](#converting-data-to-embeddings-during-ingestion): Ingest text that will be converted into vector embeddings in OpenSearch in order to perform semantic search using machine learning (ML) models.

The following table summarizes key index configuration differences for the supported use cases.

| Feature                  | Vector field type | Ingest pipeline | Transformation     | Use case   |
|--------------------------|-----------------------|---------------------|-------------------------|-------------------------|
| **Store raw vectors or embeddings generated outside of OpenSearch**   | [`knn_vector`](../../field-types/supported-field-types/knn-vector/index.md)         | Not required        | Direct ingestion        | Raw vector search   |
| **Convert data to embeddings during ingestion**      | [`knn_vector`](../../field-types/supported-field-types/knn-vector/index.md)         | Required            | Auto-generated vectors  | AI search <br><br> Automating embedding generation reduces data preprocessing and provides a more managed vector search experience.     |

## Storing raw vectors or embeddings generated outside of OpenSearch

To ingest raw vectors into an index, configure a vector field (in this request, `my_vector`) and specify its `dimension`:

```json
PUT /my-raw-vector-index
{
  "settings": {
    "index.knn": true
  },
  "mappings": {
    "properties": {
      "my_vector": {
        "type": "knn_vector",
        "dimension": 3
      }
    }
  }
}
```

## Converting data to embeddings during ingestion

To automatically generate embeddings during ingestion, configure an [ingest pipeline](../../api-reference/ingest-apis/index.md) with the model ID of the embedding model. For more information about configuring a model, see [Integrating ML models](../../ml-commons-plugin/integrating-ml-models/index.md).

Specify the `field_map` to define the source field for input text and the target field for storing embeddings. In this example, text from the `text` field is converted into embeddings and stored in `passage_embedding`:

```json
PUT /_ingest/pipeline/auto-embed-pipeline
{
  "description": "AI search ingest pipeline that automatically converts text to embeddings",
  "processors": [
    {
      "text_embedding": {
        "model_id": "mBGzipQB2gmRjlv_dOoB",
        "field_map": {
          "input_text": "output_embedding"
        }
      }
    }
  ]
}
```

For more information, see [Text embedding processor](../../ingest-pipelines/processors/text-embedding/index.md).

When creating an index, specify the pipeline as the `default_pipeline`. Ensure that `dimension` matches the dimensionality of the model configured in the pipeline:

```json
PUT /my-ai-search-index
{
  "settings": {
    "index.knn": true,
    "default_pipeline": "auto-embed-pipeline"
  },
  "mappings": {
    "properties": {
      "input_text": {
        "type": "text"
      },
      "output_embedding": {
        "type": "knn_vector",
        "dimension": 768
      }
    }
  }
}
```

## Working with sparse vectors

OpenSearch also supports sparse vectors. For more information, see [Neural sparse search](../ai-search/neural-sparse-search/index.md).

## Next steps

- [Ingesting data into a vector index](../searching-data/index.md)
- [k-NN vector](../../field-types/supported-field-types/knn-vector/index.md)
- [Methods and engines](../../field-types/supported-field-types/knn-methods-engines/index.md)
