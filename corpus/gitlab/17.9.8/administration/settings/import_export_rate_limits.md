---
collection: gitlab
version: "17.9.8"
title: "Rate limits for imports and exports of project and groups"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/administration/settings/import_export_rate_limits.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab Self-Managed

You can configure the rate limits for imports and exports of projects and groups:

To change a rate limit:

1. On the left sidebar, at the bottom, select **Admin**.
1. Select **Settings > Network**.
1. Expand **Import and export rate limits**.
1. Change the value of any rate limit. The rate limits are per minute per user, not per IP address.
   Set to `0` to disable a rate limit.

| Limit                   | Default |
|-------------------------|---------|
| Project Import          | 6       |
| Project Export          | 6       |
| Project Export Download | 1       |
| Group Import            | 6       |
| Group Export            | 6       |
| Group Export Download   | 1       |

When a user exceeds a rate limit, it is logged in `auth.log`.
