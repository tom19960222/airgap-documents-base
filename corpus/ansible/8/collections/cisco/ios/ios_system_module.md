---
collection: ansible
version: "8"
title: "cisco.ios.ios_system module – Module to manage the system attributes."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ios/ios_system_module.html
fetched_at: 2026-07-28T01:26:29+00:00
---
# cisco.ios.ios_system module – Module to manage the system attributes.

> **Note:**
>
> This module is part of the [cisco.ios collection](https://galaxy.ansible.com/ui/repo/published/cisco/ios/) (version 4.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ios`.
>
> To use it in a playbook, specify: `cisco.ios.ios_system`.

New in cisco.ios 1.0.0

- [Synopsis](ios_system_module.md#synopsis)
- [Parameters](ios_system_module.md#parameters)
- [Notes](ios_system_module.md#notes)
- [Examples](ios_system_module.md#examples)
- [Return Values](ios_system_module.md#return-values)

## [Synopsis](ios_system_module.md#id1)

- This module provides declarative management of node system attributes on Cisco IOS devices. It provides an option to configure host system parameters or remove those parameters from the device active configuration.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: system

## [Parameters](ios_system_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **domain_name**  list / elements=any | Configure the IP domain name on the remote device to the provided value. Value should be in the dotted name form and will be appended to the `hostname` to create a fully-qualified domain name. |
| **domain_search**  list / elements=any | Provides the list of domain suffixes to append to the hostname for the purpose of doing name resolution. This argument accepts a list of names and will be reconciled with the current active configuration on the running node. |
| **hostname**  string | Configure the device hostname parameter. This option takes an ASCII string value. |
| **lookup_enabled**  boolean | Administrative control for enabling or disabling DNS lookups. When this argument is set to True, lookups are performed and when it is set to False, lookups are not performed.  **Choices:**   - `false` - `true` |
| **lookup_source**  string | Provides one or more source interfaces to use for performing DNS lookups. The interface provided in `lookup_source` must be a valid interface configured on the device. |
| **name_servers**  list / elements=any | List of DNS name servers by IP address to use to perform name resolution lookups. This argument accepts either a list of DNS servers See examples. |
| **state**  string | State of the configuration values in the device’s current active configuration. When set to *present*, the values should be configured in the device active configuration and when set to *absent* the values should not be in the device active configuration  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](ios_system_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSXE Version 17.3 on CML.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](ios_system_module.md#id4)

```yaml+jinja
- name: Configure hostname and domain name
  cisco.ios.ios_system:
    hostname: ios01
    domain_name: test.example.com
    domain_search:
      - ansible.com
      - redhat.com
      - cisco.com

- name: Remove configuration
  cisco.ios.ios_system:
    state: absent

- name: Configure DNS lookup sources
  cisco.ios.ios_system:
    lookup_source: MgmtEth0/0/CPU0/0
    lookup_enabled: true

- name: Configure name servers
  cisco.ios.ios_system:
    name_servers:
      - 8.8.8.8
      - 8.8.4.4
```

## [Return Values](ios_system_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["hostname ios01", "ip domain name test.example.com"]` |

### Authors

- Peter Sprygada (@privateip)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
