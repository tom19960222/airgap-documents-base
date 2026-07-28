---
collection: ansible
version: "8"
title: "ansible.utils.multicast test – Test for a multicast IP address"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/multicast_test.html
fetched_at: 2026-07-28T01:10:19+00:00
---
# ansible.utils.multicast test – Test for a multicast IP address

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
> To use it in a playbook, specify: `ansible.utils.multicast`.

New in ansible.utils 2.2.0

- [Synopsis](multicast_test.md#synopsis)
- [Keyword parameters](multicast_test.md#keyword-parameters)
- [Examples](multicast_test.md#examples)
- [Return Value](multicast_test.md#return-value)

## [Synopsis](multicast_test.md#id1)

- This plugin checks if the provided value is a valid multicast IP address

## [Keyword parameters](multicast_test.md#id2)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.utils.multicast(key1=value1, key2=value2, ...)` and `input is not ansible.utils.multicast(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **ip**  string / required | A string that represents the value against which the test is going to be performed  For example: `224.0.0.1` or `127.0.0.1` |

## [Examples](multicast_test.md#id3)

```yaml+jinja
- name: Check if 224.0.0.1 is a valid multicast IP address
  ansible.builtin.set_fact:
    data: "{{ '224.0.0.1' is ansible.utils.multicast }}"

# TASK [Check if 224.0.0.1 is a valid multicast IP address] **********************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Check if ff02::1 is a valid multicast IP address
  ansible.builtin.set_fact:
    data: "{{ 'ff02::1' is ansible.utils.multicast }}"

# TASK [Check if ff02::1 is a valid multicast IP address] ***************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Check if 127.0.0.1 is not a valid multicast IP address
  ansible.builtin.set_fact:
    data: "{{ '127.0.0.1' is not ansible.utils.multicast }}"

# TASK [Check if 127.0.0.1 is not a valid multicast IP address] *********************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Check if helloworld is not a valid multicast IP address
  ansible.builtin.set_fact:
    data: "{{ 'helloworld' is not ansible.utils.multicast }}"

# TASK [Check if helloworld is not a valid multicast IP address] ********************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }
```

## [Return Value](multicast_test.md#id4)

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
