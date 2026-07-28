---
collection: ansible
version: "8"
title: "ansible.utils.subnet_of test – Test if a network is a subnet of another network"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/subnet_of_test.html
fetched_at: 2026-07-28T01:10:22+00:00
---
# ansible.utils.subnet_of test – Test if a network is a subnet of another network

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
> To use it in a playbook, specify: `ansible.utils.subnet_of`.

New in ansible.utils 2.2.0

- [Synopsis](subnet_of_test.md#synopsis)
- [Keyword parameters](subnet_of_test.md#keyword-parameters)
- [Examples](subnet_of_test.md#examples)
- [Return Value](subnet_of_test.md#return-value)

## [Synopsis](subnet_of_test.md#id1)

- This plugin checks if the first network is a subnet of the second network amongst the provided network addresses

## [Keyword parameters](subnet_of_test.md#id2)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.utils.subnet_of(key1=value1, key2=value2, ...)` and `input is not ansible.utils.subnet_of(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **network_a**  string / required | A string that represents the first network address  For example: `10.1.1.0/24` |
| **network_b**  string / required | A string that represents the second network address  For example: `10.0.0.0/8` |

## [Examples](subnet_of_test.md#id3)

```yaml+jinja
- name: Check if 10.1.1.0/24 is a subnet of 10.0.0.0/8
  ansible.builtin.set_fact:
    data: "{{ '10.1.1.0/24' is ansible.utils.subnet_of '10.0.0.0/8' }}"

# TASK [Check if 10.1.1.0/24 is a subnet of 10.0.0.0/8] **************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Check if 192.168.1.0/24 is not a subnet of 10.0.0.0/8
  ansible.builtin.set_fact:
    data: "{{ '192.168.1.0/24' is not ansible.utils.subnet_of '10.0.0.0/8' }}"

# TASK [Check if 192.168.1.0/24 is not a subnet of 10.0.0.0/8] *******************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }
```

## [Return Value](subnet_of_test.md#id4)

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
