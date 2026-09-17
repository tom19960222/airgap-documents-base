---
collection: "opensearch"
version: "2.19"
title: "Delete pipeline"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ingest-pipelines/delete-ingest.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ingest-pipelines/delete-ingest.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ingest-pipelines/delete-ingest/"
canonical_url: "https://docs.opensearch.org/latest/ingest-pipelines/delete-ingest/"
canonical_route: "/ingest-pipelines/delete-ingest/"
redirect_from: ["/opensearch/rest-api/ingest-apis/delete-ingest/","/api-reference/ingest-apis/delete-ingest/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 13
---
# Delete pipeline
**Introduced 1.0**
{: .label .label-purple }

Use the following request to delete a pipeline.

To delete a specific pipeline, pass the pipeline ID as a parameter:

```json
DELETE /_ingest/pipeline/<pipeline-id>
```

To delete all pipelines in a cluster, use the wildcard character (`*`):

```json
DELETE /_ingest/pipeline/*
```
