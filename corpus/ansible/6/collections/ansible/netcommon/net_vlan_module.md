---
collection: ansible
version: "6"
title: "ansible.netcommon.net_vlan module – (deprecated, removed after 2022-06-01) Manage VLANs on network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/netcommon/net_vlan_module.html
fetched_at: 2026-07-27T16:44:33+00:00
---
# ansible.netcommon.net_vlan module – (deprecated, removed after 2022-06-01) Manage VLANs on network devices

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
> To use it in a playbook, specify: `ansible.netcommon.net_vlan`.

New in ansible.netcommon 1.0.0

- [DEPRECATED](net_vlan_module.md#deprecated)
- [Synopsis](net_vlan_module.md#synopsis)
- [Parameters](net_vlan_module.md#parameters)
- [Notes](net_vlan_module.md#notes)
- [Examples](net_vlan_module.md#examples)
- [Return Values](net_vlan_module.md#return-values)
- [Status](net_vlan_module.md#status)

## [DEPRECATED](net_vlan_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality

Alternative:
:   Use platform-specific “[netos]_vlans” module

## [Synopsis](net_vlan_module.md#id2)

- This module provides declarative management of VLANs on network devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](net_vlan_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aggregate**  string | List of VLANs definitions. |
| **interfaces**  string | List of interfaces the VLAN should be configured on. |
| **name**  string | Name of the VLAN. |
| **purge**  string | Purge VLANs not defined in the *aggregate* parameter.  Default: `false` |
| **state**  string | State of the VLAN configuration.  Choices:   - `"present"` ← (default) - `"absent"` - `"active"` - `"suspend"` |
| **vlan_id**  string | ID of the VLAN. |

## [Notes](net_vlan_module.md#id4)

> **Note:**
>
> - This module is supported on `ansible_network_os` network platforms. See the :ref:`Network Platform Options <platform_options>` for details.

## [Examples](net_vlan_module.md#id5)

```yaml+jinja
- name: configure VLAN ID and name
  ansible.netcommon.net_vlan:
    vlan_id: 20
    name: test-vlan

- name: remove configuration
  ansible.netcommon.net_vlan:
    state: absent

- name: configure VLAN state
  ansible.netcommon.net_vlan:
    vlan_id:
    state: suspend
```

## [Return Values](net_vlan_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always, except for the platforms that use Netconf transport to manage the device.  Sample: `["vlan 20", "name test-vlan"]` |

## [Status](net_vlan_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](net_vlan_module.md#deprecated).

### Authors

- Ricardo Carrillo Cruz (@rcarrillocruz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
