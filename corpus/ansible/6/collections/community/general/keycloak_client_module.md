---
collection: ansible
version: "6"
title: "community.general.keycloak_client module – Allows administration of Keycloak clients via Keycloak API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/keycloak_client_module.html
fetched_at: 2026-07-27T17:10:17+00:00
---
# community.general.keycloak_client module – Allows administration of Keycloak clients via Keycloak API

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
> To use it in a playbook, specify: `community.general.keycloak_client`.

- [Synopsis](keycloak_client_module.md#synopsis)
- [Parameters](keycloak_client_module.md#parameters)
- [Examples](keycloak_client_module.md#examples)
- [Return Values](keycloak_client_module.md#return-values)

## [Synopsis](keycloak_client_module.md#id1)

- This module allows the administration of Keycloak clients via the Keycloak REST API. It requires access to the REST API via OpenID Connect; the user connecting and the client being used must have the requisite access rights. In a default Keycloak installation, admin-cli and an admin user would work, as would a separate client definition with the scope tailored to your needs and a user having the expected roles.
- The names of module options are snake_cased versions of the camelCase ones found in the Keycloak API and its documentation at <https://www.keycloak.org/docs-api/8.0/rest-api/index.html>. Aliases are provided so camelCased versions can be used as well.
- The Keycloak API does not always sanity check inputs e.g. you can set SAML-specific settings on an OpenID Connect client for instance and vice versa. Be careful. If you do not specify a setting, usually a sensible default is chosen.

## [Parameters](keycloak_client_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **admin_url**  aliases: adminUrl  string | URL to the admin interface of the client. This is ‘adminUrl’ in the Keycloak REST API. |
| **always_display_in_console**  aliases: alwaysDisplayInConsole  boolean  added in community.general 4.7.0 | Whether or not to display this client in account console, even if the user does not have an active session.  Choices:   - `false` - `true` |
| **attributes**  dictionary | A dict of further attributes for this client. This can contain various configuration settings; an example is given in the examples section. While an exhaustive list of permissible options is not available; possible options as of Keycloak 3.4 are listed below. The Keycloak API does not validate whether a given option is appropriate for the protocol used; if specified anyway, Keycloak will simply not use it. |
| **jwks.url**  string | For OpenID-Connect clients, URL where client keys in JWK are stored. |
| **jwt.credential.certificate**  string | For OpenID-Connect clients, client certificate for validating JWT issued by client and signed by its key, base64-encoded. |
| **request.object.signature.alg**  string | For OpenID-Connect clients, JWA algorithm which the client needs to use when sending OIDC request object. One of `any`, `none`, `RS256`. |
| **saml.authnstatement**  string | For SAML clients, boolean specifying whether or not a statement containing method and timestamp should be included in the login response. |
| **saml.client.signature**  string | For SAML clients, boolean specifying whether a client signature is required and validated. |
| **saml.encrypt**  string | Boolean specifying whether SAML assertions should be encrypted with the client’s public key. |
| **saml.force.post.binding**  string | For SAML clients, boolean specifying whether always to use POST binding for responses. |
| **saml.onetimeuse.condition**  string | For SAML clients, boolean specifying whether a OneTimeUse condition should be included in login responses. |
| **saml.server.signature**  string | Boolean specifying whether SAML documents should be signed by the realm. |
| **saml.server.signature.keyinfo.ext**  string | For SAML clients, boolean specifying whether REDIRECT signing key lookup should be optimized through inclusion of the signing key id in the SAML Extensions element. |
| **saml.signature.algorithm**  string | Signature algorithm used to sign SAML documents. One of `RSA_SHA256`, `RSA_SHA1`, `RSA_SHA512`, or `DSA_SHA1`. |
| **saml.signing.certificate**  string | SAML signing key certificate, base64-encoded. |
| **saml.signing.private.key**  string | SAML signing key private key, base64-encoded. |
| **saml_assertion_consumer_url_post**  string | SAML POST Binding URL for the client’s assertion consumer service (login responses). |
| **saml_assertion_consumer_url_redirect**  string | SAML Redirect Binding URL for the client’s assertion consumer service (login responses). |
| **saml_force_name_id_format**  string | For SAML clients, Boolean specifying whether to ignore requested NameID subject format and using the configured one instead. |
| **saml_name_id_format**  string | For SAML clients, the NameID format to use (one of `username`, `email`, `transient`, or `persistent`) |
| **saml_signature_canonicalization_method**  string | SAML signature canonicalization method. This is one of four values, namely `http://www.w3.org/2001/10/xml-exc-c14n#` for EXCLUSIVE, `http://www.w3.org/2001/10/xml-exc-c14n#WithComments` for EXCLUSIVE_WITH_COMMENTS, `http://www.w3.org/TR/2001/REC-xml-c14n-20010315` for INCLUSIVE, and `http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments` for INCLUSIVE_WITH_COMMENTS. |
| **saml_single_logout_service_url_post**  string | SAML POST binding url for the client’s single logout service. |
| **saml_single_logout_service_url_redirect**  string | SAML redirect binding url for the client’s single logout service. |
| **use.jwks.url**  string | For OpenID-Connect clients, boolean specifying whether to use a JWKS URL to obtain client public keys. |
| **user.info.response.signature.alg**  string | For OpenID-Connect clients, JWA algorithm for signed UserInfo-endpoint responses. One of `RS256` or `unsigned`. |
| **auth_client_id**  string | OpenID Connect *client_id* to authenticate to the API with.  Default: `"admin-cli"` |
| **auth_client_secret**  string | Client Secret to use in conjunction with *auth_client_id* (if required). |
| **auth_keycloak_url**  aliases: url  string / required | URL to the Keycloak instance. |
| **auth_password**  aliases: password  string | Password to authenticate for API access with. |
| **auth_realm**  string | Keycloak realm name to authenticate to for API access. |
| **auth_username**  aliases: username  string | Username to authenticate for API access with. |
| **authentication_flow_binding_overrides**  aliases: authenticationFlowBindingOverrides  dictionary  added in community.general 3.4.0 | Override realm authentication flow bindings. |
| **authorization_services_enabled**  aliases: authorizationServicesEnabled  boolean | Are authorization services enabled for this client or not (OpenID connect). This is ‘authorizationServicesEnabled’ in the Keycloak REST API.  Choices:   - `false` - `true` |
| **authorization_settings**  aliases: authorizationSettings  dictionary | a data structure defining the authorization settings for this client. For reference, please see the Keycloak API docs at <https://www.keycloak.org/docs-api/8.0/rest-api/index.html#_resourceserverrepresentation>. This is ‘authorizationSettings’ in the Keycloak REST API. |
| **base_url**  aliases: baseUrl  string | Default URL to use when the auth server needs to redirect or link back to the client This is ‘baseUrl’ in the Keycloak REST API. |
| **bearer_only**  aliases: bearerOnly  boolean | The access type of this client is bearer-only. This is ‘bearerOnly’ in the Keycloak REST API.  Choices:   - `false` - `true` |
| **client_authenticator_type**  aliases: clientAuthenticatorType  string | How do clients authenticate with the auth server? Either `client-secret` or `client-jwt` can be chosen. When using `client-secret`, the module parameter *secret* can set it, while for `client-jwt`, you can use the keys `use.jwks.url`, `jwks.url`, and `jwt.credential.certificate` in the *attributes* module parameter to configure its behavior. This is ‘clientAuthenticatorType’ in the Keycloak REST API.  Choices:   - `"client-secret"` - `"client-jwt"` |
| **client_id**  aliases: clientId  string | Client id of client to be worked on. This is usually an alphanumeric name chosen by you. Either this or *id* is required. If you specify both, *id* takes precedence. This is ‘clientId’ in the Keycloak REST API. |
| **client_template**  aliases: clientTemplate  string | Client template to use for this client. If it does not exist this field will silently be dropped. This is ‘clientTemplate’ in the Keycloak REST API. |
| **connection_timeout**  integer  added in community.general 4.5.0 | Controls the HTTP connections timeout period (in seconds) to Keycloak API.  Default: `10` |
| **consent_required**  aliases: consentRequired  boolean | If enabled, users have to consent to client access. This is ‘consentRequired’ in the Keycloak REST API.  Choices:   - `false` - `true` |
| **default_client_scopes**  aliases: defaultClientScopes  list / elements=string  added in community.general 4.7.0 | List of default client scopes. |
| **default_roles**  aliases: defaultRoles  list / elements=string | list of default roles for this client. If the client roles referenced do not exist yet, they will be created. This is ‘defaultRoles’ in the Keycloak REST API. |
| **description**  string | Description of the client in Keycloak. |
| **direct_access_grants_enabled**  aliases: directAccessGrantsEnabled  boolean | Are direct access grants enabled for this client or not (OpenID connect). This is ‘directAccessGrantsEnabled’ in the Keycloak REST API.  Choices:   - `false` - `true` |
| **enabled**  boolean | Is this client enabled or not?  Choices:   - `false` - `true` |
| **frontchannel_logout**  aliases: frontchannelLogout  boolean | Is frontchannel logout enabled for this client or not. This is ‘frontchannelLogout’ in the Keycloak REST API.  Choices:   - `false` - `true` |
| **full_scope_allowed**  aliases: fullScopeAllowed  boolean | Is the “Full Scope Allowed” feature set for this client or not. This is ‘fullScopeAllowed’ in the Keycloak REST API.  Choices:   - `false` - `true` |
| **http_agent**  string  added in community.general 5.4.0 | Configures the HTTP User-Agent header.  Default: `"Ansible"` |
| **id**  string | Id of client to be worked on. This is usually an UUID. Either this or *client_id* is required. If you specify both, this takes precedence. |
| **implicit_flow_enabled**  aliases: implicitFlowEnabled  boolean | Enable implicit flow for this client or not (OpenID connect). This is ‘implicitFlowEnabled’ in the Keycloak REST API.  Choices:   - `false` - `true` |
| **name**  string | Name of the client (this is not the same as *client_id*). |
| **node_re_registration_timeout**  aliases: nodeReRegistrationTimeout  integer | Cluster node re-registration timeout for this client. This is ‘nodeReRegistrationTimeout’ in the Keycloak REST API. |
| **not_before**  aliases: notBefore  integer | Revoke any tokens issued before this date for this client (this is a UNIX timestamp). This is ‘notBefore’ in the Keycloak REST API. |
| **optional_client_scopes**  aliases: optionalClientScopes  list / elements=string  added in community.general 4.7.0 | List of optional client scopes. |
| **protocol**  string | Type of client (either `openid-connect` or `saml`.  Choices:   - `"openid-connect"` - `"saml"` |
| **protocol_mappers**  aliases: protocolMappers  list / elements=dictionary | a list of dicts defining protocol mappers for this client. This is ‘protocolMappers’ in the Keycloak REST API. |
| **config**  dictionary | Dict specifying the configuration options for the protocol mapper; the contents differ depending on the value of *protocolMapper* and are not documented other than by the source of the mappers and its parent class(es). An example is given below. It is easiest to obtain valid config values by dumping an already-existing protocol mapper configuration through check-mode in the *existing* field. |
| **consentRequired**  boolean | Specifies whether a user needs to provide consent to a client for this mapper to be active.  Choices:   - `false` - `true` |
| **consentText**  string | The human-readable name of the consent the user is presented to accept. |
| **id**  string | Usually a UUID specifying the internal ID of this protocol mapper instance. |
| **name**  string | The name of this protocol mapper. |
| **protocol**  string | This is either `openid-connect` or `saml`, this specifies for which protocol this protocol mapper. is active.  Choices:   - `"openid-connect"` - `"saml"` |
| **protocolMapper**  string | The Keycloak-internal name of the type of this protocol-mapper. While an exhaustive list is impossible to provide since this may be extended through SPIs by the user of Keycloak, by default Keycloak as of 3.4 ships with at least  `docker-v2-allow-all-mapper`  `oidc-address-mapper`  `oidc-full-name-mapper`  `oidc-group-membership-mapper`  `oidc-hardcoded-claim-mapper`  `oidc-hardcoded-role-mapper`  `oidc-role-name-mapper`  `oidc-script-based-protocol-mapper`  `oidc-sha256-pairwise-sub-mapper`  `oidc-usermodel-attribute-mapper`  `oidc-usermodel-client-role-mapper`  `oidc-usermodel-property-mapper`  `oidc-usermodel-realm-role-mapper`  `oidc-usersessionmodel-note-mapper`  `saml-group-membership-mapper`  `saml-hardcode-attribute-mapper`  `saml-hardcode-role-mapper`  `saml-role-list-mapper`  `saml-role-name-mapper`  `saml-user-attribute-mapper`  `saml-user-property-mapper`  `saml-user-session-note-mapper`  An exhaustive list of available mappers on your installation can be obtained on the admin console by going to Server Info -> Providers and looking under ‘protocol-mapper’. |
| **public_client**  aliases: publicClient  boolean | Is the access type for this client public or not. This is ‘publicClient’ in the Keycloak REST API.  Choices:   - `false` - `true` |
| **realm**  string | The realm to create the client in.  Default: `"master"` |
| **redirect_uris**  aliases: redirectUris  list / elements=string | Acceptable redirect URIs for this client. This is ‘redirectUris’ in the Keycloak REST API. |
| **registered_nodes**  aliases: registeredNodes  dictionary | dict of registered cluster nodes (with `nodename` as the key and last registration time as the value). This is ‘registeredNodes’ in the Keycloak REST API. |
| **registration_access_token**  aliases: registrationAccessToken  string | The registration access token provides access for clients to the client registration service. This is ‘registrationAccessToken’ in the Keycloak REST API. |
| **root_url**  aliases: rootUrl  string | Root URL appended to relative URLs for this client. This is ‘rootUrl’ in the Keycloak REST API. |
| **secret**  string | When using *client_authenticator_type* `client-secret` (the default), you can specify a secret here (otherwise one will be generated if it does not exit). If changing this secret, the module will not register a change currently (but the changed secret will be saved). |
| **service_accounts_enabled**  aliases: serviceAccountsEnabled  boolean | Are service accounts enabled for this client or not (OpenID connect). This is ‘serviceAccountsEnabled’ in the Keycloak REST API.  Choices:   - `false` - `true` |
| **standard_flow_enabled**  aliases: standardFlowEnabled  boolean | Enable standard flow for this client or not (OpenID connect). This is ‘standardFlowEnabled’ in the Keycloak REST API.  Choices:   - `false` - `true` |
| **state**  string | State of the client  On `present`, the client will be created (or updated if it exists already).  On `absent`, the client will be removed if it exists  Choices:   - `"present"` ← (default) - `"absent"` |
| **surrogate_auth_required**  aliases: surrogateAuthRequired  boolean | Whether or not surrogate auth is required. This is ‘surrogateAuthRequired’ in the Keycloak REST API.  Choices:   - `false` - `true` |
| **token**  string  added in community.general 3.0.0 | Authentication token for Keycloak API. |
| **use_template_config**  aliases: useTemplateConfig  boolean | Whether or not to use configuration from the *client_template*. This is ‘useTemplateConfig’ in the Keycloak REST API.  Choices:   - `false` - `true` |
| **use_template_mappers**  aliases: useTemplateMappers  boolean | Whether or not to use mapper configuration from the *client_template*. This is ‘useTemplateMappers’ in the Keycloak REST API.  Choices:   - `false` - `true` |
| **use_template_scope**  aliases: useTemplateScope  boolean | Whether or not to use scope configuration from the *client_template*. This is ‘useTemplateScope’ in the Keycloak REST API.  Choices:   - `false` - `true` |
| **validate_certs**  boolean | Verify TLS certificates (do not disable this in production).  Choices:   - `false` - `true` ← (default) |
| **web_origins**  aliases: webOrigins  list / elements=string | List of allowed CORS origins. This is ‘webOrigins’ in the Keycloak REST API. |

## [Examples](keycloak_client_module.md#id3)

```yaml+jinja
- name: Create or update Keycloak client (minimal example), authentication with credentials
  community.general.keycloak_client:
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
    client_id: test
    state: present
  delegate_to: localhost

- name: Create or update Keycloak client (minimal example), authentication with token
  community.general.keycloak_client:
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    token: TOKEN
    client_id: test
    state: present
  delegate_to: localhost

- name: Delete a Keycloak client
  community.general.keycloak_client:
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
    client_id: test
    state: absent
  delegate_to: localhost

- name: Create or update a Keycloak client (with all the bells and whistles)
  community.general.keycloak_client:
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
    state: present
    realm: master
    client_id: test
    id: d8b127a3-31f6-44c8-a7e4-4ab9a3e78d95
    name: this_is_a_test
    description: Description of this wonderful client
    root_url: https://www.example.com/
    admin_url: https://www.example.com/admin_url
    base_url: basepath
    enabled: true
    client_authenticator_type: client-secret
    secret: REALLYWELLKEPTSECRET
    redirect_uris:
      - https://www.example.com/*
      - http://localhost:8888/
    web_origins:
      - https://www.example.com/*
    not_before: 1507825725
    bearer_only: false
    consent_required: false
    standard_flow_enabled: true
    implicit_flow_enabled: false
    direct_access_grants_enabled: false
    service_accounts_enabled: false
    authorization_services_enabled: false
    public_client: false
    frontchannel_logout: false
    protocol: openid-connect
    full_scope_allowed: false
    node_re_registration_timeout: -1
    client_template: test
    use_template_config: false
    use_template_scope: false
    use_template_mappers: false
    always_display_in_console: true
    registered_nodes:
      node01.example.com: 1507828202
    registration_access_token: eyJWT_TOKEN
    surrogate_auth_required: false
    default_roles:
      - test01
      - test02
    authentication_flow_binding_overrides:
        browser: 4c90336b-bf1d-4b87-916d-3677ba4e5fbb
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
      - config:
          attribute.name: Role
          attribute.nameformat: Basic
          single: false
        consentRequired: false
        name: role list
        protocol: saml
        protocolMapper: saml-role-list-mapper
    attributes:
      saml.authnstatement: true
      saml.client.signature: true
      saml.force.post.binding: true
      saml.server.signature: true
      saml.signature.algorithm: RSA_SHA256
      saml.signing.certificate: CERTIFICATEHERE
      saml.signing.private.key: PRIVATEKEYHERE
      saml_force_name_id_format: false
      saml_name_id_format: username
      saml_signature_canonicalization_method: "http://www.w3.org/2001/10/xml-exc-c14n#"
      user.info.response.signature.alg: RS256
      request.object.signature.alg: RS256
      use.jwks.url: true
      jwks.url: JWKS_URL_FOR_CLIENT_AUTH_JWT
      jwt.credential.certificate: JWT_CREDENTIAL_CERTIFICATE_FOR_CLIENT_AUTH
  delegate_to: localhost
```

## [Return Values](keycloak_client_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **end_state**  dictionary | Representation of client after module execution (sample is truncated).  Returned: on success  Sample: `{"adminUrl": "http://www.example.com/admin_url", "attributes": {"request.object.signature.alg": "RS256"}}` |
| **existing**  dictionary | Representation of existing client (sample is truncated).  Returned: always  Sample: `{"adminUrl": "http://www.example.com/admin_url", "attributes": {"request.object.signature.alg": "RS256"}}` |
| **msg**  string | Message as to what action was taken.  Returned: always  Sample: `"Client testclient has been updated"` |
| **proposed**  dictionary | Representation of proposed client.  Returned: always  Sample: `{"clientId": "test"}` |

### Authors

- Eike Frost (@eikef)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
