---
collection: ansible
version: "6"
title: "sensu.sensu_go.event_info module – List Sensu events"
source_url: https://docs.ansible.com/projects/ansible/6/collections/sensu/sensu_go/event_info_module.html
fetched_at: 2026-07-28T00:19:31+00:00
---
# sensu.sensu_go.event_info module – List Sensu events

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
> see [Requirements](event_info_module.md#ansible-collections-sensu-sensu-go-event-info-module-requirements) for details.
>
> To use it in a playbook, specify: `sensu.sensu_go.event_info`.

New in sensu.sensu_go 1.0.0

- [Synopsis](event_info_module.md#synopsis)
- [Requirements](event_info_module.md#requirements)
- [Parameters](event_info_module.md#parameters)
- [See Also](event_info_module.md#see-also)
- [Examples](event_info_module.md#examples)
- [Return Values](event_info_module.md#return-values)

## [Synopsis](event_info_module.md#id1)

- Retrieve recent events that Sensu processed.
- For more information, refer to the Sensu documentation at <https://docs.sensu.io/sensu-go/latest/reference/events/>.

## [Requirements](event_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7

## [Parameters](event_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth**  dictionary | Authentication parameters. Can define each of them with ENV as well. |
| **api_key**  string  added in sensu.sensu_go 1.3.0 | The API key that should be used when authenticating. If this is not set, the value of the SENSU_API_KEY environment variable will be checked.  This replaces *auth.user* and *auth.password* parameters.  For more information about the API key, refer to the official Sensu documentation at <https://docs.sensu.io/sensu-go/latest/guides/use-apikey-feature/>. |
| **ca_path**  path  added in sensu.sensu_go 1.5.0 | Path to the CA bundle that should be used to validate the backend certificate.  If this parameter is not set, module will use the CA bundle that python is using.  It is also possible to set this parameter via the *SENSU_CA_PATH* environment variable. |
| **password**  string | The Sensu user’s password. If this is not set the value of the SENSU_PASSWORD environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  Default: `"P@ssw0rd!"` |
| **url**  string | Location of the Sensu backend API. If this is not set the value of the SENSU_URL environment variable will be checked.  Default: `"http://localhost:8080"` |
| **user**  string | The username to use for connecting to the Sensu API. If this is not set the value of the SENSU_USER environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  Default: `"admin"` |
| **verify**  boolean  added in sensu.sensu_go 1.5.0 | Flag that controls the certificate validation.  If you are using self-signed certificates, you can set this parameter to `false`.  ONLY USE THIS PARAMETER IN DEVELOPMENT SCENARIOS! In you use self-signed certificates in production, see the *auth.ca_path* parameter.  It is also possible to set this parameter via the *SENSU_VERIFY* environment variable.  Choices:   - `false` - `true` ← (default) |
| **check**  string | Limit results to a specific check.  *entity* must also be specified if this parameter is used. |
| **entity**  string | Limit results to a specific entity. |
| **namespace**  string | RBAC namespace to operate in. If this is not set the value of the SENSU_NAMESPACE environment variable will be used.  Default: `"default"` |

## [See Also](event_info_module.md#id4)

> **See also:**
>
> [sensu.sensu_go.event](event_module.md#ansible-collections-sensu-sensu-go-event-module)
> :   Manage Sensu events.

## [Examples](event_info_module.md#id5)

```yaml+jinja
- name: List Sensu events
  sensu.sensu_go.event_info:
  register: result

- name: List Sensu events for api.example.com
  sensu.sensu_go.event_info:
    entity: api.example.com
  register: result

- name: Filter events by check and entity
  sensu.sensu_go.event_info:
    entity: api.example.com
    check: check-cpu
  register: result
```

## [Return Values](event_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **objects**  list / elements=dictionary | List of Sensu events.  Returned: success  Sample: `[{"check": {"check_hooks": null, "command": "check-cpu.sh -w 75 -c 90", "duration": 1.07055808, "env_vars": null, "executed": 1552594757, "handlers": [], "high_flap_threshold": 0, "history": [{"executed": 1552594757, "status": 0}], "interval": 60, "metadata": {"name": "check-cpu", "namespace": "default"}, "occurrences": 1, "occurrences_watermark": 1, "output": "CPU OK - Usage:3.96", "subscriptions": ["linux"], "timeout": 0, "total_state_change": 0, "ttl": 0}, "entity": {"deregister": false, "deregistration": {}, "entity_class": "agent", "last_seen": 1552594641, "metadata": {"name": "sensu-centos", "namespace": "default"}}, "id": "3a5948f3-6ffd-4ea2-a41e-334f4a72ca2f", "metadata": {"namespace": "default"}, "sequence": 1, "timestamp": 1552594758}]` |

### Authors

- Paul Arthur (@flowerysong)
- Aljaz Kosir (@aljazkosir)
- Manca Bizjak (@mancabizjak)
- Tadej Borovsak (@tadeboro)

### Collection links

[Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
[Repository (Sources)](https://github.com/sensu/sensu-go-ansible)
