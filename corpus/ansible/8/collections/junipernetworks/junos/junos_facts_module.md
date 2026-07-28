---
collection: ansible
version: "8"
title: "junipernetworks.junos.junos_facts module – Collect facts from remote devices running Juniper Junos"
source_url: https://docs.ansible.com/projects/ansible/8/collections/junipernetworks/junos/junos_facts_module.html
fetched_at: 2026-07-28T02:39:35+00:00
---
# junipernetworks.junos.junos_facts module – Collect facts from remote devices running Juniper Junos

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
> see [Requirements](junos_facts_module.md#ansible-collections-junipernetworks-junos-junos-facts-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_facts`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_facts_module.md#synopsis)
- [Requirements](junos_facts_module.md#requirements)
- [Parameters](junos_facts_module.md#parameters)
- [Notes](junos_facts_module.md#notes)
- [Examples](junos_facts_module.md#examples)

## [Synopsis](junos_facts_module.md#id1)

- Collects fact information from a remote device running the Junos operating system. By default, the module will collect basic fact information from the device to be included with the hostvars. Additional fact information can be collected based on the configured set of arguments.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: facts

## [Requirements](junos_facts_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.5.2)

## [Parameters](junos_facts_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **available_network_resources**  boolean | When ‘True’ a list of network resources for which resource modules are available will be provided.  **Choices:**   - `false` ← (default) - `true` |
| **config_format**  string | The *config_format* argument specifies the format of the configuration when serializing output from the device. This argument is applicable only when `config` value is present in *gather_subset*. The *config_format* should be supported by the junos version running on device. This value is not applicable while fetching old style facts that is when `ofacts` value is present in value if *gather_subset* value. This option is valid only for `gather_subset` values.  **Choices:**   - `"xml"` - `"text"` ← (default) - `"set"` - `"json"` |
| **gather_network_resources**  list / elements=string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include all and the resources like interfaces, vlans etc. Can specify a list of values to include a larger subset. Values can also be used with an initial `!` to specify that a specific subset should not be collected. Valid subsets are ‘all’, ‘interfaces’, ‘lacp’, ‘lacp_interfaces’, ‘lag_interfaces’, ‘l2_interfaces’, ‘l3_interfaces’, ‘lldp_global’, ‘lldp_interfaces’, ‘vlans’. |
| **gather_subset**  list / elements=string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include `all`, `hardware`, `config`, `interfaces` and `min`. Can specify a list of values to include a larger subset. Values can also be used with an initial `!` to specify that a specific subset should not be collected. To maintain backward compatibility old style facts can be retrieved by explicitly adding `ofacts` to value, this requires junos-eznc to be installed as a prerequisite. Valid value of gather_subset are default, hardware, config, interfaces, ofacts. If `ofacts` is present in the list it fetches the old style facts (fact keys without ‘ansible_’ prefix) and it requires junos-eznc library to be installed.  **Default:** `["min"]` |

## [Notes](junos_facts_module.md#id4)

> **Note:**
>
> - Ensure *config_format* used to retrieve configuration from device is supported by junos version running on device.
> - With *config_format = json*, configuration in the results will be a dictionary(and not a JSON string)
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Tested against vSRX JUNOS version 15.1X49-D15.4, vqfx-10000 JUNOS Version 15.1X53-D60.4.
> - Recommended connection is `netconf`. See [the Junos OS Platform Options](../network/user_guide/platform_junos.md).
> - This module also works with `local` connections for legacy playbooks.
> - For information on using CLI and netconf see the :ref:`Junos OS Platform Options guide <junos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Juniper network devices see <https://www.ansible.com/ansible-juniper>.

## [Examples](junos_facts_module.md#id5)

```yaml+jinja
- name: collect default set of facts
  junipernetworks.junos.junos_facts:

- name: collect default set of facts and configuration
  junipernetworks.junos.junos_facts:
    gather_subset: config

- name: Gather legacy and resource facts
  junipernetworks.junos.junos_facts:
    gather_subset: all
    gather_network_resources: all
```

### Authors

- Nathaniel Case (@Qalthos)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
