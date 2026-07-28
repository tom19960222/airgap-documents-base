---
collection: ansible
version: "8"
title: "arista.eos.eos_vrf module – Manage VRFs on Arista EOS network devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/arista/eos/eos_vrf_module.html
fetched_at: 2026-07-28T01:11:19+00:00
---
# arista.eos.eos_vrf module – Manage VRFs on Arista EOS network devices

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/ui/repo/published/arista/eos/) (version 6.2.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_vrf`.

New in arista.eos 1.0.0

- [Synopsis](eos_vrf_module.md#synopsis)
- [Parameters](eos_vrf_module.md#parameters)
- [Notes](eos_vrf_module.md#notes)
- [Examples](eos_vrf_module.md#examples)
- [Return Values](eos_vrf_module.md#return-values)

## [Synopsis](eos_vrf_module.md#id1)

- This module provides declarative management of VRFs on Arista EOS network devices.

Aliases: vrf

## [Parameters](eos_vrf_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  list / elements=dictionary | List of VRFs instances |
| **associated_interfaces**  list / elements=string | This is a intent option and checks the operational state of the for given vrf `name` for associated interfaces. If the value in the `associated_interfaces` does not match with the operational state of vrf interfaces on device it will result in failure. |
| **delay**  integer | Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state arguments.  **Default:** `10` |
| **interfaces**  list / elements=string | Identifies the set of interfaces that should be configured in the VRF. Interfaces must be routed interfaces in order to be placed into a VRF. The name of interface should be in expanded format and not abbreviated. |
| **name**  string / required | Name of the VRF. |
| **rd**  string | Route distinguisher of the VRF |
| **state**  string | State of the VRF configuration.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **associated_interfaces**  list / elements=string | This is a intent option and checks the operational state of the for given vrf `name` for associated interfaces. If the value in the `associated_interfaces` does not match with the operational state of vrf interfaces on device it will result in failure. |
| **delay**  integer | Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state arguments.  **Default:** `10` |
| **interfaces**  list / elements=string | Identifies the set of interfaces that should be configured in the VRF. Interfaces must be routed interfaces in order to be placed into a VRF. The name of interface should be in expanded format and not abbreviated. |
| **name**  string | Name of the VRF. |
| **purge**  boolean | Purge VRFs not defined in the *aggregate* parameter.  **Choices:**   - `false` ← (default) - `true` |
| **rd**  string | Route distinguisher of the VRF |
| **state**  string | State of the VRF configuration.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](eos_vrf_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F

## [Examples](eos_vrf_module.md#id4)

```yaml+jinja
- name: Create vrf
  arista.eos.eos_vrf:
    name: test
    rd: 1:200
    interfaces:
      - Ethernet2
    state: present

- name: Delete VRFs
  arista.eos.eos_vrf:
    name: test
    state: absent

- name: Create aggregate of VRFs with purge
  arista.eos.eos_vrf:
    aggregate:
      - name: test4
        rd: 1:204
      - name: test5
        rd: 1:205
    state: present
    purge: true

- name: Delete aggregate of VRFs
  arista.eos.eos_vrf:
    aggregate:
      - name: test2
      - name: test3
      - name: test4
      - name: test5
    state: absent
```

## [Return Values](eos_vrf_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["vrf instance test", "rd 1:100", "interface Ethernet1", "vrf test"]` |

### Authors

- Ricardo Carrillo Cruz (@rcarrillocruz)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/arista.eos)
