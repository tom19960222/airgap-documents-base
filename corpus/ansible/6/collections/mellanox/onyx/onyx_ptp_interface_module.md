---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_ptp_interface module – Configures PTP on interface"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_ptp_interface_module.html
fetched_at: 2026-07-27T17:55:38+00:00
---
# mellanox.onyx.onyx_ptp_interface module – Configures PTP on interface

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
> To use it in a playbook, specify: `mellanox.onyx.onyx_ptp_interface`.

- [Synopsis](onyx_ptp_interface_module.md#synopsis)
- [Parameters](onyx_ptp_interface_module.md#parameters)
- [Notes](onyx_ptp_interface_module.md#notes)
- [Examples](onyx_ptp_interface_module.md#examples)
- [Return Values](onyx_ptp_interface_module.md#return-values)

## [Synopsis](onyx_ptp_interface_module.md#id1)

- This module provides declarative management of PTP interfaces configuration on Mellanox ONYX network devices.

## [Parameters](onyx_ptp_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **announce_interval**  string | configure PTP announce setting for interval, Range -3-1 |
| **announce_timeout**  string | configure PTP announce setting for timeout, Range 2-10 |
| **delay_request**  string | configure PTP delay request interval, Range 0-5 |
| **name**  string / required | ethernet or vlan interface name that we want to configure PTP on it |
| **state**  string | Enable/Disable PTP on Interface  Choices:   - `"enabled"` ← (default) - `"disabled"` |
| **sync_interval**  string | configure PTP sync interval, Range -7–1 |

## [Notes](onyx_ptp_interface_module.md#id3)

> **Note:**
>
> - Tested on ONYX 3.6.8130
> - PTP Protocol must be enabled on switch.
> - Interface must not be a switch port interface.

## [Examples](onyx_ptp_interface_module.md#id4)

```yaml+jinja
- name: Configure PTP interface
  onyx_ptp_interface:
    state: enabled
    name: Eth1/1
    delay_request: 0
    announce_interval: -2
    announce_timeout: 3
```

## [Return Values](onyx_ptp_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["interface ethernet 1/16 ptp enable", "interface ethernet 1/16 ptp delay-req interval 0", "interface ethernet 1/16 ptp announce interval -1"]` |

### Authors

- Anas Badaha (@anasb)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
