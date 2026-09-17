---
collection: "opensearch"
version: "2.19"
title: "Settings"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_im-plugin/index-rollups/settings.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_im-plugin/index-rollups/settings.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/im-plugin/index-rollups/settings/"
canonical_url: "https://docs.opensearch.org/latest/im-plugin/index-rollups/settings/"
canonical_route: "/im-plugin/index-rollups/settings/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 30
parent: "Index rollups"
---
# Index rollup settings

We don't recommend changing these settings; the defaults should work well for most use cases.

All settings are available using the OpenSearch `_cluster/settings` operation. None require a restart, and all can be marked `persistent` or `transient`. To learn more about static and dynamic settings, see [Configuring OpenSearch](../../../install-and-configure/configuring-opensearch/index.md).

Setting | Default | Description
:--- | :--- | :---
`plugins.rollup.search.backoff_millis` | 1000 milliseconds | The backoff time between retries for failed rollup jobs.
`plugins.rollup.search.backoff_count` | 5 | How many retries the plugin should attempt for failed rollup jobs.
`plugins.rollup.search.search_all_jobs` | false | Whether OpenSearch should return all jobs that match all specified search terms. If disabled, OpenSearch returns just one, as opposed to all, of the jobs that matches the search terms.
`plugins.rollup.dashboards.enabled` | true | Whether rollups are enabled in OpenSearch Dashboards.
`plugins.rollup.enabled` | true | Whether the rollup plugin is enabled.
`plugins.ingest.backoff_millis` | 1000 milliseconds | The backoff time between data ingestions for rollup jobs.
`plugins.ingest.backoff_count` | 5 | How many retries the plugin should attempt for failed ingestions.
