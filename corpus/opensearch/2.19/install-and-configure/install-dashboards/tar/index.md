---
collection: "opensearch"
version: "2.19"
title: "Tarball"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_install-and-configure/install-dashboards/tar.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_install-and-configure/install-dashboards/tar.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/install-and-configure/install-dashboards/tar/"
canonical_url: "https://docs.opensearch.org/latest/install-and-configure/install-dashboards/tar/"
canonical_route: "/install-and-configure/install-dashboards/tar/"
redirect_from: ["/dashboards/install/tar/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 30
parent: "Installing OpenSearch Dashboards"
---
# Run OpenSearch Dashboards using the tarball

1. Download the tarball from the [OpenSearch downloads page](https://opensearch.org/downloads.html){:target='\_blank'}.

1. Extract the TAR file to a directory and change to that directory:

   ```bash
   # x64
   tar -zxf opensearch-dashboards-2.19.3-linux-x64.tar.gz
   cd opensearch-dashboards
   # ARM64
   tar -zxf opensearch-dashboards-2.19.3-linux-arm64.tar.gz
   cd opensearch-dashboards
   ```

1. If desired, modify `config/opensearch_dashboards.yml`.

1. Run OpenSearch Dashboards:

   ```bash
   ./bin/opensearch-dashboards
   ```
