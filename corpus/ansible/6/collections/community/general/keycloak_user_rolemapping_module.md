---
collection: ansible
version: "6"
title: "community.general.keycloak_user_rolemapping module – Allows administration of Keycloak user_rolemapping with the Keycloak API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/keycloak_user_rolemapping_module.html
fetched_at: 2026-07-27T17:10:24+00:00
---
# community.general.keycloak_user_rolemapping module – Allows administration of Keycloak user_rolemapping with the Keycloak API

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
> To use it in a playbook, specify: `community.general.keycloak_user_rolemapping`.

New in community.general 5.7.0

- [Synopsis](keycloak_user_rolemapping_module.md#synopsis)
- [Parameters](keycloak_user_rolemapping_module.md#parameters)
- [Examples](keycloak_user_rolemapping_module.md#examples)
- [Return Values](keycloak_user_rolemapping_module.md#return-values)

## [Synopsis](keycloak_user_rolemapping_module.md#id1)

- This module allows you to add, remove or modify Keycloak user_rolemapping with the Keycloak REST API. It requires access to the REST API via OpenID Connect; the user connecting and the client being used must have the requisite access rights. In a default Keycloak installation, admin-cli and an admin user would work, as would a separate client definition with the scope tailored to your needs and a user having the expected roles.
- The names of module options are snake_cased versions of the camelCase ones found in the Keycloak API and its documentation at <https://www.keycloak.org/docs-api/8.0/rest-api/index.html>.
- Attributes are multi-valued in the Keycloak API. All attributes are lists of individual values and will be returned that way by this module. You may pass single values for attributes when calling the module, and this will be translated into a list suitable for the API.
- When updating a user_rolemapping, where possible provide the role ID to the module. This removes a lookup to the API to translate the name into the role ID.

## [Parameters](keycloak_user_rolemapping_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_client_id**  string | OpenID Connect *client_id* to authenticate to the API with.  Default: `"admin-cli"` |
| **auth_client_secret**  string | Client Secret to use in conjunction with *auth_client_id* (if required). |
| **auth_keycloak_url**  aliases: url  string / required | URL to the Keycloak instance. |
| **auth_password**  aliases: password  string | Password to authenticate for API access with. |
| **auth_realm**  string | Keycloak realm name to authenticate to for API access. |
| **auth_username**  aliases: username  string | Username to authenticate for API access with. |
| **cid**  string | ID of the client to be mapped.  This parameter is not required for updating or deleting the rolemapping but providing it will reduce the number of API calls required. |
| **client_id**  string | Name of the client to be mapped (different than *cid*).  This parameter is required if *cid* is not provided (can be replaced by *cid* to reduce the number of API calls that must be made). |
| **connection_timeout**  integer  added in community.general 4.5.0 | Controls the HTTP connections timeout period (in seconds) to Keycloak API.  Default: `10` |
| **http_agent**  string  added in community.general 5.4.0 | Configures the HTTP User-Agent header.  Default: `"Ansible"` |
| **realm**  string | They Keycloak realm under which this role_representation resides.  Default: `"master"` |
| **roles**  list / elements=dictionary | Roles to be mapped to the user. |
| **id**  string | The unique identifier for this role_representation.  This parameter is not required for updating or deleting a role_representation but providing it will reduce the number of API calls required. |
| **name**  string | Name of the role representation.  This parameter is required only when creating or updating the role_representation. |
| **service_account_user_client_id**  string | Client ID of the service-account-user to be mapped.  This parameter is not required for updating or deleting the rolemapping but providing it will reduce the number of API calls required. |
| **state**  string | State of the user_rolemapping.  On `present`, the user_rolemapping will be created if it does not yet exist, or updated with the parameters you provide.  On `absent`, the user_rolemapping will be removed if it exists.  Choices:   - `"present"` ← (default) - `"absent"` |
| **target_username**  string | Username of the user roles are mapped to.  This parameter is not required (can be replaced by uid for less API call). |
| **token**  string  added in community.general 3.0.0 | Authentication token for Keycloak API. |
| **uid**  string | ID of the user to be mapped.  This parameter is not required for updating or deleting the rolemapping but providing it will reduce the number of API calls required. |
| **validate_certs**  boolean | Verify TLS certificates (do not disable this in production).  Choices:   - `false` - `true` ← (default) |

## [Examples](keycloak_user_rolemapping_module.md#id3)

```yaml+jinja
- name: Map a client role to a user, authentication with credentials
  community.general.keycloak_user_rolemapping:
    realm: MyCustomRealm
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
    state: present
    client_id: client1
    user_id: user1Id
    roles:
      - name: role_name1
        id: role_id1
      - name: role_name2
        id: role_id2
  delegate_to: localhost

- name: Map a client role to a service account user for a client, authentication with credentials
  community.general.keycloak_user_rolemapping:
    realm: MyCustomRealm
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
    state: present
    client_id: client1
    service_account_user_client_id: clientIdOfServiceAccount
    roles:
      - name: role_name1
        id: role_id1
      - name: role_name2
        id: role_id2
  delegate_to: localhost

- name: Map a client role to a user, authentication with token
  community.general.keycloak_user_rolemapping:
    realm: MyCustomRealm
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    token: TOKEN
    state: present
    client_id: client1
    target_username: user1
    roles:
      - name: role_name1
        id: role_id1
      - name: role_name2
        id: role_id2
  delegate_to: localhost

- name: Unmap client role from a user
  community.general.keycloak_user_rolemapping:
    realm: MyCustomRealm
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
    state: absent
    client_id: client1
    uid: 70e3ae72-96b6-11e6-9056-9737fd4d0764
    roles:
      - name: role_name1
        id: role_id1
      - name: role_name2
        id: role_id2
  delegate_to: localhost
```

## [Return Values](keycloak_user_rolemapping_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **end_state**  dictionary | Representation of client role mapping after module execution.  The sample is truncated.  Returned: on success  Sample: `{"adminUrl": "http://www.example.com/admin_url", "attributes": {"request.object.signature.alg": "RS256"}}` |
| **existing**  dictionary | Representation of existing client role mapping.  The sample is truncated.  Returned: always  Sample: `{"adminUrl": "http://www.example.com/admin_url", "attributes": {"request.object.signature.alg": "RS256"}}` |
| **msg**  string | Message as to what action was taken.  Returned: always  Sample: `"Role role1 assigned to user user1."` |
| **proposed**  dictionary | Representation of proposed client role mapping.  Returned: always  Sample: `{"clientId": "test"}` |

### Authors

- Dušan Marković (@bratwurzt)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
