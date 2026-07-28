---
collection: ansible
version: "6"
title: "community.general.keycloak_group module – Allows administration of Keycloak groups via Keycloak API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/keycloak_group_module.html
fetched_at: 2026-07-27T17:10:19+00:00
---
# community.general.keycloak_group module – Allows administration of Keycloak groups via Keycloak API

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.keycloak_group`.

- [Synopsis](keycloak_group_module.md#synopsis)
- [Parameters](keycloak_group_module.md#parameters)
- [Notes](keycloak_group_module.md#notes)
- [Examples](keycloak_group_module.md#examples)
- [Return Values](keycloak_group_module.md#return-values)

## [Synopsis](keycloak_group_module.md#id1)

- This module allows you to add, remove or modify Keycloak groups via the Keycloak REST API. It requires access to the REST API via OpenID Connect; the user connecting and the client being used must have the requisite access rights. In a default Keycloak installation, admin-cli and an admin user would work, as would a separate client definition with the scope tailored to your needs and a user having the expected roles.
- The names of module options are snake_cased versions of the camelCase ones found in the Keycloak API and its documentation at <https://www.keycloak.org/docs-api/8.0/rest-api/index.html>.
- Attributes are multi-valued in the Keycloak API. All attributes are lists of individual values and will be returned that way by this module. You may pass single values for attributes when calling the module, and this will be translated into a list suitable for the API.
- When updating a group, where possible provide the group ID to the module. This removes a lookup to the API to translate the name into the group ID.

## [Parameters](keycloak_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attributes**  dictionary | A dict of key/value pairs to set as custom attributes for the group.  Values may be single values (e.g. a string) or a list of strings. |
| **auth_client_id**  string | OpenID Connect *client_id* to authenticate to the API with.  Default: `"admin-cli"` |
| **auth_client_secret**  string | Client Secret to use in conjunction with *auth_client_id* (if required). |
| **auth_keycloak_url**  aliases: url  string / required | URL to the Keycloak instance. |
| **auth_password**  aliases: password  string | Password to authenticate for API access with. |
| **auth_realm**  string | Keycloak realm name to authenticate to for API access. |
| **auth_username**  aliases: username  string | Username to authenticate for API access with. |
| **connection_timeout**  integer  added in community.general 4.5.0 | Controls the HTTP connections timeout period (in seconds) to Keycloak API.  Default: `10` |
| **http_agent**  string  added in community.general 5.4.0 | Configures the HTTP User-Agent header.  Default: `"Ansible"` |
| **id**  string | The unique identifier for this group.  This parameter is not required for updating or deleting a group but providing it will reduce the number of API calls required. |
| **name**  string | Name of the group.  This parameter is required only when creating or updating the group. |
| **realm**  string | They Keycloak realm under which this group resides.  Default: `"master"` |
| **state**  string | State of the group.  On `present`, the group will be created if it does not yet exist, or updated with the parameters you provide.  On `absent`, the group will be removed if it exists.  Choices:   - `"present"` ← (default) - `"absent"` |
| **token**  string  added in community.general 3.0.0 | Authentication token for Keycloak API. |
| **validate_certs**  boolean | Verify TLS certificates (do not disable this in production).  Choices:   - `false` - `true` ← (default) |

## [Notes](keycloak_group_module.md#id3)

> **Note:**
>
> - Presently, the *realmRoles*, *clientRoles* and *access* attributes returned by the Keycloak API are read-only for groups. This limitation will be removed in a later version of this module.

## [Examples](keycloak_group_module.md#id4)

```yaml+jinja
- name: Create a Keycloak group, authentication with credentials
  community.general.keycloak_group:
    name: my-new-kc-group
    realm: MyCustomRealm
    state: present
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
  delegate_to: localhost

- name: Create a Keycloak group, authentication with token
  community.general.keycloak_group:
    name: my-new-kc-group
    realm: MyCustomRealm
    state: present
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    token: TOKEN
  delegate_to: localhost

- name: Delete a keycloak group
  community.general.keycloak_group:
    id: '9d59aa76-2755-48c6-b1af-beb70a82c3cd'
    state: absent
    realm: MyCustomRealm
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
  delegate_to: localhost

- name: Delete a Keycloak group based on name
  community.general.keycloak_group:
    name: my-group-for-deletion
    state: absent
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
  delegate_to: localhost

- name: Update the name of a Keycloak group
  community.general.keycloak_group:
    id: '9d59aa76-2755-48c6-b1af-beb70a82c3cd'
    name: an-updated-kc-group-name
    state: present
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
  delegate_to: localhost

- name: Create a keycloak group with some custom attributes
  community.general.keycloak_group:
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
    name: my-new_group
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

## [Return Values](keycloak_group_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **end_state**  complex | Representation of the group after module execution (sample is truncated).  Returned: on success |
| **access**  dictionary | A dict describing the accesses you have to this group based on the credentials used.  Returned: always  Sample: `{"manage": true, "manageMembership": true, "view": true}` |
| **attributes**  dictionary | Attributes applied to this group.  Returned: always  Sample: `{"attr1": ["val1", "val2", "val3"]}` |
| **clientRoles**  list / elements=string | A list of client-level roles granted to this group.  Returned: always  Sample: `[]` |
| **id**  string | GUID that identifies the group.  Returned: always  Sample: `"23f38145-3195-462c-97e7-97041ccea73e"` |
| **name**  string | Name of the group.  Returned: always  Sample: `"grp-test-123"` |
| **path**  string | URI path to the group.  Returned: always  Sample: `"/grp-test-123"` |
| **realmRoles**  list / elements=string | An array of the realm-level roles granted to this group.  Returned: always  Sample: `[]` |
| **subGroups**  list / elements=string | A list of groups that are children of this group. These groups will have the same parameters as documented here.  Returned: always |
| **group**  complex | Representation of the group after module execution.  Deprecated return value, it will be removed in community.general 6.0.0. Please use the return value *end_state* instead.  Returned: always |
| **access**  dictionary | A dict describing the accesses you have to this group based on the credentials used.  Returned: always  Sample: `{"manage": true, "manageMembership": true, "view": true}` |
| **attributes**  dictionary | Attributes applied to this group.  Returned: always  Sample: `{"attr1": ["val1", "val2", "val3"]}` |
| **clientRoles**  list / elements=string | A list of client-level roles granted to this group.  Returned: always  Sample: `[]` |
| **id**  string | GUID that identifies the group.  Returned: always  Sample: `"23f38145-3195-462c-97e7-97041ccea73e"` |
| **name**  string | Name of the group.  Returned: always  Sample: `"grp-test-123"` |
| **path**  string | URI path to the group.  Returned: always  Sample: `"/grp-test-123"` |
| **realmRoles**  list / elements=string | An array of the realm-level roles granted to this group.  Returned: always  Sample: `[]` |
| **subGroups**  list / elements=string | A list of groups that are children of this group. These groups will have the same parameters as documented here.  Returned: always |
| **msg**  string | Message as to what action was taken.  Returned: always |

### Authors

- Adam Goossens (@adamgoossens)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
