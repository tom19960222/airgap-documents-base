---
collection: "opensearch"
version: "2.19"
title: "OpenSearch Security for Security Analytics"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_security-analytics/security.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_security-analytics/security.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/security-analytics/security/"
canonical_url: "https://docs.opensearch.org/latest/security-analytics/security/"
canonical_route: "/security-analytics/security/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
layout: "default"
nav_order: 2
---
# OpenSearch Security for Security Analytics

You can use OpenSearch Security with Security Analytics to assign user permissions and manage the actions that users can and cannot perform. For example, you might want one group of users to be able to create, update, or delete detectors and another group of users to only view detectors. You may want still another group to be able to receive and acknowledge alerts but to be prevented from performing other tasks. The OpenSearch Security framework allows you to control the level of access users have to Security Analytics functionality.

---
## Security Analytics system indexes

Security Analytics indexes are protected as system indexes and treated differently than other indexes in a cluster. System indexes store configurations and other system settings and, for that reason, cannot be modified using the REST API or the OpenSearch Dashboards interface. Only a user with a TLS [admin certificate](../../security/configuration/tls/index.md#configuring-admin-certificates) can access system indexes. For more information about working with this type of index, see [System indexes](../../security/configuration/system-indices/index.md).

---
## Basic permissions

As an administrator, you can use OpenSearch Dashboards or the Security REST API to assign specific permissions to users based on the specific APIs they need to access. For a list of supported APIs, see [API tools](../api-tools/index.md).

OpenSearch Security has three built-in roles that cover most Security Analytics use cases: `security_analytics_full_access`, `security_analytics_read_access`, and `security_analytics_ack_alerts`. For descriptions of these and other roles, see [Predefined roles](../../security/access-control/users-roles/index.md#predefined-roles).

If these roles don't meet your needs, mix and match individual Security Analytics [permissions](../../security/access-control/permissions/index.md#security-analytics-permissions) to suit your use case. Each action corresponds to an operation in the REST API. For example, the `cluster:admin/opensearch/securityanalytics/detector/delete` permission allows you to delete detectors.

---
## (Advanced) Limit access by backend role

You can use backend roles to configure fine-grained access to individual detectors based on roles. For example, backend roles can be assigned to users working in different departments of an organization so that they can view only those detectors owned by the departments in which they work.

First, make sure your users have the appropriate [backend roles](../../security/access-control/index.md). Backend roles usually come from an [LDAP server](../../security/authentication-backends/ldap/index.md) or [SAML provider](../../security/authentication-backends/saml/index.md). However, if you use the internal user database, you can use the REST API to [add them manually](../../security/access-control/api/index.md#create-user).

Next, enable the following setting:

```json
PUT /_cluster/settings
{
  "transient": {
    "plugins.security_analytics.filter_by_backend_roles": "true"
  }
}
```

Now when users view Security Analytics resources in OpenSearch Dashboards (or make REST API calls), they only see detectors created by users who share at least one backend role.
For example, consider two users: `alice` and `bob`.

The following example assigns the user `alice` the `analyst` backend role:

```json
PUT /_plugins/_security/api/internalusers/alice
{
  "password": "alice",
  "backend_roles": [
    "analyst"
  ],
  "attributes": {}
}
```

The next example assigns the user `bob` the `human-resources` backend role:

```json
PUT /_plugins/_security/api/internalusers/bob
{
  "password": "bob",
  "backend_roles": [
    "human-resources"
  ],
  "attributes": {}
}
```

Finally, this last example assigns both `alice` and `bob` the role that gives them full access to Security Analytics:

```json
PUT /_plugins/_security/api/rolesmapping/security_analytics_full_access
{
  "backend_roles": [],
  "hosts": [],
  "users": [
    "alice",
    "bob"
  ]
}
```

However, because they have different backend roles, `alice` and `bob` cannot view each other's detectors or their results.

---
## A note on using fine-grained access control with the plugin

When a trigger generates an alert, the detector configurations, the alert itself, and any notifications that are sent to a channel may include metadata describing the index being queried. By design, the plugin must extract the data and store it as metadata outside of the index. [Document-level security](../../security/access-control/document-level-security/index.md) (DLS) and [field-level security](../../security/access-control/field-level-security/index.md) (FLS) access controls are designed to protect the data in the index. But once the data is stored outside the index as metadata, users with access to the detector and monitor configurations, alerts, and their notifications will be able to view this metadata and possibly infer the contents and quality of data in the index, which would otherwise be concealed by DLS and FLS access control.

To reduce the chances of unintended users viewing metadata that could describe an index, we recommend that administrators enable role-based access control and keep these kinds of design elements in mind when assigning permissions to the intended group of users. See [Limit access by backend role](#advanced-limit-access-by-backend-role) for more information.
