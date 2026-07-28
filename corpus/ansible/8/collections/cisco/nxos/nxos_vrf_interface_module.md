---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_vrf_interface module – Manages interface specific VRF configuration."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_vrf_interface_module.html
fetched_at: 2026-07-28T01:39:21+00:00
---
# cisco.nxos.nxos_vrf_interface module – Manages interface specific VRF configuration.

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/ui/repo/published/cisco/nxos/) (version 4.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_vrf_interface`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_vrf_interface_module.md#synopsis)
- [Parameters](nxos_vrf_interface_module.md#parameters)
- [Notes](nxos_vrf_interface_module.md#notes)
- [Examples](nxos_vrf_interface_module.md#examples)
- [Return Values](nxos_vrf_interface_module.md#return-values)

## [Synopsis](nxos_vrf_interface_module.md#id1)

- Manages interface specific VRF configuration.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: vrf_interface

## [Parameters](nxos_vrf_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **interface**  string / required | Full name of interface to be managed, i.e. Ethernet1/1. |
| **state**  string | Manages desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vrf**  string / required | Name of VRF to be managed. |

## [Notes](nxos_vrf_interface_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - VRF needs to be added globally with [cisco.nxos.nxos_vrf](nxos_vrf_module.md#ansible-collections-cisco-nxos-nxos-vrf-module) before adding a VRF to an interface.
> - Remove a VRF from an interface will still remove all L3 attributes just as it does from CLI.
> - VRF is not read from an interface until IP address is configured on that interface.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_vrf_interface_module.md#id4)

```yaml+jinja
- name: Ensure vrf ntc exists on Eth1/1
  cisco.nxos.nxos_vrf_interface:
    vrf: ntc
    interface: Ethernet1/1
    state: present

- name: Ensure ntc VRF does not exist on Eth1/1
  cisco.nxos.nxos_vrf_interface:
    vrf: ntc
    interface: Ethernet1/1
    state: absent
```

## [Return Values](nxos_vrf_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["interface loopback16", "vrf member ntc"]` |

### Authors

- Jason Edelman (@jedelman8)
- Gabriele Gerbino (@GGabriele)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
