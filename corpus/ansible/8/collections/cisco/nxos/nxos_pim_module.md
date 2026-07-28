---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_pim module – Manages configuration of a PIM instance."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_pim_module.html
fetched_at: 2026-07-28T01:39:01+00:00
---
# cisco.nxos.nxos_pim module – Manages configuration of a PIM instance.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_pim`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_pim_module.md#synopsis)
- [Parameters](nxos_pim_module.md#parameters)
- [Notes](nxos_pim_module.md#notes)
- [Examples](nxos_pim_module.md#examples)
- [Return Values](nxos_pim_module.md#return-values)

## [Synopsis](nxos_pim_module.md#id1)

- Manages configuration of a Protocol Independent Multicast (PIM) instance.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: pim

## [Parameters](nxos_pim_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bfd**  string | Enables BFD on all PIM interfaces.  Dependency: ‘’feature bfd’’  **Choices:**   - `"enable"` - `"disable"` |
| **ssm_range**  list / elements=string | Configure group ranges for Source Specific Multicast (SSM). Valid values are multicast addresses or the keyword `none` or keyword `default`. `none` removes all SSM group ranges. `default` will set ssm_range to the default multicast address. If you set multicast address, please ensure that it is not the same as the `default`, otherwise use the `default` option.  **Default:** `[]` |

## [Notes](nxos_pim_module.md#id3)

> **Note:**
>
> - Unsupported for Cisco MDS
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_pim_module.md#id4)

```yaml+jinja
- name: Configure ssm_range, enable bfd
  cisco.nxos.nxos_pim:
    bfd: enable
    ssm_range: 224.0.0.0/8

- name: Set to default
  cisco.nxos.nxos_pim:
    ssm_range: default

- name: Remove all ssm group ranges
  cisco.nxos.nxos_pim:
    ssm_range: none
```

## [Return Values](nxos_pim_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["ip pim bfd", "ip pim ssm range 224.0.0.0/8"]` |

### Authors

- Gabriele Gerbino (@GGabriele)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
