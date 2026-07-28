---
collection: ansible
version: "8"
title: "community.general.keycloak_role module – Allows administration of Keycloak roles via Keycloak API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/keycloak_role_module.html
fetched_at: 2026-07-28T01:47:19+00:00
---
# community.general.keycloak_role module – Allows administration of Keycloak roles via Keycloak API

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
> To use it in a playbook, specify: `community.general.keycloak_role`.

New in community.general 3.4.0

- [Synopsis](keycloak_role_module.md#synopsis)
- [Parameters](keycloak_role_module.md#parameters)
- [Attributes](keycloak_role_module.md#attributes)
- [Examples](keycloak_role_module.md#examples)
- [Return Values](keycloak_role_module.md#return-values)

## [Synopsis](keycloak_role_module.md#id1)

- This module allows you to add, remove or modify Keycloak roles via the Keycloak REST API. It requires access to the REST API via OpenID Connect; the user connecting and the client being used must have the requisite access rights. In a default Keycloak installation, admin-cli and an admin user would work, as would a separate client definition with the scope tailored to your needs and a user having the expected roles.
- The names of module options are snake_cased versions of the camelCase ones found in the Keycloak API and its documentation at <https://www.keycloak.org/docs-api/8.0/rest-api/index.html>.
- Attributes are multi-valued in the Keycloak API. All attributes are lists of individual values and will be returned that way by this module. You may pass single values for attributes when calling the module, and this will be translated into a list suitable for the API.

Aliases: identity.keycloak.keycloak_role

## [Parameters](keycloak_role_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attributes**  dictionary | A dict of key/value pairs to set as custom attributes for the role.  Values may be single values (e.g. a string) or a list of strings. |
| **auth_client_id**  string | OpenID Connect `client_id` to authenticate to the API with.  **Default:** `"admin-cli"` |
| **auth_client_secret**  string | Client Secret to use in conjunction with `auth_client_id` (if required). |
| **auth_keycloak_url**  aliases: url  string / required | URL to the Keycloak instance. |
| **auth_password**  aliases: password  string | Password to authenticate for API access with. |
| **auth_realm**  string | Keycloak realm name to authenticate to for API access. |
| **auth_username**  aliases: username  string | Username to authenticate for API access with. |
| **client_id**  string | If the role is a client role, the client id under which it resides.  If this parameter is absent, the role is considered a realm role. |
| **composite**  boolean  *added in community.general 7.1.0* | If `true`, the role is a composition of other realm and/or client role.  **Choices:**   - `false` ← (default) - `true` |
| **composites**  list / elements=dictionary  *added in community.general 7.1.0* | List of roles to include to the composite realm role.  If the composite role is a client role, the `clientId` (not ID of the client) must be specified.  **Default:** `[]` |
| **client_id**  aliases: clientId  string | Client ID if the role is a client role. Do not include this option for a REALM role.  Use the client ID you can see in the Keycloak console, not the technical ID of the client. |
| **name**  string / required | Name of the role. This can be the name of a REALM role or a client role. |
| **state**  string | Create the composite if present, remove it if absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **connection_timeout**  integer  *added in community.general 4.5.0* | Controls the HTTP connections timeout period (in seconds) to Keycloak API.  **Default:** `10` |
| **description**  string | The role description. |
| **http_agent**  string  *added in community.general 5.4.0* | Configures the HTTP User-Agent header.  **Default:** `"Ansible"` |
| **name**  string / required | Name of the role.  This parameter is required. |
| **realm**  string | The Keycloak realm under which this role resides.  **Default:** `"master"` |
| **state**  string | State of the role.  On `present`, the role will be created if it does not yet exist, or updated with the parameters you provide.  On `absent`, the role will be removed if it exists.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **token**  string  *added in community.general 3.0.0* | Authentication token for Keycloak API. |
| **validate_certs**  boolean | Verify TLS certificates (do not disable this in production).  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](keycloak_role_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](keycloak_role_module.md#id4)

```yaml+jinja
- name: Create a Keycloak realm role, authentication with credentials
  community.general.keycloak_role:
    name: my-new-kc-role
    realm: MyCustomRealm
    state: present
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
  delegate_to: localhost

- name: Create a Keycloak realm role, authentication with token
  community.general.keycloak_role:
    name: my-new-kc-role
    realm: MyCustomRealm
    state: present
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    token: TOKEN
  delegate_to: localhost

- name: Create a Keycloak client role
  community.general.keycloak_role:
    name: my-new-kc-role
    realm: MyCustomRealm
    client_id: MyClient
    state: present
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
  delegate_to: localhost

- name: Delete a Keycloak role
  community.general.keycloak_role:
    name: my-role-for-deletion
    state: absent
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
  delegate_to: localhost

- name: Create a keycloak role with some custom attributes
  community.general.keycloak_role:
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
    name: my-new-role
    attributes:
        attrib1: value1
        attrib2: value2
        attrib3:
            - with
            - numerous
            - individual
            - list
            - items
  delegate_to: localhost
```

## [Return Values](keycloak_role_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **end_state**  dictionary | Representation of role after module execution (sample is truncated).  **Returned:** on success  **Sample:** `{"attributes": {}, "clientRole": true, "composite": false, "containerId": "9f03eb61-a826-4771-a9fd-930e06d2d36a", "description": "My updated client test role", "id": "561703dd-0f38-45ff-9a5a-0c978f794547", "name": "myrole"}` |
| **existing**  dictionary | Representation of existing role.  **Returned:** always  **Sample:** `{"attributes": {}, "clientRole": true, "composite": false, "containerId": "9f03eb61-a826-4771-a9fd-930e06d2d36a", "description": "My client test role", "id": "561703dd-0f38-45ff-9a5a-0c978f794547", "name": "myrole"}` |
| **msg**  string | Message as to what action was taken.  **Returned:** always  **Sample:** `"Role myrole has been updated"` |
| **proposed**  dictionary | Representation of proposed role.  **Returned:** always  **Sample:** `{"description": "My updated test description"}` |

### Authors

- Laurent Paumier (@laurpaum)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
