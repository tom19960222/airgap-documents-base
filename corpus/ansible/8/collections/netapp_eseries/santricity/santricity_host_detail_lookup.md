---
collection: ansible
version: "8"
title: "netapp_eseries.santricity.santricity_host_detail lookup – Expands the host information from santricity_host lookup"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp_eseries/santricity/santricity_host_detail_lookup.html
fetched_at: 2026-07-28T02:44:43+00:00
---
# netapp_eseries.santricity.santricity_host_detail lookup – Expands the host information from santricity_host lookup

> **Note:**
>
> This lookup plugin is part of the [netapp_eseries.santricity collection](https://galaxy.ansible.com/ui/repo/published/netapp_eseries/santricity/) (version 1.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp_eseries.santricity`.
>
> To use it in a playbook, specify: `netapp_eseries.santricity.santricity_host_detail`.

- [Synopsis](santricity_host_detail_lookup.md#synopsis)
- [Keyword parameters](santricity_host_detail_lookup.md#keyword-parameters)

## [Synopsis](santricity_host_detail_lookup.md#id1)

- Expands the host information from santricity_host lookup to include system and port information

## [Keyword parameters](santricity_host_detail_lookup.md#id2)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('netapp_eseries.santricity.santricity_host_detail', key1=value1, key2=value2, ...)` and `query('netapp_eseries.santricity.santricity_host_detail', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **host_interface_ports**  list / elements=string / required | List of dictionaries containing “stdout_lines” which is a list of iqn/wwpns for each expected_hosts from the results of the santricity_host lookup plugin.  Register the results from the shell module that is looped over each host in expected_hosts. The command issued should result in a newline delineated list of iqns, nqns, or wwpns. |
| **hosts**  list / elements=string / required | E-Series storage array inventory, hostvars[inventory_hostname].  Run na_santricity_facts prior to calling |
| **hosts_info**  list / elements=string / required | The registered results from the setup module from each expected_hosts, hosts_info[‘results’].  Collected results from the setup module for each expected_hosts from the results of the santricity_host lookup plugin. |
| **protocol**  string / required | Storage system interface protocol (iscsi, sas, fc, ib-iser, ib-srp, nvme_ib, nvme_fc, or nvme_roce) |

### Authors

- Nathan Swartz

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/netappeseries/santricity/issues)
- [Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
