---
collection: ansible
version: "6"
title: "ansible.netcommon.net_lldp module – (deprecated, removed after 2022-06-01) Manage LLDP service configuration on network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/netcommon/net_lldp_module.html
fetched_at: 2026-07-27T16:44:30+00:00
---
# ansible.netcommon.net_lldp module – (deprecated, removed after 2022-06-01) Manage LLDP service configuration on network devices

> **Note:**
>
> This module is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ansible/netcommon) (version 3.1.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.net_lldp`.

New in ansible.netcommon 1.0.0

- [DEPRECATED](net_lldp_module.md#deprecated)
- [Synopsis](net_lldp_module.md#synopsis)
- [Parameters](net_lldp_module.md#parameters)
- [Notes](net_lldp_module.md#notes)
- [Examples](net_lldp_module.md#examples)
- [Return Values](net_lldp_module.md#return-values)
- [Status](net_lldp_module.md#status)

## [DEPRECATED](net_lldp_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality

Alternative:
:   Use platform-specific “[netos]_lldp_global” module

## [Synopsis](net_lldp_module.md#id2)

- This module provides declarative management of LLDP service configuration on network devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](net_lldp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **state**  string | State of the LLDP service configuration.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](net_lldp_module.md#id4)

> **Note:**
>
> - This module is supported on `ansible_network_os` network platforms. See the :ref:`Network Platform Options <platform_options>` for details.

## [Examples](net_lldp_module.md#id5)

```yaml+jinja
- name: Enable LLDP service
  ansible.netcommon.net_lldp:
    state: present

- name: Disable LLDP service
  ansible.netcommon.net_lldp:
    state: absent
```

## [Return Values](net_lldp_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always, except for the platforms that use Netconf transport to manage the device.  Sample: `["set service lldp"]` |

## [Status](net_lldp_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](net_lldp_module.md#deprecated).

### Authors

- Ricardo Carrillo Cruz (@rcarrillocruz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
