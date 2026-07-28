---
collection: ansible
version: "6"
title: "community.general.keycloak_authentication module – Configure authentication in Keycloak"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/keycloak_authentication_module.html
fetched_at: 2026-07-27T17:10:16+00:00
---
# community.general.keycloak_authentication module – Configure authentication in Keycloak

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
> To use it in a playbook, specify: `community.general.keycloak_authentication`.

New in community.general 3.3.0

- [Synopsis](keycloak_authentication_module.md#synopsis)
- [Parameters](keycloak_authentication_module.md#parameters)
- [Examples](keycloak_authentication_module.md#examples)
- [Return Values](keycloak_authentication_module.md#return-values)

## [Synopsis](keycloak_authentication_module.md#id1)

- This module actually can only make a copy of an existing authentication flow, add an execution to it and configure it.
- It can also delete the flow.

## [Parameters](keycloak_authentication_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **alias**  string / required | Alias for the authentication flow. |
| **auth_client_id**  string | OpenID Connect *client_id* to authenticate to the API with.  Default: `"admin-cli"` |
| **auth_client_secret**  string | Client Secret to use in conjunction with *auth_client_id* (if required). |
| **auth_keycloak_url**  aliases: url  string / required | URL to the Keycloak instance. |
| **auth_password**  aliases: password  string | Password to authenticate for API access with. |
| **auth_realm**  string | Keycloak realm name to authenticate to for API access. |
| **auth_username**  aliases: username  string | Username to authenticate for API access with. |
| **authenticationExecutions**  list / elements=dictionary | Configuration structure for the executions. |
| **authenticationConfig**  dictionary | Describe the config of the authentication. |
| **displayName**  string | Name of the execution or subflow to create or update. |
| **flowAlias**  string | Alias of parent flow. |
| **index**  integer | Priority order of the execution. |
| **providerId**  string | `providerID` for the new flow when not copied from an existing flow. |
| **requirement**  string | Control status of the subflow or execution.  Choices:   - `"REQUIRED"` - `"ALTERNATIVE"` - `"DISABLED"` - `"CONDITIONAL"` |
| **connection_timeout**  integer  added in community.general 4.5.0 | Controls the HTTP connections timeout period (in seconds) to Keycloak API.  Default: `10` |
| **copyFrom**  string | `flowAlias` of the authentication flow to use for the copy. |
| **description**  string | Description of the flow. |
| **force**  boolean | If `true`, allows to remove the authentication flow and recreate it.  Choices:   - `false` ← (default) - `true` |
| **http_agent**  string  added in community.general 5.4.0 | Configures the HTTP User-Agent header.  Default: `"Ansible"` |
| **providerId**  string | `providerId` for the new flow when not copied from an existing flow. |
| **realm**  string / required | The name of the realm in which is the authentication. |
| **state**  string | Control if the authentication flow must exists or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **token**  string  added in community.general 3.0.0 | Authentication token for Keycloak API. |
| **validate_certs**  boolean | Verify TLS certificates (do not disable this in production).  Choices:   - `false` - `true` ← (default) |

## [Examples](keycloak_authentication_module.md#id3)

```yaml+jinja
- name: Create an authentication flow from first broker login and add an execution to it.
  community.general.keycloak_authentication:
    auth_keycloak_url: http://localhost:8080/auth
    auth_realm: master
    auth_username: admin
    auth_password: password
    realm: master
    alias: "Copy of first broker login"
    copyFrom: "first broker login"
    authenticationExecutions:
      - providerId: "test-execution1"
        requirement: "REQUIRED"
        authenticationConfig:
          alias: "test.execution1.property"
          config:
            test1.property: "value"
      - providerId: "test-execution2"
        requirement: "REQUIRED"
        authenticationConfig:
          alias: "test.execution2.property"
          config:
            test2.property: "value"
    state: present

- name: Re-create the authentication flow
  community.general.keycloak_authentication:
    auth_keycloak_url: http://localhost:8080/auth
    auth_realm: master
    auth_username: admin
    auth_password: password
    realm: master
    alias: "Copy of first broker login"
    copyFrom: "first broker login"
    authenticationExecutions:
      - providerId: "test-provisioning"
        requirement: "REQUIRED"
        authenticationConfig:
          alias: "test.provisioning.property"
          config:
            test.provisioning.property: "value"
    state: present
    force: true

- name: Create an authentication flow with subflow containing an execution.
  community.general.keycloak_authentication:
    auth_keycloak_url: http://localhost:8080/auth
    auth_realm: master
    auth_username: admin
    auth_password: password
    realm: master
    alias: "Copy of first broker login"
    copyFrom: "first broker login"
    authenticationExecutions:
      - providerId: "test-execution1"
        requirement: "REQUIRED"
      - displayName: "New Subflow"
        requirement: "REQUIRED"
      - providerId: "auth-cookie"
        requirement: "REQUIRED"
        flowAlias: "New Sublow"
    state: present

- name: Remove authentication.
  community.general.keycloak_authentication:
    auth_keycloak_url: http://localhost:8080/auth
    auth_realm: master
    auth_username: admin
    auth_password: password
    realm: master
    alias: "Copy of first broker login"
    state: absent
```

## [Return Values](keycloak_authentication_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **end_state**  dictionary | Representation of the authentication after module execution.  Returned: on success  Sample: `{"alias": "Copy of first broker login", "authenticationExecutions": [{"alias": "review profile config", "authenticationConfig": {"alias": "review profile config", "config": {"update.profile.on.first.login": "missing"}, "id": "6f09e4fb-aad4-496a-b873-7fa9779df6d7"}, "configurable": true, "displayName": "Review Profile", "id": "8f77dab8-2008-416f-989e-88b09ccf0b4c", "index": 0, "level": 0, "providerId": "idp-review-profile", "requirement": "REQUIRED", "requirementChoices": ["REQUIRED", "ALTERNATIVE", "DISABLED"]}], "builtIn": false, "description": "Actions taken after first broker login with identity provider account, which is not yet linked to any Keycloak account", "id": "bc228863-5887-4297-b898-4d988f8eaa5c", "providerId": "basic-flow", "topLevel": true}` |
| **flow**  dictionary | JSON representation for the authentication.  Deprecated return value, it will be removed in community.general 6.0.0. Please use the return value *end_state* instead.  Returned: on success  Sample: `{"alias": "Copy of first broker login", "authenticationExecutions": [{"alias": "review profile config", "authenticationConfig": {"alias": "review profile config", "config": {"update.profile.on.first.login": "missing"}, "id": "6f09e4fb-aad4-496a-b873-7fa9779df6d7"}, "configurable": true, "displayName": "Review Profile", "id": "8f77dab8-2008-416f-989e-88b09ccf0b4c", "index": 0, "level": 0, "providerId": "idp-review-profile", "requirement": "REQUIRED", "requirementChoices": ["REQUIRED", "ALTERNATIVE", "DISABLED"]}], "builtIn": false, "description": "Actions taken after first broker login with identity provider account, which is not yet linked to any Keycloak account", "id": "bc228863-5887-4297-b898-4d988f8eaa5c", "providerId": "basic-flow", "topLevel": true}` |
| **msg**  string | Message as to what action was taken.  Returned: always |

### Authors

- Philippe Gauthier (@elfelip)
- Gaëtan Daubresse (@Gaetan2907)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
