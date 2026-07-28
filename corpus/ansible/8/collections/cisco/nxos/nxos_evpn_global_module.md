---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_evpn_global module – Handles the EVPN control plane for VXLAN."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_evpn_global_module.html
fetched_at: 2026-07-28T01:38:36+00:00
---
# cisco.nxos.nxos_evpn_global module – Handles the EVPN control plane for VXLAN.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_evpn_global`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_evpn_global_module.md#synopsis)
- [Parameters](nxos_evpn_global_module.md#parameters)
- [Notes](nxos_evpn_global_module.md#notes)
- [Examples](nxos_evpn_global_module.md#examples)
- [Return Values](nxos_evpn_global_module.md#return-values)

## [Synopsis](nxos_evpn_global_module.md#id1)

- Handles the EVPN control plane for VXLAN.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: evpn_global

## [Parameters](nxos_evpn_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **nv_overlay_evpn**  boolean / required | EVPN control plane.  **Choices:**   - `false` - `true` |

## [Notes](nxos_evpn_global_module.md#id3)

> **Note:**
>
> - This module is not supported on Nexus 3000 series of switches.
> - Unsupported for Cisco MDS
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_evpn_global_module.md#id4)

```yaml+jinja
- cisco.nxos.nxos_evpn_global:
    nv_overlay_evpn: true
```

## [Return Values](nxos_evpn_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The set of commands to be sent to the remote device  **Returned:** always  **Sample:** `["nv overlay evpn"]` |

### Authors

- Gabriele Gerbino (@GGabriele)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
