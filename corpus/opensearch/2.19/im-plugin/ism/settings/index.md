---
collection: "opensearch"
version: "2.19"
title: "Settings"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_im-plugin/ism/settings.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_im-plugin/ism/settings.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/im-plugin/ism/settings/"
canonical_url: "https://docs.opensearch.org/latest/im-plugin/ism/settings/"
canonical_route: "/im-plugin/ism/settings/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 4
parent: "Index State Management"
---
# ISM settings

We don't recommend changing these settings; the defaults should work well for most use cases.

Index State Management (ISM) stores its configuration in the `.opendistro-ism-config` index. Don't modify this index without using the [ISM API operations](../api/index.md).

All settings are available using the OpenSearch `_cluster/settings` operation. None require a restart, and all can be marked `persistent` or `transient`. To learn more about static and dynamic settings, see [Configuring OpenSearch](../../../install-and-configure/configuring-opensearch/index.md).

Setting | Default | Description
:--- | :--- | :---
`plugins.index_state_management.enabled` | True | Specifies whether ISM is enabled or not.
`plugins.index_state_management.job_interval` | 5 minutes | The interval at which the managed index jobs are run.
`plugins.index_state_management.jitter` | 0.6 | A randomized delay that is added to a job's base run time to prevent a surge of activity from all indexes at the same time. A value of 0.6 means a delay of 0-60% of a job interval is added to the base interval. For example, if you have a base interval time of 30 minutes, a value of 0.6 means an amount anywhere between 0 to 18 minutes gets added to your job interval. Maximum is 1, which means an additional interval time of 100%. This maximum cannot exceed `plugins.jobscheduler.jitter_limit`, which also has a default of 0.6. For example, if `plugins.index_state_management.jitter` is set to 0.8, ISM uses `plugins.jobscheduler.jitter_limit` of 0.6 instead.
`plugins.index_state_management.coordinator.sweep_period` | 10 minutes | How often the routine background sweep is run.
`plugins.index_state_management.coordinator.backoff_millis` | 50 milliseconds | The backoff time between retries for failures in the `ManagedIndexCoordinator` (such as when we update managed indexes).
`plugins.index_state_management.coordinator.backoff_count` | 2 | The count of retries for failures in the `ManagedIndexCoordinator`.
`plugins.index_state_management.history.enabled` | True | Specifies whether audit history is enabled or not. The logs from ISM are automatically indexed to a logs document.
`plugins.index_state_management.history.max_docs` | 2,500,000 | The maximum number of documents before rolling over the audit history index.
`plugins.index_state_management.history.max_age` | 24 hours | The maximum age before rolling over the audit history index.
`plugins.index_state_management.history.rollover_check_period` | 8 hours | The time between rollover checks for the audit history index.
`plugins.index_state_management.history.rollover_retention_period` | 30 days | How long audit history indexes are kept.
`plugins.index_state_management.allow_list` | All actions | List of actions that you can use.
