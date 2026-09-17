---
collection: "opensearch"
version: "2.19"
title: "Shard indexing backpressure"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_tuning-your-cluster/availability-and-recovery/shard-indexing-backpressure.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_tuning-your-cluster/availability-and-recovery/shard-indexing-backpressure.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/tuning-your-cluster/availability-and-recovery/shard-indexing-backpressure/"
canonical_url: "https://docs.opensearch.org/latest/tuning-your-cluster/availability-and-recovery/shard-indexing-backpressure/"
canonical_route: "/tuning-your-cluster/availability-and-recovery/shard-indexing-backpressure/"
redirect_from: ["/opensearch/shard-indexing-backpressure/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
layout: "default"
nav_order: 62
parent: "Availability and recovery"
---
# Shard indexing backpressure

Shard indexing backpressure is a smart rejection mechanism at a per-shard level that dynamically rejects indexing requests when your cluster is under strain. It propagates a backpressure that transfers requests from an overwhelmed node or shard to other nodes or shards that are still healthy.

With shard indexing backpressure, you can prevent nodes in your cluster from running into cascading failures due to performance degradation caused by slow nodes, stuck tasks, resource-intensive requests, traffic surges, skewed shard allocations, and so on.

Shard indexing backpressure comes into effect only when one primary and one secondary parameter is breached.

## Primary parameters

Primary parameters are early indicators that a cluster is under strain:

- Shard memory limit breach: If the memory usage of a shard exceeds 95% of its allocated memory, this limit is breached.
- Node memory limit breach: If the memory usage of a node exceeds 70% of its allocated memory, this limit is breached.

The breach of primary parameters doesn’t cause any actual request rejections, it just triggers an evaluation of the secondary parameters.

## Secondary parameters

Secondary parameters check the performance at the shard level to confirm that the cluster is under strain:

- Throughput: If the throughput at the shard level decreases significantly in its historic view, this limit is breached.
- Successful Request: If the number of pending requests increases significantly in its historic view, this limit is breached.
