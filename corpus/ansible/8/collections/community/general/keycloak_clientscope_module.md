---
collection: ansible
version: "8"
title: "community.general.keycloak_clientscope module – Allows administration of Keycloak client_scopes via Keycloak API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/keycloak_clientscope_module.html
fetched_at: 2026-07-28T01:47:12+00:00
---
# community.general.keycloak_clientscope module – Allows administration of Keycloak client_scopes via Keycloak API

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
> To use it in a playbook, specify: `community.general.keycloak_clientscope`.

New in community.general 3.4.0

- [Synopsis](keycloak_clientscope_module.md#synopsis)
- [Parameters](keycloak_clientscope_module.md#parameters)
- [Attributes](keycloak_clientscope_module.md#attributes)
- [Examples](keycloak_clientscope_module.md#examples)
- [Return Values](keycloak_clientscope_module.md#return-values)

## [Synopsis](keycloak_clientscope_module.md#id1)

- This module allows you to add, remove or modify Keycloak client_scopes via the Keycloak REST API. It requires access to the REST API via OpenID Connect; the user connecting and the client being used must have the requisite access rights. In a default Keycloak installation, admin-cli and an admin user would work, as would a separate client definition with the scope tailored to your needs and a user having the expected roles.
- The names of module options are snake_cased versions of the camelCase ones found in the Keycloak API and its documentation at <https://www.keycloak.org/docs-api/8.0/rest-api/index.html>.
- Attributes are multi-valued in the Keycloak API. All attributes are lists of individual values and will be returned that way by this module. You may pass single values for attributes when calling the module, and this will be translated into a list suitable for the API.
- When updating a client_scope, where possible provide the client_scope ID to the module. This removes a lookup to the API to translate the name into the client_scope ID.

Aliases: identity.keycloak.keycloak_clientscope

## [Parameters](keycloak_clientscope_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attributes**  dictionary | A dict of key/value pairs to set as custom attributes for the client_scope.  Values may be single values (for example a string) or a list of strings. |
| **auth_client_id**  string | OpenID Connect `client_id` to authenticate to the API with.  **Default:** `"admin-cli"` |
| **auth_client_secret**  string | Client Secret to use in conjunction with `auth_client_id` (if required). |
| **auth_keycloak_url**  aliases: url  string / required | URL to the Keycloak instance. |
| **auth_password**  aliases: password  string | Password to authenticate for API access with. |
| **auth_realm**  string | Keycloak realm name to authenticate to for API access. |
| **auth_username**  aliases: username  string | Username to authenticate for API access with. |
| **connection_timeout**  integer  *added in community.general 4.5.0* | Controls the HTTP connections timeout period (in seconds) to Keycloak API.  **Default:** `10` |
| **description**  string | Description for this client_scope.  This parameter is not required for updating or deleting a client_scope. |
| **http_agent**  string  *added in community.general 5.4.0* | Configures the HTTP User-Agent header.  **Default:** `"Ansible"` |
| **id**  string | The unique identifier for this client_scope.  This parameter is not required for updating or deleting a client_scope but providing it will reduce the number of API calls required. |
| **name**  string | Name of the client_scope.  This parameter is required only when creating or updating the client_scope. |
| **protocol**  string | Type of client.  **Choices:**   - `"openid-connect"` - `"saml"` - `"wsfed"` |
| **protocol_mappers**  aliases: protocolMappers  list / elements=dictionary | A list of dicts defining protocol mappers for this client.  This is ‘protocolMappers’ in the Keycloak REST API. |
| **config**  dictionary | Dict specifying the configuration options for the protocol mapper; the contents differ depending on the value of `protocol_mappers[].protocolMapper` and are not documented other than by the source of the mappers and its parent class(es). An example is given below. It is easiest to obtain valid config values by dumping an already-existing protocol mapper configuration through check-mode in the `existing` return value. |
| **id**  string | Usually a UUID specifying the internal ID of this protocol mapper instance. |
| **name**  string | The name of this protocol mapper. |
| **protocol**  string | This specifies for which protocol this protocol mapper.  is active.  **Choices:**   - `"openid-connect"` - `"saml"` - `"wsfed"` |
| **protocolMapper**  string | The Keycloak-internal name of the type of this protocol-mapper. While an exhaustive list is impossible to provide since this may be extended through SPIs by the user of Keycloak, by default Keycloak as of 3.4 ships with at least:  `docker-v2-allow-all-mapper`  `oidc-address-mapper`  `oidc-full-name-mapper`  `oidc-group-membership-mapper`  `oidc-hardcoded-claim-mapper`  `oidc-hardcoded-role-mapper`  `oidc-role-name-mapper`  `oidc-script-based-protocol-mapper`  `oidc-sha256-pairwise-sub-mapper`  `oidc-usermodel-attribute-mapper`  `oidc-usermodel-client-role-mapper`  `oidc-usermodel-property-mapper`  `oidc-usermodel-realm-role-mapper`  `oidc-usersessionmodel-note-mapper`  `saml-group-membership-mapper`  `saml-hardcode-attribute-mapper`  `saml-hardcode-role-mapper`  `saml-role-list-mapper`  `saml-role-name-mapper`  `saml-user-attribute-mapper`  `saml-user-property-mapper`  `saml-user-session-note-mapper`  An exhaustive list of available mappers on your installation can be obtained on the admin console by going to Server Info -> Providers and looking under ‘protocol-mapper’. |
| **realm**  string | They Keycloak realm under which this client_scope resides.  **Default:** `"master"` |
| **state**  string | State of the client_scope.  On `present`, the client_scope will be created if it does not yet exist, or updated with the parameters you provide.  On `absent`, the client_scope will be removed if it exists.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **token**  string  *added in community.general 3.0.0* | Authentication token for Keycloak API. |
| **validate_certs**  boolean | Verify TLS certificates (do not disable this in production).  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](keycloak_clientscope_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](keycloak_clientscope_module.md#id4)

```yaml+jinja
- name: Create a Keycloak client_scopes, authentication with credentials
  community.general.keycloak_clientscope:
    name: my-new-kc-clientscope
    realm: MyCustomRealm
    state: present
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
  delegate_to: localhost

- name: Create a Keycloak client_scopes, authentication with token
  community.general.keycloak_clientscope:
    name: my-new-kc-clientscope
    realm: MyCustomRealm
    state: present
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    token: TOKEN
  delegate_to: localhost

- name: Delete a keycloak client_scopes
  community.general.keycloak_clientscope:
    id: '9d59aa76-2755-48c6-b1af-beb70a82c3cd'
    state: absent
    realm: MyCustomRealm
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
  delegate_to: localhost

- name: Delete a Keycloak client_scope based on name
  community.general.keycloak_clientscope:
    name: my-clientscope-for-deletion
    state: absent
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
  delegate_to: localhost

- name: Update the name of a Keycloak client_scope
  community.general.keycloak_clientscope:
    id: '9d59aa76-2755-48c6-b1af-beb70a82c3cd'
    name: an-updated-kc-clientscope-name
    state: present
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
  delegate_to: localhost

- name: Create a Keycloak client_scope with some custom attributes
  community.general.keycloak_clientscope:
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
    name: my-new_clientscope
    description: description-of-clientscope
    protocol: openid-connect
    protocol_mappers:
      - config:
          access.token.claim: true
          claim.name: "family_name"
          id.token.claim: true
          jsonType.label: String
          user.attribute: lastName
          userinfo.token.claim: true
        name: family name
        protocol: openid-connect
        protocolMapper: oidc-usermodel-property-mapper
      - config:
          attribute.name: Role
          attribute.nameformat: Basic
          single: false
        name: role list
        protocol: saml
        protocolMapper: saml-role-list-mapper
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

## [Return Values](keycloak_clientscope_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **end_state**  dictionary | Representation of client scope after module execution (sample is truncated).  **Returned:** on success  **Sample:** `{"adminUrl": "http://www.example.com/admin_url", "attributes": {"request.object.signature.alg": "RS256"}}` |
| **existing**  dictionary | Representation of existing client scope (sample is truncated).  **Returned:** always  **Sample:** `{"adminUrl": "http://www.example.com/admin_url", "attributes": {"request.object.signature.alg": "RS256"}}` |
| **msg**  string | Message as to what action was taken.  **Returned:** always  **Sample:** `"Client_scope testclientscope has been updated"` |
| **proposed**  dictionary | Representation of proposed client scope.  **Returned:** always  **Sample:** `{"clientId": "test"}` |

### Authors

- Gaëtan Daubresse (@Gaetan2907)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
