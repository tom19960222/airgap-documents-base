---
collection: ansible
version: "6"
title: "community.network.ordnance_facts module – Collect facts from Ordnance Virtual Routers over SSH"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ordnance_facts_module.html
fetched_at: 2026-07-27T17:19:13+00:00
---
# community.network.ordnance_facts module – Collect facts from Ordnance Virtual Routers over SSH

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
> To use it in a playbook, specify: `community.network.ordnance_facts`.

- [Synopsis](ordnance_facts_module.md#synopsis)
- [Parameters](ordnance_facts_module.md#parameters)
- [Examples](ordnance_facts_module.md#examples)
- [Return Values](ordnance_facts_module.md#return-values)

## [Synopsis](ordnance_facts_module.md#id1)

- Collects a base set of device facts from an Ordnance Virtual router over SSH. This module prepends all of the base network fact keys with `ansible_net_<fact>`. The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

## [Parameters](ordnance_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **gather_subset**  string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include all, hardware, config, and interfaces. Can specify a list of values to include a larger subset. Values can also be used with an initial `!` to specify that a specific subset should not be collected.  Default: `"!config"` |

## [Examples](ordnance_facts_module.md#id3)

```yaml+jinja
---
# Note: examples below use the following provider dict to handle
#       transport and authentication to the node.
vars:
  cli:
    host: "{{ inventory_hostname }}"
    username: RouterName
    password: ordnance
    transport: cli

---
- name: Collect all facts from the device
  community.network.ordnance_facts:
    gather_subset: all
    provider: "{{ cli }}"

- name: Collect only the config and default facts
  community.network.ordnance_facts:
    gather_subset:
      - config
    provider: "{{ cli }}"

- name: Do not collect hardware facts
  community.network.ordnance_facts:
    gather_subset:
      - "!hardware"
    provider: "{{ cli }}"
```

## [Return Values](ordnance_facts_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ansible_net_all_ipv4_addresses**  list / elements=string | All IPv4 addresses configured on the virtual router  Returned: when interfaces is configured |
| **ansible_net_all_ipv6_addresses**  list / elements=string | All IPv6 addresses configured on the virtual router  Returned: when interfaces is configured |
| **ansible_net_config**  string | The current active config from the virtual router  Returned: when config is configured |
| **ansible_net_gather_subset**  list / elements=string | The list of fact subsets collected from the virtual router  Returned: always |
| **ansible_net_interfaces**  dictionary | A hash of all interfaces running on the virtual router  Returned: when interfaces is configured |

### Authors

- Alexander Turner (@alexanderturner)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
