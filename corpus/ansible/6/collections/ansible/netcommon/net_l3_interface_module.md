---
collection: ansible
version: "6"
title: "ansible.netcommon.net_l3_interface module – (deprecated, removed after 2022-06-01) Manage L3 interfaces on network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/netcommon/net_l3_interface_module.html
fetched_at: 2026-07-27T16:44:29+00:00
---
# ansible.netcommon.net_l3_interface module – (deprecated, removed after 2022-06-01) Manage L3 interfaces on network devices

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
> To use it in a playbook, specify: `ansible.netcommon.net_l3_interface`.

New in ansible.netcommon 1.0.0

- [DEPRECATED](net_l3_interface_module.md#deprecated)
- [Synopsis](net_l3_interface_module.md#synopsis)
- [Parameters](net_l3_interface_module.md#parameters)
- [Notes](net_l3_interface_module.md#notes)
- [Examples](net_l3_interface_module.md#examples)
- [Return Values](net_l3_interface_module.md#return-values)
- [Status](net_l3_interface_module.md#status)

## [DEPRECATED](net_l3_interface_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality

Alternative:
:   Use platform-specific “[netos]_l3_interfaces” module

## [Synopsis](net_l3_interface_module.md#id2)

- This module provides declarative management of L3 interfaces on network devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](net_l3_interface_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aggregate**  string | List of L3 interfaces definitions |
| **ipv4**  string | IPv4 of the L3 interface. |
| **ipv6**  string | IPv6 of the L3 interface. |
| **name**  string | Name of the L3 interface. |
| **purge**  string | Purge L3 interfaces not defined in the *aggregate* parameter.  Default: `false` |
| **state**  string | State of the L3 interface configuration.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](net_l3_interface_module.md#id4)

> **Note:**
>
> - This module is supported on `ansible_network_os` network platforms. See the :ref:`Network Platform Options <platform_options>` for details.

## [Examples](net_l3_interface_module.md#id5)

```yaml+jinja
- name: Set eth0 IPv4 address
  ansible.netcommon.net_l3_interface:
    name: eth0
    ipv4: 192.168.0.1/24

- name: Remove eth0 IPv4 address
  ansible.netcommon.net_l3_interface:
    name: eth0
    state: absent

- name: Set IP addresses on aggregate
  ansible.netcommon.net_l3_interface:
    aggregate:
    - name: eth1
      ipv4: 192.168.2.10/24
    - name: eth2
      ipv4: 192.168.3.10/24
      ipv6: fd5d:12c9:2201:1::1/64

- name: Remove IP addresses on aggregate
  ansible.netcommon.net_l3_interface:
    aggregate:
    - name: eth1
      ipv4: 192.168.2.10/24
    - name: eth2
      ipv4: 192.168.3.10/24
      ipv6: fd5d:12c9:2201:1::1/64
    state: absent
```

## [Return Values](net_l3_interface_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always, except for the platforms that use Netconf transport to manage the device.  Sample: `["set interfaces ethernet eth0 address '192.168.0.1/24'"]` |

## [Status](net_l3_interface_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](net_l3_interface_module.md#deprecated).

### Authors

- Ricardo Carrillo Cruz (@rcarrillocruz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
