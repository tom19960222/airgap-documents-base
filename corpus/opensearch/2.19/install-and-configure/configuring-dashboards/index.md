---
collection: "opensearch"
version: "2.19"
title: "Configuring OpenSearch Dashboards"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_install-and-configure/configuring-dashboards.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_install-and-configure/configuring-dashboards.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/install-and-configure/configuring-dashboards/"
canonical_url: "https://docs.opensearch.org/latest/install-and-configure/configuring-dashboards/"
canonical_route: "/install-and-configure/configuring-dashboards/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 15
---
# Configuring OpenSearch Dashboards

OpenSearch Dashboards uses the `opensearch_dashboards.yml` configuration file to read settings when you spin up a cluster. You can find `opensearch_dashboards.yml` in `/usr/share/opensearch-dashboards/config/opensearch_dashboards.yml` (Docker) or `/etc/opensearch-dashboards/opensearch_dashboards.yml` (most Linux distributions) on each node.

For information about OpenSearch Dashboards settings, see the sample [`opensearch_dashboards.yml`](https://github.com/opensearch-project/OpenSearch-Dashboards/blob/main/config/opensearch_dashboards.yml) file.
