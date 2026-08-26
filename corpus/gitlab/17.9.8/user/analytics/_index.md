---
collection: gitlab
version: "17.9.8"
title: "Analyze GitLab usage"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/user/analytics/_index.md
fetched_at: 2025-05-07T10:05:15Z
---
**History:**

- Group-level analytics moved to GitLab Premium in 13.9.

GitLab provides different types of analytics insights for instances, groups, and [projects](../project/settings/_index.md#turn-off-project-analytics).

## Analytics features

### End-to-end insight & visibility analytics

Use these features to gain insights into your overall software development lifecycle.

| Feature | Description | Project-level | Group-level | Instance-level |
| ------- | ----------- | ------------- | ----------- | -------------- |
| [Value Streams Dashboard](value_streams_dashboard.md) | Insights into DevSecOps trends, patterns, and opportunities for digital transformation improvements. | [icon: check-circle] Yes | [icon: check-circle] Yes | [icon: dotted-circle] No |
| [Value Stream Management Analytics](../group/value_stream_analytics/_index.md) | Insights into time-to-value through customizable stages. | [icon: check-circle] Yes | [icon: check-circle] Yes | [icon: dotted-circle] No |
| DevOps adoption [by group](../group/devops_adoption/_index.md) and [by instance](../../administration/analytics/dev_ops_reports.md) | Organization's maturity in DevOps adoption, with feature adoption over time and feature distribution by group. | [icon: dotted-circle] No | [icon: check-circle] Yes | [icon: check-circle] Yes |
| [Usage trends](../../administration/analytics/usage_trends.md) | Overview of instance data and changes in data volume over time. | [icon: dotted-circle] No | [icon: dotted-circle] No | [icon: check-circle] Yes |
| [Insights](../project/insights/_index.md) | Customizable reports to explore issues, merged merge requests, and triage hygiene. | [icon: check-circle] Yes | [icon: check-circle] Yes | [icon: dotted-circle] No |
| [Product analytics](../../development/internal_analytics/product_analytics.md) | Understanding how users behave and interact with your product.| [icon: dotted-circle] No | [icon: check-circle] Yes | [icon: dotted-circle] No |
| [Analytics dashboards](analytics_dashboards.md) | Built-in and customizable dashboards to visualize collected data. | [icon: check-circle] Yes | [icon: check-circle] Yes | [icon: dotted-circle] No |

### Productivity analytics

Use these features to gain insights into the productivity of your team on issues and merge requests.

| Feature | Description | Project-level | Group-level | Instance-level |
| ------- | ----------- | ------------- | ----------- | -------------- |
| [Issue analytics](../group/issues_analytics/_index.md) | Visualization of issues created each month. | [icon: check-circle] Yes | [icon: check-circle] Yes | [icon: dotted-circle] No |
| [Merge request analytics](merge_request_analytics.md) | Overview of merge requests, with mean time to merge, throughput, and activity details. | [icon: check-circle] Yes | [icon: dotted-circle] No | [icon: dotted-circle] No |
| [Productivity analytics](productivity_analytics.md) | Merge request lifecycle, filterable down to author level. | [icon: dotted-circle] No | [icon: check-circle] Yes | [icon: dotted-circle] No |
| [Code review analytics](code_review_analytics.md) | Open merge requests with information about merge request activity. | [icon: check-circle] Yes | [icon: dotted-circle] No | [icon: dotted-circle] No |

### Developer analytics

Use these features to gain insights into developer productivity and code coverage.

| Feature | Description | Project-level | Group-level | Instance-level |
| ------- | ----------- | ------------- | ----------- | -------------- |
| [Contribution analytics](../group/contribution_analytics/_index.md) | Overview of [contribution events](../profile/contributions_calendar.md) made by group members, with bar chart of push events, merge requests, and issues. | [icon: dotted-circle] No | [icon: check-circle] Yes | [icon: dotted-circle] No |
| [Contributor analytics](../analytics/contributor_analytics.md) | Overview of commits made by project members, with line chart of number of commits. | [icon: check-circle] Yes | [icon: dotted-circle] No | [icon: dotted-circle] No |
| [Repository analytics](../group/repositories_analytics/_index.md) | Programming languages used in the repository and code coverage statistics. | [icon: check-circle] Yes | [icon: check-circle] Yes | [icon: dotted-circle] No |

### CI/CD analytics

Use these features to gain insights into CI/CD performance.

| Feature | Description | Project-level | Group-level | Instance-level |
| ------- | ----------- | ------------- | ----------- | -------------- |
| [CI/CD analytics](ci_cd_analytics.md) | Pipeline duration and successes or failures. | [icon: check-circle] Yes | [icon: check-circle] Yes | [icon: dotted-circle] No |
| [DORA metrics](dora_metrics.md) | DORA metrics over time. | [icon: check-circle] Yes | [icon: check-circle] Yes | [icon: dotted-circle] No |

### Security analytics

Use these features to gain insights into security vulnerabilities and metrics.

| Feature | Description | Project-level | Group-level | Instance-level |
| ------- | ----------- | ------------- | ----------- | -------------- |
| [Security Dashboards](../application_security/security_dashboard/_index.md) | Collection of metrics, ratings, and charts for vulnerabilities detected by security scanners. | [icon: check-circle] Yes | [icon: check-circle] Yes | [icon: dotted-circle] No |

## Glossary

The following glossary provides definitions for common development metrics used in analytics features,
and explains how they are measured in GitLab.

| Metric | Definition | Measurement in GitLab |
| ------ | ---------- | --------------------- |
| Mean Time to Change (MTTC) | The average duration between idea and delivery. | From when an issue is created until its related merge request is deployed to production. |
| Mean Time to Detect (MTTD) | The average duration that a bug goes undetected in production. | From when a bug is deployed to production until an issue is created to report it. |
| Mean Time to Merge (MTTM) | The average lifespan of a merge request. | From when a merge request is created until it is merged. Excludes merge requests that are closed or unmerged. For more information, see [merge request analytics](merge_request_analytics.md). |
| Mean Time to Recover / Repair / Resolution / Resolve / Restore (MTTR) | The average duration that a bug is not fixed in production. | From when a bug is deployed to production until the bug fix is deployed. |
| Velocity | The total issue burden completed in a specific period of time. The burden is usually measured in points or weight, often per sprint. | Total points or weight of issues closed in a specific period of time. For example, "30 points per sprint". |
