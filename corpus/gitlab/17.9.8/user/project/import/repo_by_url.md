---
collection: gitlab
version: "17.9.8"
title: "Import project from repository by URL"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/user/project/import/repo_by_url.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated

You can import your existing repositories by providing the Git URL. You can't import GitLab issues and merge requests
this way. Other methods provide more complete import methods.

If the repository is too large, the import can timeout.

## Prerequisites

**History:**

- Requirement for Maintainer role instead of Developer role introduced in GitLab 16.0 and backported to GitLab 15.11.1 and GitLab 15.10.5.

- [Repository by URL import source](../../../administration/settings/import_and_export_settings.md#configure-allowed-import-sources)
  must be enabled. If not enabled, ask your GitLab administrator to enable it. The Repository by URL import source is enabled
  by default on GitLab.com.
- At least the Maintainer role on the destination group to import to.
- If importing a private repository, an access token for authenticated access to the source repository might be required
  instead of a password.

## Import project by URL

1. On the left sidebar, at the top, select **Create new** ([icon: plus]) and **New project/repository**.
1. Select **Import project**.
1. Select **Repository by URL**.
1. Enter a **Git repository URL**.
1. Complete the remaining fields. A username and password (or access token) is required for imports from private
   repositories.
1. Select **Create project**.

Your newly created project is displayed.
