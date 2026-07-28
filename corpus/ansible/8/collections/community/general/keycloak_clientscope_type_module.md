---
collection: ansible
version: "8"
title: "community.general.keycloak_clientscope_type module – Set the type of aclientscope in realm or client via Keycloak API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/keycloak_clientscope_type_module.html
fetched_at: 2026-07-28T01:47:13+00:00
---
# community.general.keycloak_clientscope_type module – Set the type of aclientscope in realm or client via Keycloak API

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
> To use it in a playbook, specify: `community.general.keycloak_clientscope_type`.

New in community.general 6.6.0

- [Synopsis](keycloak_clientscope_type_module.md#synopsis)
- [Parameters](keycloak_clientscope_type_module.md#parameters)
- [Attributes](keycloak_clientscope_type_module.md#attributes)
- [Examples](keycloak_clientscope_type_module.md#examples)
- [Return Values](keycloak_clientscope_type_module.md#return-values)

## [Synopsis](keycloak_clientscope_type_module.md#id1)

- This module allows you to set the type (optional, default) of clientscopes via the Keycloak REST API. It requires access to the REST API via OpenID Connect; the user connecting and the client being used must have the requisite access rights. In a default Keycloak installation, admin-cli and an admin user would work, as would a separate client definition with the scope tailored to your needs and a user having the expected roles.

## [Parameters](keycloak_clientscope_type_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_client_id**  string | OpenID Connect `client_id` to authenticate to the API with.  **Default:** `"admin-cli"` |
| **auth_client_secret**  string | Client Secret to use in conjunction with `auth_client_id` (if required). |
| **auth_keycloak_url**  aliases: url  string / required | URL to the Keycloak instance. |
| **auth_password**  aliases: password  string | Password to authenticate for API access with. |
| **auth_realm**  string | Keycloak realm name to authenticate to for API access. |
| **auth_username**  aliases: username  string | Username to authenticate for API access with. |
| **client_id**  aliases: clientId  string | The `client_id` of the client. If not set the clientscop types are set as a default for the realm. |
| **connection_timeout**  integer  *added in community.general 4.5.0* | Controls the HTTP connections timeout period (in seconds) to Keycloak API.  **Default:** `10` |
| **default_clientscopes**  list / elements=string | Client scopes that should be of type default. |
| **http_agent**  string  *added in community.general 5.4.0* | Configures the HTTP User-Agent header.  **Default:** `"Ansible"` |
| **optional_clientscopes**  list / elements=string | Client scopes that should be of type optional. |
| **realm**  string | The Keycloak realm.  **Default:** `"master"` |
| **token**  string  *added in community.general 3.0.0* | Authentication token for Keycloak API. |
| **validate_certs**  boolean | Verify TLS certificates (do not disable this in production).  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](keycloak_clientscope_type_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](keycloak_clientscope_type_module.md#id4)

```yaml+jinja
- name: Set default client scopes on realm level
  community.general.keycloak_clientscope_type:
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
    realm: "MyCustomRealm"
    default_clientscopes: ['profile', 'roles']
  delegate_to: localhost

- name: Set default and optional client scopes on client level with token auth
  community.general.keycloak_clientscope_type:
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    token: TOKEN
    realm: "MyCustomRealm"
    client_id: "MyCustomClient"
    default_clientscopes: ['profile', 'roles']
    optional_clientscopes: ['phone']
  delegate_to: localhost
```

## [Return Values](keycloak_clientscope_type_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **end_state**  dictionary | Representation of client scopes after module execution.  The sample is truncated.  **Returned:** on success  **Sample:** `{"default_clientscopes": ["profile", "role"], "optional_clientscopes": []}` |
| **existing**  dictionary | Representation of client scopes before module execution.  **Returned:** always  **Sample:** `{"default_clientscopes": ["profile", "role"], "optional_clientscopes": ["phone"]}` |
| **msg**  string | Message as to what action was taken.  **Returned:** always  **Sample:** `""` |
| **proposed**  dictionary | Representation of proposed client-scope types mapping.  **Returned:** always  **Sample:** `{"default_clientscopes": ["profile", "role"], "optional_clientscopes": []}` |

### Authors

- Simon Pahl (@simonpahl)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
