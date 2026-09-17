---
collection: "opensearch"
version: "2.19"
title: "Observability security"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_observing-your-data/observability-security.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_observing-your-data/observability-security.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/observing-your-data/observability-security/"
canonical_url: "https://docs.opensearch.org/latest/observing-your-data/observability-security/"
canonical_route: "/observing-your-data/observability-security/"
redirect_from: ["/observing-your-data/security/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
layout: "default"
nav_order: 5
---
# Observability security

You can use the Security plugin with Observability in OpenSearch to limit non-admin users to specific actions. For example, you might want some users to only view visualizations, notebooks, and other Observability objects, while others can create and modify them.

## Basic permissions

The Security plugin has two built-in roles that cover most Observability use cases: `observability_full_access` and `observability_read_access`. For descriptions of each, see [Predefined roles](../../security/access-control/users-roles/index.md#predefined-roles). If you don't see these predefined roles in OpenSearch Dashboards, you can create them with the following commands:

```json
PUT _plugins/_security/api/roles/observability_read_access
{
  "cluster_permissions": [
    "cluster:admin/opensearch/observability/get"
  ]
}
```

```json
PUT _plugins/_security/api/roles/observability_full_access
{
  "cluster_permissions": [
    "cluster:admin/opensearch/observability/*"
  ]
}
```

If these roles don't meet your needs, mix and match individual Observability [permissions](../../security/access-control/permissions/index.md) to suit your use case. For example, the `cluster:admin/opensearch/observability/create` permission lets you create Observability objects (visualizations, operational panels, notebooks, etc.).

The following is an example role that provides access to Observability:

```json
PUT _plugins/_security/api/roles/observability_permissions
{
  "cluster_permissions": [
    "cluster:admin/opensearch/observability/create",
    "cluster:admin/opensearch/observability/update",
    "cluster:admin/opensearch/observability/delete",
    "cluster:admin/opensearch/observability/get"
    ],
  "index_permissions": [{
    "index_patterns": [".opensearch-observability"],
    "allowed_actions": ["write", "read", "search"]
  }],
  "tenant_permissions": [{
    "tenant_patterns": ["global_tenant"],
    "allowed_actions": ["opensearch_dashboards_all_write"]
  }]
}
```
