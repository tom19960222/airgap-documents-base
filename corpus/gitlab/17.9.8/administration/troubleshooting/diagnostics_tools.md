---
collection: gitlab
version: "17.9.8"
title: "Diagnostics tools"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/administration/troubleshooting/diagnostics_tools.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab Self-Managed

These are some of the diagnostics tools the GitLab Support team uses during troubleshooting.
They are listed here for transparency, and for users with experience
with troubleshooting GitLab. If you are currently having an issue with GitLab, you
may want to check your [support options](https://about.gitlab.com/support/) first,
before attempting to use these tools.

## gitlabsos

The [gitlabsos](https://gitlab.com/gitlab-com/support/toolbox/gitlabsos/) utility
provides a unified method of gathering information and logs from GitLab and the system it's
running on.

## strace-parser

[strace-parser](https://gitlab.com/wchandler/strace-parser) is a small tool to analyze
and summarize raw `strace` data.

## `kubesos`

The [`kubesos`](https://gitlab.com/gitlab-com/support/toolbox/kubesos/) utility retrieves GitLab cluster configuration and logs from GitLab Helm chart deployments.
