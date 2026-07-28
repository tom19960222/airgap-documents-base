---
collection: ansible
version: "8"
title: "ansible.utils.replace_keys filter – Replaces specific keys with their after value from a data recursively."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/replace_keys_filter.html
fetched_at: 2026-07-28T01:10:01+00:00
---
# ansible.utils.replace_keys filter – Replaces specific keys with their after value from a data recursively.

> **Note:**
>
> This filter plugin is part of the [ansible.utils collection](https://galaxy.ansible.com/ui/repo/published/ansible/utils/) (version 2.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.utils`.
>
> To use it in a playbook, specify: `ansible.utils.replace_keys`.

New in ansible.utils 2.5.0

- [Synopsis](replace_keys_filter.md#synopsis)
- [Keyword parameters](replace_keys_filter.md#keyword-parameters)
- [Examples](replace_keys_filter.md#examples)

## [Synopsis](replace_keys_filter.md#id1)

- This plugin replaces specific keys with their after value from a data recursively.
- Matching parameter defaults to equals unless `matching_parameter` is explicitly mentioned.
- Using the parameters below- `data|ansible.utils.replace_keys(target([....]`))

## [Keyword parameters](replace_keys_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.replace_keys(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **data**  any / required | This option represents a list of dictionaries or a dictionary with any level of nesting data.  For example `config_data|ansible.utils.replace_keys(target([....]`)), in this case `config_data` represents this option. |
| **matching_parameter**  string | Specify the matching configuration of target keys and data attributes.  **Choices:**   - `"starts_with"` - `"ends_with"` - `"regex"` |
| **target**  list / elements=dictionary / required | Specify the target keys to replace in list of dictionaries format containing before and after key value. |
| **after**  string | after attribute key [change to] |
| **before**  string | before attribute key [to change] |

## [Examples](replace_keys_filter.md#id3)

```yaml+jinja
# example.yaml
# interfaces:
#   - interface_name: eth0
#     enabled: true
#     duplex: auto
#     speed: auto
#   - interface_name: eth1
#     description: Configured by Ansible - Interface 1
#     mtu: 1500
#     speed: auto
#     duplex: auto
#     is_enabled: true
#     vifs:
#     - vlan_id: 100
#       description: Eth1 - VIF 100
#       mtu: 400
#       is_enabled: true
#     - vlan_id: 101
#       description: Eth1 - VIF 101
#       is_enabled: true
#   - interface_name: eth2
#     description: Configured by Ansible - Interface 2 (ADMIN DOWN)
#     mtu: 600
#     is_enabled: false

# Playbook
- name: replace keys with specified keys dict/list to dict
  ansible.builtin.set_fact:
    data: '{{ interfaces }}'
- debug:
    msg: >-
      {{ data|ansible.utils.replace_keys(target=[{'before':'interface_name',
      'after':'name'}, {'before':'is_enabled', 'after':'enabled'}]) }}

# Output
# TASK [replace keys with specified keys dict/list to dict] *************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": [
#             {
#                 "duplex": "auto",
#                 "enabled": true,
#                 "interface_name": "eth0",
#                 "speed": "auto"
#             },
#             {
#                 "description": "Configured by Ansible - Interface 1",
#                 "duplex": "auto",
#                 "interface_name": "eth1",
#                 "is_enabled": true,
#                 "mtu": 1500,
#                 "speed": "auto",
#                 "vifs": [
#                     {
#                         "description": "Eth1 - VIF 100",
#                         "is_enabled": true,
#                         "mtu": 400,
#                         "vlan_id": 100
#                     },
#                     {
#                         "description": "Eth1 - VIF 101",
#                         "is_enabled": true,
#                         "vlan_id": 101
#                     }
#                 ]
#             },
#             {
#                 "description": "Configured by Ansible - Interface 2 (ADMIN DOWN)",
#                 "interface_name": "eth2",
#                 "is_enabled": false,
#                 "mtu": 600
#             }
#         ]
#     },
#     "changed": false
# }

# TASK [debug] **********************************************************************
# ok: [localhost] => {
#     "msg": [
#         {
#             "duplex": "auto",
#             "enabled": true,
#             "name": "eth0",
#             "speed": "auto"
#         },
#         {
#             "description": "Configured by Ansible - Interface 1",
#             "duplex": "auto",
#             "enabled": true,
#             "mtu": 1500,
#             "name": "eth1",
#             "speed": "auto",
#             "vifs": [
#                 {
#                     "description": "Eth1 - VIF 100",
#                     "enabled": true,
#                     "mtu": 400,
#                     "vlan_id": 100
#                 },
#                 {
#                     "description": "Eth1 - VIF 101",
#                     "enabled": true,
#                     "vlan_id": 101
#                 }
#             ]
#         },
#         {
#             "description": "Configured by Ansible - Interface 2 (ADMIN DOWN)",
#             "enabled": false,
#             "mtu": 600,
#             "name": "eth2"
#         }
#     ]
# }

# example.yaml
# interfaces:
#   - interface_name: eth0
#     enabled: true
#     duplex: auto
#     speed: auto
#   - interface_name: eth1
#     description: Configured by Ansible - Interface 1
#     mtu: 1500
#     speed: auto
#     duplex: auto
#     is_enabled: true
#     vifs:
#     - vlan_id: 100
#       description: Eth1 - VIF 100
#       mtu: 400
#       is_enabled: true
#     - vlan_id: 101
#       description: Eth1 - VIF 101
#       is_enabled: true
#   - interface_name: eth2
#     description: Configured by Ansible - Interface 2 (ADMIN DOWN)
#     mtu: 600
#     is_enabled: false

# Playbook
- name: replace keys with specified keys dict/list to dict
  ansible.builtin.set_fact:
    data: '{{ interfaces }}'
- debug:
    msg: >-
      {{ data|ansible.utils.replace_keys(target=[{'before':'name',
      'after':'name'}, {'before':'enabled', 'after':'enabled'}],
      matching_parameter= 'ends_with') }}

# Output
# TASK [replace keys with specified keys dict/list to dict] *********************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": [
#             {
#                 "duplex": "auto",
#                 "enabled": true,
#                 "interface_name": "eth0",
#                 "speed": "auto"
#             },
#             {
#                 "description": "Configured by Ansible - Interface 1",
#                 "duplex": "auto",
#                 "interface_name": "eth1",
#                 "is_enabled": true,
#                 "mtu": 1500,
#                 "speed": "auto",
#                 "vifs": [
#                     {
#                         "description": "Eth1 - VIF 100",
#                         "is_enabled": true,
#                         "mtu": 400,
#                         "vlan_id": 100
#                     },
#                     {
#                         "description": "Eth1 - VIF 101",
#                         "is_enabled": true,
#                         "vlan_id": 101
#                     }
#                 ]
#             },
#             {
#                 "description": "Configured by Ansible - Interface 2 (ADMIN DOWN)",
#                 "interface_name": "eth2",
#                 "is_enabled": false,
#                 "mtu": 600
#             }
#         ]
#     },
#     "changed": false
# }

# TASK [debug] ***************************************************************************
# ok: [localhost] => {
#     "msg": [
#         {
#             "duplex": "auto",
#             "enabled": true,
#             "name": "eth0",
#             "speed": "auto"
#         },
#         {
#             "description": "Configured by Ansible - Interface 1",
#             "duplex": "auto",
#             "enabled": true,
#             "mtu": 1500,
#             "name": "eth1",
#             "speed": "auto",
#             "vifs": [
#                 {
#                     "description": "Eth1 - VIF 100",
#                     "enabled": true,
#                     "mtu": 400,
#                     "vlan_id": 100
#                 },
#                 {
#                     "description": "Eth1 - VIF 101",
#                     "enabled": true,
#                     "vlan_id": 101
#                 }
#             ]
#         },
#         {
#             "description": "Configured by Ansible - Interface 2 (ADMIN DOWN)",
#             "enabled": false,
#             "mtu": 600,
#             "name": "eth2"
#         }
#     ]
# }
```

### Authors

- Sagar Paul (@KB-perByte)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
