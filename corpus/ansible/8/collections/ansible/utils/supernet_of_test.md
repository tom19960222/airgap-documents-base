---
collection: ansible
version: "8"
title: "ansible.utils.supernet_of test – Test if a network is a supernet of another network"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/supernet_of_test.html
fetched_at: 2026-07-28T01:10:23+00:00
---
# ansible.utils.supernet_of test – Test if a network is a supernet of another network

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
> To use it in a playbook, specify: `ansible.utils.supernet_of`.

New in ansible.utils 2.2.0

- [Synopsis](supernet_of_test.md#synopsis)
- [Keyword parameters](supernet_of_test.md#keyword-parameters)
- [Examples](supernet_of_test.md#examples)
- [Return Value](supernet_of_test.md#return-value)

## [Synopsis](supernet_of_test.md#id1)

- This plugin checks if the first network is a supernet of the second network amongst the provided network addresses

## [Keyword parameters](supernet_of_test.md#id2)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.utils.supernet_of(key1=value1, key2=value2, ...)` and `input is not ansible.utils.supernet_of(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **network_a**  string / required | A string that represents the first network address  For example: `10.1.1.0/24` |
| **network_b**  string / required | A string that represents the second network address  For example: `10.0.0.0/8` |

## [Examples](supernet_of_test.md#id3)

```yaml+jinja
- name: Check if 10.0.0.0/8 is a supernet of 10.1.1.0/24
  ansible.builtin.set_fact:
    data: "{{ '10.0.0.0/8' is ansible.utils.supernet_of '10.1.1.0/24' }}"

# TASK [Check if 10.0.0.0/8 is a supernet of 10.1.1.0/24] ************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Check if 10.0.0.0/8 is not a supernet of 192.168.1.0/24
  ansible.builtin.set_fact:
    data: "{{ '10.0.0.0/8' is not ansible.utils.supernet_of '192.168.1.0/24' }}"

# TASK [Check if 10.0.0.0/8 is not a supernet of 192.168.1.0/24] *****************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }
```

## [Return Value](supernet_of_test.md#id4)

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
