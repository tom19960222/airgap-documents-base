---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_mlag_ipl module – Manage IPL (inter-peer link) on Mellanox ONYX network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_mlag_ipl_module.html
fetched_at: 2026-07-27T17:55:33+00:00
---
# mellanox.onyx.onyx_mlag_ipl module – Manage IPL (inter-peer link) on Mellanox ONYX network devices

> **Note:**
>
> This module is part of the [mellanox.onyx collection](https://galaxy.ansible.com/mellanox/onyx) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install mellanox.onyx`.
>
> To use it in a playbook, specify: `mellanox.onyx.onyx_mlag_ipl`.

- [Synopsis](onyx_mlag_ipl_module.md#synopsis)
- [Parameters](onyx_mlag_ipl_module.md#parameters)
- [Notes](onyx_mlag_ipl_module.md#notes)
- [Examples](onyx_mlag_ipl_module.md#examples)
- [Return Values](onyx_mlag_ipl_module.md#return-values)

## [Synopsis](onyx_mlag_ipl_module.md#id1)

- This module provides declarative management of IPL (inter-peer link) management on Mellanox ONYX network devices.

## [Parameters](onyx_mlag_ipl_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | Name of the interface (port-channel) IPL should be configured on. |
| **peer_address**  string | IPL peer IP address. |
| **state**  string | IPL state.  Choices:   - `"present"` ← (default) - `"absent"` |
| **vlan_interface**  string | Name of the IPL vlan interface. |

## [Notes](onyx_mlag_ipl_module.md#id3)

> **Note:**
>
> - Tested on ONYX 3.6.4000

## [Examples](onyx_mlag_ipl_module.md#id4)

```yaml+jinja
- name: Run configure ipl
  onyx_mlag_ipl:
    name: Po1
    vlan_interface: Vlan 322
    state: present
    peer_address: 192.168.7.1

- name: Run remove ipl
  onyx_mlag_ipl:
    name: Po1
    state: absent
```

## [Return Values](onyx_mlag_ipl_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["interface port-channel 1 ipl 1", "interface vlan 1024 ipl 1 peer-address 10.10.10.10"]` |

### Authors

- Samer Deeb (@samerd)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
