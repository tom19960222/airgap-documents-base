---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_vxlan_vtep_vni module – Creates a Virtual Network Identifier member (VNI)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_vxlan_vtep_vni_module.html
fetched_at: 2026-07-28T01:39:26+00:00
---
# cisco.nxos.nxos_vxlan_vtep_vni module – Creates a Virtual Network Identifier member (VNI)

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
> To use it in a playbook, specify: `cisco.nxos.nxos_vxlan_vtep_vni`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_vxlan_vtep_vni_module.md#synopsis)
- [Parameters](nxos_vxlan_vtep_vni_module.md#parameters)
- [Notes](nxos_vxlan_vtep_vni_module.md#notes)
- [Examples](nxos_vxlan_vtep_vni_module.md#examples)
- [Return Values](nxos_vxlan_vtep_vni_module.md#return-values)

## [Synopsis](nxos_vxlan_vtep_vni_module.md#id1)

- Creates a Virtual Network Identifier member (VNI) for an NVE overlay interface.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: vxlan_vtep_vni

## [Parameters](nxos_vxlan_vtep_vni_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **assoc_vrf**  boolean | This attribute is used to identify and separate processing VNIs that are associated with a VRF and used for routing. The VRF and VNI specified with this command must match the configuration of the VNI under the VRF.  **Choices:**   - `false` - `true` |
| **ingress_replication**  string | Specifies mechanism for host reachability advertisement.  **Choices:**   - `"bgp"` - `"static"` - `"default"` |
| **interface**  string / required | Interface name for the VXLAN Network Virtualization Endpoint. |
| **multicast_group**  string | The multicast group (range) of the VNI. Valid values are string and keyword ‘default’. |
| **multisite_ingress_replication**  string  *added in cisco.nxos 1.1.0* | Enables multisite ingress replication.  **Choices:**   - `"disable"` - `"enable"` - `"optimized"` |
| **peer_list**  list / elements=string | Set the ingress-replication static peer list. Valid values are an array, a space-separated string of ip addresses, or the keyword ‘default’. |
| **state**  string | Determines whether the config should be present or not on the device.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **suppress_arp**  boolean | Suppress arp under layer 2 VNI.  **Choices:**   - `false` - `true` |
| **suppress_arp_disable**  boolean | Overrides the global ARP suppression config. This is available on NX-OS 9K series running 9.2.x or higher.  **Choices:**   - `false` - `true` |
| **vni**  string / required | ID of the Virtual Network Identifier. |

## [Notes](nxos_vxlan_vtep_vni_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - default, where supported, restores params default value.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_vxlan_vtep_vni_module.md#id4)

```yaml+jinja
- cisco.nxos.nxos_vxlan_vtep_vni:
    interface: nve1
    vni: 6000
    ingress_replication: default
    multisite_ingress_replication: enable
```

## [Return Values](nxos_vxlan_vtep_vni_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["interface nve1", "member vni 6000", "multisite ingress-replication"]` |

### Authors

- Gabriele Gerbino (@GGabriele)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
