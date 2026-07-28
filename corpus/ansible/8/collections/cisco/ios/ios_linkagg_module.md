---
collection: ansible
version: "8"
title: "cisco.ios.ios_linkagg module – Module to configure link aggregation groups."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ios/ios_linkagg_module.html
fetched_at: 2026-07-28T01:26:14+00:00
---
# cisco.ios.ios_linkagg module – Module to configure link aggregation groups.

> **Note:**
>
> This module is part of the [cisco.ios collection](https://galaxy.ansible.com/ui/repo/published/cisco/ios/) (version 4.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ios`.
>
> To use it in a playbook, specify: `cisco.ios.ios_linkagg`.

New in cisco.ios 1.0.0

- [DEPRECATED](ios_linkagg_module.md#deprecated)
- [Synopsis](ios_linkagg_module.md#synopsis)
- [Parameters](ios_linkagg_module.md#parameters)
- [Notes](ios_linkagg_module.md#notes)
- [Examples](ios_linkagg_module.md#examples)
- [Return Values](ios_linkagg_module.md#return-values)
- [Status](ios_linkagg_module.md#status)

## [DEPRECATED](ios_linkagg_module.md#id1)

Removed in:
:   major release after 2024-06-01

Why:
:   Updated modules released with more functionality.

Alternative:
:   ios_lag_interfaces

## [Synopsis](ios_linkagg_module.md#id2)

- This module provides declarative management of link aggregation groups on Cisco IOS network devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: linkagg

## [Parameters](ios_linkagg_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aggregate**  list / elements=dictionary | List of link aggregation definitions. |
| **group**  string / required | Channel-group number for the port-channel Link aggregation group. Range 1-255. |
| **members**  list / elements=string | List of members of the link aggregation group. |
| **mode**  string | Mode of the link aggregation group.  On mode has to be quoted as ‘on’ or else pyyaml will convert to True before it gets to Ansible.  **Choices:**   - `"active"` - `"on"` - `"passive"` - `"auto"` - `"desirable"` |
| **state**  string | State of the link aggregation group.  **Choices:**   - `"present"` - `"absent"` |
| **group**  integer | Channel-group number for the port-channel Link aggregation group. Range 1-255. |
| **members**  list / elements=string | List of members of the link aggregation group. |
| **mode**  string | Mode of the link aggregation group.  On mode has to be quoted as ‘on’ or else pyyaml will convert to True before it gets to Ansible.  **Choices:**   - `"active"` - `"on"` - `"passive"` - `"auto"` - `"desirable"` |
| **purge**  boolean | Purge links not defined in the *aggregate* parameter.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | State of the link aggregation group.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](ios_linkagg_module.md#id4)

> **Note:**
>
> - Tested against IOS 15.2
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](ios_linkagg_module.md#id5)

```yaml+jinja
- name: Create link aggregation group
  cisco.ios.ios_linkagg:
    group: 10
    state: present

- name: Delete link aggregation group
  cisco.ios.ios_linkagg:
    group: 10
    state: absent

- name: Set link aggregation group to members
  cisco.ios.ios_linkagg:
    group: 200
    mode: active
    members:
      - GigabitEthernet0/0
      - GigabitEthernet0/1

- name: Remove link aggregation group from GigabitEthernet0/0
  cisco.ios.ios_linkagg:
    group: 200
    mode: active
    members:
      - GigabitEthernet0/1

- name: Create aggregate of linkagg definitions
  cisco.ios.ios_linkagg:
    aggregate:
      - { group: 3, mode: on, members: [GigabitEthernet0/1] }
      - { group: 100, mode: passive, members: [GigabitEthernet0/2] }
```

## [Return Values](ios_linkagg_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always, except for the platforms that use Netconf transport to manage the device.  **Sample:** `["interface port-channel 30", "interface GigabitEthernet0/3", "channel-group 30 mode on", "no interface port-channel 30"]` |

## [Status](ios_linkagg_module.md#id7)

- This module will be removed in a major release after 2024-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](ios_linkagg_module.md#deprecated).

### Authors

- Trishna Guha (@trishnaguha)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
