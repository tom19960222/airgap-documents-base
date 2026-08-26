---
collection: gitlab
version: "17.9.8"
title: "Review spam logs"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/administration/review_spam_logs.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab Self-Managed

GitLab tracks user activity and flags certain behavior for potential spam.

In the **Admin** area, a GitLab administrator can view and resolve spam logs.

## Manage spam logs

**History:**

- **Trust user** [introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/131812) in GitLab 16.5.

View and resolve spam logs to moderate user activity in your instance.

To view spam logs:

1. On the left sidebar, at the bottom, select **Admin**.
1. Select **Spam logs**.
1. Optional. To resolve a spam log, select **More actions** ([icon: ellipsis_v]), then **Remove user**, **Block user**, **Remove log**, or **Trust user**.

### Resolving spam logs

You can resolve a spam log with one of the following effects:

| Option | Description |
|---------|-------------|
| **Remove user** | The user is [deleted](../user/profile/account/delete_account.md) from the instance. |
| **Block user** | The user is blocked from the instance. The spam log remains in the list. |
| **Remove log** | The spam log is removed from the list. |
| **Trust user** | The user is trusted, and can create issues, notes, snippets, and merge requests without being blocked for spam. Spam logs are not created for trusted users. |

## Related topics

- [Moderate users (administration)](moderate_users.md)
- [Review abuse reports](review_abuse_reports.md)
