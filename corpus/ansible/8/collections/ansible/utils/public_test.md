---
collection: ansible
version: "8"
title: "ansible.utils.public test – Test if an IP address is public"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/public_test.html
fetched_at: 2026-07-28T01:10:20+00:00
---
# ansible.utils.public test – Test if an IP address is public

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
> To use it in a playbook, specify: `ansible.utils.public`.

New in ansible.utils 2.2.0

- [Synopsis](public_test.md#synopsis)
- [Keyword parameters](public_test.md#keyword-parameters)
- [Examples](public_test.md#examples)
- [Return Value](public_test.md#return-value)

## [Synopsis](public_test.md#id1)

- This plugin checks if the provided value is a public IP address

## [Keyword parameters](public_test.md#id2)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.utils.public(key1=value1, key2=value2, ...)` and `input is not ansible.utils.public(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **ip**  string / required | A string that represents the value against which the test is going to be performed  For example: `8.8.8.8`, `10.1.1.1`, or `192.168.1.250` |

## [Examples](public_test.md#id3)

```yaml+jinja
- name: Check if 8.8.8.8 is a public IP address
  ansible.builtin.set_fact:
    data: "{{ '8.8.8.8' is ansible.utils.public }}"

# TASK [Check if 8.8.8.8 is a public IP address] *********************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Check if 10.1.1.1 is not a public IP address
  ansible.builtin.set_fact:
    data: "{{ '10.1.1.1' is not ansible.utils.public }}"

# TASK [Check if 10.1.1.1 is not a public IP address] ******************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }
```

## [Return Value](public_test.md#id4)

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
