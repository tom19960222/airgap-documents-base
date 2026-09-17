---
collection: "opensearch"
version: "2.19"
title: "Install and upgrade OpenSearch"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_install-and-configure/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_install-and-configure/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/install-and-configure/"
canonical_url: "https://docs.opensearch.org/latest/install-and-configure/"
canonical_route: "/install-and-configure/"
redirect_from: ["/install-and-configure/index/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
has_toc: false
layout: "default"
nav_exclude: true
nav_order: 1
---
# Install and upgrade OpenSearch

OpenSearch and OpenSearch Dashboards are available on any compatible host that supports Docker (such as Linux, MacOS, or Windows). Additionally, you can install both products on various Linux distributions and on Windows.

[Download OpenSearch](https://opensearch.org/downloads.html) for your preferred platform and then choose one of the following installation guides.

| OpenSearch | OpenSearch Dashboards |
| :--- | :--- |
| [Docker](install-opensearch/docker/index.md) | [Docker](install-dashboards/docker/index.md) |
| [Helm](install-opensearch/helm/index.md) | [Helm](install-dashboards/helm/index.md) |
| [Tarball](install-opensearch/tar/index.md) | [Tarball](install-dashboards/tar/index.md) |
| [RPM](install-opensearch/rpm/index.md) | [RPM](install-dashboards/rpm/index.md) |
| [Debian](install-opensearch/debian/index.md) | [Debian](install-dashboards/debian/index.md) |
| [Ansible playbook](install-opensearch/ansible/index.md) | |
| [Windows](install-opensearch/windows/index.md) | [Windows](install-dashboards/windows/index.md) |

After you've installed OpenSearch, learn about [configuring](configuring-opensearch/index.md) it for your deployment.

For more information about upgrading your OpenSearch cluster, see the [upgrade guide](upgrade-opensearch/index.md).

For information about upgrade tools, see [OpenSearch upgrade, migration, and comparison tools](../tools/index.md#opensearch-upgrade-migration-and-comparison-tools).

For plugin installation, see [Installing plugins](plugins/index.md).
