---
collection: gitlab
version: "17.9.8"
title: "Use ClickHouse for analytics reports"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/administration/analytics.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Premium, Ultimate
- Offering: GitLab.com, GitLab Self-Managed

**History:**

- ClickHouse data collector [introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/414610) in GitLab 16.3 [with a flag](feature_flags.md) named `clickhouse_data_collection`. Disabled by default.
- Feature flag `clickhouse_data_collection` removed in GitLab 17.0 and replaced with an application setting.

The [contribution analytics](../user/group/contribution_analytics/_index.md) report and [Value Streams Dashboard](../user/analytics/value_streams_dashboard.md#dashboard-metrics-and-drill-down-reports) contributors count metric can use ClickHouse as a data source.

Prerequisites:

- You must have [ClickHouse configured](../integration/clickhouse.md) on your instance.

To enable ClickHouse:

1. On the left sidebar, at the bottom, select **Admin**.
1. Select **Settings > General**.
1. In the **Analytics** section, select the **Enable ClickHouse** checkbox.
