---
collection: "opensearch"
version: "2.19"
title: "Managing OpenSearch Dashboards plugins"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_install-and-configure/install-dashboards/plugins.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_install-and-configure/install-dashboards/plugins.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/install-and-configure/install-dashboards/plugins/"
canonical_url: "https://docs.opensearch.org/latest/install-and-configure/install-dashboards/plugins/"
canonical_route: "/install-and-configure/install-dashboards/plugins/"
redirect_from: ["/dashboards/install/plugins/","/install-and-configure/install-dashboards/plugins/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 100
---
# Managing OpenSearch Dashboards plugins

OpenSearch Dashboards provides a command line tool called `opensearch-dashboards-plugin` for managing plugins. This tool allows you to:

- List installed plugins.
- Install plugins.
- Remove an installed plugin.

## Plugin compatibility

Major, minor, and patch plugin versions must match OpenSearch major, minor, and patch versions in order to be compatible. For example, plugins versions 2.3.0.x work only with OpenSearch 2.3.0.
{: .warning}

## Prerequisites

- A compatible OpenSearch cluster
- The corresponding OpenSearch plugins [installed on that cluster](../../plugins/index.md)
- The corresponding version of [OpenSearch Dashboards](https://docs.opensearch.org/latest/) <!-- unresolved-jekyll-link: route=/ --> (for example, OpenSearch Dashboards 2.3.0 works with OpenSearch 2.3.0)

## Available plugins

The following table lists available OpenSearch Dashboards plugins.

| Plugin Name | Repository | Earliest Available Version |
| :--- | :--- | :--- |
| Alerting Dashboards | [alerting-dashboards-plugin](https://github.com/opensearch-project/alerting-dashboards-plugin) | 1.0.0 |
| Anomaly Detection Dashboards | [anomaly-detection-dashboards-plugin](https://github.com/opensearch-project/anomaly-detection-dashboards-plugin) | 1.0.0 |
| Custom Import Maps Dashboards | [dashboards-maps](https://github.com/opensearch-project/dashboards-maps) | 2.2.0 |
| Search Relevance Dashboards | [dashboards-search-relevance](https://github.com/opensearch-project/dashboards-search-relevance) | 2.4.0 |
| Gantt Chart Dashboards | [gantt-chart](https://github.com/opensearch-project/dashboards-visualizations) | 1.0.0 |
| Index Management Dashboards | [index-management-dashboards-plugin](https://github.com/opensearch-project/index-management-dashboards-plugin) | 1.0.0 |
| Notebooks Dashboards | [dashboards-notebooks](https://github.com/opensearch-project/dashboards-notebooks) | 1.0.0 |
| Notifications Dashboards | [dashboards-notifications](https://github.com/opensearch-project/dashboards-notifications) | 2.0.0 |
| Observability Dashboards | [dashboards-observability](https://github.com/opensearch-project/dashboards-observability) | 2.0.0 |
| Query Workbench Dashboards | [query-workbench](https://github.com/opensearch-project/dashboards-query-workbench) | 1.0.0 |
| Reports Dashboards | [dashboards-reporting](https://github.com/opensearch-project/dashboards-reporting) | 1.0.0 |
| Security Analytics Dashboards | [security-analytics-dashboards-plugin](https://github.com/opensearch-project/security-analytics-dashboards-plugin)| 2.4.0 |
| Security Dashboards | [security-dashboards-plugin](https://github.com/opensearch-project/security-dashboards-plugin) | 1.0.0 |

## Install

Navigate to the OpenSearch Dashboards home directory (for example, `/usr/share/opensearch-dashboards`) and run the install command for each plugin.

## Viewing a list of installed plugins

To view the list of installed plugins from the command line, use the following command:

```bash
sudo bin/opensearch-dashboards-plugin list
```

## Remove plugins

To remove a plugin:

```bash
sudo bin/opensearch-dashboards-plugin remove <plugin-name>
```

Then remove all associated entries from `opensearch_dashboards.yml`.

For certain plugins, you must also remove the "optimize" bundle. This is a sample command for the Anomaly Detection plugin:

```bash
sudo rm /usr/share/opensearch-dashboards/optimize/bundles/opensearch-anomaly-detection-opensearch-dashboards.*
```

Then restart OpenSearch Dashboards. After you remove any plugin, OpenSearch Dashboards performs an optimize operation the next time you start it. This operation takes several minutes even on fast machines, so be patient.

## Updating plugins

OpenSearch Dashboards doesn’t update plugins. Instead, you have to remove the old version and its optimized bundle, reinstall them, and restart OpenSearch Dashboards:

1. Remove the old version:

   ```bash
   sudo bin/opensearch-dashboards-plugin remove <plugin-name>
   ```

1. Remove the optimized bundle:

   ```bash
   sudo rm /usr/share/opensearch-dashboards/optimize/bundles/<bundle-name>
   ```

1. Reinstall the new version:

   ```bash
   sudo bin/opensearch-dashboards-plugin install <plugin-name>
   ```

1. Restart OpenSearch Dashboards.

For example, to remove and reinstall the Anomaly Detection plugin:

```bash
sudo bin/opensearch-dashboards-plugin remove anomalyDetectionDashboards
sudo rm /usr/share/opensearch-dashboards/optimize/bundles/opensearch-anomaly-detection-opensearch-dashboards.*
sudo bin/opensearch-dashboards-plugin install <AD OpenSearch Dashboards plugin artifact URL>
```
