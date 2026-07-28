---
collection: ansible
version: "8"
title: "ansible.utils.loopback test – Test if an IP address is a loopback"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/loopback_test.html
fetched_at: 2026-07-28T01:10:17+00:00
---
# ansible.utils.loopback test – Test if an IP address is a loopback

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
> To use it in a playbook, specify: `ansible.utils.loopback`.

New in ansible.utils 2.2.0

- [Synopsis](loopback_test.md#synopsis)
- [Keyword parameters](loopback_test.md#keyword-parameters)
- [Examples](loopback_test.md#examples)
- [Return Value](loopback_test.md#return-value)

## [Synopsis](loopback_test.md#id1)

- This plugin checks if the provided value is a valid loopback IP address

## [Keyword parameters](loopback_test.md#id2)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.utils.loopback(key1=value1, key2=value2, ...)` and `input is not ansible.utils.loopback(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **ip**  string / required | A string that represents the value against which the test is going to be performed  For example: `127.0.0.1` or `2002::c0a8:6301:1` |

## [Examples](loopback_test.md#id3)

```yaml+jinja
- name: Check if 127.10.10.10 is a valid loopback address
  ansible.builtin.set_fact:
    data: "{{ '127.10.10.10' is ansible.utils.loopback }}"

# TASK [Check if 127.10.10.10 is a valid loopback address] *************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Check if 10.1.1.1 is not a valid loopback address
  ansible.builtin.set_fact:
    data: "{{ '10.1.1.1' is not ansible.utils.loopback }}"

# TASK [Check if 10.1.1.1 is not a valid loopback address] *************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Check if ::1 is a valid loopback address
  ansible.builtin.set_fact:
    data: "{{ '::1' is ansible.utils.loopback }}"

# TASK [Check if ::1 is a valid loopback address] **********************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }
```

## [Return Value](loopback_test.md#id4)

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
