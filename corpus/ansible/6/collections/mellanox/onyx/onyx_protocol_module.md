---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_protocol module – Enables/Disables protocols on Mellanox ONYX network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_protocol_module.html
fetched_at: 2026-07-27T17:55:37+00:00
---
# mellanox.onyx.onyx_protocol module – Enables/Disables protocols on Mellanox ONYX network devices

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
> To use it in a playbook, specify: `mellanox.onyx.onyx_protocol`.

- [Synopsis](onyx_protocol_module.md#synopsis)
- [Parameters](onyx_protocol_module.md#parameters)
- [Notes](onyx_protocol_module.md#notes)
- [Examples](onyx_protocol_module.md#examples)
- [Return Values](onyx_protocol_module.md#return-values)

## [Synopsis](onyx_protocol_module.md#id1)

- This module provides a mechanism for enabling and disabling protocols Mellanox on ONYX network devices.

## [Parameters](onyx_protocol_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bfd**  string  added in mellanox.onyx 0.2.0 | bfd protocol  Choices:   - `"enabled"` - `"disabled"` |
| **bgp**  string | BGP protocol  Choices:   - `"enabled"` - `"disabled"` |
| **dcb_pfc**  string | DCB priority flow control  Choices:   - `"enabled"` - `"disabled"` |
| **igmp_snooping**  string | IP IGMP snooping  Choices:   - `"enabled"` - `"disabled"` |
| **ip_l3**  string | IP L3 support  Choices:   - `"enabled"` - `"disabled"` |
| **ip_routing**  string | IP routing support  Choices:   - `"enabled"` - `"disabled"` |
| **lacp**  string | LACP protocol  Choices:   - `"enabled"` - `"disabled"` |
| **lldp**  string | LLDP protocol  Choices:   - `"enabled"` - `"disabled"` |
| **magp**  string | MAGP protocol  Choices:   - `"enabled"` - `"disabled"` |
| **mlag**  string | MLAG protocol  Choices:   - `"enabled"` - `"disabled"` |
| **nve**  string | nve protocol  Choices:   - `"enabled"` - `"disabled"` |
| **ospf**  string | OSPF protocol  Choices:   - `"enabled"` - `"disabled"` |
| **spanning_tree**  string | Spanning Tree support  Choices:   - `"enabled"` - `"disabled"` |

## [Notes](onyx_protocol_module.md#id3)

> **Note:**
>
> - Tested on ONYX 3.6.4000

## [Examples](onyx_protocol_module.md#id4)

```yaml+jinja
- name: Enable protocols for MLAG
  onyx_protocol:
    lacp: enabled
    spanning_tree: disabled
    ip_routing: enabled
    mlag: enabled
    dcb_pfc: enabled
```

## [Return Values](onyx_protocol_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["no spanning-tree", "protocol mlag"]` |

### Authors

- Samer Deeb (@samerd)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
