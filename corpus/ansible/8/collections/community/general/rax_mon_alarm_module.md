---
collection: ansible
version: "8"
title: "community.general.rax_mon_alarm module – Create or delete a Rackspace Cloud Monitoring alarm"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/rax_mon_alarm_module.html
fetched_at: 2026-07-28T01:49:43+00:00
---
# community.general.rax_mon_alarm module – Create or delete a Rackspace Cloud Monitoring alarm

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](rax_mon_alarm_module.md#ansible-collections-community-general-rax-mon-alarm-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.rax_mon_alarm`.

- [DEPRECATED](rax_mon_alarm_module.md#deprecated)
- [Synopsis](rax_mon_alarm_module.md#synopsis)
- [Requirements](rax_mon_alarm_module.md#requirements)
- [Parameters](rax_mon_alarm_module.md#parameters)
- [Attributes](rax_mon_alarm_module.md#attributes)
- [Notes](rax_mon_alarm_module.md#notes)
- [Examples](rax_mon_alarm_module.md#examples)
- [Status](rax_mon_alarm_module.md#status)

## [DEPRECATED](rax_mon_alarm_module.md#id1)

Removed in:
:   version 9.0.0

Why:
:   This module relies on the deprecated package pyrax.

Alternative:
:   Use the Openstack modules instead.

## [Synopsis](rax_mon_alarm_module.md#id2)

- Create or delete a Rackspace Cloud Monitoring alarm that associates an existing rax_mon_entity, rax_mon_check, and rax_mon_notification_plan with criteria that specify what conditions will trigger which levels of notifications. Rackspace monitoring module flow | rax_mon_entity -> rax_mon_check -> rax_mon_notification -> rax_mon_notification_plan -> \*rax_mon_alarm\*

Aliases: cloud.rackspace.rax_mon_alarm

## [Requirements](rax_mon_alarm_module.md#id3)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- pyrax

## [Parameters](rax_mon_alarm_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **api_key**  aliases: password  string | Rackspace API key, overrides `credentials`. |
| **auth_endpoint**  string | The URI of the authentication service.  If not specified will be set to <https://identity.api.rackspacecloud.com/v2.0/> |
| **check_id**  string / required | ID of the check that should be alerted on. May be acquired by registering the value of a rax_mon_check task. |
| **credentials**  aliases: creds_file  path | File to find the Rackspace credentials in. Ignored if `api_key` and `username` are provided. |
| **criteria**  string | Alarm DSL that describes alerting conditions and their output states. Must be between 1 and 16384 characters long. See <http://docs.rackspace.com/cm/api/v1.0/cm-devguide/content/alerts-language.html> for a reference on the alerting language. |
| **disabled**  boolean | If yes, create this alarm, but leave it in an inactive state. Defaults to no.  **Choices:**   - `false` ← (default) - `true` |
| **entity_id**  string / required | ID of the entity this alarm is attached to. May be acquired by registering the value of a rax_mon_entity task. |
| **env**  string | Environment as configured in `~/.pyrax.cfg`, see <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration>. |
| **identity_type**  string | Authentication mechanism to use, such as rackspace or keystone.  **Default:** `"rackspace"` |
| **label**  string / required | Friendly name for this alarm, used to achieve idempotence. Must be a String between 1 and 255 characters long. |
| **metadata**  dictionary | Arbitrary key/value pairs to accompany the alarm. Must be a hash of String keys and values between 1 and 255 characters long. |
| **notification_plan_id**  string / required | ID of the notification plan to trigger if this alarm fires. May be acquired by registering the value of a rax_mon_notification_plan task. |
| **region**  string | Region to create an instance in. |
| **state**  string | Ensure that the alarm with this `label` exists or does not exist.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tenant_id**  string | The tenant ID used for authentication. |
| **tenant_name**  string | The tenant name used for authentication. |
| **username**  string | Rackspace username, overrides `credentials`. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to require SSL validation of API endpoints.  **Choices:**   - `false` - `true` |

## [Attributes](rax_mon_alarm_module.md#id5)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](rax_mon_alarm_module.md#id6)

> **Note:**
>
> - The following environment variables can be used, `RAX_USERNAME`, `RAX_API_KEY`, `RAX_CREDS_FILE`, `RAX_CREDENTIALS`, `RAX_REGION`.
> - `RAX_CREDENTIALS` and `RAX_CREDS_FILE` points to a credentials file appropriate for pyrax. See <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#authenticating>
> - `RAX_USERNAME` and `RAX_API_KEY` obviate the use of a credentials file
> - `RAX_REGION` defines a Rackspace Public Cloud region (DFW, ORD, LON, …)

## [Examples](rax_mon_alarm_module.md#id7)

```yaml+jinja
- name: Alarm example
  gather_facts: false
  hosts: local
  connection: local
  tasks:
  - name: Ensure that a specific alarm exists.
    community.general.rax_mon_alarm:
      credentials: ~/.rax_pub
      state: present
      label: uhoh
      entity_id: "{{ the_entity['entity']['id'] }}"
      check_id: "{{ the_check['check']['id'] }}"
      notification_plan_id: "{{ defcon1['notification_plan']['id'] }}"
      criteria: >
        if (rate(metric['average']) > 10) {
          return new AlarmStatus(WARNING);
        }
        return new AlarmStatus(OK);
    register: the_alarm
```

## [Status](rax_mon_alarm_module.md#id8)

- This module will be removed in version 9.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](rax_mon_alarm_module.md#deprecated).

### Authors

- Ash Wilson (@smashwilson)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
