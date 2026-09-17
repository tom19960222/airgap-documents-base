---
collection: "opensearch"
version: "2.19"
title: "Configuration and system settings"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_install-and-configure/configuring-opensearch/configuration-system.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_install-and-configure/configuring-opensearch/configuration-system.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/install-and-configure/configuring-opensearch/configuration-system/"
canonical_url: "https://docs.opensearch.org/latest/install-and-configure/configuring-opensearch/configuration-system/"
canonical_route: "/install-and-configure/configuring-opensearch/configuration-system/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 10
parent: "Configuring OpenSearch"
---
# Configuration and system settings

For an overview of creating an OpenSearch cluster and examples of configuration settings, see [Creating a cluster](../../../tuning-your-cluster/index.md). To learn more about static and dynamic settings, see [Configuring OpenSearch](../index.md).

OpenSearch supports the following system settings:

- `cluster.name` (Static, string): The cluster name.

- `node.name` (Static, string): A descriptive name for the node.

- `node.roles` (Static, list): Defines one or more roles for an OpenSearch node. Valid values are `cluster_manager`, `data`, `ingest`, `search`, `ml`, `remote_cluster_client`, and `coordinating_only`.

- `path.data` (Static, string): A path to the directory where your data is stored. Separate multiple locations with commas.

- `path.logs` (Static, string): A path to log files.

- `bootstrap.memory_lock` (Static, Boolean): Locks the memory at startup. We recommend setting the heap size to about half the memory available on the system and that the owner of the process is allowed to use this limit. OpenSearch doesn't perform well when the system is swapping the memory.
