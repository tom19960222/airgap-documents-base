---
collection: "opensearch"
version: "2.19"
title: "Search pipelines"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/search-pipelines/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/search-pipelines/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/search-pipelines/"
canonical_url: "https://docs.opensearch.org/latest/search-plugins/search-pipelines/index/"
canonical_route: "/search-plugins/search-pipelines/"
redirect_from: ["/search-plugins/search-pipelines/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 100
---
# Search pipelines

You can use _search pipelines_ to build new or reuse existing result rerankers, query rewriters, and other components that operate on queries or results. Search pipelines make it easier for you to process search queries and search results within OpenSearch. Moving some of your application functionality into an OpenSearch search pipeline reduces the overall complexity of your application. As part of a search pipeline, you specify a list of processors that perform modular tasks. You can then easily add or reorder these processors to customize search results for your application.

## Terminology

The following is a list of search pipeline terminology:

* [_Search request processor_](search-processors/index.md#search-request-processors): A component that intercepts a search request (the query and the metadata passed in the request), performs an operation with or on the search request, and returns the search request.
* [_Search response processor_](search-processors/index.md#search-response-processors): A component that intercepts a search response and search request (the query, results, and metadata passed in the request), performs an operation with or on the search response, and returns the search response.
* [_Search phase results processor_](search-processors/index.md#search-phase-results-processors): A component that runs between search phases at the coordinating node level. A search phase results processor intercepts the results retrieved from one search phase and transforms them before passing them to the next search phase.
* [_Processor_](search-processors/index.md): Either a search request processor or a search response processor.
* _Search pipeline_: An ordered list of processors that is integrated into OpenSearch. The pipeline intercepts a query, performs processing on the query, sends it to OpenSearch, intercepts the results, performs processing on the results, and returns them to the calling application, as shown in the following diagram.

![Search processor diagram](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/search-pipelines.png)

Both request and response processing for the pipeline are performed on the coordinator node, so there is no shard-level processing.
{: .note}

## Processors

To learn more about available search processors, see [Search processors](search-processors/index.md).

## Example

To create a search pipeline, send a request to the search pipeline endpoint specifying an ordered list of processors, which will be applied sequentially:

```json
PUT /_search/pipeline/my_pipeline
{
  "request_processors": [
    {
      "filter_query" : {
        "tag" : "tag1",
        "description" : "This processor is going to restrict to publicly visible documents",
        "query" : {
          "term": {
            "visibility": "public"
          }
        }
      }
    }
  ],
  "response_processors": [
    {
      "rename_field": {
        "field": "message",
        "target_field": "notification"
      }
    }
  ]
}
```

For more information about creating and updating a search pipeline, see [Creating a search pipeline](creating-search-pipeline/index.md).

To use a pipeline with a query, specify the pipeline name in the `search_pipeline` query parameter:

```json
GET /my_index/_search?search_pipeline=my_pipeline
```

Alternatively, you can use a temporary pipeline with a request or set a default pipeline for an index. To learn more, see [Using a search pipeline](using-search-pipeline/index.md).

To learn about retrieving details for an existing search pipeline, see [Retrieving search pipelines](retrieving-search-pipeline/index.md).

## Search pipeline metrics

For information about retrieving search pipeline statistics, see [Search pipeline metrics](search-pipeline-metrics/index.md).
