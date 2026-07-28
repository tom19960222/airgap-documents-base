---
collection: ansible
version: "6"
title: "ansible.netcommon.net_system module – (deprecated, removed after 2022-06-01) Manage the system attributes on network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/netcommon/net_system_module.html
fetched_at: 2026-07-27T16:44:32+00:00
---
# ansible.netcommon.net_system module – (deprecated, removed after 2022-06-01) Manage the system attributes on network devices

> **Note:**
>
> This module is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ansible/netcommon) (version 3.1.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.net_system`.

New in ansible.netcommon 1.0.0

- [DEPRECATED](net_system_module.md#deprecated)
- [Synopsis](net_system_module.md#synopsis)
- [Parameters](net_system_module.md#parameters)
- [Notes](net_system_module.md#notes)
- [Examples](net_system_module.md#examples)
- [Return Values](net_system_module.md#return-values)
- [Status](net_system_module.md#status)

## [DEPRECATED](net_system_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality

Alternative:
:   Use platform-specific “[netos]_system” module

## [Synopsis](net_system_module.md#id2)

- This module provides declarative management of node system attributes on network devices. It provides an option to configure host system parameters or remove those parameters from the device active configuration.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](net_system_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **domain_name**  string | Configure the IP domain name on the remote device to the provided value. Value should be in the dotted name form and will be appended to the `hostname` to create a fully-qualified domain name. |
| **domain_search**  string | Provides the list of domain suffixes to append to the hostname for the purpose of doing name resolution. This argument accepts a name or list of names and will be reconciled with the current active configuration on the running node. |
| **hostname**  string | Configure the device hostname parameter. This option takes an ASCII string value. |
| **lookup_source**  string | Provides one or more source interfaces to use for performing DNS lookups. The interface provided in `lookup_source` must be a valid interface configured on the device. |
| **name_servers**  string | List of DNS name servers by IP address to use to perform name resolution lookups. This argument accepts either a list of DNS servers See examples. |
| **state**  string | State of the configuration values in the device’s current active configuration. When set to *present*, the values should be configured in the device active configuration and when set to *absent* the values should not be in the device active configuration  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](net_system_module.md#id4)

> **Note:**
>
> - This module is supported on `ansible_network_os` network platforms. See the :ref:`Network Platform Options <platform_options>` for details.

## [Examples](net_system_module.md#id5)

```yaml+jinja
- name: configure hostname and domain name
  ansible.netcommon.net_system:
    hostname: ios01
    domain_name: test.example.com
    domain_search:
    - ansible.com
    - redhat.com
    - cisco.com

- name: domain search on single domain
  ansible.netcommon.net_system:
    domain_search: ansible.com

- name: remove configuration
  ansible.netcommon.net_system:
    state: absent

- name: configure DNS lookup sources
  ansible.netcommon.net_system:
    lookup_source: MgmtEth0/0/CPU0/0

- name: configure name servers
  ansible.netcommon.net_system:
    name_servers:
    - 8.8.8.8
    - 8.8.4.4
```

## [Return Values](net_system_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always, except for the platforms that use Netconf transport to manage the device.  Sample: `["hostname ios01", "ip domain name test.example.com"]` |

## [Status](net_system_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](net_system_module.md#deprecated).

### Authors

- Ricardo Carrillo Cruz (@rcarrillocruz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
