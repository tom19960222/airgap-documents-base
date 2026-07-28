---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_l2_interface module – Manage Layer-2 interface on Mellanox ONYX network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_l2_interface_module.html
fetched_at: 2026-07-27T17:55:29+00:00
---
# mellanox.onyx.onyx_l2_interface module – Manage Layer-2 interface on Mellanox ONYX network devices

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
> To use it in a playbook, specify: `mellanox.onyx.onyx_l2_interface`.

- [Synopsis](onyx_l2_interface_module.md#synopsis)
- [Parameters](onyx_l2_interface_module.md#parameters)
- [Examples](onyx_l2_interface_module.md#examples)
- [Return Values](onyx_l2_interface_module.md#return-values)

## [Synopsis](onyx_l2_interface_module.md#id1)

- This module provides declarative management of Layer-2 interface on Mellanox ONYX network devices.

## [Parameters](onyx_l2_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_vlan**  string | Configure given VLAN in access port. |
| **aggregate**  string | List of Layer-2 interface definitions. |
| **mode**  string | Mode in which interface needs to be configured.  Choices:   - `"access"` ← (default) - `"trunk"` - `"hybrid"` |
| **name**  string | Name of the interface. |
| **state**  string | State of the Layer-2 Interface configuration.  Choices:   - `"present"` ← (default) - `"absent"` |
| **trunk_allowed_vlans**  string | List of allowed VLANs in a given trunk port. |

## [Examples](onyx_l2_interface_module.md#id3)

```yaml+jinja
- name: Configure Layer-2 interface
  onyx_l2_interface:
    name: Eth1/1
    mode: access
    access_vlan: 30
- name: Remove Layer-2 interface configuration
  onyx_l2_interface:
    name: Eth1/1
    state: absent
```

## [Return Values](onyx_l2_interface_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always.  Sample: `["interface ethernet 1/1", "switchport mode access", "switchport access vlan 30"]` |

### Authors

- Samer Deeb (@samerd)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
