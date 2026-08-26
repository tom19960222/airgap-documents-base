---
collection: gitlab
version: "17.9.8"
title: "Instance Kubernetes clusters (certificate-based) (deprecated)"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/user/instance/clusters/_index.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab Self-Managed

> **Warning:**
>
> This feature was [deprecated](https://gitlab.com/groups/gitlab-org/configure/-/epics/8) in GitLab 14.5. To connect clusters to GitLab,
> use the [GitLab agent](../../clusters/agent/_index.md).

Similar to Kubernetes clusters for [projects](../../project/clusters/_index.md)
and [groups](../../group/clusters/_index.md), instance Kubernetes clusters enable
you to connect a Kubernetes cluster to the GitLab instance, and use the same cluster
across multiple projects.

To view Kubernetes clusters for your instance:

1. On the left sidebar, at the bottom, select **Admin**.
1. Select **Kubernetes**.

## Cluster precedence

GitLab tries to match clusters in the following order:

- Project clusters.
- Group clusters.
- Instance clusters.

To be selected, the cluster must be enabled and
match the [environment selector](../../../ci/environments/_index.md#limit-the-environment-scope-of-a-cicd-variable).

## Cluster environments

- Tier: Premium, Ultimate
- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated

For a consolidated view of which CI [environments](../../../ci/environments/_index.md)
are deployed to the Kubernetes cluster, see the documentation for
[cluster environments](../../clusters/environments.md).

## More information

For information on integrating GitLab and Kubernetes, see
[Kubernetes clusters](../../infrastructure/clusters/_index.md).
