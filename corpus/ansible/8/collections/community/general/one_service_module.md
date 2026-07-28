---
collection: ansible
version: "8"
title: "community.general.one_service module – Deploy and manage OpenNebula services"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/one_service_module.html
fetched_at: 2026-07-28T01:48:21+00:00
---
# community.general.one_service module – Deploy and manage OpenNebula services

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.one_service`.

- [Synopsis](one_service_module.md#synopsis)
- [Parameters](one_service_module.md#parameters)
- [Attributes](one_service_module.md#attributes)
- [Examples](one_service_module.md#examples)
- [Return Values](one_service_module.md#return-values)

## [Synopsis](one_service_module.md#id1)

- Manage OpenNebula services

Aliases: cloud.opennebula.one_service

## [Parameters](one_service_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string | Password of the user to login into OpenNebula OneFlow API server. If not set then the value of the `ONEFLOW_PASSWORD` environment variable is used. |
| **api_url**  string | URL of the OpenNebula OneFlow API server.  It is recommended to use HTTPS so that the username/password are not transferred over the network unencrypted.  If not set then the value of the `ONEFLOW_URL` environment variable is used. |
| **api_username**  string | Name of the user to login into the OpenNebula OneFlow API server. If not set then the value of the `ONEFLOW_USERNAME` environment variable is used. |
| **cardinality**  integer | Number of VMs for the specified role. |
| **custom_attrs**  dictionary | Dictionary of key/value custom attributes which will be used when instantiating a new service.  **Default:** `{}` |
| **force**  boolean | Force the new cardinality even if it is outside the limits.  **Choices:**   - `false` ← (default) - `true` |
| **group_id**  integer | ID of the group which will be set as the group of the service. |
| **mode**  string | Set permission mode of a service instance in octet format, for example `0600` to give owner `use` and `manage` and nothing to group and others. |
| **owner_id**  integer | ID of the user which will be set as the owner of the service. |
| **role**  string | Name of the role whose cardinality should be changed. |
| **service_id**  integer | ID of a service instance that you would like to manage. |
| **service_name**  string | Name of a service instance that you would like to manage. |
| **state**  string | `present` - instantiate a service from a template specified with `template_id` or `template_name`.  `absent` - terminate an instance of a service specified with `template_id` or `template_name`.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **template_id**  integer | ID of a service template to use to create a new instance of a service. |
| **template_name**  string | Name of service template to use to create a new instance of a service. |
| **unique**  boolean | Setting `unique=true` will make sure that there is only one service instance running with a name set with `service_name` when instantiating a service from a template specified with `template_id` or `template_name`. Check examples below.  **Choices:**   - `false` ← (default) - `true` |
| **wait**  boolean | Wait for the instance to reach RUNNING state after DEPLOYING or COOLDOWN state after SCALING.  **Choices:**   - `false` ← (default) - `true` |
| **wait_timeout**  integer | How long before wait gives up, in seconds.  **Default:** `300` |

## [Attributes](one_service_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](one_service_module.md#id4)

```yaml+jinja
- name: Instantiate a new service
  community.general.one_service:
    template_id: 90
  register: result

- name: Print service properties
  ansible.builtin.debug:
    msg: result

- name: Instantiate a new service with specified service_name, service group and mode
  community.general.one_service:
    template_name: 'app1_template'
    service_name: 'app1'
    group_id: 1
    mode: '660'

- name: Instantiate a new service with template_id and pass custom_attrs dict
  community.general.one_service:
    template_id: 90
    custom_attrs:
      public_network_id: 21
      private_network_id: 26

- name: Instantiate a new service 'foo' if the service doesn't already exist, otherwise do nothing
  community.general.one_service:
    template_id: 53
    service_name: 'foo'
    unique: true

- name: Delete a service by ID
  community.general.one_service:
    service_id: 153
    state: absent

- name: Get service info
  community.general.one_service:
    service_id: 153
  register: service_info

- name: Change service owner, group and mode
  community.general.one_service:
    service_name: 'app2'
    owner_id: 34
    group_id: 113
    mode: '600'

- name: Instantiate service and wait for it to become RUNNING
  community.general.one_service:
    template_id: 43
    service_name: 'foo1'

- name: Wait service to become RUNNING
  community.general.one_service:
    service_id: 112
    wait: true

- name: Change role cardinality
  community.general.one_service:
    service_id: 153
    role: bar
    cardinality: 5

- name: Change role cardinality and wait for it to be applied
  community.general.one_service:
    service_id: 112
    role: foo
    cardinality: 7
    wait: true
```

## [Return Values](one_service_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **group_id**  integer | service’s group id  **Returned:** success  **Sample:** `1` |
| **group_name**  string | service’s group name  **Returned:** success  **Sample:** `"one-users"` |
| **mode**  integer | service’s mode  **Returned:** success  **Sample:** `660` |
| **owner_id**  integer | service’s owner id  **Returned:** success  **Sample:** `143` |
| **owner_name**  string | service’s owner name  **Returned:** success  **Sample:** `"ansible-test"` |
| **roles**  list / elements=string | list of dictionaries of roles, each role is described by name, cardinality, state and nodes ids  **Returned:** success  **Sample:** `[{"cardinality": 1, "ids": [123, 456], "name": "foo", "state": "RUNNING"}, {"cardinality": 2, "ids": [452, 567, 746], "name": "bar", "state": "RUNNING"}]` |
| **service_id**  integer | service id  **Returned:** success  **Sample:** `153` |
| **service_name**  string | service name  **Returned:** success  **Sample:** `"app1"` |
| **state**  string | state of service instance  **Returned:** success  **Sample:** `"RUNNING"` |

### Authors

- Milan Ilic (@ilicmilan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
