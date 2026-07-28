---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_gir_profile_management module – Create a maintenance-mode or normal-mode profile for GIR."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_gir_profile_management_module.html
fetched_at: 2026-07-28T01:38:41+00:00
---
# cisco.nxos.nxos_gir_profile_management module – Create a maintenance-mode or normal-mode profile for GIR.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_gir_profile_management`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_gir_profile_management_module.md#synopsis)
- [Parameters](nxos_gir_profile_management_module.md#parameters)
- [Notes](nxos_gir_profile_management_module.md#notes)
- [Examples](nxos_gir_profile_management_module.md#examples)
- [Return Values](nxos_gir_profile_management_module.md#return-values)

## [Synopsis](nxos_gir_profile_management_module.md#id1)

- Manage a maintenance-mode or normal-mode profile with configuration commands that can be applied during graceful removal or graceful insertion.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: gir_profile_management

## [Parameters](nxos_gir_profile_management_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **commands**  list / elements=string | List of commands to be included into the profile. |
| **mode**  string / required | Configure the profile as Maintenance or Normal mode.  **Choices:**   - `"maintenance"` - `"normal"` |
| **state**  string | Specify desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](nxos_gir_profile_management_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - `state=absent` removes the whole profile.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_gir_profile_management_module.md#id4)

```yaml+jinja
# Create a maintenance-mode profile
- cisco.nxos.nxos_gir_profile_management:
    mode: maintenance
    commands:
    - router eigrp 11
    - isolate

# Remove the maintenance-mode profile
- cisco.nxos.nxos_gir_profile_management:
    mode: maintenance
    state: absent
```

## [Return Values](nxos_gir_profile_management_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  list / elements=string | list of profile entries after module execution.  **Returned:** verbose mode  **Sample:** `["router bgp 65535", "isolate", "router eigrp 10", "isolate", "diagnostic bootup level complete", "router eigrp 11", "isolate"]` |
| **existing**  list / elements=string | list of existing profile commands.  **Returned:** verbose mode  **Sample:** `["router bgp 65535", "isolate", "router eigrp 10", "isolate", "diagnostic bootup level complete"]` |
| **proposed**  list / elements=string | list of commands passed into module.  **Returned:** verbose mode  **Sample:** `["router eigrp 11", "isolate"]` |
| **updates**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["configure maintenance profile maintenance-mode", "router eigrp 11", "isolate"]` |

### Authors

- Gabriele Gerbino (@GGabriele)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
