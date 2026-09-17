---
collection: "opensearch"
version: "2.19"
title: "Retrieving search pipelines"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/search-pipelines/retrieving-search-pipeline.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/search-pipelines/retrieving-search-pipeline.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/search-pipelines/retrieving-search-pipeline/"
canonical_url: "https://docs.opensearch.org/latest/search-plugins/search-pipelines/retrieving-search-pipeline/"
canonical_route: "/search-plugins/search-pipelines/retrieving-search-pipeline/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Search"
has_children: false
layout: "default"
nav_order: 25
parent: "Search pipelines"
---
# Retrieving search pipelines

To retrieve the details of an existing search pipeline, use the Search Pipeline API.

To view all search pipelines, use the following request:

```json
GET /_search/pipeline
```

The response contains the pipeline that you set up in the previous section:
<details open markdown="block">
  <summary>
    Response
  </summary>
  {: .text-delta}

```json
{
  "my_pipeline" : {
    "request_processors" : [
      {
        "filter_query" : {
          "tag" : "tag1",
          "description" : "This processor is going to restrict to publicly visible documents",
          "query" : {
            "term" : {
              "visibility" : "public"
            }
          }
        }
      }
    ]
  }
}
```
</details>

To view a particular pipeline, specify the pipeline name as a path parameter:

```json
GET /_search/pipeline/my_pipeline
```

You can also use wildcard patterns to view a subset of pipelines, for example:

```json
GET /_search/pipeline/my*
```
