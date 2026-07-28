---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_magp module – Manage MAGP protocol on Mellanox ONYX network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_magp_module.html
fetched_at: 2026-07-27T17:55:32+00:00
---
# mellanox.onyx.onyx_magp module – Manage MAGP protocol on Mellanox ONYX network devices

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
> To use it in a playbook, specify: `mellanox.onyx.onyx_magp`.

- [Synopsis](onyx_magp_module.md#synopsis)
- [Parameters](onyx_magp_module.md#parameters)
- [Notes](onyx_magp_module.md#notes)
- [Examples](onyx_magp_module.md#examples)
- [Return Values](onyx_magp_module.md#return-values)

## [Synopsis](onyx_magp_module.md#id1)

- This module provides declarative management of MAGP protocol on vlan interface of Mellanox ONYX network devices.

## [Parameters](onyx_magp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **interface**  string / required | VLAN Interface name. |
| **magp_id**  string / required | MAGP instance number 1-255 |
| **router_ip**  string | MAGP router IP address. |
| **router_mac**  string | MAGP router MAC address. |
| **state**  string | MAGP state.  Choices:   - `"present"` ← (default) - `"absent"` - `"enabled"` - `"disabled"` |

## [Notes](onyx_magp_module.md#id3)

> **Note:**
>
> - Tested on ONYX 3.6.4000

## [Examples](onyx_magp_module.md#id4)

```yaml+jinja
- name: Run add vlan interface with magp
  onyx_magp:
    magp_id: 103
    router_ip: 192.168.8.2
    router_mac: AA:1B:2C:3D:4E:5F
    interface: Vlan 1002
```

## [Return Values](onyx_magp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["interface vlan 234 magp 103", "exit", "interface vlan 234 magp 103 ip virtual-router address 1.2.3.4"]` |

### Authors

- Samer Deeb (@samerd)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
