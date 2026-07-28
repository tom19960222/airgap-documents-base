---
collection: ansible
version: "8"
title: "ansible.utils.remove_keys filter – Remove specific keys from a data recursively."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/remove_keys_filter.html
fetched_at: 2026-07-28T01:10:00+00:00
---
# ansible.utils.remove_keys filter – Remove specific keys from a data recursively.

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
> To use it in a playbook, specify: `ansible.utils.remove_keys`.

New in ansible.utils 2.5.0

- [Synopsis](remove_keys_filter.md#synopsis)
- [Keyword parameters](remove_keys_filter.md#keyword-parameters)
- [Examples](remove_keys_filter.md#examples)

## [Synopsis](remove_keys_filter.md#id1)

- This plugin removes specific keys from a provided data recursively.
- Matching parameter defaults to equals unless `matching_parameter` is explicitly mentioned.
- Using the parameters below- `data|ansible.utils.remove_keys(target([....]`))

## [Keyword parameters](remove_keys_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.remove_keys(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **data**  any / required | This option represents a list of dictionaries or a dictionary with any level of nesting data.  For example `config_data|ansible.utils.remove_keys(target([....]`)), in this case `config_data` represents this option. |
| **matching_parameter**  string | Specify the matching configuration of target keys and data attributes.  **Choices:**   - `"starts_with"` - `"ends_with"` - `"regex"` |
| **target**  list / elements=string / required | Specify the target keys to remove in list format. |

## [Examples](remove_keys_filter.md#id3)

```yaml+jinja
# example.yaml
# interfaces:
#   - name: eth0
#     enabled: true
#     duplex: auto
#     speed: auto
#     note:
#       - Connected green wire
#   - name: eth1
#     description: Configured by Ansible - Interface 1
#     mtu: 1500
#     speed: auto
#     duplex: auto
#     enabled: true
#     note:
#       - Connected blue wire
#       - Configured by Paul
#     vifs:
#     - vlan_id: 100
#       description: Eth1 - VIF 100
#       mtu: 400
#       enabled: true
#       comment: Needs reconfiguration
#     - vlan_id: 101
#       description: Eth1 - VIF 101
#       enabled: true
#   - name: eth2
#     description: Configured by Ansible - Interface 2 (ADMIN DOWN)
#     mtu: 600
#     enabled: false

# Playbook

- name: remove multiple keys from a provided data
  ansible.builtin.set_fact:
    data: '{{ interfaces }}'
- debug:
    msg: '{{ data|ansible.utils.remove_keys(target=[''note'', ''comment'']) }}'

# Output
# TASK [remove multiple keys from a provided data] ***************************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": [
#             {
#                 "duplex": "auto",
#                 "enabled": true,
#                 "name": "eth0",
#                 "note": [
#                     "Connected green wire"
#                 ],
#                 "speed": "auto"
#             },
#             {
#                 "description": "Configured by Ansible - Interface 1",
#                 "duplex": "auto",
#                 "enabled": true,
#                 "mtu": 1500,
#                 "name": "eth1",
#                 "note": [
#                     "Connected blue wire",
#                     "Configured by Paul"
#                 ],
#                 "speed": "auto",
#                 "vifs": [
#                     {
#                         "comment": "Needs reconfiguration",
#                         "description": "Eth1 - VIF 100",
#                         "enabled": true,
#                         "mtu": 400,
#                         "vlan_id": 100
#                     },
#                     {
#                         "description": "Eth1 - VIF 101",
#                         "enabled": true,
#                         "vlan_id": 101
#                     }
#                 ]
#             },
#             {
#                 "description": "Configured by Ansible - Interface 2 (ADMIN DOWN)",
#                 "enabled": false,
#                 "mtu": 600,
#                 "name": "eth2"
#             }
#         ]
#     },
#     "changed": false
# }
# Read vars_file 'example.yaml'

# TASK [debug] ********************************************
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
#   - name: eth0
#     enabled: true
#     duplex: auto
#     speed: auto
#     note:
#       - Connected green wire
#   - name: eth1
#     description: Configured by Ansible - Interface 1
#     mtu: 1500
#     speed: auto
#     duplex: auto
#     enabled: true
#     note:
#       - Connected blue wire
#       - Configured by Paul
#     vifs:
#     - vlan_id: 100
#       description: Eth1 - VIF 100
#       mtu: 400
#       enabled: true
#       comment: Needs reconfiguration
#     - vlan_id: 101
#       description: Eth1 - VIF 101
#       enabled: true
#   - name: eth2
#     description: Configured by Ansible - Interface 2 (ADMIN DOWN)
#     mtu: 600
#     enabled: false

# Playbook
- name: remove multiple keys from a provided data
  ansible.builtin.set_fact:
    data: '{{ interfaces }}'
- debug:
    msg: >-
      {{ data|ansible.utils.remove_keys(target=['^note$', '^comment'],
      matching_parameter= 'regex') }}

# Output
# TASK [remove multiple keys from a provided data] ***********************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": [
#             {
#                 "duplex": "auto",
#                 "enabled": true,
#                 "name": "eth0",
#                 "note": [
#                     "Connected green wire"
#                 ],
#                 "speed": "auto"
#             },
#             {
#                 "description": "Configured by Ansible - Interface 1",
#                 "duplex": "auto",
#                 "enabled": true,
#                 "mtu": 1500,
#                 "name": "eth1",
#                 "note": [
#                     "Connected blue wire",
#                     "Configured by Paul"
#                 ],
#                 "speed": "auto",
#                 "vifs": [
#                     {
#                         "comment": "Needs reconfiguration",
#                         "description": "Eth1 - VIF 100",
#                         "enabled": true,
#                         "mtu": 400,
#                         "vlan_id": 100
#                     },
#                     {
#                         "description": "Eth1 - VIF 101",
#                         "enabled": true,
#                         "vlan_id": 101
#                     }
#                 ]
#             },
#             {
#                 "description": "Configured by Ansible - Interface 2 (ADMIN DOWN)",
#                 "enabled": false,
#                 "mtu": 600,
#                 "name": "eth2"
#             }
#         ]
#     },
#     "changed": false
# }
# Read vars_file 'example.yaml'

# TASK [debug] *****************************************
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
