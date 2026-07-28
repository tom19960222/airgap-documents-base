---
collection: ansible
version: "8"
title: "community.general.keycloak_realm_key module – Allows administration of Keycloak realm keys via Keycloak API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/keycloak_realm_key_module.html
fetched_at: 2026-07-28T01:47:18+00:00
---
# community.general.keycloak_realm_key module – Allows administration of Keycloak realm keys via Keycloak API

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
> To use it in a playbook, specify: `community.general.keycloak_realm_key`.

New in community.general 7.5.0

- [Synopsis](keycloak_realm_key_module.md#synopsis)
- [Parameters](keycloak_realm_key_module.md#parameters)
- [Attributes](keycloak_realm_key_module.md#attributes)
- [Notes](keycloak_realm_key_module.md#notes)
- [Examples](keycloak_realm_key_module.md#examples)
- [Return Values](keycloak_realm_key_module.md#return-values)

## [Synopsis](keycloak_realm_key_module.md#id1)

- This module allows the administration of Keycloak realm keys via the Keycloak REST API. It requires access to the REST API via OpenID Connect; the user connecting and the realm being used must have the requisite access rights. In a default Keycloak installation, admin-cli and an admin user would work, as would a separate realm definition with the scope tailored to your needs and a user having the expected roles.
- The names of module options are snake_cased versions of the camelCase ones found in the Keycloak API and its documentation at <https://www.keycloak.org/docs-api/8.0/rest-api/index.html>. Aliases are provided so camelCased versions can be used as well.
- This module is unable to detect changes to the actual cryptographic key after importing it. However, if some other property is changed alongside the cryptographic key, then the key will also get changed as a side-effect, as the JSON payload needs to include the private key. This can be considered either a bug or a feature, as the alternative would be to always update the realm key whether it has changed or not.
- If certificate is not explicitly provided it will be dynamically created by Keycloak. Therefore comparing the current state of the certificate to the desired state (which may be empty) is not possible.

## [Parameters](keycloak_realm_key_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_client_id**  string | OpenID Connect `client_id` to authenticate to the API with.  **Default:** `"admin-cli"` |
| **auth_client_secret**  string | Client Secret to use in conjunction with `auth_client_id` (if required). |
| **auth_keycloak_url**  aliases: url  string / required | URL to the Keycloak instance. |
| **auth_password**  aliases: password  string | Password to authenticate for API access with. |
| **auth_realm**  string | Keycloak realm name to authenticate to for API access. |
| **auth_username**  aliases: username  string | Username to authenticate for API access with. |
| **config**  dictionary | Dict specifying the key and its properties. |
| **active**  boolean | Whether they key is active or inactive. Not to be confused with the state of the Ansible resource managed by the `state` parameter.  **Choices:**   - `false` - `true` ← (default) |
| **algorithm**  string | Key algorithm.  **Choices:**   - `"RS256"` ← (default) |
| **certificate**  string / required | A certificate signed with the private key as an ASCII string. Contents of the key must match `config.algorithm` and `provider_id`.  If you want Keycloak to automatically generate a certificate using your private key then set this to an empty string. |
| **enabled**  boolean | Whether the key is enabled or disabled. Not to be confused with the state of the Ansible resource managed by the `state` parameter.  **Choices:**   - `false` - `true` ← (default) |
| **priority**  integer / required | The priority of the key. |
| **private_key**  string / required | The private key as an ASCII string. Contents of the key must match `config.algorithm` and `provider_id`.  Please note that the module cannot detect whether the private key specified differs from the current state’s private key. Use `force=true` to force the module to update the private key if you expect it to be updated. |
| **connection_timeout**  integer  *added in community.general 4.5.0* | Controls the HTTP connections timeout period (in seconds) to Keycloak API.  **Default:** `10` |
| **force**  boolean | Enforce the state of the private key and certificate. This is not automatically the case as this module is unable to determine the current state of the private key and thus cannot trigger an update based on an actual divergence. That said, a private key update may happen even if force is false as a side-effect of other changes.  **Choices:**   - `false` ← (default) - `true` |
| **http_agent**  string  *added in community.general 5.4.0* | Configures the HTTP User-Agent header.  **Default:** `"Ansible"` |
| **name**  string / required | Name of the realm key to create. |
| **parent_id**  string / required | The parent_id of the realm key. In practice the ID (name) of the realm. |
| **provider_id**  string | The name of the “provider ID” for the key.  **Choices:**   - `"rsa"` ← (default) |
| **state**  string | State of the keycloak realm key.  On `present`, the realm key will be created (or updated if it exists already).  On `absent`, the realm key will be removed if it exists.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **token**  string  *added in community.general 3.0.0* | Authentication token for Keycloak API. |
| **validate_certs**  boolean | Verify TLS certificates (do not disable this in production).  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](keycloak_realm_key_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **partial** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](keycloak_realm_key_module.md#id4)

> **Note:**
>
> - Current value of the private key cannot be fetched from Keycloak. Therefore comparing its desired state to the current state is not possible.
> - If certificate is not explicitly provided it will be dynamically created by Keycloak. Therefore comparing the current state of the certificate to the desired state (which may be empty) is not possible.
> - Due to the private key and certificate options the module is **not fully idempotent**. You can use `force=true` to force the module to always update if you know that the private key might have changed.

## [Examples](keycloak_realm_key_module.md#id5)

```yaml+jinja
- name: Manage Keycloak realm key (certificate autogenerated by Keycloak)
  community.general.keycloak_realm_key:
    name: custom
    state: present
    parent_id: master
    provider_id: rsa
    auth_keycloak_url: http://localhost:8080/auth
    auth_username: keycloak
    auth_password: keycloak
    auth_realm: master
    config:
      private_key: "{{ private_key }}"
      enabled: true
      active: true
      priority: 120
      algorithm: RS256
- name: Manage Keycloak realm key and certificate
  community.general.keycloak_realm_key:
    name: custom
    state: present
    parent_id: master
    provider_id: rsa
    auth_keycloak_url: http://localhost:8080/auth
    auth_username: keycloak
    auth_password: keycloak
    auth_realm: master
    config:
      private_key: "{{ private_key }}"
      certificate: "{{ certificate }}"
      enabled: true
      active: true
      priority: 120
      algorithm: RS256
```

## [Return Values](keycloak_realm_key_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **end_state**  dictionary | Representation of the keycloak_realm_key after module execution.  **Returned:** on success |
| **config**  dictionary | Realm key configuration.  **Returned:** when `state=present`  **Sample:** `{"active": ["true"], "algorithm": ["RS256"], "enabled": ["true"], "priority": ["140"]}` |
| **id**  string | ID of the realm key.  **Returned:** when `state=present`  **Sample:** `"5b7ec13f-99da-46ad-8326-ab4c73cf4ce4"` |
| **name**  string | Name of the realm key.  **Returned:** when `state=present`  **Sample:** `"mykey"` |
| **parentId**  string | ID of the realm this key belongs to.  **Returned:** when `state=present`  **Sample:** `"myrealm"` |
| **providerId**  string | The ID of the key provider.  **Returned:** when `state=present`  **Sample:** `"rsa"` |
| **providerType**  string | The type of provider.  **Returned:** when `state=present` |
| **msg**  string | Message as to what action was taken.  **Returned:** always |

### Authors

- Samuli Seppänen (@mattock)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
