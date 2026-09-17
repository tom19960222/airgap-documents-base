---
collection: "opensearch"
version: "2.19"
title: "Access control"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_security/access-control/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_security/access-control/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/security/access-control/"
canonical_url: "https://docs.opensearch.org/latest/security/access-control/index/"
canonical_route: "/security/access-control/"
redirect_from: ["/security-plugin/access-control/index/","/security/access-control/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 75
---
# Access control

After you [configure the Security plugin](../configuration/index.md) to use your own certificates and preferred authentication backend, you can start adding users, creating roles, and mapping roles to users.

This section of the documentation covers what a user is allowed to see and do after successfully authenticating.

## Concepts

Term | Description
:--- | :---
Permission | An individual action, such as creating an index (e.g. `indices:admin/create`). For a complete list, see [Permissions](permissions/index.md).
Action group | A set of permissions. For example, the predefined `SEARCH` action group authorizes roles to use the `_search` and `_msearch` APIs.
Role | Security roles define the scope of a permission or action group: cluster, index, document, or field. For example, a role named `delivery_analyst` might have no cluster permissions, the `READ` action group for all indexes that match the `delivery-data-*` pattern, access to all document types within those indexes, and access to all fields except `delivery_driver_name`.
Backend role | (Optional) A backend role is a specific identifier assigned to a user or group of users by an external authentication system such as LDAP/Active Directory. Instead of mapping permissions to individual users, you can assign these permissions to backend roles, which can significantly streamline the role mapping process. For example, if 100 users within an organization share a common function, they can all be assigned the same backend role. With this approach you only need to map the role to the backend role identifier, rather than map to each user individually.
User | Users make requests to OpenSearch clusters. A user has credentials (e.g. a username and password), zero or more backend roles, and zero or more custom attributes.
Role mapping | Users assume roles after they successfully authenticate. Role mappings map roles to users (or backend roles). For example, a mapping of `kibana_user` (role) to `jdoe` (user) means that John Doe gains all the permissions of `kibana_user` after authenticating. Likewise, a mapping of `all_access` (role) to `admin` (backend role) means that any user with the backend role of `admin` gains all the permissions of `all_access` after authenticating. You can map each role to multiple users and/or backend roles.

The Security plugin comes with a number of [predefined action groups](default-action-groups/index.md), roles, mappings, and users. These entities serve as sensible defaults and are good examples of how to use the plugin.
