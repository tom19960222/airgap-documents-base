---
collection: ansible
version: "6"
title: "community.general.rax_mon_notification_plan module – Create or delete a Rackspace Cloud Monitoring notification plan."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/rax_mon_notification_plan_module.html
fetched_at: 2026-07-27T17:12:32+00:00
---
# community.general.rax_mon_notification_plan module – Create or delete a Rackspace Cloud Monitoring notification plan.

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
> see [Requirements](rax_mon_notification_plan_module.md#ansible-collections-community-general-rax-mon-notification-plan-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.rax_mon_notification_plan`.

- [Synopsis](rax_mon_notification_plan_module.md#synopsis)
- [Requirements](rax_mon_notification_plan_module.md#requirements)
- [Parameters](rax_mon_notification_plan_module.md#parameters)
- [Notes](rax_mon_notification_plan_module.md#notes)
- [Examples](rax_mon_notification_plan_module.md#examples)

## [Synopsis](rax_mon_notification_plan_module.md#id1)

- Create or delete a Rackspace Cloud Monitoring notification plan by associating existing rax_mon_notifications with severity levels. Rackspace monitoring module flow | rax_mon_entity -> rax_mon_check -> rax_mon_notification -> \*rax_mon_notification_plan\* -> rax_mon_alarm

## [Requirements](rax_mon_notification_plan_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- pyrax

## [Parameters](rax_mon_notification_plan_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  aliases: password  string | Rackspace API key, overrides *credentials*. |
| **auth_endpoint**  string | The URI of the authentication service.  If not specified will be set to <https://identity.api.rackspacecloud.com/v2.0/> |
| **credentials**  aliases: creds_file  path | File to find the Rackspace credentials in. Ignored if *api_key* and *username* are provided. |
| **critical_state**  list / elements=string | Notification list to use when the alarm state is CRITICAL. Must be an array of valid rax_mon_notification ids. |
| **env**  string | Environment as configured in *~/.pyrax.cfg*, see <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration>. |
| **identity_type**  string | Authentication mechanism to use, such as rackspace or keystone.  Default: `"rackspace"` |
| **label**  string / required | Defines a friendly name for this notification plan. String between 1 and 255 characters long. |
| **ok_state**  list / elements=string | Notification list to use when the alarm state is OK. Must be an array of valid rax_mon_notification ids. |
| **region**  string | Region to create an instance in. |
| **state**  string | Ensure that the notification plan with this `label` exists or does not exist.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tenant_id**  string | The tenant ID used for authentication. |
| **tenant_name**  string | The tenant name used for authentication. |
| **username**  string | Rackspace username, overrides *credentials*. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to require SSL validation of API endpoints.  Choices:   - `false` - `true` |
| **warning_state**  list / elements=string | Notification list to use when the alarm state is WARNING. Must be an array of valid rax_mon_notification ids. |

## [Notes](rax_mon_notification_plan_module.md#id4)

> **Note:**
>
> - The following environment variables can be used, `RAX_USERNAME`, `RAX_API_KEY`, `RAX_CREDS_FILE`, `RAX_CREDENTIALS`, `RAX_REGION`.
> - `RAX_CREDENTIALS` and `RAX_CREDS_FILE` points to a credentials file appropriate for pyrax. See <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#authenticating>
> - `RAX_USERNAME` and `RAX_API_KEY` obviate the use of a credentials file
> - `RAX_REGION` defines a Rackspace Public Cloud region (DFW, ORD, LON, …)

## [Examples](rax_mon_notification_plan_module.md#id5)

```yaml+jinja
- name: Example notification plan
  gather_facts: false
  hosts: local
  connection: local
  tasks:
  - name: Establish who gets called when.
    community.general.rax_mon_notification_plan:
      credentials: ~/.rax_pub
      state: present
      label: defcon1
      critical_state:
      - "{{ everyone['notification']['id'] }}"
      warning_state:
      - "{{ opsfloor['notification']['id'] }}"
    register: defcon1
```

### Authors

- Ash Wilson (@smashwilson)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
