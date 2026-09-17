---
collection: "opensearch"
version: "2.19"
title: "Cross-cluster replication"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_tuning-your-cluster/replication-plugin/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_tuning-your-cluster/replication-plugin/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/tuning-your-cluster/replication-plugin/"
canonical_url: "https://docs.opensearch.org/latest/tuning-your-cluster/replication-plugin/index/"
canonical_route: "/tuning-your-cluster/replication-plugin/"
redirect_from: ["/replication-plugin/","/tuning-your-cluster/replication-plugin/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
layout: "default"
nav_order: 12
---
# Cross-cluster replication

The cross-cluster replication plugin lets you replicate indexes, mappings, and metadata from one OpenSearch cluster to another. Cross-cluster replication has the following benefits:
- By replicating your indexes, you ensure that you can continue to handle search requests if there's an outage.
- Replicating data across geographically distant data centers minimizes the distance between the data and the application server. This reduces expensive latencies.
- You can replicate data from multiple smaller clusters to a centralized reporting cluster, which is useful when it's inefficient to query across a large network.

Replication follows an active-passive model where the follower index (where the data is replicated) pulls data from the leader (remote) index.

The replication plugin supports replication of indexes using wildcard pattern matching and provides commands to pause, resume, and stop replication. Once replication starts on an index, it initiates persistent background tasks on all primary shards on the follower cluster, which continuously poll corresponding shards from the leader cluster for updates.

You can use the replication plugin with the Security plugin to encrypt cross-cluster traffic with node-to-node encryption and control access to replication activities.

To start, see [Get started with cross-cluster replication](getting-started/index.md).
