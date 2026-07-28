---
collection: ansible
version: "8"
title: "ansible.utils.in_one_network test – Test if IP address belongs in any one of the networks in the list"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/in_one_network_test.html
fetched_at: 2026-07-28T01:10:09+00:00
---
# ansible.utils.in_one_network test – Test if IP address belongs in any one of the networks in the list

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
> To use it in a playbook, specify: `ansible.utils.in_one_network`.

New in ansible.utils 2.2.0

- [Synopsis](in_one_network_test.md#synopsis)
- [Keyword parameters](in_one_network_test.md#keyword-parameters)
- [Examples](in_one_network_test.md#examples)
- [Return Value](in_one_network_test.md#return-value)

## [Synopsis](in_one_network_test.md#id1)

- This plugin checks if the provided IP address belongs to the provided list network addresses

## [Keyword parameters](in_one_network_test.md#id2)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.utils.in_one_network(key1=value1, key2=value2, ...)` and `input is not ansible.utils.in_one_network(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **ip**  string / required | A string that represents an IP address  For example: `10.1.1.1` |
| **networks**  list / elements=string / required | A list of string and each string represents a network address in CIDR form  For example: `['10.0.0.0/8', '192.168.1.0/24']` |

## [Examples](in_one_network_test.md#id3)

```yaml+jinja
#### Simple examples

- name: Set network list
  ansible.builtin.set_fact:
    networks:
      - "10.0.0.0/8"
      - "192.168.1.0/24"

- name: Check if 10.1.1.1 is in the provided network list
  ansible.builtin.set_fact:
    data: "{{ '10.1.1.1' is ansible.utils.in_one_network networks }}"

# TASK [Check if 10.1.1.1 is in the provided network list] **********************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false

- name: Set network list
  ansible.builtin.set_fact:
    networks:
      - "10.0.0.0/8"
      - "10.1.1.0/24"

- name: Check if 10.1.1.1 is not in the provided network list
  ansible.builtin.set_fact:
    data: "{{ '10.1.1.1' is not ansible.utils.in_one_network networks }}"

# TASK [Check if 10.1.1.1 is in not the provided network list] ************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }
```

## [Return Value](in_one_network_test.md#id4)

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
