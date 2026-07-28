---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_overlay_global module – Configures anycast gateway MAC of the switch."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_overlay_global_module.html
fetched_at: 2026-07-28T01:39:00+00:00
---
# cisco.nxos.nxos_overlay_global module – Configures anycast gateway MAC of the switch.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_overlay_global`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_overlay_global_module.md#synopsis)
- [Parameters](nxos_overlay_global_module.md#parameters)
- [Notes](nxos_overlay_global_module.md#notes)
- [Examples](nxos_overlay_global_module.md#examples)
- [Return Values](nxos_overlay_global_module.md#return-values)

## [Synopsis](nxos_overlay_global_module.md#id1)

- Configures anycast gateway MAC of the switch.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: overlay_global

## [Parameters](nxos_overlay_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **anycast_gateway_mac**  string / required | Anycast gateway mac of the switch. |

## [Notes](nxos_overlay_global_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - Default restores params default value
> - Supported MAC address format are “E.E.E”, “EE-EE-EE-EE-EE-EE”, “EE:EE:EE:EE:EE:EE” and “EEEE.EEEE.EEEE”
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_overlay_global_module.md#id4)

```yaml+jinja
- cisco.nxos.nxos_overlay_global:
    anycast_gateway_mac: b.b.b
```

## [Return Values](nxos_overlay_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["fabric forwarding anycast-gateway-mac 000B.000B.000B"]` |

### Authors

- Gabriele Gerbino (@GGabriele)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
