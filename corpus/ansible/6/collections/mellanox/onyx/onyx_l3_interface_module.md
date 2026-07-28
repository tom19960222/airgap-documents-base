---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_l3_interface module – Manage L3 interfaces on Mellanox ONYX network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_l3_interface_module.html
fetched_at: 2026-07-27T17:55:30+00:00
---
# mellanox.onyx.onyx_l3_interface module – Manage L3 interfaces on Mellanox ONYX network devices

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
> To use it in a playbook, specify: `mellanox.onyx.onyx_l3_interface`.

- [Synopsis](onyx_l3_interface_module.md#synopsis)
- [Parameters](onyx_l3_interface_module.md#parameters)
- [Examples](onyx_l3_interface_module.md#examples)
- [Return Values](onyx_l3_interface_module.md#return-values)

## [Synopsis](onyx_l3_interface_module.md#id1)

- This module provides declarative management of L3 interfaces on Mellanox ONYX network devices.

## [Parameters](onyx_l3_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  string | List of L3 interfaces definitions |
| **ipv4**  string | IPv4 of the L3 interface. |
| **ipv6**  string | IPv6 of the L3 interface (not supported for now). |
| **name**  string | Name of the L3 interface. |
| **purge**  boolean | Purge L3 interfaces not defined in the *aggregate* parameter.  Choices:   - `false` ← (default) - `true` |
| **state**  string | State of the L3 interface configuration.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Examples](onyx_l3_interface_module.md#id3)

```yaml+jinja
- name: Set Eth1/1 IPv4 address
  onyx_l3_interface:
    name: Eth1/1
    ipv4: 192.168.0.1/24

- name: Remove Eth1/1 IPv4 address
  onyx_l3_interface:
    name: Eth1/1
    state: absent

- name: Set IP addresses on aggregate
  onyx_l3_interface:
    aggregate:
      - { name: Eth1/1, ipv4: 192.168.2.10/24 }
      - { name: Eth1/2, ipv4: 192.168.3.10/24 }

- name: Remove IP addresses on aggregate
  onyx_l3_interface:
    aggregate:
      - { name: Eth1/1, ipv4: 192.168.2.10/24 }
      - { name: Eth1/2, ipv4: 192.168.3.10/24 }
    state: absent
```

## [Return Values](onyx_l3_interface_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always.  Sample: `["interfaces ethernet 1/1 ip address 192.168.0.1 /24"]` |

### Authors

- Samer Deeb (@samerd)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
