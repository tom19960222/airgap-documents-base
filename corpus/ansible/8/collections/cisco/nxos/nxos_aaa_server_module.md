---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_aaa_server module – Manages AAA server global configuration."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_aaa_server_module.html
fetched_at: 2026-07-28T01:38:25+00:00
---
# cisco.nxos.nxos_aaa_server module – Manages AAA server global configuration.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_aaa_server`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_aaa_server_module.md#synopsis)
- [Parameters](nxos_aaa_server_module.md#parameters)
- [Notes](nxos_aaa_server_module.md#notes)
- [Examples](nxos_aaa_server_module.md#examples)
- [Return Values](nxos_aaa_server_module.md#return-values)

## [Synopsis](nxos_aaa_server_module.md#id1)

- Manages AAA server global configuration

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: aaa_server

## [Parameters](nxos_aaa_server_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **deadtime**  string | Duration for which a non-reachable AAA server is skipped, in minutes or keyword ‘default. Range is 1-1440. Device default is 0. |
| **directed_request**  string | Enables direct authentication requests to AAA server or keyword ‘default’ Device default is disabled.  **Choices:**   - `"enabled"` - `"disabled"` - `"default"` |
| **encrypt_type**  string | The state of encryption applied to the entered global key. O clear text, 7 encrypted. Type-6 encryption is not supported.  **Choices:**   - `"0"` - `"7"` |
| **global_key**  string | Global AAA shared secret or keyword ‘default’. |
| **server_timeout**  string | Global AAA server timeout period, in seconds or keyword ‘default. Range is 1-60. Device default is 5. |
| **server_type**  string / required | The server type is either radius or tacacs.  **Choices:**   - `"radius"` - `"tacacs"` |
| **state**  string | Manage the state of the resource.  **Choices:**   - `"present"` ← (default) - `"default"` |

## [Notes](nxos_aaa_server_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Limited Support for Cisco MDS
> - The server_type parameter is always required.
> - If encrypt_type is not supplied, the global AAA server key will be stored as encrypted (type 7).
> - Changes to the global AAA server key with encrypt_type=0 are not idempotent.
> - state=default will set the supplied parameters to their default values. The parameters that you want to default must also be set to default. If global_key=default, the global key will be removed.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_aaa_server_module.md#id4)

```yaml+jinja
# Radius Server Basic settings
- name: Radius Server Basic settings
  cisco.nxos.nxos_aaa_server:
    server_type: radius
    server_timeout: 9
    deadtime: 20
    directed_request: enabled

# Tacacs Server Basic settings
- name: Tacacs Server Basic settings
  cisco.nxos.nxos_aaa_server:
    server_type: tacacs
    server_timeout: 8
    deadtime: 19
    directed_request: disabled

# Setting Global Key
- name: AAA Server Global Key
  cisco.nxos.nxos_aaa_server:
    server_type: radius
    global_key: test_key
```

## [Return Values](nxos_aaa_server_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["radius-server deadtime 22", "radius-server timeout 11", "radius-server directed-request"]` |

### Authors

- Jason Edelman (@jedelman8)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
