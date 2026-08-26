---
collection: gitlab
version: "17.9.8"
title: "Project-level Kubernetes clusters (certificate-based) (deprecated)"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/user/project/clusters/_index.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab.com, GitLab Self-Managed

> **Warning:**
>
> This feature was [deprecated](https://gitlab.com/groups/gitlab-org/configure/-/epics/8)
> in GitLab 14.5. To connect clusters to GitLab, use the
> [GitLab agent](../../clusters/agent/_index.md).

[Project-level](../../infrastructure/clusters/connect/_index.md#cluster-levels-deprecated) Kubernetes clusters
allow you to connect a Kubernetes cluster to a project in GitLab.

You can also [connect multiple clusters](multiple_kubernetes_clusters.md)
to a single project.

## View your project-level clusters

To view project-level Kubernetes clusters:

1. On the left sidebar, select **Search or go to** and find your project.
1. Select **Operate > Kubernetes clusters**.
