---
collection: ansible
version: "8"
title: "ansible.utils.param_list_compare filter – Generate the final param list combining/comparing base and provided parameters."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/param_list_compare_filter.html
fetched_at: 2026-07-28T01:09:58+00:00
---
# ansible.utils.param_list_compare filter – Generate the final param list combining/comparing base and provided parameters.

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
> To use it in a playbook, specify: `ansible.utils.param_list_compare`.

New in ansible.utils 2.4.0

- [Synopsis](param_list_compare_filter.md#synopsis)
- [Keyword parameters](param_list_compare_filter.md#keyword-parameters)
- [Examples](param_list_compare_filter.md#examples)
- [Return Value](param_list_compare_filter.md#return-value)

## [Synopsis](param_list_compare_filter.md#id1)

- Generate the final list of parameters after comparing with base list and provided/target list of params/bangs.

## [Keyword parameters](param_list_compare_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.param_list_compare(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **base**  list / elements=string | Specify the base list. |
| **target**  list / elements=string | Specify the target list. |

## [Examples](param_list_compare_filter.md#id3)

```yaml+jinja
- set_fact:
    base: ['1', '2', '3', '4', ' 5']

- set_fact:
    target: ['!all', '2', '4']

- name: Get final list of parameters
  register: result
  set_fact:
    final_params: "{{ base | param_list_compare(target) }}"

# TASK [Target list] **********************************************************
# ok: [localhost] => {
#     "msg": {
#         "actionable": [
#             "2",
#             "4"
#         ],
#         "unsupported": []
#     }
# }

- set_fact:
    base: ['1', '2', '3', '4', '5']

- name: Get final list of parameters
  register: result
  set_fact:
    final_params: "{{ base|param_list_compare(target=['2', '7', '8']) }}"

# TASK [Get final list of parameters] ********************************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "final_params": {
#             "actionable": [
#                 "2"
#             ],
#             "unsupported": [
#                 "7",
#                 "8"
#             ]
#         }
#     },
#     "changed": false
# }

# Network Specific Example
# -----------
- set_fact:
    ios_resources:
      - "acl_interfaces"
      - "acls"
      - "bgp_address_family"
      - "bgp_global"
      - "interfaces"
      - "l2_interfaces"
      - "l3_interfaces"
      - "lacp"
      - "lacp_interfaces"
      - "lag_interfaces"
      - "lldp_global"
      - "lldp_interfaces"
      - "logging_global"
      - "ospf_interfaces"
      - "ospfv2"
      - "ospfv3"
      - "prefix_lists"
      - "route_maps"
      - "static_routes"
      - "vlans"

- set_fact:
    target_resources:
      - '!all'
      - 'vlan'
      - 'bgp_global'

- name: Get final list of target resources/params
  register: result
  set_fact:
    network_resources: "{{ ios_resources|param_list_compare(target_resources) }}"

- name: Target list of network resources
  debug:
    msg: "{{ network_resources }}"

# TASK [Target list of network resources] *******************************************************************************************************************
# ok: [localhost] => {
#     "msg": {
#         "actionable": [
#             "bgp_global",
#             "vlans"
#         ],
#         "unsupported": []
#     }
# }

- name: Get final list of target resources/params
  register: result
  set_fact:
    network_resources: "{{ ios_resources|param_list_compare(target=['vla', 'ntp_global', 'logging_global']) }}"

- name: Target list of network resources
  debug:
    msg: "{{ network_resources }}"

# TASK [Target list of network resources] ************************************************
# ok: [localhost] => {
#     "msg": {
#         "actionable": [
#             "logging_global"
#         ],
#         "unsupported": [
#             "vla",
#             "ntp_global"
#         ]
#     }
# }
```

## [Return Value](param_list_compare_filter.md#id4)

| Key | Description |
| --- | --- |
| **actionable**  list / elements=string | list of combined params  **Returned:** success |
| **unsupported**  list / elements=string | list of unsupported params  **Returned:** success |

### Authors

- Rohit Thakur (@rohitthakur2590)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
