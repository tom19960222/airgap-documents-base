---
collection: ansible
version: "8"
title: "community.general.keycloak_authz_permission_info module – Query Keycloak client authorization permissions information"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/keycloak_authz_permission_info_module.html
fetched_at: 2026-07-28T01:47:09+00:00
---
# community.general.keycloak_authz_permission_info module – Query Keycloak client authorization permissions information

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
> To use it in a playbook, specify: `community.general.keycloak_authz_permission_info`.

New in community.general 7.2.0

- [Synopsis](keycloak_authz_permission_info_module.md#synopsis)
- [Parameters](keycloak_authz_permission_info_module.md#parameters)
- [Attributes](keycloak_authz_permission_info_module.md#attributes)
- [Examples](keycloak_authz_permission_info_module.md#examples)
- [Return Values](keycloak_authz_permission_info_module.md#return-values)

## [Synopsis](keycloak_authz_permission_info_module.md#id1)

- This module allows querying information about Keycloak client authorization permissions from the resources endpoint via the Keycloak REST API. Authorization permissions are only available if a client has Authorization enabled.
- This module requires access to the REST API via OpenID Connect; the user connecting and the realm being used must have the requisite access rights. In a default Keycloak installation, admin-cli and an admin user would work, as would a separate realm definition with the scope tailored to your needs and a user having the expected roles.
- The names of module options are snake_cased versions of the camelCase options used by Keycloak. The Authorization Services paths and payloads have not officially been documented by the Keycloak project. <https://www.puppeteers.net/blog/keycloak-authorization-services-rest-api-paths-and-payload/>

## [Parameters](keycloak_authz_permission_info_module.md#id2)

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
| **http_agent**  string  *added in community.general 5.4.0* | Configures the HTTP User-Agent header.  **Default:** `"Ansible"` |
| **name**  string / required | Name of the authorization permission to create. |
| **realm**  string / required | The name of the Keycloak realm the Keycloak client is in. |
| **token**  string  *added in community.general 3.0.0* | Authentication token for Keycloak API. |
| **validate_certs**  boolean | Verify TLS certificates (do not disable this in production).  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](keycloak_authz_permission_info_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](keycloak_authz_permission_info_module.md#id4)

```yaml+jinja
- name: Query Keycloak authorization permission
  community.general.keycloak_authz_permission_info:
    name: ScopePermission
    client_id: myclient
    realm: myrealm
    auth_keycloak_url: http://localhost:8080/auth
    auth_username: keycloak
    auth_password: keycloak
    auth_realm: master
```

## [Return Values](keycloak_authz_permission_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message as to what action was taken.  **Returned:** always |
| **queried_state**  complex | State of the resource (a policy) as seen by Keycloak.  **Returned:** on success |
| **config**  dictionary | Configuration of the permission (empty in all observed cases).  **Returned:** success  **Sample:** `{}` |
| **decisionStrategy**  string | The decision strategy.  **Returned:** success  **Sample:** `"UNANIMOUS"` |
| **description**  string | Description of the authorization permission.  **Returned:** success  **Sample:** `"Resource Permission"` |
| **id**  string | ID of the authorization permission.  **Returned:** success  **Sample:** `"9da05cd2-b273-4354-bbd8-0c133918a454"` |
| **logic**  string | The logic used for the permission (part of the payload, but has a fixed value).  **Returned:** success  **Sample:** `"POSITIVE"` |
| **name**  string | Name of the authorization permission.  **Returned:** success  **Sample:** `"ResourcePermission"` |
| **type**  string | Type of the authorization permission.  **Returned:** success  **Sample:** `"resource"` |

### Authors

- Samuli Seppänen (@mattock)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
