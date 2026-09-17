---
collection: "opensearch"
version: "2.19"
title: "Search processors"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/search-pipelines/search-processors.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/search-pipelines/search-processors.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/search-pipelines/search-processors/"
canonical_url: "https://docs.opensearch.org/latest/search-plugins/search-pipelines/search-processors/"
canonical_route: "/search-plugins/search-pipelines/search-processors/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Search"
has_children: true
layout: "default"
nav_order: 40
parent: "Search pipelines"
---
# Search processors

Search processors can be of the following types:

- [Search request processors](#search-request-processors)
- [Search response processors](#search-response-processors)
- [Search phase results processors](#search-phase-results-processors)

## Search request processors

A search request processor intercepts a search request (the query and the metadata passed in the request), performs an operation with or on the search request, and submits the search request to the index.

The following table lists all supported search request processors.

Processor | Description | Earliest available version
:--- | :--- | :---
[`filter_query`](../filter-query-processor/index.md) | Adds a filtering query that is used to filter requests. | 2.8
[`ml_inference`](../ml-inference-search-request/index.md) | Invokes registered machine learning (ML) models in order to rewrite queries. | 2.16
[`neural_query_enricher`](../neural-query-enricher/index.md) | Sets a default model for neural search and neural sparse search at the index or field level. | 2.11 (neural), 2.13 (neural sparse)
[`neural_sparse_two_phase_processor`](../neural-sparse-query-two-phase-processor/index.md) | Accelerates the neural sparse query. | 2.15
[`oversample`](../oversample-processor/index.md) | Increases the search request `size` parameter, storing the original value in the pipeline state.  | 2.12
[`script`](../script-processor/index.md) | Adds a script that is run on newly indexed documents. | 2.8

## Search response processors

A search response processor intercepts a search response and search request (the query, results, and metadata passed in the request), performs an operation with or on the search response, and returns the search response.

The following table lists all supported search response processors.

Processor | Description | Earliest available version
:--- | :--- | :---
[`collapse`](../collapse-processor/index.md)| Deduplicates search hits based on a field value, similarly to `collapse` in a search request. | 2.12
[`hybrid_score_explanation`](../explanation-processor/index.md)| Adds detailed scoring information to search results when the `explain` parameter is enabled, providing information about score normalization, combination techniques, and individual score calculations in hybrid queries.  | 2.19
[`ml_inference`](../ml-inference-search-response/index.md) | Invokes registered machine learning (ML) models in order to incorporate model output as additional search response fields. | 2.16
[`personalize_search_ranking`](../personalize-search-ranking/index.md) | Uses [Amazon Personalize](https://aws.amazon.com/personalize/) to rerank search results (requires setting up the Amazon Personalize service). | 2.9
[`rename_field`](../rename-field-processor/index.md)| Renames an existing field. | 2.8
[`rerank`](../rerank-processor/index.md)| Reranks search results using a cross-encoder model. | 2.12
[`retrieval_augmented_generation`](../rag-processor/index.md) | Used for retrieval-augmented generation (RAG) in [conversational search](../../../vector-search/ai-search/conversational-search/index.md). | 2.10 (generally available in 2.12)
[`sort`](../sort-processor/index.md)| Sorts an array of items in either ascending or descending order. | 2.16
[`split`](../split-processor/index.md)| Splits a string field into an array of substrings based on a specified delimiter. | 2.17
[`truncate_hits`](../truncate-hits-processor/index.md)| Discards search hits after a specified target count is reached. Can undo the effect of the `oversample` request processor.  | 2.12

## Search phase results processors

A search phase results processor runs between search phases at the coordinating node level. It intercepts the results retrieved from one search phase and transforms them before passing them to the next search phase.

The following table lists all supported search phase results processors.

Processor | Description | Earliest available version
:--- | :--- | :---
[`normalization-processor`](../normalization-processor/index.md) | Intercepts the query phase results and normalizes and combines the document scores before passing the documents to the fetch phase. | 2.10

## Viewing available processor types

You can use the Nodes Search Pipelines API to view the available processor types:

```json
GET /_nodes/search_pipelines
```

The response contains the `search_pipelines` object that lists the available request and response processors:

<details open markdown="block">
  <summary>
    Response
  </summary>
  {: .text-delta}

```json
{
  "_nodes" : {
    "total" : 1,
    "successful" : 1,
    "failed" : 0
  },
  "cluster_name" : "runTask",
  "nodes" : {
    "36FHvCwHT6Srbm2ZniEPhA" : {
      "name" : "runTask-0",
      "transport_address" : "127.0.0.1:9300",
      "host" : "127.0.0.1",
      "ip" : "127.0.0.1",
      "version" : "3.0.0",
      "build_type" : "tar",
      "build_hash" : "unknown",
      "roles" : [
        "cluster_manager",
        "data",
        "ingest",
        "remote_cluster_client"
      ],
      "attributes" : {
        "testattr" : "test",
        "shard_indexing_pressure_enabled" : "true"
      },
      "search_pipelines" : {
        "request_processors" : [
          {
            "type" : "filter_query"
          },
          {
            "type" : "script"
          }
        ],
        "response_processors" : [
          {
            "type" : "rename_field"
          }
        ]
      }
    }
  }
}
```
</details>

In addition to the processors provided by OpenSearch, additional processors may be provided by plugins.
{: .note}

## Selectively enabling processors

Processors defined by the [search-pipeline-common module](https://github.com/opensearch-project/OpenSearch/blob/2.x/modules/search-pipeline-common/src/main/java/org/opensearch/search/pipeline/common/SearchPipelineCommonModulePlugin.java) are selectively enabled through the following cluster settings: `search.pipeline.common.request.processors.allowed`, `search.pipeline.common.response.processors.allowed`, or `search.pipeline.common.search.phase.results.processors.allowed`. If unspecified, then all processors are enabled. An empty list disables all processors. Removing enabled processors causes pipelines using them to fail after a node restart.
