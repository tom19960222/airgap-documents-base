---
collection: ansible
version: "8"
title: "sensu.sensu_go.secret module – Manage Sensu Go secrets"
source_url: https://docs.ansible.com/projects/ansible/8/collections/sensu/sensu_go/secret_module.html
fetched_at: 2026-07-28T02:53:31+00:00
---
# sensu.sensu_go.secret module – Manage Sensu Go secrets

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
> see [Requirements](secret_module.md#ansible-collections-sensu-sensu-go-secret-module-requirements) for details.
>
> To use it in a playbook, specify: `sensu.sensu_go.secret`.

New in sensu.sensu_go 1.6.0

- [Synopsis](secret_module.md#synopsis)
- [Requirements](secret_module.md#requirements)
- [Parameters](secret_module.md#parameters)
- [See Also](secret_module.md#see-also)
- [Examples](secret_module.md#examples)
- [Return Values](secret_module.md#return-values)

## [Synopsis](secret_module.md#id1)

- Create, update or delete Sensu secret.
- For more information, refer to the Sensu documentation at <https://docs.sensu.io/sensu-go/latest/operations/manage-secrets/secrets/>.

## [Requirements](secret_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7

## [Parameters](secret_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth**  dictionary | Authentication parameters. Can define each of them with ENV as well. |
| **api_key**  string  *added in sensu.sensu_go 1.3.0* | The API key that should be used when authenticating. If this is not set, the value of the SENSU_API_KEY environment variable will be checked.  This replaces *auth.user* and *auth.password* parameters.  For more information about the API key, refer to the official Sensu documentation at <https://docs.sensu.io/sensu-go/latest/guides/use-apikey-feature/>. |
| **ca_path**  path  *added in sensu.sensu_go 1.5.0* | Path to the CA bundle that should be used to validate the backend certificate.  If this parameter is not set, module will use the CA bundle that python is using.  It is also possible to set this parameter via the *SENSU_CA_PATH* environment variable. |
| **password**  string | The Sensu user’s password. If this is not set the value of the SENSU_PASSWORD environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  **Default:** `"P@ssw0rd!"` |
| **url**  string | Location of the Sensu backend API. If this is not set the value of the SENSU_URL environment variable will be checked.  **Default:** `"http://localhost:8080"` |
| **user**  string | The username to use for connecting to the Sensu API. If this is not set the value of the SENSU_USER environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  **Default:** `"admin"` |
| **verify**  boolean  *added in sensu.sensu_go 1.5.0* | Flag that controls the certificate validation.  If you are using self-signed certificates, you can set this parameter to `false`.  ONLY USE THIS PARAMETER IN DEVELOPMENT SCENARIOS! In you use self-signed certificates in production, see the *auth.ca_path* parameter.  It is also possible to set this parameter via the *SENSU_VERIFY* environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **id**  string | Secret’s id in the provider store.  Required if *state* is `present`. |
| **name**  string / required | The Sensu resource’s name. This name (in combination with the namespace where applicable) uniquely identifies the resource that Ansible operates on.  If the resource with selected name already exists, Ansible module will update it to match the specification in the task.  Consult the *name* metadata attribute specification in the upstream docs on <https://docs.sensu.io/sensu-go/latest/reference/> for more details about valid names and other restrictions. |
| **namespace**  string | RBAC namespace to operate in. If this is not set the value of the SENSU_NAMESPACE environment variable will be used.  **Default:** `"default"` |
| **provider**  string | Name of the secrets provider that backs the secret value.  Required if *state* is `present`. |
| **state**  string | Target state of the Sensu object.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [See Also](secret_module.md#id4)

> **See also:**
>
> [sensu.sensu_go.secret_info](secret_info_module.md#ansible-collections-sensu-sensu-go-secret-info-module)
> :   List available Sensu Go secrets.
>
> [sensu.sensu_go.secrets_provider_env](secrets_provider_env_module.md#ansible-collections-sensu-sensu-go-secrets-provider-env-module)
> :   Manage Sensu Env secrets provider.
>
> [sensu.sensu_go.secrets_provider_vault](secrets_provider_vault_module.md#ansible-collections-sensu-sensu-go-secrets-provider-vault-module)
> :   Manage Sensu VaultProvider secrets providers.
>
> [sensu.sensu_go.secrets_provider_info](secrets_provider_info_module.md#ansible-collections-sensu-sensu-go-secrets-provider-info-module)
> :   List Sensu secrets providers.

## [Examples](secret_module.md#id5)

```yaml+jinja
- name: Create an environment varibale-backed secret
  sensu.sensu_go.secret:
    name: env_secret
    provider: env
    id: MY_ENV_VARIABLE

- name: Create a HashiCorp Vault-backed secret
  sensu.sensu_go.secret:
    name: hashi_valut_secret
    provider: vault
    id: secret/store#name

- name: Delete a secret
  sensu.sensu_go.secret:
    name: my_secret
    state: absent
```

## [Return Values](secret_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **object**  dictionary | Object representing Sensu secret.  **Returned:** success  **Sample:** `{"id": "secret/database#password", "metadata": {"name": "sensu-ansible", "namespace": "default"}, "provider": "vault"}` |

### Authors

- Aljaz Kosir (@aljazkosir)
- Manca Bizjak (@mancabizjak)
- Miha Dolinar (@mdolin)
- Tadej Borovsak (@tadeboro)

### Collection links

- [Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
- [Repository (Sources)](https://github.com/sensu/sensu-go-ansible)
