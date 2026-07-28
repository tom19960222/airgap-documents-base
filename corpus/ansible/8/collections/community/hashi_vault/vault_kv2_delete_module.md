---
collection: ansible
version: "8"
title: "community.hashi_vault.vault_kv2_delete module – Delete one or more versions of a secret from HashiCorp Vault’s KV version 2 secret store"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/hashi_vault/vault_kv2_delete_module.html
fetched_at: 2026-07-28T01:53:27+00:00
---
# community.hashi_vault.vault_kv2_delete module – Delete one or more versions of a secret from HashiCorp Vault’s KV version 2 secret store

> **Note:**
>
> This module is part of the [community.hashi_vault collection](https://galaxy.ansible.com/ui/repo/published/community/hashi_vault/) (version 5.0.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.hashi_vault`.
> You need further requirements to be able to use this module,
> see [Requirements](vault_kv2_delete_module.md#ansible-collections-community-hashi-vault-vault-kv2-delete-module-requirements) for details.
>
> To use it in a playbook, specify: `community.hashi_vault.vault_kv2_delete`.

New in community.hashi_vault 3.4.0

- [Synopsis](vault_kv2_delete_module.md#synopsis)
- [Requirements](vault_kv2_delete_module.md#requirements)
- [Parameters](vault_kv2_delete_module.md#parameters)
- [Attributes](vault_kv2_delete_module.md#attributes)
- [Notes](vault_kv2_delete_module.md#notes)
- [See Also](vault_kv2_delete_module.md#see-also)
- [Examples](vault_kv2_delete_module.md#examples)
- [Return Values](vault_kv2_delete_module.md#return-values)

## [Synopsis](vault_kv2_delete_module.md#id1)

- Delete one or more versions of a secret from HashiCorp Vault’s KV version 2 secret store.

## [Requirements](vault_kv2_delete_module.md#id2)

The below requirements are needed on the host that executes this module.

- `hvac` ([Python library](https://hvac.readthedocs.io/en/stable/overview.html))
- For detailed requirements, see [the collection requirements page](docsite/user_guide.md#ansible-collections-community-hashi-vault-docsite-user-guide-requirements).

## [Parameters](vault_kv2_delete_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_method**  string | Authentication method to be used.  `none` auth method was added in collection version `1.2.0`.  `cert` auth method was added in collection version `1.4.0`.  `aws_iam_login` was renamed `aws_iam` in collection version `2.1.0` and was removed in `3.0.0`.  `azure` auth method was added in collection version `3.2.0`.  **Choices:**   - `"token"` ← (default) - `"userpass"` - `"ldap"` - `"approle"` - `"aws_iam"` - `"azure"` - `"jwt"` - `"cert"` - `"none"` |
| **aws_access_key**  aliases: aws_access_key_id  string | The AWS access key to use. |
| **aws_iam_server_id**  string  *added in community.hashi_vault 0.2.0* | If specified, sets the value to use for the `X-Vault-AWS-IAM-Server-ID` header as part of `GetCallerIdentity` request. |
| **aws_profile**  aliases: boto_profile  string | The AWS profile |
| **aws_secret_key**  aliases: aws_secret_access_key  string | The AWS secret key that corresponds to the access key. |
| **aws_security_token**  string | The AWS security token if using temporary access and secret keys. |
| **azure_client_id**  string  *added in community.hashi_vault 3.2.0* | The client ID (also known as application ID) of the Azure AD service principal or managed identity. Should be a UUID.  If not specified, will use the system assigned managed identity. |
| **azure_client_secret**  string  *added in community.hashi_vault 3.2.0* | The client secret of the Azure AD service principal. |
| **azure_resource**  string  *added in community.hashi_vault 3.2.0* | The resource URL for the application registered in Azure Active Directory. Usually should not be changed from the default.  **Default:** `"https://management.azure.com/"` |
| **azure_tenant_id**  string  *added in community.hashi_vault 3.2.0* | The Azure Active Directory Tenant ID (also known as the Directory ID) of the service principal. Should be a UUID.  Required when using a service principal to authenticate to Vault, e.g. required when both *azure_client_id* and *azure_client_secret* are specified.  Optional when using managed identity to authenticate to Vault. |
| **ca_cert**  aliases: cacert  string | Path to certificate to use for authentication.  If not specified by any other means, the `VAULT_CACERT` environment variable will be used. |
| **cert_auth_private_key**  path  *added in community.hashi_vault 1.4.0* | For `cert` auth, path to the private key file to authenticate with, in PEM format. |
| **cert_auth_public_key**  path  *added in community.hashi_vault 1.4.0* | For `cert` auth, path to the certificate file to authenticate with, in PEM format. |
| **engine_mount_point**  string | The path where the secret backend is mounted.  **Default:** `"secret"` |
| **jwt**  string | The JSON Web Token (JWT) to use for JWT authentication to Vault. |
| **mount_point**  string | Vault mount point.  If not specified, the default mount point for a given auth method is used.  Does not apply to token authentication. |
| **namespace**  string | Vault namespace where secrets reside. This option requires HVAC 0.7.0+ and Vault 0.11+.  Optionally, this may be achieved by prefixing the authentication mount point and/or secret path with the namespace (e.g `mynamespace/secret/mysecret`).  If environment variable `VAULT_NAMESPACE` is set, its value will be used last among all ways to specify *namespace*. |
| **password**  string | Authentication password. |
| **path**  string / required | Vault KV path to be deleted.  This is relative to the *engine_mount_point*, so the mount path should not be included.  For kv2, do not include `/data/` or `/metadata/`. |
| **proxies**  any  *added in community.hashi_vault 1.1.0* | URL(s) to the proxies used to access the Vault service.  It can be a string or a dict.  If it’s a dict, provide the scheme (eg. `http` or `https`) as the key, and the URL as the value.  If it’s a string, provide a single URL that will be used as the proxy for both `http` and `https` schemes.  A string that can be interpreted as a dictionary will be converted to one (see examples).  You can specify a different proxy for HTTP and HTTPS resources.  If not specified, [environment variables from the Requests library](https://requests.readthedocs.io/en/master/user/advanced/#proxies) are used. |
| **region**  string | The AWS region for which to create the connection. |
| **retries**  any  *added in community.hashi_vault 1.3.0* | Allows for retrying on errors, based on the [Retry class in the urllib3 library](https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html#urllib3.util.Retry).  This collection defines recommended defaults for retrying connections to Vault.  This option can be specified as a positive number (integer) or dictionary.  If this option is not specified or the number is `0`, then retries are disabled.  A number sets the total number of retries, and uses collection defaults for the other settings.  A dictionary value is used directly to initialize the `Retry` class, so it can be used to fully customize retries.  For detailed information on retries, see the collection User Guide. |
| **retry_action**  string  *added in community.hashi_vault 1.3.0* | Controls whether and how to show messages on *retries*.  This has no effect if a request is not retried.  **Choices:**   - `"ignore"` - `"warn"` ← (default) |
| **role_id**  string | Vault Role ID or name. Used in `approle`, `aws_iam`, `azure` and `cert` auth methods.  For `cert` auth, if no *role_id* is supplied, the default behavior is to try all certificate roles and return any one that matches.  For `azure` auth, *role_id* is required. |
| **secret_id**  string | Secret ID to be used for Vault AppRole authentication. |
| **timeout**  integer  *added in community.hashi_vault 1.3.0* | Sets the connection timeout in seconds.  If not set, then the `hvac` library’s default is used. |
| **token**  string | Vault token. Token may be specified explicitly, through the listed [env] vars, and also through the `VAULT_TOKEN` env var.  If no token is supplied, explicitly or through env, then the plugin will check for a token file, as determined by *token_path* and *token_file*.  The order of token loading (first found wins) is `token param -> ansible var -> ANSIBLE_HASHI_VAULT_TOKEN -> VAULT_TOKEN -> token file`. |
| **token_file**  string | If no token is specified, will try to read the token from this file in *token_path*.  **Default:** `".vault-token"` |
| **token_path**  string | If no token is specified, will try to read the *token_file* from this path. |
| **token_validate**  boolean  *added in community.hashi_vault 0.2.0* | For token auth, will perform a `lookup-self` operation to determine the token’s validity before using it.  Disable if your token does not have the `lookup-self` capability.  **Choices:**   - `false` ← (default) - `true` |
| **url**  string | URL to the Vault service.  If not specified by any other means, the value of the `VAULT_ADDR` environment variable will be used.  If `VAULT_ADDR` is also not defined then an error will be raised. |
| **username**  string | Authentication user name. |
| **validate_certs**  boolean | Controls verification and validation of SSL certificates, mostly you only want to turn off with self signed ones.  Will be populated with the inverse of `VAULT_SKIP_VERIFY` if that is set and *validate_certs* is not explicitly provided.  Will default to `true` if neither *validate_certs* or `VAULT_SKIP_VERIFY` are set.  **Choices:**   - `false` - `true` |
| **versions**  list / elements=integer | One or more versions of the secret to delete.  When omitted, the latest version of the secret is deleted. |

## [Attributes](vault_kv2_delete_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | **Action group:** **community.hashi_vault.vault** | Use `group/community.hashi_vault.vault` in `module_defaults` to set defaults for this module. |
| **check_mode** | **Support:** **partial**  In check mode, the module returns `changed` status without contacting Vault.  Consider using [community.hashi_vault.vault_kv2_get](vault_kv2_get_module.md#ansible-collections-community-hashi-vault-vault-kv2-get-module) to verify the existence of the secret first. | Can run in `check_mode` and return changed status prediction without modifying target. |

## [Notes](vault_kv2_delete_module.md#id5)

> **Note:**
>
> - This module always reports `changed` status because it cannot guarantee idempotence.
> - Use `changed_when` to control that in cases where the operation is known to not change state.

## [See Also](vault_kv2_delete_module.md#id6)

> **See also:**
>
> [community.hashi_vault.vault_kv2_get](vault_kv2_get_module.md#ansible-collections-community-hashi-vault-vault-kv2-get-module)
> :   Get a secret from HashiCorp Vault’s KV version 2 secret store.
>
> [community.hashi_vault.vault_kv2_write](vault_kv2_write_module.md#ansible-collections-community-hashi-vault-vault-kv2-write-module)
> :   Perform a write operation against a KVv2 secret in HashiCorp Vault.
>
> [KV2 Secrets Engine](https://www.vaultproject.io/docs/secrets/kv/kv-v2)
> :   Documentation for the Vault KV secrets engine, version 2.

## [Examples](vault_kv2_delete_module.md#id7)

```yaml+jinja
- name: Delete the latest version of the secret/mysecret secret.
  community.hashi_vault.vault_kv2_delete:
    url: https://vault:8201
    path: secret/mysecret
    auth_method: userpass
    username: user
    password: '{{ passwd }}'
  register: result

- name: Delete versions 1 and 3 of the secret/mysecret secret.
  community.hashi_vault.vault_kv2_delete:
    url: https://vault:8201
    path: secret/mysecret
    versions: [1, 3]
    auth_method: userpass
    username: user
    password: '{{ passwd }}'
```

## [Return Values](vault_kv2_delete_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | The raw result of the delete against the given path.  This is usually empty, but may contain warnings or other information.  **Returned:** success |

### Authors

- Isaac Wagner (@idwagner)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.hashi_vault/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.hashi_vault)
- [Discussion, Q&A, troubleshooting](https://github.com/ansible-collections/community.hashi_vault/discussions)
- [Communication](index.md#communication-for-community-hashi-vault)
