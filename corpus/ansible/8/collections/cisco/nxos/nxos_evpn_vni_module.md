---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_evpn_vni module – Manages Cisco EVPN VXLAN Network Identifier (VNI)."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_evpn_vni_module.html
fetched_at: 2026-07-28T01:38:37+00:00
---
# cisco.nxos.nxos_evpn_vni module – Manages Cisco EVPN VXLAN Network Identifier (VNI).

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
> To use it in a playbook, specify: `cisco.nxos.nxos_evpn_vni`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_evpn_vni_module.md#synopsis)
- [Parameters](nxos_evpn_vni_module.md#parameters)
- [Notes](nxos_evpn_vni_module.md#notes)
- [Examples](nxos_evpn_vni_module.md#examples)
- [Return Values](nxos_evpn_vni_module.md#return-values)

## [Synopsis](nxos_evpn_vni_module.md#id1)

- Manages Cisco Ethernet Virtual Private Network (EVPN) VXLAN Network Identifier (VNI) configurations of a Nexus device.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: evpn_vni

## [Parameters](nxos_evpn_vni_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **route_distinguisher**  string | The VPN Route Distinguisher (RD). The RD is combined with the IPv4 or IPv6 prefix learned by the PE router to create a globally unique address. |
| **route_target_both**  list / elements=string | Enables/Disables route-target settings for both import and export target communities using a single property. |
| **route_target_export**  list / elements=string | Sets the route-target ‘export’ extended communities. |
| **route_target_import**  list / elements=string | Sets the route-target ‘import’ extended communities. |
| **state**  string | Determines whether the config should be present or not on the device.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vni**  string / required | The EVPN VXLAN Network Identifier. |

## [Notes](nxos_evpn_vni_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - default, where supported, restores params default value.
> - RD override is not permitted. You should set it to the default values first and then reconfigure it.
> - `route_target_both`, `route_target_import` and `route_target_export valid` values are a list of extended communities, (i.e. [‘1.2.3.4:5’, ‘33:55’]) or the keywords ‘auto’ or ‘default’.
> - The `route_target_both` property is discouraged due to the inconsistent behavior of the property across Nexus platforms and image versions. For this reason it is recommended to use explicit `route_target_export` and `route_target_import` properties instead of `route_target_both`.
> - RD valid values are a string in one of the route-distinguisher formats, the keyword ‘auto’, or the keyword ‘default’.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_evpn_vni_module.md#id4)

```yaml+jinja
- name: vni configuration
  cisco.nxos.nxos_evpn_vni:
    vni: 6000
    route_distinguisher: 60:10
    route_target_import:
    - 5000:10
    - 4100:100
    route_target_export: auto
    route_target_both: default
```

## [Return Values](nxos_evpn_vni_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["evpn", "vni 6000 l2", "route-target import 5001:10"]` |

### Authors

- Gabriele Gerbino (@GGabriele)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
