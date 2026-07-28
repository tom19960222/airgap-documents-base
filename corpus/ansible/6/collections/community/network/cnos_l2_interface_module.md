---
collection: ansible
version: "6"
title: "community.network.cnos_l2_interface module – Manage Layer-2 interface on Lenovo CNOS devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/cnos_l2_interface_module.html
fetched_at: 2026-07-27T17:18:10+00:00
---
# community.network.cnos_l2_interface module – Manage Layer-2 interface on Lenovo CNOS devices.

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
> To use it in a playbook, specify: `community.network.cnos_l2_interface`.

- [Synopsis](cnos_l2_interface_module.md#synopsis)
- [Parameters](cnos_l2_interface_module.md#parameters)
- [Examples](cnos_l2_interface_module.md#examples)
- [Return Values](cnos_l2_interface_module.md#return-values)

## [Synopsis](cnos_l2_interface_module.md#id1)

- This module provides declarative management of Layer-2 interfaces on Lenovo CNOS devices.

## [Parameters](cnos_l2_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_vlan**  string | Configure given VLAN in access port. If `mode=access`, used as the access VLAN ID. |
| **aggregate**  string | List of Layer-2 interface definitions. |
| **mode**  string | Mode in which interface needs to be configured.  Choices:   - `"access"` ← (default) - `"trunk"` |
| **name**  aliases: interface  string / required | Full name of the interface excluding any logical unit number, i.e. Ethernet1/3. |
| **native_vlan**  string | Native VLAN to be configured in trunk port. If `mode=trunk`, used as the trunk native VLAN ID. |
| **state**  string | Manage the state of the Layer-2 Interface configuration.  Choices:   - `"present"` ← (default) - `"absent"` - `"unconfigured"` |
| **trunk_allowed_vlans**  string | List of allowed VLANs in a given trunk port. If `mode=trunk`, these are the only VLANs that will be configured on the trunk, i.e. “2-10,15”. |
| **trunk_vlans**  string | List of VLANs to be configured in trunk port. If `mode=trunk`, used as the VLAN range to ADD or REMOVE from the trunk. |

## [Examples](cnos_l2_interface_module.md#id3)

```yaml+jinja
- name: Ensure Ethernet1/5 is in its default l2 interface state
  community.network.cnos_l2_interface:
    name: Ethernet1/5
    state: unconfigured

- name: Ensure Ethernet1/5 is configured for access vlan 20
  community.network.cnos_l2_interface:
    name: Ethernet1/5
    mode: access
    access_vlan: 20

- name: Ensure Ethernet1/5 only has vlans 5-10 as trunk vlans
  community.network.cnos_l2_interface:
    name: Ethernet1/5
    mode: trunk
    native_vlan: 10
    trunk_vlans: 5-10

- name: Ensure Ethernet1/5 is a trunk port and ensure 2-50 are being tagged
        (doesn't mean others aren't also being tagged)
  community.network.cnos_l2_interface:
    name: Ethernet1/5
    mode: trunk
    native_vlan: 10
    trunk_vlans: 2-50

- name: Ensure these VLANs are not being tagged on the trunk
  community.network.cnos_l2_interface:
    name: Ethernet1/5
    mode: trunk
    trunk_vlans: 51-4094
    state: absent
```

## [Return Values](cnos_l2_interface_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always, except for the platforms that use Netconf transport to manage the device.  Sample: `["interface Ethernet1/5", "switchport access vlan 20"]` |

### Authors

- Anil Kumar Muraleedharan (@amuraleedhar)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
