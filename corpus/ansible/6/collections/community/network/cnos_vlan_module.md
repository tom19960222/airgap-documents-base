---
collection: ansible
version: "6"
title: "community.network.cnos_vlan module – Manage VLANs on CNOS network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/cnos_vlan_module.html
fetched_at: 2026-07-27T17:18:20+00:00
---
# community.network.cnos_vlan module – Manage VLANs on CNOS network devices

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
> To use it in a playbook, specify: `community.network.cnos_vlan`.

- [Synopsis](cnos_vlan_module.md#synopsis)
- [Parameters](cnos_vlan_module.md#parameters)
- [Notes](cnos_vlan_module.md#notes)
- [Examples](cnos_vlan_module.md#examples)
- [Return Values](cnos_vlan_module.md#return-values)

## [Synopsis](cnos_vlan_module.md#id1)

- This module provides declarative management of VLANs on Lenovo CNOS network devices.

## [Parameters](cnos_vlan_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  string | List of VLANs definitions. |
| **associated_interfaces**  string | This is a intent option and checks the operational state of the for given vlan `name` for associated interfaces. If the value in the `associated_interfaces` does not match with the operational state of vlan interfaces on device it will result in failure. |
| **delay**  string | Delay the play should wait to check for declarative intent params values.  Default: `10` |
| **interfaces**  string / required | List of interfaces that should be associated to the VLAN. |
| **name**  string | Name of the VLAN. |
| **purge**  boolean | Purge VLANs not defined in the *aggregate* parameter.  Choices:   - `false` ← (default) - `true` |
| **state**  string | State of the VLAN configuration.  Choices:   - `"present"` ← (default) - `"absent"` - `"active"` - `"suspend"` |
| **vlan_id**  string / required | ID of the VLAN. Range 1-4094. |

## [Notes](cnos_vlan_module.md#id3)

> **Note:**
>
> - Tested against CNOS 10.8.1

## [Examples](cnos_vlan_module.md#id4)

```yaml+jinja
- name: Create vlan
  community.network.cnos_vlan:
    vlan_id: 100
    name: test-vlan
    state: present

- name: Add interfaces to VLAN
  community.network.cnos_vlan:
    vlan_id: 100
    interfaces:
      - Ethernet1/33
      - Ethernet1/44

- name: Check if interfaces is assigned to VLAN
  community.network.cnos_vlan:
    vlan_id: 100
    associated_interfaces:
      - Ethernet1/33
      - Ethernet1/44

- name: Delete vlan
  community.network.cnos_vlan:
    vlan_id: 100
    state: absent
```

## [Return Values](cnos_vlan_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always  Sample: `["vlan 100", "name test-vlan"]` |

### Authors

- Anil Kumar Mureleedharan(@amuraleedhar)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
