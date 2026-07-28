---
collection: ansible
version: "8"
title: "ansible.netcommon.parse_cli_textfsm filter – parse_cli_textfsm filter plugin."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/parse_cli_textfsm_filter.html
fetched_at: 2026-07-28T01:09:20+00:00
---
# ansible.netcommon.parse_cli_textfsm filter – parse_cli_textfsm filter plugin.

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
> To use it in a playbook, specify: `ansible.netcommon.parse_cli_textfsm`.

New in ansible.netcommon 1.0.0

- [Synopsis](parse_cli_textfsm_filter.md#synopsis)
- [Keyword parameters](parse_cli_textfsm_filter.md#keyword-parameters)
- [Notes](parse_cli_textfsm_filter.md#notes)
- [Examples](parse_cli_textfsm_filter.md#examples)

## [Synopsis](parse_cli_textfsm_filter.md#id1)

- The network filters also support parsing the output of a CLI command using the TextFSM library. To parse the CLI output with TextFSM use this filter.
- Using the parameters below - `data | ansible.netcommon.parse_cli_textfsm(template.yml`)

## [Keyword parameters](parse_cli_textfsm_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.netcommon.parse_cli_textfsm(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **template**  string | The template to compare it with.  For example `data | ansible.netcommon.parse_cli_textfsm(template.yml`), in this case `data` represents this option. |
| **value**  any / required | This source data on which parse_cli_textfsm invokes. |

## [Notes](parse_cli_textfsm_filter.md#id3)

> **Note:**
>
> - Use of the TextFSM filter requires the TextFSM library to be installed.

## [Examples](parse_cli_textfsm_filter.md#id4)

```yaml+jinja
# Using parse_cli_textfsm

- name: "Fetch command output"
  cisco.ios.ios_command:
    commands:
      - show lldp neighbors
  register: lldp_output

- name: "Invoke parse_cli_textfsm"
  ansible.builtin.set_fact:
    device_neighbors: "{{ lldp_output.stdout[0] | parse_cli_textfsm('~/ntc-templates/templates/cisco_ios_show_lldp_neighbors.textfsm') }}"

- name: "Debug"
  ansible.builtindebug:
    msg: "{{ device_neighbors }}"

# Task Output
# -----------
#
# TASK [Fetch command output]
# ok: [rtr-2]

# TASK [Invoke parse_cli_textfsm]
# ok: [rtr-1]

# TASK [Debug]
# ok: [rtr-1] => {
#     "msg": [
#         {
#             "CAPABILITIES": "R",
#             "LOCAL_INTERFACE": "Gi0/0",
#             "NEIGHBOR": "rtr-3",
#             "NEIGHBOR_INTERFACE": "Gi0/0"
#         },
#         {
#             "CAPABILITIES": "R",
#             "LOCAL_INTERFACE": "Gi0/1",
#             "NEIGHBOR": "rtr-1",
#             "NEIGHBOR_INTERFACE": "Gi0/1"
#         }
#     ]
# }
```

### Authors

- Peter Sprygada (@privateip)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
