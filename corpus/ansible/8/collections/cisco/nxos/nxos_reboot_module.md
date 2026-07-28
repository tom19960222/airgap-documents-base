---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_reboot module – Reboot a network device."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_reboot_module.html
fetched_at: 2026-07-28T01:39:04+00:00
---
# cisco.nxos.nxos_reboot module – Reboot a network device.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_reboot`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_reboot_module.md#synopsis)
- [Parameters](nxos_reboot_module.md#parameters)
- [Notes](nxos_reboot_module.md#notes)
- [Examples](nxos_reboot_module.md#examples)
- [Return Values](nxos_reboot_module.md#return-values)

## [Synopsis](nxos_reboot_module.md#id1)

- Reboot a network device.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: reboot

## [Parameters](nxos_reboot_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **confirm**  boolean | Safeguard boolean. Set to true if you’re sure you want to reboot.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](nxos_reboot_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Tested against Cisco MDS NX-OS 9.2(1)
> - The module will fail due to timeout issues, but the reboot will be performed anyway.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_reboot_module.md#id4)

```yaml+jinja
- cisco.nxos.nxos_reboot:
    confirm: true
```

## [Return Values](nxos_reboot_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **rebooted**  boolean | Whether the device was instructed to reboot.  **Returned:** success  **Sample:** `true` |

### Authors

- Jason Edelman (@jedelman8)
- Gabriele Gerbino (@GGabriele)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
