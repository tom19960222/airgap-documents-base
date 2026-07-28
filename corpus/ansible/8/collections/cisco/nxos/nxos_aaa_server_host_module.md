---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_aaa_server_host module – Manages AAA server host-specific configuration."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_aaa_server_host_module.html
fetched_at: 2026-07-28T01:38:26+00:00
---
# cisco.nxos.nxos_aaa_server_host module – Manages AAA server host-specific configuration.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_aaa_server_host`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_aaa_server_host_module.md#synopsis)
- [Parameters](nxos_aaa_server_host_module.md#parameters)
- [Notes](nxos_aaa_server_host_module.md#notes)
- [Examples](nxos_aaa_server_host_module.md#examples)
- [Return Values](nxos_aaa_server_host_module.md#return-values)

## [Synopsis](nxos_aaa_server_host_module.md#id1)

- Manages AAA server host-specific configuration.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: aaa_server_host

## [Parameters](nxos_aaa_server_host_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **acct_port**  string | Alternate UDP port for RADIUS accounting or keyword ‘default’. |
| **address**  string / required | Address or name of the radius or tacacs host. |
| **auth_port**  string | Alternate UDP port for RADIUS authentication or keyword ‘default’. |
| **encrypt_type**  string | The state of encryption applied to the entered key. O for clear text, 7 for encrypted. Type-6 encryption is not supported.  **Choices:**   - `"0"` - `"7"` |
| **host_timeout**  string | Timeout period for specified host, in seconds or keyword ‘default. Range is 1-60. |
| **key**  string | Shared secret for the specified host or keyword ‘default’. |
| **server_type**  string / required | The server type is either radius or tacacs.  **Choices:**   - `"radius"` - `"tacacs"` |
| **state**  string | Manage the state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tacacs_port**  string | Alternate TCP port TACACS Server or keyword ‘default’. |

## [Notes](nxos_aaa_server_host_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Limited Support for Cisco MDS
> - Changes to the host key (shared secret) are not idempotent for type 0.
> - If `state=absent` removes the whole host configuration.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_aaa_server_host_module.md#id4)

```yaml+jinja
# Radius Server Host Basic settings
- name: Radius Server Host Basic settings
  cisco.nxos.nxos_aaa_server_host:
    state: present
    server_type: radius
    address: 1.2.3.4
    acct_port: 2084
    host_timeout: 10

# Radius Server Host Key Configuration
- name: Radius Server Host Key Configuration
  cisco.nxos.nxos_aaa_server_host:
    state: present
    server_type: radius
    address: 1.2.3.4
    key: hello
    encrypt_type: 7

# TACACS Server Host Configuration
- name: Tacacs Server Host Configuration
  cisco.nxos.nxos_aaa_server_host:
    state: present
    server_type: tacacs
    tacacs_port: 89
    host_timeout: 10
    address: 5.6.7.8
```

## [Return Values](nxos_aaa_server_host_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of configuration after module execution  **Returned:** always  **Sample:** `{"address": "1.2.3.4", "auth_port": "2084", "host_timeout": "10", "server_type": "radius"}` |
| **existing**  dictionary | k/v pairs of existing configuration  **Returned:** always  **Sample:** `{}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"address": "1.2.3.4", "auth_port": "2084", "host_timeout": "10", "server_type": "radius"}` |
| **updates**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["radius-server host 1.2.3.4 auth-port 2084 timeout 10"]` |

### Authors

- Jason Edelman (@jedelman8)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
