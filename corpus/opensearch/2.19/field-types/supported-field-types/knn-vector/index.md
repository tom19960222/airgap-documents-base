---
collection: "opensearch"
version: "2.19"
title: "k-NN vector"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/supported-field-types/knn-vector.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/supported-field-types/knn-vector.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/supported-field-types/knn-vector/"
canonical_url: "https://docs.opensearch.org/latest/mappings/supported-field-types/knn-vector/"
canonical_route: "/mappings/supported-field-types/knn-vector/"
redirect_from: ["/mappings/supported-field-types/knn-vector/","/mappings/supported-field-types/vector-field-types/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_math: true
layout: "default"
nav_order: 20
parent: "Supported field types"
---
# k-NN vector
**Introduced 1.0**
{: .label .label-purple }

The `knn_vector` data type allows you to ingest vectors into an OpenSearch index and perform different kinds of vector search. The `knn_vector` field is highly configurable and can serve many different vector workloads. In general, a `knn_vector` field can be built either by [providing a method definition](#method-definitions) or [specifying a model ID](#model-ids).

## Example

To map `my_vector` as a `knn_vector`, use the following request:

```json
PUT /test-index
{
  "settings": {
    "index": {
      "knn": true
    }
  },
  "mappings": {
    "properties": {
      "my_vector": {
        "type": "knn_vector",
        "dimension": 3,
        "space_type": "l2"
      }
    }
  }
}
```

## Optimizing vector storage

To optimize vector storage, you can specify a [vector workload mode](../knn-memory-optimized/index.md#vector-workload-modes) as `in_memory` (which optimizes for lowest latency) or `on_disk` (which optimizes for lowest cost). The `on_disk` mode reduces memory usage. Optionally, you can specify a [`compression_level`](../knn-memory-optimized/index.md#compression-levels) to fine-tune the vector memory consumption:

```json
PUT test-index
{
  "settings": {
    "index": {
      "knn": true
    }
  },
  "mappings": {
    "properties": {
      "my_vector": {
        "type": "knn_vector",
        "dimension": 3,
        "space_type": "l2",
        "mode": "on_disk",
        "compression_level": "16x"
      }
    }
  }
}
```

## Method definitions

[Method definitions](../knn-methods-engines/index.md) are used when the underlying [approximate k-NN (ANN)](../../../vector-search/vector-search-techniques/approximate-knn/index.md) algorithm does not require training. For example, the following `knn_vector` field specifies that a Faiss implementation of HNSW should be used for ANN search. During indexing, Faiss builds the corresponding HNSW segment files:

```json
PUT test-index
{
  "settings": {
    "index": {
      "knn": true,
      "knn.algo_param.ef_search": 100
    }
  },
  "mappings": {
    "properties": {
      "my_vector1": {
        "type": "knn_vector",
        "dimension": 1024,
        "method": {
          "name": "hnsw",
          "space_type": "l2",
          "engine": "faiss",
          "parameters": {
            "ef_construction": 100,
            "m": 16
          }
        }
      }
    }
  }
}
```

You can also specify the `space_type` at the top level:

```json
PUT test-index
{
  "settings": {
    "index": {
      "knn": true,
      "knn.algo_param.ef_search": 100
    }
  },
  "mappings": {
    "properties": {
      "my_vector1": {
        "type": "knn_vector",
        "dimension": 1024,
        "space_type": "l2",
        "method": {
          "name": "hnsw",
          "engine": "faiss",
          "parameters": {
            "ef_construction": 100,
            "m": 16
          }
        }
      }
    }
  }
}
```

## Model IDs

Model IDs are used when the underlying ANN algorithm requires a training step. As a prerequisite, the model must be created using the [Train API](../../../vector-search/api/knn/index.md#train-a-model). The model contains the information needed to initialize the native library segment files. To configure a model for a vector field, specify the `model_id`:

```json
"my_vector": {
  "type": "knn_vector",
  "model_id": "my-model"
}
```

However, if you intend to use Painless scripting or a k-NN score script, you only need to pass the `dimension`:

```json
"my_vector": {
   "type": "knn_vector",
   "dimension": 128
 }
```

For more information, see [Building a vector index from a model](../../../vector-search/vector-search-techniques/approximate-knn/index.md#building-a-vector-index-from-a-model).

### Parameters

The following table lists the parameters accepted by k-NN vector field types.

Parameter | Data type | Description
:--- | :---
`type` | String | The vector field type. Must be `knn_vector`. Required.
`dimension` | Integer | The size of the vectors used. Valid values are in the [1, 16,000] range. Required.
`data_type` | String | The data type of the vector elements. Valid values are `binary`, `byte`, and `float`. Optional. Default is `float`.
`space_type` | String | The vector space used to calculate the distance between vectors. Valid values are `l1`, `l2`, `linf`, `cosinesimil`, `innerproduct`, `hamming`, and `hammingbit`. Not every method/engine combination supports each of the spaces. For a list of supported spaces, see the section for a specific engine. Note: This value can also be specified within the `method`. Optional. For more information, see [Spaces](../knn-spaces/index.md).
`mode` | String | Sets appropriate default values for k-NN parameters based on your priority: either low latency or low cost. Valid values are `in_memory` and `on_disk`. Optional. Default is `in_memory`. For more information, see [Memory-optimized vectors](../knn-memory-optimized/index.md).
`compression_level` | String | Selects a quantization encoder that reduces vector memory consumption by the given factor. Valid values are `1x`, `2x`, `4x`, `8x`, `16x`, and `32x`. Optional. For more information, see [Memory-optimized vectors](../knn-memory-optimized/index.md).
`method` | Object | The algorithm used for organizing vector data at indexing time and searching it at search time. Used when the ANN algorithm does not require training. Optional. For more information, see [Methods and engines](../knn-methods-engines/index.md).
`model_id` | String | The model ID of a trained model. Used when the ANN algorithm requires training. See [Model IDs](#model-ids). Optional.

## Next steps

- [Spaces](../knn-spaces/index.md)
- [Methods and engines](../knn-methods-engines/index.md)
- [Memory-optimized vectors](../knn-memory-optimized/index.md)
- [Vector search](../../../vector-search/index.md)
- [k-NN query](../../../query-dsl/specialized/k-nn/index.md)
