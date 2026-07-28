---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_qos module – Configures QoS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_qos_module.html
fetched_at: 2026-07-27T17:55:39+00:00
---
# mellanox.onyx.onyx_qos module – Configures QoS

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
> To use it in a playbook, specify: `mellanox.onyx.onyx_qos`.

- [Synopsis](onyx_qos_module.md#synopsis)
- [Parameters](onyx_qos_module.md#parameters)
- [Notes](onyx_qos_module.md#notes)
- [Examples](onyx_qos_module.md#examples)
- [Return Values](onyx_qos_module.md#return-values)

## [Synopsis](onyx_qos_module.md#id1)

- This module provides declarative management of Onyx QoS configuration on Mellanox ONYX network devices.

## [Parameters](onyx_qos_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **interfaces**  string / required | list of interfaces name. |
| **rewrite_dscp**  string | rewrite with type dscp.  Choices:   - `"enabled"` - `"disabled"` ← (default) |
| **rewrite_pcp**  string | rewrite with type pcp.  Choices:   - `"enabled"` - `"disabled"` ← (default) |
| **trust**  string | trust type.  Choices:   - `"L2"` ← (default) - `"L3"` - `"both"` |

## [Notes](onyx_qos_module.md#id3)

> **Note:**
>
> - Tested on ONYX 3.6.8130

## [Examples](onyx_qos_module.md#id4)

```yaml+jinja
- name: Configure QoS
  onyx_QoS:
    interfaces:
      - Mpo7
      - Mpo7
    trust: L3
    rewrite_pcp: disabled
    rewrite_dscp: enabled

- name: Configure QoS
  onyx_QoS:
    interfaces:
      - Eth1/1
      - Eth1/2
    trust: both
    rewrite_pcp: disabled
    rewrite_dscp: enabled
```

## [Return Values](onyx_qos_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["interface ethernet 1/16 qos trust L3", "interface mlag-port-channel 7 qos trust L3", "interface port-channel 1 qos trust L3", "interface mlag-port-channel 7 qos trust L2", "interface mlag-port-channel 7 qos rewrite dscp", "interface ethernet 1/16 qos rewrite pcp", "interface ethernet 1/1 no qos rewrite pcp"]` |

### Authors

- Anas Badaha (@anasb)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
