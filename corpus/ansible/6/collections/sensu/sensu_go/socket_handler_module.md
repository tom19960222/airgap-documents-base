---
collection: ansible
version: "6"
title: "sensu.sensu_go.socket_handler module – Manage Sensu TCP/UDP handler"
source_url: https://docs.ansible.com/projects/ansible/6/collections/sensu/sensu_go/socket_handler_module.html
fetched_at: 2026-07-28T00:19:50+00:00
---
# sensu.sensu_go.socket_handler module – Manage Sensu TCP/UDP handler

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
> see [Requirements](socket_handler_module.md#ansible-collections-sensu-sensu-go-socket-handler-module-requirements) for details.
>
> To use it in a playbook, specify: `sensu.sensu_go.socket_handler`.

New in sensu.sensu_go 1.0.0

- [Synopsis](socket_handler_module.md#synopsis)
- [Requirements](socket_handler_module.md#requirements)
- [Parameters](socket_handler_module.md#parameters)
- [See Also](socket_handler_module.md#see-also)
- [Examples](socket_handler_module.md#examples)
- [Return Values](socket_handler_module.md#return-values)

## [Synopsis](socket_handler_module.md#id1)

- Create, update or delete Sensu socket handler.
- For more information, refer to the Sensu documentation at <https://docs.sensu.io/sensu-go/latest/reference/handlers/#tcp-udp-handlers>.

## [Requirements](socket_handler_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7

## [Parameters](socket_handler_module.md#id3)

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
| **filters**  list / elements=string | List of filters to use when determining whether to pass the check result to this handler. |
| **host**  string | The socket host address (IP or hostname) to connect to.  Required if *state* is `present`. |
| **labels**  dictionary | Custom metadata fields that can be accessed within Sensu, as key/value pairs. |
| **mutator**  string | Mutator to call for transforming the check result before passing it to this handler. |
| **name**  string / required | The Sensu resource’s name. This name (in combination with the namespace where applicable) uniquely identifies the resource that Ansible operates on.  If the resource with selected name already exists, Ansible module will update it to match the specification in the task.  Consult the *name* metadata attribute specification in the upstream docs on <https://docs.sensu.io/sensu-go/latest/reference/> for more details about valid names and other restrictions. |
| **namespace**  string | RBAC namespace to operate in. If this is not set the value of the SENSU_NAMESPACE environment variable will be used.  Default: `"default"` |
| **port**  integer | The socket port to connect to.  Required if *state* is `present`. |
| **state**  string | Target state of the Sensu object.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | Timeout for handler execution. |
| **type**  string | The handler type.  Required if *state* is `present`.  Choices:   - `"tcp"` - `"udp"` |

## [See Also](socket_handler_module.md#id4)

> **See also:**
>
> [sensu.sensu_go.handler_info](handler_info_module.md#ansible-collections-sensu-sensu-go-handler-info-module)
> :   List Sensu handlers.
>
> [sensu.sensu_go.pipe_handler](pipe_handler_module.md#ansible-collections-sensu-sensu-go-pipe-handler-module)
> :   Manage Sensu pipe handler.
>
> [sensu.sensu_go.handler_set](handler_set_module.md#ansible-collections-sensu-sensu-go-handler-set-module)
> :   Manage Sensu handler set.

## [Examples](socket_handler_module.md#id5)

```yaml+jinja
- name: TCP handler
  sensu.sensu_go.socket_handler:
    name: tcp_handler
    type: tcp
    host: 10.0.1.99
    port: 4444

- name: UDP handler
  sensu.sensu_go.socket_handler:
    name: udp_handler
    type: udp
    host: 10.0.1.99
    port: 4444

- name: Delete a handler
  sensu.sensu_go.socket_handler:
    name: udp_handler
    state: absent
```

## [Return Values](socket_handler_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **object**  dictionary | Object representing Sensu socket handler.  Returned: success  Sample: `[{"metadata": {"name": "udp_handler", "namespace": "default"}, "socket": {"host": "10.0.1.99", "port": 4444}, "type": "udp"}]` |

### Authors

- Aljaz Kosir (@aljazkosir)
- Miha Plesko (@miha-plesko)
- Tadej Borovsak (@tadeboro)

### Collection links

[Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
[Repository (Sources)](https://github.com/sensu/sensu-go-ansible)
