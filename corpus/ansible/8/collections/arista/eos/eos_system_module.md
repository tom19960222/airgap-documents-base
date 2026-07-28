---
collection: ansible
version: "8"
title: "arista.eos.eos_system module – Manage the system attributes on Arista EOS devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/arista/eos/eos_system_module.html
fetched_at: 2026-07-28T01:11:16+00:00
---
# arista.eos.eos_system module – Manage the system attributes on Arista EOS devices

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/ui/repo/published/arista/eos/) (version 6.2.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_system`.

New in arista.eos 1.0.0

- [Synopsis](eos_system_module.md#synopsis)
- [Parameters](eos_system_module.md#parameters)
- [Notes](eos_system_module.md#notes)
- [Examples](eos_system_module.md#examples)
- [Return Values](eos_system_module.md#return-values)

## [Synopsis](eos_system_module.md#id1)

- This module provides declarative management of node system attributes on Arista EOS devices. It provides an option to configure host system parameters or remove those parameters from the device active configuration.

Aliases: system

## [Parameters](eos_system_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **domain_list**  aliases: domain_search  list / elements=string | Provides the list of domain suffixes to append to the hostname for the purpose of doing name resolution. This argument accepts a list of names and will be reconciled with the current active configuration on the running node. |
| **domain_name**  string | Configure the IP domain name on the remote device to the provided value. Value should be in the dotted name form and will be appended to the `hostname` to create a fully-qualified domain name. |
| **hostname**  string | Configure the device hostname parameter. This option takes an ASCII string value. |
| **lookup_source**  list / elements=any | Provides one or more source interfaces to use for performing DNS lookups. The interface provided in `lookup_source` can only exist in a single VRF. This argument accepts either a list of interface names or a list of hashes that configure the interface name and VRF name. See examples. |
| **name_servers**  list / elements=string | List of DNS name servers by IP address to use to perform name resolution lookups. This argument accepts either a list of DNS servers or a list of hashes that configure the name server and VRF name. See examples. |
| **state**  string | State of the configuration values in the device’s current active configuration. When set to *present*, the values should be configured in the device active configuration and when set to *absent* the values should not be in the device active configuration  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](eos_system_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F

## [Examples](eos_system_module.md#id4)

```yaml+jinja
- name: configure hostname and domain-name
  arista.eos.eos_system:
    hostname: eos01
    domain_name: test.example.com

- name: remove configuration
  arista.eos.eos_system:
    state: absent

- name: configure DNS lookup sources
  arista.eos.eos_system:
    lookup_source: Management1

- name: configure DNS lookup sources with VRF support
  arista.eos.eos_system:
    lookup_source:
      - interface: Management1
        vrf: mgmt
      - interface: Ethernet1
        vrf: myvrf

- name: configure name servers
  arista.eos.eos_system:
    name_servers:
      - 8.8.8.8
      - 8.8.4.4

- name: configure name servers with VRF support
  arista.eos.eos_system:
    name_servers:
      - {server: 8.8.8.8, vrf: mgmt}
      - {server: 8.8.4.4, vrf: mgmt}
```

## [Return Values](eos_system_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["hostname eos01", "dns domain test.example.com"]` |
| **session_name**  string | The EOS config session name used to load the configuration  **Returned:** changed  **Sample:** `"ansible_1479315771"` |

### Authors

- Peter Sprygada (@privateip)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/arista.eos)
