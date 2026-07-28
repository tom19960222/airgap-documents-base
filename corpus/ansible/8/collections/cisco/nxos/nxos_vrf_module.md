---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_vrf module – Manages global VRF configuration."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_vrf_module.html
fetched_at: 2026-07-28T01:39:20+00:00
---
# cisco.nxos.nxos_vrf module – Manages global VRF configuration.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_vrf`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_vrf_module.md#synopsis)
- [Parameters](nxos_vrf_module.md#parameters)
- [Notes](nxos_vrf_module.md#notes)
- [Examples](nxos_vrf_module.md#examples)
- [Return Values](nxos_vrf_module.md#return-values)

## [Synopsis](nxos_vrf_module.md#id1)

- This module provides declarative management of VRFs on CISCO NXOS network devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: vrf

## [Parameters](nxos_vrf_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **admin_state**  string | Administrative state of the VRF.  **Choices:**   - `"up"` ← (default) - `"down"` |
| **aggregate**  list / elements=dictionary | List of VRFs definitions. |
| **admin_state**  string | Administrative state of the VRF.  **Choices:**   - `"up"` - `"down"` |
| **associated_interfaces**  list / elements=string | This is a intent option and checks the operational state of the for given vrf `name` for associated interfaces. If the value in the `associated_interfaces` does not match with the operational state of vrf interfaces on device it will result in failure. |
| **delay**  integer | Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state arguments. |
| **description**  string | Description of the VRF or keyword ‘default’. |
| **interfaces**  list / elements=string | List of interfaces to check the VRF has been configured correctly or keyword ‘default’. |
| **name**  aliases: vrf  string | Name of VRF to be managed. |
| **rd**  string | VPN Route Distinguisher (RD). Valid values are a string in one of the route-distinguisher formats (ASN2:NN, ASN4:NN, or IPV4:NN); the keyword ‘auto’, or the keyword ‘default’. |
| **state**  string | Manages desired state of the resource.  **Choices:**   - `"present"` - `"absent"` |
| **vni**  string | Specify virtual network identifier. Valid values are Integer or keyword ‘default’. |
| **associated_interfaces**  list / elements=string | This is a intent option and checks the operational state of the for given vrf `name` for associated interfaces. If the value in the `associated_interfaces` does not match with the operational state of vrf interfaces on device it will result in failure. |
| **delay**  integer | Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state arguments.  **Default:** `10` |
| **description**  string | Description of the VRF or keyword ‘default’. |
| **interfaces**  list / elements=string | List of interfaces to check the VRF has been configured correctly or keyword ‘default’. |
| **name**  aliases: vrf  string | Name of VRF to be managed. |
| **purge**  boolean | Purge VRFs not defined in the *aggregate* parameter.  **Choices:**   - `false` ← (default) - `true` |
| **rd**  string | VPN Route Distinguisher (RD). Valid values are a string in one of the route-distinguisher formats (ASN2:NN, ASN4:NN, or IPV4:NN); the keyword ‘auto’, or the keyword ‘default’. |
| **state**  string | Manages desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vni**  string | Specify virtual network identifier. Valid values are Integer or keyword ‘default’. |

## [Notes](nxos_vrf_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - Cisco NX-OS creates the default VRF by itself. Therefore, you’re not allowed to use default as *vrf* name in this module.
> - `vrf` name must be shorter than 32 chars.
> - VRF names are not case sensible in NX-OS. Anyway, the name is stored just like it’s inserted by the user and it’ll not be changed again unless the VRF is removed and re-created. i.e. `vrf=NTC` will create a VRF named NTC, but running it again with `vrf=ntc` will not cause a configuration change.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_vrf_module.md#id4)

```yaml+jinja
- name: Ensure ntc VRF exists on switch
  cisco.nxos.nxos_vrf:
    name: ntc
    description: testing
    state: present

- name: Aggregate definition of VRFs
  cisco.nxos.nxos_vrf:
    aggregate:
    - {name: test1, description: Testing, admin_state: down}
    - {name: test2, interfaces: Ethernet1/2}

- name: Aggregate definitions of VRFs with Purge
  cisco.nxos.nxos_vrf:
    aggregate:
    - {name: ntc1, description: purge test1}
    - {name: ntc2, description: purge test2}
    state: present
    purge: true

- name: Delete VRFs exist on switch
  cisco.nxos.nxos_vrf:
    aggregate:
    - {name: ntc1}
    - {name: ntc2}
    state: absent

- name: Assign interfaces to VRF declaratively
  cisco.nxos.nxos_vrf:
    name: test1
    interfaces:
    - Ethernet2/3
    - Ethernet2/5

- name: Check interfaces assigned to VRF
  cisco.nxos.nxos_vrf:
    name: test1
    associated_interfaces:
    - Ethernet2/3
    - Ethernet2/5

- name: Ensure VRF is tagged with interface Ethernet2/5 only (Removes from Ethernet2/3)
  cisco.nxos.nxos_vrf:
    name: test1
    interfaces:
    - Ethernet2/5

- name: Delete VRF
  cisco.nxos.nxos_vrf:
    name: ntc
    state: absent
```

## [Return Values](nxos_vrf_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["vrf context ntc", "no shutdown", "interface Ethernet1/2", "no switchport", "vrf member test2"]` |

### Authors

- Jason Edelman (@jedelman8)
- Gabriele Gerbino (@GGabriele)
- Trishna Guha (@trishnaguha)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
