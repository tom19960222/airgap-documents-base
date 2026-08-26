---
collection: gitlab
version: "17.9.8"
title: "Praefect Rake tasks"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/administration/raketasks/praefect.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab Self-Managed

Rake tasks are available for projects that have been created on Praefect storage. See the
[Praefect documentation](../gitaly/praefect.md) for information on configuring Praefect.

## Replica checksums

`gitlab:praefect:replicas` prints out checksums of the repository of a given `project_id` on:

- The primary Gitaly node.
- Secondary internal Gitaly nodes.

Run this Rake task on the node that GitLab is installed and not on the node that Praefect is installed.

- Linux package installations:

  ```shell
  sudo gitlab-rake "gitlab:praefect:replicas[project_id]"
  ```

- Self-compiled installations:

  ```shell
  sudo -u git -H bundle exec rake "gitlab:praefect:replicas[project_id]" RAILS_ENV=production
  ```
