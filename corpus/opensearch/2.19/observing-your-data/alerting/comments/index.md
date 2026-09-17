---
collection: "opensearch"
version: "2.19"
title: "Adding comments"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_observing-your-data/alerting/comments.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_observing-your-data/alerting/comments.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/observing-your-data/alerting/comments/"
canonical_url: "https://docs.opensearch.org/latest/observing-your-data/alerting/comments/"
canonical_route: "/observing-your-data/alerting/comments/"
redirect_from: ["/monitoring-plugins/alerting/comments/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
layout: "default"
nav_order: 35
parent: "Alerting"
---
# Adding comments

This is an experimental feature and is not recommended for use in a production environment. For updates on the progress of the feature or if you want to leave feedback, see the associated [GitHub issue](https://github.com/opensearch-project/OpenSearch-Dashboards/issues/6999).
{: .warning}

When an alert is generated, add comments to share information about its root cause and facilitate resolution. Comments are enabled by setting `plugins.alerting.comments_enabled` to `true` using the [`cluster/settings` API](../settings/index.md).

Comments can be accessed through the alerts table view by selecting the comment icon within an alert's row. From there, comments can be added, edited, or deleted. An Alerting Comments API is also available for programmatic comment management. For more information, see [Alerting API](../api/index.md).

## Viewing comment authors

If the Security plugin is installed, then the comment's author is displayed. Otherwise, `Unknown` is displayed.

## Assigning permissions

Comment permissions are determined by the backend roles associated with the alert. These backend roles are inherited from the monitor that generated the alert. For more information about how to limit access based on backend roles, see [Limit access by backend role](../security/index.md#advanced-limit-access-by-backend-role).
