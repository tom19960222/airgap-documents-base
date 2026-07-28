---
collection: ansible
version: "6"
title: "community.hashi_vault.vault_token_create module – Create a HashiCorp Vault token"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/hashi_vault/vault_token_create_module.html
fetched_at: 2026-07-27T17:15:43+00:00
---
# community.hashi_vault.vault_token_create module – Create a HashiCorp Vault token

> **Note:**
>
> This module is part of the [community.hashi_vault collection](https://galaxy.ansible.com/community/hashi_vault) (version 3.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.hashi_vault`.
> You need further requirements to be able to use this module,
> see [Requirements](vault_token_create_module.md#ansible-collections-community-hashi-vault-vault-token-create-module-requirements) for details.
>
> To use it in a playbook, specify: `community.hashi_vault.vault_token_create`.

New in community.hashi_vault 2.3.0

- [Synopsis](vault_token_create_module.md#synopsis)
- [Requirements](vault_token_create_module.md#requirements)
- [Parameters](vault_token_create_module.md#parameters)
- [Notes](vault_token_create_module.md#notes)
- [See Also](vault_token_create_module.md#see-also)
- [Examples](vault_token_create_module.md#examples)
- [Return Values](vault_token_create_module.md#return-values)

## [Synopsis](vault_token_create_module.md#id1)

- Creates a token in HashiCorp Vault, returning the response, including the token.

## [Requirements](vault_token_create_module.md#id2)

The below requirements are needed on the host that executes this module.

- `hvac` ([Python library](https://hvac.readthedocs.io/en/stable/overview.html))
- For detailed requirements, see [the collection requirements page](docsite/user_guide.md#ansible-collections-community-hashi-vault-docsite-user-guide-requirements).

## [Parameters](vault_token_create_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_method**  string | Authentication method to be used.  `none` auth method was added in collection version `1.2.0`.  `cert` auth method was added in collection version `1.4.0`.  `aws_iam_login` was renamed `aws_iam` in collection version `2.1.0` and was removed in `3.0.0`.  `azure` auth method was added in collection version `3.2.0`.  Choices:   - `"token"` ← (default) - `"userpass"` - `"ldap"` - `"approle"` - `"aws_iam"` - `"azure"` - `"jwt"` - `"cert"` - `"none"` |
| **aws_access_key**  aliases: aws_access_key_id  string | The AWS access key to use. |
| **aws_iam_server_id**  string  added in community.hashi_vault 0.2.0 | If specified, sets the value to use for the `X-Vault-AWS-IAM-Server-ID` header as part of `GetCallerIdentity` request. |
| **aws_profile**  aliases: boto_profile  string | The AWS profile |
| **aws_secret_key**  aliases: aws_secret_access_key  string | The AWS secret key that corresponds to the access key. |
| **aws_security_token**  string | The AWS security token if using temporary access and secret keys. |
| **azure_client_id**  string  added in community.hashi_vault 3.2.0 | The client ID (also known as application ID) of the Azure AD service principal or managed identity. Should be a UUID.  If not specified, will use the system assigned managed identity. |
| **azure_client_secret**  string  added in community.hashi_vault 3.2.0 | The client secret of the Azure AD service principal. |
| **azure_resource**  string  added in community.hashi_vault 3.2.0 | The resource URL for the application registered in Azure Active Directory. Usually should not be changed from the default.  Default: `"https://management.azure.com/"` |
| **azure_tenant_id**  string  added in community.hashi_vault 3.2.0 | The Azure Active Directory Tenant ID (also known as the Directory ID) of the service principal. Should be a UUID.  Required when using a service principal to authenticate to Vault, e.g. required when both *azure_client_id* and *azure_client_secret* are specified.  Optional when using managed identity to authenticate to Vault. |
| **ca_cert**  aliases: cacert  string | Path to certificate to use for authentication.  If not specified by any other means, the `VAULT_CACERT` environment variable will be used. |
| **cert_auth_private_key**  path  added in community.hashi_vault 1.4.0 | For `cert` auth, path to the private key file to authenticate with, in PEM format. |
| **cert_auth_public_key**  path  added in community.hashi_vault 1.4.0 | For `cert` auth, path to the certificate file to authenticate with, in PEM format. |
| **display_name**  string | The display name of the token. |
| **entity_alias**  string | Name of the entity alias to associate with during token creation.  Only works in combination with *role_name* option and used entity alias must be listed in `allowed_entity_aliases`.  If this has been specified, the entity will not be inherited from the parent. |
| **explicit_max_ttl**  string | If set, the token will have an explicit max TTL set upon it.  This maximum token TTL cannot be changed later, and unlike with normal tokens, updates to the system/mount max TTL value will have no effect at renewal time.  The token will never be able to be renewed or used past the value set at issue time. |
| **id**  string | The ID of the client token. Can only be specified by a root token.  The ID provided may not contain a `.` character.  Otherwise, the token ID is a randomly generated value. |
| **jwt**  string | The JSON Web Token (JWT) to use for JWT authentication to Vault. |
| **meta**  dictionary | A dict of string to string valued metadata. This is passed through to the audit devices. |
| **mount_point**  string | Vault mount point.  If not specified, the default mount point for a given auth method is used.  Does not apply to token authentication. |
| **namespace**  string | Vault namespace where secrets reside. This option requires HVAC 0.7.0+ and Vault 0.11+.  Optionally, this may be achieved by prefixing the authentication mount point and/or secret path with the namespace (e.g `mynamespace/secret/mysecret`).  If environment variable `VAULT_NAMESPACE` is set, its value will be used last among all ways to specify *namespace*. |
| **no_default_policy**  boolean | If `true` the default policy will not be contained in this token’s policy set.  If the token will be used with this collection, set *token_validate=false*.  Choices:   - `false` - `true` |
| **no_parent**  boolean | This option only has effect if used by a `root` or `sudo` caller and only when *orphan=false*.  When `true`, the token created will not have a parent.  Choices:   - `false` - `true` |
| **num_uses**  integer | The maximum uses for the given token. This can be used to create a one-time-token or limited use token.  The value of `0` has no limit to the number of uses. |
| **orphan**  boolean | When `true`, uses the `/create-orphan` API endpoint, which requires `sudo` (but not `root`) to create an orphan.  With `hvac>=1.0.0`, requires collection version `>=3.3.0`.  Choices:   - `false` ← (default) - `true` |
| **password**  string | Authentication password. |
| **period**  string | If specified, the token will be periodic.  It will have no maximum TTL (unless an *explicit_max_ttl* is also set) but every renewal will use the given period.  Requires a root token or one with the `sudo` capability. |
| **policies**  list / elements=string | A list of policies for the token. This must be a subset of the policies belonging to the token making the request, unless root.  If not specified, defaults to all the policies of the calling token. |
| **proxies**  any  added in community.hashi_vault 1.1.0 | URL(s) to the proxies used to access the Vault service.  It can be a string or a dict.  If it’s a dict, provide the scheme (eg. `http` or `https`) as the key, and the URL as the value.  If it’s a string, provide a single URL that will be used as the proxy for both `http` and `https` schemes.  A string that can be interpreted as a dictionary will be converted to one (see examples).  You can specify a different proxy for HTTP and HTTPS resources.  If not specified, [environment variables from the Requests library](https://requests.readthedocs.io/en/master/user/advanced/#proxies) are used. |
| **region**  string | The AWS region for which to create the connection. |
| **renewable**  boolean | Set to `false` to disable the ability of the token to be renewed past its initial TTL.  Setting the value to `true` will allow the token to be renewable up to the system/mount maximum TTL.  Choices:   - `false` - `true` |
| **retries**  any  added in community.hashi_vault 1.3.0 | Allows for retrying on errors, based on the [Retry class in the urllib3 library](https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html#urllib3.util.Retry).  This collection defines recommended defaults for retrying connections to Vault.  This option can be specified as a positive number (integer) or dictionary.  If this option is not specified or the number is `0`, then retries are disabled.  A number sets the total number of retries, and uses collection defaults for the other settings.  A dictionary value is used directly to initialize the `Retry` class, so it can be used to fully customize retries.  For detailed information on retries, see the collection User Guide. |
| **retry_action**  string  added in community.hashi_vault 1.3.0 | Controls whether and how to show messages on *retries*.  This has no effect if a request is not retried.  Choices:   - `"ignore"` - `"warn"` ← (default) |
| **role_id**  string | Vault Role ID or name. Used in `approle`, `aws_iam`, `azure` and `cert` auth methods.  For `cert` auth, if no *role_id* is supplied, the default behavior is to try all certificate roles and return any one that matches.  For `azure` auth, *role_id* is required. |
| **role_name**  string | The name of the token role. If used, the token will be created against the specified role name which may override options set during this call. |
| **secret_id**  string | Secret ID to be used for Vault AppRole authentication. |
| **timeout**  integer  added in community.hashi_vault 1.3.0 | Sets the connection timeout in seconds.  If not set, then the `hvac` library’s default is used. |
| **token**  string | Vault token. Token may be specified explicitly, through the listed [env] vars, and also through the `VAULT_TOKEN` env var.  If no token is supplied, explicitly or through env, then the plugin will check for a token file, as determined by *token_path* and *token_file*.  The order of token loading (first found wins) is `token param -> ansible var -> ANSIBLE_HASHI_VAULT_TOKEN -> VAULT_TOKEN -> token file`. |
| **token_file**  string | If no token is specified, will try to read the token from this file in *token_path*.  Default: `".vault-token"` |
| **token_path**  string | If no token is specified, will try to read the *token_file* from this path. |
| **token_validate**  boolean  added in community.hashi_vault 0.2.0 | For token auth, will perform a `lookup-self` operation to determine the token’s validity before using it.  Disable if your token does not have the `lookup-self` capability.  The default value is `true`.  The default value will change to `false` in version 4.0.0.  Choices:   - `false` - `true` |
| **ttl**  string | The TTL period of the token, provided as `1h` for example, where hour is the largest suffix.  If not provided, the token is valid for the default lease TTL, or indefinitely if the root policy is used. |
| **type**  string | The token type. The default is determined by the role configuration specified by *role_name*.  Choices:   - `"batch"` - `"service"` |
| **url**  string | URL to the Vault service.  If not specified by any other means, the value of the `VAULT_ADDR` environment variable will be used.  If `VAULT_ADDR` is also not defined then an error will be raised. |
| **username**  string | Authentication user name. |
| **validate_certs**  boolean | Controls verification and validation of SSL certificates, mostly you only want to turn off with self signed ones.  Will be populated with the inverse of `VAULT_SKIP_VERIFY` if that is set and *validate_certs* is not explicitly provided.  Will default to `true` if neither *validate_certs* or `VAULT_SKIP_VERIFY` are set.  Choices:   - `false` - `true` |
| **wrap_ttl**  string | Specifies response wrapping token creation with duration. For example `15s`, `20m`, `25h`. |

## [Notes](vault_token_create_module.md#id4)

> **Note:**
>
> - Token creation is a write operation (creating a token persisted to storage), so this module always reports `changed=True`.
> - For the purposes of Ansible playbooks however, it may be more useful to set *changed_when=false* if you are doing idempotency checks against the target system.
> - In check mode, this module will not create a token, and will instead return a basic structure with an empty token. However, this may not be useful if the token is required for follow on tasks. It may be better to use this module with *check_mode=no* in order to have a valid token that can be used.

## [See Also](vault_token_create_module.md#id5)

> **See also:**
>
> [community.hashi_vault.vault_token_create lookup](vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup)
> :   The official documentation for the `community.hashi_vault.vault_token_create` lookup plugin.
>
> [community.hashi_vault.vault_login](vault_login_module.md#ansible-collections-community-hashi-vault-vault-login-module)
> :   Perform a login operation against HashiCorp Vault.
>
> [community.hashi_vault.vault_login lookup](vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup)
> :   The official documentation for the `community.hashi_vault.vault_login` lookup plugin.
>
> community.hashi_vault.vault_login_token filter
> :   The official documentation for the `community.hashi_vault.vault_login_token` filter plugin.

## [Examples](vault_token_create_module.md#id6)

```yaml+jinja
- name: Login via userpass and create a child token
  community.hashi_vault.vault_token_create:
    url: https://vault:8201
    auth_method: userpass
    username: user
    password: '{{ passwd }}'
  register: token_data

- name: Retrieve an approle role ID using the child token (token via filter)
  community.hashi_vault.vault_read:
    url: https://vault:8201
    auth_method: token
    token: '{{ token_data | community.hashi_vault.vault_login_token }}'
    path: auth/approle/role/role-name/role-id
  register: approle_id

- name: Retrieve an approle role ID using the child token (token via direct dict access)
  community.hashi_vault.vault_read:
    url: https://vault:8201
    auth_method: token
    token: '{{ token_data.login.auth.client_token }}'
    path: auth/approle/role/role-name/role-id
  register: approle_id

# implicitly uses token auth with a token from the environment
- name: Create an orphaned token with a short TTL
  community.hashi_vault.vault_token_create:
    url: https://vault:8201
    orphan: true
    ttl: 60s
  register: token_data

- name: Display the full response
  ansible.builtin.debug:
    var: token_data.login
```

## [Return Values](vault_token_create_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **login**  dictionary | The result of the token creation operation.  Returned: success  Sample: `{"auth": {"client_token": "s.rlwajI2bblHAWU7uPqZhLru3"}, "data": null}` |
| **auth**  dictionary | The `auth` member of the token response.  Returned: success |
| **client_token**  string | Contains the newly created token.  Returned: success |
| **data**  dictionary | The `data` member of the token response.  Returned: success, when available |

### Authors

- Brian Scholer (@briantist)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.hashi_vault/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.hashi_vault)
[Discussion, Q&A, troubleshooting](https://github.com/ansible-collections/community.hashi_vault/discussions)
[Communication](index.md#communication-for-community-hashi_vault)
