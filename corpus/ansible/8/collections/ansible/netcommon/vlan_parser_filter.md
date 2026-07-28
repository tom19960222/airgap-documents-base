---
collection: ansible
version: "8"
title: "ansible.netcommon.vlan_parser filter – The vlan_parser filter plugin."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/vlan_parser_filter.html
fetched_at: 2026-07-28T01:04:56+00:00
---
# ansible.netcommon.vlan_parser filter – The vlan_parser filter plugin.

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
> To use it in a playbook, specify: `ansible.netcommon.vlan_parser`.

New in ansible.netcommon 1.0.0

- [Synopsis](vlan_parser_filter.md#synopsis)
- [Keyword parameters](vlan_parser_filter.md#keyword-parameters)
- [Notes](vlan_parser_filter.md#notes)
- [Examples](vlan_parser_filter.md#examples)

## [Synopsis](vlan_parser_filter.md#id1)

- The filter plugin converts a list of vlans to IOS like vlan configuration.
- Converts list to a list of range of numbers into multiple lists.
- `vlans_data | ansible.netcommon.vlan_parser(first_line_len = 20, other_line_len=20`)

## [Keyword parameters](vlan_parser_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.netcommon.vlan_parser(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **data**  list / elements=string / required | This option represents a list containing vlans. |
| **first_line_len**  integer | The first line of the list can be first_line_len characters long.  **Default:** `48` |
| **other_line_len**  integer | The subsequent list lines can be other_line_len characters.  **Default:** `44` |

## [Notes](vlan_parser_filter.md#id3)

> **Note:**
>
> - The filter plugin extends vlans when data provided in range or comma separated.

## [Examples](vlan_parser_filter.md#id4)

```yaml+jinja
# Using vlan_parser

- name: Setting host facts for vlan_parser filter plugin
  ansible.builtin.set_fact:
    vlans:
      [
        100,
        1688,
        3002,
        3003,
        3004,
        3005,
        3102,
        3103,
        3104,
        3105,
        3802,
        3900,
        3998,
        3999,
      ]

- name: Invoke vlan_parser filter plugin
  ansible.builtin.set_fact:
    vlans_ranges: "{{ vlans | ansible.netcommon.vlan_parser(first_line_len = 20, other_line_len=20) }}"

# Task Output
# -----------
#
# TASK [Setting host facts for vlan_parser filter plugin]
# ok: [host] => changed=false
#   ansible_facts:
#     vlans:
#     - 100
#     - 1688
#     - 3002
#     - 3003
#     - 3004
#     - 3005
#     - 3102
#     - 3103
#     - 3104
#     - 3105
#     - 3802
#     - 3900
#     - 3998
#     - 3999

# TASK [Invoke vlan_parser filter plugin]
# ok: [host] => changed=false
#   ansible_facts:
#     msg:
#     - 100,1688,3002-3005
#     - 3102-3105,3802,3900
#     - 3998,3999
```

### Authors

- Steve Dodd (@idahood)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
