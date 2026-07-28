---
collection: ansible
version: "8"
title: "community.network.ce_facts module – Gets facts about HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_facts_module.html
fetched_at: 2026-07-28T01:55:25+00:00
---
# community.network.ce_facts module – Gets facts about HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_facts`.

- [Synopsis](ce_facts_module.md#synopsis)
- [Parameters](ce_facts_module.md#parameters)
- [Notes](ce_facts_module.md#notes)
- [Examples](ce_facts_module.md#examples)
- [Return Values](ce_facts_module.md#return-values)

## [Synopsis](ce_facts_module.md#id1)

- Collects facts from CloudEngine devices running the CloudEngine operating system. Fact collection is supported over Cli transport. This module prepends all of the base network fact keys with `ansible_net_<fact>`. The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

Aliases: network.cloudengine.ce_facts

## [Parameters](ce_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **gather_subset**  string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include all, hardware, config, and interfaces. Can specify a list of values to include a larger subset. Values can also be used with an initial `!` to specify that a specific subset should not be collected.  **Default:** `"!config"` |

## [Notes](ce_facts_module.md#id3)

> **Note:**
>
> - Recommended connection is `network_cli`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_facts_module.md#id4)

```yaml+jinja
# Note: examples below use the following provider dict to handle
#       transport and authentication to the node.

- name: CloudEngine facts test
  hosts: cloudengine
  connection: local
  gather_facts: false
  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ username }}"
      password: "{{ password }}"
      transport: cli

  tasks:

  - name: "Gather_subset is all"
    community.network.ce_facts:
      gather_subset: all
      provider: "{{ cli }}"

  - name: "Collect only the config facts"
    community.network.ce_facts:
      gather_subset: config
      provider: "{{ cli }}"

  - name: "Do not collect hardware facts"
    community.network.ce_facts:
      gather_subset: "!hardware"
      provider: "{{ cli }}"
```

## [Return Values](ce_facts_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **all_ipv4_addresses**  list / elements=string | All IPv4 addresses configured on the device  **Returned:** when interfaces is configured |
| **BIOS Version**  string | The BIOS version running on the remote device  **Returned:** always |
| **Board Type**  string | The board type of the remote device  **Returned:** always |
| **config**  string | The current system configuration on the device  **Returned:** when config is configured |
| **CPLD1 Version**  string | The CPLD1 Version running the remote device  **Returned:** always |
| **CPLD2 Version**  string | The CPLD2 Version running the remote device  **Returned:** always |
| **FAN**  string | The fan state on the device  **Returned:** when hardware is configured |
| **filesystems**  string | The filesystems on the device  **Returned:** when hardware is configured |
| **flash_free**  string | The flash free space on the device  **Returned:** when hardware is configured |
| **flash_total**  string | The flash total space on the device  **Returned:** when hardware is configured |
| **gather_subset**  list / elements=string | The list of fact subsets collected from the device  **Returned:** always |
| **hostname**  string | The hostname of the remote device  **Returned:** always |
| **interfaces**  dictionary | A hash of all interfaces running on the system  **Returned:** when interfaces is configured |
| **MAB Version**  string | The MAB Version running the remote device  **Returned:** always |
| **memory_free**  string | The memory free space on the remote device  **Returned:** when hardware is configured |
| **memory_total**  string | The memory total space on the remote device  **Returned:** when hardware is configured |
| **neighbors**  dictionary | The list of LLDP neighbors from the remote device  **Returned:** when interfaces is configured |
| **PCB Version**  string | The PCB Version running the remote device  **Returned:** always |
| **PWR**  string | The power state on the device  **Returned:** when hardware is configured |

### Authors

- wangdezhuang (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
