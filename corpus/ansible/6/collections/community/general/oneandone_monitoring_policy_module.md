---
collection: ansible
version: "6"
title: "community.general.oneandone_monitoring_policy module – Configure 1&1 monitoring policy"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/oneandone_monitoring_policy_module.html
fetched_at: 2026-07-27T17:11:19+00:00
---
# community.general.oneandone_monitoring_policy module – Configure 1&1 monitoring policy

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](oneandone_monitoring_policy_module.md#ansible-collections-community-general-oneandone-monitoring-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.oneandone_monitoring_policy`.

- [Synopsis](oneandone_monitoring_policy_module.md#synopsis)
- [Requirements](oneandone_monitoring_policy_module.md#requirements)
- [Parameters](oneandone_monitoring_policy_module.md#parameters)
- [Examples](oneandone_monitoring_policy_module.md#examples)
- [Return Values](oneandone_monitoring_policy_module.md#return-values)

## [Synopsis](oneandone_monitoring_policy_module.md#id1)

- Create, remove, update monitoring policies (and add/remove ports, processes, and servers). This module has a dependency on 1and1 >= 1.0

## [Requirements](oneandone_monitoring_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- 1and1
- python >= 2.6

## [Parameters](oneandone_monitoring_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **add_ports**  list / elements=dictionary | Ports to add to the monitoring policy.  Default: `[]` |
| **add_processes**  list / elements=dictionary | Processes to add to the monitoring policy.  Default: `[]` |
| **add_servers**  list / elements=string | Servers to add to the monitoring policy.  Default: `[]` |
| **agent**  string | Set true for using agent. |
| **api_url**  string | Custom API URL. Overrides the ONEANDONE_API_URL environment variable. |
| **auth_token**  string | Authenticating API token provided by 1&1. |
| **description**  string | Monitoring policy description. maxLength=256 |
| **email**  string | User’s email. maxLength=128 |
| **monitoring_policy**  string | The identifier (id or name) of the monitoring policy used with update state. |
| **name**  string | Monitoring policy name used with present state. Used as identifier (id or name) when used with absent state. maxLength=128 |
| **ports**  list / elements=dictionary | Array of ports that will be monitoring.  Default: `[]` |
| **alert_if**  string / required | Case of alert.  Choices:   - `"RESPONDING"` - `"NOT_RESPONDING"` |
| **email_notification**  string / required | Set true for sending e-mail notifications. |
| **port**  string / required | Port number. minimum=1, maximum=65535 |
| **protocol**  string / required | Internet protocol.  Choices:   - `"TCP"` - `"UDP"` |
| **processes**  list / elements=dictionary | Array of processes that will be monitoring.  Default: `[]` |
| **alert_if**  string / required | Case of alert.  Choices:   - `"RUNNING"` - `"NOT_RUNNING"` |
| **process**  string / required | Name of the process. maxLength=50 |
| **remove_ports**  list / elements=string | Ports to remove from the monitoring policy.  Default: `[]` |
| **remove_processes**  list / elements=string | Processes to remove from the monitoring policy.  Default: `[]` |
| **remove_servers**  list / elements=string | Servers to remove from the monitoring policy.  Default: `[]` |
| **state**  string | Define a monitoring policy’s state to create, remove, update.  Choices:   - `"present"` ← (default) - `"absent"` - `"update"` |
| **thresholds**  list / elements=dictionary | Monitoring policy thresholds. Each of the suboptions have warning and critical, which both have alert and value suboptions. Warning is used to set limits for warning alerts, critical is used to set critical alerts. alert enables alert, and value is used to advise when the value is exceeded.  Default: `[]` |
| **cpu**  string / required | Consumption limits of CPU. |
| **disk**  string / required | Consumption limits of hard disk. |
| **internal_ping**  string / required | Response limits of internal ping. |
| **ram**  string / required | Consumption limits of RAM. |
| **transfer**  string / required | Consumption limits for transfer. |
| **update_ports**  list / elements=dictionary | Ports to be updated on the monitoring policy.  Default: `[]` |
| **update_processes**  list / elements=dictionary | Processes to be updated on the monitoring policy.  Default: `[]` |
| **wait**  boolean | wait for the instance to be in state ‘running’ before returning  Choices:   - `false` - `true` ← (default) |
| **wait_interval**  integer | Defines the number of seconds to wait when using the _wait_for methods  Default: `5` |
| **wait_timeout**  integer | how long before wait gives up, in seconds  Default: `600` |

## [Examples](oneandone_monitoring_policy_module.md#id4)

```yaml+jinja
- name: Create a monitoring policy
  community.general.oneandone_monitoring_policy:
    auth_token: oneandone_private_api_key
    name: ansible monitoring policy
    description: Testing creation of a monitoring policy with ansible
    email: your@emailaddress.com
    agent: true
    thresholds:
     -
       cpu:
         warning:
           value: 80
           alert: false
         critical:
           value: 92
           alert: false
     -
       ram:
         warning:
           value: 80
           alert: false
         critical:
           value: 90
           alert: false
     -
       disk:
         warning:
           value: 80
           alert: false
         critical:
           value: 90
           alert: false
     -
       internal_ping:
         warning:
           value: 50
           alert: false
         critical:
           value: 100
           alert: false
     -
       transfer:
         warning:
           value: 1000
           alert: false
         critical:
           value: 2000
           alert: false
    ports:
     -
       protocol: TCP
       port: 22
       alert_if: RESPONDING
       email_notification: false
    processes:
     -
       process: test
       alert_if: NOT_RUNNING
       email_notification: false
    wait: true

- name: Destroy a monitoring policy
  community.general.oneandone_monitoring_policy:
    auth_token: oneandone_private_api_key
    state: absent
    name: ansible monitoring policy

- name: Update a monitoring policy
  community.general.oneandone_monitoring_policy:
    auth_token: oneandone_private_api_key
    monitoring_policy: ansible monitoring policy
    name: ansible monitoring policy updated
    description: Testing creation of a monitoring policy with ansible updated
    email: another@emailaddress.com
    thresholds:
     -
       cpu:
         warning:
           value: 70
           alert: false
         critical:
           value: 90
           alert: false
     -
       ram:
         warning:
           value: 70
           alert: false
         critical:
           value: 80
           alert: false
     -
       disk:
         warning:
           value: 70
           alert: false
         critical:
           value: 80
           alert: false
     -
       internal_ping:
         warning:
           value: 60
           alert: false
         critical:
           value: 90
           alert: false
     -
       transfer:
         warning:
           value: 900
           alert: false
         critical:
           value: 1900
           alert: false
    wait: true
    state: update

- name: Add a port to a monitoring policy
  community.general.oneandone_monitoring_policy:
    auth_token: oneandone_private_api_key
    monitoring_policy: ansible monitoring policy updated
    add_ports:
     -
       protocol: TCP
       port: 33
       alert_if: RESPONDING
       email_notification: false
    wait: true
    state: update

- name: Update existing ports of a monitoring policy
  community.general.oneandone_monitoring_policy:
    auth_token: oneandone_private_api_key
    monitoring_policy: ansible monitoring policy updated
    update_ports:
     -
       id: existing_port_id
       protocol: TCP
       port: 34
       alert_if: RESPONDING
       email_notification: false
     -
       id: existing_port_id
       protocol: TCP
       port: 23
       alert_if: RESPONDING
       email_notification: false
    wait: true
    state: update

- name: Remove a port from a monitoring policy
  community.general.oneandone_monitoring_policy:
    auth_token: oneandone_private_api_key
    monitoring_policy: ansible monitoring policy updated
    remove_ports:
     - port_id
    state: update

- name: Add a process to a monitoring policy
  community.general.oneandone_monitoring_policy:
    auth_token: oneandone_private_api_key
    monitoring_policy: ansible monitoring policy updated
    add_processes:
     -
       process: test_2
       alert_if: NOT_RUNNING
       email_notification: false
    wait: true
    state: update

- name: Update existing processes of a monitoring policy
  community.general.oneandone_monitoring_policy:
    auth_token: oneandone_private_api_key
    monitoring_policy: ansible monitoring policy updated
    update_processes:
     -
       id: process_id
       process: test_1
       alert_if: NOT_RUNNING
       email_notification: false
     -
       id: process_id
       process: test_3
       alert_if: NOT_RUNNING
       email_notification: false
    wait: true
    state: update

- name: Remove a process from a monitoring policy
  community.general.oneandone_monitoring_policy:
    auth_token: oneandone_private_api_key
    monitoring_policy: ansible monitoring policy updated
    remove_processes:
     - process_id
    wait: true
    state: update

- name: Add server to a monitoring policy
  community.general.oneandone_monitoring_policy:
    auth_token: oneandone_private_api_key
    monitoring_policy: ansible monitoring policy updated
    add_servers:
     - server id or name
    wait: true
    state: update

- name: Remove server from a monitoring policy
  community.general.oneandone_monitoring_policy:
    auth_token: oneandone_private_api_key
    monitoring_policy: ansible monitoring policy updated
    remove_servers:
     - server01
    wait: true
    state: update
```

## [Return Values](oneandone_monitoring_policy_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **monitoring_policy**  dictionary | Information about the monitoring policy that was processed  Returned: always  Sample: `{"id": "92B74394A397ECC3359825C1656D67A6", "name": "Default Policy"}` |

### Authors

- Amel Ajdinovic (@aajdinov)
- Ethan Devenport (@edevenport)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
