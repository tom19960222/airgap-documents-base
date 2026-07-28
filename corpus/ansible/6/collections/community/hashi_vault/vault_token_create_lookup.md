---
collection: ansible
version: "6"
title: "community.hashi_vault.vault_token_create lookup – Create a HashiCorp Vault token"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/hashi_vault/vault_token_create_lookup.html
fetched_at: 2026-07-27T17:15:48+00:00
---
# community.hashi_vault.vault_token_create lookup – Create a HashiCorp Vault token

> **Note:**
>
> This lookup plugin is part of the [community.hashi_vault collection](https://galaxy.ansible.com/community/hashi_vault) (version 3.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.hashi_vault`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.hashi_vault.vault_token_create`.

New in community.hashi_vault 2.3.0

- [Synopsis](vault_token_create_lookup.md#synopsis)
- [Requirements](vault_token_create_lookup.md#requirements)
- [Terms](vault_token_create_lookup.md#terms)
- [Keyword parameters](vault_token_create_lookup.md#keyword-parameters)
- [Notes](vault_token_create_lookup.md#notes)
- [See Also](vault_token_create_lookup.md#see-also)
- [Examples](vault_token_create_lookup.md#examples)
- [Return Value](vault_token_create_lookup.md#return-value)

## [Synopsis](vault_token_create_lookup.md#id1)

- Creates a token in HashiCorp Vault, returning the response, including the token.

## [Requirements](vault_token_create_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- `hvac` ([Python library](https://hvac.readthedocs.io/en/stable/overview.html))
- For detailed requirements, see [the collection requirements page](docsite/user_guide.md#ansible-collections-community-hashi-vault-docsite-user-guide-requirements).

## [Terms](vault_token_create_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  string | This is unused and any terms supplied will be ignored. |

## [Keyword parameters](vault_token_create_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.hashi_vault.vault_token_create', key1=value1, key2=value2, ...)` and `query('community.hashi_vault.vault_token_create', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **auth_method**  string | Authentication method to be used.  `none` auth method was added in collection version `1.2.0`.  `cert` auth method was added in collection version `1.4.0`.  `aws_iam_login` was renamed `aws_iam` in collection version `2.1.0` and was removed in `3.0.0`.  `azure` auth method was added in collection version `3.2.0`.  Choices:   - `"token"` ← (default) - `"userpass"` - `"ldap"` - `"approle"` - `"aws_iam"` - `"azure"` - `"jwt"` - `"cert"` - `"none"`   Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   auth_method = token   ```  added in community.hashi_vault 1.4.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_AUTH_METHOD`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_AUTH_METHOD)  added in community.hashi_vault 0.2.0 - Variable: ansible_hashi_vault_auth_method  added in community.hashi_vault 1.2.0 |
| **aws_access_key**  aliases: aws_access_key_id  string | The AWS access key to use.  Configuration:   - Environment variable: [`EC2_ACCESS_KEY`](../../environment_variables.md#envvar-EC2_ACCESS_KEY) - Environment variable: [`AWS_ACCESS_KEY`](../../environment_variables.md#envvar-AWS_ACCESS_KEY) - Environment variable: [`AWS_ACCESS_KEY_ID`](../../environment_variables.md#envvar-AWS_ACCESS_KEY_ID) |
| **aws_iam_server_id**  string  added in community.hashi_vault 0.2.0 | If specified, sets the value to use for the `X-Vault-AWS-IAM-Server-ID` header as part of `GetCallerIdentity` request.  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   aws_iam_server_id = VALUE   ```  added in community.hashi_vault 1.4.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_AWS_IAM_SERVER_ID`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_AWS_IAM_SERVER_ID) |
| **aws_profile**  aliases: boto_profile  string | The AWS profile  Configuration:   - Environment variable: [`AWS_DEFAULT_PROFILE`](../../environment_variables.md#envvar-AWS_DEFAULT_PROFILE) - Environment variable: [`AWS_PROFILE`](../../environment_variables.md#envvar-AWS_PROFILE) |
| **aws_secret_key**  aliases: aws_secret_access_key  string | The AWS secret key that corresponds to the access key.  Configuration:   - Environment variable: [`EC2_SECRET_KEY`](../../environment_variables.md#envvar-EC2_SECRET_KEY) - Environment variable: [`AWS_SECRET_KEY`](../../environment_variables.md#envvar-AWS_SECRET_KEY) - Environment variable: [`AWS_SECRET_ACCESS_KEY`](../../environment_variables.md#envvar-AWS_SECRET_ACCESS_KEY) |
| **aws_security_token**  string | The AWS security token if using temporary access and secret keys.  Configuration:   - Environment variable: [`EC2_SECURITY_TOKEN`](../../environment_variables.md#envvar-EC2_SECURITY_TOKEN) - Environment variable: [`AWS_SESSION_TOKEN`](../../environment_variables.md#envvar-AWS_SESSION_TOKEN) - Environment variable: [`AWS_SECURITY_TOKEN`](../../environment_variables.md#envvar-AWS_SECURITY_TOKEN) |
| **azure_client_id**  string  added in community.hashi_vault 3.2.0 | The client ID (also known as application ID) of the Azure AD service principal or managed identity. Should be a UUID.  If not specified, will use the system assigned managed identity.  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   azure_client_id = VALUE   ``` - Environment variable: [`ANSIBLE_HASHI_VAULT_AZURE_CLIENT_ID`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_AZURE_CLIENT_ID) - Variable: ansible_hashi_vault_azure_client_id |
| **azure_client_secret**  string  added in community.hashi_vault 3.2.0 | The client secret of the Azure AD service principal.  Configuration:   - Environment variable: [`ANSIBLE_HASHI_VAULT_AZURE_CLIENT_SECRET`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_AZURE_CLIENT_SECRET) - Variable: ansible_hashi_vault_azure_client_secret |
| **azure_resource**  string  added in community.hashi_vault 3.2.0 | The resource URL for the application registered in Azure Active Directory. Usually should not be changed from the default.  Default: `"https://management.azure.com/"`  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   azure_resource = https://management.azure.com/   ``` - Environment variable: [`ANSIBLE_HASHI_VAULT_AZURE_RESOURCE`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_AZURE_RESOURCE) - Variable: ansible_hashi_vault_azure_resource |
| **azure_tenant_id**  string  added in community.hashi_vault 3.2.0 | The Azure Active Directory Tenant ID (also known as the Directory ID) of the service principal. Should be a UUID.  Required when using a service principal to authenticate to Vault, e.g. required when both *azure_client_id* and *azure_client_secret* are specified.  Optional when using managed identity to authenticate to Vault.  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   azure_tenant_id = VALUE   ``` - Environment variable: [`ANSIBLE_HASHI_VAULT_AZURE_TENANT_ID`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_AZURE_TENANT_ID) - Variable: ansible_hashi_vault_azure_tenant_id |
| **ca_cert**  aliases: cacert  string | Path to certificate to use for authentication.  If not specified by any other means, the `VAULT_CACERT` environment variable will be used.  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   ca_cert = VALUE   ```  added in community.hashi_vault 1.4.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_CA_CERT`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_CA_CERT)  added in community.hashi_vault 1.2.0 - Variable: ansible_hashi_vault_ca_cert  added in community.hashi_vault 1.2.0 |
| **cert_auth_private_key**  path  added in community.hashi_vault 1.4.0 | For `cert` auth, path to the private key file to authenticate with, in PEM format.  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   cert_auth_private_key = VALUE   ``` - Environment variable: [`ANSIBLE_HASHI_VAULT_CERT_AUTH_PRIVATE_KEY`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_CERT_AUTH_PRIVATE_KEY) |
| **cert_auth_public_key**  path  added in community.hashi_vault 1.4.0 | For `cert` auth, path to the certificate file to authenticate with, in PEM format.  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   cert_auth_public_key = VALUE   ``` - Environment variable: [`ANSIBLE_HASHI_VAULT_CERT_AUTH_PUBLIC_KEY`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_CERT_AUTH_PUBLIC_KEY) |
| **display_name**  string | The display name of the token. |
| **entity_alias**  string | Name of the entity alias to associate with during token creation.  Only works in combination with *role_name* option and used entity alias must be listed in `allowed_entity_aliases`.  If this has been specified, the entity will not be inherited from the parent. |
| **explicit_max_ttl**  string | If set, the token will have an explicit max TTL set upon it.  This maximum token TTL cannot be changed later, and unlike with normal tokens, updates to the system/mount max TTL value will have no effect at renewal time.  The token will never be able to be renewed or used past the value set at issue time. |
| **id**  string | The ID of the client token. Can only be specified by a root token.  The ID provided may not contain a `.` character.  Otherwise, the token ID is a randomly generated value. |
| **jwt**  string | The JSON Web Token (JWT) to use for JWT authentication to Vault.  Configuration:   - Environment variable: [`ANSIBLE_HASHI_VAULT_JWT`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_JWT) |
| **meta**  dictionary | A dict of string to string valued metadata. This is passed through to the audit devices. |
| **mount_point**  string | Vault mount point.  If not specified, the default mount point for a given auth method is used.  Does not apply to token authentication.  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   mount_point = VALUE   ```  added in community.hashi_vault 1.5.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_MOUNT_POINT`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_MOUNT_POINT)  added in community.hashi_vault 1.5.0 - Variable: ansible_hashi_vault_mount_point  added in community.hashi_vault 1.5.0 |
| **namespace**  string | Vault namespace where secrets reside. This option requires HVAC 0.7.0+ and Vault 0.11+.  Optionally, this may be achieved by prefixing the authentication mount point and/or secret path with the namespace (e.g `mynamespace/secret/mysecret`).  If environment variable `VAULT_NAMESPACE` is set, its value will be used last among all ways to specify *namespace*.  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   namespace = VALUE   ```  added in community.hashi_vault 1.4.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_NAMESPACE`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_NAMESPACE)  added in community.hashi_vault 0.2.0 - Variable: ansible_hashi_vault_namespace  added in community.hashi_vault 1.2.0 |
| **no_default_policy**  boolean | If `true` the default policy will not be contained in this token’s policy set.  If the token will be used with this collection, set *token_validate=false*.  Choices:   - `false` - `true` |
| **no_parent**  boolean | This option only has effect if used by a `root` or `sudo` caller and only when *orphan=false*.  When `true`, the token created will not have a parent.  Choices:   - `false` - `true` |
| **num_uses**  integer | The maximum uses for the given token. This can be used to create a one-time-token or limited use token.  The value of `0` has no limit to the number of uses. |
| **orphan**  boolean | When `true`, uses the `/create-orphan` API endpoint, which requires `sudo` (but not `root`) to create an orphan.  With `hvac>=1.0.0`, requires collection version `>=3.3.0`.  Choices:   - `false` ← (default) - `true` |
| **password**  string | Authentication password.  Configuration:   - Environment variable: [`ANSIBLE_HASHI_VAULT_PASSWORD`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_PASSWORD)  added in community.hashi_vault 1.2.0 - Variable: ansible_hashi_vault_password  added in community.hashi_vault 1.2.0 |
| **period**  string | If specified, the token will be periodic.  It will have no maximum TTL (unless an *explicit_max_ttl* is also set) but every renewal will use the given period.  Requires a root token or one with the `sudo` capability. |
| **policies**  list / elements=string | A list of policies for the token. This must be a subset of the policies belonging to the token making the request, unless root.  If not specified, defaults to all the policies of the calling token. |
| **proxies**  any  added in community.hashi_vault 1.1.0 | URL(s) to the proxies used to access the Vault service.  It can be a string or a dict.  If it’s a dict, provide the scheme (eg. `http` or `https`) as the key, and the URL as the value.  If it’s a string, provide a single URL that will be used as the proxy for both `http` and `https` schemes.  A string that can be interpreted as a dictionary will be converted to one (see examples).  You can specify a different proxy for HTTP and HTTPS resources.  If not specified, [environment variables from the Requests library](https://requests.readthedocs.io/en/master/user/advanced/#proxies) are used.  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   proxies = VALUE   ```  added in community.hashi_vault 1.4.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_PROXIES`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_PROXIES) - Variable: ansible_hashi_vault_proxies  added in community.hashi_vault 1.2.0 |
| **region**  string | The AWS region for which to create the connection.  Configuration:   - Environment variable: [`EC2_REGION`](../../environment_variables.md#envvar-EC2_REGION) - Environment variable: [`AWS_REGION`](../../environment_variables.md#envvar-AWS_REGION) |
| **renewable**  boolean | Set to `false` to disable the ability of the token to be renewed past its initial TTL.  Setting the value to `true` will allow the token to be renewable up to the system/mount maximum TTL.  Choices:   - `false` - `true` |
| **retries**  any  added in community.hashi_vault 1.3.0 | Allows for retrying on errors, based on the [Retry class in the urllib3 library](https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html#urllib3.util.Retry).  This collection defines recommended defaults for retrying connections to Vault.  This option can be specified as a positive number (integer) or dictionary.  If this option is not specified or the number is `0`, then retries are disabled.  A number sets the total number of retries, and uses collection defaults for the other settings.  A dictionary value is used directly to initialize the `Retry` class, so it can be used to fully customize retries.  For detailed information on retries, see the collection User Guide.  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   retries = VALUE   ```  added in community.hashi_vault 1.4.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_RETRIES`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_RETRIES) - Variable: ansible_hashi_vault_retries |
| **retry_action**  string  added in community.hashi_vault 1.3.0 | Controls whether and how to show messages on *retries*.  This has no effect if a request is not retried.  Choices:   - `"ignore"` - `"warn"` ← (default)   Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   retry_action = warn   ```  added in community.hashi_vault 1.4.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_RETRY_ACTION`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_RETRY_ACTION) - Variable: ansible_hashi_vault_retry_action |
| **role_id**  string | Vault Role ID or name. Used in `approle`, `aws_iam`, `azure` and `cert` auth methods.  For `cert` auth, if no *role_id* is supplied, the default behavior is to try all certificate roles and return any one that matches.  For `azure` auth, *role_id* is required.  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   role_id = VALUE   ```  added in community.hashi_vault 1.4.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_ROLE_ID`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_ROLE_ID)  added in community.hashi_vault 0.2.0 - Variable: ansible_hashi_vault_role_id  added in community.hashi_vault 1.2.0 |
| **role_name**  string | The name of the token role. If used, the token will be created against the specified role name which may override options set during this call. |
| **secret_id**  string | Secret ID to be used for Vault AppRole authentication.  Configuration:   - Environment variable: [`ANSIBLE_HASHI_VAULT_SECRET_ID`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_SECRET_ID)  added in community.hashi_vault 0.2.0 - Variable: ansible_hashi_vault_secret_id  added in community.hashi_vault 1.2.0 |
| **timeout**  integer  added in community.hashi_vault 1.3.0 | Sets the connection timeout in seconds.  If not set, then the `hvac` library’s default is used.  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   timeout = VALUE   ```  added in community.hashi_vault 1.4.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_TIMEOUT`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_TIMEOUT) - Variable: ansible_hashi_vault_timeout |
| **token**  string | Vault token. Token may be specified explicitly, through the listed [env] vars, and also through the `VAULT_TOKEN` env var.  If no token is supplied, explicitly or through env, then the plugin will check for a token file, as determined by *token_path* and *token_file*.  The order of token loading (first found wins) is `token param -> ansible var -> ANSIBLE_HASHI_VAULT_TOKEN -> VAULT_TOKEN -> token file`.  Configuration:   - Environment variable: [`ANSIBLE_HASHI_VAULT_TOKEN`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_TOKEN)  added in community.hashi_vault 0.2.0 - Variable: ansible_hashi_vault_token  added in community.hashi_vault 1.2.0 |
| **token_file**  string | If no token is specified, will try to read the token from this file in *token_path*.  Default: `".vault-token"`  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   token_file = .vault-token   ```  added in community.hashi_vault 1.4.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_TOKEN_FILE`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_TOKEN_FILE)  added in community.hashi_vault 0.2.0 - Variable: ansible_hashi_vault_token_file  added in community.hashi_vault 1.2.0 |
| **token_path**  string | If no token is specified, will try to read the *token_file* from this path.  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   token_path = VALUE   ```  added in community.hashi_vault 1.4.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_TOKEN_PATH`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_TOKEN_PATH)  added in community.hashi_vault 0.2.0 - Variable: ansible_hashi_vault_token_path  added in community.hashi_vault 1.2.0 |
| **token_validate**  boolean  added in community.hashi_vault 0.2.0 | For token auth, will perform a `lookup-self` operation to determine the token’s validity before using it.  Disable if your token does not have the `lookup-self` capability.  The default value is `true`.  The default value will change to `false` in version 4.0.0.  Choices:   - `false` - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   token_validate = VALUE   ```  added in community.hashi_vault 1.4.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_TOKEN_VALIDATE`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_TOKEN_VALIDATE) - Variable: ansible_hashi_vault_token_validate  added in community.hashi_vault 1.2.0 |
| **ttl**  string | The TTL period of the token, provided as `1h` for example, where hour is the largest suffix.  If not provided, the token is valid for the default lease TTL, or indefinitely if the root policy is used. |
| **type**  string | The token type. The default is determined by the role configuration specified by *role_name*.  Choices:   - `"batch"` - `"service"` |
| **url**  string | URL to the Vault service.  If not specified by any other means, the value of the `VAULT_ADDR` environment variable will be used.  If `VAULT_ADDR` is also not defined then an error will be raised.  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   url = VALUE   ```  added in community.hashi_vault 1.4.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_ADDR`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_ADDR)  added in community.hashi_vault 0.2.0 - Variable: ansible_hashi_vault_url  added in community.hashi_vault 1.2.0 - Variable: ansible_hashi_vault_addr  added in community.hashi_vault 1.2.0 |
| **username**  string | Authentication user name.  Configuration:   - Environment variable: [`ANSIBLE_HASHI_VAULT_USERNAME`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_USERNAME)  added in community.hashi_vault 1.2.0 - Variable: ansible_hashi_vault_username  added in community.hashi_vault 1.2.0 |
| **validate_certs**  boolean | Controls verification and validation of SSL certificates, mostly you only want to turn off with self signed ones.  Will be populated with the inverse of `VAULT_SKIP_VERIFY` if that is set and *validate_certs* is not explicitly provided.  Will default to `true` if neither *validate_certs* or `VAULT_SKIP_VERIFY` are set.  Choices:   - `false` - `true`   Configuration:   - Variable: ansible_hashi_vault_validate_certs  added in community.hashi_vault 1.2.0 |
| **wrap_ttl**  string | Specifies response wrapping token creation with duration. For example `15s`, `20m`, `25h`.  Configuration:   - Variable: ansible_hashi_vault_wrap_ttl |

## [Notes](vault_token_create_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.hashi_vault.vault_token_create', term1, term2, key1=value1, key2=value2)` and `query('community.hashi_vault.vault_token_create', term1, term2, key1=value1, key2=value2)`
> - Token creation is a write operation (creating a token persisted to storage), so this module always reports `changed=True`.
> - For the purposes of Ansible playbooks however, it may be more useful to set *changed_when=false* if you are doing idempotency checks against the target system.
> - In check mode, this module will not create a token, and will instead return a basic structure with an empty token. However, this may not be useful if the token is required for follow on tasks. It may be better to use this module with *check_mode=no* in order to have a valid token that can be used.

## [See Also](vault_token_create_lookup.md#id6)

> **See also:**
>
> [community.hashi_vault.vault_token_create](vault_token_create_module.md#ansible-collections-community-hashi-vault-vault-token-create-module)
> :   Create a HashiCorp Vault token.
>
> [community.hashi_vault.vault_login lookup](vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup)
> :   The official documentation for the `community.hashi_vault.vault_login` lookup plugin.
>
> [community.hashi_vault.vault_login](vault_login_module.md#ansible-collections-community-hashi-vault-vault-login-module)
> :   Perform a login operation against HashiCorp Vault.
>
> community.hashi_vault.vault_login_token filter
> :   The official documentation for the `community.hashi_vault.vault_login_token` filter plugin.

## [Examples](vault_token_create_lookup.md#id7)

```yaml+jinja
- name: Login via userpass and create a child token
  ansible.builtin.set_fact:
    token_data: "{{ lookup('community.hashi_vault.vault_token_create', url='https://vault', auth_method='userpass', username=user, password=passwd) }}"

- name: Retrieve an approle role ID using the child token (token via filter)
  community.hashi_vault.vault_read:
    url: https://vault:8201
    auth_method: token
    token: '{{ token_data | community.hashi_vault.vault_login_token }}'
    path: auth/approle/role/role-name/role-id
  register: approle_id

- name: Retrieve an approle role ID (token via direct dict access)
  community.hashi_vault.vault_read:
    url: https://vault:8201
    auth_method: token
    token: '{{ token_data.auth.client_token }}'
    path: auth/approle/role/role-name/role-id
  register: approle_id

# implicitly uses url & token auth with a token from the environment
- name: Create an orphaned token with a short TTL and display the full response
  ansible.builtin.debug:
    var: lookup('community.hashi_vault.vault_token_create', orphan=True, ttl='60s')
```

## [Return Value](vault_token_create_lookup.md#id8)

| Key | Description |
| --- | --- |
| **Return value**  dictionary | The result of the token creation operation.  Returned: success  Sample: `{"auth": {"client_token": "s.rlwajI2bblHAWU7uPqZhLru3"}, "data": null}` |
| **auth**  dictionary | The `auth` member of the token response.  Returned: success |
| **client_token**  string | Contains the newly created token.  Returned: success |
| **data**  dictionary | The `data` member of the token response.  Returned: success, when available |

### Authors

- Brian Scholer (@briantist)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.hashi_vault/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.hashi_vault)
[Discussion, Q&A, troubleshooting](https://github.com/ansible-collections/community.hashi_vault/discussions)
[Communication](index.md#communication-for-community-hashi_vault)
