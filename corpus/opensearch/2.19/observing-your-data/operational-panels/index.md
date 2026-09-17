---
collection: "opensearch"
version: "2.19"
title: "Operational panels"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_observing-your-data/operational-panels.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_observing-your-data/operational-panels.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/observing-your-data/operational-panels/"
canonical_url: "https://docs.opensearch.org/latest/observing-your-data/operational-panels/"
canonical_route: "/observing-your-data/operational-panels/"
redirect_from: ["/observing-your-data/operational-panels/","/observability-plugin/operational-panels/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 60
---
# Operational panels

Operational panels in OpenSearch Dashboards are collections of visualizations generated using [Piped Processing Language](../../search-plugins/sql/ppl/index.md) (PPL) queries.

## Get started with operational panels

If you want to start using operational panels without adding any data, expand the **Action** menu, choose **Add samples**, and Dashboards adds a set of operational panels with saved visualizations for you to explore.

## Create an operational panel

To create an operational panel and add visualizations:

1. From the **Add Visualization** dropdown menu, choose **Select Existing Visualization** or **Create New Visualization**, which takes you to the [event analytics](../event-analytics/index.md) explorer, where you can use PPL to create visualizations.
1. If you're adding already existing visualizations, choose a visualization from the dropdown menu.
1. Choose **Add**.

![Sample operational panel](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/operational-panel.png)

To search for a particular visualization in your operation panels, use PPL queries to search for data you've already added to your panel.
