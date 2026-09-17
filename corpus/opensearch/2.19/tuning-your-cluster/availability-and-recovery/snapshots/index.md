---
collection: "opensearch"
version: "2.19"
title: "Snapshots"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_tuning-your-cluster/availability-and-recovery/snapshots/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_tuning-your-cluster/availability-and-recovery/snapshots/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/tuning-your-cluster/availability-and-recovery/snapshots/"
canonical_url: "https://docs.opensearch.org/latest/tuning-your-cluster/availability-and-recovery/snapshots/index/"
canonical_route: "/tuning-your-cluster/availability-and-recovery/snapshots/"
redirect_from: ["/opensearch/snapshots/","/tuning-your-cluster/availability-and-recovery/snapshots/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 5
parent: "Availability and recovery"
---
# Snapshots

Snapshots are backups of a cluster's indexes and state. State includes cluster settings, node information, index metadata (mappings, settings, or templates), and shard allocation.

Snapshots have two main uses:

- **Recovering from failure**

  For example, if cluster health goes red, you might restore the red indexes from a snapshot.

- **Migrating from one cluster to another**

  For example, if you're moving from a proof-of-concept to a production cluster, you might take a snapshot of the former and restore it on the latter.

You can take and restore snapshots using the [snapshot API](snapshot-restore/index.md).

If you need to automate snapshot creation, you can use the [snapshot management](snapshot-management/index.md) feature.
