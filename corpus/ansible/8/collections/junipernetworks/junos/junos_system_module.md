---
collection: ansible
version: "8"
title: "junipernetworks.junos.junos_system module – Manage the system attributes on Juniper JUNOS devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/junipernetworks/junos/junos_system_module.html
fetched_at: 2026-07-28T02:39:59+00:00
---
# junipernetworks.junos.junos_system module – Manage the system attributes on Juniper JUNOS devices

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/ui/repo/published/junipernetworks/junos/) (version 5.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_system_module.md#ansible-collections-junipernetworks-junos-junos-system-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_system`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_system_module.md#synopsis)
- [Requirements](junos_system_module.md#requirements)
- [Parameters](junos_system_module.md#parameters)
- [Notes](junos_system_module.md#notes)
- [Examples](junos_system_module.md#examples)
- [Return Values](junos_system_module.md#return-values)

## [Synopsis](junos_system_module.md#id1)

- This module provides declarative management of node system attributes on Juniper JUNOS devices. It provides an option to configure host system parameters or remove those parameters from the device active configuration.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: system

## [Requirements](junos_system_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.5.2)

## [Parameters](junos_system_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **active**  boolean | Specifies whether or not the configuration is active or deactivated  **Choices:**   - `false` - `true` ← (default) |
| **domain_name**  string | Configure the IP domain name on the remote device to the provided value. Value should be in the dotted name form and will be appended to the `hostname` to create a fully-qualified domain name. |
| **domain_search**  list / elements=string | Provides the list of domain suffixes to append to the hostname for the purpose of doing name resolution. This argument accepts a list of names and will be reconciled with the current active configuration on the running node. |
| **hostname**  string | Configure the device hostname parameter. This option takes an ASCII string value. |
| **name_servers**  list / elements=string | List of DNS name servers by IP address to use to perform name resolution lookups. This argument accepts either a list of DNS servers See examples. |
| **state**  string | State of the configuration values in the device’s current active configuration. When set to *present*, the values should be configured in the device active configuration and when set to *absent* the values should not be in the device active configuration  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](junos_system_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Tested against vSRX JUNOS version 15.1X49-D15.4, vqfx-10000 JUNOS Version 15.1X53-D60.4.
> - Recommended connection is `netconf`. See [the Junos OS Platform Options](../network/user_guide/platform_junos.md).
> - This module also works with `local` connections for legacy playbooks.
> - For information on using CLI and netconf see the :ref:`Junos OS Platform Options guide <junos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Juniper network devices see <https://www.ansible.com/ansible-juniper>.

## [Examples](junos_system_module.md#id5)

```yaml+jinja
- name: configure hostname and domain name
  junipernetworks.junos.junos_system:
    hostname: junos01
    domain_name: test.example.com
    domain-search:
      - ansible.com
      - redhat.com
      - juniper.net

- name: remove configuration
  junipernetworks.junos.junos_system:
    state: absent

- name: configure name servers
  junipernetworks.junos.junos_system:
    name_servers:
      - 8.8.8.8
      - 8.8.4.4
```

## [Return Values](junos_system_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **diff.prepared**  string | Configuration difference before and after applying change.  **Returned:** when configuration is changed and diff option is enabled.  **Sample:** `"[edit system] +  host-name test; +  domain-name ansible.com; +  domain-search redhat.com; [edit system name-server]\n    172.26.1.1 { ... }\n+   8.8.8.8;\n"` |

### Authors

- Ganesh Nalawade (@ganeshrn)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
