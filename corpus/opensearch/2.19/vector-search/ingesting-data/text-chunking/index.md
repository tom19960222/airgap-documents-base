---
collection: "opensearch"
version: "2.19"
title: "Text chunking"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_vector-search/ingesting-data/text-chunking.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_vector-search/ingesting-data/text-chunking.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/vector-search/ingesting-data/text-chunking/"
canonical_url: "https://docs.opensearch.org/latest/vector-search/ingesting-data/text-chunking/"
canonical_route: "/vector-search/ingesting-data/text-chunking/"
redirect_from: ["/search-plugins/text-chunking/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 80
parent: "Ingesting data"
---
# Text chunking
Introduced 2.13
{: .label .label-purple }

When working with large text documents in [AI search](../../ai-search/index.md), it's often necessary to split them into smaller passages because most embedding models have token length limitations. This process, called _text chunking_, helps maintain the quality and relevance of vector search results by ensuring that each embedding represents a focused piece of content that fits within model constraints.

To split long text into passages, you can use a `text_chunking` processor as a preprocessing step for a `text_embedding` or `sparse_encoding` processor in order to obtain embeddings for each chunked passage. For more information about the processor parameters, see [Text chunking processor](../../../ingest-pipelines/processors/text-chunking/index.md). Before you start, follow the steps outlined in the [pretrained model documentation](../../../ml-commons-plugin/pretrained-models/index.md) to register an embedding model. The following example preprocesses text by splitting it into passages and then produces embeddings using the `text_embedding` processor.

## Step 1: Create a pipeline

The following example request creates an ingest pipeline that converts the text in the `passage_text` field into chunked passages, which will be stored in the `passage_chunk` field. The text in the `passage_chunk` field is then converted into text embeddings, and the embeddings are stored in the `passage_embedding` field:

```json
PUT _ingest/pipeline/text-chunking-embedding-ingest-pipeline
{
  "description": "A text chunking and embedding ingest pipeline",
  "processors": [
    {
      "text_chunking": {
        "algorithm": {
          "fixed_token_length": {
            "token_limit": 10,
            "overlap_rate": 0.2,
            "tokenizer": "standard"
          }
        },
        "field_map": {
          "passage_text": "passage_chunk"
        }
      }
    },
    {
      "text_embedding": {
        "model_id": "LMLPWY4BROvhdbtgETaI",
        "field_map": {
          "passage_chunk": "passage_chunk_embedding"
        }
      }
    }
  ]
}
```

## Step 2: Create an index for ingestion

In order to use the ingest pipeline, you need to create a vector index. The `passage_chunk_embedding` field must be of the `nested` type. The `knn.dimension` field must contain the number of dimensions for your model:

```json
PUT testindex
{
  "settings": {
    "index": {
      "knn": true
    }
  },
  "mappings": {
    "properties": {
      "text": {
        "type": "text"
      },
      "passage_chunk_embedding": {
        "type": "nested",
        "properties": {
          "knn": {
            "type": "knn_vector",
            "dimension": 768
          }
        }
      }
    }
  }
}
```

## Step 3: Ingest documents into the index

To ingest a document into the index created in the previous step, send the following request:

```json
POST testindex/_doc?pipeline=text-chunking-embedding-ingest-pipeline
{
  "passage_text": "This is an example document to be chunked. The document contains a single paragraph, two sentences and 24 tokens by standard tokenizer in OpenSearch."
}
```

## Step 4: Search the index

You can use a `nested` query to perform vector search on your index. We recommend setting `score_mode` to `max`, where the document score is set to the highest score out of all passage embeddings:

```json
GET testindex/_search
{
  "query": {
    "nested": {
      "score_mode": "max",
      "path": "passage_chunk_embedding",
      "query": {
        "neural": {
          "passage_chunk_embedding.knn": {
            "query_text": "document",
            "model_id": "-tHZeI4BdQKclr136Wl7"
          }
        }
      }
    }
  }
}
```

## Next steps

- Explore our [tutorials](../../../tutorials/vector-search/index.md) to learn how to build AI search applications.
