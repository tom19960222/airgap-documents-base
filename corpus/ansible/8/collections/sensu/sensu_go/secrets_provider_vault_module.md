---
collection: ansible
version: "8"
title: "sensu.sensu_go.secrets_provider_vault module – Manage Sensu VaultProvider secrets providers"
source_url: https://docs.ansible.com/projects/ansible/8/collections/sensu/sensu_go/secrets_provider_vault_module.html
fetched_at: 2026-07-28T02:53:35+00:00
---
# sensu.sensu_go.secrets_provider_vault module – Manage Sensu VaultProvider secrets providers

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
> see [Requirements](secrets_provider_vault_module.md#ansible-collections-sensu-sensu-go-secrets-provider-vault-module-requirements) for details.
>
> To use it in a playbook, specify: `sensu.sensu_go.secrets_provider_vault`.

New in sensu.sensu_go 1.6.0

- [Synopsis](secrets_provider_vault_module.md#synopsis)
- [Requirements](secrets_provider_vault_module.md#requirements)
- [Parameters](secrets_provider_vault_module.md#parameters)
- [See Also](secrets_provider_vault_module.md#see-also)
- [Examples](secrets_provider_vault_module.md#examples)
- [Return Values](secrets_provider_vault_module.md#return-values)

## [Synopsis](secrets_provider_vault_module.md#id1)

- Create, update or delete a Sensu Go VaultProvider secrets provider.
- For more information, refer to the Sensu Go documentation at <https://docs.sensu.io/sensu-go/latest/operations/manage-secrets/secrets-providers/>.

## [Requirements](secrets_provider_vault_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7

## [Parameters](secrets_provider_vault_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **address**  string | Address of the Vault server.  Required if *state* is `present`. |
| **auth**  dictionary | Authentication parameters. Can define each of them with ENV as well. |
| **api_key**  string  *added in sensu.sensu_go 1.3.0* | The API key that should be used when authenticating. If this is not set, the value of the SENSU_API_KEY environment variable will be checked.  This replaces *auth.user* and *auth.password* parameters.  For more information about the API key, refer to the official Sensu documentation at <https://docs.sensu.io/sensu-go/latest/guides/use-apikey-feature/>. |
| **ca_path**  path  *added in sensu.sensu_go 1.5.0* | Path to the CA bundle that should be used to validate the backend certificate.  If this parameter is not set, module will use the CA bundle that python is using.  It is also possible to set this parameter via the *SENSU_CA_PATH* environment variable. |
| **password**  string | The Sensu user’s password. If this is not set the value of the SENSU_PASSWORD environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  **Default:** `"P@ssw0rd!"` |
| **url**  string | Location of the Sensu backend API. If this is not set the value of the SENSU_URL environment variable will be checked.  **Default:** `"http://localhost:8080"` |
| **user**  string | The username to use for connecting to the Sensu API. If this is not set the value of the SENSU_USER environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  **Default:** `"admin"` |
| **verify**  boolean  *added in sensu.sensu_go 1.5.0* | Flag that controls the certificate validation.  If you are using self-signed certificates, you can set this parameter to `false`.  ONLY USE THIS PARAMETER IN DEVELOPMENT SCENARIOS! In you use self-signed certificates in production, see the *auth.ca_path* parameter.  It is also possible to set this parameter via the *SENSU_VERIFY* environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **burst_limit**  integer | Maximum allowed number of secrets requests in a rate interval. |
| **max_retries**  integer | Maximum number of times to retry failed connections to Vault server. |
| **name**  string / required | The Sensu resource’s name. This name (in combination with the namespace where applicable) uniquely identifies the resource that Ansible operates on.  If the resource with selected name already exists, Ansible module will update it to match the specification in the task.  Consult the *name* metadata attribute specification in the upstream docs on <https://docs.sensu.io/sensu-go/latest/reference/> for more details about valid names and other restrictions. |
| **rate_limit**  float | Maximum number of secrets requests for per second. |
| **state**  string | Target state of the Sensu object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | Timeout (in seconds) for connection to Vault server. |
| **tls**  dictionary | TLS configuration for establishing connection with Vault server. |
| **ca_cert**  string | Path to the certificate file of the trusted certificate authority. |
| **client_cert**  string | Path to the client certificate file. |
| **client_key**  string | Path to the client key file. |
| **cname**  string | Canonical name for the client. |
| **token**  string | Authentication token to use with Vault.  Required if *state* is `present`. |
| **version**  string | Version of the Vault key/value store.  Please refer to <https://www.vaultproject.io/docs/secrets/kv> for additional information.  Required if *state* is `present`.  **Choices:**   - `"v1"` - `"v2"` |

## [See Also](secrets_provider_vault_module.md#id4)

> **See also:**
>
> [sensu.sensu_go.secrets_provider_env](secrets_provider_env_module.md#ansible-collections-sensu-sensu-go-secrets-provider-env-module)
> :   Manage Sensu Env secrets provider.
>
> [sensu.sensu_go.secrets_provider_info](secrets_provider_info_module.md#ansible-collections-sensu-sensu-go-secrets-provider-info-module)
> :   List Sensu secrets providers.
>
> [sensu.sensu_go.secret](secret_module.md#ansible-collections-sensu-sensu-go-secret-module)
> :   Manage Sensu Go secrets.
>
> [sensu.sensu_go.secret_info](secret_info_module.md#ansible-collections-sensu-sensu-go-secret-info-module)
> :   List available Sensu Go secrets.

## [Examples](secrets_provider_vault_module.md#id5)

```yaml+jinja
- name: Create a vault secrets provider
  sensu.sensu_go.secrets_provider_vault:
    name: my-vault
    address: https://my-vault.com
    token: VAULT_TOKEN
    version: v1

- name: Delete a vault secrets provider
  sensu.sensu_go.secrets_provider_vault:
    name: my-vault
    state: absent
```

## [Return Values](secrets_provider_vault_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **object**  dictionary | Object representing Sensu vault secrets provider.  **Returned:** success  **Sample:** `{"client": {"address": "https://vaultserver.example.com:8200", "max_retries": 2, "rate_limiter": {"burst": 100, "limit": 10}, "timeout": "20s", "tls": {"ca_cert": "/etc/ssl/certs/vault_ca_cert.pem"}, "token": "VAULT_TOKEN", "version": "v1"}, "metadata": {"name": "vault"}}` |

### Authors

- Aljaz Kosir (@aljazkosir)
- Manca Bizjak (@mancabizjak)
- Miha Dolinar (@mdolin)
- Tadej Borovsak (@tadeboro)

### Collection links

- [Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
- [Repository (Sources)](https://github.com/sensu/sensu-go-ansible)
