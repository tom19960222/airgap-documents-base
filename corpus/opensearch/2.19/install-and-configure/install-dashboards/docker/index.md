---
collection: "opensearch"
version: "2.19"
title: "Docker"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_install-and-configure/install-dashboards/docker.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_install-and-configure/install-dashboards/docker.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/install-and-configure/install-dashboards/docker/"
canonical_url: "https://docs.opensearch.org/latest/install-and-configure/install-dashboards/docker/"
canonical_route: "/install-and-configure/install-dashboards/docker/"
redirect_from: ["/dashboards/install/docker/","/opensearch/install/docker-security/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 1
parent: "Installing OpenSearch Dashboards"
---
# Run OpenSearch Dashboards using Docker

You *can* start OpenSearch Dashboards using `docker run` after [creating a Docker network](https://docs.docker.com/engine/reference/commandline/network_create/) and starting OpenSearch, but the process of connecting OpenSearch Dashboards to OpenSearch is significantly easier with a Docker Compose file.

1. Run `docker pull opensearchproject/opensearch-dashboards:2`.

1. Create a [`docker-compose.yml`](https://docs.docker.com/compose/compose-file/) file appropriate for your environment. A sample file that includes OpenSearch Dashboards is available on the OpenSearch [Docker installation page](../../install-opensearch/docker/index.md#sample-docker-composeyml).

   Just like `opensearch.yml`, you can pass a custom `opensearch_dashboards.yml` to the container in the Docker Compose file.
   {: .tip }

1. Run `docker compose up`.

   Wait for the containers to start. Then see the [OpenSearch Dashboards documentation](https://docs.opensearch.org/latest/dashboards/index/) <!-- unresolved-cross-corpus-link: collection=opensearch-dashboards route=/dashboards/ -->.

1. When finished, run `docker compose down`.
