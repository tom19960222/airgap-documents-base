---
collection: ansible
version: "8"
title: "community.general.keycloak_authentication_required_actions module – Allows administration of Keycloak authentication required actions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/keycloak_authentication_required_actions_module.html
fetched_at: 2026-07-28T01:47:07+00:00
---
# community.general.keycloak_authentication_required_actions module – Allows administration of Keycloak authentication required actions

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
> To use it in a playbook, specify: `community.general.keycloak_authentication_required_actions`.

New in community.general 7.1.0

- [Synopsis](keycloak_authentication_required_actions_module.md#synopsis)
- [Parameters](keycloak_authentication_required_actions_module.md#parameters)
- [Attributes](keycloak_authentication_required_actions_module.md#attributes)
- [Examples](keycloak_authentication_required_actions_module.md#examples)
- [Return Values](keycloak_authentication_required_actions_module.md#return-values)

## [Synopsis](keycloak_authentication_required_actions_module.md#id1)

- This module can register, update and delete required actions.
- It also filters out any duplicate required actions by their alias. The first occurrence is preserved.

## [Parameters](keycloak_authentication_required_actions_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_client_id**  string | OpenID Connect `client_id` to authenticate to the API with.  **Default:** `"admin-cli"` |
| **auth_client_secret**  string | Client Secret to use in conjunction with `auth_client_id` (if required). |
| **auth_keycloak_url**  aliases: url  string / required | URL to the Keycloak instance. |
| **auth_password**  aliases: password  string | Password to authenticate for API access with. |
| **auth_realm**  string | Keycloak realm name to authenticate to for API access. |
| **auth_username**  aliases: username  string | Username to authenticate for API access with. |
| **connection_timeout**  integer  *added in community.general 4.5.0* | Controls the HTTP connections timeout period (in seconds) to Keycloak API.  **Default:** `10` |
| **http_agent**  string  *added in community.general 5.4.0* | Configures the HTTP User-Agent header.  **Default:** `"Ansible"` |
| **realm**  string / required | The name of the realm in which are the authentication required actions. |
| **required_actions**  list / elements=dictionary | Authentication required action. |
| **alias**  string / required | Unique name of the required action. |
| **config**  dictionary | Configuration for the required action. |
| **defaultAction**  boolean | Indicates, if any new user will have the required action assigned to it.  **Choices:**   - `false` - `true` |
| **enabled**  boolean | Indicates, if the required action is enabled or not.  **Choices:**   - `false` - `true` |
| **name**  string | Displayed name of the required action. Required for registration. |
| **priority**  integer | Priority of the required action. |
| **providerId**  string | Provider ID of the required action. Required for registration. |
| **state**  string / required | Control if the realm authentication required actions are going to be registered/updated (`present`) or deleted (`absent`).  **Choices:**   - `"absent"` - `"present"` |
| **token**  string  *added in community.general 3.0.0* | Authentication token for Keycloak API. |
| **validate_certs**  boolean | Verify TLS certificates (do not disable this in production).  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](keycloak_authentication_required_actions_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](keycloak_authentication_required_actions_module.md#id4)

```yaml+jinja
- name: Register a new required action.
  community.general.keycloak_authentication_required_actions:
    auth_client_id: "admin-cli"
    auth_keycloak_url: "http://localhost:8080"
    auth_password: "password"
    auth_realm: "master"
    auth_username: "admin"
    realm: "master"
    required_action:
      - alias: "TERMS_AND_CONDITIONS"
        name: "Terms and conditions"
        providerId: "TERMS_AND_CONDITIONS"
        enabled: true
    state: "present"

- name: Update the newly registered required action.
  community.general.keycloak_authentication_required_actions:
    auth_client_id: "admin-cli"
    auth_keycloak_url: "http://localhost:8080"
    auth_password: "password"
    auth_realm: "master"
    auth_username: "admin"
    realm: "master"
    required_action:
      - alias: "TERMS_AND_CONDITIONS"
        enabled: false
    state: "present"

- name: Delete the updated registered required action.
  community.general.keycloak_authentication_required_actions:
    auth_client_id: "admin-cli"
    auth_keycloak_url: "http://localhost:8080"
    auth_password: "password"
    auth_realm: "master"
    auth_username: "admin"
    realm: "master"
    required_action:
      - alias: "TERMS_AND_CONDITIONS"
    state: "absent"
```

## [Return Values](keycloak_authentication_required_actions_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **end_state**  complex | Representation of the authentication required actions after module execution.  **Returned:** on success |
| **alias**  string | Unique name of the required action.  **Returned:** success  **Sample:** `"test-provider-id"` |
| **config**  dictionary | Configuration for the required action.  **Returned:** success  **Sample:** `{}` |
| **defaultAction**  boolean | Indicates, if any new user will have the required action assigned to it.  **Returned:** success  **Sample:** `false` |
| **enabled**  boolean | Indicates, if the required action is enabled or not.  **Returned:** success  **Sample:** `false` |
| **name**  string | Displayed name of the required action. Required for registration.  **Returned:** success  **Sample:** `"Test provider ID"` |
| **priority**  integer | Priority of the required action.  **Returned:** success  **Sample:** `90` |
| **providerId**  string | Provider ID of the required action. Required for registration.  **Returned:** success  **Sample:** `"test-provider-id"` |
| **msg**  string | Message as to what action was taken.  **Returned:** always |

### Authors

- Skrekulko (@Skrekulko)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
