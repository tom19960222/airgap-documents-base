---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_udld module – Manages UDLD global configuration params."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_udld_module.html
fetched_at: 2026-07-28T01:39:15+00:00
---
# cisco.nxos.nxos_udld module – Manages UDLD global configuration params.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_udld`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_udld_module.md#synopsis)
- [Parameters](nxos_udld_module.md#parameters)
- [Notes](nxos_udld_module.md#notes)
- [Examples](nxos_udld_module.md#examples)
- [Return Values](nxos_udld_module.md#return-values)

## [Synopsis](nxos_udld_module.md#id1)

- Manages UDLD global configuration params.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: udld

## [Parameters](nxos_udld_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggressive**  string | Toggles aggressive mode.  **Choices:**   - `"enabled"` - `"disabled"` |
| **msg_time**  string | Message time in seconds for UDLD packets or keyword ‘default’. |
| **reset**  boolean | Ability to reset all ports shut down by UDLD. ‘state’ parameter cannot be ‘absent’ when this is present.  **Choices:**   - `false` - `true` |
| **state**  string | Manage the state of the resource. When set to ‘absent’, aggressive and msg_time are set to their default values.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](nxos_udld_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - Module will fail if the udld feature has not been previously enabled.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_udld_module.md#id4)

```yaml+jinja
# ensure udld aggressive mode is globally disabled and se global message interval is 20
- cisco.nxos.nxos_udld:
    aggressive: disabled
    msg_time: 20
    host: '{{ inventory_hostname }}'
    username: '{{ un }}'
    password: '{{ pwd }}'

# Ensure agg mode is globally enabled and msg time is 15
- cisco.nxos.nxos_udld:
    aggressive: enabled
    msg_time: 15
    host: '{{ inventory_hostname }}'
    username: '{{ un }}'
    password: '{{ pwd }}'
```

## [Return Values](nxos_udld_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of udld configuration after module execution  **Returned:** always  **Sample:** `{"aggressive": "enabled", "msg_time": "40"}` |
| **existing**  dictionary | k/v pairs of existing udld configuration  **Returned:** always  **Sample:** `{"aggressive": "disabled", "msg_time": "15"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"aggressive": "enabled", "msg_time": "40"}` |
| **updates**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["udld message-time 40", "udld aggressive"]` |

### Authors

- Jason Edelman (@jedelman8)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
