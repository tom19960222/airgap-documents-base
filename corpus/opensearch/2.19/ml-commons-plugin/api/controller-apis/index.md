---
collection: "opensearch"
version: "2.19"
title: "Controller APIs"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/controller-apis/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/controller-apis/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/controller-apis/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/controller-apis/index/"
canonical_route: "/ml-commons-plugin/api/controller-apis/"
redirect_from: ["/ml-commons-plugin/api/controller-apis/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 29
parent: "ML Commons APIs"
---
# Controller APIs
**Introduced 2.12**
{: .label .label-purple }

You can configure a rate limit for a specific user or users of a model by calling the Controller APIs.

ML Commons supports the following controller-level APIs:

- [Create or update controller](create-controller/index.md)
- [Get controller](get-controller/index.md)
- [Delete controller](delete-controller/index.md)

## Required permissions

To call the Controller APIs, you must have `cluster:admin/opensearch/ml/controllers/` permissions. Links to more information about each Controller API are provided in the preceding section.
