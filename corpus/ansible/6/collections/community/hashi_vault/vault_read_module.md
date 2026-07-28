---
collection: ansible
version: "6"
title: "community.hashi_vault.vault_read module – Perform a read operation against HashiCorp Vault"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/hashi_vault/vault_read_module.html
fetched_at: 2026-07-27T17:15:42+00:00
---
# community.hashi_vault.vault_read module – Perform a read operation against HashiCorp Vault

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
> see [Requirements](vault_read_module.md#ansible-collections-community-hashi-vault-vault-read-module-requirements) for details.
>
> To use it in a playbook, specify: `community.hashi_vault.vault_read`.

New in community.hashi_vault 1.4.0

- [Synopsis](vault_read_module.md#synopsis)
- [Requirements](vault_read_module.md#requirements)
- [Parameters](vault_read_module.md#parameters)
- [See Also](vault_read_module.md#see-also)
- [Examples](vault_read_module.md#examples)
- [Return Values](vault_read_module.md#return-values)

## [Synopsis](vault_read_module.md#id1)

- Performs a generic read operation against a given path in HashiCorp Vault.

## [Requirements](vault_read_module.md#id2)

The below requirements are needed on the host that executes this module.

- `hvac` ([Python library](https://hvac.readthedocs.io/en/stable/overview.html))
- For detailed requirements, see [the collection requirements page](docsite/user_guide.md#ansible-collections-community-hashi-vault-docsite-user-guide-requirements).

## [Parameters](vault_read_module.md#id3)

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
| **jwt**  string | The JSON Web Token (JWT) to use for JWT authentication to Vault. |
| **mount_point**  string | Vault mount point.  If not specified, the default mount point for a given auth method is used.  Does not apply to token authentication. |
| **namespace**  string | Vault namespace where secrets reside. This option requires HVAC 0.7.0+ and Vault 0.11+.  Optionally, this may be achieved by prefixing the authentication mount point and/or secret path with the namespace (e.g `mynamespace/secret/mysecret`).  If environment variable `VAULT_NAMESPACE` is set, its value will be used last among all ways to specify *namespace*. |
| **password**  string | Authentication password. |
| **path**  string / required | Vault path to be read. |
| **proxies**  any  added in community.hashi_vault 1.1.0 | URL(s) to the proxies used to access the Vault service.  It can be a string or a dict.  If it’s a dict, provide the scheme (eg. `http` or `https`) as the key, and the URL as the value.  If it’s a string, provide a single URL that will be used as the proxy for both `http` and `https` schemes.  A string that can be interpreted as a dictionary will be converted to one (see examples).  You can specify a different proxy for HTTP and HTTPS resources.  If not specified, [environment variables from the Requests library](https://requests.readthedocs.io/en/master/user/advanced/#proxies) are used. |
| **region**  string | The AWS region for which to create the connection. |
| **retries**  any  added in community.hashi_vault 1.3.0 | Allows for retrying on errors, based on the [Retry class in the urllib3 library](https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html#urllib3.util.Retry).  This collection defines recommended defaults for retrying connections to Vault.  This option can be specified as a positive number (integer) or dictionary.  If this option is not specified or the number is `0`, then retries are disabled.  A number sets the total number of retries, and uses collection defaults for the other settings.  A dictionary value is used directly to initialize the `Retry` class, so it can be used to fully customize retries.  For detailed information on retries, see the collection User Guide. |
| **retry_action**  string  added in community.hashi_vault 1.3.0 | Controls whether and how to show messages on *retries*.  This has no effect if a request is not retried.  Choices:   - `"ignore"` - `"warn"` ← (default) |
| **role_id**  string | Vault Role ID or name. Used in `approle`, `aws_iam`, `azure` and `cert` auth methods.  For `cert` auth, if no *role_id* is supplied, the default behavior is to try all certificate roles and return any one that matches.  For `azure` auth, *role_id* is required. |
| **secret_id**  string | Secret ID to be used for Vault AppRole authentication. |
| **timeout**  integer  added in community.hashi_vault 1.3.0 | Sets the connection timeout in seconds.  If not set, then the `hvac` library’s default is used. |
| **token**  string | Vault token. Token may be specified explicitly, through the listed [env] vars, and also through the `VAULT_TOKEN` env var.  If no token is supplied, explicitly or through env, then the plugin will check for a token file, as determined by *token_path* and *token_file*.  The order of token loading (first found wins) is `token param -> ansible var -> ANSIBLE_HASHI_VAULT_TOKEN -> VAULT_TOKEN -> token file`. |
| **token_file**  string | If no token is specified, will try to read the token from this file in *token_path*.  Default: `".vault-token"` |
| **token_path**  string | If no token is specified, will try to read the *token_file* from this path. |
| **token_validate**  boolean  added in community.hashi_vault 0.2.0 | For token auth, will perform a `lookup-self` operation to determine the token’s validity before using it.  Disable if your token does not have the `lookup-self` capability.  The default value is `true`.  The default value will change to `false` in version 4.0.0.  Choices:   - `false` - `true` |
| **url**  string | URL to the Vault service.  If not specified by any other means, the value of the `VAULT_ADDR` environment variable will be used.  If `VAULT_ADDR` is also not defined then an error will be raised. |
| **username**  string | Authentication user name. |
| **validate_certs**  boolean | Controls verification and validation of SSL certificates, mostly you only want to turn off with self signed ones.  Will be populated with the inverse of `VAULT_SKIP_VERIFY` if that is set and *validate_certs* is not explicitly provided.  Will default to `true` if neither *validate_certs* or `VAULT_SKIP_VERIFY` are set.  Choices:   - `false` - `true` |

## [See Also](vault_read_module.md#id4)

> **See also:**
>
> [community.hashi_vault.vault_read lookup](vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup)
> :   The official documentation for the `community.hashi_vault.vault_read` lookup plugin.
>
> [community.hashi_vault.hashi_vault lookup](hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup)
> :   The official documentation for the `community.hashi_vault.hashi_vault` lookup plugin.

## [Examples](vault_read_module.md#id5)

```yaml+jinja
- name: Read a kv2 secret from Vault via the remote host with userpass auth
  community.hashi_vault.vault_read:
    url: https://vault:8201
    path: secret/data/hello
    auth_method: userpass
    username: user
    password: '{{ passwd }}'
  register: secret

- name: Display the secret data
  ansible.builtin.debug:
    msg: "{{ secret.data.data.data }}"

- name: Retrieve an approle role ID from Vault via the remote host
  community.hashi_vault.vault_read:
    url: https://vault:8201
    path: auth/approle/role/role-name/role-id
  register: approle_id

- name: Display the role ID
  ansible.builtin.debug:
    msg: "{{ approle_id.data.data.role_id }}"
```

## [Return Values](vault_read_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | The raw result of the read against the given path.  Returned: success |

### Authors

- Brian Scholer (@briantist)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.hashi_vault/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.hashi_vault)
[Discussion, Q&A, troubleshooting](https://github.com/ansible-collections/community.hashi_vault/discussions)
[Communication](index.md#communication-for-community-hashi_vault)
