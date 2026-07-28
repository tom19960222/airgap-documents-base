---
collection: ansible
version: "6"
title: "sensu.sensu_go.pipe_handler module – Manage Sensu pipe handler"
source_url: https://docs.ansible.com/projects/ansible/6/collections/sensu/sensu_go/pipe_handler_module.html
fetched_at: 2026-07-28T00:19:41+00:00
---
# sensu.sensu_go.pipe_handler module – Manage Sensu pipe handler

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
> see [Requirements](pipe_handler_module.md#ansible-collections-sensu-sensu-go-pipe-handler-module-requirements) for details.
>
> To use it in a playbook, specify: `sensu.sensu_go.pipe_handler`.

New in sensu.sensu_go 1.0.0

- [Synopsis](pipe_handler_module.md#synopsis)
- [Requirements](pipe_handler_module.md#requirements)
- [Parameters](pipe_handler_module.md#parameters)
- [See Also](pipe_handler_module.md#see-also)
- [Examples](pipe_handler_module.md#examples)
- [Return Values](pipe_handler_module.md#return-values)

## [Synopsis](pipe_handler_module.md#id1)

- Create, update or delete a Sensu pipe handler.
- For more information, refer to the Sensu documentation at <https://docs.sensu.io/sensu-go/latest/reference/handlers/#pipe-handlers>.

## [Requirements](pipe_handler_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7

## [Parameters](pipe_handler_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **annotations**  dictionary | Custom metadata fields with fewer restrictions, as key/value pairs.  These are preserved by Sensu but not accessible as tokens or identifiers, and are mainly intended for use with external tools. |
| **auth**  dictionary | Authentication parameters. Can define each of them with ENV as well. |
| **api_key**  string  added in sensu.sensu_go 1.3.0 | The API key that should be used when authenticating. If this is not set, the value of the SENSU_API_KEY environment variable will be checked.  This replaces *auth.user* and *auth.password* parameters.  For more information about the API key, refer to the official Sensu documentation at <https://docs.sensu.io/sensu-go/latest/guides/use-apikey-feature/>. |
| **ca_path**  path  added in sensu.sensu_go 1.5.0 | Path to the CA bundle that should be used to validate the backend certificate.  If this parameter is not set, module will use the CA bundle that python is using.  It is also possible to set this parameter via the *SENSU_CA_PATH* environment variable. |
| **password**  string | The Sensu user’s password. If this is not set the value of the SENSU_PASSWORD environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  Default: `"P@ssw0rd!"` |
| **url**  string | Location of the Sensu backend API. If this is not set the value of the SENSU_URL environment variable will be checked.  Default: `"http://localhost:8080"` |
| **user**  string | The username to use for connecting to the Sensu API. If this is not set the value of the SENSU_USER environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  Default: `"admin"` |
| **verify**  boolean  added in sensu.sensu_go 1.5.0 | Flag that controls the certificate validation.  If you are using self-signed certificates, you can set this parameter to `false`.  ONLY USE THIS PARAMETER IN DEVELOPMENT SCENARIOS! In you use self-signed certificates in production, see the *auth.ca_path* parameter.  It is also possible to set this parameter via the *SENSU_VERIFY* environment variable.  Choices:   - `false` - `true` ← (default) |
| **command**  string | The handler command to be executed. The event data is passed to the process through STDIN.  Required if *state* is `present`. |
| **env_vars**  dictionary | A mapping of environment variable names and values to use with command execution. |
| **filters**  list / elements=string | List of filters to use when determining whether to pass the check result to this handler. |
| **labels**  dictionary | Custom metadata fields that can be accessed within Sensu, as key/value pairs. |
| **mutator**  string | Mutator to call for transforming the check result before passing it to this handler. |
| **name**  string / required | The Sensu resource’s name. This name (in combination with the namespace where applicable) uniquely identifies the resource that Ansible operates on.  If the resource with selected name already exists, Ansible module will update it to match the specification in the task.  Consult the *name* metadata attribute specification in the upstream docs on <https://docs.sensu.io/sensu-go/latest/reference/> for more details about valid names and other restrictions. |
| **namespace**  string | RBAC namespace to operate in. If this is not set the value of the SENSU_NAMESPACE environment variable will be used.  Default: `"default"` |
| **runtime_assets**  list / elements=string | List of runtime assets to required to run the handler `command`. |
| **secrets**  list / elements=dictionary  added in sensu.sensu_go 1.6.0 | List of secrets that are available to the command. |
| **name**  string / required  added in sensu.sensu_go 1.6.0 | Variable name that will contain the sensitive data. |
| **secret**  string / required  added in sensu.sensu_go 1.6.0 | Name of the secret that contains sensitive data. |
| **state**  string | Target state of the Sensu object.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | Timeout for handler execution. |

## [See Also](pipe_handler_module.md#id4)

> **See also:**
>
> [sensu.sensu_go.socket_handler](socket_handler_module.md#ansible-collections-sensu-sensu-go-socket-handler-module)
> :   Manage Sensu TCP/UDP handler.
>
> [sensu.sensu_go.handler_info](handler_info_module.md#ansible-collections-sensu-sensu-go-handler-info-module)
> :   List Sensu handlers.
>
> [sensu.sensu_go.handler_set](handler_set_module.md#ansible-collections-sensu-sensu-go-handler-set-module)
> :   Manage Sensu handler set.

## [Examples](pipe_handler_module.md#id5)

```yaml+jinja
- name: Setup InfluxDB handler
  sensu.sensu_go.pipe_handler:
    name: influx-db
    command: sensu-influxdb-handler -d sensu
    env_vars:
      INFLUXDB_ADDR: http://influxdb.default.svc.cluster.local:8086
      INFLUXDB_USER: sensu
      INFLUXDB_PASS: password
    runtime_assets:
      - sensu-influxdb-handler

- name: Delete  handler
  sensu.sensu_go.pipe_handler:
    name: influx-db
    state: absent
```

## [Return Values](pipe_handler_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **object**  dictionary | Object representing Sensu pipe handler.  Returned: success  Sample: `{"command": "command-example", "metadata": {"name": "pipe_handler_minimum", "namespace": "default"}, "type": "pipe"}` |

### Authors

- Aljaz Kosir (@aljazkosir)
- Miha Plesko (@miha-plesko)
- Tadej Borovsak (@tadeboro)

### Collection links

[Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
[Repository (Sources)](https://github.com/sensu/sensu-go-ansible)
