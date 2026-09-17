---
collection: "opensearch"
version: "2.19"
title: "Using snapshots to migrate data"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_upgrade-to/snapshot-migrate.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_upgrade-to/snapshot-migrate.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/upgrade-to/snapshot-migrate/"
canonical_url: "https://docs.opensearch.org/latest/tuning-your-cluster/availability-and-recovery/snapshots/snapshot-restore/"
canonical_route: "/tuning-your-cluster/availability-and-recovery/snapshots/snapshot-restore/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 5
---
# Using snapshots to migrate data

One popular approach is to take a [snapshot](../../tuning-your-cluster/availability-and-recovery/snapshots/snapshot-restore/index.md) of your Elasticsearch OSS 6.x or 7.x indexes, [create an OpenSearch cluster](../../install-and-configure/install-opensearch/index.md), restore the snapshot on the new cluster, and point your clients to the new host.

The snapshot approach can mean running two clusters in parallel, but lets you validate that the OpenSearch cluster is working in a way that meets your needs prior to modifying the Elasticsearch OSS cluster.

Elasticsearch OSS version | Snapshot migration path
:--- | :---
5.x | Upgrade to 5.6, then upgrade to 6.8. Reindex all 5.x indexes, make a snapshot, and restore in OpenSearch 1.x.
6.x | Make a snapshot and restore in OpenSearch 1.x
7.x | Make a snapshot and restore in OpenSearch 1.x or OpenSearch 2.x
