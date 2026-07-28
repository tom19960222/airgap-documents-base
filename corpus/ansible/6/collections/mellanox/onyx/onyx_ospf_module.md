---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_ospf module – Manage OSPF protocol on Mellanox ONYX network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_ospf_module.html
fetched_at: 2026-07-27T17:55:36+00:00
---
# mellanox.onyx.onyx_ospf module – Manage OSPF protocol on Mellanox ONYX network devices

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
> To use it in a playbook, specify: `mellanox.onyx.onyx_ospf`.

- [Synopsis](onyx_ospf_module.md#synopsis)
- [Parameters](onyx_ospf_module.md#parameters)
- [Notes](onyx_ospf_module.md#notes)
- [Examples](onyx_ospf_module.md#examples)
- [Return Values](onyx_ospf_module.md#return-values)

## [Synopsis](onyx_ospf_module.md#id1)

- This module provides declarative management and configuration of OSPF protocol on Mellanox ONYX network devices.

## [Parameters](onyx_ospf_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **interfaces**  string | List of interfaces and areas. Required if *state=present*. |
| **area**  string / required | OSPF area. |
| **name**  string / required | Interface name. |
| **ospf**  string / required | OSPF instance number 1-65535 |
| **router_id**  string | OSPF router ID. Required if *state=present*. |
| **state**  string | OSPF state.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](onyx_ospf_module.md#id3)

> **Note:**
>
> - Tested on ONYX 3.6.4000

## [Examples](onyx_ospf_module.md#id4)

```yaml+jinja
- name: Add ospf router to interface
  onyx_ospf:
    ospf: 2
    router_id: 192.168.8.2
    interfaces:
      - name: Eth1/1
      - area: 0.0.0.0
```

## [Return Values](onyx_ospf_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["router ospf 2", "router-id 192.168.8.2", "exit", "interface ethernet 1/1 ip ospf area 0.0.0.0"]` |

### Authors

- Samer Deeb (@samerd)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
