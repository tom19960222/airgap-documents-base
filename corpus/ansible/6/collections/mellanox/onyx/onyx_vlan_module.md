---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_vlan module – Manage VLANs on Mellanox ONYX network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_vlan_module.html
fetched_at: 2026-07-27T17:55:44+00:00
---
# mellanox.onyx.onyx_vlan module – Manage VLANs on Mellanox ONYX network devices

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
> To use it in a playbook, specify: `mellanox.onyx.onyx_vlan`.

- [Synopsis](onyx_vlan_module.md#synopsis)
- [Parameters](onyx_vlan_module.md#parameters)
- [Examples](onyx_vlan_module.md#examples)
- [Return Values](onyx_vlan_module.md#return-values)

## [Synopsis](onyx_vlan_module.md#id1)

- This module provides declarative management of VLANs on Mellanox ONYX network devices.

## [Parameters](onyx_vlan_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  string | List of VLANs definitions. |
| **name**  string | Name of the VLAN. |
| **purge**  boolean | Purge VLANs not defined in the *aggregate* parameter.  Choices:   - `false` ← (default) - `true` |
| **state**  string | State of the VLAN configuration.  Choices:   - `"present"` ← (default) - `"absent"` |
| **vlan_id**  string | ID of the VLAN. |

## [Examples](onyx_vlan_module.md#id3)

```yaml+jinja
- name: Configure VLAN ID and name
  onyx_vlan:
    vlan_id: 20
    name: test-vlan

- name: Remove configuration
  onyx_vlan:
    state: absent
```

## [Return Values](onyx_vlan_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always.  Sample: `["vlan 20", "name test-vlan", "exit"]` |

### Authors

- Samer Deeb (@samerd) Alex Tabachnik (@atabachnik)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
