---
collection: ansible
version: "6"
title: "community.network.slxos_linkagg module – Manage link aggregation groups on Extreme Networks SLX-OS network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/slxos_linkagg_module.html
fetched_at: 2026-07-27T17:19:45+00:00
---
# community.network.slxos_linkagg module – Manage link aggregation groups on Extreme Networks SLX-OS network devices

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.slxos_linkagg`.

- [Synopsis](slxos_linkagg_module.md#synopsis)
- [Parameters](slxos_linkagg_module.md#parameters)
- [Notes](slxos_linkagg_module.md#notes)
- [Examples](slxos_linkagg_module.md#examples)
- [Return Values](slxos_linkagg_module.md#return-values)

## [Synopsis](slxos_linkagg_module.md#id1)

- This module provides declarative management of link aggregation groups on Extreme Networks SLX-OS network devices.

## [Parameters](slxos_linkagg_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  string | List of link aggregation definitions. |
| **group**  string | Channel-group number for the port-channel Link aggregation group. Range 1-1024. |
| **members**  string | List of members of the link aggregation group. |
| **mode**  string | Mode of the link aggregation group.  Choices:   - `"active"` - `"on"` - `"passive"` |
| **purge**  boolean | Purge links not defined in the *aggregate* parameter.  Choices:   - `false` ← (default) - `true` |
| **state**  string | State of the link aggregation group.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](slxos_linkagg_module.md#id3)

> **Note:**
>
> - Tested against SLX-OS 17s.1.02

## [Examples](slxos_linkagg_module.md#id4)

```yaml+jinja
- name: Create link aggregation group
  community.network.slxos_linkagg:
    group: 10
    state: present

- name: Delete link aggregation group
  community.network.slxos_linkagg:
    group: 10
    state: absent

- name: Set link aggregation group to members
  community.network.slxos_linkagg:
    group: 200
    mode: active
    members:
      - Ethernet 0/1
      - Ethernet 0/2

- name: Remove link aggregation group from Ethernet 0/1
  community.network.slxos_linkagg:
    group: 200
    mode: active
    members:
      - Ethernet 0/1

- name: Create aggregate of linkagg definitions
  community.network.slxos_linkagg:
    aggregate:
      - { group: 3, mode: on, members: [Ethernet 0/1] }
      - { group: 100, mode: passive, members: [Ethernet 0/2] }
```

## [Return Values](slxos_linkagg_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always, except for the platforms that use Netconf transport to manage the device.  Sample: `["interface port-channel 30", "interface Ethernet 0/3", "channel-group 30 mode on", "no interface port-channel 30"]` |

### Authors

- Matthew Stone (@bigmstone)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
