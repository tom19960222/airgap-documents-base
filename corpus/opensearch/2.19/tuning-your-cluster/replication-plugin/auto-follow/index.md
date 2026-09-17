---
collection: "opensearch"
version: "2.19"
title: "Auto-follow"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_tuning-your-cluster/replication-plugin/auto-follow.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_tuning-your-cluster/replication-plugin/auto-follow.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/tuning-your-cluster/replication-plugin/auto-follow/"
canonical_url: "https://docs.opensearch.org/latest/tuning-your-cluster/replication-plugin/auto-follow/"
canonical_route: "/tuning-your-cluster/replication-plugin/auto-follow/"
redirect_from: ["/replication-plugin/auto-follow/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 20
parent: "Cross-cluster replication"
---
# Auto-follow for cross-cluster replication

Auto-follow lets you automatically replicate indexes created on the leader cluster based on matching patterns. When you create an index on the leader cluster with a name that matches a specified pattern (for example, `index-01*`), a corresponding follower index is automatically created on the follower cluster.

You can configure multiple replication rules for a single cluster. The patterns currently only support wildcard matching.

## Prerequisites

You need to [set up a cross-cluster connection](../getting-started/index.md#set-up-a-cross-cluster-connection) between two clusters before you can enable auto-follow.

## Permissions

If the Security plugin is enabled, make sure that non-admin users are mapped to the appropriate permissions so they can perform replication actions. For index and cluster-level permissions requirements, see [Cross-cluster replication permissions](../permissions/index.md).

## Get started with auto-follow

Replication rules are a collection of patterns that you create against a single follower cluster. When you create a replication rule, it starts by automatically replicating any *existing* indexes that match the pattern. It will then continue to replicate any *new* indexes that you create that match the pattern.

Create a replication rule on the follower cluster:

```bash
curl -XPOST -k -H 'Content-Type: application/json' -u 'admin:<custom-admin-password>' 'https://localhost:9200/_plugins/_replication/_autofollow?pretty' -d '
{
   "leader_alias" : "my-connection-alias",
   "name": "my-replication-rule",
   "pattern": "movies*",
   "use_roles":{
      "leader_cluster_role": "all_access",
      "follower_cluster_role": "all_access"
   }
}'
```

If the Security plugin is disabled, you can leave out the `use_roles` parameter. If it's enabled, however, you need to specify the leader and follower cluster roles that OpenSearch uses to authenticate requests. This example uses `all_access` for simplicity, but we recommend creating a replication user on each cluster and [mapping it accordingly](../permissions/index.md#map-the-leader-and-follower-cluster-roles).
{: .tip }

To test the rule, create a matching index on the leader cluster:

```bash
curl -XPUT -k -H 'Content-Type: application/json' -u 'admin:<custom-admin-password>' 'https://localhost:9201/movies-0001?pretty'
```

And confirm its replica shows up on the follower cluster:

```bash
curl -XGET -u 'admin:<custom-admin-password>' -k 'https://localhost:9200/_cat/indices?v'
```

It might take several seconds for the index to appear.

```bash
health status index        uuid                     pri rep docs.count docs.deleted store.size pri.store.size
yellow open   movies-0001  kHOxYYHxRMeszLjTD9rvSQ     1   1          0            0       208b           208b
```

## Retrieve replication rules

To retrieve a list of existing replication rules that are configured on a cluster, send the following request:

```bash
curl -XGET -u 'admin:<custom-admin-password>' -k 'https://localhost:9200/_plugins/_replication/autofollow_stats'

{
   "num_success_start_replication": 1,
   "num_failed_start_replication": 0,
   "num_failed_leader_calls": 0,
   "failed_indices":[

   ],
   "autofollow_stats":[
      {
         "name":"my-replication-rule",
         "pattern":"movies*",
         "num_success_start_replication": 1,
         "num_failed_start_replication": 0,
         "num_failed_leader_calls": 0,
         "failed_indices":[

         ]
      }
   ]
}
```

## Delete a replication rule

To delete a replication rule, send the following request to the follower cluster:

```bash
curl -XDELETE -k -H 'Content-Type: application/json' -u 'admin:<custom-admin-password>' 'https://localhost:9200/_plugins/_replication/_autofollow?pretty' -d '
{
   "leader_alias" : "my-connection-alias",
   "name": "my-replication-rule"
}'
```

When you delete a replication rule, OpenSearch stops replicating *new* indexes that match the pattern, but existing indexes that the rule previously created remain read-only and continue to replicate. If you need to stop existing replication activity and open the indexes up for writes, use the [stop replication API operation](../api/index.md#stop-replication).
