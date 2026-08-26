---
collection: gitlab
version: "17.9.8"
title: "View GitLab Dedicated instance details"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/administration/dedicated/tenant_overview.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Ultimate
- Offering: GitLab Dedicated

Monitor your GitLab Dedicated instance details, maintenance windows, and configuration status in Switchboard.

## View your instance details

To access your instance details:

1. Sign in to [Switchboard](https://console.gitlab-dedicated.com/).
1. Select your tenant.

The **Overview** page displays:

- Any pending configuration changes
- When the instance was updated
- Instance details
- Maintenance windows
- Hosted runners

## Tenant overview

The top section shows important information about your tenant, including:

- Tenant name and URL
- Total Git repository capacity
- Current GitLab version
- Reference architecture
- Maintenance window
- AWS regions for data storage and backup

## Maintenance windows

The **Maintenance windows** section displays the:

- Next scheduled maintenance window
- Most recent completed maintenance window
- Most recent emergency maintenance window (if applicable)
- Upcoming GitLab version upgrade

> **Note:**
>
> Each Sunday night in UTC, Switchboard updates to display the planned GitLab version upgrades for the upcoming week's maintenance windows. For more information, see [Maintenance windows](../dedicated/maintenance.md#maintenance-windows).

## Hosted runners

The **Hosted runners** section shows the [hosted runners](../dedicated/hosted_runners.md) associated with your instance.
