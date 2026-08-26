---
collection: gitlab
version: "17.9.8"
title: "Terraform limits"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/administration/settings/terraform_limits.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab Self-Managed

**History:**

- [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/352951) in GitLab 15.7.

You can limit the total storage of [Terraform state files](../terraform_state.md).
The limit applies to each individual
state file version, and is checked whenever a new version is created.

To add a storage limit:

1. On the left sidebar, at the bottom, select **Admin**.
1. Select **Settings > Preferences**.
1. Expand **Terraform limits**.
1. Enter a size limit in bytes. Set to `0` to allow files of unlimited size.

When Terraform state files exceed this limit, they are not saved, and associated Terraform operations are rejected.
