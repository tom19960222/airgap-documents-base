---
collection: "opensearch"
version: "2.19"
title: "Document APIs"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/document-apis/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/document-apis/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/document-apis/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/document-apis/index/"
canonical_route: "/api-reference/document-apis/"
redirect_from: ["/opensearch/rest-api/document-apis/index/","/api-reference/document-apis/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
layout: "default"
nav_order: 25
---
# Document APIs
**Introduced 1.0**
{: .label .label-purple }

The document APIs allow you to handle documents relative to your index, such as adding, updating, and deleting documents.

Document APIs are separated into two categories: single document operations and multi-document operations. Multi-document operations offer performance advantages over submitting many individual requests, so whenever practical, we recommend that you use multi-document operations.

## Single document operations

- Index
- Get
- Delete
- Update

## Multi-document operations

- Bulk
- Multi get
- Delete by query
- Update by query
- Reindex
