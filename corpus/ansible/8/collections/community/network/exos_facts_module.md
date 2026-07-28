---
collection: ansible
version: "8"
title: "community.network.exos_facts module – Collect facts from devices running Extreme EXOS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/exos_facts_module.html
fetched_at: 2026-07-28T01:56:36+00:00
---
# community.network.exos_facts module – Collect facts from devices running Extreme EXOS

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.exos_facts`.

- [Synopsis](exos_facts_module.md#synopsis)
- [Parameters](exos_facts_module.md#parameters)
- [Notes](exos_facts_module.md#notes)
- [Examples](exos_facts_module.md#examples)
- [Return Values](exos_facts_module.md#return-values)

## [Synopsis](exos_facts_module.md#id1)

- Collects a base set of device facts from a remote device that is running EXOS. This module prepends all of the base network fact keys with `ansible_net_<fact>`. The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

Aliases: network.exos.exos_facts

## [Parameters](exos_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **gather_network_resources**  list / elements=string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include all and the resources like interfaces, vlans etc. Can specify a list of values to include a larger subset. Values can also be used with an initial `!` to specify that a specific subset should not be collected. Valid subsets are ‘all’, ‘lldp_global’, ‘lldp_interfaces’, ‘vlans’, ‘l2_interfaces’. |
| **gather_subset**  list / elements=string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include all, hardware, config, and interfaces. Can specify a list of values to include a larger subset. Values can also be used with an initial `!` to specify that a specific subset should not be collected.  **Default:** `["!config"]` |

## [Notes](exos_facts_module.md#id3)

> **Note:**
>
> - Tested against EXOS 22.5.1.7
> - The *gather_network_resources* option currently only works with `ansible_connection: ansible.netcommon.httpapi`. For details, see <https://github.com/ansible-collections/community.network/issues/460>.

## [Examples](exos_facts_module.md#id4)

```yaml+jinja
- name:  Gather all legacy facts
  community.network.exos_facts:
    gather_subset: all

- name: Gather only the config and default facts
  community.network.exos_facts:
    gather_subset: config

- name: Do not gather hardware facts
  community.network.exos_facts:
    gather_subset: "!hardware"

- name: Gather legacy and resource facts
  community.network.exos_facts:
    gather_subset: all
    gather_network_resources: all

- name: Gather only the lldp global resource facts and no legacy facts
  community.network.exos_facts:
    gather_subset:
      - '!all'
      - '!min'
    gather_network_resources:
      - lldp_global

- name: Gather lldp global resource and minimal legacy facts
  community.network.exos_facts:
    gather_subset: min
    gather_network_resources: lldp_global
```

## [Return Values](exos_facts_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ansible_net_all_ipv4_addresses**  list / elements=string | All IPv4 addresses configured on the device  **Returned:** when interfaces is configured |
| **ansible_net_all_ipv6_addresses**  list / elements=string | All Primary IPv6 addresses configured on the device  **Returned:** when interfaces is configured |
| **ansible_net_config**  string | The current active config from the device  **Returned:** when config is configured |
| **ansible_net_gather_network_resources**  list / elements=string | The list of fact for network resource subsets collected from the device  **Returned:** when the resource is configured |
| **ansible_net_gather_subset**  list / elements=string | The list of fact subsets collected from the device  **Returned:** always |
| **ansible_net_hostname**  string | The configured hostname of the device  **Returned:** always |
| **ansible_net_interfaces**  dictionary | A hash of all interfaces running on the system  **Returned:** when interfaces is configured |
| **ansible_net_memfree_mb**  integer | The available free memory on the remote device in Mb  **Returned:** when hardware is configured |
| **ansible_net_memtotal_mb**  integer | The total memory on the remote device in Mb  **Returned:** when hardware is configured |
| **ansible_net_model**  string | The model name returned from the device  **Returned:** always |
| **ansible_net_neighbors**  dictionary | The list of LLDP neighbors from the remote device  **Returned:** when interfaces is configured |
| **ansible_net_serialnum**  string | The serial number of the remote device  **Returned:** always |
| **ansible_net_version**  string | The operating system version running on the remote device  **Returned:** always |

### Authors

- Lance Richardson (@hlrichardson)
- Ujwal Koamrla (@ujwalkomarla)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
