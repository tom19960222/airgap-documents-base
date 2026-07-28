---
collection: ansible
version: "8"
title: "community.network.cnos_vrf module – Manage VRFs on Lenovo CNOS network devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/cnos_vrf_module.html
fetched_at: 2026-07-28T01:56:23+00:00
---
# community.network.cnos_vrf module – Manage VRFs on Lenovo CNOS network devices

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.cnos_vrf`.

- [Synopsis](cnos_vrf_module.md#synopsis)
- [Parameters](cnos_vrf_module.md#parameters)
- [Notes](cnos_vrf_module.md#notes)
- [Examples](cnos_vrf_module.md#examples)
- [Return Values](cnos_vrf_module.md#return-values)

## [Synopsis](cnos_vrf_module.md#id1)

- This module provides declarative management of VRFs on Lenovo CNOS network devices.

Aliases: network.cnos.cnos_vrf

## [Parameters](cnos_vrf_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  string | List of VRFs contexts |
| **associated_interfaces**  string | This is a intent option and checks the operational state of the for given vrf `name` for associated interfaces. If the value in the `associated_interfaces` does not match with the operational state of vrf interfaces on device it will result in failure. |
| **delay**  string | Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state arguments.  **Default:** `10` |
| **interfaces**  string | Identifies the set of interfaces that should be configured in the VRF. Interfaces must be routed interfaces in order to be placed into a VRF. The name of interface should be in expanded format and not abbreviated. |
| **name**  string / required | Name of the VRF. |
| **purge**  boolean | Purge VRFs not defined in the *aggregate* parameter.  **Choices:**   - `false` ← (default) - `true` |
| **rd**  string | Route distinguisher of the VRF |
| **state**  string | State of the VRF configuration.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](cnos_vrf_module.md#id3)

> **Note:**
>
> - Tested against CNOS 10.9.1

## [Examples](cnos_vrf_module.md#id4)

```yaml+jinja
- name: Create vrf
  community.network.cnos_vrf:
    name: test
    rd: 1:200
    interfaces:
      - Ethernet1/33
    state: present

- name: Delete VRFs
  community.network.cnos_vrf:
    name: test
    state: absent

- name: Create aggregate of VRFs with purge
  community.network.cnos_vrf:
    aggregate:
      - { name: test4, rd: "1:204" }
      - { name: test5, rd: "1:205" }
    state: present
    purge: true

- name: Delete aggregate of VRFs
  community.network.cnos_vrf:
    aggregate:
      - name: test2
      - name: test3
      - name: test4
      - name: test5
    state: absent
```

## [Return Values](cnos_vrf_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["vrf context test", "rd 1:100", "interface Ethernet1/44", "vrf member test"]` |

### Authors

- Anil Kumar Muraleedharan (@amuraleedhar)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
