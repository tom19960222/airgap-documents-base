---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_mlag_vip module – Configures MLAG VIP on Mellanox ONYX network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_mlag_vip_module.html
fetched_at: 2026-07-27T17:55:34+00:00
---
# mellanox.onyx.onyx_mlag_vip module – Configures MLAG VIP on Mellanox ONYX network devices

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
> To use it in a playbook, specify: `mellanox.onyx.onyx_mlag_vip`.

- [Synopsis](onyx_mlag_vip_module.md#synopsis)
- [Parameters](onyx_mlag_vip_module.md#parameters)
- [Notes](onyx_mlag_vip_module.md#notes)
- [Examples](onyx_mlag_vip_module.md#examples)
- [Return Values](onyx_mlag_vip_module.md#return-values)

## [Synopsis](onyx_mlag_vip_module.md#id1)

- This module provides declarative management of MLAG virtual IPs on Mellanox ONYX network devices.

## [Parameters](onyx_mlag_vip_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **delay**  string | Delay interval, in seconds, waiting for the changes on mlag VIP to take effect.  Default: `12` |
| **group_name**  string | MLAG group name. Required if *state=present*. |
| **ipaddress**  string | Virtual IP address of the MLAG. Required if *state=present*. |
| **mac_address**  string | MLAG system MAC address. Required if *state=present*. |
| **state**  string | MLAG VIP state.  Choices:   - `"present"` - `"absent"` |

## [Notes](onyx_mlag_vip_module.md#id3)

> **Note:**
>
> - Tested on ONYX 3.6.4000

## [Examples](onyx_mlag_vip_module.md#id4)

```yaml+jinja
- name: Configure mlag-vip
  onyx_mlag_vip:
    ipaddress: 50.3.3.1/24
    group_name: ansible-test-group
    mac_address: 00:11:12:23:34:45
```

## [Return Values](onyx_mlag_vip_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["mlag-vip ansible_test_group ip 50.3.3.1 /24 force", "no mlag shutdown"]` |

### Authors

- Samer Deeb (@samerd)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
