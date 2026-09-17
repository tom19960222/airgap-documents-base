---
collection: "opensearch"
version: "2.19"
title: "Neural sparse search using raw vectors"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_vector-search/ai-search/neural-sparse-with-raw-vectors.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_vector-search/ai-search/neural-sparse-with-raw-vectors.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/vector-search/ai-search/neural-sparse-with-raw-vectors/"
canonical_url: "https://docs.opensearch.org/latest/vector-search/ai-search/neural-sparse-with-raw-vectors/"
canonical_route: "/vector-search/ai-search/neural-sparse-with-raw-vectors/"
redirect_from: ["/search-plugins/neural-sparse-with-raw-vectors/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "AI search"
has_children: false
layout: "default"
nav_order: 20
parent: "Neural sparse search"
---
# Neural sparse search using raw vectors

If you're using self-hosted sparse embedding models, you can ingest raw sparse vectors and use neural sparse search.

## Tutorial

This tutorial consists of the following steps:

1. [**Ingest sparse vectors**](#step-1-ingest-sparse-vectors)
    1. [Create an index](#step-1a-create-an-index)
    1. [Ingest documents into the index](#step-1b-ingest-documents-into-the-index)
1. [**Search the data using raw sparse vector**](#step-2-search-the-data-using-a-sparse-vector).

## Step 1: Ingest sparse vectors

Once you have generated sparse vector embeddings, you can directly ingest them into OpenSearch.

### Step 1(a): Create an index

In order to ingest documents containing raw sparse vectors, create a rank features index:

```json
PUT /my-nlp-index
{
  "mappings": {
    "properties": {
      "id": {
        "type": "text"
      },
      "passage_embedding": {
        "type": "rank_features"
      },
      "passage_text": {
        "type": "text"
      }
    }
  }
}
```

### Step 1(b): Ingest documents into the index

To ingest documents into the index created in the previous step, send the following request:

```json
PUT /my-nlp-index/_doc/1
{
  "passage_text": "Hello world",
  "id": "s1",
  "passage_embedding": {
    "hi" : 4.338913,
    "planets" : 2.7755864,
    "planet" : 5.0969057,
    "mars" : 1.7405145,
    "earth" : 2.6087382,
    "hello" : 3.3210192
  }
}
```

## Step 2: Search the data using a sparse vector

To search the documents using a sparse vector, provide the sparse embeddings in the `neural_sparse` query:

```json
GET my-nlp-index/_search
{
  "query": {
    "neural_sparse": {
      "passage_embedding": {
        "query_tokens": {
          "hi" : 4.338913,
          "planets" : 2.7755864,
          "planet" : 5.0969057,
          "mars" : 1.7405145,
          "earth" : 2.6087382,
          "hello" : 3.3210192
        }
      }
    }
  }
}
```

## Accelerating neural sparse search

To learn more about improving retrieval time for neural sparse search, see [Accelerating neural sparse search](../neural-sparse-search/index.md#accelerating-neural-sparse-search).

## Next steps

- Explore our [tutorials](../../../tutorials/vector-search/index.md) to learn how to build AI search applications.
