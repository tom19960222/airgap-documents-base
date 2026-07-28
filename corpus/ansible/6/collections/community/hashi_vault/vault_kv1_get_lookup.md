---
collection: ansible
version: "6"
title: "community.hashi_vault.vault_kv1_get lookup – Get a secret from HashiCorp Vault’s KV version 1 secret store"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/hashi_vault/vault_kv1_get_lookup.html
fetched_at: 2026-07-27T17:15:45+00:00
---
# community.hashi_vault.vault_kv1_get lookup – Get a secret from HashiCorp Vault’s KV version 1 secret store

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
> see [Requirements](vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.hashi_vault.vault_kv1_get`.

New in community.hashi_vault 2.5.0

- [Synopsis](vault_kv1_get_lookup.md#synopsis)
- [Requirements](vault_kv1_get_lookup.md#requirements)
- [Terms](vault_kv1_get_lookup.md#terms)
- [Keyword parameters](vault_kv1_get_lookup.md#keyword-parameters)
- [Notes](vault_kv1_get_lookup.md#notes)
- [See Also](vault_kv1_get_lookup.md#see-also)
- [Examples](vault_kv1_get_lookup.md#examples)
- [Return Value](vault_kv1_get_lookup.md#return-value)

## [Synopsis](vault_kv1_get_lookup.md#id1)

- Gets a secret from HashiCorp Vault’s KV version 1 secret store.

## [Requirements](vault_kv1_get_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- `hvac` ([Python library](https://hvac.readthedocs.io/en/stable/overview.html))
- For detailed requirements, see [the collection requirements page](docsite/user_guide.md#ansible-collections-community-hashi-vault-docsite-user-guide-requirements).

## [Terms](vault_kv1_get_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | Vault KV path(s) to be read.  These are relative to the *engine_mount_point*, so the mount path should not be included. |

## [Keyword parameters](vault_kv1_get_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.hashi_vault.vault_kv1_get', key1=value1, key2=value2, ...)` and `query('community.hashi_vault.vault_kv1_get', key1=value1, key2=value2, ...)`

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
| **engine_mount_point**  string | The path where the secret backend is mounted.  Default: `"kv"`  Configuration:   - Variable: ansible_hashi_vault_engine_mount_point |
| **jwt**  string | The JSON Web Token (JWT) to use for JWT authentication to Vault.  Configuration:   - Environment variable: [`ANSIBLE_HASHI_VAULT_JWT`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_JWT) |
| **mount_point**  string | Vault mount point.  If not specified, the default mount point for a given auth method is used.  Does not apply to token authentication.  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   mount_point = VALUE   ```  added in community.hashi_vault 1.5.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_MOUNT_POINT`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_MOUNT_POINT)  added in community.hashi_vault 1.5.0 - Variable: ansible_hashi_vault_mount_point  added in community.hashi_vault 1.5.0 |
| **namespace**  string | Vault namespace where secrets reside. This option requires HVAC 0.7.0+ and Vault 0.11+.  Optionally, this may be achieved by prefixing the authentication mount point and/or secret path with the namespace (e.g `mynamespace/secret/mysecret`).  If environment variable `VAULT_NAMESPACE` is set, its value will be used last among all ways to specify *namespace*.  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   namespace = VALUE   ```  added in community.hashi_vault 1.4.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_NAMESPACE`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_NAMESPACE)  added in community.hashi_vault 0.2.0 - Variable: ansible_hashi_vault_namespace  added in community.hashi_vault 1.2.0 |
| **password**  string | Authentication password.  Configuration:   - Environment variable: [`ANSIBLE_HASHI_VAULT_PASSWORD`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_PASSWORD)  added in community.hashi_vault 1.2.0 - Variable: ansible_hashi_vault_password  added in community.hashi_vault 1.2.0 |
| **proxies**  any  added in community.hashi_vault 1.1.0 | URL(s) to the proxies used to access the Vault service.  It can be a string or a dict.  If it’s a dict, provide the scheme (eg. `http` or `https`) as the key, and the URL as the value.  If it’s a string, provide a single URL that will be used as the proxy for both `http` and `https` schemes.  A string that can be interpreted as a dictionary will be converted to one (see examples).  You can specify a different proxy for HTTP and HTTPS resources.  If not specified, [environment variables from the Requests library](https://requests.readthedocs.io/en/master/user/advanced/#proxies) are used.  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   proxies = VALUE   ```  added in community.hashi_vault 1.4.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_PROXIES`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_PROXIES) - Variable: ansible_hashi_vault_proxies  added in community.hashi_vault 1.2.0 |
| **region**  string | The AWS region for which to create the connection.  Configuration:   - Environment variable: [`EC2_REGION`](../../environment_variables.md#envvar-EC2_REGION) - Environment variable: [`AWS_REGION`](../../environment_variables.md#envvar-AWS_REGION) |
| **retries**  any  added in community.hashi_vault 1.3.0 | Allows for retrying on errors, based on the [Retry class in the urllib3 library](https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html#urllib3.util.Retry).  This collection defines recommended defaults for retrying connections to Vault.  This option can be specified as a positive number (integer) or dictionary.  If this option is not specified or the number is `0`, then retries are disabled.  A number sets the total number of retries, and uses collection defaults for the other settings.  A dictionary value is used directly to initialize the `Retry` class, so it can be used to fully customize retries.  For detailed information on retries, see the collection User Guide.  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   retries = VALUE   ```  added in community.hashi_vault 1.4.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_RETRIES`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_RETRIES) - Variable: ansible_hashi_vault_retries |
| **retry_action**  string  added in community.hashi_vault 1.3.0 | Controls whether and how to show messages on *retries*.  This has no effect if a request is not retried.  Choices:   - `"ignore"` - `"warn"` ← (default)   Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   retry_action = warn   ```  added in community.hashi_vault 1.4.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_RETRY_ACTION`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_RETRY_ACTION) - Variable: ansible_hashi_vault_retry_action |
| **role_id**  string | Vault Role ID or name. Used in `approle`, `aws_iam`, `azure` and `cert` auth methods.  For `cert` auth, if no *role_id* is supplied, the default behavior is to try all certificate roles and return any one that matches.  For `azure` auth, *role_id* is required.  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   role_id = VALUE   ```  added in community.hashi_vault 1.4.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_ROLE_ID`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_ROLE_ID)  added in community.hashi_vault 0.2.0 - Variable: ansible_hashi_vault_role_id  added in community.hashi_vault 1.2.0 |
| **secret_id**  string | Secret ID to be used for Vault AppRole authentication.  Configuration:   - Environment variable: [`ANSIBLE_HASHI_VAULT_SECRET_ID`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_SECRET_ID)  added in community.hashi_vault 0.2.0 - Variable: ansible_hashi_vault_secret_id  added in community.hashi_vault 1.2.0 |
| **timeout**  integer  added in community.hashi_vault 1.3.0 | Sets the connection timeout in seconds.  If not set, then the `hvac` library’s default is used.  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   timeout = VALUE   ```  added in community.hashi_vault 1.4.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_TIMEOUT`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_TIMEOUT) - Variable: ansible_hashi_vault_timeout |
| **token**  string | Vault token. Token may be specified explicitly, through the listed [env] vars, and also through the `VAULT_TOKEN` env var.  If no token is supplied, explicitly or through env, then the plugin will check for a token file, as determined by *token_path* and *token_file*.  The order of token loading (first found wins) is `token param -> ansible var -> ANSIBLE_HASHI_VAULT_TOKEN -> VAULT_TOKEN -> token file`.  Configuration:   - Environment variable: [`ANSIBLE_HASHI_VAULT_TOKEN`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_TOKEN)  added in community.hashi_vault 0.2.0 - Variable: ansible_hashi_vault_token  added in community.hashi_vault 1.2.0 |
| **token_file**  string | If no token is specified, will try to read the token from this file in *token_path*.  Default: `".vault-token"`  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   token_file = .vault-token   ```  added in community.hashi_vault 1.4.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_TOKEN_FILE`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_TOKEN_FILE)  added in community.hashi_vault 0.2.0 - Variable: ansible_hashi_vault_token_file  added in community.hashi_vault 1.2.0 |
| **token_path**  string | If no token is specified, will try to read the *token_file* from this path.  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   token_path = VALUE   ```  added in community.hashi_vault 1.4.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_TOKEN_PATH`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_TOKEN_PATH)  added in community.hashi_vault 0.2.0 - Variable: ansible_hashi_vault_token_path  added in community.hashi_vault 1.2.0 |
| **token_validate**  boolean  added in community.hashi_vault 0.2.0 | For token auth, will perform a `lookup-self` operation to determine the token’s validity before using it.  Disable if your token does not have the `lookup-self` capability.  The default value is `true`.  The default value will change to `false` in version 4.0.0.  Choices:   - `false` - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   token_validate = VALUE   ```  added in community.hashi_vault 1.4.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_TOKEN_VALIDATE`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_TOKEN_VALIDATE) - Variable: ansible_hashi_vault_token_validate  added in community.hashi_vault 1.2.0 |
| **url**  string | URL to the Vault service.  If not specified by any other means, the value of the `VAULT_ADDR` environment variable will be used.  If `VAULT_ADDR` is also not defined then an error will be raised.  Configuration:   - INI entry:  ```YAML+Jinja   [hashi_vault_collection]   url = VALUE   ```  added in community.hashi_vault 1.4.0 - Environment variable: [`ANSIBLE_HASHI_VAULT_ADDR`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_ADDR)  added in community.hashi_vault 0.2.0 - Variable: ansible_hashi_vault_url  added in community.hashi_vault 1.2.0 - Variable: ansible_hashi_vault_addr  added in community.hashi_vault 1.2.0 |
| **username**  string | Authentication user name.  Configuration:   - Environment variable: [`ANSIBLE_HASHI_VAULT_USERNAME`](../../environment_variables.md#envvar-ANSIBLE_HASHI_VAULT_USERNAME)  added in community.hashi_vault 1.2.0 - Variable: ansible_hashi_vault_username  added in community.hashi_vault 1.2.0 |
| **validate_certs**  boolean | Controls verification and validation of SSL certificates, mostly you only want to turn off with self signed ones.  Will be populated with the inverse of `VAULT_SKIP_VERIFY` if that is set and *validate_certs* is not explicitly provided.  Will default to `true` if neither *validate_certs* or `VAULT_SKIP_VERIFY` are set.  Choices:   - `false` - `true`   Configuration:   - Variable: ansible_hashi_vault_validate_certs  added in community.hashi_vault 1.2.0 |

## [Notes](vault_kv1_get_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.hashi_vault.vault_kv1_get', term1, term2, key1=value1, key2=value2)` and `query('community.hashi_vault.vault_kv1_get', term1, term2, key1=value1, key2=value2)`

## [See Also](vault_kv1_get_lookup.md#id6)

> **See also:**
>
> [community.hashi_vault.vault_kv1_get](vault_kv1_get_module.md#ansible-collections-community-hashi-vault-vault-kv1-get-module)
> :   Get a secret from HashiCorp Vault’s KV version 1 secret store.
>
> [community.hashi_vault.vault_kv2_get lookup](vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup)
> :   The official documentation for the `community.hashi_vault.vault_kv2_get` lookup plugin.
>
> [community.hashi_vault.vault_kv2_get](vault_kv2_get_module.md#ansible-collections-community-hashi-vault-vault-kv2-get-module)
> :   Get a secret from HashiCorp Vault’s KV version 2 secret store.
>
> [community.hashi_vault Lookup Guide](docsite/lookup_guide.md#ansible-collections-community-hashi-vault-docsite-lookup-guide)
> :   Guidance on using lookups in `community.hashi_vault`.
>
> [KV1 Secrets Engine](https://www.vaultproject.io/docs/secrets/kv/kv-v1)
> :   Documentation for the Vault KV secrets engine, version 1.

## [Examples](vault_kv1_get_lookup.md#id7)

```yaml+jinja
- name: Read a kv1 secret with the default mount point
  ansible.builtin.set_fact:
    response: "{{ lookup('community.hashi_vault.vault_kv1_get', 'hello', url='https://vault:8201') }}"
  # equivalent API path is kv/hello

- name: Display the results
  ansible.builtin.debug:
    msg:
      - "Secret: {{ response.secret }}"
      - "Data: {{ response.data }} (same as secret in kv1)"
      - "Metadata: {{ response.metadata }} (response info in kv1)"
      - "Full response: {{ response.raw }}"
      - "Value of key 'password' in the secret: {{ response.secret.password }}"

- name: Read a kv1 secret with a different mount point
  ansible.builtin.set_fact:
    response: "{{ lookup('community.hashi_vault.vault_kv1_get', 'hello', engine_mount_point='custom/kv1/mount', url='https://vault:8201') }}"
  # equivalent API path is custom/kv1/mount/hello

- name: Display the results
  ansible.builtin.debug:
    msg:
      - "Secret: {{ response.secret }}"
      - "Data: {{ response.data }} (same as secret in kv1)"
      - "Metadata: {{ response.metadata }} (response info in kv1)"
      - "Full response: {{ response.raw }}"
      - "Value of key 'password' in the secret: {{ response.secret.password }}"

- name: Perform multiple kv1 reads with a single Vault login, showing the secrets
  vars:
    paths:
      - hello
      - my-secret/one
      - my-secret/two
  ansible.builtin.debug:
    msg: "{{ lookup('community.hashi_vault.vault_kv1_get', *paths, auth_method='userpass', username=user, password=pwd)['secret'] }}"

- name: Perform multiple kv1 reads with a single Vault login in a loop
  vars:
    paths:
      - hello
      - my-secret/one
      - my-secret/two
  ansible.builtin.debug:
    msg: '{{ item }}'
  loop: "{{ query('community.hashi_vault.vault_kv1_get', *paths, auth_method='userpass', username=user, password=pwd) }}"

- name: Perform multiple kv1 reads with a single Vault login in a loop (via with_), display values only
  vars:
    ansible_hashi_vault_auth_method: userpass
    ansible_hashi_vault_username: '{{ user }}'
    ansible_hashi_vault_password: '{{ pwd }}'
  ansible.builtin.debug:
    msg: '{{ item.values() | list }}'
  with_community.hashi_vault.vault_kv1_get:
    - hello
    - my-secret/one
    - my-secret/two
```

## [Return Value](vault_kv1_get_lookup.md#id8)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=dictionary | The result of the read(s) against the given path(s).  Returned: success |
| **data**  dictionary | The `data` field of raw result. This can also be accessed via `raw.data`.  Returned: success  Sample: `{"Key1": "value1", "Key2": "value2"}` |
| **metadata**  dictionary | This is a synthetic result. It is the same as `raw` with `data` removed.  Returned: success  Sample: `{"auth": null, "lease_duration": 2764800, "lease_id": "", "renewable": false, "request_id": "e99f145f-f02a-7073-1229-e3f191057a70", "warnings": null, "wrap_info": null}` |
| **raw**  dictionary | The raw result of the read against the given path.  Returned: success  Sample: `{"auth": null, "data": {"Key1": "value1", "Key2": "value2"}, "lease_duration": 2764800, "lease_id": "", "renewable": false, "request_id": "e99f145f-f02a-7073-1229-e3f191057a70", "warnings": null, "wrap_info": null}` |
| **secret**  dictionary | The `data` field of the raw result. This is identical to `data` in the return values.  Returned: success  Sample: `{"Key1": "value1", "Key2": "value2"}` |

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
