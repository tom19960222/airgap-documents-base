---
collection: gitlab
version: "17.9.8"
title: "Add a cluster using cluster certificates (deprecated)"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/user/project/clusters/add_remove_clusters.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab.com, GitLab Self-Managed

**History:**

- [Deprecated](https://gitlab.com/gitlab-org/gitlab/-/issues/327908) in GitLab 14.0.

> **Warning:**
>
> This feature was [deprecated](https://gitlab.com/gitlab-org/gitlab/-/issues/327908) in GitLab 14.0.
> To create and manage a new cluster use [Infrastructure as Code](../../infrastructure/iac/_index.md).

## Disable a cluster

When you successfully connect an existing cluster using cluster certificates, the cluster connection to GitLab becomes enabled. To disable it:

1. Go to your:
   - Project's [icon: cloud-gear] **Operate > Kubernetes clusters** page, for a project-level cluster.
   - Group's [icon: cloud-gear] **Kubernetes** page, for a group-level cluster.
   - The **Admin** area's **Kubernetes** page, for an instance-level cluster.
1. Select the name of the cluster you want to disable.
1. Toggle **GitLab Integration** off (in gray).
1. Select **Save changes**.

## Remove a cluster

When you remove a cluster integration, you only remove the cluster relationship
to GitLab, not the cluster. To remove the cluster itself, go to your cluster's
GKE or EKS dashboard to do it from their UI or use `kubectl`.

You need at least Maintainer [permissions](../../permissions.md) to your
project or group to remove the integration with GitLab.

When removing a cluster integration, you have two options:

- **Remove integration**: remove only the Kubernetes integration.
- **Remove integration and resources**: remove the cluster integration and
  all GitLab cluster-related resources such as namespaces, roles, and bindings.

To remove the Kubernetes cluster integration:

1. Go to your cluster details page.
1. Select the **Advanced Settings** tab.
1. Select either **Remove integration** or **Remove integration and resources**.

### Remove clusters by using the Rails console

- Tier: Free, Premium, Ultimate
- Offering: GitLab Self-Managed, GitLab Dedicated

[Start a Rails console session](../../../administration/operations/rails_console.md#starting-a-rails-console-session).

To find a cluster:

``` ruby
cluster = Clusters::Cluster.find(1)
cluster = Clusters::Cluster.find_by(name: 'cluster_name')
```

To delete a cluster but not the associated resources:

```ruby
# Find users who have administrator access
user = User.find_by(username: 'admin_user')

# Find the cluster with the ID
cluster = Clusters::Cluster.find(1)

# Delete the cluster
Clusters::DestroyService.new(user).execute(cluster)
```
