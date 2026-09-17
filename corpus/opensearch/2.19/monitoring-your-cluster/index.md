---
collection: "opensearch"
version: "2.19"
title: "Monitoring your cluster"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_monitoring-your-cluster/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_monitoring-your-cluster/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/monitoring-your-cluster/"
canonical_url: "https://docs.opensearch.org/latest/monitoring-your-cluster/"
canonical_route: "/monitoring-your-cluster/"
redirect_from: ["/monitoring-your-cluster/index/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
has_toc: false
layout: "default"
nav_exclude: true
nav_order: 1
---
# Monitoring your cluster

OpenSearch provides several ways for you to monitor your cluster health and performance and automate common tasks:

- The OpenSearch [logs](../install-and-configure/configuring-opensearch/logs/index.md) include valuable information for monitoring cluster operations and troubleshooting issues.

- [Performance analyzer](pa/index.md) is an agent and REST API that allows you to query numerous performance metrics for your cluster, including aggregations of those metrics.

- OpenSearch [Job Scheduler](job-scheduler/index.md) plugin provides a framework that you can use to build schedules for common cluster management tasks.
- The OpenSearch [Metrics Framework](metrics/getting-started/index.md) plugin provides a framework that you can use to export the telemetry metrics to the store of your choice.
