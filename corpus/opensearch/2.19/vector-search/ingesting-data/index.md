---
collection: "opensearch"
version: "2.19"
title: "Ingesting data"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_vector-search/ingesting-data/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_vector-search/ingesting-data/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/vector-search/ingesting-data/"
canonical_url: "https://docs.opensearch.org/latest/vector-search/ingesting-data/index/"
canonical_route: "/vector-search/ingesting-data/"
redirect_from: ["/vector-search/ingesting-data/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 30
---
# Ingesting data into a vector index

After creating a vector index, you need to either ingest raw vector data or convert data to embeddings while ingesting it.

## Comparison of ingestion methods

The following table compares the two ingestion methods.

| Feature                       | Data format          | Ingest pipeline | Vector generation         | Additional fields            |
|-------------------------------|----------------------------|---------------------|---------------------------------|-----------------------------------|
| **Raw vector ingestion**      | Pre-generated vectors      | Not required        | External                        | Optional metadata                |
| **Converting data to embeddings during ingestion** | Text or image data                   | Required            | Internal (during ingestion)     | Original data + embeddings        |

## Raw vector ingestion

When working with raw vectors or embeddings generated outside of OpenSearch, you directly ingest vector data into the `knn_vector` field. No pipeline is required because the vectors are already generated:

```json
PUT /my-raw-vector-index/_doc/1
{
  "my_vector": [0.1, 0.2, 0.3],
  "metadata": "Optional additional information"
}
```

You can also use the [Bulk API](../../api-reference/document-apis/bulk/index.md) to ingest multiple vectors efficiently:

```json
PUT /_bulk
{"index": {"_index": "my-raw-vector-index", "_id": 1}}
{"my_vector": [0.1, 0.2, 0.3], "metadata": "First item"}
{"index": {"_index": "my-raw-vector-index", "_id": 2}}
{"my_vector": [0.2, 0.3, 0.4], "metadata": "Second item"}
```

## Converting data to embeddings during ingestion

After you have [configured an ingest pipeline](../creating-vector-index/index.md#converting-data-to-embeddings-during-ingestion) that automatically generates embeddings, you can ingest text data directly into your index:

```json
PUT /my-ai-search-index/_doc/1
{
  "input_text": "Example: AI search description"
}
```

The pipeline automatically generates and stores the embeddings in the `output_embedding` field.

You can also use the [Bulk API](../../api-reference/document-apis/bulk/index.md) to ingest multiple documents efficiently:

```json
PUT /_bulk
{"index": {"_index": "my-ai-search-index", "_id": 1}}
{"input_text": "Example AI search description"}
{"index": {"_index": "my-ai-search-index", "_id": 2}}
{"input_text": "Bulk API operation description"}
```

## Working with sparse vectors

OpenSearch also supports sparse vectors. For more information, see [Neural sparse search](../ai-search/neural-sparse-search/index.md).

## Text chunking

For information about splitting large documents into smaller passages before generating embeddings during dense or sparse AI search, see [Text chunking](text-chunking/index.md).

## Next steps

- [Searching vector data](../searching-data/index.md)
- [Bulk API](../../api-reference/document-apis/bulk/index.md)
- [Ingest pipelines](../../api-reference/ingest-apis/index.md)
- [Text embedding processor](../../ingest-pipelines/processors/text-embedding/index.md)
