---
collection: ansible
version: "8"
title: "ansible.utils.unspecified test – Test for an unspecified IP address"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/unspecified_test.html
fetched_at: 2026-07-28T01:10:23+00:00
---
# ansible.utils.unspecified test – Test for an unspecified IP address

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
> To use it in a playbook, specify: `ansible.utils.unspecified`.

New in ansible.utils 2.2.0

- [Synopsis](unspecified_test.md#synopsis)
- [Keyword parameters](unspecified_test.md#keyword-parameters)
- [Examples](unspecified_test.md#examples)
- [Return Value](unspecified_test.md#return-value)

## [Synopsis](unspecified_test.md#id1)

- This plugin checks if the provided value is an unspecified IP address

## [Keyword parameters](unspecified_test.md#id2)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.utils.unspecified(key1=value1, key2=value2, ...)` and `input is not ansible.utils.unspecified(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **ip**  string / required | A string that represents the value against which the test is going to be performed  For example: `0.0.0.0`, `0:0:0:0:0:0:0:0`, `::`, or `::1` |

## [Examples](unspecified_test.md#id3)

```yaml+jinja
#### Simple examples

- name: Check if 0.0.0.0 is an unspecified IP address
  ansible.builtin.set_fact:
    data: "{{ '0.0.0.0' is ansible.utils.unspecified }}"

# TASK [Check if 0.0.0.0 is an unspecified IP address] ***************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Check if 0:0:0:0:0:0:0:0 is an unspecified IP address
  ansible.builtin.set_fact:
    data: "{{ '0:0:0:0:0:0:0:0' is ansible.utils.unspecified }}"

# TASK [Check if 0:0:0:0:0:0:0:0 is an unspecified IP address] *******************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Check if "::" is an unspecified IP address
  ansible.builtin.set_fact:
    data: "{{ '::' is ansible.utils.unspecified }}"

# TASK [Check if "::" is an unspecified IP address] ******************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Check if ::1 is not an unspecified IP address
  ansible.builtin.set_fact:
    data: "{{ '::1' is not ansible.utils.unspecified }}"

# TASK [Check if ::1 is not an unspecified IP address] ***************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }
```

## [Return Value](unspecified_test.md#id4)

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
