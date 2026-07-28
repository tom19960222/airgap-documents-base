---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_vxlan_vtep module – Manages VXLAN Network Virtualization Endpoint (NVE)."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_vxlan_vtep_module.html
fetched_at: 2026-07-28T01:39:25+00:00
---
# cisco.nxos.nxos_vxlan_vtep module – Manages VXLAN Network Virtualization Endpoint (NVE).

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
> To use it in a playbook, specify: `cisco.nxos.nxos_vxlan_vtep`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_vxlan_vtep_module.md#synopsis)
- [Parameters](nxos_vxlan_vtep_module.md#parameters)
- [Notes](nxos_vxlan_vtep_module.md#notes)
- [Examples](nxos_vxlan_vtep_module.md#examples)
- [Return Values](nxos_vxlan_vtep_module.md#return-values)

## [Synopsis](nxos_vxlan_vtep_module.md#id1)

- Manages VXLAN Network Virtualization Endpoint (NVE) overlay interface that terminates VXLAN tunnels.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: vxlan_vtep

## [Parameters](nxos_vxlan_vtep_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **advertise_virtual_rmac**  boolean | The advertise_virtual_rmac parameter lets BGP to use the VMAC with VIP as next-hop when advertising type-2 routes. Should be used together with advertise_pip parameter from cisco.nxos.nxos_bgp_address_family module.  **Choices:**   - `false` - `true` |
| **description**  string | Description of the NVE interface. |
| **global_ingress_replication_bgp**  boolean | Configures ingress replication protocol as bgp for all VNIs. This is available on Nexus 9000 series switches running NX-OS software release 9.2(x) or higher.  **Choices:**   - `false` - `true` |
| **global_mcast_group_L2**  string | Global multicast IP prefix for L2 VNIs or the keyword ‘default’. This is available on Nexus 9000 series switches running NX-OS software release 9.2(x) or higher. |
| **global_mcast_group_L3**  string | Global multicast IP prefix for L3 VNIs or the keyword ‘default’. This is available on Nexus 9000 series switches running NX-OS software release 9.2(x) or higher. |
| **global_suppress_arp**  boolean | Enables ARP suppression for all VNIs. This is available on NX-OS 9K series running 9.2.x or higher.  **Choices:**   - `false` - `true` |
| **host_reachability**  boolean | Specify mechanism for host reachability advertisement. A Boolean value of ‘true’ indicates that BGP will be used for host reachability advertisement. A Boolean value of ‘false’ indicates that no protocol is used for host reachability advertisement. Other host reachability advertisement protocols (e.g. OpenFlow, controller, etc.) are not supported.  **Choices:**   - `false` - `true` |
| **interface**  string / required | Interface name for the VXLAN Network Virtualization Endpoint. |
| **multisite_border_gateway_interface**  string  *added in cisco.nxos 1.1.0* | Specify the loopback interface whose IP address should be used for the NVE Multisite Border-gateway Interface. This is available on specific Nexus 9000 series switches running NX-OS 7.0(3)I7(x) or higher. Specify “default” to remove an existing gateway config. |
| **shutdown**  boolean | Administratively shutdown the NVE interface.  **Choices:**   - `false` - `true` |
| **source_interface**  string | Specify the loopback interface whose IP address should be used for the NVE interface. |
| **source_interface_hold_down_time**  string | Suppresses advertisement of the NVE loopback address until the overlay has converged. |
| **state**  string | Determines whether the config should be present or not on the device.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](nxos_vxlan_vtep_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - The module is used to manage NVE properties, not to create NVE interfaces. Use [cisco.nxos.nxos_interfaces](nxos_interfaces_module.md#ansible-collections-cisco-nxos-nxos-interfaces-module) if you wish to do so.
> - `state=absent` removes the interface.
> - Default, where supported, restores params default value.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_vxlan_vtep_module.md#id4)

```yaml+jinja
- cisco.nxos.nxos_vxlan_vtep:
    interface: nve1
    description: default
    host_reachability: true
    source_interface: Loopback0
    source_interface_hold_down_time: 30
    shutdown: default
    multisite_border_gateway_interface: Loopback0
```

## [Return Values](nxos_vxlan_vtep_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["interface nve1", "source-interface loopback0", "source-interface hold-down-time 30", "description simple description", "shutdown", "host-reachability protocol bgp", "multisite border-gateway interface loopback0"]` |

### Authors

- Gabriele Gerbino (@GGabriele)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
