---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_ntp_auth module – Manages NTP authentication."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_ntp_auth_module.html
fetched_at: 2026-07-28T01:38:54+00:00
---
# cisco.nxos.nxos_ntp_auth module – Manages NTP authentication.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_ntp_auth`.

New in cisco.nxos 1.0.0

- [DEPRECATED](nxos_ntp_auth_module.md#deprecated)
- [Synopsis](nxos_ntp_auth_module.md#synopsis)
- [Parameters](nxos_ntp_auth_module.md#parameters)
- [Notes](nxos_ntp_auth_module.md#notes)
- [Examples](nxos_ntp_auth_module.md#examples)
- [Return Values](nxos_ntp_auth_module.md#return-values)
- [Status](nxos_ntp_auth_module.md#status)

## [DEPRECATED](nxos_ntp_auth_module.md#id1)

Removed in:
:   major release after 2024-01-01

Why:
:   Updated module released with more functionality.

Alternative:
:   nxos_ntp_global

## [Synopsis](nxos_ntp_auth_module.md#id2)

- Manages NTP authentication.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: ntp_auth

## [Parameters](nxos_ntp_auth_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_type**  string | Whether the given md5string is in cleartext or has been encrypted. If in cleartext, the device will encrypt it before storing it.  **Choices:**   - `"text"` ← (default) - `"encrypt"` |
| **authentication**  string | Turns NTP authentication on or off.  **Choices:**   - `"on"` - `"off"` |
| **key_id**  string | Authentication key identifier (numeric). |
| **md5string**  string | MD5 String. |
| **state**  string | Manage the state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **trusted_key**  string | Whether the given key is required to be supplied by a time source for the device to synchronize to the time source.  **Choices:**   - `"false"` ← (default) - `"true"` |

## [Notes](nxos_ntp_auth_module.md#id4)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Limited Support for Cisco MDS
> - If `state=absent`, the module will remove the given key configuration if it exists.
> - If `state=absent` and `authentication=on`, authentication will be turned off.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_ntp_auth_module.md#id5)

```yaml+jinja
# Basic NTP authentication configuration
- cisco.nxos.nxos_ntp_auth:
    key_id: 32
    md5string: hello
    auth_type: text
```

## [Return Values](nxos_ntp_auth_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["ntp authentication-key 32 md5 helloWorld 0", "ntp trusted-key 32"]` |

## [Status](nxos_ntp_auth_module.md#id7)

- This module will be removed in a major release after 2024-01-01.
  *[deprecated]*
- For more information see [DEPRECATED](nxos_ntp_auth_module.md#deprecated).

### Authors

- Jason Edelman (@jedelman8)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
