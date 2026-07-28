---
collection: ansible
version: "6"
title: "ansible.netcommon.net_vrf module – (deprecated, removed after 2022-06-01) Manage VRFs on network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/netcommon/net_vrf_module.html
fetched_at: 2026-07-27T16:44:34+00:00
---
# ansible.netcommon.net_vrf module – (deprecated, removed after 2022-06-01) Manage VRFs on network devices

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
> To use it in a playbook, specify: `ansible.netcommon.net_vrf`.

New in ansible.netcommon 1.0.0

- [DEPRECATED](net_vrf_module.md#deprecated)
- [Synopsis](net_vrf_module.md#synopsis)
- [Parameters](net_vrf_module.md#parameters)
- [Notes](net_vrf_module.md#notes)
- [Examples](net_vrf_module.md#examples)
- [Return Values](net_vrf_module.md#return-values)
- [Status](net_vrf_module.md#status)

## [DEPRECATED](net_vrf_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality

Alternative:
:   Use platform-specific “[netos]_vrf” module

## [Synopsis](net_vrf_module.md#id2)

- This module provides declarative management of VRFs on network devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](net_vrf_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aggregate**  string | List of VRFs definitions |
| **interfaces**  string | List of interfaces the VRF should be configured on. |
| **name**  string | Name of the VRF. |
| **purge**  string | Purge VRFs not defined in the *aggregate* parameter.  Default: `false` |
| **state**  string | State of the VRF configuration.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](net_vrf_module.md#id4)

> **Note:**
>
> - This module is supported on `ansible_network_os` network platforms. See the :ref:`Network Platform Options <platform_options>` for details.

## [Examples](net_vrf_module.md#id5)

```yaml+jinja
- name: Create VRF named MANAGEMENT
  ansible.netcommon.net_vrf:
    name: MANAGEMENT

- name: remove VRF named MANAGEMENT
  ansible.netcommon.net_vrf:
    name: MANAGEMENT
    state: absent

- name: Create aggregate of VRFs with purge
  ansible.netcommon.net_vrf:
    aggregate:
    - name: test4
      rd: 1:204
    - name: test5
      rd: 1:205
    state: present
    purge: yes

- name: Delete aggregate of VRFs
  ansible.netcommon.net_vrf:
    aggregate:
    - name: test2
    - name: test3
    - name: test4
    - name: test5
    state: absent
```

## [Return Values](net_vrf_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always, except for the platforms that use Netconf transport to manage the device.  Sample: `["vrf definition MANAGEMENT"]` |

## [Status](net_vrf_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](net_vrf_module.md#deprecated).

### Authors

- Ricardo Carrillo Cruz (@rcarrillocruz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
