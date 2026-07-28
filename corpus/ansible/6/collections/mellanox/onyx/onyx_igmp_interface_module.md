---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_igmp_interface module – Configures IGMP interface parameters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_igmp_interface_module.html
fetched_at: 2026-07-27T17:55:27+00:00
---
# mellanox.onyx.onyx_igmp_interface module – Configures IGMP interface parameters

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
> To use it in a playbook, specify: `mellanox.onyx.onyx_igmp_interface`.

- [Synopsis](onyx_igmp_interface_module.md#synopsis)
- [Parameters](onyx_igmp_interface_module.md#parameters)
- [Notes](onyx_igmp_interface_module.md#notes)
- [Examples](onyx_igmp_interface_module.md#examples)
- [Return Values](onyx_igmp_interface_module.md#return-values)

## [Synopsis](onyx_igmp_interface_module.md#id1)

- This module provides declarative management of IGMP interface configuration on Mellanox ONYX network devices.

## [Parameters](onyx_igmp_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | interface name that we want to configure IGMP on it |
| **state**  string | IGMP Interface state.  Choices:   - `"enabled"` ← (default) - `"disabled"` |

## [Notes](onyx_igmp_interface_module.md#id3)

> **Note:**
>
> - Tested on ONYX 3.6.8130

## [Examples](onyx_igmp_interface_module.md#id4)

```yaml+jinja
- name: Configure igmp interface
  onyx_igmp_interface:
    state: enabled
    name: Eth1/1
```

## [Return Values](onyx_igmp_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["interface ethernet 1/1 ip igmp snooping fast-leave"]` |

### Authors

- Anas Badaha (@anasb)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
