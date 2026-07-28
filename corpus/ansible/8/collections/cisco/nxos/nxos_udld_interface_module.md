---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_udld_interface module – Manages UDLD interface configuration params."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_udld_interface_module.html
fetched_at: 2026-07-28T01:39:16+00:00
---
# cisco.nxos.nxos_udld_interface module – Manages UDLD interface configuration params.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_udld_interface`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_udld_interface_module.md#synopsis)
- [Parameters](nxos_udld_interface_module.md#parameters)
- [Notes](nxos_udld_interface_module.md#notes)
- [Examples](nxos_udld_interface_module.md#examples)
- [Return Values](nxos_udld_interface_module.md#return-values)

## [Synopsis](nxos_udld_interface_module.md#id1)

- Manages UDLD interface configuration params.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: udld_interface

## [Parameters](nxos_udld_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **interface**  string / required | FULL name of the interface, i.e. Ethernet1/1- |
| **mode**  string / required | Manages UDLD mode for an interface.  **Choices:**   - `"enabled"` - `"disabled"` - `"aggressive"` |
| **state**  string | Manage the state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](nxos_udld_interface_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - Feature UDLD must be enabled on the device to use this module.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_udld_interface_module.md#id4)

```yaml+jinja
# ensure Ethernet1/1 is configured to be in aggressive mode
- cisco.nxos.nxos_udld_interface:
    interface: Ethernet1/1
    mode: aggressive
    state: present
    host: '{{ inventory_hostname }}'
    username: '{{ un }}'
    password: '{{ pwd }}'

# Remove the aggressive config only if it's currently in aggressive mode and then disable udld (switch default)
- cisco.nxos.nxos_udld_interface:
    interface: Ethernet1/1
    mode: aggressive
    state: absent
    host: '{{ inventory_hostname }}'
    username: '{{ un }}'
    password: '{{ pwd }}'

# ensure Ethernet1/1 has aggressive mode enabled
- cisco.nxos.nxos_udld_interface:
    interface: Ethernet1/1
    mode: enabled
    host: '{{ inventory_hostname }}'
    username: '{{ un }}'
    password: '{{ pwd }}'
```

## [Return Values](nxos_udld_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of configuration after module execution  **Returned:** always  **Sample:** `{"mode": "enabled"}` |
| **existing**  dictionary | k/v pairs of existing configuration  **Returned:** always  **Sample:** `{"mode": "aggressive"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"mode": "enabled"}` |
| **updates**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["interface ethernet1/33", "no udld aggressive ; no udld disable"]` |

### Authors

- Jason Edelman (@jedelman8)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
