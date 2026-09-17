---
collection: "opensearch"
version: "2.19"
title: "Workflow settings"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_automating-configurations/workflow-settings.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_automating-configurations/workflow-settings.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/automating-configurations/workflow-settings/"
canonical_url: "https://docs.opensearch.org/latest/automating-configurations/workflow-settings/"
canonical_route: "/automating-configurations/workflow-settings/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 30
---
# Workflow settings

The following keys represent configurable workflow settings.

|Setting	|Data type	|Default value	|Description	|
|:---	|:---	|:---	|:---	|
|`plugins.flow_framework.enabled`	|Boolean	|`false`	|Whether the Flow Framework API is enabled.	|
|`plugins.flow_framework.max_workflows`	|Integer	|`1000`	| The maximum number of workflows that you can create. When the limit is above 1,000, the number of existing workflows is defined as a lower bound for performance reasons, so the actual maximum may slightly exceed this value.	|
|`plugins.flow_framework.max_workflow_steps`	|Integer	|`50`	|The maximum number of steps a workflow can have.	|
|`plugins.flow_framework.request_timeout`	|Time units	|`10s`	|The default timeout for REST requests, which applies to internal search queries.	|
|`plugins.flow_framework.task_request_retry_duration`	|Time units	|`5s`	| When steps correspond to an API that produces a `task_id`, OpenSearch will retry them at this interval until completion.	|
