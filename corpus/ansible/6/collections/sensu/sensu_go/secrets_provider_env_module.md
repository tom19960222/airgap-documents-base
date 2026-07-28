---
collection: ansible
version: "6"
title: "sensu.sensu_go.secrets_provider_env module – Manage Sensu Env secrets provider"
source_url: https://docs.ansible.com/projects/ansible/6/collections/sensu/sensu_go/secrets_provider_env_module.html
fetched_at: 2026-07-28T00:19:46+00:00
---
# sensu.sensu_go.secrets_provider_env module – Manage Sensu Env secrets provider

> **Note:**
>
> This module is part of the [sensu.sensu_go collection](https://galaxy.ansible.com/sensu/sensu_go) (version 1.13.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install sensu.sensu_go`.
> You need further requirements to be able to use this module,
> see [Requirements](secrets_provider_env_module.md#ansible-collections-sensu-sensu-go-secrets-provider-env-module-requirements) for details.
>
> To use it in a playbook, specify: `sensu.sensu_go.secrets_provider_env`.

New in sensu.sensu_go 1.6.0

- [Synopsis](secrets_provider_env_module.md#synopsis)
- [Requirements](secrets_provider_env_module.md#requirements)
- [Parameters](secrets_provider_env_module.md#parameters)
- [See Also](secrets_provider_env_module.md#see-also)
- [Examples](secrets_provider_env_module.md#examples)
- [Return Values](secrets_provider_env_module.md#return-values)

## [Synopsis](secrets_provider_env_module.md#id1)

- Create or delete a Sensu Go Env secrets provider.
- The module operates on a secrets provider named `env`.
- For more information, refer to the Sensu Go documentation at <https://docs.sensu.io/sensu-go/latest/operations/manage-secrets/secrets-providers/>.

## [Requirements](secrets_provider_env_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7

## [Parameters](secrets_provider_env_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth**  dictionary | Authentication parameters. Can define each of them with ENV as well. |
| **api_key**  string  added in sensu.sensu_go 1.3.0 | The API key that should be used when authenticating. If this is not set, the value of the SENSU_API_KEY environment variable will be checked.  This replaces *auth.user* and *auth.password* parameters.  For more information about the API key, refer to the official Sensu documentation at <https://docs.sensu.io/sensu-go/latest/guides/use-apikey-feature/>. |
| **ca_path**  path  added in sensu.sensu_go 1.5.0 | Path to the CA bundle that should be used to validate the backend certificate.  If this parameter is not set, module will use the CA bundle that python is using.  It is also possible to set this parameter via the *SENSU_CA_PATH* environment variable. |
| **password**  string | The Sensu user’s password. If this is not set the value of the SENSU_PASSWORD environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  Default: `"P@ssw0rd!"` |
| **url**  string | Location of the Sensu backend API. If this is not set the value of the SENSU_URL environment variable will be checked.  Default: `"http://localhost:8080"` |
| **user**  string | The username to use for connecting to the Sensu API. If this is not set the value of the SENSU_USER environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  Default: `"admin"` |
| **verify**  boolean  added in sensu.sensu_go 1.5.0 | Flag that controls the certificate validation.  If you are using self-signed certificates, you can set this parameter to `false`.  ONLY USE THIS PARAMETER IN DEVELOPMENT SCENARIOS! In you use self-signed certificates in production, see the *auth.ca_path* parameter.  It is also possible to set this parameter via the *SENSU_VERIFY* environment variable.  Choices:   - `false` - `true` ← (default) |
| **state**  string | Target state of the Sensu object.  Choices:   - `"present"` ← (default) - `"absent"` |

## [See Also](secrets_provider_env_module.md#id4)

> **See also:**
>
> [sensu.sensu_go.secrets_provider_vault](secrets_provider_vault_module.md#ansible-collections-sensu-sensu-go-secrets-provider-vault-module)
> :   Manage Sensu VaultProvider secrets providers.
>
> [sensu.sensu_go.secrets_provider_info](secrets_provider_info_module.md#ansible-collections-sensu-sensu-go-secrets-provider-info-module)
> :   List Sensu secrets providers.
>
> [sensu.sensu_go.secret](secret_module.md#ansible-collections-sensu-sensu-go-secret-module)
> :   Manage Sensu Go secrets.
>
> [sensu.sensu_go.secret_info](secret_info_module.md#ansible-collections-sensu-sensu-go-secret-info-module)
> :   List available Sensu Go secrets.

## [Examples](secrets_provider_env_module.md#id5)

```yaml+jinja
- name: Create the env secrets provider
  sensu.sensu_go.secrets_provider_env:

- name: Delete the env secrets provider
  sensu.sensu_go.secrets_provider_env:
    state: absent
```

## [Return Values](secrets_provider_env_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **object**  dictionary | Object representing Sensu Env secrets provider.  Returned: success  Sample: `[{"metadata": {"name": "env"}}]` |

### Authors

- Aljaz Kosir (@aljazkosir)
- Manca Bizjak (@mancabizjak)
- Miha Dolinar (@mdolin)
- Tadej Borovsak (@tadeboro)

### Collection links

[Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
[Repository (Sources)](https://github.com/sensu/sensu-go-ansible)
