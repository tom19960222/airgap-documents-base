---
collection: ansible
version: "6"
title: "ansible.netcommon.net_linkagg module – (deprecated, removed after 2022-06-01) Manage link aggregation groups on network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/netcommon/net_linkagg_module.html
fetched_at: 2026-07-27T16:44:30+00:00
---
# ansible.netcommon.net_linkagg module – (deprecated, removed after 2022-06-01) Manage link aggregation groups on network devices

> **Note:**
>
> This module is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ansible/netcommon) (version 3.1.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.net_linkagg`.

New in ansible.netcommon 1.0.0

- [DEPRECATED](net_linkagg_module.md#deprecated)
- [Synopsis](net_linkagg_module.md#synopsis)
- [Parameters](net_linkagg_module.md#parameters)
- [Notes](net_linkagg_module.md#notes)
- [Examples](net_linkagg_module.md#examples)
- [Return Values](net_linkagg_module.md#return-values)
- [Status](net_linkagg_module.md#status)

## [DEPRECATED](net_linkagg_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality

Alternative:
:   Use platform-specific “[netos]_lag_interfaces” module

## [Synopsis](net_linkagg_module.md#id2)

- This module provides declarative management of link aggregation groups on network devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](net_linkagg_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aggregate**  string | List of link aggregation definitions. |
| **members**  string / required | List of members interfaces of the link aggregation group. The value can be single interface or list of interfaces. |
| **min_links**  string | Minimum members that should be up before bringing up the link aggregation group. |
| **mode**  string | Mode of the link aggregation group. A value of `on` will enable LACP. `active` configures the link to actively information about the state of the link, or it can be configured in `passive` mode ie. send link state information only when received them from another link.  Choices:   - `true` ← (default) - `"active"` - `"passive"` |
| **name**  string / required | Name of the link aggregation group. |
| **purge**  string | Purge link aggregation groups not defined in the *aggregate* parameter.  Default: `false` |
| **state**  string | State of the link aggregation group.  Choices:   - `"present"` ← (default) - `"absent"` - `"up"` - `"down"` |

## [Notes](net_linkagg_module.md#id4)

> **Note:**
>
> - This module is supported on `ansible_network_os` network platforms. See the :ref:`Network Platform Options <platform_options>` for details.

## [Examples](net_linkagg_module.md#id5)

```yaml+jinja
- name: configure link aggregation group
  ansible.netcommon.net_linkagg:
    name: bond0
    members:
    - eth0
    - eth1

- name: remove configuration
  ansible.netcommon.net_linkagg:
    name: bond0
    state: absent

- name: Create aggregate of linkagg definitions
  ansible.netcommon.net_linkagg:
    aggregate:
    - {name: bond0, members: [eth1]}
    - {name: bond1, members: [eth2]}

- name: Remove aggregate of linkagg definitions
  ansible.netcommon.net_linkagg:
    aggregate:
    - name: bond0
    - name: bond1
    state: absent
```

## [Return Values](net_linkagg_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always, except for the platforms that use Netconf transport to manage the device.  Sample: `["set interfaces bonding bond0", "set interfaces ethernet eth0 bond-group 'bond0'", "set interfaces ethernet eth1 bond-group 'bond0'"]` |

## [Status](net_linkagg_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](net_linkagg_module.md#deprecated).

### Authors

- Ricardo Carrillo Cruz (@rcarrillocruz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
