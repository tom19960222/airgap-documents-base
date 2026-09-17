---
collection: "opensearch"
version: "2.19"
title: "Upgrading OpenSearch"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_upgrade-to/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_upgrade-to/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/upgrade-to/"
canonical_url: "https://docs.opensearch.org/latest/migrate-or-upgrade/"
canonical_route: "/migrate-or-upgrade/"
redirect_from: ["/upgrade-to/index/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_exclude: true
nav_order: 1
---
# Upgrading OpenSearch

The process of upgrading your OpenSearch version varies depending on your current version of OpenSearch, installation type, tolerance for downtime, and cost-sensitivity. For migrating to OpenSearch, we provide a [Migration Assistant](https://docs.opensearch.org/latest/migration-assistant/) <!-- unresolved-jekyll-link: route=/migration-assistant/ -->.

Two upgrade approaches exists:

- Perform a [restart upgrade or a rolling upgrade](snapshot-migrate/index.md) on your existing nodes. A restart upgrade involves upgrading the entire cluster and restarting it, whereas a rolling upgrade requires upgrading and restarting nodes in the cluster one by one.
- Replace existing OpenSearch nodes with new OpenSearch nodes. Node replacement is most popular when upgrading [Docker clusters](docker-upgrade-to/index.md).

Regardless of your approach, to safeguard against data loss, we recommend that you take a [snapshot](../tuning-your-cluster/availability-and-recovery/snapshots/snapshot-restore/index.md) of all indexes prior to any migration.

If your existing clients include a version check, such as recent versions of Logstash OSS and Filebeat OSS, [check compatibility](../tools/index.md#compatibility-matrices) before upgrading.

For more information about OpenSearch migration tools, see [OpenSearch upgrade, migration, and comparison tools](../tools/index.md#opensearch-upgrade-migration-and-comparison-tools).

## Upgrading from Open Distro

For steps to upgrade from Open Distro to OpenSearch, refer to the blog post [How To: Upgrade from Open Distro to OpenSearch](https://opensearch.org/blog/technical-posts/2021/07/how-to-upgrade-from-opendistro-to-opensearch/).
