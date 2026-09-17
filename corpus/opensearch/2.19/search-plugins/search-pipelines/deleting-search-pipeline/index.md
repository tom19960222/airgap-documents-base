---
collection: "opensearch"
version: "2.19"
title: "Deleting search pipelines"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/search-pipelines/deleting-search-pipeline.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/search-pipelines/deleting-search-pipeline.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/search-pipelines/deleting-search-pipeline/"
canonical_url: "https://docs.opensearch.org/latest/search-plugins/search-pipelines/deleting-search-pipeline/"
canonical_route: "/search-plugins/search-pipelines/deleting-search-pipeline/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Search"
has_children: false
layout: "default"
nav_order: 30
parent: "Search pipelines"
---
# Deleting search pipelines

Use the following request to delete a pipeline.

To delete a specific search pipeline, pass the pipeline ID as a parameter:

```json
DELETE /_search/pipeline/<pipeline-id>
```

To delete all search pipelines in a cluster, use the wildcard character (`*`):

```json
DELETE /_search/pipeline/*
```
