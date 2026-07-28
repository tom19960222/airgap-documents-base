---
collection: ansible
version: "8"
title: "ansible.utils.reserved test – Test for a reserved IP address"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/reserved_test.html
fetched_at: 2026-07-28T01:10:21+00:00
---
# ansible.utils.reserved test – Test for a reserved IP address

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
> To use it in a playbook, specify: `ansible.utils.reserved`.

New in ansible.utils 2.2.0

- [Synopsis](reserved_test.md#synopsis)
- [Keyword parameters](reserved_test.md#keyword-parameters)
- [Examples](reserved_test.md#examples)
- [Return Value](reserved_test.md#return-value)

## [Synopsis](reserved_test.md#id1)

- This plugin checks if the provided value is a reserved IP address

## [Keyword parameters](reserved_test.md#id2)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.utils.reserved(key1=value1, key2=value2, ...)` and `input is not ansible.utils.reserved(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **ip**  string / required | A string that represents the value against which the test is going to be performed  For example: `253.0.0.1` or `128.146.1.7` |

## [Examples](reserved_test.md#id3)

```yaml+jinja
- name: Check if 253.0.0.1 is a reserved IP address
  ansible.builtin.set_fact:
    data: "{{ '253.0.0.1' is ansible.utils.reserved }}"

# TASK [Check if 253.0.0.1 is a reserved IP address] *****************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Check if 128.146.1.7 is not a reserved IP address
  ansible.builtin.set_fact:
    data: "{{ '128.146.1.7' is not ansible.utils.reserved }}"

# TASK [Check if 128.146.1.7 is not a reserved IP address] ***********************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }
```

## [Return Value](reserved_test.md#id4)

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
