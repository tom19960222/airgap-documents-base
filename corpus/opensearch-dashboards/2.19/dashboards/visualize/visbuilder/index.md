---
collection: "opensearch-dashboards"
version: "2.19"
title: "VisBuilder"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_dashboards/visualize/visbuilder.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_dashboards/visualize/visbuilder.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/dashboards/visualize/visbuilder/"
canonical_url: "https://docs.opensearch.org/latest/dashboards/visualize/visualize-app/visbuilder/"
canonical_route: "/dashboards/visualize/visualize-app/visbuilder/"
redirect_from: ["/dashboards/drag-drop-wizard/","/dashboards/visualize/visualize-app/visbuilder/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.1"
chart_version: ""
layout: "default"
nav_order: 100
parent: "Building data visualizations"
---
# VisBuilder

You can use the VisBuilder visualization type in OpenSearch Dashboards to create data visualizations by using a drag-and-drop gesture. With VisBuilder you have:

* An immediate view of your data without the need to preselect the visualization output.
* The flexibility to change visualization types and index patterns quickly.
* The ability to easily navigate between multiple screens.

<img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/dashboards/vis-builder-2.png" alt="VisBuilder new visualization start page">

## Try VisBuilder in the OpenSearch Dashboards playground

You can try VisBuilder without installing OpenSearch locally by using [OpenSearch Dashboards Playground](https://playground.opensearch.org/app/vis-builder#/). VisBuilder is enabled by default.

## Try VisBuilder locally

Follow these steps to create a new visualization using VisBuilder in your environment:

1. Open Dashboards:
    - If you're not running the Security plugin, go to http://localhost:5601.
    - If you're running the Security plugin, go to https://localhost:5601 and log in with your username and password (default is `admin/admin`).

1. From the top menu, select **Visualize > Create visualization > VisBuilder**.

   <img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/dashboards/vis-builder-1.png" alt="Select the VisBuilder visualization type" width="550">

1. Drag and drop field names from the left column into the **Configuration** panel to generate a visualization.

Here’s an example visualization. Your visualization will look different depending on your data and the fields you select.

<img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/dashboards/drag-drop-generated-viz.png" alt="Visualization generated using sample data">
