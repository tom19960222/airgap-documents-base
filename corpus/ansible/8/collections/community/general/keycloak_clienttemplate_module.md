---
collection: ansible
version: "8"
title: "community.general.keycloak_clienttemplate module – Allows administration of Keycloak client templates via Keycloak API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/keycloak_clienttemplate_module.html
fetched_at: 2026-07-28T01:47:15+00:00
---
# community.general.keycloak_clienttemplate module – Allows administration of Keycloak client templates via Keycloak API

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
> To use it in a playbook, specify: `community.general.keycloak_clienttemplate`.

- [Synopsis](keycloak_clienttemplate_module.md#synopsis)
- [Parameters](keycloak_clienttemplate_module.md#parameters)
- [Attributes](keycloak_clienttemplate_module.md#attributes)
- [Notes](keycloak_clienttemplate_module.md#notes)
- [Examples](keycloak_clienttemplate_module.md#examples)
- [Return Values](keycloak_clienttemplate_module.md#return-values)

## [Synopsis](keycloak_clienttemplate_module.md#id1)

- This module allows the administration of Keycloak client templates via the Keycloak REST API. It requires access to the REST API via OpenID Connect; the user connecting and the client being used must have the requisite access rights. In a default Keycloak installation, admin-cli and an admin user would work, as would a separate client definition with the scope tailored to your needs and a user having the expected roles.
- The names of module options are snake_cased versions of the camelCase ones found in the Keycloak API and its documentation at <https://www.keycloak.org/docs-api/8.0/rest-api/index.html>
- The Keycloak API does not always enforce for only sensible settings to be used – you can set SAML-specific settings on an OpenID Connect client for instance and vice versa. Be careful. If you do not specify a setting, usually a sensible default is chosen.

Aliases: identity.keycloak.keycloak_clienttemplate

## [Parameters](keycloak_clienttemplate_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attributes**  dictionary | A dict of further attributes for this client template. This can contain various configuration settings, though in the default installation of Keycloak as of 3.4, none are documented or known, so this is usually empty. |
| **auth_client_id**  string | OpenID Connect `client_id` to authenticate to the API with.  **Default:** `"admin-cli"` |
| **auth_client_secret**  string | Client Secret to use in conjunction with `auth_client_id` (if required). |
| **auth_keycloak_url**  aliases: url  string / required | URL to the Keycloak instance. |
| **auth_password**  aliases: password  string | Password to authenticate for API access with. |
| **auth_realm**  string | Keycloak realm name to authenticate to for API access. |
| **auth_username**  aliases: username  string | Username to authenticate for API access with. |
| **connection_timeout**  integer  *added in community.general 4.5.0* | Controls the HTTP connections timeout period (in seconds) to Keycloak API.  **Default:** `10` |
| **description**  string | Description of the client template in Keycloak. |
| **full_scope_allowed**  boolean | Is the “Full Scope Allowed” feature set for this client template or not. This is ‘fullScopeAllowed’ in the Keycloak REST API.  **Choices:**   - `false` - `true` |
| **http_agent**  string  *added in community.general 5.4.0* | Configures the HTTP User-Agent header.  **Default:** `"Ansible"` |
| **id**  string | Id of client template to be worked on. This is usually a UUID. |
| **name**  string | Name of the client template. |
| **protocol**  string | Type of client template.  **Choices:**   - `"openid-connect"` - `"saml"` |
| **protocol_mappers**  list / elements=dictionary | a list of dicts defining protocol mappers for this client template. This is ‘protocolMappers’ in the Keycloak REST API. |
| **config**  dictionary | Dict specifying the configuration options for the protocol mapper; the contents differ depending on the value of `protocol_mappers[].protocolMapper` and are not documented other than by the source of the mappers and its parent class(es). An example is given below. It is easiest to obtain valid config values by dumping an already-existing protocol mapper configuration through check-mode in the `existing` field. |
| **consentRequired**  boolean | Specifies whether a user needs to provide consent to a client for this mapper to be active.  **Choices:**   - `false` - `true` |
| **consentText**  string | The human-readable name of the consent the user is presented to accept. |
| **id**  string | Usually a UUID specifying the internal ID of this protocol mapper instance. |
| **name**  string | The name of this protocol mapper. |
| **protocol**  string | This specifies for which protocol this protocol mapper is active.  **Choices:**   - `"openid-connect"` - `"saml"` |
| **protocolMapper**  string | The Keycloak-internal name of the type of this protocol-mapper. While an exhaustive list is impossible to provide since this may be extended through SPIs by the user of Keycloak, by default Keycloak as of 3.4 ships with at least:  `docker-v2-allow-all-mapper`  `oidc-address-mapper`  `oidc-full-name-mapper`  `oidc-group-membership-mapper`  `oidc-hardcoded-claim-mapper`  `oidc-hardcoded-role-mapper`  `oidc-role-name-mapper`  `oidc-script-based-protocol-mapper`  `oidc-sha256-pairwise-sub-mapper`  `oidc-usermodel-attribute-mapper`  `oidc-usermodel-client-role-mapper`  `oidc-usermodel-property-mapper`  `oidc-usermodel-realm-role-mapper`  `oidc-usersessionmodel-note-mapper`  `saml-group-membership-mapper`  `saml-hardcode-attribute-mapper`  `saml-hardcode-role-mapper`  `saml-role-list-mapper`  `saml-role-name-mapper`  `saml-user-attribute-mapper`  `saml-user-property-mapper`  `saml-user-session-note-mapper`  An exhaustive list of available mappers on your installation can be obtained on the admin console by going to Server Info -> Providers and looking under ‘protocol-mapper’. |
| **realm**  string | Realm this client template is found in.  **Default:** `"master"` |
| **state**  string | State of the client template.  On `present`, the client template will be created (or updated if it exists already).  On `absent`, the client template will be removed if it exists  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **token**  string  *added in community.general 3.0.0* | Authentication token for Keycloak API. |
| **validate_certs**  boolean | Verify TLS certificates (do not disable this in production).  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](keycloak_clienttemplate_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](keycloak_clienttemplate_module.md#id4)

> **Note:**
>
> - The Keycloak REST API defines further fields (namely `bearerOnly`, `consentRequired`, `standardFlowEnabled`, `implicitFlowEnabled`, `directAccessGrantsEnabled`, `serviceAccountsEnabled`, `publicClient`, and `frontchannelLogout`) which, while available with keycloak_client, do not have any effect on Keycloak client-templates and are discarded if supplied with an API request changing client-templates. As such, they are not available through this module.

## [Examples](keycloak_clienttemplate_module.md#id5)

```yaml+jinja
- name: Create or update Keycloak client template (minimal), authentication with credentials
  community.general.keycloak_client:
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
    realm: master
    name: this_is_a_test
  delegate_to: localhost

- name: Create or update Keycloak client template (minimal), authentication with token
  community.general.keycloak_clienttemplate:
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    token: TOKEN
    realm: master
    name: this_is_a_test
  delegate_to: localhost

- name: Delete Keycloak client template
  community.general.keycloak_client:
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
    realm: master
    state: absent
    name: test01
  delegate_to: localhost

- name: Create or update Keycloak client template (with a protocol mapper)
  community.general.keycloak_client:
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
    realm: master
    name: this_is_a_test
    protocol_mappers:
      - config:
          access.token.claim: true
          claim.name: "family_name"
          id.token.claim: true
          jsonType.label: String
          user.attribute: lastName
          userinfo.token.claim: true
        consentRequired: true
        consentText: "${familyName}"
        name: family name
        protocol: openid-connect
        protocolMapper: oidc-usermodel-property-mapper
    full_scope_allowed: false
    id: bce6f5e9-d7d3-4955-817e-c5b7f8d65b3f
  delegate_to: localhost
```

## [Return Values](keycloak_clienttemplate_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **end_state**  dictionary | Representation of client template after module execution (sample is truncated).  **Returned:** on success  **Sample:** `{"description": "test01", "fullScopeAllowed": false, "id": "9c3712ab-decd-481e-954f-76da7b006e5f", "name": "test01", "protocol": "saml"}` |
| **existing**  dictionary | Representation of existing client template (sample is truncated).  **Returned:** always  **Sample:** `{"description": "test01", "fullScopeAllowed": false, "id": "9c3712ab-decd-481e-954f-76da7b006e5f", "name": "test01", "protocol": "saml"}` |
| **msg**  string | Message as to what action was taken.  **Returned:** always  **Sample:** `"Client template testclient has been updated"` |
| **proposed**  dictionary | Representation of proposed client template.  **Returned:** always  **Sample:** `{"name": "test01"}` |

### Authors

- Eike Frost (@eikef)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
