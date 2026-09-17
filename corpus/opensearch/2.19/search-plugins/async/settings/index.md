---
collection: "opensearch"
version: "2.19"
title: "Settings"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/async/settings.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/async/settings.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/async/settings/"
canonical_url: "https://docs.opensearch.org/latest/search-plugins/async/settings/"
canonical_route: "/search-plugins/async/settings/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Improving search performance"
layout: "default"
nav_order: 4
parent: "Asynchronous search"
---
# Asynchronous Search settings

The Asynchronous Search plugin adds several settings to the standard OpenSearch cluster settings. They are dynamic, so you can change the default behavior of the plugin without restarting your cluster. To learn more about static and dynamic settings, see [Configuring OpenSearch](../../../install-and-configure/configuring-opensearch/index.md).

You can mark the settings as `persistent` or `transient`.

For example, to update the retention period of the result index:

```json
PUT _cluster/settings
{
  "transient": {
    "plugins.asynchronous_search.max_wait_for_completion_timeout": "5m"
  }
}
```

Setting | Default | Description
:--- | :--- | :---
`plugins.asynchronous_search.max_search_running_time` | 12 hours | The maximum running time for the search beyond which the search is terminated.
`plugins.asynchronous_search.node_concurrent_running_searches` | 20 | The concurrent searches running per coordinator node.
`plugins.asynchronous_search.max_keep_alive` | 5 days | The maximum amount of time that search results can be stored in the cluster.
`plugins.asynchronous_search.max_wait_for_completion_timeout` | 1 minute | The maximum value for the `wait_for_completion_timeout` parameter.
`plugins.asynchronous_search.persist_search_failures` | false | Persist asynchronous search results that end with a search failure in the system index.
