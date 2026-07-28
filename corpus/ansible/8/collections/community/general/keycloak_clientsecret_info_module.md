---
collection: ansible
version: "8"
title: "community.general.keycloak_clientsecret_info module – Retrieve client secret via Keycloak API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/keycloak_clientsecret_info_module.html
fetched_at: 2026-07-28T01:47:13+00:00
---
# community.general.keycloak_clientsecret_info module – Retrieve client secret via Keycloak API

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
> To use it in a playbook, specify: `community.general.keycloak_clientsecret_info`.

New in community.general 6.1.0

- [Synopsis](keycloak_clientsecret_info_module.md#synopsis)
- [Parameters](keycloak_clientsecret_info_module.md#parameters)
- [Attributes](keycloak_clientsecret_info_module.md#attributes)
- [Examples](keycloak_clientsecret_info_module.md#examples)
- [Return Values](keycloak_clientsecret_info_module.md#return-values)

## [Synopsis](keycloak_clientsecret_info_module.md#id1)

- This module allows you to get a Keycloak client secret via the Keycloak REST API. It requires access to the REST API via OpenID Connect; the user connecting and the client being used must have the requisite access rights. In a default Keycloak installation, admin-cli and an admin user would work, as would a separate client definition with the scope tailored to your needs and a user having the expected roles.
- When retrieving a new client secret, where possible provide the client’s `id` (not `client_id`) to the module. This removes a lookup to the API to translate the `client_id` into the client ID.
- Note that this module returns the client secret. To avoid this showing up in the logs, please add `no_log: true` to the task.

## [Parameters](keycloak_clientsecret_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_client_id**  string | OpenID Connect `client_id` to authenticate to the API with.  **Default:** `"admin-cli"` |
| **auth_client_secret**  string | Client Secret to use in conjunction with `auth_client_id` (if required). |
| **auth_keycloak_url**  aliases: url  string / required | URL to the Keycloak instance. |
| **auth_password**  aliases: password  string | Password to authenticate for API access with. |
| **auth_realm**  string | Keycloak realm name to authenticate to for API access. |
| **auth_username**  aliases: username  string | Username to authenticate for API access with. |
| **client_id**  aliases: clientId  string | The `client_id` of the client. Passing this instead of `id` results in an extra API call. |
| **connection_timeout**  integer  *added in community.general 4.5.0* | Controls the HTTP connections timeout period (in seconds) to Keycloak API.  **Default:** `10` |
| **http_agent**  string  *added in community.general 5.4.0* | Configures the HTTP User-Agent header.  **Default:** `"Ansible"` |
| **id**  string | The unique identifier for this client.  This parameter is not required for getting or generating a client secret but providing it will reduce the number of API calls required. |
| **realm**  string | They Keycloak realm under which this client resides.  **Default:** `"master"` |
| **token**  string  *added in community.general 3.0.0* | Authentication token for Keycloak API. |
| **validate_certs**  boolean | Verify TLS certificates (do not disable this in production).  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](keycloak_clientsecret_info_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](keycloak_clientsecret_info_module.md#id4)

```yaml+jinja
- name: Get a Keycloak client secret, authentication with credentials
  community.general.keycloak_clientsecret_info:
    id: '9d59aa76-2755-48c6-b1af-beb70a82c3cd'
    realm: MyCustomRealm
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
  delegate_to: localhost
  no_log: true

- name: Get a new Keycloak client secret, authentication with token
  community.general.keycloak_clientsecret_info:
    id: '9d59aa76-2755-48c6-b1af-beb70a82c3cd'
    realm: MyCustomRealm
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    token: TOKEN
  delegate_to: localhost
  no_log: true

- name: Get a new Keycloak client secret, passing client_id instead of id
  community.general.keycloak_clientsecret_info:
    client_id: 'myClientId'
    realm: MyCustomRealm
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    token: TOKEN
  delegate_to: localhost
  no_log: true
```

## [Return Values](keycloak_clientsecret_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **clientsecret_info**  complex | Representation of the client secret  **Returned:** on success |
| **type**  string | Credential type.  **Returned:** always  **Sample:** `"secret"` |
| **value**  string | Client secret.  **Returned:** always  **Sample:** `"cUGnX1EIeTtPPAkcyGMv0ncyqDPu68P1"` |
| **msg**  string | Textual description of whether we succeeded or failed  **Returned:** always |

### Authors

- Fynn Chen (@fynncfchen)
- John Cant (@johncant)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
