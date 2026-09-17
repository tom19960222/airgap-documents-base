---
collection: "opensearch"
version: "2.19"
title: "Replication security"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_tuning-your-cluster/replication-plugin/permissions.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_tuning-your-cluster/replication-plugin/permissions.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/tuning-your-cluster/replication-plugin/permissions/"
canonical_url: "https://docs.opensearch.org/latest/tuning-your-cluster/replication-plugin/permissions/"
canonical_route: "/tuning-your-cluster/replication-plugin/permissions/"
redirect_from: ["/replication-plugin/permissions/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 30
parent: "Cross-cluster replication"
---
# Cross-cluster replication security

You can use the [Security plugin](../../../security/index.md) with cross-cluster replication to limit users to certain actions. For example, you might want certain users to only perform replication activity on the leader or follower cluster.

Because cross-cluster replication involves multiple clusters, it's possible that clusters might have different security configurations. The following configurations are supported:

- Security plugin fully enabled on both clusters
- Security plugin enabled only for TLS on both clusters (`plugins.security.ssl_only`)
- Security plugin absent or disabled on both clusters (not recommended)

Enable node-to-node encryption on both the leader and the follower cluster to ensure that replication traffic between the clusters is encrypted.

## Basic permissions

In order for non-admin users to perform replication activities, they must be mapped to the appropriate permissions.

The Security plugin has two built-in roles that cover most replication use cases: `cross_cluster_replication_leader_full_access`, which provides replication permissions on the leader cluster, and `cross_cluster_replication_follower_full_access`, which provides replication permissions on the follower cluster. For descriptions of each, see [Predefined roles](../../../security/access-control/users-roles/index.md#predefined-roles).

If you don't want to use the default roles, you can combine individual replication [permissions](index.md#replication-permissions) to meet your needs. Most permissions correspond to specific REST API operations. For example, the `indices:admin/plugins/replication/index/pause` permission lets you pause replication.

## Map the leader and follower cluster roles

The [start replication](../api/index.md#start-replication) and [create replication rule](../api/index.md#create-replication-rule) operations are special cases. They involve background processes on the leader and follower clusters that must be associated with roles. When you perform one of these actions, you must explicitly pass the `leader_cluster_role` and
`follower_cluster_role` in the request, which OpenSearch then uses in all backend replication tasks.

To enable non-admins to start replication and create replication rules, create an identical user on each cluster (for example, `replication_user`) and map them to the `cross_cluster_replication_leader_full_access` role on the remote cluster and `cross_cluster_replication_follower_full_access` on the follower cluster. For a tutorial, see [Mapping users to roles](../../../security/access-control/users-roles/index.md#mapping-users-to-roles).

Then add those roles to the request, and sign it with the appropriate credentials:

```bash
curl -XPUT -k -H 'Content-Type: application/json' -u 'replication_user:password' 'https://localhost:9200/_plugins/_replication/follower-01/_start?pretty' -d '
{
   "leader_alias": "leader-cluster",
   "leader_index": "leader-01",
   "use_roles":{
      "leader_cluster_role": "cross_cluster_replication_leader_full_access",
      "follower_cluster_role": "cross_cluster_replication_follower_full_access"
   }
}'
```

You can create your own, custom leader and follower cluster roles using individual permissions, but we recommend using the default roles, which are a good fit for most use cases.

## Replication permissions

The following sections list the available index and cluster-level permissions for cross-cluster replication.

### Follower cluster

The Security plugin supports these permissions for the follower cluster:

```
indices:admin/plugins/replication/index/setup/validate
indices:admin/plugins/replication/index/start
indices:admin/plugins/replication/index/pause
indices:admin/plugins/replication/index/resume
indices:admin/plugins/replication/index/stop
indices:admin/plugins/replication/index/update
indices:admin/plugins/replication/index/status_check
indices:data/write/plugins/replication/changes
cluster:admin/plugins/replication/autofollow/update
```

### Leader cluster

The Security plugin supports these permissions for the leader cluster:

```
indices:admin/plugins/replication/index/setup/validate
indices:data/read/plugins/replication/file_chunk
indices:data/read/plugins/replication/changes
```
