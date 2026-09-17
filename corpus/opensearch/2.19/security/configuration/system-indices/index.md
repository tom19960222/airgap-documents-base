---
collection: "opensearch"
version: "2.19"
title: "System indexes"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_security/configuration/system-indices.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_security/configuration/system-indices.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/security/configuration/system-indices/"
canonical_url: "https://docs.opensearch.org/latest/security/configuration/system-indices/"
canonical_route: "/security/configuration/system-indices/"
redirect_from: ["/security-plugin/configuration/system-indices/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 4
parent: "Configuration"
---
# System indexes

By default, OpenSearch has a protected system index, `.opendistro_security`, which is used to store the Security configuration YAML files. You create this index using [securityadmin.sh](../security-admin/index.md). Even with a user account that has read permissions for all indexes, you can't directly access the data in this system index.

Instead, you first need to authenticate with an [admin certificate](../tls/index.md#configuring-admin-certificates) to gain access:

```bash
curl -k --cert ./kirk.pem --key ./kirk-key.pem -XGET 'https://localhost:9200/.opendistro_security/_search'
```

When Security is installed, the demo configuration automatically creates the `.opendistro_security` system index. It also adds several other indexes for the various OpenSearch plugins that integrate with the Security plugin:

```yml
plugins.security.system_indices.enabled: true
plugins.security.system_indices.indices: [".opendistro-alerting-config", ".opendistro-alerting-alert*", ".opendistro-anomaly-results*", ".opendistro-anomaly-detector*", ".opendistro-anomaly-checkpoints", ".opendistro-anomaly-detection-state", ".opendistro-reports-*", ".opendistro-notifications-*", ".opendistro-notebooks", ".opendistro-asynchronous-search-response*"]
```

You can add additional system indexes in `opensearch.yml`. An alternative way to remove a system index is to delete it from the `plugins.security.system_indices.indices` list on each node and restart OpenSearch.
