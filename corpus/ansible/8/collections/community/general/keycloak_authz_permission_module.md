---
collection: ansible
version: "8"
title: "community.general.keycloak_authz_permission module – Allows administration of Keycloak client authorization permissions via Keycloak API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/keycloak_authz_permission_module.html
fetched_at: 2026-07-28T01:47:09+00:00
---
# community.general.keycloak_authz_permission module – Allows administration of Keycloak client authorization permissions via Keycloak API

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.keycloak_authz_permission`.

New in community.general 7.2.0

- [Synopsis](keycloak_authz_permission_module.md#synopsis)
- [Parameters](keycloak_authz_permission_module.md#parameters)
- [Attributes](keycloak_authz_permission_module.md#attributes)
- [Examples](keycloak_authz_permission_module.md#examples)
- [Return Values](keycloak_authz_permission_module.md#return-values)

## [Synopsis](keycloak_authz_permission_module.md#id1)

- This module allows the administration of Keycloak client authorization permissions via the Keycloak REST API. Authorization permissions are only available if a client has Authorization enabled.
- There are some peculiarities in JSON paths and payloads for authorization permissions. In particular POST and PUT operations are targeted at permission endpoints, whereas GET requests go to policies endpoint. To make matters more interesting the JSON responses from GET requests return data in a different format than what is expected for POST and PUT. The end result is that it is not possible to detect changes to things like policies, scopes or resources - at least not without a large number of additional API calls. Therefore this module always updates authorization permissions instead of attempting to determine if changes are truly needed.
- This module requires access to the REST API via OpenID Connect; the user connecting and the realm being used must have the requisite access rights. In a default Keycloak installation, admin-cli and an admin user would work, as would a separate realm definition with the scope tailored to your needs and a user having the expected roles.
- The names of module options are snake_cased versions of the camelCase options used by Keycloak. The Authorization Services paths and payloads have not officially been documented by the Keycloak project. <https://www.puppeteers.net/blog/keycloak-authorization-services-rest-api-paths-and-payload/>

## [Parameters](keycloak_authz_permission_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_client_id**  string | OpenID Connect `client_id` to authenticate to the API with.  **Default:** `"admin-cli"` |
| **auth_client_secret**  string | Client Secret to use in conjunction with `auth_client_id` (if required). |
| **auth_keycloak_url**  aliases: url  string / required | URL to the Keycloak instance. |
| **auth_password**  aliases: password  string | Password to authenticate for API access with. |
| **auth_realm**  string | Keycloak realm name to authenticate to for API access. |
| **auth_username**  aliases: username  string | Username to authenticate for API access with. |
| **client_id**  string / required | The clientId of the keycloak client that should have the authorization scope.  This is usually a human-readable name of the Keycloak client. |
| **connection_timeout**  integer  *added in community.general 4.5.0* | Controls the HTTP connections timeout period (in seconds) to Keycloak API.  **Default:** `10` |
| **decision_strategy**  string | The decision strategy to use with this permission.  **Choices:**   - `"UNANIMOUS"` ← (default) - `"AFFIRMATIVE"` - `"CONSENSUS"` |
| **description**  string | The description of the authorization permission. |
| **http_agent**  string  *added in community.general 5.4.0* | Configures the HTTP User-Agent header.  **Default:** `"Ansible"` |
| **name**  string / required | Name of the authorization permission to create. |
| **permission_type**  string / required | The type of authorization permission.  On `scope` create a scope-based permission.  On `resource` create a resource-based permission.  **Choices:**   - `"resource"` - `"scope"` |
| **policies**  list / elements=string | Policy names to attach to this permission.  **Default:** `[]` |
| **realm**  string / required | The name of the Keycloak realm the Keycloak client is in. |
| **resources**  list / elements=string | Resource names to attach to this permission.  Scope-based permissions can only include one resource.  Resource-based permissions can include multiple resources.  **Default:** `[]` |
| **scopes**  list / elements=string | Scope names to attach to this permission.  Resource-based permissions cannot have scopes attached to them.  **Default:** `[]` |
| **state**  string | State of the authorization permission.  On `present`, the authorization permission will be created (or updated if it exists already).  On `absent`, the authorization permission will be removed if it exists.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **token**  string  *added in community.general 3.0.0* | Authentication token for Keycloak API. |
| **validate_certs**  boolean | Verify TLS certificates (do not disable this in production).  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](keycloak_authz_permission_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](keycloak_authz_permission_module.md#id4)

```yaml+jinja
- name: Manage scope-based Keycloak authorization permission
  community.general.keycloak_authz_permission:
    name: ScopePermission
    state: present
    description: Scope permission
    permission_type: scope
    scopes:
      - file:delete
    policies:
      - Default Policy
    client_id: myclient
    realm: myrealm
    auth_keycloak_url: http://localhost:8080/auth
    auth_username: keycloak
    auth_password: keycloak
    auth_realm: master

- name: Manage resource-based Keycloak authorization permission
  community.general.keycloak_authz_permission:
    name: ResourcePermission
    state: present
    description: Resource permission
    permission_type: resource
    resources:
      - Default Resource
    policies:
      - Default Policy
    client_id: myclient
    realm: myrealm
    auth_keycloak_url: http://localhost:8080/auth
    auth_username: keycloak
    auth_password: keycloak
    auth_realm: master
```

## [Return Values](keycloak_authz_permission_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **end_state**  complex | Representation of the authorization permission after module execution.  **Returned:** on success |
| **decisionStrategy**  string | The decision strategy to use.  **Returned:** when `state=present`  **Sample:** `"UNANIMOUS"` |
| **description**  string | Description of the authorization permission.  **Returned:** when `state=present`  **Sample:** `"Resource Permission"` |
| **id**  string | ID of the authorization permission.  **Returned:** when `state=present`  **Sample:** `"9da05cd2-b273-4354-bbd8-0c133918a454"` |
| **logic**  string | The logic used for the permission (part of the payload, but has a fixed value).  **Returned:** when `state=present`  **Sample:** `"POSITIVE"` |
| **name**  string | Name of the authorization permission.  **Returned:** when `state=present`  **Sample:** `"ResourcePermission"` |
| **policies**  list / elements=string | IDs of policies attached to this permission.  **Returned:** when `state=present`  **Sample:** `["9da05cd2-b273-4354-bbd8-0c133918a454"]` |
| **resources**  list / elements=string | IDs of resources attached to this permission.  **Returned:** when `state=present`  **Sample:** `["49e052ff-100d-4b79-a9dd-52669ed3c11d"]` |
| **scopes**  list / elements=string | IDs of scopes attached to this permission.  **Returned:** when `state=present`  **Sample:** `["9da05cd2-b273-4354-bbd8-0c133918a454"]` |
| **type**  string | Type of the authorization permission.  **Returned:** when `state=present`  **Sample:** `"resource"` |
| **msg**  string | Message as to what action was taken.  **Returned:** always |

### Authors

- Samuli Seppänen (@mattock)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
