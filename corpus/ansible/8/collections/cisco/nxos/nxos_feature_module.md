---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_feature module – Manage features in NX-OS switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_feature_module.html
fetched_at: 2026-07-28T01:38:38+00:00
---
# cisco.nxos.nxos_feature module – Manage features in NX-OS switches.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_feature`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_feature_module.md#synopsis)
- [Parameters](nxos_feature_module.md#parameters)
- [Notes](nxos_feature_module.md#notes)
- [Examples](nxos_feature_module.md#examples)
- [Return Values](nxos_feature_module.md#return-values)

## [Synopsis](nxos_feature_module.md#id1)

- Offers ability to enable and disable features in NX-OS.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: feature

## [Parameters](nxos_feature_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **feature**  string / required | Name of feature. |
| **state**  string | Desired state of the feature.  **Choices:**   - `"enabled"` ← (default) - `"disabled"` |

## [Notes](nxos_feature_module.md#id3)

> **Note:**
>
> - Tested against Cisco MDS NX-OS 9.2(2)
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_feature_module.md#id4)

```yaml+jinja
- name: Ensure lacp is enabled
  cisco.nxos.nxos_feature:
    feature: lacp
    state: enabled

- name: Ensure ospf is disabled
  cisco.nxos.nxos_feature:
    feature: ospf
    state: disabled

- name: Ensure vpc is enabled
  cisco.nxos.nxos_feature:
    feature: vpc
    state: enabled
```

## [Return Values](nxos_feature_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The set of commands to be sent to the remote device  **Returned:** always  **Sample:** `["nv overlay evpn"]` |

### Authors

- Jason Edelman (@jedelman8)
- Gabriele Gerbino (@GGabriele)
- Suhas Bharadwaj (@srbharadwaj)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
