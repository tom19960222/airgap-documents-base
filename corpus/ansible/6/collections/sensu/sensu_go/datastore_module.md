---
collection: ansible
version: "6"
title: "sensu.sensu_go.datastore module – Manage Sensu external datastore providers"
source_url: https://docs.ansible.com/projects/ansible/6/collections/sensu/sensu_go/datastore_module.html
fetched_at: 2026-07-28T00:19:27+00:00
---
# sensu.sensu_go.datastore module – Manage Sensu external datastore providers

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
> see [Requirements](datastore_module.md#ansible-collections-sensu-sensu-go-datastore-module-requirements) for details.
>
> To use it in a playbook, specify: `sensu.sensu_go.datastore`.

New in sensu.sensu_go 1.1.0

- [Synopsis](datastore_module.md#synopsis)
- [Requirements](datastore_module.md#requirements)
- [Parameters](datastore_module.md#parameters)
- [Notes](datastore_module.md#notes)
- [See Also](datastore_module.md#see-also)
- [Examples](datastore_module.md#examples)
- [Return Values](datastore_module.md#return-values)

## [Synopsis](datastore_module.md#id1)

- Add or remove external datastore provider.
- For more information, refer to the Sensu documentation at <https://docs.sensu.io/sensu-go/latest/reference/datastore/>.

## [Requirements](datastore_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7

## [Parameters](datastore_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth**  dictionary | Authentication parameters. Can define each of them with ENV as well. |
| **api_key**  string  added in sensu.sensu_go 1.3.0 | The API key that should be used when authenticating. If this is not set, the value of the SENSU_API_KEY environment variable will be checked.  This replaces *auth.user* and *auth.password* parameters.  For more information about the API key, refer to the official Sensu documentation at <https://docs.sensu.io/sensu-go/latest/guides/use-apikey-feature/>. |
| **ca_path**  path  added in sensu.sensu_go 1.5.0 | Path to the CA bundle that should be used to validate the backend certificate.  If this parameter is not set, module will use the CA bundle that python is using.  It is also possible to set this parameter via the *SENSU_CA_PATH* environment variable. |
| **password**  string | The Sensu user’s password. If this is not set the value of the SENSU_PASSWORD environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  Default: `"P@ssw0rd!"` |
| **url**  string | Location of the Sensu backend API. If this is not set the value of the SENSU_URL environment variable will be checked.  Default: `"http://localhost:8080"` |
| **user**  string | The username to use for connecting to the Sensu API. If this is not set the value of the SENSU_USER environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  Default: `"admin"` |
| **verify**  boolean  added in sensu.sensu_go 1.5.0 | Flag that controls the certificate validation.  If you are using self-signed certificates, you can set this parameter to `false`.  ONLY USE THIS PARAMETER IN DEVELOPMENT SCENARIOS! In you use self-signed certificates in production, see the *auth.ca_path* parameter.  It is also possible to set this parameter via the *SENSU_VERIFY* environment variable.  Choices:   - `false` - `true` ← (default) |
| **dsn**  string | Attribute that specifies the data source names as a URL or PostgreSQL connection string. See the PostgreSQL docs for more information about connection strings. |
| **name**  string / required | The Sensu resource’s name. This name (in combination with the namespace where applicable) uniquely identifies the resource that Ansible operates on.  If the resource with selected name already exists, Ansible module will update it to match the specification in the task.  Consult the *name* metadata attribute specification in the upstream docs on <https://docs.sensu.io/sensu-go/latest/reference/> for more details about valid names and other restrictions. |
| **pool_size**  integer | The maximum number of connections to hold in the PostgreSQL connection pool. |
| **state**  string | Target state of the Sensu object.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](datastore_module.md#id4)

> **Note:**
>
> - Currently, only one external datastore can be active at a time. The module will fail to perform its operation if this would break that invariant.

## [See Also](datastore_module.md#id5)

> **See also:**
>
> [sensu.sensu_go.datastore_info](datastore_info_module.md#ansible-collections-sensu-sensu-go-datastore-info-module)
> :   List external Sensu datastore providers.

## [Examples](datastore_module.md#id6)

```yaml+jinja
- name: Add external datastore
  sensu.sensu_go.datastore:
    name: my-postgres
    dsn: postgresql://user:secret@host:port/dbname

- name: Remove external datastore
  sensu.sensu_go.datastore:
    name: my-postgres
    state: absent
```

## [Return Values](datastore_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **object**  dictionary | Object representing external datastore provider.  Returned: success  Sample: `{"batch_buffer": 0, "batch_size": 1, "batch_workers": 0, "dsn": "postgresql://user:secret@host:port/dbname", "enable_round_robin": true, "max_conn_lifetime": "5m", "max_idle_conns": 2, "metadata": {"name": "my-postgres"}, "pool_size": 20, "strict": true}` |

### Authors

- Manca Bizjak (@mancabizjak)
- Tadej Borovsak (@tadeboro)

### Collection links

[Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
[Repository (Sources)](https://github.com/sensu/sensu-go-ansible)
