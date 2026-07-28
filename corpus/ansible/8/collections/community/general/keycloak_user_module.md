---
collection: ansible
version: "8"
title: "community.general.keycloak_user module – Create and configure a user in Keycloak"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/keycloak_user_module.html
fetched_at: 2026-07-28T01:47:20+00:00
---
# community.general.keycloak_user module – Create and configure a user in Keycloak

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
> To use it in a playbook, specify: `community.general.keycloak_user`.

New in community.general 7.1.0

- [Synopsis](keycloak_user_module.md#synopsis)
- [Parameters](keycloak_user_module.md#parameters)
- [Attributes](keycloak_user_module.md#attributes)
- [Notes](keycloak_user_module.md#notes)
- [Examples](keycloak_user_module.md#examples)
- [Return Values](keycloak_user_module.md#return-values)

## [Synopsis](keycloak_user_module.md#id1)

- This module creates, removes, or updates Keycloak users.

## [Parameters](keycloak_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access**  dictionary | list user access. |
| **attributes**  list / elements=dictionary | List of user attributes. |
| **name**  string | Name of the attribute. |
| **state**  string | Control whether the attribute must exists or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **values**  list / elements=string | Values for the attribute as list. |
| **auth_client_id**  string | OpenID Connect `client_id` to authenticate to the API with.  **Default:** `"admin-cli"` |
| **auth_client_secret**  string | Client Secret to use in conjunction with `auth_client_id` (if required). |
| **auth_keycloak_url**  aliases: url  string / required | URL to the Keycloak instance. |
| **auth_password**  aliases: password  string | Password to authenticate for API access with. |
| **auth_realm**  string | Keycloak realm name to authenticate to for API access. |
| **auth_username**  string | Username to authenticate for API access with. |
| **client_consents**  aliases: clientConsents  list / elements=dictionary | Client Authenticator Type.  **Default:** `[]` |
| **client_id**  aliases: clientId  string / required | Client ID of the client role. Not the technical ID of the client. |
| **roles**  list / elements=string / required | List of client roles to assign to the user. |
| **connection_timeout**  integer  *added in community.general 4.5.0* | Controls the HTTP connections timeout period (in seconds) to Keycloak API.  **Default:** `10` |
| **credentials**  list / elements=dictionary | User credentials.  **Default:** `[]` |
| **temporary**  boolean | If `true`, the users are required to reset their credentials at next login.  **Choices:**   - `false` ← (default) - `true` |
| **type**  string / required | Credential type. |
| **value**  string / required | Value of the credential. |
| **disableable_credential_types**  aliases: disableableCredentialTypes  list / elements=string | list user Credential Type.  **Default:** `[]` |
| **email**  string | User email. |
| **email_verified**  aliases: emailVerified  boolean | Check the validity of user email.  **Choices:**   - `false` ← (default) - `true` |
| **enabled**  boolean | Enabled user.  **Choices:**   - `false` - `true` |
| **federated_identities**  aliases: federatedIdentities  list / elements=string | List of IDPs of user.  **Default:** `[]` |
| **federation_link**  aliases: federationLink  string | Federation Link. |
| **first_name**  aliases: firstName  string | The user’s first name. |
| **force**  boolean | If `true`, allows to remove user and recreate it.  **Choices:**   - `false` ← (default) - `true` |
| **groups**  list / elements=dictionary | List of groups for the user.  **Default:** `[]` |
| **name**  string | Name of the group. |
| **state**  string | Control whether the user must be member of this group or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **http_agent**  string  *added in community.general 5.4.0* | Configures the HTTP User-Agent header.  **Default:** `"Ansible"` |
| **id**  string | ID of the user on the Keycloak server if known. |
| **last_name**  aliases: lastName  string | The user’s last name. |
| **origin**  string | user origin. |
| **realm**  string | The name of the realm in which is the client.  **Default:** `"master"` |
| **required_actions**  aliases: requiredActions  list / elements=string | RequiredActions user Auth.  **Default:** `[]` |
| **self**  string | user self administration. |
| **service_account_client_id**  aliases: serviceAccountClientId  string | Description of the client Application. |
| **state**  string | Control whether the user should exists or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **token**  string  *added in community.general 3.0.0* | Authentication token for Keycloak API. |
| **username**  string / required | Username for the user. |
| **validate_certs**  boolean | Verify TLS certificates (do not disable this in production).  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](keycloak_user_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](keycloak_user_module.md#id4)

> **Note:**
>
> - The module does not modify the user ID of an existing user.

## [Examples](keycloak_user_module.md#id5)

```yaml+jinja
- name: Create a user user1
  community.general.keycloak_user:
    auth_keycloak_url: http://localhost:8080/auth
    auth_username: admin
    auth_password: password
    realm: master
    username: user1
    firstName: user1
    lastName: user1
    email: user1
    enabled: true
    emailVerified: false
    credentials:
        - type: password
          value: password
          temporary: false
    attributes:
        - name: attr1
          values:
            - value1
          state: present
        - name: attr2
          values:
            - value2
          state: absent
    groups:
        - name: group1
          state: present
    state: present

- name: Re-create a User
  community.general.keycloak_user:
    auth_keycloak_url: http://localhost:8080/auth
    auth_username: admin
    auth_password: password
    realm: master
    username: user1
    firstName: user1
    lastName: user1
    email: user1
    enabled: true
    emailVerified: false
    credentials:
        - type: password
          value: password
          temporary: false
    attributes:
        - name: attr1
          values:
            - value1
          state: present
        - name: attr2
          values:
            - value2
          state: absent
    groups:
        - name: group1
          state: present
    state: present

- name: Re-create a User
  community.general.keycloak_user:
    auth_keycloak_url: http://localhost:8080/auth
    auth_username: admin
    auth_password: password
    realm: master
    username: user1
    firstName: user1
    lastName: user1
    email: user1
    enabled: true
    emailVerified: false
    credentials:
        - type: password
          value: password
          temporary: false
    attributes:
        - name: attr1
          values:
            - value1
          state: present
        - name: attr2
          values:
            - value2
          state: absent
    groups:
        - name: group1
          state: present
    state: present
    force: true

- name: Remove User
  community.general.keycloak_user:
    auth_keycloak_url: http://localhost:8080/auth
    auth_username: admin
    auth_password: password
    realm: master
    username: user1
    state: absent
```

## [Return Values](keycloak_user_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Return `true` if the operation changed the user on the keycloak server, `false` otherwise.  **Returned:** always |
| **end_state**  dictionary | Representation of the user after module execution  **Returned:** on success |
| **existing**  dictionary | Representation of the existing user.  **Returned:** on success |
| **msg**  string | Message as to what action was taken.  **Returned:** always  **Sample:** `"User f18c709c-03d6-11ee-970b-c74bf2721112 created"` |
| **proposed**  dictionary | Representation of the proposed user.  **Returned:** on success |

### Authors

- Philippe Gauthier (@elfelip)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
