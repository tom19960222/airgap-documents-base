---
collection: ansible
version: "8"
title: "ansible.netcommon.parse_cli filter – parse_cli filter plugin."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/parse_cli_filter.html
fetched_at: 2026-07-28T01:04:54+00:00
---
# ansible.netcommon.parse_cli filter – parse_cli filter plugin.

> **Note:**
>
> This filter plugin is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ui/repo/published/ansible/netcommon/) (version 5.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.parse_cli`.

New in ansible.netcommon 1.0.0

- [Synopsis](parse_cli_filter.md#synopsis)
- [Keyword parameters](parse_cli_filter.md#keyword-parameters)
- [Notes](parse_cli_filter.md#notes)
- [Examples](parse_cli_filter.md#examples)

## [Synopsis](parse_cli_filter.md#id1)

- The filter plugins converts the output of a network device CLI command into structured JSON output.
- Using the parameters below - `xml_data | ansible.netcommon.parse_cli(template.yml`)

## [Keyword parameters](parse_cli_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.netcommon.parse_cli(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **output**  any / required | This source data on which parse_cli invokes. |
| **tmpl**  string | The spec file should be valid formatted YAML. It defines how to parse the CLI output and return JSON data.  For example `cli_data | ansible.netcommon.parse_cli(template.yml`), in this case `cli_data` represents cli output. |

## [Notes](parse_cli_filter.md#id3)

> **Note:**
>
> - The parse_cli filter will load the spec file and pass the command output through it, returning JSON output. The YAML spec file defines how to parse the CLI output

## [Examples](parse_cli_filter.md#id4)

```yaml+jinja
# Using parse_cli

# outputConfig

# ip dhcp pool Data
#   import all
#   network 192.168.1.0 255.255.255.0
#   update dns
#   default-router 192.168.1.1
#   dns-server 192.168.1.1 8.8.8.8
#   option 42 ip 192.168.1.1
#   domain-name test.local
#   lease 8

# pconnection.yml

# ---
# vars:
#   dhcp_pool:
#     name: "{{ item.name }}"
#     network: "{{ item.network_ip }}"
#     subnet: "{{ item.network_subnet }}"
#     dns_servers: "{{ item.dns_servers_1 }}{{ item.dns_servers_2 }}"
#     domain_name: "{{ item.domain_name_0 }}{{ item.domain_name_1 }}{{ item.domain_name_2 }}{{ item.domain_name_3 }}"
#     options: "{{ item.options_1 }}{{ item.options_2 }}"
#     lease_days: "{{ item.lease_days }}"
#     lease_hours: "{{ item.lease_hours }}"
#     lease_minutes: "{{ item.lease_minutes }}"

# keys:
#   dhcp_pools:
#     value: "{{ dhcp_pool }}"
#     items: "^ip dhcp pool (
#           ?P<name>[^\\n]+)\\s+(?:import (?P<import_all>all)\\s*)?(?:network (?P<network_ip>[\\d.]+)
#           (?P<network_subnet>[\\d.]+)?\\s*)?(?:update dns\\s*)?(?:host (?P<host_ip>[\\d.]+)
#           (?P<host_subnet>[\\d.]+)\\s*)?(?:domain-name (?P<domain_name_0>[\\w._-]+)\\s+)?
#           (?:default-router (?P<default_router>[\\d.]+)\\s*)?(?:dns-server
#           (?P<dns_servers_1>(?:[\\d.]+ ?)+ ?)+\\s*)?(?:domain-name (?P<domain_name_1>[\\w._-]+)\\s+)?
#           (?P<options_1>(?:option [^\\n]+\\n*\\s*)*)?(?:domain-name (?P<domain_name_2>[\\w._-]+)\\s+)?(?P<options_2>(?:option [^\\n]+\\n*\\s*)*)?
#           (?:dns-server (?P<dns_servers_2>(?:[\\d.]+ ?)+ ?)+\\s*)?(?:domain-name
#           (?P<domain_name_3>[\\w._-]+)\\s*)?(lease (?P<lease_days>\\d+)(?: (?P<lease_hours>\\d+))?(?: (?P<lease_minutes>\\d+))?\\s*)?(?:update arp)?"

# playbook

- name: Add config data
  ansible.builtin.set_fact:
    opconfig: "{{lookup('ansible.builtin.file', 'outputConfig') }}"

- name: Parse Data
  ansible.builtin.set_fact:
    output: "{{ opconfig | parse_cli('pconnection.yml') }}"

# Task Output
# -----------
#
# TASK [Add config data]
# ok: [host] => changed=false
#   ansible_facts:
#     xml: |-
#       ip dhcp pool Data
#         import all
#         network 192.168.1.0 255.255.255.0
#         update dns
#         default-router 192.168.1.1
#         dns-server 192.168.1.1 8.8.8.8
#         option 42 ip 192.168.1.1
#         domain-name test.local
#         lease 8

# TASK [Parse Data]
# ok: [host] => changed=false
#   ansible_facts:
#     output:
#       dhcp_pools:
#       - dns_servers: 192.168.1.1 8.8.8.8
#         domain_name: test.local
#         lease_days: 8
#         lease_hours: null
#         lease_minutes: null
#         name: Data
#         network: 192.168.1.0
#         options: |-
#           option 42 ip 192.168.1.1
#         subnet: 255.255.255.0
```

### Authors

- Peter Sprygada (@privateip)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
