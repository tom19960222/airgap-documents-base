---
collection: ansible
version: "6"
title: "community.network.cnos_system module – Manage the system attributes on Lenovo CNOS devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/cnos_system_module.html
fetched_at: 2026-07-27T17:18:17+00:00
---
# community.network.cnos_system module – Manage the system attributes on Lenovo CNOS devices

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.cnos_system`.

- [Synopsis](cnos_system_module.md#synopsis)
- [Parameters](cnos_system_module.md#parameters)
- [Examples](cnos_system_module.md#examples)
- [Return Values](cnos_system_module.md#return-values)

## [Synopsis](cnos_system_module.md#id1)

- This module provides declarative management of node system attributes on Lenovo CNOS devices. It provides an option to configure host system parameters or remove those parameters from the device active configuration.

## [Parameters](cnos_system_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **domain_name**  string | Configures the default domain name suffix to be used when referencing this node by its FQDN. This argument accepts either a list of domain names or a list of dicts that configure the domain name and VRF name or keyword ‘default’. See examples. |
| **domain_search**  string | Configures a list of domain name suffixes to search when performing DNS name resolution. This argument accepts either a list of domain names or a list of dicts that configure the domain name and VRF name or keyword ‘default’. See examples. |
| **hostname**  string | Configure the device hostname parameter. This option takes an ASCII string value or keyword ‘default’ |
| **lookup_enabled**  boolean | Administrative control for enabling or disabling DNS lookups. When this argument is set to True, lookups are performed and when it is set to False, lookups are not performed.  Choices:   - `false` - `true` |
| **lookup_source**  string | Provides one or more source interfaces to use for performing DNS lookups. The interface must be a valid interface configured. on the device. |
| **name_servers**  string | List of DNS name servers by IP address to use to perform name resolution lookups. This argument accepts either a list of DNS servers or a list of hashes that configure the name server and VRF name or keyword ‘default’. See examples. |
| **state**  string | State of the configuration values in the device’s current active configuration. When set to *present*, the values should be configured in the device active configuration and when set to *absent* the values should not be in the device active configuration  Choices:   - `"present"` ← (default) - `"absent"` |

## [Examples](cnos_system_module.md#id3)

```yaml+jinja
- name: Configure hostname and domain-name
  community.network.cnos_system:
    hostname: cnos01
    domain_name: test.example.com

- name: Remove configuration
  community.network.cnos_system:
    state: absent

- name: Configure name servers
  community.network.cnos_system:
    name_servers:
      - 8.8.8.8
      - 8.8.4.4

- name: Configure DNS Lookup sources
  community.network.cnos_system:
    lookup_source: MgmtEth0/0/CPU0/0
    lookup_enabled: yes

- name: Configure name servers with VRF support
  nxos_system:
    name_servers:
      - { server: 8.8.8.8, vrf: mgmt }
      - { server: 8.8.4.4, vrf: mgmt }
```

## [Return Values](cnos_system_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always  Sample: `["hostname cnos01", "ip domain-name test.example.com vrf default"]` |

### Authors

- Anil Kumar Muraleedharan (@amuraleedhar)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
