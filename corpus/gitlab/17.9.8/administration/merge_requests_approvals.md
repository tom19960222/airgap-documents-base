---
collection: gitlab
version: "17.9.8"
title: "Merge request approvals"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/administration/merge_requests_approvals.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Premium, Ultimate
- Offering: GitLab Self-Managed

Merge request approval rules prevent users from overriding certain settings for the project.
When enabled for the entire instance, these settings
[cascade](../user/project/merge_requests/approvals/settings.md#cascade-settings-from-the-instance-or-top-level-group)
and can no longer be changed:

- In projects.
- In groups.

To enable merge request approval settings for an instance:

1. On the left sidebar, at the bottom, select **Admin**.
1. Select **Push rules**.
1. Expand **Merge request approvals**.
1. Choose the required options.
1. Select **Save changes**.

## Available rules

Merge request approval settings that can be set for the instance are:

- **Prevent approval by author**. Prevents project maintainers from allowing request authors to
  merge their own merge requests.
- **Prevent approvals by users who add commits**. Prevents project maintainers from allowing users
  to approve merge requests if they have submitted any commits to the source branch.
- **Prevent editing approval rules in projects and merge requests**. Prevents users from modifying
  the approvers list in project settings or in individual merge requests.

The following are also affected by rules for the entire instance:

- [Project merge request approval rules](../user/project/merge_requests/approvals/_index.md).
- [Group merge request approval settings](../user/group/manage.md#group-merge-request-approval-settings).
