---
collection: ansible
version: "8"
title: "community.network.ironware_facts module – Collect facts from devices running Extreme Ironware"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ironware_facts_module.html
fetched_at: 2026-07-28T01:57:01+00:00
---
# community.network.ironware_facts module – Collect facts from devices running Extreme Ironware

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
> To use it in a playbook, specify: `community.network.ironware_facts`.

- [Synopsis](ironware_facts_module.md#synopsis)
- [Parameters](ironware_facts_module.md#parameters)
- [Notes](ironware_facts_module.md#notes)
- [Examples](ironware_facts_module.md#examples)
- [Return Values](ironware_facts_module.md#return-values)

## [Synopsis](ironware_facts_module.md#id1)

- Collects a base set of device facts from a remote device that is running Ironware. This module prepends all of the base network fact keys with `ansible_net_<fact>`. The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

Aliases: network.ironware.ironware_facts

## [Parameters](ironware_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **authorize**  boolean | **Deprecated**  Starting with Ansible 2.7 we recommend using `connection: network_cli` and `become: true`.  For more information please see the [IronWare Platform Options guide](user_guide/platform_ironware.md).   ---   Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  **Choices:**   - `false` ← (default) - `true` |
| **gather_subset**  string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include all, hardware, config, mpls and interfaces. Can specify a list of values to include a larger subset. Values can also be used with an initial `!` to specify that a specific subset should not be collected.  **Default:** `["!config", "!mpls"]` |

## [Notes](ironware_facts_module.md#id3)

> **Note:**
>
> - Tested against Ironware 5.8e
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`

## [Examples](ironware_facts_module.md#id4)

```yaml+jinja
- name: Collect all facts from the device
  community.network.ironware_facts:
    gather_subset: all

- name: Collect only the config and default facts
  community.network.ironware_facts:
    gather_subset:
      - config

- name: Do not collect hardware facts
  community.network.ironware_facts:
    gather_subset:
      - "!hardware"
```

## [Return Values](ironware_facts_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ansible_net_all_ipv4_addresses**  list / elements=string | All IPv4 addresses configured on the device  **Returned:** when interfaces is configured |
| **ansible_net_all_ipv6_addresses**  list / elements=string | All IPv6 addresses configured on the device  **Returned:** when interfaces is configured |
| **ansible_net_config**  string | The current active config from the device  **Returned:** when config is configured |
| **ansible_net_filesystems**  list / elements=string | All file system names available on the device  **Returned:** when hardware is configured |
| **ansible_net_gather_subset**  list / elements=string | The list of fact subsets collected from the device  **Returned:** always |
| **ansible_net_interfaces**  dictionary | A hash of all interfaces running on the system  **Returned:** when interfaces is configured |
| **ansible_net_memfree_mb**  integer | The available free memory on the remote device in Mb  **Returned:** when hardware is configured |
| **ansible_net_memtotal_mb**  integer | The total memory on the remote device in Mb  **Returned:** when hardware is configured |
| **ansible_net_model**  string | The model name returned from the device  **Returned:** always |
| **ansible_net_mpls_lsps**  dictionary | All MPLS LSPs configured on the device  **Returned:** When LSP is configured |
| **ansible_net_mpls_vll**  dictionary | All VLL instances configured on the device  **Returned:** When MPLS VLL is configured |
| **ansible_net_mpls_vll_local**  dictionary | All VLL-LOCAL instances configured on the device  **Returned:** When MPLS VLL-LOCAL is configured |
| **ansible_net_mpls_vpls**  dictionary | All VPLS instances configured on the device  **Returned:** When MPLS VPLS is configured |
| **ansible_net_neighbors**  dictionary | The list of LLDP neighbors from the remote device  **Returned:** when interfaces is configured |
| **ansible_net_serialnum**  string | The serial number of the remote device  **Returned:** always |
| **ansible_net_version**  string | The operating system version running on the remote device  **Returned:** always |

### Authors

- Paul Baker (@paulquack)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
