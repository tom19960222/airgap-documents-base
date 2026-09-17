---
collection: "opensearch"
version: "2.19"
title: "Availability and recovery settings"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_install-and-configure/configuring-opensearch/availability-recovery.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_install-and-configure/configuring-opensearch/availability-recovery.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/install-and-configure/configuring-opensearch/availability-recovery/"
canonical_url: "https://docs.opensearch.org/latest/install-and-configure/configuring-opensearch/availability-recovery/"
canonical_route: "/install-and-configure/configuring-opensearch/availability-recovery/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 90
parent: "Configuring OpenSearch"
---
# Availability and recovery settings

Availability and recovery settings include settings for the following:

- [Snapshots](#snapshot-settings)
- [Cluster manager task throttling](#cluster-manager-task-throttling-settings)
- [Remote-backed storage](#remote-backed-storage-settings)
- [Search backpressure](#search-backpressure-settings)
- [Shard indexing backpressure](#shard-indexing-backpressure-settings)
- [Segment replication](#segment-replication-settings)
- [Cross-cluster replication](#cross-cluster-replication-settings)

To learn more about static and dynamic settings, see [Configuring OpenSearch](../index.md).

## Snapshot settings

OpenSearch supports the following snapshot settings:

- `snapshot.max_concurrent_operations`(Dynamic, integer): The maximum number of concurrent snapshot operations. Default is `1000`.

### Security-related snapshot settings

For security-related snapshot settings, see [Security settings](../security-settings/index.md).

### File system settings

For information about file system settings, see [Shared file system](../../../tuning-your-cluster/availability-and-recovery/snapshots/snapshot-restore/index.md#shared-file-system).

### Amazon S3 settings

For information about Amazon S3 repository settings, see [Amazon S3](../../../tuning-your-cluster/availability-and-recovery/snapshots/snapshot-restore/index.md#amazon-s3).

## Cluster manager task throttling settings

For information about cluster manager task throttling settings, see [Setting throttling limits](../../../tuning-your-cluster/cluster-manager-task-throttling/index.md#setting-throttling-limits).

## Remote-backed storage settings

OpenSearch supports the following cluster-level remote-backed storage settings:

- `cluster.remote_store.translog.buffer_interval` (Dynamic, time unit): The default value of the translog buffer interval used when performing periodic translog updates. This setting is only effective when the index setting `index.remote_store.translog.buffer_interval` is not present.

- `remote_store.moving_average_window_size` (Dynamic, integer): The moving average window size used to calculate the rolling statistic values exposed through the [Remote Store Stats API](../../../tuning-your-cluster/availability-and-recovery/remote-store/remote-store-stats-api/index.md). Default is `20`. Minimum enforced is `5`.

For more remote-backed storage settings, see [Remote-backed storage](../../../tuning-your-cluster/availability-and-recovery/remote-store/index.md) and [Configuring remote-backed storage](../../../tuning-your-cluster/availability-and-recovery/remote-store/index.md#configuring-remote-backed-storage).

For remote segment backpressure settings, see [Remote segment backpressure settings](../../../tuning-your-cluster/availability-and-recovery/remote-store/remote-segment-backpressure/index.md#remote-segment-backpressure-settings).

## Search backpressure settings

Search backpressure is a mechanism used to identify resource-intensive search requests and cancel them when the node is under duress. For more information, see [Search backpressure settings](../../../tuning-your-cluster/availability-and-recovery/search-backpressure/index.md#search-backpressure-settings).

## Shard indexing backpressure settings

Shard indexing backpressure is a smart rejection mechanism at a per-shard level that dynamically rejects indexing requests when your cluster is under strain. For more information, see shard indexing backpressure [settings](../../../tuning-your-cluster/availability-and-recovery/shard-indexing-settings/index.md).

## Segment replication settings

For information about segment replication settings, see [Segment replication](../../../tuning-your-cluster/availability-and-recovery/segment-replication/index.md).

For information about segment replication backpressure settings, see [Segment replication backpressure](../../../tuning-your-cluster/availability-and-recovery/segment-replication/backpressure/index.md).

## Cross-cluster replication settings

For information about cross-cluster replication settings, see [Replication settings](../../../tuning-your-cluster/replication-plugin/settings/index.md).
