---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_ptp_global module – Configures PTP Global parameters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_ptp_global_module.html
fetched_at: 2026-07-27T17:55:38+00:00
---
# mellanox.onyx.onyx_ptp_global module – Configures PTP Global parameters

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
> To use it in a playbook, specify: `mellanox.onyx.onyx_ptp_global`.

- [Synopsis](onyx_ptp_global_module.md#synopsis)
- [Parameters](onyx_ptp_global_module.md#parameters)
- [Notes](onyx_ptp_global_module.md#notes)
- [Examples](onyx_ptp_global_module.md#examples)
- [Return Values](onyx_ptp_global_module.md#return-values)

## [Synopsis](onyx_ptp_global_module.md#id1)

- This module provides declarative management of PTP Global configuration on Mellanox ONYX network devices.

## [Parameters](onyx_ptp_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **domain**  string | set PTP domain number Range 0-127 |
| **ntp_state**  string | NTP state.  Choices:   - `"enabled"` - `"disabled"` |
| **primary_priority**  string | set PTP primary priority Range 0-225 |
| **ptp_state**  string | PTP state.  Choices:   - `"enabled"` ← (default) - `"disabled"` |
| **secondary_priority**  string | set PTP secondary priority Range 0-225 |

## [Notes](onyx_ptp_global_module.md#id3)

> **Note:**
>
> - Tested on ONYX 3.6.8130 ptp and ntp protocols cannot be enabled at the same time

## [Examples](onyx_ptp_global_module.md#id4)

```yaml+jinja
- name: Configure PTP
  onyx_ptp_global:
    ntp_state: enabled
    ptp_state: disabled
    domain: 127
    primary_priority: 128
    secondary_priority: 128
```

## [Return Values](onyx_ptp_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["no ntp enable", "protocol ptp", "ptp domain 127"]` |

### Authors

- Anas Badaha (@anasb)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
