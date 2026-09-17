---
collection: "opensearch"
version: "2.19"
title: "Index management security"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_im-plugin/security.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_im-plugin/security.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/im-plugin/security/"
canonical_url: "https://docs.opensearch.org/latest/im-plugin/security/"
canonical_route: "/im-plugin/security/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
layout: "default"
nav_order: 40
---
# Index management security

Using the Security plugin with index management lets you limit non-admin users to certain actions. For example, you might want to set up your security such that a group of users can only read ISM policies, while others can create, delete, or change policies.

All index management data are protected as system indexes, and only a super admin or an admin with a Transport Layer Security (TLS) certificate can access system indexes. For more information, see [System indexes](../../security/configuration/system-indices/index.md).

## Basic permissions

The Security plugin comes with one role that offers full access to index management: `index_management_full_access`. For a description of the role's permissions, see [Predefined roles](../../security/access-control/users-roles/index.md#predefined-roles).

With security enabled, users not only need the correct index management permissions, but they also need permissions to execute actions to involved indexes. For example, if a user wants to use the REST API to attach a policy that executes a rollup job to an index named `system-logs`, they would need the permissions to attach a policy and execute a rollup job, as well as access to `system-logs`.

Finally, with the exceptions of Create Policy, Get Policy, and Delete Policy, users also need the `indices:admin/opensearch/ism/managedindex` permission to execute [ISM APIs](../ism/api/index.md).

## (Advanced) Limit access by backend role

You can use backend roles to configure fine-grained access to index management policies and actions. For example, users of different departments in an organization might view different policies depending on what roles and permissions they are assigned.

First, ensure your users have the appropriate [backend roles](../../security/access-control/index.md). Backend roles usually come from an [LDAP server](../../security/authentication-backends/ldap/index.md) or [SAML provider](../../security/authentication-backends/saml/index.md). However, if you use the internal user database, you can use the REST API to [add them manually](../../security/access-control/api/index.md#create-user).

Use the REST API to enable the following setting:

```json
PUT _cluster/settings
{
  "transient": {
    "plugins.index_management.filter_by_backend_roles": "true"
  }
}
```

With security enabled, only users who share at least one backend role can see and execute the policies and actions relevant to their roles.

For example, consider a scenario with three users: `John` and `Jill`, who have the backend role `helpdesk_staff`, and `Jane`, who has the backend role `phone_operator`. `John` wants to create a policy that performs a rollup job on an index named `airline_data`, so `John` would need a backend role that has permissions to access that index, create relevant policies, and execute relevant actions, and `Jill` would be able to access the same index, policy, and job. However, `Jane` cannot access or edit those resources or actions.
