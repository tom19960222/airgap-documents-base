---
collection: "opensearch"
version: "2.19"
title: "Memory APIs"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/memory-apis/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/memory-apis/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/memory-apis/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/memory-apis/index/"
canonical_route: "/ml-commons-plugin/api/memory-apis/"
redirect_from: ["/ml-commons-plugin/api/memory-apis/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 28
parent: "ML Commons APIs"
---
# Memory APIs
**Introduced 2.12**
{: .label .label-purple }

Memory APIs provide operations needed to implement [conversational search](../../../vector-search/ai-search/conversational-search/index.md). A memory stores conversation history for the current conversation. A message represents one question/answer interaction between the user and a large language model. Messages are organized into memories.

ML Commons supports the following memory-level APIs:

- [Create or update memory](create-memory/index.md)
- [Get memory](get-memory/index.md)
- [Search memory](search-memory/index.md)
- [Delete memory](delete-memory/index.md)

ML Commons supports the following message-level APIs:

- [Create or update message](create-message/index.md)
- [Get message](get-message/index.md)
- [Search message](search-message/index.md)
- [Get message traces](get-message-traces/index.md)

When the Security plugin is enabled, all memories exist in a `private` security mode. Only the user who created a memory can interact with that memory and its messages.
{: .important}
