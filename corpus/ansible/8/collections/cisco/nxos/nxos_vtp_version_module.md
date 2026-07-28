---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_vtp_version module – Manages VTP version configuration."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_vtp_version_module.html
fetched_at: 2026-07-28T01:39:24+00:00
---
# cisco.nxos.nxos_vtp_version module – Manages VTP version configuration.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_vtp_version`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_vtp_version_module.md#synopsis)
- [Parameters](nxos_vtp_version_module.md#parameters)
- [Notes](nxos_vtp_version_module.md#notes)
- [Examples](nxos_vtp_version_module.md#examples)
- [Return Values](nxos_vtp_version_module.md#return-values)

## [Synopsis](nxos_vtp_version_module.md#id1)

- Manages VTP version configuration.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: vtp_version

## [Parameters](nxos_vtp_version_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **version**  string / required | VTP version number.  **Choices:**   - `"1"` - `"2"` |

## [Notes](nxos_vtp_version_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - VTP feature must be active on the device to use this module.
> - This module is used to manage only VTP version.
> - Use this in combination with [cisco.nxos.nxos_vtp_password](nxos_vtp_password_module.md#ansible-collections-cisco-nxos-nxos-vtp-password-module) and [cisco.nxos.nxos_vtp_version](nxos_vtp_version_module.md#ansible-collections-cisco-nxos-nxos-vtp-version-module) to fully manage VTP operations.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_vtp_version_module.md#id4)

```yaml+jinja
# ENSURE VTP VERSION IS 2
- cisco.nxos.nxos_vtp_version:
    version: 2
    host: '{{ inventory_hostname }}'
    username: '{{ un }}'
    password: '{{ pwd }}'
```

## [Return Values](nxos_vtp_version_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of vtp after module execution  **Returned:** always  **Sample:** `{"domain": "testing", "version": "2", "vtp_password": "password"}` |
| **existing**  dictionary | k/v pairs of existing vtp  **Returned:** always  **Sample:** `{"domain": "testing", "version": "1", "vtp_password": "password"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"version": "2"}` |
| **updates**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["vtp version 2"]` |

### Authors

- Gabriele Gerbino (@GGabriele)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
