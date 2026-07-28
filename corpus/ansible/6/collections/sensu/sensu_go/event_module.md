---
collection: ansible
version: "6"
title: "sensu.sensu_go.event module – Manage Sensu events"
source_url: https://docs.ansible.com/projects/ansible/6/collections/sensu/sensu_go/event_module.html
fetched_at: 2026-07-28T00:19:31+00:00
---
# sensu.sensu_go.event module – Manage Sensu events

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
> see [Requirements](event_module.md#ansible-collections-sensu-sensu-go-event-module-requirements) for details.
>
> To use it in a playbook, specify: `sensu.sensu_go.event`.

New in sensu.sensu_go 1.0.0

- [Synopsis](event_module.md#synopsis)
- [Requirements](event_module.md#requirements)
- [Parameters](event_module.md#parameters)
- [Notes](event_module.md#notes)
- [See Also](event_module.md#see-also)
- [Examples](event_module.md#examples)
- [Return Values](event_module.md#return-values)

## [Synopsis](event_module.md#id1)

- Send a synthetic event to Sensu.
- For more information, refer to the Sensu documentation at <https://docs.sensu.io/sensu-go/latest/reference/events/>.

## [Requirements](event_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7

## [Parameters](event_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth**  dictionary | Authentication parameters. Can define each of them with ENV as well. |
| **api_key**  string  added in sensu.sensu_go 1.3.0 | The API key that should be used when authenticating. If this is not set, the value of the SENSU_API_KEY environment variable will be checked.  This replaces *auth.user* and *auth.password* parameters.  For more information about the API key, refer to the official Sensu documentation at <https://docs.sensu.io/sensu-go/latest/guides/use-apikey-feature/>. |
| **ca_path**  path  added in sensu.sensu_go 1.5.0 | Path to the CA bundle that should be used to validate the backend certificate.  If this parameter is not set, module will use the CA bundle that python is using.  It is also possible to set this parameter via the *SENSU_CA_PATH* environment variable. |
| **password**  string | The Sensu user’s password. If this is not set the value of the SENSU_PASSWORD environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  Default: `"P@ssw0rd!"` |
| **url**  string | Location of the Sensu backend API. If this is not set the value of the SENSU_URL environment variable will be checked.  Default: `"http://localhost:8080"` |
| **user**  string | The username to use for connecting to the Sensu API. If this is not set the value of the SENSU_USER environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  Default: `"admin"` |
| **verify**  boolean  added in sensu.sensu_go 1.5.0 | Flag that controls the certificate validation.  If you are using self-signed certificates, you can set this parameter to `false`.  ONLY USE THIS PARAMETER IN DEVELOPMENT SCENARIOS! In you use self-signed certificates in production, see the *auth.ca_path* parameter.  It is also possible to set this parameter via the *SENSU_VERIFY* environment variable.  Choices:   - `false` - `true` ← (default) |
| **check**  string / required | Name of the check associated with this event. It must exist before event creation. |
| **check_attributes**  dictionary | Additional check parameters. Find out more at <https://docs.sensu.io/sensu-go/latest/reference/events/#check-attributes>. |
| **duration**  float | Command execution time in seconds. |
| **executed**  integer | Time that the check request was executed. |
| **history**  list / elements=dictionary | Check status history for the last 21 check executions. |
| **issued**  integer | Time that the check request was issued in seconds since the Unix epoch. |
| **last_ok**  integer | The last time that the check returned an OK status (0) in seconds since the Unix epoch. |
| **output**  string | The output from the execution of the check command. |
| **state**  string | The state of the check.  Choices:   - `"passing"` - `"failing"` - `"flapping"` |
| **status**  string | Exit status code produced by the check.  Choices:   - `"ok"` - `"warning"` - `"critical"` - `"unknown"` |
| **total_state_change**  integer | The total state change percentage for the check’s history. |
| **entity**  string / required | Name of the entity associated with this event. It must exist before event creation. |
| **metric_attributes**  dictionary | Metric attributes. Find out more at <https://docs.sensu.io/sensu-go/latest/reference/events/#metric-attributes>. |
| **handlers**  list / elements=string | An array of Sensu handlers to use for events created by the check. Each array item must be a string. |
| **points**  list / elements=dictionary | Metric data points including a name, timestamp, value, and tags. |
| **namespace**  string | RBAC namespace to operate in. If this is not set the value of the SENSU_NAMESPACE environment variable will be used.  Default: `"default"` |
| **timestamp**  integer | UNIX time at which the event occurred. |

## [Notes](event_module.md#id4)

> **Note:**
>
> - Metric events bypass the store and are sent off to the event pipeline and corresponding event handlers. Read more about this at <https://docs.sensu.io/sensu-go/latest/reference/events/#metric-only-events>.

## [See Also](event_module.md#id5)

> **See also:**
>
> [sensu.sensu_go.event_info](event_info_module.md#ansible-collections-sensu-sensu-go-event-info-module)
> :   List Sensu events.

## [Examples](event_module.md#id6)

```yaml+jinja
- name: Create an event
  sensu.sensu_go.event:
    auth:
      url: http://localhost:8080
    entity: awesome_entity
    check: awesome_check
    check_attributes:
      duration: 1.945
      executed: 1522100915
      history:
        - executed: 1552505193
          status: 1
      issued: 1552506034
      last_ok: 1552506033
      output: '10'
      state: 'passing'
      status: 'ok'
      total_state_change: 0
    metric_attributes:
      handlers:
        - handler1
        - handler2
      points:
        - name: "sensu-go-sandbox.curl_timings.time_total"
          tags:
            - name: "response_time_in_ms"
              value: 101
          timestamp: 1552506033
          value: 0.005
        - name: "sensu-go-sandbox.curl_timings.time_namelookup"
          tags:
            - name: "namelookup_time_in_ms"
              value: 57
          timestamp: 1552506033
          value: 0.004
```

## [Return Values](event_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **object**  dictionary | Object representing Sensu event (deprecated).  Returned: success  Sample: `{"check": {"check_hooks": null, "command": "check-cpu.sh -w 75 -c 90", "duration": 1.07055808, "env_vars": null, "executed": 1552594757, "handlers": [], "high_flap_threshold": 0, "history": [{"executed": 1552594757, "status": 0}], "interval": 60, "metadata": {"name": "check-cpu", "namespace": "default"}, "occurrences": 1, "occurrences_watermark": 1, "output": "CPU OK - Usage:3.96", "subscriptions": ["linux"], "timeout": 0, "total_state_change": 0, "ttl": 0}, "entity": {"deregister": false, "deregistration": {}, "entity_class": "agent", "last_seen": 1552594641, "metadata": {"name": "sensu-centos", "namespace": "default"}}, "id": "3a5948f3-6ffd-4ea2-a41e-334f4a72ca2f", "metadata": {"namespace": "default"}, "sequence": 1, "timestamp": 1552594758}` |

### Authors

- Paul Arthur (@flowerysong)
- Aljaz Kosir (@aljazkosir)
- Manca Bizjak (@mancabizjak)
- Tadej Borovsak (@tadeboro)

### Collection links

[Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
[Repository (Sources)](https://github.com/sensu/sensu-go-ansible)
