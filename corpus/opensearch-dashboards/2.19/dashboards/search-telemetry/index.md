---
collection: "opensearch-dashboards"
version: "2.19"
title: "Search telemetry"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_dashboards/search-telemetry.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_dashboards/search-telemetry.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/dashboards/search-telemetry/"
canonical_url: "https://docs.opensearch.org/latest/dashboards/search-telemetry/"
canonical_route: "/dashboards/search-telemetry/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.1"
chart_version: ""
layout: "default"
nav_order: 140
---
# Search telemetry

You can use search telemetry to analyze search request performance by success or failure in OpenSearch Dashboards. OpenSearch stores telemetry data in the `.kibana_1` index.

Because there are thousands of concurrent search requests from OpenSearch Dashboards, the heavy traffic can cause significant load in an OpenSearch cluster.

OpenSearch clusters perform better with search telemetry turned off.
{: .tip }

## Turning on search telemetry

Search usage telemetry is turned off by default. To turn it on, you need to set `data.search.usageTelemetry.enabled` to `true` in the `opensearch_dashboards.yml` file.

You can find the [OpenSearch Dashboards YAML file](https://github.com/opensearch-project/OpenSearch-Dashboards/blob/main/config/opensearch_dashboards.yml) in the opensearch-project repository on GitHub.

Turning on telemetry in the `opensearch_dashboards.yml` file overrides the default search telemetry setting of `false` in the [Data plugin configuration file](https://github.com/opensearch-project/OpenSearch-Dashboards/blob/main/src/plugins/data/config.ts).
{: .note }

### Turning search telemetry on or off

The following table shows the `data.search.usageTelemetry.enabled` values you can set in `opensearch_dashboards.yml` to turn search telemetry on or off.

OpenSearch Dashboards YAML value  | Search telemetry status: on or off
:--- |  :---
 `true`  | On
 `false` | Off
 `none`  | Off

#### Sample opensearch_dashboards.yml with telemetry enabled

 This OpenSearch Dashboards YAML file excerpt shows the telemetry setting set to `true` to turn on search telemetry:

 ```json
# Set the value of this setting to false to suppress
# search usage telemetry to reduce the load of the OpenSearch cluster.
 data.search.usageTelemetry.enabled: true
```
