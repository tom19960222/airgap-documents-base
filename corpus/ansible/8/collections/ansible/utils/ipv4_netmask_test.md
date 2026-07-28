---
collection: ansible
version: "8"
title: "ansible.utils.ipv4_netmask test – Test if an address is a valid netmask"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/ipv4_netmask_test.html
fetched_at: 2026-07-28T01:10:13+00:00
---
# ansible.utils.ipv4_netmask test – Test if an address is a valid netmask

> **Note:**
>
> This test plugin is part of the [ansible.utils collection](https://galaxy.ansible.com/ui/repo/published/ansible/utils/) (version 2.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.utils`.
>
> To use it in a playbook, specify: `ansible.utils.ipv4_netmask`.

New in ansible.utils 2.2.0

- [Synopsis](ipv4_netmask_test.md#synopsis)
- [Keyword parameters](ipv4_netmask_test.md#keyword-parameters)
- [Examples](ipv4_netmask_test.md#examples)
- [Return Value](ipv4_netmask_test.md#return-value)

## [Synopsis](ipv4_netmask_test.md#id1)

- This plugin checks if the provided ip address is a valid IPv4 netmask or not

## [Keyword parameters](ipv4_netmask_test.md#id2)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.utils.ipv4_netmask(key1=value1, key2=value2, ...)` and `input is not ansible.utils.ipv4_netmask(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **mask**  string / required | A string that represents the value against which the test is going to be performed  For example: `0.1.255.255` or `255.255.255.0` |

## [Examples](ipv4_netmask_test.md#id3)

```yaml+jinja
#### Simple examples

- name: Check if 255.255.255.0 is a netmask
  ansible.builtin.set_fact:
    data: "{{ '255.255.255.0' is ansible.utils.ipv4_netmask }}"

# TASK [Check if 255.255.255.0 is a netmask] *******************************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Check if 255.255.255.128 is a netmask
  ansible.builtin.set_fact:
    data: "{{ '255.255.255.128' is ansible.utils.ipv4_netmask }}"

# TASK [Check if 255.255.255.128 is a netmask] *****************************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Check if 255.255.255.127 is not a netmask
  ansible.builtin.set_fact:
    data: "{{ '255.255.255.127' is not ansible.utils.ipv4_netmask }}"

# TASK [Check if 255.255.255.127 is not a netmask] *************************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }
```

## [Return Value](ipv4_netmask_test.md#id4)

| Key | Description |
| --- | --- |
| **data**  string | If jinja test satisfies plugin expression `true`  If jinja test does not satisfy plugin expression `false`  **Returned:** success |

### Authors

- Priyam Sahoo (@priyamsahoo)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
