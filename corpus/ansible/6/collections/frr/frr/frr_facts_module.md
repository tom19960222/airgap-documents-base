---
collection: ansible
version: "6"
title: "frr.frr.frr_facts module – Collect facts from remote devices running Free Range Routing (FRR)."
source_url: https://docs.ansible.com/projects/ansible/6/collections/frr/frr/frr_facts_module.html
fetched_at: 2026-07-27T17:47:31+00:00
---
# frr.frr.frr_facts module – Collect facts from remote devices running Free Range Routing (FRR).

> **Note:**
>
> This module is part of the [frr.frr collection](https://galaxy.ansible.com/frr/frr) (version 2.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install frr.frr`.
>
> To use it in a playbook, specify: `frr.frr.frr_facts`.

New in frr.frr 1.0.0

- [Synopsis](frr_facts_module.md#synopsis)
- [Parameters](frr_facts_module.md#parameters)
- [Notes](frr_facts_module.md#notes)
- [Examples](frr_facts_module.md#examples)
- [Return Values](frr_facts_module.md#return-values)

## [Synopsis](frr_facts_module.md#id1)

- Collects a base set of device facts from a remote device that is running FRR. This module prepends all of the base network fact keys with `ansible_net_<fact>`. The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

## [Parameters](frr_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **gather_subset**  list / elements=string | When supplied, this argument restricts the facts collected to a given subset.  Possible values for this argument include `all`, `hardware`, `config`, and `interfaces`.  Specify a list of values to include a larger subset.  Use a value with an initial `!` to collect all facts except that subset.  Default: `["!config"]` |

## [Notes](frr_facts_module.md#id3)

> **Note:**
>
> - Tested against FRR 6.0.

## [Examples](frr_facts_module.md#id4)

```yaml+jinja
- name: Collect all facts from the device
  frr.frr.frr_facts:
    gather_subset: all

- name: Collect only the config and default facts
  frr.frr.frr_facts:
    gather_subset:
    - config

- name: Collect the config and hardware facts
  frr.frr.frr_facts:
    gather_subset:
    - config
    - hardware

- name: Do not collect hardware facts
  frr.frr.frr_facts:
    gather_subset:
    - '!hardware'
```

## [Return Values](frr_facts_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ansible_net_all_ipv4_addresses**  list / elements=string | All IPv4 addresses configured on the device  Returned: when interfaces is configured |
| **ansible_net_all_ipv6_addresses**  list / elements=string | All IPv6 addresses configured on the device  Returned: when interfaces is configured |
| **ansible_net_api**  string | The name of the transport  Returned: always |
| **ansible_net_config**  string | The current active config from the device  Returned: when config is configured |
| **ansible_net_gather_subset**  list / elements=string | The list of fact subsets collected from the device  Returned: always |
| **ansible_net_hostname**  string | The configured hostname of the device  Returned: always |
| **ansible_net_interfaces**  dictionary | A hash of all interfaces running on the system  Returned: when interfaces is configured |
| **ansible_net_mem_stats**  dictionary | The memory statistics fetched from the device  Returned: when hardware is configured |
| **ansible_net_mpls_ldp_neighbors**  dictionary | The list of MPLS LDP neighbors from the remote device  Returned: when interfaces is configured and LDP daemon is running on the device |
| **ansible_net_python_version**  string | The Python version that the Ansible controller is using  Returned: always |
| **ansible_net_version**  string | The FRR version running on the remote device  Returned: always |

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/frr.frr/issues)
[Repository (Sources)](https://github.com/ansible-collections/frr.frr)
