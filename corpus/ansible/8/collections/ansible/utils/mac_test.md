---
collection: ansible
version: "8"
title: "ansible.utils.mac test – Test if something appears to be a valid MAC address"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/mac_test.html
fetched_at: 2026-07-28T01:10:18+00:00
---
# ansible.utils.mac test – Test if something appears to be a valid MAC address

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
> To use it in a playbook, specify: `ansible.utils.mac`.

New in ansible.utils 2.2.0

- [Synopsis](mac_test.md#synopsis)
- [Keyword parameters](mac_test.md#keyword-parameters)
- [Examples](mac_test.md#examples)
- [Return Value](mac_test.md#return-value)

## [Synopsis](mac_test.md#id1)

- This plugin checks if the provided value is a valid MAC address that follows the industry level standards

## [Keyword parameters](mac_test.md#id2)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.utils.mac(key1=value1, key2=value2, ...)` and `input is not ansible.utils.mac(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **mac**  string / required | A string that represents the value against which the test is going to be performed  For example: `02:16:3e:e4:16:f3`, `02-16-3e-e4-16-f3`, `0216.3ee4.16f3`, or `02163ee416f3` |

## [Examples](mac_test.md#id3)

```yaml+jinja
- name: Check if 02:16:3e:e4:16:f3 is a valid MAC address
  ansible.builtin.set_fact:
    data: "{{ '02:16:3e:e4:16:f3' is ansible.utils.mac }}"

# TASK [Check if 02:16:3e:e4:16:f3 is a valid MAC address] ********************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Check if 02-16-3e-e4-16-f3 is a valid MAC address
  ansible.builtin.set_fact:
    data: "{{ '02-16-3e-e4-16-f3' is ansible.utils.mac }}"

# TASK [Check if 02-16-3e-e4-16-f3 is a valid MAC address] ********************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Check if 0216.3ee4.16f3 is a valid MAC address
  ansible.builtin.set_fact:
    data: "{{ '0216.3ee4.16f3' is ansible.utils.mac }}"

# TASK [Check if 0216.3ee4.16f3 is a valid MAC address] ***********************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Check if 02163ee416f3 is a valid MAC address
  ansible.builtin.set_fact:
    data: "{{ '02163ee416f3' is ansible.utils.mac }}"

# TASK [Check if 02163ee416f3 is a valid MAC address] *************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Check if helloworld is not a valid MAC address
  ansible.builtin.set_fact:
    data: "{{ 'helloworld' is not ansible.utils.mac }}"

# TASK [Check if helloworld is not a valid MAC address] ***********************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }
```

## [Return Value](mac_test.md#id4)

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
