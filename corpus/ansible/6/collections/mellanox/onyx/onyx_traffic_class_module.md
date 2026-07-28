---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_traffic_class module – Configures Traffic Class"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_traffic_class_module.html
fetched_at: 2026-07-27T17:55:43+00:00
---
# mellanox.onyx.onyx_traffic_class module – Configures Traffic Class

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
> To use it in a playbook, specify: `mellanox.onyx.onyx_traffic_class`.

- [Synopsis](onyx_traffic_class_module.md#synopsis)
- [Parameters](onyx_traffic_class_module.md#parameters)
- [Examples](onyx_traffic_class_module.md#examples)
- [Return Values](onyx_traffic_class_module.md#return-values)

## [Synopsis](onyx_traffic_class_module.md#id1)

- This module provides declarative management of Traffic Class configuration on Mellanox ONYX network devices.

## [Parameters](onyx_traffic_class_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **congestion_control**  string | configure congestion control on interface. |
| **control**  string / required | congestion control type.  Choices:   - `"red"` - `"ecn"` - `"both"` |
| **max_threshold**  string / required | Set maximum-threshold value (in KBs) for marking traffic-class queue. |
| **min_threshold**  string / required | Set minimum-threshold value (in KBs) for marking traffic-class queue. |
| **threshold_mode**  string / required | congestion control threshold mode.  Choices:   - `"absolute"` - `"relative"` |
| **dcb**  string | configure dcb control on interface. |
| **mode**  string / required | dcb control mode.  Choices:   - `"strict"` - `"wrr"` |
| **weight**  string | Relevant only for wrr mode. |
| **interfaces**  string / required | list of interfaces name. |
| **state**  string | enable congestion control on interface.  Choices:   - `"enabled"` ← (default) - `"disabled"` |
| **tc**  string / required | traffic class, range 0-7. |

## [Examples](onyx_traffic_class_module.md#id3)

```yaml+jinja
- name: Configure traffic class
  onyx_traffic_class:
    interfaces:
      - Eth1/1
      - Eth1/2
    tc: 3
    congestion_control:
      control: ecn
      threshold_mode: absolute
      min_threshold: 500
      max_threshold: 1500
    dcb:
      mode: strict
```

## [Return Values](onyx_traffic_class_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["interface ethernet 1/15 traffic-class 3 congestion-control ecn minimum-absolute 150 maximum-absolute 1500", "interface ethernet 1/16 traffic-class 3 congestion-control ecn minimum-absolute 150 maximum-absolute 1500", "interface mlag-port-channel 7 traffic-class 3 congestion-control ecn minimum-absolute 150 maximum-absolute 1500", "interface port-channel 1 traffic-class 3 congestion-control ecn minimum-absolute 150 maximum-absolute 1500", "interface ethernet 1/15 traffic-class 3 dcb ets strict", "interface ethernet 1/16 traffic-class 3 dcb ets strict", "interface mlag-port-channel 7 traffic-class 3 dcb ets strict", "interface port-channel 1 traffic-class 3 dcb ets strict"]` |

### Authors

- Anas Badaha (@anasb)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
