---
collection: gitlab
version: "17.9.8"
title: "Issue closing pattern"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/administration/issue_closing_pattern.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab Self-Managed

> **Note:**
>
> This page explains how an administrator can configure issue closing patterns.
> For user documentation about the feature, see
> [Closing issues automatically](../user/project/issues/managing_issues.md#closing-issues-automatically).

When a commit or merge request resolves one or more issues, GitLab can close those issues when the
commit or merge request lands in the project's default branch.

## Change the issue closing pattern

The [default issue closing pattern](../user/project/issues/managing_issues.md#default-closing-pattern)
covers a wide range of words.

To change the default issue closing pattern to suit your needs:

**Tab: Linux package (Omnibus)**

1. Edit `/etc/gitlab/gitlab.rb` and change the `gitlab_rails['gitlab_issue_closing_pattern']`
   value:

   ```ruby
   gitlab_rails['gitlab_issue_closing_pattern'] = /<regular_expression>/.source
   ```

1. Save the file and reconfigure GitLab:

   ```shell
   sudo gitlab-ctl reconfigure
   ```

**Tab: Helm chart (Kubernetes)**

1. Export the Helm values:

   ```shell
   helm get values gitlab > gitlab_values.yaml
   ```

1. Edit `gitlab_values.yaml` and change the `issueClosingPattern` value:

   ```yaml
   global:
     appConfig:
       issueClosingPattern: "<regular_expression>"
   ```

1. Save the file and apply the new values:

   ```shell
   helm upgrade -f gitlab_values.yaml gitlab gitlab/gitlab
   ```

**Tab: Docker**

1. Edit `docker-compose.yml` and change the `gitlab_rails['gitlab_issue_closing_pattern']`
   value:

   ```yaml
   version: "3.6"
   services:
     gitlab:
       environment:
         GITLAB_OMNIBUS_CONFIG: |
           gitlab_rails['gitlab_issue_closing_pattern'] = /<regular_expression>/.source
   ```

1. Save the file and restart GitLab:

   ```shell
   docker compose up -d
   ```

**Tab: Self-compiled (source)**

1. Edit `/home/git/gitlab/config/gitlab.yml` and change the `issue_closing_pattern` value:

   ```yaml
   production: &base
     gitlab:
       issue_closing_pattern: "<regular_expression>"
   ```

1. Save the file and restart GitLab:

   ```shell
   # For systems running systemd
   sudo systemctl restart gitlab.target

   # For systems running SysV init
   sudo service gitlab restart
   ```

To test the issue closing pattern, use [Rubular](https://rubular.com).
Rubular does not understand `%{issue_ref}`. When you test your patterns,
replace this string with `#\d+`, which matches only local issue references like `#123`.
