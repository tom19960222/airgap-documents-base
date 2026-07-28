---
collection: ansible
version: "8"
title: "ansible.utils.ip test – Test if something in an IP address or network"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/ip_test.html
fetched_at: 2026-07-28T01:10:10+00:00
---
# ansible.utils.ip test – Test if something in an IP address or network

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
> To use it in a playbook, specify: `ansible.utils.ip`.

New in ansible.utils 2.2.0

- [Synopsis](ip_test.md#synopsis)
- [Keyword parameters](ip_test.md#keyword-parameters)
- [Examples](ip_test.md#examples)
- [Return Value](ip_test.md#return-value)

## [Synopsis](ip_test.md#id1)

- This plugin checks if the provided value is a valid host or network IP address

## [Keyword parameters](ip_test.md#id2)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.utils.ip(key1=value1, key2=value2, ...)` and `input is not ansible.utils.ip(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **ip**  string / required | A string that represents the value against which the test is going to be performed  For example: `10.1.1.1`, `2001:db8:a::123`, or `"hello-world"` |

## [Examples](ip_test.md#id3)

```yaml+jinja
#### Simple examples

- name: Check if 10.1.1.1 is a valid IP address
  ansible.builtin.set_fact:
    data: "{{ '10.1.1.1' is ansible.utils.ip }}"

# TASK [Check if 10.1.1.1 is a valid IP address] *****************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Check if 2001:db8:a::123 is a valid IP address
  ansible.builtin.set_fact:
    data: "{{ '2001:db8:a::123' is ansible.utils.ip }}"

# TASK [Check if 2001:db8:a::123 is a valid IP address] **********************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Check if "hello-world" is not a valid IP address
  ansible.builtin.set_fact:
    data: "{{ 'hello-world' is not ansible.utils.ip }}"

# TASK [Check if "hello-world" is not a valid IP address] ********************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Check if 300.1.1.1 is a valid IP address
  ansible.builtin.set_fact:
    data: "{{ '300.1.1.1' is ansible.utils.ip }}"

# TASK [Check if 300.1.1.1 is a valid IP address] ****************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": false
#     },
#     "changed": false
# }

- name: Check if 10.0.0.0/8 is a valid IP address
  ansible.builtin.set_fact:
    data: "{{ '10.0.0.0/8' is ansible.utils.ip }}"

# TASK [Check if 10.0.0.0/8 is a valid IP address] ***************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }
```

## [Return Value](ip_test.md#id4)

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
