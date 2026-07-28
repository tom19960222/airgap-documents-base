---
collection: ansible
version: "8"
title: "ansible.utils.cidr_merge filter – This filter can be used to merge subnets or individual addresses."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/cidr_merge_filter.html
fetched_at: 2026-07-28T01:09:43+00:00
---
# ansible.utils.cidr_merge filter – This filter can be used to merge subnets or individual addresses.

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
> To use it in a playbook, specify: `ansible.utils.cidr_merge`.

New in ansible.utils 2.5.0

- [Synopsis](cidr_merge_filter.md#synopsis)
- [Keyword parameters](cidr_merge_filter.md#keyword-parameters)
- [Examples](cidr_merge_filter.md#examples)
- [Return Value](cidr_merge_filter.md#return-value)

## [Synopsis](cidr_merge_filter.md#id1)

- This filter can be used to merge subnets or individual addresses into their minimal representation, collapsing
- overlapping subnets and merging adjacent ones wherever possible.

## [Keyword parameters](cidr_merge_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.cidr_merge(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **action**  string | Action to be performed.example merge,span  **Default:** `"merge"` |
| **value**  list / elements=string / required | list of subnets or individual address to be merged |

## [Examples](cidr_merge_filter.md#id3)

```yaml+jinja
#### examples
- name: cidr_merge with merge action
  ansible.builtin.set_fact:
    value:
      - 192.168.0.0/17
      - 192.168.128.0/17
      - 192.168.128.1
- debug:
    msg: '{{ value|ansible.utils.cidr_merge }}'

# TASK [cidr_merge with merge action] **********************************************************************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "value": [
#             "192.168.0.0/17",
#             "192.168.128.0/17",
#             "192.168.128.1"
#         ]
#     },
#     "changed": false
# }
# TASK [debug] *********************************************************************************************************
# ok: [loalhost] => {
#     "msg": [
#         "192.168.0.0/16"
#     ]
# }

- name: Cidr_merge with span.
  ansible.builtin.set_fact:
    value:
      - 192.168.1.1
      - 192.168.1.2
      - 192.168.1.3
      - 192.168.1.4
- debug:
    msg: '{{ value|ansible.utils.cidr_merge(''span'') }}'

# TASK [Cidr_merge with span.] ********************************************************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "value": [
#             "192.168.1.1",
#             "192.168.1.2",
#             "192.168.1.3",
#             "192.168.1.4"
#         ]
#     },
#     "changed": false
# }
#
# TASK [debug] ************************************************************************************
# ok: [localhost] => {
#     "msg": "192.168.1.0/29"
# }
```

## [Return Value](cidr_merge_filter.md#id4)

| Key | Description |
| --- | --- |
| **data**  any | Returns a minified list of subnets or a single subnet that spans all of the inputs.  **Returned:** success |

### Authors

- Ashwini Mhatre (@amhatre)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
