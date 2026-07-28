---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_ntp_options module – Manages NTP options."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_ntp_options_module.html
fetched_at: 2026-07-28T01:38:56+00:00
---
# cisco.nxos.nxos_ntp_options module – Manages NTP options.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_ntp_options`.

New in cisco.nxos 1.0.0

- [DEPRECATED](nxos_ntp_options_module.md#deprecated)
- [Synopsis](nxos_ntp_options_module.md#synopsis)
- [Parameters](nxos_ntp_options_module.md#parameters)
- [Notes](nxos_ntp_options_module.md#notes)
- [Examples](nxos_ntp_options_module.md#examples)
- [Return Values](nxos_ntp_options_module.md#return-values)
- [Status](nxos_ntp_options_module.md#status)

## [DEPRECATED](nxos_ntp_options_module.md#id1)

Removed in:
:   major release after 2024-01-01

Why:
:   Updated module released with more functionality.

Alternative:
:   nxos_ntp_global

## [Synopsis](nxos_ntp_options_module.md#id2)

- Manages NTP options, e.g. authoritative server and logging.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: ntp_options

## [Parameters](nxos_ntp_options_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **logging**  boolean | Sets whether NTP logging is enabled on the device.  **Choices:**   - `false` - `true` |
| **master**  boolean | Sets whether the device is an authoritative NTP server.  **Choices:**   - `false` - `true` |
| **state**  string | Manage the state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **stratum**  string | If `master=true`, an optional stratum can be supplied (1-15). The device default is 8. |

## [Notes](nxos_ntp_options_module.md#id4)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Limited Support for Cisco MDS
> - When `state=absent`, master and logging will be set to False and stratum will be removed as well
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_ntp_options_module.md#id5)

```yaml+jinja
# Basic NTP options configuration
- cisco.nxos.nxos_ntp_options:
    master: true
    stratum: 12
    logging: false
    host: '{{ inventory_hostname }}'
    username: '{{ un }}'
    password: '{{ pwd }}'
```

## [Return Values](nxos_ntp_options_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **updates**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["no ntp logging", "ntp master 12"]` |

## [Status](nxos_ntp_options_module.md#id7)

- This module will be removed in a major release after 2024-01-01.
  *[deprecated]*
- For more information see [DEPRECATED](nxos_ntp_options_module.md#deprecated).

### Authors

- Jason Edelman (@jedelman8)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
