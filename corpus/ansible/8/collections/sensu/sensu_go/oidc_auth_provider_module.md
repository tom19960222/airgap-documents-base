---
collection: ansible
version: "8"
title: "sensu.sensu_go.oidc_auth_provider module – Manage Sensu OIDC authentication provider"
source_url: https://docs.ansible.com/projects/ansible/8/collections/sensu/sensu_go/oidc_auth_provider_module.html
fetched_at: 2026-07-28T02:53:23+00:00
---
# sensu.sensu_go.oidc_auth_provider module – Manage Sensu OIDC authentication provider

> **Note:**
>
> This module is part of the [sensu.sensu_go collection](https://galaxy.ansible.com/ui/repo/published/sensu/sensu_go/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install sensu.sensu_go`.
> You need further requirements to be able to use this module,
> see [Requirements](oidc_auth_provider_module.md#ansible-collections-sensu-sensu-go-oidc-auth-provider-module-requirements) for details.
>
> To use it in a playbook, specify: `sensu.sensu_go.oidc_auth_provider`.

New in sensu.sensu_go 1.10.0

- [Synopsis](oidc_auth_provider_module.md#synopsis)
- [Requirements](oidc_auth_provider_module.md#requirements)
- [Parameters](oidc_auth_provider_module.md#parameters)
- [Notes](oidc_auth_provider_module.md#notes)
- [See Also](oidc_auth_provider_module.md#see-also)
- [Examples](oidc_auth_provider_module.md#examples)
- [Return Values](oidc_auth_provider_module.md#return-values)

## [Synopsis](oidc_auth_provider_module.md#id1)

- Create, update or delete a Sensu Go OIDC authentication provider.
- For more information, refer to the Sensu Go documentation at <https://docs.sensu.io/sensu-go/latest/operations/control-access/oidc-auth/>.

## [Requirements](oidc_auth_provider_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7

## [Parameters](oidc_auth_provider_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **additional_scopes**  list / elements=string | Scopes to include in the claims.  **Default:** `["openid"]` |
| **auth**  dictionary | Authentication parameters. Can define each of them with ENV as well. |
| **api_key**  string  *added in sensu.sensu_go 1.3.0* | The API key that should be used when authenticating. If this is not set, the value of the SENSU_API_KEY environment variable will be checked.  This replaces *auth.user* and *auth.password* parameters.  For more information about the API key, refer to the official Sensu documentation at <https://docs.sensu.io/sensu-go/latest/guides/use-apikey-feature/>. |
| **ca_path**  path  *added in sensu.sensu_go 1.5.0* | Path to the CA bundle that should be used to validate the backend certificate.  If this parameter is not set, module will use the CA bundle that python is using.  It is also possible to set this parameter via the *SENSU_CA_PATH* environment variable. |
| **password**  string | The Sensu user’s password. If this is not set the value of the SENSU_PASSWORD environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  **Default:** `"P@ssw0rd!"` |
| **url**  string | Location of the Sensu backend API. If this is not set the value of the SENSU_URL environment variable will be checked.  **Default:** `"http://localhost:8080"` |
| **user**  string | The username to use for connecting to the Sensu API. If this is not set the value of the SENSU_USER environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  **Default:** `"admin"` |
| **verify**  boolean  *added in sensu.sensu_go 1.5.0* | Flag that controls the certificate validation.  If you are using self-signed certificates, you can set this parameter to `false`.  ONLY USE THIS PARAMETER IN DEVELOPMENT SCENARIOS! In you use self-signed certificates in production, see the *auth.ca_path* parameter.  It is also possible to set this parameter via the *SENSU_VERIFY* environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **client_id**  string | The OIDC provider application Client ID.  Required if *state* is `present`. |
| **client_secret**  string | The OIDC provider application Client Secret.  Required if *state* is `present`. |
| **disable_offline_access**  boolean | If `true`, the OIDC provider cannot include the offline_access scope in the authentication request. Otherwise, `false`.  **Choices:**   - `false` ← (default) - `true` |
| **groups_claim**  string | The claim to use to form the associated RBAC groups. |
| **groups_prefix**  string | The prefix added to all OIDC groups. |
| **name**  string / required | The Sensu resource’s name. This name (in combination with the namespace where applicable) uniquely identifies the resource that Ansible operates on.  If the resource with selected name already exists, Ansible module will update it to match the specification in the task.  Consult the *name* metadata attribute specification in the upstream docs on <https://docs.sensu.io/sensu-go/latest/reference/> for more details about valid names and other restrictions. |
| **redirect_uri**  string | Redirect URL to provide to the OIDC provider. |
| **server**  string | The location of the OIDC server you wish to authenticate against.  Required if *state* is `present`. |
| **state**  string | Target state of the Sensu object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username_claim**  string | The claim to use to form the final RBAC user name.  Required if *state* is `present`. |
| **username_prefix**  string | The prefix added to all OIDC usernames. |

## [Notes](oidc_auth_provider_module.md#id4)

> **Note:**
>
> - Supported only on Sensu Go versions >= 6.

## [See Also](oidc_auth_provider_module.md#id5)

> **See also:**
>
> [sensu.sensu_go.auth_provider_info](auth_provider_info_module.md#ansible-collections-sensu-sensu-go-auth-provider-info-module)
> :   List Sensu authentication providers.
>
> [sensu.sensu_go.ldap_auth_provider](ldap_auth_provider_module.md#ansible-collections-sensu-sensu-go-ldap-auth-provider-module)
> :   Manage Sensu LDAP authentication provider.
>
> [sensu.sensu_go.ad_auth_provider](ad_auth_provider_module.md#ansible-collections-sensu-sensu-go-ad-auth-provider-module)
> :   Manage Sensu AD authentication provider.

## [Examples](oidc_auth_provider_module.md#id6)

```yaml+jinja
- name: Create a OIDC auth provider
  sensu.sensu_go.oidc_auth_provider:
    state: present
    name: oidc_name
    additional_scopes:
        - groups
        - email
    client_id: a8e43af034e7f2608780
    client_secret: b63968394be6ed2edb61c93847ee792f31bf6216
    disable_offline_access: false
    redirect_uri: http://127.0.0.1:8080/api/enterprise/authentication/v2/oidc/callback
    server: https://oidc.example.com:9031
    groups_claim: groups
    groups_prefix: 'oidc:'
    username_claim: email
    username_prefix: 'oidc:'

- name: Delete a OIDC auth provider
  sensu.sensu_go.oidc_auth_provider:
    name: oidc_name
    state: absent
```

## [Return Values](oidc_auth_provider_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **object**  dictionary | Object representing Sensu OIDC authentication provider.  **Returned:** success  **Sample:** `{"additional_scopes": ["groups", "email"], "client_id": "a8e43af034e7f2608780", "disable_offline_access": false, "groups_claim": "groups", "groups_prefix": "oidc:", "metadata": {"created_by": "admin", "name": "oidc_name"}, "redirect_uri": "http://sensu-backend.example.com:8080/api/enterprise/authentication/v2/oidc/callback", "server": "https://oidc.example.com:9031", "username_claim": "email", "username_prefix": "oidc:"}` |

### Authors

- Aljaz Kosir (@aljazkosir)
- Manca Bizjak (@mancabizjak)
- Miha Dolinar (@mdolin)
- Tadej Borovsak (@tadeboro)

### Collection links

- [Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
- [Repository (Sources)](https://github.com/sensu/sensu-go-ansible)
