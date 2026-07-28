---
collection: ansible
version: "8"
title: "vyos.vyos.vyos_vlan module – Manage VLANs on VyOS network devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vyos/vyos/vyos_vlan_module.html
fetched_at: 2026-07-28T02:59:28+00:00
---
# vyos.vyos.vyos_vlan module – Manage VLANs on VyOS network devices

> **Note:**
>
> This module is part of the [vyos.vyos collection](https://galaxy.ansible.com/ui/repo/published/vyos/vyos/) (version 4.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vyos.vyos`.
>
> To use it in a playbook, specify: `vyos.vyos.vyos_vlan`.

New in vyos.vyos 1.0.0

- [Synopsis](vyos_vlan_module.md#synopsis)
- [Parameters](vyos_vlan_module.md#parameters)
- [Notes](vyos_vlan_module.md#notes)
- [Examples](vyos_vlan_module.md#examples)
- [Return Values](vyos_vlan_module.md#return-values)

## [Synopsis](vyos_vlan_module.md#id1)

- This module provides declarative management of VLANs on VyOS network devices.

Aliases: vlan

## [Parameters](vyos_vlan_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  string | Configure Virtual interface address. |
| **aggregate**  list / elements=dictionary | List of VLANs definitions. |
| **address**  string | Configure Virtual interface address. |
| **associated_interfaces**  list / elements=string | This is a intent option and checks the operational state of the for given vlan `name` for associated interfaces. If the value in the `associated_interfaces` does not match with the operational state of vlan on device it will result in failure. |
| **delay**  integer | Delay the play should wait to check for declarative intent params values. |
| **interfaces**  list / elements=string / required | List of interfaces that should be associated to the VLAN. |
| **name**  string | Name of the VLAN. |
| **state**  string | State of the VLAN configuration.  **Choices:**   - `"present"` - `"absent"` |
| **vlan_id**  integer / required | ID of the VLAN. Range 0-4094. |
| **associated_interfaces**  list / elements=string | This is a intent option and checks the operational state of the for given vlan `name` for associated interfaces. If the value in the `associated_interfaces` does not match with the operational state of vlan on device it will result in failure. |
| **delay**  integer | Delay the play should wait to check for declarative intent params values.  **Default:** `10` |
| **interfaces**  list / elements=string | List of interfaces that should be associated to the VLAN. |
| **name**  string | Name of the VLAN. |
| **purge**  boolean | Purge VLANs not defined in the *aggregate* parameter.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | State of the VLAN configuration.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vlan_id**  integer | ID of the VLAN. Range 0-4094. |

## [Notes](vyos_vlan_module.md#id3)

> **Note:**
>
> - Tested against VyOS 1.1.8 (helium).
> - This module works with connection `ansible.netcommon.network_cli`. See [the VyOS OS Platform Options](../network/user_guide/platform_vyos.md).
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`

## [Examples](vyos_vlan_module.md#id4)

```yaml+jinja
- name: Create vlan
  vyos.vyos.vyos_vlan:
    vlan_id: 100
    name: vlan-100
    interfaces: eth1
    state: present

- name: Add interfaces to VLAN
  vyos.vyos.vyos_vlan:
    vlan_id: 100
    interfaces:
    - eth1
    - eth2

- name: Configure virtual interface address
  vyos.vyos.vyos_vlan:
    vlan_id: 100
    interfaces: eth1
    address: 172.26.100.37/24

- name: vlan interface config + intent
  vyos.vyos.vyos_vlan:
    vlan_id: 100
    interfaces: eth0
    associated_interfaces:
    - eth0

- name: vlan intent check
  vyos.vyos.vyos_vlan:
    vlan_id: 100
    associated_interfaces:
    - eth3
    - eth4

- name: Delete vlan
  vyos.vyos.vyos_vlan:
    vlan_id: 100
    interfaces: eth1
    state: absent
```

## [Return Values](vyos_vlan_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["set interfaces ethernet eth1 vif 100 description VLAN 100", "set interfaces ethernet eth1 vif 100 address 172.26.100.37/24", "delete interfaces ethernet eth1 vif 100"]` |

### Authors

- Trishna Guha (@trishnaguha)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
