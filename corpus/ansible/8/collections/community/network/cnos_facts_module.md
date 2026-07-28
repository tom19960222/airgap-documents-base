---
collection: ansible
version: "8"
title: "community.network.cnos_facts module – Collect facts from remote devices running Lenovo CNOS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/cnos_facts_module.html
fetched_at: 2026-07-28T01:56:11+00:00
---
# community.network.cnos_facts module – Collect facts from remote devices running Lenovo CNOS

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
> To use it in a playbook, specify: `community.network.cnos_facts`.

- [Synopsis](cnos_facts_module.md#synopsis)
- [Parameters](cnos_facts_module.md#parameters)
- [Notes](cnos_facts_module.md#notes)
- [Examples](cnos_facts_module.md#examples)
- [Return Values](cnos_facts_module.md#return-values)

## [Synopsis](cnos_facts_module.md#id1)

- Collects a base set of device facts from a remote Lenovo device running on CNOS. This module prepends all of the base network fact keys with `ansible_net_<fact>`. The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

Aliases: network.cnos.cnos_facts

## [Parameters](cnos_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  **Choices:**   - `false` ← (default) - `true` |
| **gather_subset**  string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include all, hardware, config, and interfaces. Can specify a list of values to include a larger subset. Values can also be used with an initial `!` to specify that a specific subset should not be collected.  **Default:** `"!config"` |

## [Notes](cnos_facts_module.md#id3)

> **Note:**
>
> - Tested against CNOS 10.8.1

## [Examples](cnos_facts_module.md#id4)

```yaml+jinja
Tasks: The following are examples of using the module cnos_facts.
---
- name: Test cnos Facts
  community.network.cnos_facts:

---
# Collect all facts from the device
- community.network.cnos_facts:
    gather_subset: all

# Collect only the config and default facts
- community.network.cnos_facts:
    gather_subset:
      - config

# Do not collect hardware facts
- community.network.cnos_facts:
    gather_subset:
      - "!hardware"
```

## [Return Values](cnos_facts_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ansible_net_all_ipv4_addresses**  list / elements=string | All IPv4 addresses configured on the device  **Returned:** when interfaces is configured |
| **ansible_net_all_ipv6_addresses**  list / elements=string | All IPv6 addresses configured on the device  **Returned:** when interfaces is configured |
| **ansible_net_config**  string | The current active config from the device  **Returned:** when config is configured |
| **ansible_net_gather_subset**  list / elements=string | The list of fact subsets collected from the device  **Returned:** always |
| **ansible_net_hostname**  string | The configured hostname of the device  **Returned:** always |
| **ansible_net_image**  string | Indicates the active image for the device  **Returned:** always |
| **ansible_net_interfaces**  dictionary | A hash of all interfaces running on the system. This gives information on description, mac address, mtu, speed, duplex and operstatus  **Returned:** when interfaces is configured |
| **ansible_net_memfree_mb**  integer | The available free memory on the remote device in MB  **Returned:** when hardware is configured |
| **ansible_net_model**  string | The model name returned from the Lenovo CNOS device  **Returned:** always |
| **ansible_net_neighbors**  dictionary | The list of LLDP neighbors from the remote device  **Returned:** when interfaces is configured |
| **ansible_net_serialnum**  string | The serial number of the Lenovo CNOS device  **Returned:** always |
| **ansible_net_version**  string | The CNOS operating system version running on the remote device  **Returned:** always |

### Authors

- Anil Kumar Muraleedharan (@amuraleedhar)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
