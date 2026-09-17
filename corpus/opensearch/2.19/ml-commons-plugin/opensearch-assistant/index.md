---
collection: "opensearch"
version: "2.19"
title: "OpenSearch Assistant Toolkit"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/opensearch-assistant.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/opensearch-assistant.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/opensearch-assistant/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/opensearch-assistant/"
canonical_route: "/ml-commons-plugin/opensearch-assistant/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
has_toc: false
layout: "default"
nav_order: 28
---
# OpenSearch Assistant Toolkit
**Introduced 2.13**
{: .label .label-purple }

The OpenSearch Assistant Toolkit helps you create AI-powered assistants for OpenSearch Dashboards. The toolkit includes the following elements:

- [**Agents and tools**](../agents-tools/index.md): _Agents_ interface with a large language model (LLM) and execute high-level tasks, such as summarization or generating Piped Processing Language (PPL) queries from natural language. The agent's high-level tasks consist of low-level tasks called _tools_, which can be reused by multiple agents.
- [**Configuration automation**](../../automating-configurations/index.md): Uses templates to set up infrastructure for artificial intelligence and machine learning (AI/ML) applications. For example, you can automate configuring agents to be used for chat or generating PPL queries from natural language.
- [**OpenSearch Assistant for OpenSearch Dashboards**](https://docs.opensearch.org/latest/dashboards/dashboards-assistant/index/) <!-- unresolved-cross-corpus-link: collection=opensearch-dashboards route=/dashboards/dashboards-assistant/ -->: This is the OpenSearch Dashboards UI for the AI-powered assistant. The assistant's workflow is configured with various agents and tools.

## Enabling OpenSearch Assistant

To enable OpenSearch Assistant, perform the following steps:

- Enable the agent framework and retrieval-augmented generation (RAG) by configuring the following settings:
    ```yaml
    plugins.ml_commons.agent_framework_enabled: true
    plugins.ml_commons.rag_pipeline_feature_enabled: true
    ```

- Enable the assistant by configuring the following settings:
    ```yaml
    assistant.chat.enabled: true
    observability.query_assist.enabled: true
    ```

## Next steps

- For more information about the OpenSearch Assistant UI, see [OpenSearch Assistant for OpenSearch Dashboards](https://docs.opensearch.org/latest/dashboards/dashboards-assistant/index/) <!-- unresolved-cross-corpus-link: collection=opensearch-dashboards route=/dashboards/dashboards-assistant/ -->
