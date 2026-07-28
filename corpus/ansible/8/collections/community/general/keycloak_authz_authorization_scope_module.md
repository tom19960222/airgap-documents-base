---
collection: ansible
version: "8"
title: "community.general.keycloak_authz_authorization_scope module – Allows administration of Keycloak client authorization scopes via Keycloak API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/keycloak_authz_authorization_scope_module.html
fetched_at: 2026-07-28T01:47:07+00:00
---
# community.general.keycloak_authz_authorization_scope module – Allows administration of Keycloak client authorization scopes via Keycloak API

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
> To use it in a playbook, specify: `community.general.keycloak_authz_authorization_scope`.

New in community.general 6.6.0

- [Synopsis](keycloak_authz_authorization_scope_module.md#synopsis)
- [Parameters](keycloak_authz_authorization_scope_module.md#parameters)
- [Attributes](keycloak_authz_authorization_scope_module.md#attributes)
- [Examples](keycloak_authz_authorization_scope_module.md#examples)
- [Return Values](keycloak_authz_authorization_scope_module.md#return-values)

## [Synopsis](keycloak_authz_authorization_scope_module.md#id1)

- This module allows the administration of Keycloak client Authorization Scopes via the Keycloak REST API. Authorization Scopes are only available if a client has Authorization enabled.
- This module requires access to the REST API via OpenID Connect; the user connecting and the realm being used must have the requisite access rights. In a default Keycloak installation, admin-cli and an admin user would work, as would a separate realm definition with the scope tailored to your needs and a user having the expected roles.
- The names of module options are snake_cased versions of the camelCase options used by Keycloak. The Authorization Services paths and payloads have not officially been documented by the Keycloak project. <https://www.puppeteers.net/blog/keycloak-authorization-services-rest-api-paths-and-payload/>

## [Parameters](keycloak_authz_authorization_scope_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_client_id**  string | OpenID Connect `client_id` to authenticate to the API with.  **Default:** `"admin-cli"` |
| **auth_client_secret**  string | Client Secret to use in conjunction with `auth_client_id` (if required). |
| **auth_keycloak_url**  aliases: url  string / required | URL to the Keycloak instance. |
| **auth_password**  aliases: password  string | Password to authenticate for API access with. |
| **auth_realm**  string | Keycloak realm name to authenticate to for API access. |
| **auth_username**  aliases: username  string | Username to authenticate for API access with. |
| **client_id**  string / required | The `clientId` of the Keycloak client that should have the authorization scope.  This is usually a human-readable name of the Keycloak client. |
| **connection_timeout**  integer  *added in community.general 4.5.0* | Controls the HTTP connections timeout period (in seconds) to Keycloak API.  **Default:** `10` |
| **display_name**  string | The display name of the authorization scope. |
| **http_agent**  string  *added in community.general 5.4.0* | Configures the HTTP User-Agent header.  **Default:** `"Ansible"` |
| **icon_uri**  string | The icon URI for the authorization scope. |
| **name**  string / required | Name of the authorization scope to create. |
| **realm**  string / required | The name of the Keycloak realm the Keycloak client is in. |
| **state**  string | State of the authorization scope.  On `present`, the authorization scope will be created (or updated if it exists already).  On `absent`, the authorization scope will be removed if it exists.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **token**  string  *added in community.general 3.0.0* | Authentication token for Keycloak API. |
| **validate_certs**  boolean | Verify TLS certificates (do not disable this in production).  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](keycloak_authz_authorization_scope_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](keycloak_authz_authorization_scope_module.md#id4)

```yaml+jinja
- name: Manage Keycloak file:delete authorization scope
  keycloak_authz_authorization_scope:
    name: file:delete
    state: present
    display_name: File delete
    client_id: myclient
    realm: myrealm
    auth_keycloak_url: http://localhost:8080/auth
    auth_username: keycloak
    auth_password: keycloak
    auth_realm: master
```

## [Return Values](keycloak_authz_authorization_scope_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **end_state**  complex | Representation of the authorization scope after module execution.  **Returned:** on success |
| **display_name**  string | Display name of the authorization scope.  **Returned:** when `state=present`  **Sample:** `"File delete"` |
| **icon_uri**  string | Icon URI for the authorization scope.  **Returned:** when `state=present`  **Sample:** `"http://localhost/icon.png"` |
| **id**  string | ID of the authorization scope.  **Returned:** when `state=present`  **Sample:** `"a6ab1cf2-1001-40ec-9f39-48f23b6a0a41"` |
| **name**  string | Name of the authorization scope.  **Returned:** when `state=present`  **Sample:** `"file:delete"` |
| **msg**  string | Message as to what action was taken.  **Returned:** always |

### Authors

- Samuli Seppänen (@mattock)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
