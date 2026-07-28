---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_system module – Manage the system attributes on Cisco NXOS devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_system_module.html
fetched_at: 2026-07-28T01:39:14+00:00
---
# cisco.nxos.nxos_system module – Manage the system attributes on Cisco NXOS devices

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
> To use it in a playbook, specify: `cisco.nxos.nxos_system`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_system_module.md#synopsis)
- [Parameters](nxos_system_module.md#parameters)
- [Notes](nxos_system_module.md#notes)
- [Examples](nxos_system_module.md#examples)
- [Return Values](nxos_system_module.md#return-values)

## [Synopsis](nxos_system_module.md#id1)

- This module provides declarative management of node system attributes on Cisco NXOS devices. It provides an option to configure host system parameters or remove those parameters from the device active configuration.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: system

## [Parameters](nxos_system_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **domain_lookup**  boolean | Enables or disables the DNS lookup feature in Cisco NXOS. This argument accepts boolean values. When enabled, the system will try to resolve hostnames using DNS and when disabled, hostnames will not be resolved.  **Choices:**   - `false` - `true` |
| **domain_name**  list / elements=any | Configures the default domain name suffix to be used when referencing this node by its FQDN. This argument accepts either a list of domain names or a list of dicts that configure the domain name and VRF name or keyword ‘default’. See examples. |
| **domain_search**  list / elements=any | Configures a list of domain name suffixes to search when performing DNS name resolution. This argument accepts either a list of domain names or a list of dicts that configure the domain name and VRF name or keyword ‘default’. See examples. |
| **hostname**  string | Configure the device hostname parameter. This option takes an ASCII string value or keyword ‘default’ |
| **name_servers**  list / elements=any | List of DNS name servers by IP address to use to perform name resolution lookups. This argument accepts either a list of DNS servers or a list of hashes that configure the name server and VRF name or keyword ‘default’. See examples. |
| **state**  string | State of the configuration values in the device’s current active configuration. When set to *present*, the values should be configured in the device active configuration and when set to *absent* the values should not be in the device active configuration  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **system_mtu**  string | Specifies the mtu, must be an integer or keyword ‘default’. |

## [Notes](nxos_system_module.md#id3)

> **Note:**
>
> - Unsupported for Cisco MDS
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_system_module.md#id4)

```yaml+jinja
- name: configure hostname and domain-name
  cisco.nxos.nxos_system:
    hostname: nxos01
    domain_name: test.example.com

- name: remove configuration
  cisco.nxos.nxos_system:
    state: absent

- name: configure name servers
  cisco.nxos.nxos_system:
    name_servers:
    - 8.8.8.8
    - 8.8.4.4

- name: configure name servers with VRF support
  cisco.nxos.nxos_system:
    name_servers:
    - {server: 8.8.8.8, vrf: mgmt}
    - {server: 8.8.4.4, vrf: mgmt}
```

## [Return Values](nxos_system_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["hostname nxos01", "ip domain-name test.example.com"]` |

### Authors

- Peter Sprygada (@privateip)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
