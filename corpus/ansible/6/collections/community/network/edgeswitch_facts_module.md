---
collection: ansible
version: "6"
title: "community.network.edgeswitch_facts module – Collect facts from remote devices running Edgeswitch"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/edgeswitch_facts_module.html
fetched_at: 2026-07-27T17:18:27+00:00
---
# community.network.edgeswitch_facts module – Collect facts from remote devices running Edgeswitch

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
> To use it in a playbook, specify: `community.network.edgeswitch_facts`.

- [Synopsis](edgeswitch_facts_module.md#synopsis)
- [Parameters](edgeswitch_facts_module.md#parameters)
- [Notes](edgeswitch_facts_module.md#notes)
- [Examples](edgeswitch_facts_module.md#examples)
- [Return Values](edgeswitch_facts_module.md#return-values)

## [Synopsis](edgeswitch_facts_module.md#id1)

- Collects a base set of device facts from a remote device that is running Ubiquiti Edgeswitch. This module prepends all of the base network fact keys with `ansible_net_<fact>`. The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

## [Parameters](edgeswitch_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **gather_subset**  string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include all, config, and interfaces. Can specify a list of values to include a larger subset. Values can also be used with an initial `!` to specify that a specific subset should not be collected.  Default: `"!config"` |

## [Notes](edgeswitch_facts_module.md#id3)

> **Note:**
>
> - Tested against Edgeswitch 1.7.4

## [Examples](edgeswitch_facts_module.md#id4)

```yaml+jinja
- name: Collect all facts from the device
  community.network.edgeswitch_facts:
    gather_subset: all

- name: Collect only the running config and default facts
  community.network.edgeswitch_facts:
    gather_subset:
      - config
```

## [Return Values](edgeswitch_facts_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ansible_net_config**  string | The current active config from the device  Returned: when config is configured |
| **ansible_net_gather_subset**  list / elements=string | The list of fact subsets collected from the device  Returned: always |
| **ansible_net_hostname**  string | The configured hostname of the device  Returned: always |
| **ansible_net_interfaces**  dictionary | A hash of all interfaces running on the system  Returned: when interfaces is configured |
| **ansible_net_model**  string | The model name returned from the device  Returned: always |
| **ansible_net_serialnum**  string | The serial number of the remote device  Returned: always |
| **ansible_net_startupconfig**  string  added in community.network 1.2.0 | The startup config from the device  Returned: when config is configured |
| **ansible_net_version**  string | The operating system version running on the remote device  Returned: always |

### Authors

- Frederic Bor (@f-bor)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
