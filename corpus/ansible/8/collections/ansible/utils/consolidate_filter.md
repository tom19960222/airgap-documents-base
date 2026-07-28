---
collection: ansible
version: "8"
title: "ansible.utils.consolidate filter – Consolidate facts together on common attributes."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/consolidate_filter.html
fetched_at: 2026-07-28T01:09:43+00:00
---
# ansible.utils.consolidate filter – Consolidate facts together on common attributes.

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
> To use it in a playbook, specify: `ansible.utils.consolidate`.

New in ansible.utils 2.6.0

- [Synopsis](consolidate_filter.md#synopsis)
- [Keyword parameters](consolidate_filter.md#keyword-parameters)
- [Examples](consolidate_filter.md#examples)

## [Synopsis](consolidate_filter.md#id1)

- This plugin presents collective structured data including all supplied facts grouping on common attributes mentioned.
- All other boolean parameter defaults to False unless parameters is explicitly mentioned.
- Using the parameters below- `data_sources|ansible.utils.consolidate(fail_missing_match_key=False`))

## [Keyword parameters](consolidate_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.consolidate(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **data_sources**  list / elements=dictionary / required | This option represents a list of dictionaries to perform the operation on.  For example `facts_source|ansible.utils.consolidate(fail_missing_match_key=False`)), in this case `facts_source` represents this option. |
| **data**  any / required | Specify facts data that gets consolidated. |
| **match_key**  string / required | Specify key to match on. |
| **name**  string / required | Specify the name with which the result set be created. |
| **fail_duplicate**  boolean | Fail if the match key’s value exists more than once in a given data set.  **Choices:**   - `false` - `true` ← (default) |
| **fail_missing_match_key**  boolean | Fail if match_key is not found in a specific data set.  **Choices:**   - `false` - `true` ← (default) |
| **fail_missing_match_value**  boolean | Fail if the match key’s value is not found in every data source.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](consolidate_filter.md#id3)

```yaml+jinja
# Consolidated filter plugin example
# ----------------------------------

# play.yml
- name: Define some test data
  ansible.builtin.set_fact:
    values:
      - name: a
        value: 1
      - name: b
        value: 2
      - name: c
        value: 3
    colors:
      - name: a
        color: red
      - name: b
        color: green
      - name: c
        color: blue
- name: Define some test data
  ansible.builtin.set_fact:
    base_data:
      - data: '{{ values }}'
        match_key: name
        name: values
      - data: '{{ colors }}'
        match_key: name
        name: colors
- name: Consolidate the data source using the name key
  ansible.builtin.set_fact:
    consolidated: '{{ data_sources|ansible.utils.consolidate }}'
    vars:
      sizes:
        - name: a
          size: small
        - name: b
          size: medium
        - name: c
          size: large
      additional_data_source:
        - data: '{{ sizes }}'
          match_key: name
          name: sizes
      data_sources: '{{ base_data + additional_data_source }}'

# Output

# ok: [localhost] => {
#     "ansible_facts": {
#         "consolidated": {
#             "a": {
#                 "colors": {
#                     "color": "red",
#                     "name": "a"
#                 },
#                 "sizes": {
#                     "name": "a",
#                     "size": "small"
#                 },
#                 "values": {
#                     "name": "a",
#                     "value": 1
#                 }
#             },
#             "b": {
#                 "colors": {
#                     "color": "green",
#                     "name": "b"
#                 },
#                 "sizes": {
#                     "name": "b",
#                     "size": "medium"
#                 },
#                 "values": {
#                     "name": "b",
#                     "value": 2
#                 }
#             },
#             "c": {
#                 "colors": {
#                     "color": "blue",
#                     "name": "c"
#                 },
#                 "sizes": {
#                     "name": "c",
#                     "size": "large"
#                 },
#                 "values": {
#                     "name": "c",
#                     "value": 3
#                 }
#             }
#         }
#     },
#     "changed": false
# }

- name: Consolidate the data source using different keys
  ansible.builtin.set_fact: null
  consolidated: '{{ data_sources|ansible.utils.consolidate }}'
  vars:
    sizes:
      - title: a
        size: small
      - title: b
        size: medium
      - title: c
        size: large
    additional_data_source:
      - data: '{{ sizes }}'
        match_key: title
        name: sizes
    data_sources: '{{ base_data + additional_data_source }}'

# Output

# ok: [localhost] => {
#     "ansible_facts": {
#         "consolidated": {
#             "a": {
#                 "colors": {
#                     "color": "red",
#                     "name": "a"
#                 },
#                 "sizes": {
#                     "size": "small",
#                     "title": "a"
#                 },
#                 "values": {
#                     "name": "a",
#                     "value": 1
#                 }
#             },
#             "b": {
#                 "colors": {
#                     "color": "green",
#                     "name": "b"
#                 },
#                 "sizes": {
#                     "size": "medium",
#                     "title": "b"
#                 },
#                 "values": {
#                     "name": "b",
#                     "value": 2
#                 }
#             },
#             "c": {
#                 "colors": {
#                     "color": "blue",
#                     "name": "c"
#                 },
#                 "sizes": {
#                     "size": "large",
#                     "title": "c"
#                 },
#                 "values": {
#                     "name": "c",
#                     "value": 3
#                 }
#             }
#         }
#     },
#     "changed": false
# }

- name: Consolidate the data source using the name key (fail_missing_match_key)
  ansible.builtin.set_fact: null
  consolidated: '{{ data_sources|ansible.utils.consolidate(fail_missing_match_key=True) }}'
  ignore_errors: true
  vars:
    sizes:
      - size: small
      - size: medium
      - size: large
    additional_data_source:
      - data: '{{ sizes }}'
        match_key: name
        name: sizes
    data_sources: '{{ base_data + additional_data_source }}'

# Output

# fatal: [localhost]: FAILED! => {
#     "msg": "Error when using plugin 'consolidate': 'fail_missing_match_key'
#                   reported missing match key 'name' in data source 3 in list entry 1,
#                            missing match key 'name' in data source 3 in list entry 2,
#                            missing match key 'name' in data source 3 in list entry 3"
# }

- name: Consolidate the data source using the name key (fail_missing_match_value)
  ansible.builtin.set_fact:
    consolidated: "{{ data_sources|ansible.utils.consolidate(fail_missing_match_value=True) }}"
  ignore_errors: true
  vars:
    sizes:
      - name: a
        size: small
      - name: b
        size: medium
    additional_data_source:
      - data: "{{ sizes }}"
        match_key: name
        name: sizes
    data_sources: "{{ base_data + additional_data_source }}"

# fatal: [localhost]: FAILED! => {
#     "msg": "Error when using plugin 'consolidate': 'fail_missing_match_value'
#                   reported missing match value c in data source 3"
# }

- name: Consolidate the data source using the name key (fail_duplicate)
  ansible.builtin.set_fact:
    consolidated: "{{ data_sources|ansible.utils.consolidate(fail_duplicate=True) }}"
  ignore_errors: true
  vars:
    sizes:
      - name: a
        size: small
      - name: a
        size: small
    additional_data_source:
      - data: "{{ sizes }}"
        match_key: name
        name: sizes
    data_sources: "{{ base_data + additional_data_source }}"

# fatal: [localhost]: FAILED! => {
#     "msg": "Error when using plugin 'consolidate': 'fail_duplicate'
#                   reported duplicate values in data source 3"
# }

# facts.yml

# interfaces:
#   - name: GigabitEthernet0/0
#     enabled: true
#     duplex: auto
#     speed: auto
#     note:
#       - Connected green wire
#   - name: GigabitEthernet0/1
#     description: Configured by Ansible - Interface 1
#     mtu: 1500
#     speed: auto
#     duplex: auto
#     enabled: true
#     note:
#       - Connected blue wire
#       - Configured by Paul
#     vifs:
#       - vlan_id: 100
#         description: Eth1 - VIF 100
#         mtu: 400
#         enabled: true
#         comment: Needs reconfiguration
#       - vlan_id: 101
#         description: Eth1 - VIF 101
#         enabled: true
#   - name: GigabitEthernet0/2
#     description: Configured by Ansible - Interface 2 (ADMIN DOWN)
#     mtu: 600
#     enabled: false
# l2_interfaces:
#   - name: GigabitEthernet0/0
#   - mode: access
#     name: GigabitEthernet0/1
#     trunk:
#       allowed_vlans:
#         - "11"
#         - "12"
#         - "59"
#         - "67"
#         - "75"
#         - "77"
#         - "81"
#         - "100"
#         - 400-408
#         - 411-413
#         - "415"
#         - "418"
#         - "982"
#         - "986"
#         - "988"
#         - "993"
#   - mode: trunk
#     name: GigabitEthernet0/2
#     trunk:
#       allowed_vlans:
#         - "11"
#         - "12"
#         - "59"
#         - "67"
#         - "75"
#         - "77"
#         - "81"
#         - "100"
#         - 400-408
#         - 411-413
#         - "415"
#         - "418"
#         - "982"
#         - "986"
#         - "988"
#         - "993"
#       encapsulation: dot1q
# l3_interfaces:
#   - ipv4:
#       - address: 192.168.0.2/24
#     name: GigabitEthernet0/0
#   - name: GigabitEthernet0/1
#   - name: GigabitEthernet0/2
#   - name: Loopback888
#   - name: Loopback999

# Playbook
- name: Build the facts collection
  set_fact:
    data_sources:
      - data: '{{ interfaces }}'
        match_key: name
        name: interfaces
      - data: '{{ l2_interfaces }}'
        match_key: name
        name: l2_interfaces
      - data: '{{ l3_interfaces }}'
        match_key: name
        name: l3_interfaces
- name: Combine all the facts based on match_keys
  set_fact:
    combined: >-
      {{ data_sources|ansible.utils.consolidate(fail_missing_match_value=False)
      }}

# Output
# ok: [localhost] => {
#     "ansible_facts": {
#         "data_sources": [
#             {
#                 "data": [
#                     {
#                         "duplex": "auto",
#                         "enabled": true,
#                         "name": "GigabitEthernet0/0",
#                         "note": [
#                             "Connected green wire"
#                         ],
#                         "speed": "auto"
#                     },
#                     {
#                         "description": "Configured by Ansible - Interface 1",
#                         "duplex": "auto",
#                         "enabled": true,
#                         "mtu": 1500,
#                         "name": "GigabitEthernet0/1",
#                         "note": [
#                             "Connected blue wire",
#                             "Configured by Paul"
#                         ],
#                         "speed": "auto",
#                         "vifs": [
#                             {
#                                 "comment": "Needs reconfiguration",
#                                 "description": "Eth1 - VIF 100",
#                                 "enabled": true,
#                                 "mtu": 400,
#                                 "vlan_id": 100
#                             },
#                             {
#                                 "description": "Eth1 - VIF 101",
#                                 "enabled": true,
#                                 "vlan_id": 101
#                             }
#                         ]
#                     },
#                     {
#                         "description": "Configured by Ansible - Interface 2 (ADMIN DOWN)",
#                         "enabled": false,
#                         "mtu": 600,
#                         "name": "GigabitEthernet0/2"
#                     }
#                 ],
#                 "match_key": "name",
#                 "name": "interfaces"
#             },
#             {
#                 "data": [
#                     {
#                         "name": "GigabitEthernet0/0"
#                     },
#                     {
#                         "mode": "access",
#                         "name": "GigabitEthernet0/1",
#                         "trunk": {
#                             "allowed_vlans": [
#                                 "11",
#                                 "12",
#                                 "59",
#                                 "67",
#                                 "75",
#                                 "77",
#                                 "81",
#                                 "100",
#                                 "400-408",
#                                 "411-413",
#                                 "415",
#                                 "418",
#                                 "982",
#                                 "986",
#                                 "988",
#                                 "993"
#                             ]
#                         }
#                     },
#                     {
#                         "mode": "trunk",
#                         "name": "GigabitEthernet0/2",
#                         "trunk": {
#                             "allowed_vlans": [
#                                 "11",
#                                 "12",
#                                 "59",
#                                 "67",
#                                 "75",
#                                 "77",
#                                 "81",
#                                 "100",
#                                 "400-408",
#                                 "411-413",
#                                 "415",
#                                 "418",
#                                 "982",
#                                 "986",
#                                 "988",
#                                 "993"
#                             ],
#                             "encapsulation": "dot1q"
#                         }
#                     }
#                 ],
#                 "match_key": "name",
#                 "name": "l2_interfaces"
#             },
#             {
#                 "data": [
#                     {
#                         "ipv4": [
#                             {
#                                 "address": "192.168.0.2/24"
#                             }
#                         ],
#                         "name": "GigabitEthernet0/0"
#                     },
#                     {
#                         "name": "GigabitEthernet0/1"
#                     },
#                     {
#                         "name": "GigabitEthernet0/2"
#                     },
#                     {
#                         "name": "Loopback888"
#                     },
#                     {
#                         "name": "Loopback999"
#                     }
#                 ],
#                 "match_key": "name",
#                 "name": "l3_interfaces"
#             }
#         ]
#     },
#     "changed": false
# }
# Read vars_file 'facts.yml'

# TASK [Combine all the facts based on match_keys]
# ok: [localhost] => {
#     "ansible_facts": {
#         "combined": {
#             "GigabitEthernet0/0": {
#                 "interfaces": {
#                     "duplex": "auto",
#                     "enabled": true,
#                     "name": "GigabitEthernet0/0",
#                     "note": [
#                         "Connected green wire"
#                     ],
#                     "speed": "auto"
#                 },
#                 "l2_interfaces": {
#                     "name": "GigabitEthernet0/0"
#                 },
#                 "l3_interfaces": {
#                     "ipv4": [
#                         {
#                             "address": "192.168.0.2/24"
#                         }
#                     ],
#                     "name": "GigabitEthernet0/0"
#                 }
#             },
#             "GigabitEthernet0/1": {
#                 "interfaces": {
#                     "description": "Configured by Ansible - Interface 1",
#                     "duplex": "auto",
#                     "enabled": true,
#                     "mtu": 1500,
#                     "name": "GigabitEthernet0/1",
#                     "note": [
#                         "Connected blue wire",
#                         "Configured by Paul"
#                     ],
#                     "speed": "auto",
#                     "vifs": [
#                         {
#                             "comment": "Needs reconfiguration",
#                             "description": "Eth1 - VIF 100",
#                             "enabled": true,
#                             "mtu": 400,
#                             "vlan_id": 100
#                         },
#                         {
#                             "description": "Eth1 - VIF 101",
#                             "enabled": true,
#                             "vlan_id": 101
#                         }
#                     ]
#                 },
#                 "l2_interfaces": {
#                     "mode": "access",
#                     "name": "GigabitEthernet0/1",
#                     "trunk": {
#                         "allowed_vlans": [
#                             "11",
#                             "12",
#                             "59",
#                             "67",
#                             "75",
#                             "77",
#                             "81",
#                             "100",
#                             "400-408",
#                             "411-413",
#                             "415",
#                             "418",
#                             "982",
#                             "986",
#                             "988",
#                             "993"
#                         ]
#                     }
#                 },
#                 "l3_interfaces": {
#                     "name": "GigabitEthernet0/1"
#                 }
#             },
#             "GigabitEthernet0/2": {
#                 "interfaces": {
#                     "description": "Configured by Ansible - Interface 2 (ADMIN DOWN)",
#                     "enabled": false,
#                     "mtu": 600,
#                     "name": "GigabitEthernet0/2"
#                 },
#                 "l2_interfaces": {
#                     "mode": "trunk",
#                     "name": "GigabitEthernet0/2",
#                     "trunk": {
#                         "allowed_vlans": [
#                             "11",
#                             "12",
#                             "59",
#                             "67",
#                             "75",
#                             "77",
#                             "81",
#                             "100",
#                             "400-408",
#                             "411-413",
#                             "415",
#                             "418",
#                             "982",
#                             "986",
#                             "988",
#                             "993"
#                         ],
#                         "encapsulation": "dot1q"
#                     }
#                 },
#                 "l3_interfaces": {
#                     "name": "GigabitEthernet0/2"
#                 }
#             },
#             "Loopback888": {
#                 "interfaces": {},
#                 "l2_interfaces": {},
#                 "l3_interfaces": {
#                     "name": "Loopback888"
#                 }
#             },
#             "Loopback999": {
#                 "interfaces": {},
#                 "l2_interfaces": {},
#                 "l3_interfaces": {
#                     "name": "Loopback999"
#                 }
#             }
#         }
#     },
#     "changed": false
# }

# Failing on missing match values
# -------------------------------

# facts.yaml
# interfaces:
#   - name: GigabitEthernet0/0
#     enabled: true
#     duplex: auto
#     speed: auto
#     note:
#       - Connected green wire
#   - name: GigabitEthernet0/1
#     description: Configured by Ansible - Interface 1
#     mtu: 1500
#     speed: auto
#     duplex: auto
#     enabled: true
#     note:
#       - Connected blue wire
#       - Configured by Paul
#     vifs:
#       - vlan_id: 100
#         description: Eth1 - VIF 100
#         mtu: 400
#         enabled: true
#         comment: Needs reconfiguration
#       - vlan_id: 101
#         description: Eth1 - VIF 101
#         enabled: true
#   - name: GigabitEthernet0/2
#     description: Configured by Ansible - Interface 2 (ADMIN DOWN)
#     mtu: 600
#     enabled: false
# l2_interfaces:
#   - name: GigabitEthernet0/0
#   - mode: access
#     name: GigabitEthernet0/1
#     trunk:
#       allowed_vlans:
#         - "11"
#         - "12"
#         - "59"
#         - "67"
#         - "75"
#         - "77"
#         - "81"
#         - "100"
#         - 400-408
#         - 411-413
#         - "415"
#         - "418"
#         - "982"
#         - "986"
#         - "988"
#         - "993"
#   - mode: trunk
#     name: GigabitEthernet0/2
#     trunk:
#       allowed_vlans:
#         - "11"
#         - "12"
#         - "59"
#         - "67"
#         - "75"
#         - "77"
#         - "81"
#         - "100"
#         - 400-408
#         - 411-413
#         - "415"
#         - "418"
#         - "982"
#         - "986"
#         - "988"
#         - "993"
#       encapsulation: dot1q
# l3_interfaces:
#   - ipv4:
#       - address: 192.168.0.2/24
#     name: GigabitEthernet0/0
#   - name: GigabitEthernet0/1
#   - name: GigabitEthernet0/2
#   - name: Loopback888
#   - name: Loopback999

# Playbook
- name: Build the facts collection
  set_fact:
    data_sources:
      - data: '{{ interfaces }}'
        match_key: name
        name: interfaces
      - data: '{{ l2_interfaces }}'
        match_key: name
        name: l2_interfaces
      - data: '{{ l3_interfaces }}'
        match_key: name
        name: l3_interfaces
- name: Combine all the facts based on match_keys
  set_fact:
    combined: >-
      {{ data_sources|ansible.utils.consolidate(fail_missing_match_value=True)
      }}

# Output
# ok: [localhost] => {
#     "ansible_facts": {
#         "data_sources": [
#             {
#                 "data": [
#                     {
#                         "duplex": "auto",
#                         "enabled": true,
#                         "name": "GigabitEthernet0/0",
#                         "note": [
#                             "Connected green wire"
#                         ],
#                         "speed": "auto"
#                     },
#                     {
#                         "description": "Configured by Ansible - Interface 1",
#                         "duplex": "auto",
#                         "enabled": true,
#                         "mtu": 1500,
#                         "name": "GigabitEthernet0/1",
#                         "note": [
#                             "Connected blue wire",
#                             "Configured by Paul"
#                         ],
#                         "speed": "auto",
#                         "vifs": [
#                             {
#                                 "comment": "Needs reconfiguration",
#                                 "description": "Eth1 - VIF 100",
#                                 "enabled": true,
#                                 "mtu": 400,
#                                 "vlan_id": 100
#                             },
#                             {
#                                 "description": "Eth1 - VIF 101",
#                                 "enabled": true,
#                                 "vlan_id": 101
#                             }
#                         ]
#                     },
#                     {
#                         "description": "Configured by Ansible - Interface 2 (ADMIN DOWN)",
#                         "enabled": false,
#                         "mtu": 600,
#                         "name": "GigabitEthernet0/2"
#                     }
#                 ],
#                 "match_key": "name",
#                 "name": "interfaces"
#             },
#             {
#                 "data": [
#                     {
#                         "name": "GigabitEthernet0/0"
#                     },
#                     {
#                         "mode": "access",
#                         "name": "GigabitEthernet0/1",
#                         "trunk": {
#                             "allowed_vlans": [
#                                 "11",
#                                 "12",
#                                 "59",
#                                 "67",
#                                 "75",
#                                 "77",
#                                 "81",
#                                 "100",
#                                 "400-408",
#                                 "411-413",
#                                 "415",
#                                 "418",
#                                 "982",
#                                 "986",
#                                 "988",
#                                 "993"
#                             ]
#                         }
#                     },
#                     {
#                         "mode": "trunk",
#                         "name": "GigabitEthernet0/2",
#                         "trunk": {
#                             "allowed_vlans": [
#                                 "11",
#                                 "12",
#                                 "59",
#                                 "67",
#                                 "75",
#                                 "77",
#                                 "81",
#                                 "100",
#                                 "400-408",
#                                 "411-413",
#                                 "415",
#                                 "418",
#                                 "982",
#                                 "986",
#                                 "988",
#                                 "993"
#                             ],
#                             "encapsulation": "dot1q"
#                         }
#                     }
#                 ],
#                 "match_key": "name",
#                 "name": "l2_interfaces"
#             },
#             {
#                 "data": [
#                     {
#                         "ipv4": [
#                             {
#                                 "address": "192.168.0.2/24"
#                             }
#                         ],
#                         "name": "GigabitEthernet0/0"
#                     },
#                     {
#                         "name": "GigabitEthernet0/1"
#                     },
#                     {
#                         "name": "GigabitEthernet0/2"
#                     },
#                     {
#                         "name": "Loopback888"
#                     },
#                     {
#                         "name": "Loopback999"
#                     }
#                 ],
#                 "match_key": "name",
#                 "name": "l3_interfaces"
#             }
#         ]
#     },
#     "changed": false
# }
# Read vars_file 'facts.yml'

# TASK [Combine all the facts based on match_keys]
# fatal: [localhost]: FAILED! => {
#     "msg": "Error when using plugin 'consolidate': 'fail_missing_match_value' reported Missing match value Loopback999,
#     Loopback888 in data source 0, Missing match value Loopback999, Loopback888 in data source 1"
# }

# Failing on missing match keys
# -----------------------------

# facts.yaml
# interfaces:
#   - name: GigabitEthernet0/0
#     enabled: true
#     duplex: auto
#     speed: auto
#     note:
#       - Connected green wire
#   - name: GigabitEthernet0/1
#     description: Configured by Ansible - Interface 1
#     mtu: 1500
#     speed: auto
#     duplex: auto
#     enabled: true
#     note:
#       - Connected blue wire
#       - Configured by Paul
#     vifs:
#       - vlan_id: 100
#         description: Eth1 - VIF 100
#         mtu: 400
#         enabled: true
#         comment: Needs reconfiguration
#       - vlan_id: 101
#         description: Eth1 - VIF 101
#         enabled: true
#   - name: GigabitEthernet0/2
#     description: Configured by Ansible - Interface 2 (ADMIN DOWN)
#     mtu: 600
#     enabled: false
# l2_interfaces:
#   - name: GigabitEthernet0/0
#   - mode: access
#     name: GigabitEthernet0/1
#     trunk:
#       allowed_vlans:
#         - "11"
#         - "12"
#         - "59"
#         - "67"
#         - "75"
#         - "77"
#         - "81"
#         - "100"
#         - 400-408
#         - 411-413
#         - "415"
#         - "418"
#         - "982"
#         - "986"
#         - "988"
#         - "993"
#   - mode: trunk
#     name: GigabitEthernet0/2
#     trunk:
#       allowed_vlans:
#         - "11"
#         - "12"
#         - "59"
#         - "67"
#         - "75"
#         - "77"
#         - "81"
#         - "100"
#         - 400-408
#         - 411-413
#         - "415"
#         - "418"
#         - "982"
#         - "986"
#         - "988"
#         - "993"
#       encapsulation: dot1q
# l3_interfaces:
#   - ipv4:
#       - address: 192.168.0.2/24
#     inft_name: GigabitEthernet0/0
#   - inft_name: GigabitEthernet0/1
#   - inft_name: GigabitEthernet0/2
#   - inft_name: Loopback888
#   - inft_name: Loopback999

# Playbook
- name: Build the facts collection
  set_fact:
    data_sources:
      - data: '{{ interfaces }}'
        match_key: name
        name: interfaces
      - data: '{{ l2_interfaces }}'
        match_key: name
        name: l2_interfaces
      - data: '{{ l3_interfaces }}'
        match_key: name
        name: l3_interfaces
- name: Combine all the facts based on match_keys
  set_fact:
    combined: '{{ data_sources|ansible.utils.consolidate(fail_missing_match_key=True) }}'

# Output
# ok: [localhost] => {
#     "ansible_facts": {
#         "data_sources": [
#             {
#                 "data": [
#                     {
#                         "duplex": "auto",
#                         "enabled": true,
#                         "name": "GigabitEthernet0/0",
#                         "note": [
#                             "Connected green wire"
#                         ],
#                         "speed": "auto"
#                     },
#                     {
#                         "description": "Configured by Ansible - Interface 1",
#                         "duplex": "auto",
#                         "enabled": true,
#                         "mtu": 1500,
#                         "name": "GigabitEthernet0/1",
#                         "note": [
#                             "Connected blue wire",
#                             "Configured by Paul"
#                         ],
#                         "speed": "auto",
#                         "vifs": [
#                             {
#                                 "comment": "Needs reconfiguration",
#                                 "description": "Eth1 - VIF 100",
#                                 "enabled": true,
#                                 "mtu": 400,
#                                 "vlan_id": 100
#                             },
#                             {
#                                 "description": "Eth1 - VIF 101",
#                                 "enabled": true,
#                                 "vlan_id": 101
#                             }
#                         ]
#                     },
#                     {
#                         "description": "Configured by Ansible - Interface 2 (ADMIN DOWN)",
#                         "enabled": false,
#                         "mtu": 600,
#                         "name": "GigabitEthernet0/2"
#                     }
#                 ],
#                 "match_key": "name",
#                 "name": "interfaces"
#             },
#             {
#                 "data": [
#                     {
#                         "name": "GigabitEthernet0/0"
#                     },
#                     {
#                         "mode": "access",
#                         "name": "GigabitEthernet0/1",
#                         "trunk": {
#                             "allowed_vlans": [
#                                 "11",
#                                 "12",
#                                 "59",
#                                 "67",
#                                 "75",
#                                 "77",
#                                 "81",
#                                 "100",
#                                 "400-408",
#                                 "411-413",
#                                 "415",
#                                 "418",
#                                 "982",
#                                 "986",
#                                 "988",
#                                 "993"
#                             ]
#                         }
#                     },
#                     {
#                         "mode": "trunk",
#                         "name": "GigabitEthernet0/2",
#                         "trunk": {
#                             "allowed_vlans": [
#                                 "11",
#                                 "12",
#                                 "59",
#                                 "67",
#                                 "75",
#                                 "77",
#                                 "81",
#                                 "100",
#                                 "400-408",
#                                 "411-413",
#                                 "415",
#                                 "418",
#                                 "982",
#                                 "986",
#                                 "988",
#                                 "993"
#                             ],
#                             "encapsulation": "dot1q"
#                         }
#                     }
#                 ],
#                 "match_key": "name",
#                 "name": "l2_interfaces"
#             },
#             {
#                 "data": [
#                     {
#                         "inft_name": "GigabitEthernet0/0",
#                         "ipv4": [
#                             {
#                                 "address": "192.168.0.2/24"
#                             }
#                         ]
#                     },
#                     {
#                         "inft_name": "GigabitEthernet0/1"
#                     },
#                     {
#                         "inft_name": "GigabitEthernet0/2"
#                     },
#                     {
#                         "inft_name": "Loopback888"
#                     },
#                     {
#                         "inft_name": "Loopback999"
#                     }
#                 ],
#                 "match_key": "name",
#                 "name": "l3_interfaces"
#             }
#         ]
#     },
#     "changed": false
# }
# Read vars_file 'facts.yml'

# TASK [Combine all the facts based on match_keys]
# fatal: [localhost]: FAILED! => {
#     "msg": "Error when using plugin 'consolidate': 'fail_missing_match_key' reported Missing match
#     key 'name' in data source 2 in list entry 0, Missing match key 'name' in data
#     source 2 in list entry 1, Missing match key 'name' in data source 2 in list
#     entry 2, Missing match key 'name' in data source 2 in list entry 3, Missing
#     match key 'name' in data source 2 in list entry 4"
# }

# Failing on duplicate values in facts
# ------------------------------------

# facts.yaml
# interfaces:
#   - name: GigabitEthernet0/0
#     enabled: true
#     duplex: auto
#     speed: auto
#     note:
#       - Connected green wire
#   - name: GigabitEthernet0/1
#     description: Configured by Ansible - Interface 1
#     mtu: 1500
#     speed: auto
#     duplex: auto
#     enabled: true
#     note:
#       - Connected blue wire
#       - Configured by Paul
#     vifs:
#       - vlan_id: 100
#         description: Eth1 - VIF 100
#         mtu: 400
#         enabled: true
#         comment: Needs reconfiguration
#       - vlan_id: 101
#         description: Eth1 - VIF 101
#         enabled: true
#   - name: GigabitEthernet0/2
#     description: Configured by Ansible - Interface 2 (ADMIN DOWN)
#     mtu: 600
#     enabled: false
# l2_interfaces:
#   - name: GigabitEthernet0/0
#   - name: GigabitEthernet0/0
#   - mode: access
#     name: GigabitEthernet0/1
#     trunk:
#       allowed_vlans:
#         - "11"
#         - "12"
#         - "59"
#         - "67"
#         - "75"
#         - "77"
#         - "81"
#         - "100"
#         - 400-408
#         - 411-413
#         - "415"
#         - "418"
#         - "982"
#         - "986"
#         - "988"
#         - "993"
#   - mode: trunk
#     name: GigabitEthernet0/2
#     trunk:
#       allowed_vlans:
#         - "11"
#         - "12"
#         - "59"
#         - "67"
#         - "75"
#         - "77"
#         - "81"
#         - "100"
#         - 400-408
#         - 411-413
#         - "415"
#         - "418"
#         - "982"
#         - "986"
#         - "988"
#         - "993"
#       encapsulation: dot1q
# l3_interfaces:
#   - ipv4:
#       - address: 192.168.0.2/24
#     name: GigabitEthernet0/0
#   - name: GigabitEthernet0/1
#   - name: GigabitEthernet0/2
#   - name: Loopback888
#   - name: Loopback999

# Playbook
- name: Build the facts collection
  set_fact:
    data_sources:
      - data: '{{ interfaces }}'
        match_key: name
        name: interfaces
      - data: '{{ l2_interfaces }}'
        match_key: name
        name: l2_interfaces
      - data: '{{ l3_interfaces }}'
        match_key: name
        name: l3_interfaces
- name: Combine all the facts based on match_keys
  set_fact:
    combined: '{{ data_sources|ansible.utils.consolidate(fail_duplicate=True) }}'

# Output
# ok: [localhost] => {
#     "ansible_facts": {
#         "data_sources": [
#             {
#                 "data": [
#                     {
#                         "duplex": "auto",
#                         "enabled": true,
#                         "name": "GigabitEthernet0/0",
#                         "note": [
#                             "Connected green wire"
#                         ],
#                         "speed": "auto"
#                     },
#                     {
#                         "description": "Configured by Ansible - Interface 1",
#                         "duplex": "auto",
#                         "enabled": true,
#                         "mtu": 1500,
#                         "name": "GigabitEthernet0/1",
#                         "note": [
#                             "Connected blue wire",
#                             "Configured by Paul"
#                         ],
#                         "speed": "auto",
#                         "vifs": [
#                             {
#                                 "comment": "Needs reconfiguration",
#                                 "description": "Eth1 - VIF 100",
#                                 "enabled": true,
#                                 "mtu": 400,
#                                 "vlan_id": 100
#                             },
#                             {
#                                 "description": "Eth1 - VIF 101",
#                                 "enabled": true,
#                                 "vlan_id": 101
#                             }
#                         ]
#                     },
#                     {
#                         "description": "Configured by Ansible - Interface 2 (ADMIN DOWN)",
#                         "enabled": false,
#                         "mtu": 600,
#                         "name": "GigabitEthernet0/2"
#                     }
#                 ],
#                 "match_key": "name",
#                 "name": "interfaces"
#             },
#             {
#                 "data": [
#                     {
#                         "name": "GigabitEthernet0/0"
#                     },
#                     {
#                         "name": "GigabitEthernet0/0"
#                     },
#                     {
#                         "mode": "access",
#                         "name": "GigabitEthernet0/1",
#                         "trunk": {
#                             "allowed_vlans": [
#                                 "11",
#                                 "12",
#                                 "59",
#                                 "67",
#                                 "75",
#                                 "77",
#                                 "81",
#                                 "100",
#                                 "400-408",
#                                 "411-413",
#                                 "415",
#                                 "418",
#                                 "982",
#                                 "986",
#                                 "988",
#                                 "993"
#                             ]
#                         }
#                     },
#                     {
#                         "mode": "trunk",
#                         "name": "GigabitEthernet0/2",
#                         "trunk": {
#                             "allowed_vlans": [
#                                 "11",
#                                 "12",
#                                 "59",
#                                 "67",
#                                 "75",
#                                 "77",
#                                 "81",
#                                 "100",
#                                 "400-408",
#                                 "411-413",
#                                 "415",
#                                 "418",
#                                 "982",
#                                 "986",
#                                 "988",
#                                 "993"
#                             ],
#                             "encapsulation": "dot1q"
#                         }
#                     }
#                 ],
#                 "match_key": "name",
#                 "name": "l2_interfaces"
#             },
#             {
#                 "data": [
#                     {
#                         "ipv4": [
#                             {
#                                 "address": "192.168.0.2/24"
#                             }
#                         ],
#                         "name": "GigabitEthernet0/0"
#                     },
#                     {
#                         "name": "GigabitEthernet0/1"
#                     },
#                     {
#                         "name": "GigabitEthernet0/2"
#                     },
#                     {
#                         "name": "Loopback888"
#                     },
#                     {
#                         "name": "Loopback999"
#                     }
#                 ],
#                 "match_key": "name",
#                 "name": "l3_interfaces"
#             }
#         ]
#     },
#     "changed": false
# }
# Read vars_file 'facts.yml'

# TASK [Combine all the facts based on match_keys]
# fatal: [localhost]: FAILED! => {
#     "msg": "Error when using plugin 'consolidate': 'fail_duplicate' reported Duplicate values in data source 1"
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
