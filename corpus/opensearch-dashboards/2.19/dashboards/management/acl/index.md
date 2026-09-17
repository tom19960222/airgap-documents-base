---
collection: "opensearch-dashboards"
version: "2.19"
title: "Access control lists for saved objects"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_dashboards/management/acl.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_dashboards/management/acl.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/dashboards/management/acl/"
canonical_url: "https://docs.opensearch.org/latest/dashboards/management/acl/"
canonical_route: "/dashboards/management/acl/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.1"
chart_version: ""
layout: "default"
nav_order: 50
parent: "Dashboards Management"
---
# Access control lists for saved objects
Introduced 2.18
{: .label .label-purple }

You can use access control lists (ACLs) to manage permissions for your saved objects, providing authorization (AuthZ) capabilities without requiring backend plugin integration.

## Understanding ACL types

ACLs are applied at two levels:

1. **Workspace ACL:** Workspace objects inherit permissions from their parent workspace. See [Workspace ACL](../../workspace/workspace-acl/index.md) for more information.
2. **Objects ACL:** Each individual object can have its own ACL policy. All operations on these objects must pass ACL policy validation.

## Enabling the ACL feature

The ACL feature must be enabled before you can define any access controls. Enable it by:

1. Opening your `opensearch_dashboards.yml` file.
2. Enabling permissions with `savedObjects.permission.enabled: true`.

## Defining ACL permissions

ACL permissions are defined using the following schema:

```json
{
  "permissions": {
    "<permission_type_1>": {
        "users": ["<principal_1>", "<principal_2>"],
        "groups": ["<principal_3>", "<principal_4>"]
    }
  }
}
```

### Granting permissions to authenticated users

The wildcard character (`*`) grants permissions to all authenticated users. In the following example, the ACL grants workspace management permissions to the `finance_manager` group and dashboard creation permissions to the `finance_analyst` group:

```json
{
  "permissions": {
    "write": {
        "groups": ["finance_manager"]
    },
    "library_write": {
        "groups": ["finance_analyst"]
    }
  }
}
```

### Configuring mixed-level permissions

To allow one user, `user-1` for example, to modify an object while giving read-only access to others, you can configure the ACL policy as follows:

```json
{
  "permissions": {
    "read": {
        "users": ["*"]
    },
    "write": {
        "users": ["user-1"]
    },
  }
}
```
