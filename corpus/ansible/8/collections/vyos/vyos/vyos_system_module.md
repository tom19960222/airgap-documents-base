---
collection: ansible
version: "8"
title: "vyos.vyos.vyos_system module – Run `set system` commands on VyOS devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vyos/vyos/vyos_system_module.html
fetched_at: 2026-07-28T02:59:27+00:00
---
# vyos.vyos.vyos_system module – Run `set system` commands on VyOS devices

> **Note:**
>
> This module is part of the [vyos.vyos collection](https://galaxy.ansible.com/ui/repo/published/vyos/vyos/) (version 4.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vyos.vyos`.
>
> To use it in a playbook, specify: `vyos.vyos.vyos_system`.

New in vyos.vyos 1.0.0

- [Synopsis](vyos_system_module.md#synopsis)
- [Parameters](vyos_system_module.md#parameters)
- [Notes](vyos_system_module.md#notes)
- [Examples](vyos_system_module.md#examples)
- [Return Values](vyos_system_module.md#return-values)

## [Synopsis](vyos_system_module.md#id1)

- Runs one or more commands on remote devices running VyOS. This module can also be introspected to validate key parameters before returning successfully.

Aliases: system

## [Parameters](vyos_system_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **domain_name**  string | The new domain name to apply to the device. |
| **domain_search**  list / elements=string | A list of domain names to search. Mutually exclusive with *name_server* |
| **host_name**  string | Configure the device hostname parameter. This option takes an ASCII string value. |
| **name_server**  aliases: name_servers  list / elements=string | A list of name servers to use with the device. Mutually exclusive with *domain_search* |
| **state**  string | Whether to apply (`present`) or remove (`absent`) the settings.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](vyos_system_module.md#id3)

> **Note:**
>
> - Tested against VyOS 1.1.8 (helium).
> - This module works with connection `ansible.netcommon.network_cli`. See [the VyOS OS Platform Options](../network/user_guide/platform_vyos.md).
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`

## [Examples](vyos_system_module.md#id4)

```yaml+jinja
- name: configure hostname and domain-name
  vyos.vyos.vyos_system:
    host_name: vyos01
    domain_name: test.example.com

- name: remove all configuration
  vyos.vyos.vyos_system:
    state: absent

- name: configure name servers
  vyos.vyos.vyos_system: name_servers - 8.8.8.8 - 8.8.4.4
- name: configure domain search suffixes
  vyos.vyos.vyos_system:
    domain_search:
    - sub1.example.com
    - sub2.example.com
```

## [Return Values](vyos_system_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["set system hostname vyos01", "set system domain-name foo.example.com"]` |

### Authors

- Nathaniel Case (@Qalthos)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
