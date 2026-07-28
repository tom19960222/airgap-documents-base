---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_rollback module – Set a checkpoint or rollback to a checkpoint."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_rollback_module.html
fetched_at: 2026-07-28T01:39:05+00:00
---
# cisco.nxos.nxos_rollback module – Set a checkpoint or rollback to a checkpoint.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_rollback`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_rollback_module.md#synopsis)
- [Parameters](nxos_rollback_module.md#parameters)
- [Notes](nxos_rollback_module.md#notes)
- [Examples](nxos_rollback_module.md#examples)
- [Return Values](nxos_rollback_module.md#return-values)

## [Synopsis](nxos_rollback_module.md#id1)

- This module offers the ability to set a configuration checkpoint file or rollback to a configuration checkpoint file on Cisco NXOS switches.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: rollback

## [Parameters](nxos_rollback_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **checkpoint_file**  string | Name of checkpoint file to create. Mutually exclusive with rollback_to. |
| **rollback_to**  string | Name of checkpoint file to rollback to. Mutually exclusive with checkpoint_file. |

## [Notes](nxos_rollback_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - Sometimes `transport=nxapi` may cause a timeout error.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_rollback_module.md#id4)

```yaml+jinja
- cisco.nxos.nxos_rollback:
    checkpoint_file: backup.cfg
    username: '{{ un }}'
    password: '{{ pwd }}'
    host: '{{ inventory_hostname }}'
- cisco.nxos.nxos_rollback:
    rollback_to: backup.cfg
    username: '{{ un }}'
    password: '{{ pwd }}'
    host: '{{ inventory_hostname }}'
```

## [Return Values](nxos_rollback_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **filename**  string | The filename of the checkpoint/rollback file.  **Returned:** success  **Sample:** `"backup.cfg"` |
| **status**  string | Which operation took place and whether it was successful.  **Returned:** success  **Sample:** `"rollback executed"` |

### Authors

- Jason Edelman (@jedelman8)
- Gabriele Gerbino (@GGabriele)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
