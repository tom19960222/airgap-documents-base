---
collection: "opensearch"
version: "2.19"
title: "Filter query"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/search-pipelines/filter-query-processor.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/search-pipelines/filter-query-processor.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/search-pipelines/filter-query-processor/"
canonical_url: "https://docs.opensearch.org/latest/search-plugins/search-pipelines/filter-query-processor/"
canonical_route: "/search-plugins/search-pipelines/filter-query-processor/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Search pipelines"
has_children: false
layout: "default"
nav_order: 20
parent: "Search processors"
---
# Filter query processor
Introduced 2.8
{: .label .label-purple }

The `filter_query` search request processor intercepts a search request and applies an additional query to the request, filtering the results. This is useful when you don't want to rewrite existing queries in your application but need additional filtering of the results.

## Request body fields

The following table lists all available request fields.

Field | Data type | Description
:--- | :--- | :---
`query` | Object | A query in query domain-specific language (DSL). For a list of OpenSearch query types, see [Query DSL](../../../query-dsl/index.md). Required.
`tag` | String | The processor's identifier. Optional.
`description` | String | A description of the processor. Optional.
`ignore_failure` | Boolean | If `true`, OpenSearch [ignores any failure](../creating-search-pipeline/index.md#ignoring-processor-failures) of this processor and continues to run the remaining processors in the search pipeline. Optional. Default is `false`.

## Example

The following example demonstrates using a search pipeline with a `filter_query` processor.

### Setup

Create an index named `my_index` and index two documents, one public and one private:

```json
POST /my_index/_doc/1
{
  "message": "This is a public message",
  "visibility":"public"
}
```

```json
POST /my_index/_doc/2
{
  "message": "This is a private message",
  "visibility": "private"
}
```

### Creating a search pipeline

The following request creates a search pipeline called `my_pipeline` with a `filter_query` request processor that uses a term query to return only public messages:

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
  ]
}
```

### Using a search pipeline

Search for documents in `my_index` without a search pipeline:

```json
GET /my_index/_search
```

The response contains both documents:

<details open markdown="block">
  <summary>
    Response
  </summary>
  {: .text-delta}
```json
{
  "took" : 47,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "my_index",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "message" : "This is a public message",
          "visibility" : "public"
        }
      },
      {
        "_index" : "my_index",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "message" : "This is a private message",
          "visibility" : "private"
        }
      }
    ]
  }
}
```
</details>

To search with a pipeline, specify the pipeline name in the `search_pipeline` query parameter:

```json
GET /my_index/_search?search_pipeline=my_pipeline
```

The response contains only the document with `public` visibility:

<details open markdown="block">
  <summary>
    Response
  </summary>
  {: .text-delta}
```json
{
  "took" : 19,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 0.0,
    "hits" : [
      {
        "_index" : "my_index",
        "_id" : "1",
        "_score" : 0.0,
        "_source" : {
          "message" : "This is a public message",
          "visibility" : "public"
        }
      }
    ]
  }
}
```
</details>
