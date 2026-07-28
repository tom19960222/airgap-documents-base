---
collection: ansible
version: "6"
title: "community.network.icx_facts module – Collect facts from remote Ruckus ICX 7000 series switches"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/icx_facts_module.html
fetched_at: 2026-07-27T17:18:43+00:00
---
# community.network.icx_facts module – Collect facts from remote Ruckus ICX 7000 series switches

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
> To use it in a playbook, specify: `community.network.icx_facts`.

- [Synopsis](icx_facts_module.md#synopsis)
- [Parameters](icx_facts_module.md#parameters)
- [Notes](icx_facts_module.md#notes)
- [Examples](icx_facts_module.md#examples)
- [Return Values](icx_facts_module.md#return-values)

## [Synopsis](icx_facts_module.md#id1)

- Collects a base set of device facts from a remote device that is running ICX. This module prepends all of the base network fact keys with `ansible_net_<fact>`. The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

## [Parameters](icx_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **gather_subset**  list / elements=string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include all, hardware, config, and interfaces. Can specify a list of values to include a larger subset. Values can also be used with an initial `!` to specify that a specific subset should not be collected.  Default: `["!config"]` |

## [Notes](icx_facts_module.md#id3)

> **Note:**
>
> - Tested against ICX 10.1.
> - For information on using ICX platform, see [the ICX OS Platform Options guide](user_guide/platform_icx.md).

## [Examples](icx_facts_module.md#id4)

```yaml+jinja
- name: Collect all facts from the device
  community.network.icx_facts:
    gather_subset: all

- name: Collect only the config and default facts
  community.network.icx_facts:
    gather_subset:
      - config

- name: Do not collect hardware facts
  community.network.icx_facts:
    gather_subset:
      - "!hardware"
```

## [Return Values](icx_facts_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ansible_net_all_ipv4_addresses**  list / elements=string | All IPv4 addresses configured on the device  Returned: when interfaces is configured |
| **ansible_net_all_ipv6_addresses**  list / elements=string | All IPv6 addresses configured on the device  Returned: when interfaces is configured |
| **ansible_net_config**  string | The current active config from the device  Returned: when config is configured |
| **ansible_net_filesystems**  list / elements=string | All file system names available on the device  Returned: when hardware is configured |
| **ansible_net_filesystems_info**  dictionary | A hash of all file systems containing info about each file system (e.g. free and total space)  Returned: when hardware is configured |
| **ansible_net_gather_subset**  list / elements=string | The list of fact subsets collected from the device  Returned: always |
| **ansible_net_hostname**  string | The configured hostname of the device  Returned: always |
| **ansible_net_image**  string | The image file the device is running  Returned: always |
| **ansible_net_interfaces**  dictionary | A hash of all interfaces running on the system  Returned: when interfaces is configured |
| **ansible_net_memfree_mb**  integer | The available free memory on the remote device in Mb  Returned: when hardware is configured |
| **ansible_net_memtotal_mb**  integer | The total memory on the remote device in Mb  Returned: when hardware is configured |
| **ansible_net_model**  string | The model name returned from the device  Returned: always |
| **ansible_net_neighbors**  dictionary | The list of LLDP neighbors from the remote device  Returned: when interfaces is configured |
| **ansible_net_serialnum**  string | The serial number of the remote device  Returned: always |
| **ansible_net_stacked_models**  list / elements=string | The model names of each device in the stack  Returned: when multiple devices are configured in a stack |
| **ansible_net_stacked_serialnums**  list / elements=string | The serial numbers of each device in the stack  Returned: when multiple devices are configured in a stack |
| **ansible_net_version**  string | The operating system version running on the remote device  Returned: always |

### Authors

- Ruckus Wireless (@Commscope)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
