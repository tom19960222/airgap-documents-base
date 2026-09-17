---
collection: "opensearch"
version: "2.19"
title: "Get pipeline"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ingest-pipelines/get-ingest.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ingest-pipelines/get-ingest.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ingest-pipelines/get-ingest/"
canonical_url: "https://docs.opensearch.org/latest/ingest-pipelines/get-ingest/"
canonical_route: "/ingest-pipelines/get-ingest/"
redirect_from: ["/opensearch/rest-api/ingest-apis/get-ingest/","/api-reference/ingest-apis/get-ingest/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 12
---
# Get pipeline
**Introduced 1.0**
{: .label .label-purple }

Use the get ingest pipeline API operation to retrieve all the information about the pipeline.

## Retrieving information about all pipelines

The following example request returns information about all ingest pipelines:

```json
GET _ingest/pipeline/
```

## Retrieving information about a specific pipeline

The following example request returns information about a specific pipeline, which for this example is `my-pipeline`:

```json
GET _ingest/pipeline/my-pipeline
```

The response contains the pipeline information:

```json
{
  "my-pipeline": {
    "description": "This pipeline processes student data",
    "processors": [
      {
        "set": {
          "description": "Sets the graduation year to 2023",
          "field": "grad_year",
          "value": 2023
        }
      },
      {
        "set": {
          "description": "Sets graduated to true",
          "field": "graduated",
          "value": true
        }
      },
      {
        "uppercase": {
          "field": "name"
        }
      }
    ]
  }
}
```
