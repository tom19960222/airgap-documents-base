---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_pim_rp_address module – Manages configuration of an PIM static RP address instance."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_pim_rp_address_module.html
fetched_at: 2026-07-28T01:39:02+00:00
---
# cisco.nxos.nxos_pim_rp_address module – Manages configuration of an PIM static RP address instance.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_pim_rp_address`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_pim_rp_address_module.md#synopsis)
- [Parameters](nxos_pim_rp_address_module.md#parameters)
- [Notes](nxos_pim_rp_address_module.md#notes)
- [Examples](nxos_pim_rp_address_module.md#examples)
- [Return Values](nxos_pim_rp_address_module.md#return-values)

## [Synopsis](nxos_pim_rp_address_module.md#id1)

- Manages configuration of an Protocol Independent Multicast (PIM) static rendezvous point (RP) address instance.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: pim_rp_address

## [Parameters](nxos_pim_rp_address_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bidir**  boolean | Group range is treated in PIM bidirectional mode.  **Choices:**   - `false` - `true` |
| **group_list**  string | Group range for static RP. Valid values are multicast addresses. |
| **prefix_list**  string | Prefix list policy for static RP. Valid values are prefix-list policy names. |
| **route_map**  string | Route map policy for static RP. Valid values are route-map policy names. |
| **rp_address**  string / required | Configures a Protocol Independent Multicast (PIM) static rendezvous point (RP) address. Valid values are unicast addresses. |
| **state**  string | Specify desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](nxos_pim_rp_address_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - `state=absent` is currently not supported on all platforms.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_pim_rp_address_module.md#id4)

```yaml+jinja
- cisco.nxos.nxos_pim_rp_address:
    rp_address: 10.1.1.20
    state: present
```

## [Return Values](nxos_pim_rp_address_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["router bgp 65535", "vrf test", "router-id 192.0.2.1"]` |

### Authors

- Gabriele Gerbino (@GGabriele)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
