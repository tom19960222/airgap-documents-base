---
collection: ansible
version: "6"
title: "community.general.keycloak_identity_provider module – Allows administration of Keycloak identity providers via Keycloak API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/keycloak_identity_provider_module.html
fetched_at: 2026-07-27T17:10:20+00:00
---
# community.general.keycloak_identity_provider module – Allows administration of Keycloak identity providers via Keycloak API

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
> To use it in a playbook, specify: `community.general.keycloak_identity_provider`.

New in community.general 3.6.0

- [Synopsis](keycloak_identity_provider_module.md#synopsis)
- [Parameters](keycloak_identity_provider_module.md#parameters)
- [Examples](keycloak_identity_provider_module.md#examples)
- [Return Values](keycloak_identity_provider_module.md#return-values)

## [Synopsis](keycloak_identity_provider_module.md#id1)

- This module allows you to add, remove or modify Keycloak identity providers via the Keycloak REST API. It requires access to the REST API via OpenID Connect; the user connecting and the client being used must have the requisite access rights. In a default Keycloak installation, admin-cli and an admin user would work, as would a separate client definition with the scope tailored to your needs and a user having the expected roles.
- The names of module options are snake_cased versions of the camelCase ones found in the Keycloak API and its documentation at <https://www.keycloak.org/docs-api/15.0/rest-api/index.html>.

## [Parameters](keycloak_identity_provider_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **add_read_token_role_on_create**  aliases: addReadTokenRoleOnCreate  boolean | Enable/disable whether new users can read any stored tokens. This assigns the `broker.read-token` role.  Choices:   - `false` - `true` |
| **alias**  string / required | The alias uniquely identifies an identity provider and it is also used to build the redirect URI. |
| **auth_client_id**  string | OpenID Connect *client_id* to authenticate to the API with.  Default: `"admin-cli"` |
| **auth_client_secret**  string | Client Secret to use in conjunction with *auth_client_id* (if required). |
| **auth_keycloak_url**  aliases: url  string / required | URL to the Keycloak instance. |
| **auth_password**  aliases: password  string | Password to authenticate for API access with. |
| **auth_realm**  string | Keycloak realm name to authenticate to for API access. |
| **auth_username**  aliases: username  string | Username to authenticate for API access with. |
| **authenticate_by_default**  aliases: authenticateByDefault  boolean | Specifies if this identity provider should be used by default for authentication even before displaying login screen.  Choices:   - `false` - `true` |
| **config**  dictionary | Dict specifying the configuration options for the provider; the contents differ depending on the value of *providerId*. Examples are given below for `oidc` and `saml`. It is easiest to obtain valid config values by dumping an already-existing identity provider configuration through check-mode in the *existing* field. |
| **authorizationUrl**  string | The Authorization URL. |
| **backchannelSupported**  string | Does the external IDP support backchannel logout? |
| **clientAuthMethod**  string | The client authentication method. |
| **clientId**  string | The client or client identifier registered within the identity provider. |
| **clientSecret**  string | The client or client secret registered within the identity provider. |
| **defaultScope**  string | The scopes to be sent when asking for authorization. |
| **entityId**  string | The Entity ID that will be used to uniquely identify this SAML Service Provider. |
| **gui_order**  aliases: guiOrder  integer | Number defining order of the provider in GUI (for example, on Login page). |
| **hide_on_login_page**  aliases: hideOnLoginPage  boolean | If hidden, login with this provider is possible only if requested explicitly, for example using the `kc_idp_hint` parameter.  Choices:   - `false` - `true` |
| **issuer**  string | The issuer identifier for the issuer of the response. If not provided, no validation will be performed. |
| **jwksUrl**  string | URL where identity provider keys in JWK format are stored. See JWK specification for more details. |
| **logoutUrl**  string | End session endpoint to use to logout user from external IDP. |
| **nameIDPolicyFormat**  string | Specifies the URI reference corresponding to a name identifier format. |
| **principalType**  string | Way to identify and track external users from the assertion. |
| **singleLogoutServiceUrl**  string | The URL that must be used to send logout requests. |
| **singleSignOnServiceUrl**  string | The URL that must be used to send authentication requests (SAML AuthnRequest). |
| **sync_mode**  aliases: syncMode  string | Default sync mode for all mappers. The sync mode determines when user data will be synced using the mappers. |
| **tokenUrl**  string | The Token URL. |
| **useJwksUrl**  boolean | If the switch is on, identity provider public keys will be downloaded from given JWKS URL.  Choices:   - `false` - `true` |
| **userInfoUrl**  string | The User Info URL. |
| **validateSignature**  boolean | Enable/disable signature validation of external IDP signatures.  Choices:   - `false` - `true` |
| **connection_timeout**  integer  added in community.general 4.5.0 | Controls the HTTP connections timeout period (in seconds) to Keycloak API.  Default: `10` |
| **display_name**  aliases: displayName  string | Friendly name for identity provider. |
| **enabled**  boolean | Enable/disable this identity provider.  Choices:   - `false` - `true` |
| **first_broker_login_flow_alias**  aliases: firstBrokerLoginFlowAlias  string | Alias of authentication flow, which is triggered after first login with this identity provider. |
| **http_agent**  string  added in community.general 5.4.0 | Configures the HTTP User-Agent header.  Default: `"Ansible"` |
| **link_only**  aliases: linkOnly  boolean | If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don’t want to allow login from the provider, but want to integrate with a provider.  Choices:   - `false` - `true` |
| **mappers**  list / elements=dictionary | A list of dicts defining mappers associated with this Identity Provider. |
| **config**  dictionary | Dict specifying the configuration options for the mapper; the contents differ depending on the value of *identityProviderMapper*. |
| **id**  string | Unique ID of this mapper. |
| **identityProviderAlias**  string | Alias of the identity provider for this mapper. |
| **identityProviderMapper**  string | Type of mapper. |
| **name**  string | Name of the mapper. |
| **post_broker_login_flow_alias**  aliases: postBrokerLoginFlowAlias  string | Alias of authentication flow, which is triggered after each login with this identity provider. |
| **provider_id**  aliases: providerId  string | Protocol used by this provider (supported values are `oidc` or `saml`). |
| **realm**  string | The Keycloak realm under which this identity provider resides.  Default: `"master"` |
| **state**  string | State of the identity provider.  On `present`, the identity provider will be created if it does not yet exist, or updated with the parameters you provide.  On `absent`, the identity provider will be removed if it exists.  Choices:   - `"present"` ← (default) - `"absent"` |
| **store_token**  aliases: storeToken  boolean | Enable/disable whether tokens must be stored after authenticating users.  Choices:   - `false` - `true` |
| **token**  string  added in community.general 3.0.0 | Authentication token for Keycloak API. |
| **trust_email**  aliases: trustEmail  boolean | If enabled, email provided by this provider is not verified even if verification is enabled for the realm.  Choices:   - `false` - `true` |
| **validate_certs**  boolean | Verify TLS certificates (do not disable this in production).  Choices:   - `false` - `true` ← (default) |

## [Examples](keycloak_identity_provider_module.md#id3)

```yaml+jinja
- name: Create OIDC identity provider, authentication with credentials
  community.general.keycloak_identity_provider:
    state: present
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: admin
    auth_password: admin
    realm: myrealm
    alias: oidc-idp
    display_name: OpenID Connect IdP
    enabled: true
    provider_id: oidc
    config:
      issuer: https://idp.example.com
      authorizationUrl: https://idp.example.com/auth
      tokenUrl: https://idp.example.com/token
      userInfoUrl: https://idp.example.com/userinfo
      clientAuthMethod: client_secret_post
      clientId: my-client
      clientSecret: secret
      syncMode: FORCE
    mappers:
      - name: first_name
        identityProviderMapper: oidc-user-attribute-idp-mapper
        config:
          claim: first_name
          user.attribute: first_name
          syncMode: INHERIT
      - name: last_name
        identityProviderMapper: oidc-user-attribute-idp-mapper
        config:
          claim: last_name
          user.attribute: last_name
          syncMode: INHERIT

- name: Create SAML identity provider, authentication with credentials
  community.general.keycloak_identity_provider:
    state: present
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: admin
    auth_password: admin
    realm: myrealm
    alias: saml-idp
    display_name: SAML IdP
    enabled: true
    provider_id: saml
    config:
      entityId: https://auth.example.com/auth/realms/myrealm
      singleSignOnServiceUrl: https://idp.example.com/login
      wantAuthnRequestsSigned: true
      wantAssertionsSigned: true
    mappers:
      - name: roles
        identityProviderMapper: saml-user-attribute-idp-mapper
        config:
          user.attribute: roles
          attribute.friendly.name: User Roles
          attribute.name: roles
          syncMode: INHERIT
```

## [Return Values](keycloak_identity_provider_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **end_state**  dictionary | Representation of identity provider after module execution.  Returned: on success  Sample: `{"addReadTokenRoleOnCreate": false, "alias": "my-idp", "authenticateByDefault": false, "config": {"authorizationUrl": "https://idp.example.com/auth", "clientAuthMethod": "client_secret_post", "clientId": "my-client", "clientSecret": "**********", "issuer": "https://idp.example.com", "tokenUrl": "https://idp.example.com/token", "userInfoUrl": "https://idp.example.com/userinfo"}, "displayName": "OpenID Connect IdP", "enabled": true, "firstBrokerLoginFlowAlias": "first broker login", "internalId": "4d28d7e3-1b80-45bb-8a30-5822bf55aa1c", "linkOnly": false, "providerId": "oidc", "storeToken": false, "trustEmail": false}` |
| **existing**  dictionary | Representation of existing identity provider.  Returned: always  Sample: `{"addReadTokenRoleOnCreate": false, "alias": "my-idp", "authenticateByDefault": false, "config": {"authorizationUrl": "https://old.example.com/auth", "clientAuthMethod": "client_secret_post", "clientId": "my-client", "clientSecret": "**********", "issuer": "https://old.example.com", "syncMode": "FORCE", "tokenUrl": "https://old.example.com/token", "userInfoUrl": "https://old.example.com/userinfo"}, "displayName": "OpenID Connect IdP", "enabled": true, "firstBrokerLoginFlowAlias": "first broker login", "internalId": "4d28d7e3-1b80-45bb-8a30-5822bf55aa1c", "linkOnly": false, "providerId": "oidc", "storeToken": false, "trustEmail": false}` |
| **msg**  string | Message as to what action was taken.  Returned: always  Sample: `"Identity provider my-idp has been created"` |
| **proposed**  dictionary | Representation of proposed identity provider.  Returned: always  Sample: `{"config": {"authorizationUrl": "https://idp.example.com/auth", "clientAuthMethod": "client_secret_post", "clientId": "my-client", "clientSecret": "secret", "issuer": "https://idp.example.com", "tokenUrl": "https://idp.example.com/token", "userInfoUrl": "https://idp.example.com/userinfo"}, "displayName": "OpenID Connect IdP", "providerId": "oidc"}` |

### Authors

- Laurent Paumier (@laurpaum)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
