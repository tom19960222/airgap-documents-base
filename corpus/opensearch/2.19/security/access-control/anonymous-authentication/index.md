---
collection: "opensearch"
version: "2.19"
title: "Anonymous authentication"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_security/access-control/anonymous-authentication.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_security/access-control/anonymous-authentication.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/security/access-control/anonymous-authentication/"
canonical_url: "https://docs.opensearch.org/latest/security/access-control/anonymous-authentication/"
canonical_route: "/security/access-control/anonymous-authentication/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 145
parent: "Access control"
---
# Anonymous authentication

The Security plugin supports anonymous authentication, through which a user is able to access a cluster without providing credentials. This is useful in cases where you want lots of people to be able to access your cluster with a common set of privileges.

## Configuration

To enable anonymous authentication, you need to modify the `config.yml` file inside the `opensearch-security` configuration subdirectory of your cluster.

In the `config.yml` file, there is an `http` section, which includes the `anonymous_auth_enabled` setting:

```yml
http:
  anonymous_auth_enabled: <true|false>
  ...
```

The following table describes the `anonymous_auth_enabled` setting. For more information, see the [configuration](../../configuration/configuration/index.md) file overview.

| Setting | Description                                                                                                                                                                                                                                                                                   |
| :--- |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `anonymous_auth_enabled` | Either enables or disables anonymous authentication. When you enable anonymous authentication, all defined HTTP authenticators are non-challenging. See [The challenge setting](../../authentication-backends/basic-authc/index.md#the-challenge-setting). |

If you disable anonymous authentication, you must provide at least one `authc` in order for the Security plugin to initialize successfully.
{: .important }

## OpenSearch Dashboards configuration

To enable anonymous authentication for OpenSearch Dashboards, you need to modify the `opensearch_dashboards.yml` file in the configuration directory of your OpenSearch Dashboards installation.

Add the following setting to `opensearch_dashboards.yml`:

```yml
opensearch_security.auth.anonymous_auth_enabled: true
```

Anonymous login for OpenSearch Dashboards requires anonymous authentication to be enabled on the OpenSearch cluster.
{: .important}

## Defining anonymous authentication privileges

When anonymous authentication is enabled, your defined HTTP authenticators still try to find user credentials inside your HTTP request. If credentials are found, the user is authenticated. If none are found, the user is authenticated as an `anonymous` user.

All anonymous users have the username `anonymous` and a single role named `anonymous_backendrole`.

You can configure the privileges associated with the `opendistro_security_anonymous_backendrole` in the [roles.yml](../users-roles/index.md) file.

We recommend that your defined role have very limited privileges. Generally, an anonymous user should **never** be able to write to your cluster.
{: .important}

The following is an example role definition for an `anonymous_users_role`. You can use this example as a reference for defining your own role in the `roles.yml` file:

```yaml
anonymous_users_role:
  reserved: false
  hidden: false
  cluster_permissions:
  - "OPENDISTRO_SECURITY_CLUSTER_COMPOSITE_OPS"
  index_permissions:
  - index_patterns:
    - "public_index_*"
    allowed_actions:
    - "read"
```

Then, in the `roles_mapping.yml` file, you can define the appropriate mapping for this new role:

```yaml
anonymous_users_role:
  reserved: false
  hidden: false
  backend_roles: ["opendistro_security_anonymous_backendrole"]
  hosts: []
```

Notice that the role is mapped to `opendistro_security_anonymous_backendrole`, which means that all users with the anonymous user backend role will have these privileges.

Alternatively, you can complete these steps using the REST API or OpenSearch Dashboards.
