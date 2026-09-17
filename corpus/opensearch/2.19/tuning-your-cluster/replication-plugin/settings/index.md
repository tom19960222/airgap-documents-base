---
collection: "opensearch"
version: "2.19"
title: "Replication settings"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_tuning-your-cluster/replication-plugin/settings.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_tuning-your-cluster/replication-plugin/settings.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/tuning-your-cluster/replication-plugin/settings/"
canonical_url: "https://docs.opensearch.org/latest/tuning-your-cluster/replication-plugin/settings/"
canonical_route: "/tuning-your-cluster/replication-plugin/settings/"
redirect_from: ["/replication-plugin/settings/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 40
parent: "Cross-cluster replication"
---
# Replication settings

The replication plugin adds several settings to the standard OpenSearch cluster settings.
The settings are dynamic, so you can change the default behavior of the plugin without restarting your cluster. To learn more about static and dynamic settings, see [Configuring OpenSearch](../../../install-and-configure/configuring-opensearch/index.md).

You can mark settings as `persistent` or `transient`.

For example, to update how often the follower cluster polls the leader cluster for updates:

```json
PUT _cluster/settings
{
  "persistent": {
    "plugins.replication.follower.metadata_sync_interval": "30s"
  }
}
```

These settings manage the resources consumed by remote recoveries. We don’t recommend changing these settings; the defaults should work well for most use cases.

Setting | Default | Description
:--- | :--- | :---
`plugins.replication.follower.index.recovery.chunk_size` | 10 MB | The chunk size requested by the follower cluster during file transfer. Specify the chunk size as a value and unit, for example, 10 MB, 5 KB. See [Supported units](../../../api-reference/units/index.md).
`plugins.replication.follower.index.recovery.max_concurrent_file_chunks` | 4 | The number of file chunk requests that can be sent in parallel for each recovery.
`plugins.replication.follower.index.ops_batch_size` | 50000 | The number of operations that can be fetched at a time during the syncing phase of replication.
`plugins.replication.follower.concurrent_readers_per_shard` | 2 | The number of concurrent requests from the follower cluster per shard during the syncing phase of replication.
`plugins.replication.autofollow.fetch_poll_interval` | 30s | How often auto-follow tasks poll the leader cluster for new matching indexes.
`plugins.replication.follower.metadata_sync_interval` | 60s | How often the follower cluster polls the leader cluster for updated index metadata.
`plugins.replication.translog.retention_lease.pruning.enabled` | true | If enabled, prunes the translog based on retention leases on the leader index.
`plugins.replication.translog.retention_size` | 512 MB | Controls the size of the translog on the leader index.
