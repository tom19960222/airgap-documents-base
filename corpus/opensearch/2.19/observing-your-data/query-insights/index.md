---
collection: "opensearch"
version: "2.19"
title: "Query insights"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_observing-your-data/query-insights/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_observing-your-data/query-insights/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/observing-your-data/query-insights/"
canonical_url: "https://docs.opensearch.org/latest/observing-your-data/query-insights/index/"
canonical_route: "/observing-your-data/query-insights/"
redirect_from: ["/query-insights/","/observing-your-data/query-insights/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 40
---
# Query insights
**Introduced 2.12**
{: .label .label-purple }

To monitor and analyze the search queries within your OpenSearch cluster, you can obtain query insights. With minimal performance impact, query insights features aim to provide comprehensive insights into search query execution, enabling you to better understand search query characteristics, patterns, and system behavior during query execution stages. Query insights facilitate enhanced detection, diagnosis, and prevention of query performance issues, ultimately improving query processing performance, user experience, and overall system resilience.

Typical use cases for query insights features include the following:

- Identifying top queries by latency within specific time frames
- Debugging slow search queries and latency spikes

Query insights features are supported by the Query Insights plugin. At a high level, query insights features comprise the following components:

* _Collectors_: Gather performance-related data points at various stages of search query execution.
* _Processors_: Perform lightweight aggregation and processing on data collected by the collectors.
* _Exporters_: Export the data into different sinks.

## Installing the Query Insights plugin

You need to install the `query-insights` plugin to enable query insights features. To install the plugin, run the following command:

```bash
bin/opensearch-plugin install query-insights
```
For information about installing plugins, see [Installing plugins](../../install-and-configure/plugins/index.md).

## Query Insights settings

You can obtain the following information using Query Insights:

- [Top n queries](top-n-queries/index.md)
- [Grouping top N queries](grouping-top-n-queries/index.md)
- [Query metrics](query-metrics/index.md)

## Query Insights plugin health

For information about monitoring the health of the Query Insights plugin, see [Query Insights plugin health](health/index.md).
