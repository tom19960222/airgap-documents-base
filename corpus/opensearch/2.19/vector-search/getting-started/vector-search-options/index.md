---
collection: "opensearch"
version: "2.19"
title: "Preparing vectors"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_vector-search/getting-started/vector-search-options.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_vector-search/getting-started/vector-search-options.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/vector-search/getting-started/vector-search-options/"
canonical_url: "https://docs.opensearch.org/latest/vector-search/getting-started/vector-search-options/"
canonical_route: "/vector-search/getting-started/vector-search-options/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
auto_items: [{"heading":"Configure an embedding model","description":"Configure a machine learning model that will automatically generate embeddings from your text at ingestion time and query time.","link":"/ml-commons-plugin/integrating-ml-models/"},{"heading":"Create an OpenSearch index","description":"Create an OpenSearch index to store your text.","link":"/vector-search/creating-vector-index/#converting-data-to-embeddings-during-ingestion"},{"heading":"Ingest text","description":"Ingest your text into the index.","link":"/vector-search/ingesting-data/#converting-data-to-embeddings-during-ingestion"},{"heading":"Search text","description":"Search your text using vector search. Query text is automatically converted to vector embeddings and compared to document embeddings.","link":"/vector-search/searching-data/#searching-auto-generated-embeddings"}]
layout: "default"
nav_order: 20
parent: "Getting started"
pre_items: [{"heading":"Generate embeddings","description":"Generate embeddings outside of OpenSearch using your favorite embedding utility."},{"heading":"Create an OpenSearch index","description":"Create an OpenSearch index to store your embeddings.","link":"/vector-search/creating-vector-index/#storing-raw-vectors-or-embeddings-generated-outside-of-opensearch"},{"heading":"Ingest embeddings","description":"Ingest your embeddings into the index.","link":"/vector-search/ingesting-data/#raw-vector-ingestion"},{"heading":"Search embeddings","description":"Search your embeddings using vector search.","link":"/vector-search/searching-data/#searching-raw-vectors"}]
quickstart_cards: [{"heading":"Getting started with vector search","description":"Use raw vectors or embeddings generated outside of OpenSearch","link":"/vector-search/getting-started/"}]
tutorial_cards: [{"heading":"Generating embeddings automatically","description":"Automatically convert data to embeddings within OpenSearch","link":"/vector-search/getting-started/auto-generated-embeddings/"},{"heading":"Getting started with semantic and hybrid search","description":"Learn how to implement semantic and hybrid search","link":"/vector-search/tutorials/neural-search-tutorial/"}]
---
# Preparing vectors

In OpenSearch, you can either bring your own vectors or let OpenSearch generate them automatically from your data. Letting OpenSearch automatically generate your embeddings reduces data preprocessing effort at ingestion and search time.

### Option 1: Bring your own raw vectors or generated embeddings

You already have pre-computed embeddings or raw vectors from external tools or services.
  - **Ingestion**: Ingest pregenerated embeddings directly into OpenSearch.

      ![Pre-generated embeddings ingestion](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/vector-search/raw-vector-ingest.png)
  - **Search**: Perform vector search to find the vectors that are closest to a query vector.

      ![Pre-generated embeddings search](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/vector-search/raw-vector-search.png)

<details markdown="block">
  <summary>
    Steps
  </summary>
  {: .fs-5 .fw-700}

Working with embeddings generated outside of OpenSearch involves the following steps:

1. Generate embeddings
   Generate embeddings outside of OpenSearch using your favorite embedding utility.
2. [Create an OpenSearch index](../../creating-vector-index/index.md#storing-raw-vectors-or-embeddings-generated-outside-of-opensearch)
   Create an OpenSearch index to store your embeddings.
3. [Ingest embeddings](../../ingesting-data/index.md#raw-vector-ingestion)
   Ingest your embeddings into the index.
4. [Search embeddings](../../searching-data/index.md#searching-raw-vectors)
   Search your embeddings using vector search.

</details>

<div class="card-container">

- [Getting started with vector search](../index.md)
  Use raw vectors or embeddings generated outside of OpenSearch

</div>

### Option 2: Generate embeddings within OpenSearch

Use this option to let OpenSearch automatically generate vector embeddings from your data using a machine learning (ML) model.
  - **Ingestion**: You ingest plain data, and OpenSearch uses an ML model to generate embeddings dynamically.

      ![Auto-generated embeddings ingestion](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/vector-search/auto-vector-ingest.png)
  - **Search**: At query time, OpenSearch uses the same ML model to convert your input data to embeddings, and these embeddings are used for vector search.

      ![Auto-generated embeddings search](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/vector-search/auto-vector-search.png)

<details markdown="block">
  <summary>
    Steps
  </summary>
  {: .fs-5 .fw-700}

Working with text that is automatically converted to embeddings within OpenSearch involves the following steps:

1. [Configure an embedding model](../../../ml-commons-plugin/integrating-ml-models/index.md)
   Configure a machine learning model that will automatically generate embeddings from your text at ingestion time and query time.
2. [Create an OpenSearch index](../../creating-vector-index/index.md#converting-data-to-embeddings-during-ingestion)
   Create an OpenSearch index to store your text.
3. [Ingest text](../../ingesting-data/index.md#converting-data-to-embeddings-during-ingestion)
   Ingest your text into the index.
4. [Search text](../../searching-data/index.md#searching-auto-generated-embeddings)
   Search your text using vector search. Query text is automatically converted to vector embeddings and compared to document embeddings.

</details>

<div class="card-container">

- [Generating embeddings automatically](../auto-generated-embeddings/index.md)
  Automatically convert data to embeddings within OpenSearch

- [Getting started with semantic and hybrid search](../../../tutorials/vector-search/neural-search-tutorial/index.md)
  Learn how to implement semantic and hybrid search

</div>
