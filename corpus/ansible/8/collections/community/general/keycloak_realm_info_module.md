---
collection: ansible
version: "8"
title: "community.general.keycloak_realm_info module – Allows obtaining Keycloak realm public information via Keycloak API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/keycloak_realm_info_module.html
fetched_at: 2026-07-28T01:47:18+00:00
---
# community.general.keycloak_realm_info module – Allows obtaining Keycloak realm public information via Keycloak API

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
> To use it in a playbook, specify: `community.general.keycloak_realm_info`.

New in community.general 4.3.0

- [Synopsis](keycloak_realm_info_module.md#synopsis)
- [Parameters](keycloak_realm_info_module.md#parameters)
- [Attributes](keycloak_realm_info_module.md#attributes)
- [Examples](keycloak_realm_info_module.md#examples)
- [Return Values](keycloak_realm_info_module.md#return-values)

## [Synopsis](keycloak_realm_info_module.md#id1)

- This module allows you to get Keycloak realm public information via the Keycloak REST API.
- The names of module options are snake_cased versions of the camelCase ones found in the Keycloak API and its documentation at <https://www.keycloak.org/docs-api/8.0/rest-api/index.html>.
- Attributes are multi-valued in the Keycloak API. All attributes are lists of individual values and will be returned that way by this module. You may pass single values for attributes when calling the module, and this will be translated into a list suitable for the API.

Aliases: identity.keycloak.keycloak_realm_info

## [Parameters](keycloak_realm_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_keycloak_url**  aliases: url  string / required | URL to the Keycloak instance. |
| **realm**  string | They Keycloak realm ID.  **Default:** `"master"` |
| **validate_certs**  boolean | Verify TLS certificates (do not disable this in production).  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](keycloak_realm_info_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](keycloak_realm_info_module.md#id4)

```yaml+jinja
- name: Get a Keycloak public key
  community.general.keycloak_realm_info:
    realm: MyCustomRealm
    auth_keycloak_url: https://auth.example.com/auth
  delegate_to: localhost
```

## [Return Values](keycloak_realm_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message as to what action was taken.  **Returned:** always |
| **realm_info**  dictionary | Representation of the realm public information.  **Returned:** always |
| **account-service**  string | Account console URL.  **Returned:** always  **Sample:** `"https://auth.example.com/auth/realms/MyRealm/account"` |
| **public_key**  string | Public key of the realm.  **Returned:** always  **Sample:** `"MIIBIjANBgkqhkiG9w0BAQEFAAO..."` |
| **realm**  string | Realm ID.  **Returned:** always  **Sample:** `"MyRealm"` |
| **token-service**  string | Token endpoint URL.  **Returned:** always  **Sample:** `"https://auth.example.com/auth/realms/MyRealm/protocol/openid-connect"` |
| **tokens-not-before**  integer | The token not before.  **Returned:** always  **Sample:** `0` |

### Authors

- Fynn Chen (@fynncfchen)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
