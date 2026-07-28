---
collection: ansible
version: "8"
title: "ansible.netcommon.vlan_expander filter – The vlan_expander filter plugin."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/vlan_expander_filter.html
fetched_at: 2026-07-28T01:09:22+00:00
---
# ansible.netcommon.vlan_expander filter – The vlan_expander filter plugin.

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
> To use it in a playbook, specify: `ansible.netcommon.vlan_expander`.

New in ansible.netcommon 2.3.0

- [Synopsis](vlan_expander_filter.md#synopsis)
- [Keyword parameters](vlan_expander_filter.md#keyword-parameters)
- [Notes](vlan_expander_filter.md#notes)
- [Examples](vlan_expander_filter.md#examples)

## [Synopsis](vlan_expander_filter.md#id1)

- Expand shorthand list of VLANs to list all VLANs. Inverse of vlan_parser
- Using the parameters below - `vlans_data | ansible.netcommon.vlan_expander`

## [Keyword parameters](vlan_expander_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.netcommon.vlan_expander(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **data**  string / required | This option represents a string containing the range of vlans. |

## [Notes](vlan_expander_filter.md#id3)

> **Note:**
>
> - The filter plugin extends vlans when data provided in range or comma separated.

## [Examples](vlan_expander_filter.md#id4)

```yaml+jinja
# Using vlan_expander

- name: Setting host facts for vlan_expander filter plugin
  ansible.builtin.set_fact:
    vlan_ranges: "1,10-12,15,20-22"

- name: Invoke vlan_expander filter plugin
  ansible.builtin.set_fact:
    extended_vlans: "{{ vlan_ranges | ansible.netcommon.vlan_expander }}"

# Task Output
# -----------
#
# TASK [Setting host facts for vlan_expander filter plugin]
# ok: [host] => changed=false
#   ansible_facts:
#     vlan_ranges: 1,10-12,15,20-22

# TASK [Invoke vlan_expander filter plugin]
# ok: [host] => changed=false
#   ansible_facts:
#     extended_vlans:
#     - 1
#     - 10
#     - 11
#     - 12
#     - 15
#     - 20
#     - 21
#     - 22
```

### Authors

- Akira Yokochi (@akira6592)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
