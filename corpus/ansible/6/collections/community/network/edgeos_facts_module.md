---
collection: ansible
version: "6"
title: "community.network.edgeos_facts module – Collect facts from remote devices running EdgeOS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/edgeos_facts_module.html
fetched_at: 2026-07-27T17:18:26+00:00
---
# community.network.edgeos_facts module – Collect facts from remote devices running EdgeOS

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
> To use it in a playbook, specify: `community.network.edgeos_facts`.

- [Synopsis](edgeos_facts_module.md#synopsis)
- [Parameters](edgeos_facts_module.md#parameters)
- [Notes](edgeos_facts_module.md#notes)
- [Examples](edgeos_facts_module.md#examples)
- [Return Values](edgeos_facts_module.md#return-values)

## [Synopsis](edgeos_facts_module.md#id1)

- Collects a base set of device facts from a remote device that is running EdgeOS. This module prepends all of the base network fact keys with ansible_net_<fact>. The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

## [Parameters](edgeos_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **gather_subset**  string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include all, default, config, and neighbors. Can specify a list of values to include a larger subset. Values can also be used with an initial `!` to specify that a specific subset should not be collected.  Default: `"!config"` |

## [Notes](edgeos_facts_module.md#id3)

> **Note:**
>
> - Tested against EdgeOS 1.9.7

## [Examples](edgeos_facts_module.md#id4)

```yaml+jinja
- name: Collect all facts from the device
  community.network.edgeos_facts:
    gather_subset: all

- name: Collect only the config and default facts
  community.network.edgeos_facts:
    gather_subset: config

- name: Collect everything exception the config
  community.network.edgeos_facts:
    gather_subset: "!config"
```

## [Return Values](edgeos_facts_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ansible_net_commits**  list / elements=string | The set of available configuration revisions  Returned: when present |
| **ansible_net_config**  string | The running-config from the device  Returned: when config is configured |
| **ansible_net_gather_subset**  list / elements=string | The list of subsets gathered by the module  Returned: always |
| **ansible_net_hostname**  string | The configured system hostname  Returned: always |
| **ansible_net_model**  string | The device model string  Returned: always |
| **ansible_net_neighbors**  list / elements=string | The set of LLDP neighbors  Returned: when interface is configured |
| **ansible_net_serialnum**  string | The serial number of the device  Returned: always |
| **ansible_net_version**  string | The version of the software running  Returned: always |

### Authors

- Nathaniel Case (@Qalthos)
- Sam Doran (@samdoran)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
