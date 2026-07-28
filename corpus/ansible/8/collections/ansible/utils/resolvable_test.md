---
collection: ansible
version: "8"
title: "ansible.utils.resolvable test – Test if an IP or name can be resolved via /etc/hosts or DNS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/resolvable_test.html
fetched_at: 2026-07-28T01:10:21+00:00
---
# ansible.utils.resolvable test – Test if an IP or name can be resolved via /etc/hosts or DNS

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
> To use it in a playbook, specify: `ansible.utils.resolvable`.

New in ansible.utils 2.2.0

- [Synopsis](resolvable_test.md#synopsis)
- [Keyword parameters](resolvable_test.md#keyword-parameters)
- [Examples](resolvable_test.md#examples)
- [Return Value](resolvable_test.md#return-value)

## [Synopsis](resolvable_test.md#id1)

- This plugin checks if the provided IP address of host name can be resolved using /etc/hosts or DNS

## [Keyword parameters](resolvable_test.md#id2)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.utils.resolvable(key1=value1, key2=value2, ...)` and `input is not ansible.utils.resolvable(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **host**  string / required | A string that represents the IP address or the host name  For example: `"docs.ansible.com"`, `127.0.0.1`, or `::1` |

## [Examples](resolvable_test.md#id3)

```yaml+jinja
#### Simple examples

- name: Check if docs.ansible.com is resolvable or not
  ansible.builtin.set_fact:
    data: "{{ 'docs.ansible.com' is ansible.utils.resolvable }}"

# TASK [Check if docs.ansible.com is resolvable or not] **********************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Set host name variables
  ansible.builtin.set_fact:
    good_name: www.google.com
    bad_name: foo.google.com

- name: Assert good_name's resolvability
  assert:
    that: "{{ 'www.google.com' is ansible.utils.resolvable }}"

- name: Assert bad_name's resolvability
  assert:
    that: "{{ 'foo.google.com' is not ansible.utils.resolvable }}"

# TASK [Assert good_name's resolvability] ************************************************
# ok: [localhost] => {
#     "changed": false,
#     "msg": "All assertions passed"
# }

# TASK [Assert bad_name's resolvability] *************************************************
# ok: [localhost] => {
#     "changed": false,
#     "msg": "All assertions passed"
# }

- name: Set ip variables
  ansible.builtin.set_fact:
    ipv4_localhost: "127.0.0.1"
    ipv6_localhost: "::1"

- name: Assert ipv4_localhost's resolvability
  assert:
    that: "{{ ipv4_localhost is ansible.utils.resolvable }}"

- name: Assert ipv6_localhost's resolvability
  assert:
    that: "{{ ipv6_localhost is ansible.utils.resolvable }}"

# TASK [Assert ipv4_localhost's resolvability] *******************************************
# ok: [localhost] => {
#     "changed": false,
#     "msg": "All assertions passed"
# }

# TASK [Assert ipv6_localhost's resolvability] *******************************************
# ok: [localhost] => {
#     "changed": false,
#     "msg": "All assertions passed"
# }
```

## [Return Value](resolvable_test.md#id4)

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
