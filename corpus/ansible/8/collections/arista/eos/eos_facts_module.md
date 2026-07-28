---
collection: ansible
version: "8"
title: "arista.eos.eos_facts module – Collect facts from remote devices running Arista EOS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/arista/eos/eos_facts_module.html
fetched_at: 2026-07-28T01:04:29+00:00
---
# arista.eos.eos_facts module – Collect facts from remote devices running Arista EOS

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/ui/repo/published/arista/eos/) (version 6.2.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_facts`.

New in arista.eos 1.0.0

- [Synopsis](eos_facts_module.md#synopsis)
- [Parameters](eos_facts_module.md#parameters)
- [Examples](eos_facts_module.md#examples)
- [Return Values](eos_facts_module.md#return-values)

## [Synopsis](eos_facts_module.md#id1)

- Collects facts from Arista devices running the EOS operating system. This module places the facts gathered in the fact tree keyed by the respective resource name. The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

Aliases: facts

## [Parameters](eos_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **available_network_resources**  boolean | When ‘True’ a list of network resources for which resource modules are available will be provided.  **Choices:**   - `false` ← (default) - `true` |
| **gather_network_resources**  list / elements=string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include all and the resources like interfaces, vlans etc. Can specify a list of values to include a larger subset. Values can also be used with an initial `!` to specify that a specific subset should not be collected. Values can also be used with an initial `!` to specify that a specific subset should not be collected. Valid subsets are ‘all’, ‘interfaces’, ‘l2_interfaces’, ‘l3_interfaces’, ‘lacp’, ‘lacp_interfaces’, ‘lag_interfaces’, ‘lldp_global’, ‘lldp_interfaces’, ‘vlans’, ‘acls’. |
| **gather_subset**  list / elements=string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include `all`, `hardware`, `config`, `legacy`, `interfaces`, and `min`. Can specify a list of values to include a larger subset. Values can also be used with an initial `!` to specify that a specific subset should not be collected.  **Default:** `["min"]` |

## [Examples](eos_facts_module.md#id3)

```yaml+jinja
- name: Gather all legacy facts
- arista.eos.eos_facts:
    gather_subset: all

- name: Gather only the config and default facts
  arista.eos.eos_facts:
    gather_subset:
      - config

- name: Do not gather hardware facts
  arista.eos.eos_facts:
    gather_subset:
      - '!hardware'

- name: Gather legacy and resource facts
  arista.eos.eos_facts:
    gather_subset: all
    gather_network_resources: all

- name: Gather only the interfaces resource facts and no legacy facts
- arista.eos.eos_facts:
    gather_subset:
      - '!all'
      - '!min'
    gather_network_resources:
      - interfaces

- name: Gather all resource facts and minimal legacy facts
  arista.eos.eos_facts:
    gather_subset: min
    gather_network_resources: all
```

## [Return Values](eos_facts_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ansible_net_all_ipv4_addresses**  list / elements=string | All IPv4 addresses configured on the device  **Returned:** when interfaces is configured |
| **ansible_net_all_ipv6_addresses**  list / elements=string | All IPv6 addresses configured on the device  **Returned:** when interfaces is configured |
| **ansible_net_api**  string | The name of the transport  **Returned:** always |
| **ansible_net_config**  string | The current active config from the device  **Returned:** when config is configured |
| **ansible_net_filesystems**  list / elements=string | All file system names available on the device  **Returned:** when hardware is configured |
| **ansible_net_fqdn**  string | The fully qualified domain name of the device  **Returned:** always |
| **ansible_net_gather_network_resources**  list / elements=string | The list of fact for network resource subsets collected from the device  **Returned:** when the resource is configured |
| **ansible_net_gather_subset**  list / elements=string | The list of fact subsets collected from the device  **Returned:** always |
| **ansible_net_hostname**  string | The configured hostname of the device  **Returned:** always |
| **ansible_net_image**  string | The image file the device is running  **Returned:** always |
| **ansible_net_interfaces**  dictionary | A hash of all interfaces running on the system  **Returned:** when interfaces is configured |
| **ansible_net_memfree_mb**  integer | The available free memory on the remote device in Mb  **Returned:** when hardware is configured |
| **ansible_net_memtotal_mb**  integer | The total memory on the remote device in Mb  **Returned:** when hardware is configured |
| **ansible_net_model**  string | The model name returned from the device  **Returned:** always |
| **ansible_net_neighbors**  dictionary | The list of LLDP neighbors from the remote device  **Returned:** when interfaces is configured |
| **ansible_net_python_version**  string | The Python version Ansible controller is using  **Returned:** always |
| **ansible_net_serialnum**  string | The serial number of the remote device  **Returned:** always |
| **ansible_net_version**  string | The operating system version running on the remote device  **Returned:** always |

### Authors

- Peter Sprygada (@privateip)
- Nathaniel Case (@Qalthos)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/arista.eos)
