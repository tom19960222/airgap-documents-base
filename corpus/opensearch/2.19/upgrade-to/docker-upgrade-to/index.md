---
collection: "opensearch"
version: "2.19"
title: "Migrating Docker clusters to OpenSearch"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_upgrade-to/docker-upgrade-to.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_upgrade-to/docker-upgrade-to.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/upgrade-to/docker-upgrade-to/"
canonical_url: "https://docs.opensearch.org/latest/migrate-or-upgrade/"
canonical_route: "/migrate-or-upgrade/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 25
---
# Migrating Docker clusters to OpenSearch

If you use a container orchestration system like Kubernetes (or manage your containers manually) and want to avoid downtime, think of the process not as an upgrade of each node, but as a decommissioning and replacement of each node. One by one, add OpenSearch nodes to the cluster and remove Elasticsearch OSS nodes, pointing to existing data volumes as necessary and allowing time for all indexes to return to a green status prior to proceeding.

If you use Docker Compose, we highly recommend that you perform what amounts to a [cluster restart upgrade](../upgrade-to/index.md). Update your cluster configuration with new images, new settings, and new environment variables, and test it. Then stop and start the cluster. This process requires downtime, but takes very few steps and lets you continue to treat the cluster as a single entity that you can reliably deploy and redeploy.

The most important step is to leave your data volumes intact. **Don't** run `docker compose down -v`.
