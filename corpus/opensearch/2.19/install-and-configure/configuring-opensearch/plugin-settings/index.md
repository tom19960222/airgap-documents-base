---
collection: "opensearch"
version: "2.19"
title: "Plugin settings"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_install-and-configure/configuring-opensearch/plugin-settings.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_install-and-configure/configuring-opensearch/plugin-settings.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/install-and-configure/configuring-opensearch/plugin-settings/"
canonical_url: "https://docs.opensearch.org/latest/install-and-configure/configuring-opensearch/plugin-settings/"
canonical_route: "/install-and-configure/configuring-opensearch/plugin-settings/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 100
parent: "Configuring OpenSearch"
---
# Plugin settings

The following settings are related to OpenSearch plugins.

## Alerting plugin settings

For information about alerting settings, see [Alerting settings](../../../observing-your-data/alerting/settings/index.md#alerting-settings).

## Anomaly Detection plugin settings

For information about anomaly detection settings, see [Anomaly Detection settings](../../../observing-your-data/ad/settings/index.md).

## Asynchronous Search plugin settings

For information about asynchronous search settings, see [Asynchronous Search settings](../../../search-plugins/async/settings/index.md).

## Cross-Cluster Replication plugin settings

For information about cross-cluster replication settings, see [Replication settings](../../../tuning-your-cluster/replication-plugin/settings/index.md).

## Flow Framework plugin settings

For information about automatic workflow settings, see [Workflow settings](../../../automating-configurations/workflow-settings/index.md).

## Geospatial plugin settings

For information about the Geospatial plugin's IP2Geo processor settings, see [Cluster settings](../../../ingest-pipelines/processors/ip2geo/index.md#cluster-settings).

## Index Management plugin settings

For information about index state management (ISM) settings, see [ISM settings](../../../im-plugin/ism/settings/index.md).

### Index rollup settings

For information about index rollup settings, see [Index rollup settings](../../../im-plugin/index-rollups/settings/index.md).

## Job Scheduler plugin settings

For information about the Job Scheduler plugin settings, see [Job Scheduler cluster settings](../../../monitoring-your-cluster/job-scheduler/index.md#job-scheduler-cluster-settings).

## k-NN plugin settings

For information about k-NN settings, see [k-NN settings](../../../vector-search/settings/index.md).

## ML Commons plugin settings

For information about machine learning settings, see [ML Commons cluster settings](../../../ml-commons-plugin/cluster-settings/index.md).

## Neural Search plugin settings

The Security Analytics plugin supports the following settings:

- `plugins.neural_search.hybrid_search_disabled` (Dynamic, Boolean): Disables hybrid search. Default is `false`.

## Notifications plugin settings

The Notifications plugin supports the following settings. All settings in this list are dynamic:

- `opensearch.notifications.core.allowed_config_types` (List): The allowed configuration types of the Notifications plugin. Use the `GET /_plugins/_notifications/features` API to retrieve the value of this setting. Configuration types include `slack`, `chime`, `microsoft_teams`, `webhook`, `email`, `sns`, `ses_account`, `smtp_account`, and `email_group`.

- `opensearch.notifications.core.email.minimum_header_length` (Integer): The minimum email header length. Used for email message total length validation. Default is `160`.

- `opensearch.notifications.core.email.size_limit` (Integer): The email size limit. Used for email message total length validation. Default is `10000000`.

- `opensearch.notifications.core.http.connection_timeout` (Integer): The internal HTTP client connection timeout. The client is used for webhook-based notification channels. Default is `5000`.

- `opensearch.notifications.core.http.host_deny_list` (List): A list of denied hosts. The HTTP client does not send notifications to webhook URLs in this list.

- `opensearch.notifications.core.http.max_connection_per_route` (Integer): The maximum number of HTTP connections per route of the internal HTTP client. The client is used for webhook-based notification channels. Default is `20`.

- `opensearch.notifications.core.http.max_connections` (Integer): The maximum number of HTTP connections of the internal HTTP client. The client is used for webhook-based notification channels. Default is `60`.

- `opensearch.notifications.core.http.socket_timeout` (Integer): The socket timeout configuration of the internal HTTP client. The client is used for webhook-based notification channels. Default is `50000`.

- `opensearch.notifications.core.tooltip_support` (Boolean): Enables tooltip support for the Notifications plugin. Use the `GET /_plugins/_notifications/features` API to retrieve the value of this setting. Default is `true`.

- `opensearch.notifications.general.filter_by_backend_roles` (Boolean): Enables filtering by backend roles (role-based access control for the notification channels). Default is `false`.

## Query Insights plugin settings

For information about Query Insights plugin settings, see [Query insights settings](../../../observing-your-data/query-insights/index.md#query-insights-settings).

## Security plugin settings

For information about the Security plugin settings, see [Security settings](../security-settings/index.md).

## Security Analytics plugin settings

For information about security analytics settings, see [Security Analytics settings](../../../security-analytics/settings/index.md).

## SQL plugin settings

For information about settings related to SQL and PPL, see [SQL settings](../../../search-plugins/sql/settings/index.md).
