---
collection: ansible
version: "6"
title: "community.routeros.facts module – Collect facts from remote devices running MikroTik RouterOS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/routeros/facts_module.html
fetched_at: 2026-07-27T17:20:55+00:00
---
# community.routeros.facts module – Collect facts from remote devices running MikroTik RouterOS

> **Note:**
>
> This module is part of the [community.routeros collection](https://galaxy.ansible.com/community/routeros) (version 2.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.routeros`.
>
> To use it in a playbook, specify: `community.routeros.facts`.

- [Synopsis](facts_module.md#synopsis)
- [Parameters](facts_module.md#parameters)
- [Attributes](facts_module.md#attributes)
- [See Also](facts_module.md#see-also)
- [Examples](facts_module.md#examples)
- [Returned Facts](facts_module.md#returned-facts)

## [Synopsis](facts_module.md#id1)

- Collects a base set of device facts from a remote device that is running RouterOS. This module prepends all of the base network fact keys with `ansible_net_<fact>`. The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

## [Parameters](facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **gather_subset**  list / elements=string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include `all`, `hardware`, `config`, `interfaces`, and `routing`.  Can specify a list of values to include a larger subset. Values can also be used with an initial `!` to specify that a specific subset should not be collected.  Default: `["!config"]` |

## [Attributes](facts_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support:  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **facts** | Support: full | Action returns an `ansible_facts` dictionary that will update existing host facts. |
| **platform** | Platform: RouterOS | Target OS/families that can be operated against. |

## [See Also](facts_module.md#id4)

> **See also:**
>
> [How to connect to RouterOS devices with SSH](docsite/ssh-guide.md#ansible-collections-community-routeros-docsite-ssh-guide)
> :   How to connect to RouterOS devices with SSH

## [Examples](facts_module.md#id5)

```yaml+jinja
- name: Collect all facts from the device
  community.routeros.facts:
    gather_subset: all

- name: Collect only the config and default facts
  community.routeros.facts:
    gather_subset:
      - config

- name: Do not collect hardware facts
  community.routeros.facts:
    gather_subset:
      - "!hardware"
```

## [Returned Facts](facts_module.md#id6)

Facts returned by this module are added/updated in the `hostvars` host facts and can be referenced by name just like any other host fact. They do not need to be registered in order to use them.

| Key | Description |
| --- | --- |
| **ansible_net_all_ipv4_addresses**  list / elements=string | All IPv4 addresses configured on the device.  Returned: *gather_subset* contains `interfaces` |
| **ansible_net_all_ipv6_addresses**  list / elements=string | All IPv6 addresses configured on the device.  Returned: *gather_subset* contains `interfaces` |
| **ansible_net_arch**  string | The CPU architecture of the device.  Returned: *gather_subset* contains `default` |
| **ansible_net_bgp_instance**  dictionary | A dictionary with BGP instance information.  Returned: *gather_subset* contains `routing` |
| **ansible_net_bgp_peer**  dictionary | A dictionary with BGP peer information.  Returned: *gather_subset* contains `routing` |
| **ansible_net_bgp_vpnv4_route**  dictionary | A dictionary with BGP vpnv4 route information.  Returned: *gather_subset* contains `routing` |
| **ansible_net_config**  string | The current active config from the device.  Returned: *gather_subset* contains `config` |
| **ansible_net_config_nonverbose**  string  added in community.routeros 1.2.0 | The current active config from the device in minimal form.  This value is idempotent in the sense that if the facts module is run twice and the device’s config was not changed between the runs, the value is identical. This is achieved by running `/export` and stripping the timestamp from the comment in the first line.  Returned: *gather_subset* contains `config` |
| **ansible_net_cpu_load**  string | Current CPU load.  Returned: *gather_subset* contains `default` |
| **ansible_net_gather_subset**  list / elements=string | The list of fact subsets collected from the device.  Returned: always |
| **ansible_net_hostname**  string | The configured hostname of the device.  Returned: *gather_subset* contains `default` |
| **ansible_net_interfaces**  dictionary | A hash of all interfaces running on the system.  Returned: *gather_subset* contains `interfaces` |
| **ansible_net_memfree_mb**  integer | The available free memory on the remote device in MiB.  Returned: *gather_subset* contains `hardware` |
| **ansible_net_memtotal_mb**  integer | The total memory on the remote device in MiB.  Returned: *gather_subset* contains `hardware` |
| **ansible_net_model**  string | The model name returned from the device.  Returned: *gather_subset* contains `default` |
| **ansible_net_neighbors**  dictionary | The list of neighbors from the remote device.  Returned: *gather_subset* contains `interfaces` |
| **ansible_net_ospf_instance**  dictionary | A dictionary with OSPF instances.  Returned: *gather_subset* contains `routing` |
| **ansible_net_ospf_neighbor**  dictionary | A dictionary with OSPF neighbors.  Returned: *gather_subset* contains `routing` |
| **ansible_net_route**  dictionary | A dictionary for routes in all routing tables.  Returned: *gather_subset* contains `routing` |
| **ansible_net_serialnum**  string | The serial number of the remote device.  Returned: *gather_subset* contains `default` |
| **ansible_net_spacefree_mb**  dictionary | The available disk space on the remote device in MiB.  Returned: *gather_subset* contains `hardware` |
| **ansible_net_spacetotal_mb**  dictionary | The total disk space on the remote device in MiB.  Returned: *gather_subset* contains `hardware` |
| **ansible_net_uptime**  string | The uptime of the device.  Returned: *gather_subset* contains `default` |
| **ansible_net_version**  string | The operating system version running on the remote device.  Returned: *gather_subset* contains `default` |

### Authors

- Egor Zaitsev (@heuels)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.routeros/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.routeros)
[Submit a bug report](https://github.com/ansible-collections/community.routeros/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.routeros/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-routeros)
